"""Automação do YouTube Studio com Playwright (Chrome real, perfil persistente).

Seletores vêm do método validado pelas rotinas em 03–07/11/2026 (ver status dos canais
no Projeto). O Studio muda de vez em quando: cada passo tira screenshot quando falha
(pasta LOG_DIR) para facilitar o ajuste.
"""
from __future__ import annotations

import logging
import re
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


def open_browser(profile_dir: Path):
    """Abre o Chrome com o perfil já logado. Retorna (playwright, context)."""
    lock = profile_dir / "SingletonLock"
    if lock.exists() or lock.is_symlink():
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
    ctx.set_default_timeout(30_000)
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
        self.page.goto("https://studio.youtube.com/", wait_until="domcontentloaded")
        try:
            self.page.wait_for_url(re.compile(r"/channel/UC"), timeout=20_000)
        except PWTimeout:
            return None
        m = re.search(r"/channel/(UC[\w-]+)", self.page.url)
        return m.group(1) if m else None

    def switch_channel(self, channel_id: str, channel_name: str):
        for attempt in range(2):
            if self.active_channel_id() == channel_id:
                return
            self.page.goto("https://www.youtube.com/channel_switcher", wait_until="domcontentloaded")
            self.page.wait_for_timeout(3000)
            # cartão do canal: link com o nome exato
            loc = self.page.get_by_text(channel_name, exact=True)
            if loc.count() == 0:
                self.shot(f"switcher-sem-{channel_name}")
                raise StudioError(f"canal '{channel_name}' não aparece no channel_switcher")
            loc.first.click()
            self.page.wait_for_timeout(4000)
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
        time_input = p.locator("#time-of-day-container input, ytcp-form-input-container#time-of-day-container input").first
        time_input.click()
        p.keyboard.press("Control+A")
        p.keyboard.insert_text(when.strftime("%H:%M"))
        p.keyboard.press("Enter")
        p.wait_for_timeout(800)
        shown = norm(self.js("() => (document.querySelector('#second-container')||{}).innerText || ''"))
        if when.strftime("%H:%M") not in shown:
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
