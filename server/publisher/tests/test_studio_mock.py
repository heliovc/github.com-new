"""Testa o fluxo do robô contra um Studio FALSO (HTML local com os mesmos seletores).

Não prova que o Studio real aceita — prova que a lógica (troca de canal, dedupe, campos,
legenda, agenda, captura do link) está certa. O teste real é `publisher.py test-upload`.
Precisa do Google Chrome instalado. Rodar: pytest -q tests/
"""
import json
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import manifest as mf  # noqa: E402
from studio import Studio  # noqa: E402

pytestmark = pytest.mark.skipif(not shutil.which("google-chrome"), reason="precisa do Google Chrome")
SP = timezone(timedelta(hours=-3))
CHANNELS = {"UCd_BGmJ5gbQ0kECAxmbvQHA": "Por Trás do Dinheiro", "UCsYYjUbmq4n3lAKgw2F2IJw": "Cosmic Scale"}

COMMON_JS = """
const cookie = n => (document.cookie.split('; ').find(c => c.startsWith(n+'='))||'').split('=')[1];
const db = () => JSON.parse(localStorage.getItem('db') || '[]');
"""

SWITCHER = """<html lang="pt-BR"><body><h1>All channels</h1>%s
<script>""" + COMMON_JS + """
for (const a of document.querySelectorAll('a.ch')) a.onclick = e => { e.preventDefault();
  document.cookie = 'active=' + a.dataset.id + '; path=/; domain=.youtube.com'; location.href = 'https://www.youtube.com/'; };
</script></body></html>"""

ROOT = """<html lang="pt-BR"><body><script>""" + COMMON_JS + """
location.replace('https://studio.youtube.com/channel/' + (cookie('active') || 'UCsYYjUbmq4n3lAKgw2F2IJw'));
</script></body></html>"""

LIST = """<html lang="pt-BR"><body><div id="list"></div><script>""" + COMMON_JS + """
const cid = location.pathname.split('/')[2];
if (cookie('active') !== cid) document.body.innerHTML = 'Ops, você não tem permissão';
else for (const v of db().filter(v => v.channel === cid)) {
  const r = document.createElement('ytcp-video-row');
  r.innerHTML = `<a id="thumbnail-anchor" href="https://studio.youtube.com/video/${v.id}/edit">t</a><span id="video-title">${v.title}</span>`;
  document.getElementById('list').appendChild(r);
}
</script></body></html>"""

UPLOAD = """<html lang="pt-BR"><body>
<ytcp-uploads-file-picker><input type="file" id="pick"></ytcp-uploads-file-picker>
<ytcp-uploads-dialog style="display:none">
  <section id="s1">
    <div id="title-textarea"><div id="textbox" contenteditable="true"></div></div>
    <div id="description-textarea"><div id="textbox" contenteditable="true"></div></div>
    <ytcp-thumbnail-uploader><input type="file" id="thumb"></ytcp-thumbnail-uploader>
    <tp-yt-paper-radio-button name="VIDEO_MADE_FOR_KIDS_NOT_MFK" onclick="S.kids='no'">Não é para crianças</tp-yt-paper-radio-button>
    <button id="toggle-button" onclick="document.getElementById('more').style.display='block'">Mostrar mais</button>
    <div id="more" style="display:none">
      <tp-yt-paper-radio-button name="VIDEO_HAS_ALTERED_CONTENT_YES" onclick="S.ai='yes'">Sim</tp-yt-paper-radio-button>
      <input aria-label="Tags" id="tags">
    </div>
    <a href="https://youtu.be/AbCdEfGhIjK">https://youtu.be/AbCdEfGhIjK</a>
  </section>
  <section id="s2" style="display:none">
    <button id="subtitles-button" onclick="document.getElementById('cap1').style.display='block'">Legendas</button>
    <div id="cap1" style="display:none"><span onclick="document.getElementById('cap2').style.display='block'">Enviar arquivo</span>
      <div id="cap2" style="display:none"><input type="file" id="captions-file-loader">
        <button onclick="S.capDone=true;document.getElementById('cap1').style.display='none'">Pronto</button></div></div>
  </section>
  <section id="s3" style="display:none">Verificações</section>
  <section id="s4" style="display:none">
    <tp-yt-paper-radio-button name="PRIVATE" onclick="S.vis='private'">Privado</tp-yt-paper-radio-button>
    <tp-yt-paper-radio-button name="PUBLIC" onclick="S.vis='public'">Público</tp-yt-paper-radio-button>
    <button id="second-container-expand-button" onclick="S.vis='schedule';document.getElementById('second-container').style.display='block'">Programar</button>
    <div id="second-container" style="display:none">
      <button id="datepicker-trigger" onclick="document.getElementById('dp').style.display='block'">data</button>
      <ytcp-date-picker id="dp" style="display:none"><tp-yt-paper-input><input id="date"></tp-yt-paper-input></ytcp-date-picker>
      <div id="time-of-day-container"><input id="time"></div>
      <span id="shown"></span>
    </div>
  </section>
  <button id="next-button">Avançar</button>
  <button id="done-button">Salvar</button>
</ytcp-uploads-dialog>
<div id="share"></div>
<script>""" + COMMON_JS + """
const cid = location.pathname.split('/')[2];
if (cookie('active') !== cid) document.body.innerHTML = 'Ops, você não tem permissão';
window.S = {step: 1};
const $ = id => document.getElementById(id);
$('pick').onchange = () => { S.video = $('pick').files[0].name; document.querySelector('ytcp-uploads-dialog').style.display='block'; };
$('thumb').onchange = () => S.thumb = $('thumb').files[0].name;
$('captions-file-loader').onchange = () => S.cap = $('captions-file-loader').files[0].name;
$('tags').oninput = () => S.tags = $('tags').value;
const upd = () => $('shown').textContent = ($('date').value||'') + ' ' + ($('time').value||'');
$('date').onkeydown = e => { if (e.key==='Enter') { S.date = $('date').value; upd(); } };
$('time').onkeydown = e => { if (e.key==='Enter') { S.time = $('time').value; upd(); } };
$('next-button').onclick = () => { $('s'+S.step).style.display='none'; S.step++; $('s'+S.step).style.display='block'; };
$('done-button').onclick = () => {
  const boxes = document.querySelectorAll('ytcp-uploads-dialog #textbox');
  S.title = boxes[0].innerText; S.desc = boxes[1].innerText;
  const all = db(); all.push({id: 'AbCdEfGhIjK', channel: cid, title: S.title}); localStorage.setItem('db', JSON.stringify(all));
  localStorage.setItem('last', JSON.stringify(S));
  $('share').innerHTML = '<ytcp-video-share-dialog><a href="https://youtu.be/AbCdEfGhIjK">link</a><button id="close-button" onclick="this.parentNode.remove()">x</button></ytcp-video-share-dialog>';
};
</script></body></html>"""


def route(r):
    url = r.request.url
    if url.startswith("https://www.youtube.com/channel_switcher"):
        links = "".join(f'<a class="ch" href="#" data-id="{cid}">{name}</a><br>' for cid, name in CHANNELS.items())
        return r.fulfill(body=SWITCHER % links, content_type="text/html; charset=utf-8")
    if url.startswith("https://www.youtube.com/"):
        return r.fulfill(body="<html><body>home</body></html>", content_type="text/html; charset=utf-8")
    if url.rstrip("/") == "https://studio.youtube.com":
        return r.fulfill(body=ROOT, content_type="text/html; charset=utf-8")
    if url.startswith("https://studio.youtube.com/channel/"):
        if "/videos/upload?d=ud" in url:
            return r.fulfill(body=UPLOAD, content_type="text/html; charset=utf-8")
        if "/videos/" in url:
            return r.fulfill(body=LIST, content_type="text/html; charset=utf-8")
        return r.fulfill(body="<html lang='pt-BR'><body>Painel</body></html>", content_type="text/html; charset=utf-8")
    return r.abort()


@pytest.fixture()
def studio(tmp_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        ctx.route("**/*", route)
        ctx.set_default_timeout(10_000)
        ctx.new_page()
        yield Studio(ctx, tmp_path / "logs")
        browser.close()


def test_full_flow(studio, tmp_path):
    d = tmp_path / "ep07"
    d.mkdir()
    for f in ("video.mp4", "thumbnail.png", "legendas.srt"):
        (d / f).write_bytes(b"x")
    (d / "publish.json").write_text(json.dumps({
        "version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": "2026-11-07T15:00:00-03:00",
        "items": [{"key": "ptd-ep07-long", "kind": "long", "video": "video.mp4", "title": "Pix: quem paga a conta?",
                   "description": "Linha 1\nLinha 2", "tags": ["pix", "banco central"], "thumbnail": "thumbnail.png",
                   "captions": "legendas.srt", "publish_at": "2026-11-08T18:00:00-03:00"}]}))
    it = mf.discover(tmp_path)[0][0]

    studio.switch_channel(it.channel_id, "Por Trás do Dinheiro")
    assert studio.active_channel_id() == "UCd_BGmJ5gbQ0kECAxmbvQHA"
    assert studio.title_exists(it.channel_id, it.clean_title()) is None

    url = studio.upload(it, it.video_paths()[0], "schedule", it.publish_at)
    assert url == "https://youtu.be/AbCdEfGhIjK"
    s = json.loads(studio.js("localStorage.getItem('last')"))
    assert s["title"] == "Pix: quem paga a conta?"
    assert "Linha 2" in s["desc"]
    assert s["video"] == "video.mp4" and s["thumb"] == "thumbnail.png" and s["cap"] == "legendas.srt"
    assert s["kids"] == "no" and s["ai"] == "yes" and s["capDone"] is True
    assert s["tags"] == "pix, banco central,"
    assert s["vis"] == "schedule" and s["date"] == "8 de nov. de 2026" and s["time"] == "18:00"

    # dedupe: agora o título existe no canal
    assert studio.title_exists(it.channel_id, it.clean_title()) == "https://youtu.be/AbCdEfGhIjK"

    # troca para outro canal e publica "agora" (público)
    studio.switch_channel("UCsYYjUbmq4n3lAKgw2F2IJw", "Cosmic Scale")
    it.channel_id = "UCsYYjUbmq4n3lAKgw2F2IJw"
    it.title = "Another title"
    it.captions = None
    studio.upload(it, it.video_paths()[0], "public", None)
    s = json.loads(studio.js("localStorage.getItem('last')"))
    assert s["vis"] == "public" and s["title"] == "Another title"
