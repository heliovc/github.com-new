"""publish.json: descoberta, validação e regras de agenda.

Cada pasta de episódio no repositório pode ter um publish.json. Formato (v1):

{
  "version": 1,
  "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA",
  "created_at": "2026-11-07T18:10:00-03:00",
  "items": [
    {
      "key": "ptd-ep06-long",            # único no repositório inteiro (canal-episódio-tipo)
      "kind": "long",                     # long | short
      "video": ["video.mp4"],             # 1 arquivo, ou partes em ordem (video.part00, video.part01...)
      "title": "...",
      "description": "...",
      "tags": ["a", "b"],
      "thumbnail": "thumbnail.png",       # opcional (Shorts ignoram)
      "captions": "legendas.srt",         # opcional
      "publish_at": "2026-11-08T18:00:00-03:00",   # null = publicar já
      "if_late": "public_now",            # public_now | skip   (se publish_at já passou)
      "made_for_kids": false,
      "altered_content": true,
      "done_url": null,                   # se a rotina já publicou por outro caminho, preencha e o robô pula
      "related_key": "cosmic-ep08-long",  # só Shorts: key do longo para o campo "Vídeo relacionado"
      "pinned_comment": "Which star ..."  # opcional: comentário fixado (postado quando o vídeo ficar público)
    }
  ]
}
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

KINDS = {"long", "short"}
LATE_RULES = {"public_now", "skip"}
TITLE_MAX = 100
DESC_MAX = 5000
TAGS_MAX_CHARS = 480  # limite do YouTube é 500 (conta vírgulas); margem


class ManifestError(ValueError):
    pass


@dataclass
class Item:
    key: str
    kind: str
    channel_id: str
    folder: Path
    video: list[str]
    title: str
    description: str = ""
    tags: list[str] = field(default_factory=list)
    thumbnail: str | None = None
    captions: str | None = None
    publish_at: datetime | None = None
    if_late: str = "public_now"
    made_for_kids: bool = False
    altered_content: bool = True
    done_url: str | None = None
    related_key: str | None = None
    pinned_comment: str | None = None
    created_at: datetime | None = None
    manifest_path: Path | None = None

    # ---- arquivos ----
    def video_paths(self) -> list[Path]:
        return [self.folder / v for v in self.video]

    def path(self, name: str | None) -> Path | None:
        return (self.folder / name) if name else None

    def missing_files(self) -> list[str]:
        miss = [str(p) for p in self.video_paths() if not p.exists()]
        for opt in (self.thumbnail, self.captions):
            if opt and not (self.folder / opt).exists():
                miss.append(str(self.folder / opt))
        return miss

    # ---- texto já limpo para o Studio ----
    def clean_title(self) -> str:
        return sanitize(self.title)[:TITLE_MAX]

    def clean_description(self) -> str:
        return sanitize(self.description)[:DESC_MAX]

    def clean_tags(self) -> list[str]:
        out, total = [], 0
        for t in self.tags:
            t = sanitize(t).replace(",", " ").strip()
            if not t:
                continue
            cost = len(t) + (2 if " " in t else 0) + 1
            if total + cost > TAGS_MAX_CHARS:
                break
            out.append(t)
            total += cost
        return out


def sanitize(text: str) -> str:
    """O Studio recusa '<' e '>' em título/descrição."""
    return (text or "").replace("->", "→").replace("<", "‹").replace(">", "›").strip()


def parse_dt(value) -> datetime | None:
    if value in (None, "", "now"):
        return None
    dt = datetime.fromisoformat(str(value))
    if dt.tzinfo is None:
        raise ManifestError(f"data sem fuso horário: {value!r} (use -03:00)")
    return dt


def load_manifest(path: Path) -> list[Item]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ManifestError(f"{path}: JSON inválido: {e}") from e
    if data.get("version") != 1:
        raise ManifestError(f"{path}: version deve ser 1")
    channel_id = data.get("channel_id") or ""
    if not channel_id.startswith("UC"):
        raise ManifestError(f"{path}: channel_id inválido")
    created = parse_dt(data.get("created_at"))
    items = []
    for raw in data.get("items") or []:
        for req in ("key", "kind", "video", "title"):
            if not raw.get(req):
                raise ManifestError(f"{path}: item sem '{req}'")
        if raw["kind"] not in KINDS:
            raise ManifestError(f"{path}: kind inválido {raw['kind']!r}")
        video = raw["video"] if isinstance(raw["video"], list) else [raw["video"]]
        if_late = raw.get("if_late", "public_now")
        if if_late not in LATE_RULES:
            raise ManifestError(f"{path}: if_late inválido {if_late!r}")
        items.append(Item(
            key=raw["key"], kind=raw["kind"], channel_id=raw.get("channel_id", channel_id),
            folder=path.parent, video=video, title=raw["title"],
            description=raw.get("description", ""), tags=list(raw.get("tags") or []),
            thumbnail=raw.get("thumbnail"), captions=raw.get("captions"),
            publish_at=parse_dt(raw.get("publish_at")), if_late=if_late,
            made_for_kids=bool(raw.get("made_for_kids", False)),
            altered_content=bool(raw.get("altered_content", True)),
            done_url=raw.get("done_url"), created_at=created, manifest_path=path,
            related_key=raw.get("related_key") or None,
            pinned_comment=(raw.get("pinned_comment") or "").strip() or None,
        ))
    return items


def discover(repo: Path) -> tuple[list[Item], list[str]]:
    """Acha todos os publish.json (fora de .git e server/). Retorna itens e erros."""
    items, errors, seen = [], [], {}
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in (".git", "server", "server-data", "node_modules")]
        if "publish.json" in files:
            p = Path(root) / "publish.json"
            try:
                for it in load_manifest(p):
                    if it.key in seen:
                        errors.append(f"key repetida {it.key!r}: {seen[it.key]} e {p}")
                        continue
                    seen[it.key] = p
                    items.append(it)
            except ManifestError as e:
                errors.append(str(e))
    return items, errors


@dataclass
class Decision:
    action: str          # upload | wait | skip | done
    visibility: str = "" # schedule | public | private
    when: datetime | None = None
    reason: str = ""


MIN_LEAD = timedelta(minutes=20)  # o Studio exige agendar com folga


def decide(item: Item, state: dict, now: datetime, grace: timedelta) -> Decision:
    """Decide o que fazer com o item agora."""
    st = state.get(item.key) or {}
    if st.get("status") == "published":
        return Decision("done", reason="já publicado pelo robô")
    if item.done_url:
        return Decision("done", reason="rotina já publicou (done_url)")
    if st.get("attempts", 0) >= 3 and st.get("status") == "error":
        return Decision("skip", reason="3 falhas — precisa de revisão manual")
    if item.created_at and now - item.created_at < grace:
        return Decision("wait", reason="dentro da carência (rotina pode publicar pelo Chrome)")
    if item.publish_at is None:
        return Decision("upload", "public", reason="publicar já")
    if item.publish_at - now >= MIN_LEAD:
        return Decision("upload", "schedule", item.publish_at, "agendar")
    if item.if_late == "skip":
        return Decision("skip", reason="horário já passou e if_late=skip")
    return Decision("upload", "public", reason="horário já passou → público agora")


def now_sp() -> datetime:
    return datetime.now(timezone(timedelta(hours=-3)))
