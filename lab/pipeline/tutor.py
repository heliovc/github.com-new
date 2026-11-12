"""Shortcut Lab - software/AI tutorials, drawn 100% by code.
Script (scenes: say + vis) -> Kokoro voice (en-us, am_eric) -> editor / terminal / file-explorer / chat animations -> MP4 1080p24 + SRT.
Usage:
  python3 -I tutor.py ep01.py out/ep01 --preview        # one still per scene (at 85% of the scene)
  python3 -I tutor.py ep01.py out/ep01                  # full render -> final.mp4, subtitles.srt, chapters.txt
  python3 -I tutor.py ep01.py out/ep01 --vertical "0,3,5" "TITLE"   # Short 1080x1920 from scenes (uses cached voice)
Scene types: title, steps, code, term, files, tip, keys, compare, chat, outro, tree (EP02), map (EP02), sheet + args (EP03), prompt + flow (EP04), stage + timeline (EP05: Git areas and commit history), term colors diff +/- lines and errors (EP05), figure (EP06: real matplotlib PNG in a plot window, left-to-right wipe + numbered callouts), nav (EP07: folder tree with a moving "YOU ARE HERE" pin driven by cd commands + live pwd bar), cards (EP07: cheat-sheet grid of command cards popping in, optional highlight), funnel (EP08: a QUERY string read clause by clause, each clause
  highlighted on top while its mini result table appears in a column - rows shrinking left to right, row-count badges); sheet results now
  draw the header row in bold when a QUERY result starts on row 1 (EP08)
Identity: charcoal #0F1115, lime #B6F35C, coral #FF7A59, sky #6CC4FF, Poppins + DejaVu Sans Mono.
"""
import sys, os, re, math, json, hashlib, subprocess, importlib.util
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 24
HERE = os.path.dirname(os.path.abspath(__file__))
PF = "/usr/share/fonts/truetype/google-fonts/Poppins-"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
_fc = {}
def F(size, w="Medium"):
    w = {"SemiBold": "Bold"}.get(w, w)
    k = (int(size), w)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(MONO if w == "mono" else MONOB if w == "monob" else PF + f"{w}.ttf", int(size))
    return _fc[k]

BG, PANEL, PANEL2, LINE = (15, 17, 21), (24, 27, 34), (31, 35, 44), (46, 51, 63)
TXT, DIM, LIME, CORAL, SKY, VIO, YEL = (232, 236, 242), (130, 138, 155), (182, 243, 92), (255, 122, 89), (108, 196, 255), (190, 150, 255), (255, 211, 105)
BRAND = "SHORTCUT LAB"
ACC = LIME  # per-episode accent (ep module: ACCENT = SKY / CORAL / YEL ...)

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def mix(a, b, t): t = max(0, min(1, t)); return tuple(int(x + (y - x) * t) for x, y in zip(a, b))

# ---------------- background
def make_bg(w=W, h=H):
    img = Image.new("RGB", (w, h), BG); d = ImageDraw.Draw(img)
    for x in range(0, w, 48):
        for y in range(0, h, 48): d.point((x, y), fill=(34, 38, 47))
    g = Image.new("L", (w, h), 0); dg = ImageDraw.Draw(g); dg.ellipse([-w * 0.3, -h * 0.6, w * 0.6, h * 0.5], fill=40)
    g = g.filter(ImageFilter.GaussianBlur(160))
    img = Image.composite(Image.new("RGB", (w, h), mix(BG, ACC, 0.16)), img, g)
    return img.convert("RGBA")

def chrome(img, prog, label=""):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([56, 40, 96, 80], 9, fill=ACC); d.text((76, 60), "⌘", font=F(28, "monob"), fill=BG, anchor="mm")
    d.text((110, 60), BRAND, font=F(22, "SemiBold"), fill=TXT, anchor="lm")
    if label: d.text((W - 60, 60), label, font=F(20, "Medium"), fill=DIM, anchor="rm")
    d.rectangle([0, H - 6, W * prog, H], fill=ACC)

def text_a(img, xy, s, font, fill, a=1.0, anchor="la"):
    if a <= 0: return
    if a >= 0.999: ImageDraw.Draw(img).text(xy, s, font=font, fill=fill, anchor=anchor); return  # fast path (EP03)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).text(xy, s, font=font, fill=fill + (int(255 * a),), anchor=anchor)
    img.alpha_composite(lay)

def wrap(s, font, maxw):
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if font.getlength(t) > maxw and cur: out.append(cur); cur = w
        else: cur = t
    return out + ([cur] if cur else [])

def window(img, box, title, kind="editor", a=1.0):
    x0, y0, x1, y1 = box
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    ds.rounded_rectangle([x0 + 10, y0 + 18, x1 + 10, y1 + 18], 18, fill=(0, 0, 0, int(140 * a))); sh = sh.filter(ImageFilter.GaussianBlur(18)); img.alpha_composite(sh)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box, 16, fill=PANEL if kind == "editor" else (12, 13, 16), outline=LINE, width=2)
    d.rounded_rectangle([x0, y0, x1, y0 + 52], 16, fill=PANEL2); d.rectangle([x0, y0 + 36, x1, y0 + 52], fill=PANEL2)
    for i, c in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]): d.ellipse([x0 + 22 + i * 26, y0 + 18, x0 + 38 + i * 26, y0 + 34], fill=c)
    if kind == "editor":
        tw = F(20, "mono").getlength(title) + 40
        d.rectangle([x0 + 110, y0 + 8, x0 + 110 + tw, y0 + 52], fill=PANEL); d.line([x0 + 110, y0 + 8, x0 + 110 + tw, y0 + 8], fill=ACC, width=3)
        d.text((x0 + 130, y0 + 30), title, font=F(20, "mono"), fill=TXT, anchor="lm")
    else:
        d.text(((x0 + x1) / 2, y0 + 26), title, font=F(20, "mono"), fill=DIM, anchor="mm")

# ---------------- syntax highlight (python + shell, small and safe)
KW = set("from import def return for in if else elif while with as not and or is None True False class try except finally lambda pass break continue print".split())
TOK = re.compile(r"(#.*$)|(f?\"[^\"]*\"|f?'[^']*')|(\b\d+\b)|(\b[A-Za-z_]\w*\b)|(\s+)|(.)")
def colorize(line, lang="py"):
    out = []
    if lang == "sh":
        if line.startswith("$ "): return [("$ ", LIME), (line[2:], TXT)]
        if line[:1] == "+" and not line.startswith("+++"): return [(line, LIME)]  # EP05: diff / error colors
        if line[:1] == "-" and not line.startswith("---") and not re.match(r"-[rwxsStT-]{9}", line): return [(line, CORAL)]  # EP07: ls -l file lines stay neutral
        if line.startswith("@@"): return [(line, VIO)]
        if re.match(r"(fatal:|error:|\w+Error:|Author identity unknown|bash: |rm: |rmdir: |mkdir: |cat: |cp: |mv: )", line): return [(line, CORAL)]
        return [(line, DIM if line.startswith("#") else (200, 206, 216))]
    for m in TOK.finditer(line):
        com, st, num, word, sp, other = m.groups()
        if com: out.append((com, (106, 153, 85) if False else (110, 120, 140)))
        elif st: out.append((st, YEL))
        elif num: out.append((num, CORAL))
        elif word:
            nxt = line[m.end():m.end() + 1]
            out.append((word, VIO if word in KW else SKY if nxt == "(" else TXT))
        else: out.append((sp or other, DIM if (other and other in "()[]{}.,:=") else TXT))
    return out

def draw_code(img, x, y, lines, chars, lang, hl=(), lh=44, size=26, a=1.0, cursor=True, t=0, numbers=True, num0=0):
    d = ImageDraw.Draw(img); f = F(size, "mono"); cw = f.getlength("M"); left = chars
    for i, ln in enumerate(lines):
        yy = y + i * lh
        if (i + 1) in hl and left > 0:
            d.rectangle([x - 16, yy - 6, x + 1474, yy + lh - 8], fill=mix(PANEL, ACC, 0.2))
            d.rectangle([x - 16, yy - 6, x - 10, yy + lh - 8], fill=ACC)
        if numbers: d.text((x - 70, yy), f"{i + 1 + num0:>2}", font=f, fill=(78, 86, 102))
        if left <= 0: continue
        show = ln[:max(0, left)]; left -= len(ln) + 1
        cx = x
        for s, c in colorize(show, lang):
            d.text((cx, yy), s, font=f, fill=c); cx += f.getlength(s)
        if cursor and 0 <= left < 1 + 0 and (int(t * 2) % 2 == 0):
            d.rectangle([cx + 2, yy, cx + 4 + cw * 0.12, yy + size + 6], fill=ACC)
    return left

# ---------------- scenes  (each: sc_x(img, v, t, d))
def sc_title(img, v, t, d):
    a = ease(t / 0.6)
    text_a(img, (W / 2, 330), v.get("kicker", "TUTORIAL").upper(), F(30, "SemiBold"), ACC, a, "mm")
    lines = wrap(v["text"], F(96, "Bold"), 1500)
    for i, ln in enumerate(lines): text_a(img, (W / 2, 450 + i * 116 + (1 - a) * 30), ln, F(96, "Bold"), TXT, a, "mm")
    if v.get("sub"): text_a(img, (W / 2, 470 + len(lines) * 116), v["sub"], F(40, "Regular"), DIM, ease((t - 0.5) / 0.6), "mm")

def sc_steps(img, v, t, d):
    text_a(img, (160, 190), v["title"], F(60, "Bold"), TXT, ease(t / 0.4))
    n = len(v["items"]); per = max(0.6, (d * 0.75) / n); rh = min(120, 720 / n); bh = rh - 24; y0 = 330 if n <= 5 else 290
    for i, it in enumerate(v["items"]):
        a = ease((t - 0.4 - i * per) / 0.4); y = y0 + i * rh
        if a <= 0: continue
        dr = ImageDraw.Draw(img); m = (bh - 56) / 2
        dr.rounded_rectangle([160, y, 1760, y + bh], 18, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=2)
        dr.rounded_rectangle([184, y + m, 240, y + m + 56], 12, fill=mix(BG, ACC, a)); dr.text((212, y + bh / 2), str(i + 1), font=F(32, "Bold"), fill=BG, anchor="mm")
        text_a(img, (272, y + bh / 2), it, F(38 if n <= 5 else 34, "Medium"), TXT, a, "lm")

def sc_code(img, v, t, d):
    lines = v["code"].strip("\n").split("\n"); lh = v.get("lh", 46); size = v.get("size", 28)
    v0 = 0
    if v.get("view"):  # show only lines view[0]+1 .. view[1] of a longer file (real line numbers kept)
        v0, v1 = v["view"]; lines = lines[v0:v1]
        v = dict(v, hl=tuple(h - v0 for h in v.get("hl", ())), **({"from": max(0, v["from"] - v0)} if v.get("from") else {}))
    while size > 18 and F(size, "mono").getlength(max(lines, key=len)) > 1440: size -= 1  # keep long lines inside the window
    h = 52 + 50 + len(lines) * lh + 30; y0 = max(150, (H - h) / 2 + 20); box = [160, y0, 1760, y0 + h]
    window(img, box, v.get("file", "rename.py"))
    total = sum(len(l) + 1 for l in lines)
    start = v.get("from", 0)
    if start: start = sum(len(l) + 1 for l in lines[:start])
    typ = v.get("type", True)
    dur = min(d * 0.7, max(1.0, (total - start) / v.get("cps", 38)))
    chars = start + (total - start) * ease(t / dur) if typ else total
    hl = v.get("hl", ()) if t > dur * 0.6 or not typ else ()
    draw_code(img, 270, y0 + 82, lines, int(chars), v.get("lang", "py"), hl, lh, size, t=t, num0=v0)
    if v.get("note"):
        a = ease((t - dur) / 0.5); dr = ImageDraw.Draw(img)
        f = F(32, "SemiBold"); tw = f.getlength(v["note"])
        if a > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, box[3] + 24, W / 2 + tw / 2 + 30, box[3] + 88], 32, fill=mix(BG, ACC, a))
            dr.text((W / 2, box[3] + 56), v["note"], font=f, fill=BG, anchor="mm")

def sc_term(img, v, t, d):
    cmds = v["lines"]; lh = 42
    h = 52 + 40 + len(cmds) * lh + 30; y0 = max(150, (H - h) / 2); box = [200, y0, 1720, y0 + h]
    window(img, box, v.get("title", "Terminal — bash"), kind="term")
    # typed commands ($ ...), instant outputs after each command
    tt, shown = t - 0.3, []
    for ln in cmds:
        if ln.startswith("$ "):
            need = len(ln) / 30.0
            if tt <= 0: break
            k = int(len(ln) * min(1, tt / need)); shown.append(ln[:k]); tt -= need + 0.35
            if k < len(ln): break
        else:
            if tt <= 0: break
            shown.append(ln); tt -= v.get("out_gap", 0.18)
    dr = ImageDraw.Draw(img); f = F(26, "mono")
    for i, ln in enumerate(shown):
        cx = 240
        for s, c in colorize(ln, "sh"): dr.text((cx, y0 + 76 + i * lh), s, font=f, fill=c); cx += f.getlength(s)
    if int(t * 2) % 2 == 0 and shown:
        i = len(shown) - 1; cx = 240 + f.getlength(shown[-1]); dr.rectangle([cx + 2, y0 + 76 + i * lh, cx + 16, y0 + 76 + i * lh + 30], fill=ACC)

def sc_files(img, v, t, d):
    before, after = v["before"], v.get("after")
    text_a(img, (W / 2, 190), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    def col(x, names, hdr, a, accent):
        dr = ImageDraw.Draw(img)
        dr.rounded_rectangle([x, 270, x + 660, 290 + 70 * len(names) + 60], 18, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=2)
        text_a(img, (x + 30, 300), hdr, F(26, "SemiBold"), accent, a)
        for i, n in enumerate(names):
            y = 360 + i * 70; dr.rounded_rectangle([x + 30, y + 8, x + 62, y + 44], 6, fill=mix(BG, accent, a * 0.85))
            text_a(img, (x + 84, y + 26), n, F(28, "mono"), TXT, a, "lm")
    if after:
        col(220, before, v.get("hdr1", "BEFORE"), ease(t / 0.5), CORAL)
        k = ease((t - d * 0.35) / 0.8)
        col(1040, after, v.get("hdr2", "AFTER"), k, ACC)
        if k > 0: text_a(img, (960, 360 + 35 * len(before)), "→", F(80, "monob"), ACC, k, "mm")
    else:
        col(630, before, v.get("hdr1", "FOLDER"), ease(t / 0.5), SKY)

def sc_tip(img, v, t, d):
    a = ease(t / 0.5); dr = ImageDraw.Draw(img)
    lines = wrap(v["text"], F(50, "SemiBold"), 1240); h = 200 + len(lines) * 70
    y0 = (H - h) / 2; dr.rounded_rectangle([300, y0, 1620, y0 + h], 28, fill=mix(BG, PANEL, a), outline=mix(BG, v.get("color", YEL), a), width=3)
    dr.rounded_rectangle([340, y0 + 40, 340 + F(26, "Bold").getlength(v.get("tag", "TIP")) + 40, y0 + 90], 25, fill=mix(BG, v.get("color", YEL), a))
    text_a(img, (360, y0 + 65), v.get("tag", "TIP"), F(26, "Bold"), BG, a, "lm")
    for i, ln in enumerate(lines): text_a(img, (340, y0 + 130 + i * 70), ln, F(50, "SemiBold"), TXT, ease((t - 0.2 - i * 0.15) / 0.5))

def sc_keys(img, v, t, d):
    text_a(img, (W / 2, 300), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    keys = v["keys"]; f = F(54, "SemiBold"); ws = [max(140, f.getlength(k) + 80) for k in keys]
    tot = sum(ws) + 70 * (len(keys) - 1); x = (W - tot) / 2; dr = ImageDraw.Draw(img)
    for i, (k, w) in enumerate(zip(keys, ws)):
        a = ease((t - 0.3 - i * 0.25) / 0.4); press = 8 if (t * 1.2) % 2 < 0.25 and a >= 1 else 0
        dr.rounded_rectangle([x, 470 + 12, x + w, 610 + 12], 22, fill=mix(BG, (10, 11, 14), a))
        dr.rounded_rectangle([x, 470 + press, x + w, 610 + press], 22, fill=mix(BG, PANEL2, a), outline=mix(BG, ACC, a), width=3)
        text_a(img, (x + w / 2, 540 + press), k, f, TXT, a, "mm")
        if i < len(keys) - 1: text_a(img, (x + w + 35, 540), "+", F(54, "Bold"), DIM, a, "mm")
        x += w + 70
    if v.get("sub"): text_a(img, (W / 2, 720), v["sub"], F(36, "Regular"), DIM, ease((t - 1) / 0.5), "mm")

def sc_compare(img, v, t, d):
    text_a(img, (W / 2, 200), v.get("title", ""), F(56, "Bold"), TXT, ease(t / 0.4), "mm")
    for j, (hdr, items, col) in enumerate([(v["left"][0], v["left"][1], CORAL), (v["right"][0], v["right"][1], ACC)]):
        a = ease((t - 0.3 - j * d * 0.3) / 0.5); x = 200 + j * 800; dr = ImageDraw.Draw(img)
        dr.rounded_rectangle([x, 300, x + 720, 860], 24, fill=mix(BG, PANEL, a), outline=mix(BG, col, a), width=3)
        text_a(img, (x + 40, 350), hdr, F(40, "Bold"), col, a)
        for i, it in enumerate(items):
            for k, ln in enumerate(wrap(it, F(32, "Medium"), 600)[:2]):
                text_a(img, (x + 50, 440 + i * 100 + k * 40), ("• " if k == 0 else "  ") + ln, F(32, "Medium"), TXT, a)

def sc_chat(img, v, t, d):
    box = [260, 150, 1660, 960]; window(img, box, v.get("title", "AI assistant"), kind="term")
    dr = ImageDraw.Draw(img); y = 240
    if v.get("badge"):  # EP04: honest label on illustrated replies
        fb = F(22, "SemiBold"); bw = fb.getlength(v["badge"]) + 36
        dr.rounded_rectangle([box[2] - 30 - bw, box[3] - 62, box[2] - 30, box[3] - 22], 20, fill=mix(PANEL, ACC, 0.25), outline=ACC, width=2)
        dr.text((box[2] - 30 - bw / 2, box[3] - 42), v["badge"], font=fb, fill=TXT, anchor="mm")
    for k, (who, msg) in enumerate(v["msgs"]):
        start = k * d * v.get("gap", 0.35); a = ease((t - start) / 0.4)
        if a <= 0: break
        f = F(v.get("size", 30), "Regular"); lines = [l for p in msg.split("\n") for l in (wrap(p, f, 980) or [" "])]
        if who == "ai":
            n = int(sum(len(l) for l in lines) * min(1, (t - start) / max(0.5, d * 0.3))); show = []
            for l in lines:
                show.append(l[:max(0, n)]); n -= len(l)
            lines = [l for l in show if l]
        lh = int(f.size * 1.45)
        bw = max(f.getlength(l) for l in lines) + 60 if lines else 100; bh = 40 + lh * max(1, len(lines))
        x = box[2] - 50 - bw if who == "you" else box[0] + 50
        dr.rounded_rectangle([x, y, x + bw, y + bh], 22, fill=mix(PANEL, mix(PANEL2, ACC, 0.22) if who == "you" else PANEL2, a))
        for i, l in enumerate(lines): text_a(img, (x + 30, y + 22 + i * lh), l, f, TXT, a)
        y += bh + 30

def sc_outro(img, v, t, d):
    a = ease(t / 0.6)
    text_a(img, (W / 2, 330), "NEXT ON SHORTCUT LAB", F(30, "SemiBold"), ACC, a, "mm")
    for i, ln in enumerate(wrap(v["next"], F(72, "Bold"), 1500)): text_a(img, (W / 2, 440 + i * 90), ln, F(72, "Bold"), TXT, a, "mm")
    k = ease((t - 0.8) / 0.5); dr = ImageDraw.Draw(img)
    if k > 0:
        dr.rounded_rectangle([W / 2 - 230, 700, W / 2 + 230, 790], 45, fill=mix(BG, CORAL, k)); text_a(img, (W / 2, 745), "SUBSCRIBE", F(40, "Bold"), (255, 255, 255), k, "mm")
        text_a(img, (W / 2, 850), v.get("sub", "One useful tutorial every day."), F(34, "Regular"), DIM, k, "mm")

# ---- EP02: folder tree (flat "before" list -> nested "after" tree, files dim on the left as they land on the right)
FOLDER_COL = {"Images": SKY, "Documents": YEL, "Audio": VIO, "Video": CORAL, "Archives": LIME}
def icon_folder(dr, x, y, col, a=1.0):
    c = mix(BG, col, a); dr.rounded_rectangle([x, y + 4, x + 14, y + 10], 3, fill=c); dr.rounded_rectangle([x, y + 8, x + 34, y + 30], 5, fill=c)
def icon_file(dr, x, y, col, a=1.0):
    c = mix(BG, col, a); dr.rounded_rectangle([x + 4, y + 2, x + 26, y + 30], 4, outline=c, width=3); dr.line([x + 10, y + 12, x + 20, y + 12], fill=c, width=2); dr.line([x + 10, y + 19, x + 20, y + 19], fill=c, width=2)

def sc_tree(img, v, t, d):
    before, after, root = v.get("before", []), v["after"], v.get("root", "Downloads/")
    text_a(img, (W / 2, 175), v.get("title", ""), F(50, "Bold"), TXT, ease(t / 0.4), "mm")
    dr = ImageDraw.Draw(img)
    rows = []  # (kind, label, color, parent_last)
    for name, kids in after:
        rows.append(("dir", name + "/", FOLDER_COL.get(name, v.get("dircol", DIM)), None))
        for k, f in enumerate(kids): rows.append(("file", f, FOLDER_COL.get(name, DIM), k == len(kids) - 1))
    span = d * v.get("build", 0.55); t0 = v.get("delay", 0.4 if before else 0.2)
    shown = int(len(rows) * max(0, min(1, (t - t0) / span))) if span > 0 else len(rows)
    placed = {r[1] for r in rows[:shown] if r[0] == "file"}
    rh = min(46, 720 / max(1, len(rows) + 1)); fs = int(min(26, rh * 0.68))
    if before:
        a = ease(t / 0.5); x0, x1 = 170, 800; y0 = 250; bh = 70 + len(before) * 46
        dr.rounded_rectangle([x0, y0, x1, y0 + bh], 18, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=2)
        icon_folder(dr, x0 + 28, y0 + 18, CORAL, a); text_a(img, (x0 + 76, y0 + 34), root + "  " + v.get("hdr1", "(messy)"), F(26, "SemiBold"), CORAL, a, "lm")
        for i, n in enumerate(before):
            y = y0 + 70 + i * 46; done = n in placed or n.rstrip("/") + "/" in placed
            col = DIM if done else TXT
            (icon_folder if n.endswith("/") else icon_file)(dr, x0 + 40, y, mix(CORAL, LINE, 0.7 if done else 0), a)
            text_a(img, (x0 + 92, y + 16), n, F(24, "mono"), col, a * (0.45 if done else 1), "lm")
        if shown: text_a(img, (900, y0 + bh / 2), "→", F(80, "monob"), ACC, ease((t - t0) / 0.4), "mm")
        rx0 = 1000
    else:
        rx0 = 600
    if shown <= 0: return
    ry0 = 250 if before else 230; rbh = 70 + len(rows) * rh + 10; rx1 = rx0 + 760
    dr.rounded_rectangle([rx0, ry0, rx1, ry0 + rbh], 18, fill=PANEL, outline=mix(LINE, ACC, 0.5), width=2)
    icon_folder(dr, rx0 + 28, ry0 + 18, ACC); text_a(img, (rx0 + 76, ry0 + 34), root + "  " + v.get("hdr2", "(sorted)"), F(26, "SemiBold"), ACC, 1, "lm")
    for i, (kind, label, col, last) in enumerate(rows[:shown]):
        y = ry0 + 70 + i * rh; k = ease((t - t0 - span * i / len(rows)) / 0.3)
        if kind == "dir":
            icon_folder(dr, rx0 + 36, y + rh / 2 - 17, col, k); text_a(img, (rx0 + 84, y + rh / 2), label, F(fs, "SemiBold"), col, k, "lm")
        else:
            lx = rx0 + 54; dr.line([lx, y - 4, lx, y + (rh / 2 if last else rh)], fill=LINE, width=2); dr.line([lx, y + rh / 2, lx + 30, y + rh / 2], fill=LINE, width=2)
            text_a(img, (lx + 44, y + rh / 2), label, F(fs, "mono"), TXT, k, "lm")

# ---- EP02: mapping table (extension chips -> destination folder), rows appear one by one
def sc_map(img, v, t, d):
    text_a(img, (W / 2, 175), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    rows = v["rows"] + ([(v["default"], ["anything else"], DIM)] if v.get("default") else [])
    n = len(rows); per = max(0.5, d * 0.7 / n); rh = min(110, 760 / n); dr = ImageDraw.Draw(img)
    for i, (folder, exts, col) in enumerate(rows):
        a = ease((t - 0.4 - i * per) / 0.4)
        if a <= 0: continue
        y = 270 + i * rh; x = 200; f = F(30, "mono")
        for e in exts:
            w = f.getlength(e) + 40
            dr.rounded_rectangle([x, y + 14, x + w, y + rh - 26], 14, fill=mix(BG, PANEL2, a), outline=mix(BG, col, a * 0.8), width=2)
            text_a(img, (x + w / 2, y + rh / 2 - 6), e, f, TXT, a, "mm"); x += w + 16
        text_a(img, (1230, y + rh / 2 - 6), "→", F(56, "monob"), col, a, "mm")
        dr.rounded_rectangle([1300, y + 8, 1720, y + rh - 20], 18, fill=mix(BG, mix(PANEL, col, 0.18), a), outline=mix(BG, col, a), width=3)
        icon_folder(dr, 1330, y + rh / 2 - 23, col, a); text_a(img, (1384, y + rh / 2 - 6), folder + "/", F(36, "SemiBold"), TXT, a, "lm")

# ---- EP03: spreadsheet (formula bar typing, colored range references, spilled / filled results, #SPILL! demo)
def _addr(a):
    m = re.match(r"([A-Z]+)(\d+)", a); return ord(m.group(1)) - 65, int(m.group(2))
def _rng(r):
    a, b = (r.split(":") + [r])[:2]; (c0, r0), (c1, r1) = _addr(a), _addr(b); return c0, r0, c1, r1
REFCOL = [(108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 160, 200)]
def sc_sheet(img, v, t, d):
    widths = v.get("widths", [110, 95, 105, 130, 115, 130, 130, 130, 130, 130, 130]); nrows = v.get("rows", 14); rh = v.get("rh", 46)
    hw, hh = 56, 40; tot = hw + sum(widths); scl = min(1.3, 1560 / tot)
    widths = [w * scl for w in widths]; x0 = (W - hw - sum(widths)) / 2; xs = [x0 + hw]; fsc = min(1.12, scl)
    for w in widths: xs.append(xs[-1] + w)
    gy = 236; ys = [gy + hh + i * rh for i in range(nrows + 1)]; gx1 = xs[-1]; gy1 = ys[-1]
    a = ease(t / 0.4); dr = ImageDraw.Draw(img)
    form = v.get("formula", ""); at = v.get("at"); t0 = 0.5 if not v.get("static") else -0.2
    dur = (min(d * 0.4, max(0.8, len(form) / v.get("cps", 20))) if not v.get("static") else 0.01) if form else 0
    typed = int(len(form) * max(0, min(1, (t - t0) / dur))) if form else 0; done = form and t >= t0 + dur
    rv = ease((t - t0 - dur - 0.25) / 0.6) if form else 1  # reveal of results
    # formula bar
    fx0, fx1 = min(x0, (W - 1500) / 2), max(gx1, (W + 1500) / 2)
    dr.rounded_rectangle([fx0, 140, fx1, 200], 10, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=2)
    dr.rectangle([fx0 + 2, 142, fx0 + 110, 198], fill=mix(BG, PANEL2, a)); text_a(img, (fx0 + 56, 170), at or "", F(24, "SemiBold"), TXT, a, "mm")
    text_a(img, (fx0 + 146, 170), "fx", F(26, "Medium"), DIM, a, "mm"); dr.line([fx0 + 180, 150, fx0 + 180, 190], fill=LINE, width=2)
    refs = []  # (start, end, color, range)
    for k, rg in enumerate(v.get("ranges", [])):
        rr = rg[0] if isinstance(rg, tuple) else rg; col = rg[1] if isinstance(rg, tuple) and len(rg) > 1 else REFCOL[k % len(REFCOL)]
        i = form.find(rr.replace("$", "")) if rr.replace("$", "") in form else form.find(rr)
        if i >= 0: refs.append((i, i + len(rr), col, rr))
    fsz = 28
    while fsz > 16 and F(fsz, "mono").getlength(form) > fx1 - fx0 - 220: fsz -= 1
    fm = F(fsz, "mono"); cx = fx0 + 200
    for j, ch in enumerate(form[:typed]):
        col = TXT
        for (i0, i1, c, _) in refs:
            if i0 <= j < i1: col = c
        text_a(img, (cx, 170), ch, fm, col, a, "lm"); cx += fm.getlength(ch)
    if form and not done and int(t * 3) % 2 == 0: dr.rectangle([cx + 2, 154, cx + 5, 186], fill=ACC)
    # grid
    dr.rectangle([x0, gy, gx1, gy1], fill=mix(BG, (20, 22, 27), a))
    dr.rectangle([x0, gy, gx1, gy + hh], fill=mix(BG, PANEL2, a)); dr.rectangle([x0, gy, x0 + hw, gy1], fill=mix(BG, PANEL2, a))
    for rnum in v.get("mark", []):
        k = rv if form else a; dr.rectangle([xs[0], ys[rnum - 1], gx1, ys[rnum]], fill=mix((20, 22, 27), mix(BG, v.get("markcol", YEL), 0.2), k))
    for (i0, i1, c, rr) in refs:
        if i0 >= 0 and typed >= i1 and not done or (done and rv < 1 and i0 >= 0):
            c0, r0, c1, r1 = _rng(rr); dr.rectangle([xs[c0], ys[r0 - 1], xs[c1 + 1], ys[r1]], fill=mix((20, 22, 27), c, 0.16))
    for i, x in enumerate(xs): dr.line([x, gy, x, gy1], fill=mix(BG, LINE, a), width=1)
    for i, y in enumerate([gy] + ys): dr.line([x0, y, gx1, y], fill=mix(BG, LINE, a), width=1)
    fl, fs, fh = F(22, "SemiBold"), F(23 * fsc, "Regular"), F(23 * fsc, "SemiBold")
    for c in range(len(widths)): text_a(img, ((xs[c] + xs[c + 1]) / 2, gy + hh / 2), chr(65 + c), fl, DIM, a, "mm")
    for r in range(1, nrows + 1): text_a(img, (x0 + hw / 2, (ys[r - 1] + ys[r]) / 2), str(r), fl, DIM, a, "mm")
    def put(c, r, val, col=TXT, font=None, alpha=1.0):
        if r > nrows or c >= len(widths): return
        y = (ys[r - 1] + ys[r]) / 2; f = font or (fh if r == 1 else fs); s = str(val)
        if (isinstance(val, (int, float)) and not isinstance(val, bool)) or re.match(r"\d{4}-\d\d-\d\d$", s): text_a(img, (xs[c + 1] - 12, y), s, f, col, a * alpha, "rm")
        else: text_a(img, (xs[c] + 12, y), s, f, col, a * alpha, "lm")
    for k, val in v.get("cells", {}).items():
        c, r = _addr(k); put(c, r, val, ACC if k == v.get("block") else TXT)
    for (i0, i1, c, rr) in refs:  # range borders while editing (Excel style)
        if i0 >= 0 and typed >= i1 and (not done or rv < 1):
            c0, r0, c1, r1 = _rng(rr); dr.rectangle([xs[c0], ys[r0 - 1], xs[c1 + 1], ys[r1]], outline=c, width=3)
    if at:
        ac, ar = _addr(at)
        if v.get("block"):
            bc, br = _addr(v["block"]); dr.rectangle([xs[bc], ys[br - 1], xs[bc + 1], ys[br]], outline=CORAL, width=3)
        if form and not done:  # edit mode: formula shown in the cell, overflowing to the right
            s = form[:typed]; f = F(21 * fsc, "mono"); tw = f.getlength(s) + 24
            dr.rectangle([xs[ac], ys[ar - 1], max(xs[ac + 1], xs[ac] + tw), ys[ar]], fill=(20, 22, 27))
            text_a(img, (xs[ac] + 10, (ys[ar - 1] + ys[ar]) / 2), s, f, TXT, a, "lm")
        elif v.get("error"):
            put(ac, ar, v["error"], CORAL, F(23 * fsc, "SemiBold"), rv)
            if v.get("ghost") and rv > 0:
                c0, r0, c1, r1 = _rng(v["ghost"]); X0, Y0, X1, Y1 = xs[c0], ys[r0 - 1], xs[c1 + 1], ys[r1]
                for xx in range(int(X0), int(X1), 18): dr.line([xx, Y0, min(xx + 9, X1), Y0], fill=CORAL, width=3); dr.line([xx, Y1, min(xx + 9, X1), Y1], fill=CORAL, width=3)
                for yy in range(int(Y0), int(Y1), 18): dr.line([X0, yy, X0, min(yy + 9, Y1)], fill=CORAL, width=3); dr.line([X1, yy, X1, min(yy + 9, Y1)], fill=CORAL, width=3)
        else:
            res = v.get("result", []); oc, orow = _addr(v.get("out", at)); n = len(res)
            for i, row in enumerate(res):
                k = ease((rv * (n + 2) - i) / 2) if n else 0
                if k <= 0: continue
                for j, val in enumerate(row if isinstance(row, (list, tuple)) else [row]): put(oc + j, orow + i, val, ACC if (orow + i == 1 and v.get("hdr")) else v.get("rescol", TXT), fh if orow + i == 1 else fs, k)
            if rv > 0.6 and res and not v.get("fill"):
                wcols = max(len(r) if isinstance(r, (list, tuple)) else 1 for r in res)
                dr.rectangle([xs[oc], ys[orow - 1], xs[min(len(widths), oc + wcols)], ys[min(nrows, orow + n - 1)]], outline=SKY, width=2)
        dr.rectangle([xs[ac] - 1, ys[ar - 1] - 1, xs[ac + 1] + 1, ys[ar] + 1], outline=ACC, width=4)
    if v.get("note"):
        k = ease((t - t0 - dur - 0.8) / 0.5) if form else ease((t - 0.8) / 0.5); f = F(32, "SemiBold"); tw = f.getlength(v["note"])
        if k > 0:
            ny = min(gy1 + 24, H - 100); dr.rounded_rectangle([W / 2 - tw / 2 - 30, ny, W / 2 + tw / 2 + 30, ny + 62], 31, fill=mix(BG, v.get("notecol", ACC), k))
            dr.text((W / 2, ny + 31), v["note"], font=f, fill=BG, anchor="mm")

# ---- EP03: function syntax card (argument rows appear one by one, example formula colored by argument)
def sc_args(img, v, t, d):
    text_a(img, (160, 175), v.get("title", ""), F(30, "SemiBold"), ACC, ease(t / 0.4))
    fn = v["fn"]; f0 = F(64, "monob"); text_a(img, (160, 260), "=" + fn + "(", f0, TXT, ease(t / 0.4), "lm")
    args = v["args"]; n = len(args); per = max(0.5, d * 0.55 / n); rh = min(104, 470 / n); dr = ImageDraw.Draw(img)
    lx = max(720, max(F(32, "mono").getlength(a[0]) + 48 + (130 if (len(a) > 2 and a[2]) else 0) for a in args) + 250)
    for i, (name, label, *opt) in enumerate(args):
        k = ease((t - 0.5 - i * per) / 0.4); col = REFCOL[i % len(REFCOL)]
        if k <= 0: continue
        y = 330 + i * rh; optional = bool(opt and opt[0]); f = F(32, "mono"); w = f.getlength(name) + 48
        dr.rounded_rectangle([200, y, 200 + w, y + rh - 22], 14, fill=mix(BG, mix(PANEL, col, 0.22), k), outline=mix(BG, col, k * (0.5 if optional else 1)), width=3)
        text_a(img, (224, y + (rh - 22) / 2), name, f, col, k, "lm")
        text_a(img, (lx, y + (rh - 22) / 2), label, F(34, "Medium"), TXT if not optional else DIM, k, "lm")
        if optional: text_a(img, (200 + w + 18, y + (rh - 22) / 2), "optional", F(22, "Medium"), DIM, k, "lm")
    if v.get("example"):
        k = ease((t - 0.5 - n * per - 0.3) / 0.5)
        if k > 0:
            ex = v["example"]; fe = F(34, "mono")
            while fe.size > 20 and fe.getlength(ex) > 1500: fe = F(fe.size - 1, "mono")
            yb = 330 + n * rh + 30; dr.rounded_rectangle([160, yb, 1760, yb + 90], 16, fill=mix(BG, PANEL, k), outline=mix(BG, LINE, k), width=2)
            spans = []
            for i, part in enumerate(v.get("parts", [])):
                j = ex.find(part)
                if j >= 0: spans.append((j, j + len(part), REFCOL[i % len(REFCOL)]))
            cx = 960 - fe.getlength(ex) / 2
            for j, ch in enumerate(ex):
                col = TXT
                for (a0, a1, c) in spans:
                    if a0 <= j < a1: col = c
                text_a(img, (cx, yb + 45), ch, fe, col, k, "lm"); cx += fe.getlength(ch)

# ---- EP04: prompt anatomy (a vague "before" prompt, then the better prompt growing segment by segment, each part colored + labeled)
def sc_prompt(img, v, t, d):
    dr = ImageDraw.Draw(img); segs = v["segs"]; n = len(segs)
    if "_oy" not in v:  # vertical centering, computed once per scene (layout estimate)
        f0 = F(v.get("size", 36), "Regular"); words = sum(f0.getlength(sg[0] + " ") for sg in segs); nl = words / (1290 - 160 - 80) + (n * 0.5 if v.get("breaks") else 0.5)
        bh0 = max(70 + int(nl + 0.5) * int(v.get("size", 36) * 1.55) + 30, 20 + n * 76)
        tot = 55 + (135 if v.get("before") else 0) + bh0 + (92 if v.get("note") else 0); v["_oy"] = max(0, (H - 150 - 60 - tot) / 2 - 20)
    oy = v["_oy"]
    text_a(img, (160, 150 + oy), v.get("title", ""), F(30, "SemiBold"), ACC, ease(t / 0.4))
    y = 205 + oy
    if v.get("before"):
        a = ease(t / 0.4); fb = F(34, "Regular")
        dr.rounded_rectangle([160, y, 1760, y + 100], 18, fill=mix(BG, PANEL, a), outline=mix(BG, CORAL, a * 0.7), width=2)
        dr.rounded_rectangle([190, y + 30, 330, y + 70], 20, fill=mix(BG, CORAL, a)); text_a(img, (260, y + 50), v.get("hdr1", "BEFORE"), F(22, "Bold"), BG, a, "mm")
        text_a(img, (360, y + 50), v["before"], fb, mix(BG, TXT, a), 1, "lm")
        if v.get("strike") and t > v["strike"]:
            k = ease((t - v["strike"]) / 0.4); dr.line([360, y + 52, 360 + fb.getlength(v["before"]) * k, y + 52], fill=CORAL, width=4)
        y += 135
    size = v.get("size", 36); f = F(size, "Regular"); lh = int(size * 1.55); bx0, bx1 = 160, 1290; maxw = bx1 - bx0 - 80
    toks = []
    for i, seg in enumerate(segs):
        for w in seg[0].split(" "):
            if w: toks.append((w, i))
        if v.get("breaks"): toks.append(("\n", i))
    lines, cur, cw = [], [], 0
    for w, i in toks:
        if w == "\n":
            if cur: lines.append(cur)
            cur, cw = [], 0; continue
        ww = f.getlength(w + " ")
        if cw + ww > maxw and cur: lines.append(cur); cur, cw = [], 0
        cur.append((w, i)); cw += ww
    if cur: lines.append(cur)
    grow = v.get("grow", True); per = max(0.5, d * v.get("span", 0.6) / n); t0 = v.get("delay", 0.6 if v.get("before") else 0.3)
    ks = [ease((t - t0 - i * per) / 0.45) if grow else ease(t / 0.4) for i in range(n)]
    bh = 70 + len(lines) * lh + 30; bh = max(bh, 10 + n * 76 + 10)
    dr.rounded_rectangle([bx0, y, bx1, y + bh], 18, fill=PANEL, outline=mix(LINE, ACC, 0.6), width=2)
    hdr = v.get("hdr2", "PROMPT"); fh = F(22, "Bold"); hw = fh.getlength(hdr) + 40
    dr.rounded_rectangle([bx0 + 30, y + 24, bx0 + 30 + hw, y + 62], 19, fill=ACC); dr.text((bx0 + 30 + hw / 2, y + 43), hdr, font=fh, fill=BG, anchor="mm")
    cols = [s[2] if len(s) > 2 else REFCOL[i % len(REFCOL)] for i, s in enumerate(segs)]
    stop = False
    for li, ln in enumerate(lines):
        cx = bx0 + 40; yy = y + 84 + li * lh
        for w, i in ln:
            if ks[i] <= 0: stop = True; break
            dr.text((cx, yy), w, font=f, fill=mix(PANEL, cols[i], ks[i]))
            dr.line([cx, yy + size + 10, cx + f.getlength(w + " "), yy + size + 10], fill=mix(PANEL, cols[i], ks[i] * 0.55), width=3)
            cx += f.getlength(w + " ")
        if stop: break
    for i, s in enumerate(segs):  # label chips on the right
        k = ks[i]
        if k <= 0 or not s[1]: continue
        ly = y + 10 + i * 76; fl = F(28, "SemiBold")
        dr.rounded_rectangle([1330, ly, 1760, ly + 60], 16, fill=mix(BG, mix(PANEL, cols[i], 0.2), k), outline=mix(BG, cols[i], k), width=2)
        dr.ellipse([1352, ly + 20, 1372, ly + 40], fill=mix(BG, cols[i], k)); text_a(img, (1392, ly + 30), s[1], fl, mix(BG, TXT, k), 1, "lm")
    if v.get("note"):
        k = ease((t - t0 - n * per - 0.3) / 0.5) if grow else ease((t - 0.8) / 0.5); fn = F(32, "SemiBold"); tw = fn.getlength(v["note"])
        if k > 0:
            ny = min(y + bh + 30, H - 100); dr.rounded_rectangle([W / 2 - tw / 2 - 30, ny, W / 2 + tw / 2 + 30, ny + 62], 31, fill=mix(BG, v.get("notecol", ACC), k))
            dr.text((W / 2, ny + 31), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP04: flow (a big task split into small steps; boxes + arrows appear in order, a check mark between steps)
def sc_flow(img, v, t, d):
    text_a(img, (W / 2, 210), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    st = v["steps"]; n = len(st); gap = 90; bw = (1640 - gap * (n - 1)) / n; y0, y1 = 400, 700; dr = ImageDraw.Draw(img)
    per = max(0.6, d * 0.65 / n); cols = v.get("cols", [SKY, VIO, YEL, LIME, CORAL])
    for i, s in enumerate(st):
        k = ease((t - 0.5 - i * per) / 0.45)
        if k <= 0: continue
        x = 140 + i * (bw + gap); c = cols[i % len(cols)]; lift = (1 - k) * 30
        dr.rounded_rectangle([x, y0 + lift, x + bw, y1 + lift], 22, fill=mix(BG, PANEL, k), outline=mix(BG, c, k), width=3)
        dr.ellipse([x + bw / 2 - 34, y0 - 34 + lift, x + bw / 2 + 34, y0 + 34 + lift], fill=mix(BG, c, k)); dr.text((x + bw / 2, y0 + lift), str(i + 1), font=F(36, "Bold"), fill=BG, anchor="mm")
        fs = 34; ls = wrap(s, F(fs, "SemiBold"), bw - 50)
        while len(ls) > 4 and fs > 24: fs -= 2; ls = wrap(s, F(fs, "SemiBold"), bw - 50)
        for j, l in enumerate(ls): text_a(img, (x + bw / 2, (y0 + y1) / 2 + 10 + lift + (j - (len(ls) - 1) / 2) * fs * 1.4), l, F(fs, "SemiBold"), mix(BG, TXT, k), 1, "mm")
        if i < n - 1:
            ka = ease((t - 0.5 - i * per - per * 0.6) / 0.3)
            if ka > 0:
                ax = x + bw + gap / 2; text_a(img, (ax, (y0 + y1) / 2), "→", F(56, "monob"), mix(BG, c, ka), 1, "mm")
                if v.get("check"):
                    text_a(img, (ax, y1 + 70), "✓", F(44, "monob"), mix(BG, LIME, ka), 1, "mm")
    if v.get("check"):
        k = ease((t - 0.5 - per) / 0.5)
        if k > 0: text_a(img, (W / 2, y1 + 140), "✓ = you check the result before the next step", F(28, "mono"), mix(BG, DIM, k), 1, "mm")
    if v.get("note"):
        k = ease((t - 0.5 - n * per) / 0.5); fn = F(32, "SemiBold"); tw = fn.getlength(v["note"])
        if k > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 920, W / 2 + tw / 2 + 30, 982], 31, fill=mix(BG, ACC, k)); dr.text((W / 2, 951), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP05: stage (Git's three areas: your folder -> staging area -> history; file chips slide across on "git add" / "git commit")
def sc_stage(img, v, t, d):
    text_a(img, (W / 2, 190), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    names = v.get("areas", ["Your folder", "Staging area", "History"]); subs = v.get("subs", ["where you edit", "what goes in the next save", "saved versions (commits)"])
    cols = [SKY, YEL, LIME]; bw, gap, y0, y1 = 420, 200, 300, 820; x0 = (W - 3 * bw - 2 * gap) / 2; dr = ImageDraw.Draw(img)
    for i in range(3):
        a = ease((t - 0.2 - i * 0.25) / 0.45); x = x0 + i * (bw + gap); c = cols[i]
        if a <= 0: continue
        dr.rounded_rectangle([x, y0, x + bw, y1], 24, fill=mix(BG, PANEL, a), outline=mix(BG, c, a if i == v.get("focus", i) else a * 0.45), width=3)
        text_a(img, (x + bw / 2, y0 + 50), names[i], F(36, "Bold"), c, a, "mm")
        text_a(img, (x + bw / 2, y0 + 95), subs[i], F(24, "Regular"), DIM, a, "mm")
    for j, lab in enumerate(v.get("arrows", ["git add", "git commit"])):
        a = ease((t - 0.9 - j * 0.3) / 0.4)
        if a <= 0 or not lab: continue
        ax = x0 + (j + 1) * bw + j * gap + gap / 2; on = v.get("hl") in (None, j)
        text_a(img, (ax, (y0 + y1) / 2 - 10), "→", F(64, "monob"), cols[j + 1] if on else DIM, a, "mm")
        fl = F(24, "monob"); lw = fl.getlength(lab) + 28
        dr.rounded_rectangle([ax - lw / 2, (y0 + y1) / 2 + 40, ax + lw / 2, (y0 + y1) / 2 + 84], 22, fill=mix(BG, cols[j + 1] if on else LINE, a))
        text_a(img, (ax, (y0 + y1) / 2 + 62), lab, fl, BG if on else TXT, a, "mm")
    per = max(0.8, d * 0.6 / max(1, len(v.get("chips", []))))
    for k, ch in enumerate(v.get("chips", [])):  # (label, from_area, to_area)
        lab, fa, ta = ch[:3]; m = ease((t - 1.5 - k * per) / 0.9) if fa != ta else 1
        a = ease((t - 1.0) / 0.4)
        if a <= 0: continue
        cx = x0 + bw / 2 + (fa + (ta - fa) * m) * (bw + gap); cy = y0 + 180 + k * 92 - math.sin(math.pi * m) * 40 * (fa != ta)
        c = cols[int(round(fa + (ta - fa) * m))]; f = F(26, "mono"); w2 = f.getlength(lab) / 2 + 26
        dr.rounded_rectangle([cx - w2, cy, cx + w2, cy + 64], 14, fill=mix(BG, mix(PANEL2, c, 0.25), a), outline=mix(BG, c, a), width=2)
        text_a(img, (cx, cy + 32), lab, f, TXT, a, "mm")
    if v.get("note"):
        k = ease((t - d * 0.55) / 0.5); fn = F(32, "SemiBold"); tw = fn.getlength(v["note"])
        if k > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 880, W / 2 + tw / 2 + 30, 942], 31, fill=mix(BG, ACC, k)); dr.text((W / 2, 911), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP05: timeline (commit history as save points on a line; HEAD/branch pill, optional "go back" arc and a side branch)
def sc_timeline(img, v, t, d):
    text_a(img, (W / 2, 180), v.get("title", ""), F(52, "Bold"), TXT, ease(t / 0.4), "mm")
    cm = v["commits"]; n = len(cm); br = v.get("branch"); ly = v.get("y", 600 if not br else 680)
    sp = min(340, 1500 / max(1, n - 1 + (len(br[1]) if br else 0))); x0 = (W - sp * (n - 1 + (len(br[1]) if br else 0))) / 2; dr = ImageDraw.Draw(img)
    per = max(0.35, d * v.get("span", 0.4) / n); fh, fm = F(24, "monob"), F(26, "Medium")
    pts = []
    for i, (h, msg) in enumerate(cm):
        a = ease((t - 0.4 - i * per) / 0.4); x = x0 + i * sp; pts.append(x)
        if a <= 0: continue
        if i: dr.line([x - sp + 30, ly, x - 30, ly], fill=mix(BG, LINE, a), width=6)
        bad = i in v.get("bad", ()); c = CORAL if bad else ACC
        r = 26 + 6 * math.sin(math.pi * min(1, (t - 0.4 - i * per) / 0.4))
        dr.ellipse([x - r, ly - r, x + r, ly + r], fill=mix(BG, c, a), outline=BG, width=4)
        text_a(img, (x, ly - 62), h, fh, mix(BG, c, a), 1, "mm")
        for j, l in enumerate(wrap(msg, fm, sp - 30)[:3]): text_a(img, (x, ly + 62 + j * 36), l, fm, mix(BG, TXT, a), 1, "mm")
    if br:
        fi, bc, bname = br; ky = ly - 230
        for k, (h, msg) in enumerate(bc):
            a = ease((t - 0.4 - (n + k) * per) / 0.4); x = x0 + (fi + 1 + k) * sp
            if a <= 0: continue
            px, py = (x0 + fi * sp, ly) if k == 0 else (x - sp, ky)
            dr.line([px + 20, py - (20 if k == 0 else 0), x - 28, ky], fill=mix(BG, VIO, a), width=6)
            dr.ellipse([x - 26, ky - 26, x + 26, ky + 26], fill=mix(BG, VIO, a), outline=BG, width=4)
            text_a(img, (x, ky - 96), h, fh, mix(BG, VIO, a), 1, "mm"); text_a(img, (x, ky - 54), msg, fm, mix(BG, TXT, a), 1, "mm")
            if k == len(bc) - 1:
                fl = F(24, "Bold"); lw = fl.getlength(bname) + 30
                dr.rounded_rectangle([x - lw / 2, ky - 174, x + lw / 2, ky - 134], 20, fill=mix(BG, VIO, a)); text_a(img, (x, ky - 154), bname, fl, BG, a, "mm")
    hi = v.get("head", n - 1); a = ease((t - 0.4 - n * per) / 0.4)
    if a > 0 and hi is not None and hi < len(pts):
        x = pts[hi]; fl = F(24, "Bold"); lab = v.get("label", "main"); lw = fl.getlength(lab) + 30
        dr.rounded_rectangle([x - lw / 2, ly - 150, x + lw / 2, ly - 110], 20, fill=mix(BG, SKY, a)); text_a(img, (x, ly - 130), lab, fl, BG, a, "mm")
    if v.get("back") is not None:  # dashed arc from the head commit back to an older one
        k = ease((t - 0.6 - n * per) / 0.9)
        if k > 0:
            xa, xb = pts[hi], pts[v["back"]]; cy = ly + 250; ay = ly + 150; rx = (xa - xb) / 2; mx = (xa + xb) / 2
            steps = int(60 * k)
            for s in range(0, steps, 2):
                th0, th1 = math.pi * s / 60, math.pi * (s + 1) / 60
                dr.line([mx + rx * math.cos(th0), ay + (cy - ay) * math.sin(th0), mx + rx * math.cos(th1), ay + (cy - ay) * math.sin(th1)], fill=YEL, width=5)
            if k >= 1:
                text_a(img, (xb, ay - 4), "▲", F(30, "monob"), YEL, 1, "mm")
                fl = F(28, "monob"); lab = v.get("back_label", ""); lw = fl.getlength(lab) + 36
                dr.rounded_rectangle([mx - lw / 2, cy + 30, mx + lw / 2, cy + 84], 27, fill=mix(BG, YEL, 0.25), outline=YEL, width=2); text_a(img, (mx, cy + 57), lab, fl, TXT, 1, "mm")
    if v.get("note"):
        k = ease((t - d * 0.6) / 0.5); fn = F(32, "SemiBold"); tw = fn.getlength(v["note"])
        if k > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 930, W / 2 + tw / 2 + 30, 992], 31, fill=mix(BG, v.get("notecol", ACC), k)); dr.text((W / 2, 961), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP06: figure window - shows a REAL chart PNG produced by the episode's code, wiped in left to right, then numbered callouts
_imc = {}
def sc_figure(img, v, t, d):
    if v["img"] not in _imc: _imc[v["img"]] = Image.open(v["img"]).convert("RGBA")
    src = _imc[v["img"]]; maxw, maxh = v.get("maxw", 1440), v.get("maxh", 720)
    sc = min(maxw / src.width, maxh / src.height); iw, ih = int(src.width * sc), int(src.height * sc)
    top = 150 if v.get("title") is None else 210
    bw, bh = iw + 60, ih + 52 + 60; x0 = (W - bw) // 2; y0 = top + max(0, (H - 60 - top - bh) // 2)
    if v.get("title"): text_a(img, (W / 2, 175), v["title"], F(44, "Bold"), TXT, ease(t / 0.4), "mm")
    window(img, [x0, y0, x0 + bw, y0 + bh], v.get("win", "Figure 1"), kind="term")
    pic = src.resize((iw, ih), Image.LANCZOS); px, py = x0 + 30, y0 + 52 + 30
    k = ease((t - 0.3) / max(0.6, d * v.get("wipe", 0.35)))
    if v.get("fade"): pic.putalpha(int(255 * k)); img.alpha_composite(pic, (px, py))
    elif k > 0:
        cw = max(1, int(iw * k)); img.alpha_composite(pic.crop((0, 0, cw, ih)), (px, py))
        if k < 1: ImageDraw.Draw(img).rectangle([px + cw - 2, py, px + cw + 2, py + ih], fill=ACC)
    dr = ImageDraw.Draw(img)
    for i, co in enumerate(v.get("callouts", [])):  # (fx, fy, label[, side]) fx, fy = fraction of the picture; side "l"/"r" forces the label side
        fx, fy, lab = co[:3]; side = co[3] if len(co) > 3 else ("r" if fx < 0.6 else "l")
        a = ease((t - 0.5 - d * v.get("wipe", 0.35) - i * 0.9) / 0.4)
        if a <= 0: continue
        cx, cy = px + fx * iw, py + fy * ih; r = 26
        dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=mix(BG, ACC, a), width=5)
        fl = F(28, "SemiBold"); lw = fl.getlength(lab) + 70; lx = cx + 40 if side == "r" else cx - 40 - lw; ly = cy - 80 if fy > 0.25 else cy + 40
        dr.line([cx, cy, lx + (0 if side == "r" else lw), ly + 22], fill=mix(BG, ACC, a), width=3)
        dr.rounded_rectangle([lx, ly, lx + lw, ly + 44], 22, fill=mix(BG, ACC, a))
        dr.ellipse([lx + 8, ly + 6, lx + 40, ly + 38], fill=BG); dr.text((lx + 24, ly + 22), str(i + 1), font=F(22, "Bold"), fill=ACC, anchor="mm")
        dr.text((lx + 52, ly + 22), lab, font=fl, fill=BG, anchor="lm")
    if v.get("note"):
        a = ease((t - d * 0.6) / 0.5); fn = F(32, "SemiBold"); tw = fn.getlength(v["note"])
        if a > 0:
            ny = min(H - 80, y0 + bh + 20)
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, ny, W / 2 + tw / 2 + 30, ny + 60], 30, fill=mix(BG, ACC, a)); dr.text((W / 2, ny + 30), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP07: nav - folder tree on the left, a "YOU ARE HERE" pin that jumps between folders as each cd command is typed (right column), live pwd bar
def sc_nav(img, v, t, d):
    tree, steps = v["tree"], v["steps"]  # tree: [(depth, name)], steps: [(cmd, tree_index)]
    text_a(img, (W / 2, 175), v.get("title", ""), F(48, "Bold"), TXT, ease(t / 0.4), "mm")
    dr = ImageDraw.Draw(img); x0, y0, rh = 200, 250, 62; bx1 = 900
    dr.rounded_rectangle([x0 - 30, y0 - 30, bx1, y0 + len(tree) * rh + 10], 18, fill=PANEL, outline=LINE, width=2)
    t0 = 0.6; per = max(1.2, (d * v.get("span", 0.75) - t0) / max(1, len(steps)))
    k = int(max(0, min(len(steps), (t - t0) / per + 1))) if t > t0 else 0
    cur = steps[k - 1][1] if k else v.get("start", 0)
    prev = steps[k - 2][1] if k >= 2 else v.get("start", 0)
    mv = ease(((t - t0) - (k - 1) * per) / 0.45) if k else 1
    for i, (dep, name) in enumerate(tree):
        y = y0 + i * rh; x = x0 + dep * 56
        if dep: dr.line([x - 34, y - rh / 2 + 14, x - 34, y + 16], fill=LINE, width=2); dr.line([x - 34, y + 16, x - 8, y + 16], fill=LINE, width=2)
        on = i == cur
        isdir = name.endswith("/")
        (icon_folder if isdir else icon_file)(dr, x, y, ACC if on else (SKY if isdir else DIM))
        dr.text((x + 48, y + 17), name, font=F(30, "SemiBold" if on else "Medium"), fill=TXT if on else (200, 206, 216), anchor="lm")
    # pin glides from prev to cur
    py = y0 + (prev + (cur - prev) * mv) * rh + 17
    lab = "YOU ARE HERE"; fl = F(22, "Bold"); lw = fl.getlength(lab) + 40
    px = bx1 - lw - 30
    dr.rounded_rectangle([px, py - 22, px + lw, py + 22], 22, fill=ACC); dr.polygon([(px - 16, py), (px + 2, py - 12), (px + 2, py + 12)], fill=ACC)
    dr.text((px + lw / 2, py), lab, font=fl, fill=BG, anchor="mm")
    # right column: typed commands
    cx = 990; f = F(30, "mono")
    for j, (cmd, idx) in enumerate(steps[:k]):
        a = ease(((t - t0) - j * per) / 0.35); y = y0 + j * 84
        col = ACC if j == k - 1 else DIM
        dr.rounded_rectangle([cx, y - 6, 1740, y + 58], 14, fill=mix(BG, PANEL2, a), outline=mix(BG, col, a), width=2)
        text_a(img, (cx + 24, y + 26), "$", F(30, "monob"), mix(BG, LIME, a), a, "lm")
        text_a(img, (cx + 60, y + 26), cmd, f, mix(BG, TXT, a), a, "lm")
    # pwd bar
    path = v.get("paths", {}).get(cur, "")
    if path:
        fy = H - 150; tw = F(30, "mono").getlength("pwd → " + path)
        dr.rounded_rectangle([W / 2 - tw / 2 - 40, fy, W / 2 + tw / 2 + 40, fy + 64], 32, fill=PANEL2, outline=ACC, width=2)
        dr.text((W / 2 - tw / 2, fy + 32), "pwd", font=F(30, "monob"), fill=ACC, anchor="lm")
        dr.text((W / 2 - tw / 2 + F(30, "mono").getlength("pwd "), fy + 32), "→", font=F(30, "monob"), fill=DIM, anchor="lm")
        dr.text((W / 2 - tw / 2 + F(30, "mono").getlength("pwd → "), fy + 32), path, font=F(30, "mono"), fill=TXT, anchor="lm")

# ---- EP07: cards - cheat-sheet grid of command cards (mono command + plain-English meaning), popping in one by one; hl = index to glow
def sc_cards(img, v, t, d):
    items = v["items"]; cols = v.get("cols", 3); n = len(items); rows = (n + cols - 1) // cols
    text_a(img, (W / 2, 175), v.get("title", ""), F(50, "Bold"), TXT, ease(t / 0.4), "mm")
    gw, gh = 1640, min(760, rows * (260 if rows == 1 else 190)); cw, ch = gw / cols, gh / rows; x0 = (W - gw) / 2; y0 = 250
    span = d * v.get("span", 0.6); dr = ImageDraw.Draw(img)
    for i, (cmd, mean) in enumerate(items):
        a = ease((t - 0.4 - span * i / n) / 0.35)
        if a <= 0: continue
        r, c = divmod(i, cols); bx = x0 + c * cw + 12; by = y0 + r * ch + 12 + (1 - a) * 30
        glow = v.get("hl") == i
        col = v.get("colors", [ACC])[i % len(v.get("colors", [ACC]))]
        dr.rounded_rectangle([bx, by, bx + cw - 24, by + ch - 24], 18, fill=mix(BG, mix(PANEL, col, 0.18) if glow else PANEL, a), outline=mix(BG, col if glow else LINE, a), width=3 if glow else 2)
        dr.rectangle([bx + 2, by + 16, bx + 8, by + ch - 40], fill=mix(BG, col, a))
        fs = 34
        while F(fs, "monob").getlength(cmd) > cw - 80 and fs > 20: fs -= 2
        text_a(img, (bx + 30, by + 26), cmd, F(fs, "monob"), mix(BG, col, a), a)
        for k2, ln in enumerate(wrap(mean, F(26, "Medium"), cw - 80)[:2]):
            text_a(img, (bx + 30, by + 26 + fs + 18 + k2 * 36), ln, F(26, "Medium"), mix(BG, (200, 206, 216), a), a)

# ---- EP08: funnel - the query string on top, clause by clause; under it one column per stage with the rows that survive it
def sc_funnel(img, v, t, d):
    stages = v["stages"]; n = len(stages); span = d * v.get("span", 0.75); dr = ImageDraw.Draw(img)
    text_a(img, (W / 2, 150), v.get("title", ""), F(44, "Bold"), TXT, ease(t / 0.4), "mm")
    cur = max(0, min(n - 1, int((t - 0.4) / (span / n)))) if t > 0.4 else -1
    # query string, current clause highlighted
    fq = F(30, "mono"); full = "".join(s["clause"] for s in stages); x = W / 2 - fq.getlength(full) / 2; yq = 232
    dr.rounded_rectangle([x - 30, yq - 34, x + fq.getlength(full) + 30, yq + 34], 16, fill=PANEL, outline=LINE, width=2)
    for i, s in enumerate(stages):
        c = s["clause"]; wl = fq.getlength(c)
        lw = fq.getlength(c[:len(c) - len(c.lstrip())])
        if i == cur and c.strip(): dr.rounded_rectangle([x + lw - 4, yq - 24, x + wl + 4, yq + 24], 8, fill=mix(PANEL, ACC, 0.28))
        text_a(img, (x, yq), c, fq, ACC if i == cur else (TXT if i < cur else DIM), ease(t / 0.4), "lm"); x += wl
    gw = 1760; cw = gw / n; x0 = (W - gw) / 2; y0 = 300; rh = 38; fr = F(24, "Medium"); fm = F(24, "mono")
    for i, s in enumerate(stages):
        a = ease((t - 0.4 - span * i / n) / 0.4)
        if a <= 0: continue
        bx = x0 + i * cw + 14; bw = cw - 70; col = s.get("color", ACC)
        dr.rounded_rectangle([bx, y0, bx + bw, y0 + 60], 14, fill=mix(BG, mix(PANEL, col, 0.25), a), outline=mix(BG, col, a), width=2)
        text_a(img, (bx + bw / 2, y0 + 30), s["label"], F(26, "SemiBold"), col, a, "mm")
        rows = s["rows"]
        for k, row in enumerate(rows):
            ka = ease((t - 0.6 - span * i / n - k * 0.04) / 0.3) * a
            if ka <= 0: continue
            ry = y0 + 78 + k * rh; dr.rounded_rectangle([bx, ry, bx + bw, ry + rh - 6], 8, fill=mix(BG, PANEL if k % 2 == 0 else PANEL2, ka))
            text_a(img, (bx + 16, ry + (rh - 6) / 2), str(row[0]), fr, TXT, ka, "lm")
            text_a(img, (bx + bw - 16, ry + (rh - 6) / 2), str(row[1]), fm, col if s.get("hl") else TXT, ka, "rm")
        by = y0 + 78 + len(rows) * rh + 8; b = f"{len(rows)} row" + ("s" if len(rows) != 1 else "")
        text_a(img, (bx + bw / 2, by + 20), b, F(22, "SemiBold"), DIM, a, "mm")
        if i < n - 1: text_a(img, (bx + bw + 35, y0 + 30), "→", F(40, "monob"), mix(BG, DIM, a), a, "mm")
    if v.get("note"):
        k = ease((t - 0.4 - span - 0.2) / 0.5)
        if k > 0:
            f = F(32, "SemiBold"); tw = f.getlength(v["note"]); ny = 960
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, ny, W / 2 + tw / 2 + 30, ny + 62], 31, fill=mix(BG, ACC, k)); dr.text((W / 2, ny + 31), v["note"], font=f, fill=BG, anchor="mm")

SC = {k[3:]: f for k, f in list(globals().items()) if k.startswith("sc_")}

# ---------------- voice / timing
def tts(scenes, outdir, voice, speed):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(HERE, "models/kokoro.onnx"), os.path.join(HERE, "models/voices.bin"))
    durs, chunks, sr = [], [], 24000; os.makedirs(os.path.join(outdir, "tts"), exist_ok=True)
    for i, s in enumerate(scenes):
        key = f"{voice}|{speed}|{s['say']}"; p = os.path.join(outdir, "tts", hashlib.md5(key.encode()).hexdigest()[:12] + ".wav")
        if os.path.exists(p): a, sr = sf.read(p, dtype="float32")
        else:
            a, sr = k.create(s["say"], voice=voice, speed=speed, lang="en-us"); sf.write(p, a, sr)
        a = np.concatenate([np.zeros(int(sr * 0.25)), a, np.zeros(int(sr * s.get("hold", 0.8)))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr); print(f"tts {i + 1}/{len(scenes)} {durs[-1]:.1f}s", flush=True)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.9
    tt = np.arange(len(audio)) / sr  # soft lo-fi bed: two detuned sines + gentle pulse, very low
    bed = (np.sin(2 * np.pi * 98 * tt) * 0.5 + np.sin(2 * np.pi * 146.8 * tt) * 0.35 + np.sin(2 * np.pi * 196.5 * tt) * 0.2) * (0.7 + 0.3 * np.sin(2 * np.pi * tt / 4.0) ** 2) * 0.018
    sf.write(os.path.join(outdir, "voice.wav"), np.clip(audio + bed, -1, 1).astype(np.float32), sr)
    return durs

def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
def mmss(x): x = int(x); return f"{x // 60}:{x % 60:02d}"

def write_srt(scenes, durs, path):
    out, t0, n = [], 0.0, 1
    for s, d in zip(scenes, durs):
        sents = [x.strip() for x in re.split(r"(?<=[.?!])\s+", s["say"]) if x.strip()]; tot = sum(len(x) for x in sents); t = t0 + 0.25
        for x in sents:
            dd = (d - 0.7) * len(x) / tot; out.append(f"{n}\n{ts(t)} --> {ts(t + dd)}\n{x}\n"); n += 1; t += dd
        t0 += d
    open(path, "w").write("\n".join(out))

BGIMG = None
def frame(scenes, durs, gt, label=""):
    total = sum(durs); acc = 0
    for i, (s, d) in enumerate(zip(scenes, durs)):
        if gt < acc + d: break
        acc += d
    t = gt - acc; img = BGIMG.copy()
    SC[s["vis"]["type"]](img, s["vis"], t, d)
    chrome(img, gt / total, s.get("chapter_label", label))
    if t < 0.25: img = Image.blend(BGIMG, img, ease(t / 0.25))
    return img

def render(scenes, durs, outdir, name="final.mp4"):
    total = sum(durs); tmp = os.path.join(outdir, "video.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", os.path.join(outdir, "voice.wav"),
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-shortest", tmp]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        p.stdin.write(frame(scenes, durs, f / FPS).convert("RGB").tobytes())
        if f % 1200 == 0: print(f"frame {f}/{int(total * FPS)}", flush=True)
    p.stdin.close(); p.wait()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", os.path.join(outdir, name)], check=True)

def vertical(scenes, durs, outdir, idx, title):
    """Short: 16:9 frame scaled into a 1080x1920 canvas, title on top, big captions below."""
    sel = [(scenes[i], durs[i]) for i in idx]; tot = sum(d for _, d in sel)
    sr = 24000; voice, _ = sf.read(os.path.join(outdir, "voice.wav"), dtype="float32")
    starts = np.cumsum([0] + durs)
    aud = np.concatenate([voice[int(starts[i] * sr):int((starts[i] + durs[i]) * sr)] for i in idx]); sf.write(os.path.join(outdir, "vvoice.wav"), aud, sr)
    VW, VH = 1080, 1920; vbg = make_bg(VW, VH)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}", "-r", str(FPS), "-i", "-", "-i", os.path.join(outdir, "vvoice.wav"),
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-af", "loudnorm=I=-14:TP=-1.5", "-shortest", "-movflags", "+faststart", os.path.join(outdir, "vertical.mp4")]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    sub_s = [s for s, _ in sel]; sub_d = [d for _, d in sel]
    for f in range(int(tot * FPS)):
        gt = f / FPS; fr = frame(sub_s, sub_d, gt).convert("RGB").resize((VW, int(VW * 9 / 16)), Image.LANCZOS)
        img = vbg.copy(); img.paste(fr, (0, 560))
        d = ImageDraw.Draw(img)
        for i, ln in enumerate(wrap(title, F(76, "Bold"), 960)): d.text((VW / 2, 230 + i * 92), ln, font=F(76, "Bold"), fill=TXT, anchor="mm")
        d.rounded_rectangle([VW / 2 - 150, 90, VW / 2 + 150, 140], 25, fill=ACC); d.text((VW / 2, 115), BRAND, font=F(26, "Bold"), fill=BG, anchor="mm")
        acc = 0
        for s, dd in sel:
            if gt < acc + dd: break
            acc += dd
        sents = [x.strip() for x in re.split(r"(?<=[.?!,])\s+", s["say"]) if x.strip()]; tot_c = sum(len(x) for x in sents); tl = (gt - acc - 0.25) / max(0.1, dd - 0.7) * tot_c; cur = sents[-1]
        for x in sents:
            if tl < len(x): cur = x; break
            tl -= len(x)
        for i, ln in enumerate(wrap(cur, F(56, "Bold"), 940)[:3]): d.text((VW / 2, 1260 + i * 72), ln, font=F(56, "Bold"), fill=YEL if i == 0 else TXT, anchor="mm", stroke_width=3, stroke_fill=BG)
        d.rectangle([0, VH - 10, VW * gt / tot, VH], fill=ACC)
        p.stdin.write(img.convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("vertical ok", round(tot, 1), "s")

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    voice = os.environ.get("VOICE", getattr(ep, "VOICE", "am_eric")); speed = float(os.environ.get("SPEED", getattr(ep, "SPEED", 1.0)))
    scenes = ep.SCENES; ACC = getattr(ep, "ACCENT", LIME); BGIMG = make_bg()
    if "--preview" in sys.argv:
        durs = [6.0] * len(scenes)
        for i in range(len(scenes)): frame(scenes, durs, i * 6 + 5.1).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}.jpg"), quality=80)
        print("preview ok"); sys.exit()
    if "--vertical" in sys.argv:
        k = sys.argv.index("--vertical"); idx = [int(x) for x in sys.argv[k + 1].split(",")]
        durs = json.load(open(os.path.join(outdir, "durs.json"))); vertical(scenes, durs, outdir, idx, sys.argv[k + 2]); sys.exit()
    durs = tts(scenes, outdir, voice, speed); json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
    write_srt(scenes, durs, os.path.join(outdir, "subtitles.srt"))
    acc, ch = 0.0, []
    for s, d in zip(scenes, durs):
        if s.get("chapter"): ch.append(f"{mmss(acc)} {s['chapter']}")
        acc += d
    open(os.path.join(outdir, "chapters.txt"), "w").write("\n".join(ch) + "\n")
    print("total", mmss(sum(durs)))
    if "--tts" in sys.argv: sys.exit()
    render(scenes, durs, outdir); print("ok")
