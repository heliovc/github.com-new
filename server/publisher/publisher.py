#!/usr/bin/env python3
"""Robô publicador dos canais dark (roda no servidor, sem o Mac).

Comandos:
  run       git pull → acha publish.json → publica no Studio o que estiver pendente → grava status no repo
  metrics   coleta métricas de todos os canais (Studio) → server-data/metrics/AAAA-MM-DD.json no repo
  check     testa login + troca de canal em todos os canais (screenshots em LOG_DIR)
  plan      mostra o que seria feito agora, sem abrir o navegador
  test-upload --key K   publica um item como PRIVADO (teste do fluxo)
  test-post related|comment ...   roda o vínculo Short→longo ou o comentário fixado num vídeo (teste)

Config por variáveis de ambiente (arquivo /etc/canal-publisher.env):
  REPO_DIR, PROFILE_DIR, STATE_DIR, LOG_DIR, GRACE_MINUTES, NOTIFY_URL, GIT_PUSH (1/0)
"""
from __future__ import annotations

import argparse
import fcntl
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import manifest as mf  # noqa: E402

REPO = Path(os.environ.get("REPO_DIR", "/opt/canal-publisher/repo"))
PROFILE = Path(os.environ.get("PROFILE_DIR", "/opt/canal-publisher/profile"))
STATE_DIR = Path(os.environ.get("STATE_DIR", "/opt/canal-publisher/state"))
LOG_DIR = Path(os.environ.get("LOG_DIR", "/opt/canal-publisher/logs"))
GRACE = timedelta(minutes=int(os.environ.get("GRACE_MINUTES", "90")))
NOTIFY_URL = os.environ.get("NOTIFY_URL", "")
GIT_PUSH = os.environ.get("GIT_PUSH", "1") == "1"
DATA_DIR_NAME = "server-data"

log = logging.getLogger("publisher")


# ----------------------------------------------------------------- infra
def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler(LOG_DIR / "publisher.log")],
    )


def single_instance(wait_minutes: int = 0):
    """Um navegador por vez (o perfil do Chrome não pode abrir 2x).
    run: se já tem outra execução, sai. metrics/check: espera até wait_minutes."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    fh = open(STATE_DIR / "run.lock", "w")
    end = time.time() + wait_minutes * 60
    while True:
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fh
        except BlockingIOError:
            if time.time() >= end:
                log.info("outra execução em andamento — saindo")
                sys.exit(0)
            time.sleep(20)


def notify(msg: str):
    log.warning("NOTIFY: %s", msg)
    if not NOTIFY_URL:
        return
    try:
        req = urllib.request.Request(NOTIFY_URL, data=msg.encode("utf-8"), method="POST",
                                     headers={"Title": "Canal Dark - robo", "Tags": "robot"})
        urllib.request.urlopen(req, timeout=15).read()
    except Exception as e:  # noqa: BLE001
        log.error("falha ao notificar: %s", e)


def git(*args, check=True) -> str:
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def git_pull():
    git("fetch", "--depth=1", "origin", "main")
    git("reset", "--hard", "origin/main")  # o servidor nunca edita nada fora de server-data/ sem commitar logo


def git_push_data(message: str):
    if not GIT_PUSH:
        return
    for attempt in range(3):
        try:
            git("add", DATA_DIR_NAME)
            if not git("status", "--porcelain", DATA_DIR_NAME):
                return
            git("-c", "user.name=canal-publisher", "-c", "user.email=publisher@localhost", "commit", "-m", message)
            git("push", "origin", "HEAD:main")
            return
        except RuntimeError as e:
            log.warning("push falhou (%s), tentando rebase: %s", attempt + 1, e)
            git("fetch", "--depth=1", "origin", "main", check=False)
            git("rebase", "origin/main", check=False)
            time.sleep(3)
    notify("não consegui fazer push do status no GitHub (3 tentativas)")


# ----------------------------------------------------------------- state
def state_file() -> Path:
    return STATE_DIR / "state.json"


def load_state() -> dict:
    p = state_file()
    return json.loads(p.read_text()) if p.exists() else {}


def save_state(state: dict):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = state_file().with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1))
    tmp.replace(state_file())
    # cópia no repo para as rotinas do Claude lerem
    data = REPO / DATA_DIR_NAME
    data.mkdir(exist_ok=True)
    (data / "published.json").write_text(json.dumps(state, ensure_ascii=False, indent=1))


def write_heartbeat(extra: dict):
    data = REPO / DATA_DIR_NAME
    data.mkdir(exist_ok=True)
    hb = {"last_run": mf.now_sp().isoformat(), **extra}
    (data / "heartbeat.json").write_text(json.dumps(hb, ensure_ascii=False, indent=1))


def heartbeat_due(minutes: int = 60) -> bool:
    """Evita 1 commit a cada 10 min: só empurra o heartbeat de hora em hora (ou se o status mudou)."""
    mark = STATE_DIR / "last_push"
    changed = bool(git("status", "--porcelain", DATA_DIR_NAME + "/published.json", check=False))
    old = mark.exists() and time.time() - mark.stat().st_mtime < minutes * 60
    if changed or not old:
        mark.touch()
        return True
    return False


def channels() -> list[dict]:
    return json.loads((HERE / "channels.json").read_text())


def channel_name(cid: str) -> str:
    for c in channels():
        if c["id"] == cid:
            return c["name"]
    raise KeyError(f"canal {cid} não está em channels.json")


def joined_video(item) -> tuple[Path, bool]:
    """Junta partes (video.part00, part01...) num arquivo temporário. Retorna (caminho, é_temporário)."""
    paths = item.video_paths()
    if len(paths) == 1:
        return paths[0], False
    fd, tmp = tempfile.mkstemp(suffix=".mp4", dir=str(STATE_DIR))
    with os.fdopen(fd, "wb") as out:
        for p in paths:
            with open(p, "rb") as f:
                while chunk := f.read(8 << 20):
                    out.write(chunk)
    return Path(tmp), True


# ------------------------------------------------- tarefas pós-publicação
POST_MAX_AGE = timedelta(days=7)   # vínculo/comentário só para vídeos recentes
PUBLIC_MARGIN = timedelta(minutes=5)


def video_id(url: str | None) -> str | None:
    m = re.search(r"(?:youtu\.be/|/shorts/|[?&]v=|/video/)([\w-]{11})", url or "")
    return m.group(1) if m else None


def remember(state: dict, it) -> None:
    """Copia para o estado o que as tarefas pós-publicação precisam: a pasta do episódio
    some do repositório no dia seguinte, mas o vínculo/comentário pode ficar para depois."""
    rec = state.get(it.key)
    if not rec or rec.get("status") != "published":
        return
    rec["channel_id"] = it.channel_id
    rec["title"] = it.clean_title()
    rec["kind"] = it.kind
    if it.publish_at:
        rec["publish_at"] = it.publish_at.isoformat()
    else:
        rec.setdefault("publish_at", rec.get("at"))
    if it.related_key:
        rec["related_key"] = it.related_key
    if it.pinned_comment:
        rec["pinned_comment"] = it.pinned_comment


def _dt(value: str | None) -> datetime | None:
    try:
        return datetime.fromisoformat(value) if value else None
    except ValueError:
        return None


def is_public(rec: dict, now) -> bool:
    t = _dt(rec.get("publish_at"))
    return t is None or now >= t + PUBLIC_MARGIN


def post_tasks(state: dict, now) -> list[tuple[str, str]]:
    """(tipo, key) para fazer agora: 'related' (Short → longo) e 'comment' (comentário fixado)."""
    out = []
    for key, rec in state.items():
        if rec.get("status") != "published" or not video_id(rec.get("url")):
            continue
        at = _dt(rec.get("publish_at")) or _dt(rec.get("at"))
        if at and now - at > POST_MAX_AGE:
            continue
        rk = rec.get("related_key")
        if rk and not rec.get("related_done") and rec.get("related_attempts", 0) < 3:
            target = state.get(rk) or {}
            if target.get("status") == "published" and video_id(target.get("url")) and is_public(target, now):
                out.append(("related", key))
        if rec.get("pinned_comment") and not rec.get("comment_done") and rec.get("comment_attempts", 0) < 3 \
                and is_public(rec, now):
            out.append(("comment", key))
    return out


def run_post_task(st, state: dict, kind: str, key: str) -> str:
    rec = state[key]
    st.switch_channel(rec["channel_id"], channel_name(rec["channel_id"]))
    if kind == "related":
        target = state[rec["related_key"]]
        return st.set_related_video(video_id(rec["url"]), video_id(target["url"]), target.get("title", ""))
    return st.post_pinned_comment(video_id(rec["url"]), rec["pinned_comment"], channel_name(rec["channel_id"]))


# ----------------------------------------------------------------- comandos
def cmd_plan(_args):
    git_pull()
    items, errors = mf.discover(REPO)
    state, now = load_state(), mf.now_sp()
    for e in errors:
        print("ERRO:", e)
    for it in items:
        d = mf.decide(it, state, now, GRACE)
        print(f"{d.action:7} {it.key:28} {d.visibility:8} {d.when or ''} — {d.reason}")
    for kind, key in post_tasks(state, now):
        print(f"{kind:7} {key}")


def cmd_run(args):
    git_pull()
    # importa DEPOIS do pull: senão a rodada usa o studio.py antigo (visto em 09/11)
    from studio import LoginNeeded, Studio, StudioError, open_browser  # noqa: F401
    items, errors = mf.discover(REPO)
    for e in errors:
        log.error(e)
    state, now = load_state(), mf.now_sp()
    todo = []
    for it in items:
        d = mf.decide(it, state, now, GRACE)
        if d.action == "done" and it.done_url and state.get(it.key, {}).get("status") != "published":
            state[it.key] = {"status": "published", "url": it.done_url, "by": "rotina", "at": now.isoformat()}
        if d.action == "upload":
            miss = it.missing_files()
            if miss:
                log.error("%s: arquivos faltando %s", it.key, miss)
                continue
            todo.append((it, d))
        remember(state, it)
    later = post_tasks(state, now)
    summary = {"pending": len(todo), "post_tasks": len(later), "errors": errors}
    if not todo and not later:
        save_state(state)
        write_heartbeat(summary)
        if heartbeat_due():
            git_push_data("robo: heartbeat")
        log.info("nada para publicar")
        return

    todo.sort(key=lambda x: (x[0].channel_id, x[0].publish_at or now))
    pw, ctx = open_browser(PROFILE)
    published = []
    try:
        st = Studio(ctx, LOG_DIR)
        st.ensure_logged_in()
        for it, d in todo:
            rec = state.setdefault(it.key, {"attempts": 0})
            rec["attempts"] = rec.get("attempts", 0) + 1
            try:
                st.switch_channel(it.channel_id, channel_name(it.channel_id))
                existing = st.title_exists(it.channel_id, it.clean_title())
                if existing:
                    rec.update(status="published", url=existing, by="ja-existia", at=mf.now_sp().isoformat())
                    log.info("%s já existe no canal (%s) — pulando", it.key, existing)
                    save_state(state)
                    continue
                video, temp = joined_video(it)
                try:
                    url = st.upload(it, video, d.visibility, d.when)
                finally:
                    if temp:
                        video.unlink(missing_ok=True)
                rec.update(status="published", url=url, by="robo", visibility=d.visibility,
                           when=d.when.isoformat() if d.when else None, at=mf.now_sp().isoformat(), error=None)
                remember(state, it)
                published.append(f"{it.key}: {url}")
                log.info("PUBLICADO %s → %s", it.key, url)
            except LoginNeeded:
                raise
            except Exception as e:  # noqa: BLE001
                shot = st.shot(f"erro-{it.key}")
                rec.update(status="error", error=str(e)[:300], screenshot=shot.name, at=mf.now_sp().isoformat())
                log.exception("falha em %s", it.key)
                st.close_popups()
                if rec["attempts"] >= 3:
                    notify(f"{it.key}: 3 falhas seguidas — {str(e)[:150]}")
            finally:
                save_state(state)
        # vínculo do Short ao longo e comentário fixado: só quando o vídeo já está público
        for kind, key in post_tasks(state, mf.now_sp()):
            rec = state[key]
            field = "related" if kind == "related" else "comment"
            rec[f"{field}_attempts"] = rec.get(f"{field}_attempts", 0) + 1
            try:
                result = run_post_task(st, state, kind, key)
                rec[f"{field}_done"] = mf.now_sp().isoformat()
                rec.pop(f"{field}_error", None)
                published.append(f"{key}: {field} {result}")
                log.info("%s %s: %s", field.upper(), key, result)
            except LoginNeeded:
                raise
            except Exception as e:  # noqa: BLE001
                shot = st.shot(f"erro-{field}-{key}")
                rec[f"{field}_error"] = f"{str(e)[:250]} ({shot.name})"
                log.exception("falha (%s) em %s", field, key)
                st.close_popups()
                if rec[f"{field}_attempts"] >= 3:
                    notify(f"{key}: {field} falhou 3 vezes — {str(e)[:150]}")
            finally:
                save_state(state)
    except LoginNeeded as e:
        notify(str(e))
        summary["login_needed"] = True
    finally:
        ctx.close()
        pw.stop()
        summary["published_now"] = published
        write_heartbeat(summary)
        git_push_data(f"robo: {len(published)} publicado(s)")
    if published and args.notify_ok:
        notify("Publicado:\n" + "\n".join(published))


def cmd_metrics(_args):
    git_pull()
    from studio import Studio, open_browser
    pw, ctx = open_browser(PROFILE)
    result = {"collected_at": mf.now_sp().isoformat(), "channels": []}
    try:
        st = Studio(ctx, LOG_DIR)
        st.ensure_logged_in()
        for c in channels():
            try:
                st.switch_channel(c["id"], c["name"])
                data = st.collect_metrics(c["id"])
                data["name"] = c["name"]
                result["channels"].append(data)
            except Exception as e:  # noqa: BLE001
                log.exception("métricas %s", c["name"])
                result["channels"].append({"name": c["name"], "channel_id": c["id"], "error": str(e)[:300]})
    finally:
        ctx.close()
        pw.stop()
    out = REPO / DATA_DIR_NAME / "metrics"
    out.mkdir(parents=True, exist_ok=True)
    day = mf.now_sp().strftime("%Y-%m-%d")
    (out / f"{day}.json").write_text(json.dumps(result, ensure_ascii=False, indent=1))
    # mantém só 30 dias de arquivos
    for old in sorted(out.glob("*.json"))[:-30]:
        old.unlink()
    git_push_data(f"robo: métricas {day}")
    log.info("métricas gravadas: %s", out / f"{day}.json")


def cmd_check(_args):
    from studio import Studio, open_browser

    pw, ctx = open_browser(PROFILE)
    try:
        st = Studio(ctx, LOG_DIR)
        st.ensure_logged_in()
        print("login OK")
        for c in channels():
            try:
                st.switch_channel(c["id"], c["name"])
                print(f"OK  {c['name']}  → {st.shot('check-' + c['name'])}")
            except Exception as e:  # noqa: BLE001
                print(f"ERRO {c['name']}: {e}")
    finally:
        ctx.close()
        pw.stop()


def cmd_test_upload(args):
    from studio import Studio, open_browser

    git_pull()
    items, _ = mf.discover(REPO)
    it = next((i for i in items if i.key == args.key), None)
    if not it:
        sys.exit(f"key {args.key} não encontrada")
    pw, ctx = open_browser(PROFILE)
    try:
        st = Studio(ctx, LOG_DIR)
        st.ensure_logged_in()
        st.switch_channel(it.channel_id, channel_name(it.channel_id))
        video, temp = joined_video(it)
        try:
            url = st.upload(it, video, "public", None, private_test=True)
        finally:
            if temp:
                video.unlink(missing_ok=True)
        print("TESTE OK (vídeo PRIVADO):", url)
    finally:
        ctx.close()
        pw.stop()


def cmd_test_post(args):
    """Roda uma tarefa pós-publicação avulsa (sem mexer no estado), para testar no Studio real."""
    from studio import Studio, open_browser

    pw, ctx = open_browser(PROFILE)
    try:
        st = Studio(ctx, LOG_DIR)
        st.ensure_logged_in()
        st.switch_channel(args.channel, channel_name(args.channel))
        if args.kind == "related":
            print("RESULTADO:", st.set_related_video(args.video, args.target, args.title or ""))
        else:
            print("RESULTADO:", st.post_pinned_comment(args.video, args.text, channel_name(args.channel)))
    finally:
        ctx.close()
        pw.stop()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--notify-ok", action="store_true", help="avisar também quando publicar com sucesso")
    sub.add_parser("metrics")
    sub.add_parser("check")
    sub.add_parser("plan")
    t = sub.add_parser("test-upload")
    t.add_argument("--key", required=True)
    tp = sub.add_parser("test-post")
    tp.add_argument("kind", choices=["related", "comment"])
    tp.add_argument("--channel", required=True)
    tp.add_argument("--video", required=True, help="ID do Short (related) ou do vídeo (comment)")
    tp.add_argument("--target", help="related: ID do longo")
    tp.add_argument("--title", help="related: título do longo")
    tp.add_argument("--text", help="comment: texto do comentário")
    args = ap.parse_args()
    setup_logging()
    _lock = single_instance(0 if args.cmd in ("run", "plan") else 45)
    {"run": cmd_run, "metrics": cmd_metrics, "check": cmd_check, "plan": cmd_plan,
     "test-upload": cmd_test_upload, "test-post": cmd_test_post}[args.cmd](args)


if __name__ == "__main__":
    main()
