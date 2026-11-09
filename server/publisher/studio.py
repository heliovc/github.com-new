"""Automação do YouTube Studio com Playwright (Chrome real, perfil persistente).

Seletores vêm do método validado pelas rotinas em 03–07/11/2026 (ver status dos canais
no Projeto). O Studio muda de vez em quando: cada passo tira screenshot quando falha
(pasta LOG_DIR) para facilitar o ajuste.
"""
from __future__ import annotations

import logging
import os
import re
import socket
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import BrowserContext, Page, TimeoutError as PWTimeout, sync_playwright

log = logging.getLogger("studio")

PT_MONTHS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
EN_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

DIALOG = "ytcp-uploads-dialog"


class StudioError(RuntimeError):
    pass


class LoginNeeded(StudioError):
    pass


def _lock_is_stale(lock: Path) -> bool:
    """SingletonLock aponta para 'host-pid'. Se esse processo não existe mais, é sobra de um
    Chrome que morreu (OOM, kill, queda) e travaria o robô para sempre."""
    try:
        host, _, pid = os.readlink(lock).rpartition("-")
    except OSError:
        return False
    if host != socket.gethostname() or not pid.isdigit():
        return False
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return True
    except PermissionError:
        return False
    return False


def open_browser(profile_dir: Path):
    """Abre o Chrome com o perfil já logado. Retorna (playwright, context)."""
    lock = profile_dir / "SingletonLock"
    if lock.exists() or lock.is_symlink():
        if _lock_is_stale(lock):
            log.warning("lock de Chrome morto (%s): removendo", os.readlink(lock))
            for name in ("SingletonLock", "SingletonCookie", "SingletonSocket"):
                (profile_dir / name).unlink(missing_ok=True)
        else:
            # perfil aberto por outro Chrome (ex.: login.sh esquecido aberto)
            raise StudioError(f"perfil em uso ({lock}). Feche o Chrome do login.sh antes.")
    pw = sync_playwright().start()
    ctx = pw.chromium.launch_persistent_context(
        str(profile_dir),
        channel="chrome",
        headless=False,  # roda dentro do Xvfb (xvfb-run); headless chama mais atenção do Google
        viewport={"width": 1440, "height": 900},
        locale="pt-BR",
        timezone_id="America/Sao_Paulo",
        accept_downloads=False,
        ignore_default_args=["--enable-automation"],
        args=["--disable-blink-features=AutomationControlled", "--no-first-run", "--no-default-browser-check"],
    )
    ctx.set_default_timeout(60_000)  # droplet de 2 GB é lento: 30 s estourava no goto do Studio
    return pw, ctx


class Studio:
    def __init__(self, ctx: BrowserContext, log_dir: Path):
        self.ctx = ctx
        self.page: Page = ctx.pages[0] if ctx.pages else ctx.new_page()
        self.log_dir = log_dir
        log_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------ util
    def shot(self, name: str) -> Path:
        p = self.log_dir / f"{datetime.now():%Y%m%d-%H%M%S}-{re.sub(r'[^a-z0-9_-]+', '_', name.lower())}.png"
        try:
            self.page.screenshot(path=str(p), full_page=False)
        except Exception:  # noqa: BLE001
            pass
        return p

    def js(self, code: str, arg=None):
        return self.page.evaluate(code, arg)

    def click_text(self, texts: list[str], scope: str = "body", timeout: float = 8.0) -> bool:
        """Clica no 1º elemento visível cujo texto é exatamente um dos textos (pt/en)."""
        end = time.time() + timeout
        while time.time() < end:
            for t in texts:
                loc = self.page.locator(scope).get_by_text(t, exact=True)
                for i in range(min(loc.count(), 5)):
                    el = loc.nth(i)
                    try:
                        if el.is_visible():
                            el.click()
                            return True
                    except Exception:  # noqa: BLE001
                        continue
            time.sleep(0.5)
        return False

    def wait_visible(self, selector: str, timeout: float = 30.0):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout * 1000)

    def ui_lang(self) -> str:
        lang = (self.js("document.documentElement.lang") or "").lower()
        return "en" if lang.startswith("en") else "pt"

    # ------------------------------------------------------------ login/canal
    def ensure_logged_in(self):
        self.page.goto("https://studio.youtube.com/", wait_until="domcontentloaded")
        self.page.wait_for_timeout(4000)
        if "accounts.google.com" in self.page.url or "ServiceLogin" in self.page.url:
            self.shot("login-needed")
            raise LoginNeeded("Google pediu login — rode login.sh e entre na conta de novo")

    def active_channel_id(self) -> str | None:
        """Canal ativo no Studio. Com o droplet carregado o redirecionamento para /channel/UC… pode
        passar de 20 s (09/11: Painel já mostrava o canal certo e a URL ainda não tinha o ID), então
        espera até 60 s e, se a URL não trouxer o ID, lê dos links do menu lateral."""
        try:
            self.page.goto("https://studio.youtube.com/", wait_until="domcontentloaded")
        except PWTimeout:
            log.warning("Studio demorou para abrir; tentando ler o canal assim mesmo")
        end = time.time() + 60
        while time.time() < end:
            m = re.search(r"/channel/(UC[\w-]+)", self.page.url)
            if m:
                return m.group(1)
            try:
                cid = self.js("""() => {
                  for (const a of document.querySelectorAll('ytcp-navigation-drawer a[href*="/channel/UC"], a[href*="studio.youtube.com/channel/UC"]')) {
                    const m = (a.getAttribute('href') || '').match(/\\/channel\\/(UC[\\w-]+)/);
                    if (m) return m[1];
                  }
                  return null;
                }""")
            except Exception:  # noqa: BLE001  (página navegando)
                cid = None
            if cid:
                return cid
            self.page.wait_for_timeout(2000)
        return None

    def _fresh_tab(self):
        """O Studio guarda o canal ativo na aba: na mesma aba ele continua no canal antigo
        mesmo depois da troca (provado no droplet em 08/11). Uma aba nova enxerga a troca."""
        old = self.page
        self.page = self.ctx.new_page()
        old.close()

    def switch_channel(self, channel_id: str, channel_name: str):
        for attempt in range(2):
            if self.active_channel_id() == channel_id:
                return
            self.page.goto("https://www.youtube.com/channel_switcher", wait_until="domcontentloaded")
            # cartão do canal: link com o nome exato. A lista carrega devagar (~8 s no droplet),
            # então espera o nome aparecer em vez de um tempo fixo.
            loc = self.page.get_by_text(channel_name, exact=True)
            try:
                loc.first.wait_for(timeout=45_000)
            except PWTimeout:
                self.shot(f"switcher-sem-{channel_name}")
                raise StudioError(f"canal '{channel_name}' não aparece no channel_switcher")
            loc.first.click()
            # A troca termina em segundo plano na home do youtube.com. Ir para o Studio cedo demais
            # interrompe a troca (no droplet, 4 s fixos deixavam o Studio no canal antigo).
            try:
                self.page.wait_for_url(lambda u: "channel_switcher" not in u, timeout=30_000)
                self.page.wait_for_load_state("load", timeout=60_000)
            except PWTimeout:
                pass
            self.page.wait_for_timeout(15_000)
            self._fresh_tab()
        if self.active_channel_id() == channel_id:
            return
        # plano B (validado em 07/11): youtube.com → avatar → "Mudar de conta" → canal
        try:
            self.page.goto("https://www.youtube.com/", wait_until="domcontentloaded")
            self.page.wait_for_timeout(3000)
            self.page.locator("#avatar-btn, button#avatar-btn").first.click()
            self.page.wait_for_timeout(1500)
            if self.click_text(["Mudar de conta", "Switch account"], timeout=6):
                self.page.wait_for_timeout(1500)
                self.page.get_by_text(channel_name, exact=True).first.click()
                self.page.wait_for_timeout(15_000)
                self._fresh_tab()
        except Exception as e:  # noqa: BLE001
            log.warning("plano B de troca de canal falhou: %s", e)
        if self.active_channel_id() != channel_id:
            self.shot(f"switch-falhou-{channel_name}")
            raise StudioError(f"não consegui ativar o canal {channel_name} ({channel_id})")

    # --------------------------------------------------------------- dedupe
    def title_exists(self, channel_id: str, title: str) -> str | None:
        """Procura o título na lista de Conteúdo (vídeos e Shorts). Retorna o link se achar."""
        needle = norm(title)[:60]
        for tab in ("upload", "short"):
            self.page.goto(f"https://studio.youtube.com/channel/{channel_id}/videos/{tab}", wait_until="domcontentloaded")
            try:
                self.page.wait_for_selector("ytcp-video-row, ytcp-video-list-cell-video", timeout=15_000)
            except PWTimeout:
                continue
            self.page.wait_for_timeout(1500)
            found = self.js(
                """(needle) => {
                  const norm = s => (s||'').toLowerCase().replace(/\\s+/g,' ').trim();
                  for (const row of document.querySelectorAll('ytcp-video-row')) {
                    const t = row.querySelector('#video-title');
                    if (t && norm(t.textContent).startsWith(needle)) {
                      const a = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
                      const m = a && (a.href||'').match(/\\/video\\/([\\w-]{11})/);
                      return m ? m[1] : 'found';
                    }
                  }
                  return null;
                }""",
                needle,
            )
            if found:
                return f"https://youtu.be/{found}" if found != "found" else "found"
        return None

    # --------------------------------------------------------------- upload
    def open_upload_dialog(self, channel_id: str):
        self.page.goto(f"https://studio.youtube.com/channel/{channel_id}/videos/upload?d=ud", wait_until="domcontentloaded")
        sel = "ytcp-uploads-file-picker input[type=file]"
        try:
            self.page.wait_for_selector(sel, state="attached", timeout=15_000)
            return
        except PWTimeout:
            pass
        # plano B: botão de upload do Painel
        self.page.goto(f"https://studio.youtube.com/channel/{channel_id}", wait_until="domcontentloaded")
        self.page.wait_for_timeout(3000)
        for s in ("#upload-icon", "ytcp-icon-button#upload-icon", "#create-icon"):
            if self.page.locator(s).count():
                self.page.locator(s).first.click()
                break
        self.click_text(["Enviar vídeos", "Upload videos"], timeout=5)
        try:
            self.page.wait_for_selector(sel, state="attached", timeout=15_000)
        except PWTimeout as e:
            self.shot("upload-dialog")
            raise StudioError("diálogo de upload não abriu") from e

    def set_textbox(self, which: int, text: str):
        """which: 0 = título, 1 = descrição (contenteditable #textbox dentro do diálogo)."""
        box = self.page.locator(f"{DIALOG} #textbox").nth(which)
        box.scroll_into_view_if_needed()
        box.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Delete")
        if text:
            self.page.keyboard.insert_text(text)
        self.page.wait_for_timeout(400)
        got = norm(box.inner_text())
        if norm(text)[:40] not in got:
            raise StudioError(f"campo {which} não aceitou o texto (ficou: {got[:60]!r})")

    def video_link(self) -> str | None:
        return self.js(
            """() => {
              const d = document.querySelector('ytcp-uploads-dialog');
              if (!d) return null;
              for (const a of d.querySelectorAll('a')) {
                const h = a.href || '';
                if (/youtu\\.be\\/|youtube\\.com\\/(shorts|watch)/.test(h)) return h;
              }
              return null;
            }"""
        )

    def next_step(self):
        self.page.locator(f"{DIALOG} #next-button").click()
        self.page.wait_for_timeout(1500)

    def upload(self, item, video_file: Path, visibility: str, when: datetime | None, private_test: bool = False) -> str:
        """Faz o upload completo. Retorna o link do vídeo."""
        p = self.page
        self.open_upload_dialog(item.channel_id)
        p.locator("ytcp-uploads-file-picker input[type=file]").set_input_files(str(video_file))
        self.wait_visible(f"{DIALOG} #textbox", 120)
        p.wait_for_timeout(2500)

        # Detalhes
        self.set_textbox(0, item.clean_title())
        self.set_textbox(1, item.clean_description())

        thumb = item.path(item.thumbnail)
        if thumb and item.kind == "long":
            try:
                p.locator(f"{DIALOG} ytcp-thumbnail-uploader input[type=file]").first.set_input_files(str(thumb))
                p.wait_for_timeout(2500)
            except Exception as e:  # noqa: BLE001
                log.warning("thumbnail não entrou: %s", e)
                self.shot("thumbnail")

        kids = "VIDEO_MADE_FOR_KIDS_MFK" if item.made_for_kids else "VIDEO_MADE_FOR_KIDS_NOT_MFK"
        p.locator(f'tp-yt-paper-radio-button[name="{kids}"]').scroll_into_view_if_needed()
        p.locator(f'tp-yt-paper-radio-button[name="{kids}"]').click()

        p.locator(f"{DIALOG} #toggle-button").click()  # Mostrar mais
        p.wait_for_timeout(1000)
        ai = "VIDEO_HAS_ALTERED_CONTENT_YES" if item.altered_content else "VIDEO_HAS_ALTERED_CONTENT_NO"
        if p.locator(f'tp-yt-paper-radio-button[name="{ai}"]').count():
            p.locator(f'tp-yt-paper-radio-button[name="{ai}"]').scroll_into_view_if_needed()
            p.locator(f'tp-yt-paper-radio-button[name="{ai}"]').click()
        else:
            log.warning("opção de conteúdo alterado/IA não encontrada")
            self.shot("ai-disclosure")

        tags = item.clean_tags()
        if tags:
            tag_input = p.locator(f'{DIALOG} input[aria-label="Tags"], {DIALOG} ytcp-free-text-chip-bar input').first
            tag_input.scroll_into_view_if_needed()
            tag_input.click()
            p.keyboard.insert_text(", ".join(tags) + ",")
            p.wait_for_timeout(800)

        link = self.video_link()

        # Elementos (legendas)
        self.next_step()
        cap = item.path(item.captions)
        if cap:
            try:
                self.add_captions(cap)
            except Exception as e:  # noqa: BLE001
                log.warning("legendas não entraram: %s", e)
                self.shot("legendas")
                self.close_popups()

        # Verificações → Visibilidade
        self.next_step()
        self.next_step()
        link = link or self.video_link()

        if private_test:
            p.locator('tp-yt-paper-radio-button[name="PRIVATE"]').click()
        elif visibility == "schedule" and when:
            self.set_schedule(when)
        else:
            p.locator('tp-yt-paper-radio-button[name="PUBLIC"]').click()

        p.wait_for_timeout(800)
        p.locator(f"{DIALOG} #done-button").click()
        p.wait_for_timeout(3000)
        # aviso "ainda estamos verificando..." → Ok / Publicar mesmo assim
        for sel in ("ytcp-prechecks-warning-dialog #primary-action-button", "ytcp-dialog #primary-action-button"):
            if p.locator(sel).count() and p.locator(sel).first.is_visible():
                p.locator(sel).first.click()
                p.wait_for_timeout(2000)
        try:
            p.wait_for_selector("ytcp-video-share-dialog, ytcp-uploads-still-processing-dialog", timeout=60_000)
        except PWTimeout:
            # Visto no droplet em 08/11: o Studio salvou (vídeo apareceu como Privado no Conteúdo) e
            # fechou o diálogo sem mostrar a confirmação. Diálogo fechado + link já capturado = salvo.
            if link and not p.locator(DIALOG).first.is_visible():
                log.warning("Studio fechou o diálogo sem confirmação; considerando salvo: %s", link)
                return link
            self.shot("sem-confirmacao")
            raise StudioError("Studio não confirmou a publicação")
        share = self.js(
            """() => { const d = document.querySelector('ytcp-video-share-dialog, ytcp-uploads-still-processing-dialog');
                       if (!d) return null;
                       for (const a of d.querySelectorAll('a')) if (/youtu/.test(a.href)) return a.href;
                       const m = (d.innerText||'').match(/https:\\/\\/(youtu\\.be|youtube\\.com)\\/[\\w\\/?=-]+/);
                       return m ? m[0] : null; }"""
        )
        self.close_popups()
        return share or link or "publicado (link não capturado)"

    def add_captions(self, srt: Path):
        p = self.page
        p.locator("#subtitles-button").click()
        p.wait_for_timeout(1500)
        if not self.click_text(["Enviar arquivo", "Upload file"], timeout=8):
            raise StudioError("botão 'Enviar arquivo' das legendas não apareceu")
        p.wait_for_timeout(1500)
        # NÃO clicar em Continuar (abre seletor nativo): injeta direto no loader
        loader = p.locator("#captions-file-loader input[type=file], input#captions-file-loader")
        if loader.count() == 0:
            loader = p.locator("#captions-file-loader")
        loader.first.set_input_files(str(srt))
        p.wait_for_timeout(4000)
        if not self.click_text(["Pronto", "Done"], timeout=10):
            raise StudioError("botão Pronto das legendas não apareceu")
        p.wait_for_timeout(1500)

    def set_schedule(self, when: datetime):
        p = self.page
        p.locator("#second-container-expand-button").click()
        p.wait_for_timeout(1200)
        lang = self.ui_lang()
        if lang == "en":
            date_txt = f"{EN_MONTHS[when.month - 1]} {when.day}, {when.year}"
        else:
            date_txt = f"{when.day} de {PT_MONTHS[when.month - 1]}. de {when.year}"
        p.locator("#datepicker-trigger").click()
        p.wait_for_timeout(800)
        date_input = p.locator("ytcp-date-picker tp-yt-paper-input input, ytcp-date-picker input").first
        date_input.click()
        p.keyboard.press("Control+A")
        p.keyboard.insert_text(date_txt)
        p.keyboard.press("Enter")
        p.wait_for_timeout(800)
        hhmm = when.strftime("%H:%M")
        time_input = p.locator("#time-of-day-container input, ytcp-form-input-container#time-of-day-container input").first
        time_input.click()
        p.wait_for_timeout(800)
        # o campo de hora abre uma lista (intervalos de 15 min): clicar no item é o caminho validado em 07/11
        opt = p.locator("tp-yt-paper-item", has_text=re.compile(rf"^\s*{re.escape(hhmm)}\s*$"))
        if opt.count():
            opt.first.scroll_into_view_if_needed()
            opt.first.click()
        else:
            p.keyboard.press("Control+A")
            p.keyboard.insert_text(hhmm)
            p.keyboard.press("Enter")
        p.wait_for_timeout(800)
        shown = norm(self.js("() => (document.querySelector('#second-container')||{}).innerText || ''"))
        if hhmm not in shown:
            self.shot("agenda")
            raise StudioError(f"agenda não conferiu (mostrando: {shown[:120]!r})")

    def close_popups(self):
        for sel in ("ytcp-video-share-dialog #close-button", "ytcp-uploads-still-processing-dialog #close-button",
                    "ytcp-uploads-dialog #close-button"):
            try:
                if self.page.locator(sel).count() and self.page.locator(sel).first.is_visible():
                    self.page.locator(sel).first.click()
                    self.page.wait_for_timeout(800)
            except Exception:  # noqa: BLE001
                pass

    # ------------------------------------------------- pós-publicação: vínculo
    def set_related_video(self, short_id: str, long_id: str, long_title: str) -> str:
        """Campo "Vídeo relacionado" do Short → o longo (só aceita vídeo já público do canal).
        Caminho visto no Studio em 09/11: Detalhes → #linked-video-editor-link → ytcp-video-pick-dialog
        (cartões com miniatura i.ytimg.com/vi/<id>/ e busca #search-yours) → Salvar."""
        p = self.page
        p.goto(f"https://studio.youtube.com/video/{short_id}/edit", wait_until="domcontentloaded")
        field = p.locator("#linked-video-editor-link")
        field.wait_for(state="attached", timeout=90_000)
        p.wait_for_timeout(3000)
        want = norm(long_title)[:30]
        current = norm(field.inner_text())
        if want and want in current:
            return "já estava vinculado"
        field.scroll_into_view_if_needed()
        field.locator("ytcp-dropdown-trigger").first.click()
        dlg = p.locator("ytcp-video-pick-dialog")
        dlg.wait_for(state="visible", timeout=30_000)
        p.wait_for_timeout(2500)
        if long_title:
            box = dlg.locator("#search-yours")
            if box.count():
                box.first.click()
                p.keyboard.insert_text(long_title[:60])
                p.wait_for_timeout(4000)
        clicked = self.js(
            """([vid, want]) => {
              const norm = s => (s || '').toLowerCase().replace(/\\s+/g, ' ').trim();
              const d = document.querySelector('ytcp-video-pick-dialog');
              if (!d) return 'sem-dialogo';
              const cards = [...d.querySelectorAll('ytcp-entity-card, ytcp-video-pick-dialog-contents [role=button], ytcp-video-pick-dialog-contents [tabindex]')];
              const visible = cards.filter(c => c.offsetParent !== null);
              let hit = visible.find(c => [...c.querySelectorAll('img')].some(i => (i.src || '').includes('/vi/' + vid + '/')));
              if (!hit && want) hit = visible.find(c => norm(c.innerText).startsWith(want));
              if (!hit) {  // cartão genérico: sobe a partir da miniatura
                const img = [...d.querySelectorAll('img')].find(i => (i.src || '').includes('/vi/' + vid + '/'));
                if (img) hit = img.closest('[role=button], [tabindex], ytcp-entity-card') || img;
              }
              if (!hit) return 'nao-achei';
              hit.scrollIntoView({block: 'center'});
              hit.click();
              return 'ok';
            }""",
            [long_id, want],
        )
        if clicked != "ok":
            self.shot("relacionado-dialogo")
            p.keyboard.press("Escape")
            raise StudioError(f"vídeo {long_id} não apareceu na lista do 'Vídeo relacionado' ({clicked})")
        p.wait_for_timeout(2500)
        if want and want not in norm(field.inner_text()):
            self.shot("relacionado-nao-marcou")
            raise StudioError("cliquei no vídeo mas o campo não mostrou o título")
        save = p.locator("ytcp-button#save, #save").first
        save.click()
        p.wait_for_timeout(5000)
        # confere recarregando a página
        p.goto(f"https://studio.youtube.com/video/{short_id}/edit", wait_until="domcontentloaded")
        p.locator("#linked-video-editor-link").wait_for(state="attached", timeout=90_000)
        p.wait_for_timeout(3000)
        if want and want not in norm(p.locator("#linked-video-editor-link").inner_text()):
            self.shot("relacionado-nao-salvou")
            raise StudioError("o vínculo não ficou salvo")
        return f"vinculado a {long_id}"

    # ---------------------------------------------- pós-publicação: comentário
    def post_pinned_comment(self, video_id: str, text: str, channel_name: str) -> str:
        """Posta o comentário como o canal (o ativo no youtube.com) e fixa. Só funciona com o vídeo
        público. Se o comentário não sair como dono do canal, apaga e falha (não deixa comentário
        de outra identidade)."""
        p = self.page
        p.goto(f"https://www.youtube.com/watch?v={video_id}", wait_until="domcontentloaded")
        p.wait_for_timeout(6000)
        self.js("() => { const v = document.querySelector('video'); if (v) v.pause(); }")
        for _ in range(8):  # comentários carregam sob demanda
            p.mouse.wheel(0, 900)
            p.wait_for_timeout(1500)
            if p.locator("ytd-comments #simplebox-placeholder").count():
                break
        thread = self._find_comment(text)
        if thread is None:
            ph = p.locator("ytd-comments #simplebox-placeholder").first
            ph.wait_for(state="visible", timeout=30_000)
            ph.scroll_into_view_if_needed()
            ph.click()
            box = p.locator("ytd-comments #contenteditable-root").first
            box.wait_for(state="visible", timeout=15_000)
            box.click()
            p.keyboard.insert_text(text)
            p.wait_for_timeout(800)
            p.locator("ytd-comments #submit-button").first.click()
            p.wait_for_timeout(5000)
            thread = self._find_comment(text)
            if thread is None:
                self.shot("comentario-nao-apareceu")
                raise StudioError("o comentário não apareceu depois de enviar")
        if not thread.locator("ytd-author-comment-badge-renderer, #author-comment-badge ytd-author-comment-badge-renderer").count():
            self._delete_comment(thread)
            self.shot("comentario-identidade")
            raise StudioError(f"comentário saiu com outra identidade (não {channel_name}); apaguei")
        if self._is_pinned(thread):
            return "já estava fixado"
        thread.locator("#action-menu button, #action-menu yt-icon-button").first.click()
        p.wait_for_timeout(1500)
        # menu visto em 09/11: "Fixar no topo" / "Editar" / "Excluir"
        if not self.click_text(["Fixar no topo", "Fixar", "Pin"], timeout=8):
            self.shot("comentario-menu")
            raise StudioError("opção 'Fixar' não apareceu no menu do comentário")
        p.wait_for_timeout(1500)
        for sel in ("yt-confirm-dialog-renderer #confirm-button", "#confirm-button"):
            if p.locator(sel).count() and p.locator(sel).first.is_visible():
                p.locator(sel).first.click()
                break
        p.wait_for_timeout(4000)
        thread = self._find_comment(text)
        if thread is None or not self._is_pinned(thread):
            self.shot("comentario-nao-fixou")
            raise StudioError("comentário postado mas não ficou fixado")
        return "comentário fixado"

    @staticmethod
    def _is_pinned(thread) -> bool:
        # 09/11: o selo é só texto "Fixado por @handle" acima do autor (sem elemento próprio)
        try:
            txt = norm(thread.inner_text())
        except Exception:  # noqa: BLE001
            return False
        return "fixado por" in txt or "pinned by" in txt

    def _find_comment(self, text: str):
        want = norm(text)[:60]
        threads = self.page.locator("ytd-comment-thread-renderer")
        for i in range(min(threads.count(), 20)):
            t = threads.nth(i)
            try:
                body = norm(t.locator("#content-text").first.inner_text())
            except Exception:  # noqa: BLE001
                continue
            if body.startswith(want):
                return t
        return None

    def _delete_comment(self, thread):
        try:
            thread.locator("#action-menu button, #action-menu yt-icon-button").first.click()
            self.page.wait_for_timeout(1200)
            if self.click_text(["Excluir", "Delete"], timeout=6):
                self.page.wait_for_timeout(1200)
                self.page.locator("#confirm-button").first.click()
                self.page.wait_for_timeout(2000)
        except Exception as e:  # noqa: BLE001
            log.warning("não consegui apagar o comentário: %s", e)

    # -------------------------------------------------------------- métricas
    EXPLORE = ("https://studio.youtube.com/channel/{cid}/analytics/tab-overview/period-default/explore?"
               "entity_type=CHANNEL&entity_id={cid}&time_period=lifetime&explore_type=TABLE_AND_CHART&metric=EXTERNAL_VIEWS"
               "&granularity=DAY&t_metrics=EXTERNAL_VIEWS&t_metrics=EXTERNAL_WATCH_TIME&t_metrics=SUBSCRIBERS_NET_CHANGE"
               "&t_metrics=VIDEO_THUMBNAIL_IMPRESSIONS&t_metrics=VIDEO_THUMBNAIL_IMPRESSIONS_VTR&t_metrics=AVERAGE_WATCH_TIME"
               "&t_metrics=AVERAGE_WATCH_PERCENTAGE&dimension=VIDEO&o_column=EXTERNAL_VIEWS"
               "&o_direction=ANALYTICS_ORDER_DIRECTION_DESC")

    def collect_metrics(self, channel_id: str) -> dict:
        p = self.page
        out = {"channel_id": channel_id, "collected_at": datetime.now().astimezone().isoformat()}
        p.goto(self.EXPLORE.format(cid=channel_id), wait_until="domcontentloaded")
        try:
            p.wait_for_selector("yta-explore-table", timeout=30_000)
            p.wait_for_timeout(4000)
            out["table_text"] = self.js("() => document.querySelector('yta-explore-table').innerText")
        except PWTimeout:
            out["table_text"] = None
            out["table_error"] = "tabela não carregou"
            self.shot(f"metricas-{channel_id}")
        p.goto(f"https://studio.youtube.com/channel/{channel_id}", wait_until="domcontentloaded")
        p.wait_for_timeout(6000)
        out["dashboard_text"] = self.js("() => document.body.innerText")[:8000]
        p.goto(f"https://studio.youtube.com/channel/{channel_id}/monetization", wait_until="domcontentloaded")
        p.wait_for_timeout(5000)
        out["monetization_text"] = self.js("() => document.body.innerText")[:4000]
        return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").lower()).strip()
