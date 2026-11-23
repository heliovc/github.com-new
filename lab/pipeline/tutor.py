"""Shortcut Lab - software/AI tutorials, drawn 100% by code.
Script (scenes: say + vis) -> Kokoro voice (en-us, am_eric) -> editor / terminal / file-explorer / chat animations -> MP4 1080p24 + SRT.
Usage:
  python3 -I tutor.py ep01.py out/ep01 --preview        # one still per scene (at 85% of the scene)
  python3 -I tutor.py ep01.py out/ep01                  # full render -> final.mp4, subtitles.srt, chapters.txt
  python3 -I tutor.py ep01.py out/ep01 --vertical "0,3,5" "TITLE"   # Short 1080x1920 from scenes (uses cached voice)
Scene types: title, steps, code, term, files, tip, keys, compare, chat, outro, tree (EP02), map (EP02), sheet + args (EP03), prompt + flow (EP04), stage + timeline (EP05: Git areas and commit history), term colors diff +/- lines and errors (EP05), figure (EP06: real matplotlib PNG in a plot window, left-to-right wipe + numbered callouts), nav (EP07: folder tree with a moving "YOU ARE HERE" pin driven by cd commands + live pwd bar), cards (EP07: cheat-sheet grid of command cards popping in, optional highlight), funnel (EP08: a QUERY string read clause by clause, each clause
  highlighted on top while its mini result table appears in a column - rows shrinking left to right, row-count badges); sheet results now
  draw the header row in bold when a QUERY result starts on row 1 (EP08)
  live (EP09: split screen - code editor on the left typing HTML/CSS with new lines highlighted, a browser window on the right
  with address bar + "reload" sweep that reveals a REAL Chromium screenshot of that exact file; phone=True draws a phone frame);
  colorize() now also highlights lang="html" (tags, attributes, values) and lang="css" (selectors, properties, values) (EP09)
  pdfx (EP10: a REAL rendered PDF page in a viewer window, a scan beam sweeps down and every box pdfplumber really found - text lines or
  table rows - lights up as it passes, while its extracted text lands on the right as lines or as a cell grid; empty= for scanned pages)
  rx (EP11: regex lab - the pattern in a big bar on top, split into colored parts that pop in as "chips" explaining each piece; below,
  the sample text in a window where every REAL match (re.finditer at render time) lights up one after another, capture groups in their
  own colors, with a live match counter; sub= swaps each match for its re.sub replacement after the sweep)
  cron (EP12: a crontab line decoded - five time fields pop in as colored tiles with label + plain meaning, then a 7-day x 24-hour
  calendar where a cursor sweeps and every REAL run time (cron matcher at render time, dom/dow OR rule) drops a dot + run counter)
  vsc (EP13: a code editor driven by real shortcut semantics - multi-cursor carets, add-next-match (whole word, match case), select all
  matches, cursor below, move/copy/delete line, toggle comment, F2 rename (identifiers only), go-to-line box, quick-open/command palette
  with a live fuzzy filter, terminal panel + explorer toggles; keycap HUD with Windows/Linux + Mac keys and a shortcut history;
  the edit engine runs at render time and ep13 runs the resulting files for the real terminal output)
  merge (EP14: a folder window with one tile per REAL workbook feeding a combined sheet - files are read slow-then-fast, each flies
  in as a chip, the sheet keeps the newest blocks (real first row + "... N more rows") with a colored Source stripe, live file/row
  counters add the REAL row counts; naive=True shows the "Qty" file as NaN, a lock file stops the run with the real error unless skip=True)
  clean (EP15: a REAL messy table on the right + a rail of cleaning steps on the left; per step a scan bar sweeps the touched columns,
  every cell that really changes flashes coral -> accent and morphs old -> new, extra spaces are drawn as visible dots, NaN glows,
  removed rows are struck and collapse; badges + counters show the REAL whole-file numbers. frm/upto pick the steps to animate)
  xlsx (EP16: a REAL .xlsx read back with openpyxl - formula bar with name box + the selected cell's formula, letters/row numbers,
  the real column widths, bold/font color/fill, number formats, #### when a number doesn't fit, frozen header line and sheet tabs;
  build=True drops rows in, morph=<plain workbook> morphs the unformatted file into the formatted one)
  scrape (EP17: a REAL Chromium screenshot in a browser window + a CSS selector bar; every element the selector really matches
  (Playwright bounding boxes) lights up with a numbered badge while the value BeautifulSoup really extracted lands in a "What Python gets"
  table; inner= outlines a child selector; mode="inspect" = DevTools-style hovered element + its HTML with the lines highlighted;
  mode="nojs" = the browser view next to a REAL JavaScript-off screenshot = what requests downloads)
  group (EP16: groupby made visible - the REAL rows stream by on the left, each revenue flies as a chip into its city bucket, bars and
  running totals grow with the REAL cumulative sums (slow first rows, then fast-forward) and end at the real groupby result)
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
HTMLTOK = re.compile(r"(<!--.*?-->)|(</?[A-Za-z!][\w-]*|/?>)|(\b[\w-]+(?==))|(\"[^\"]*\")|([^<\"]+?(?=<|\"|$|\b[\w-]+=))|(.)")
def colorize(line, lang="py"):
    out = []
    if lang == "html":  # EP09
        intag = False
        for m in HTMLTOK.finditer(line):
            com, tag, attr, val, txt, other = m.groups()
            if com: out.append((com, DIM))
            elif tag: out.append((tag, CORAL)); intag = not tag.endswith(">")
            elif attr and intag: out.append((attr, SKY))
            elif val and intag: out.append((val, YEL))
            else: out.append((m.group(0), TXT))
        return out
    if lang == "css":  # EP09
        st = line.strip()
        if ":" in st and st.endswith(";"):
            k, _, rest = line.partition(":"); return [(k, SKY), (":", DIM), (rest[:-1], YEL), (";", DIM)]
        if st.endswith("{"): return [(line[:-1], CORAL if not st.startswith("@") else VIO), ("{", DIM)]
        return [(line, DIM if st in ("}", "") else TXT)]
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

# ---- EP09: live - editor (left) + browser (right). After the code finishes typing, a reload sweep reveals a REAL screenshot of that file.
def sc_live(img, v, t, d):
    lines = v["code"].strip("\n").split("\n"); v0 = 0
    if v.get("view"): v0, v1 = v["view"]; lines = lines[v0:v1]
    hl = tuple(h - v0 for h in v.get("hl", ())); start = v.get("from", 0); start = max(0, start - v0)
    ex0, ey0, ex1, ey1 = 50, 140, 1000, 1000; bx0, bx1 = 1030, 1870
    size = v.get("size", 23)
    while size > 15 and (F(size, "mono").getlength(max(lines, key=len)) > ex1 - ex0 - 130 or len(lines) * size * 1.5 > ey1 - ey0 - 90): size -= 1
    lh = int(size * 1.5)
    window(img, [ex0, ey0, ex1, ey1], v.get("file", "index.html"))
    total = sum(len(l) + 1 for l in lines); st = sum(len(l) + 1 for l in lines[:start])
    typ = v.get("typed", True); dur = min(d * 0.55, max(0.8, (total - st) / v.get("cps", 40)))
    chars = st + (total - st) * ease(t / dur) if typ else total
    tmp = img.copy()  # draw on a copy, keep only the editor area (line highlights stay inside the narrower editor)
    draw_code(tmp, ex0 + 100, ey0 + 76, lines, int(chars), v.get("lang", "html"), hl if (t > dur * 0.6 or not typ) else (), lh, size, t=t, num0=v0)
    img.paste(tmp.crop((ex0 + 2, ey0 + 54, ex1 - 2, ey1 - 2)), (ex0 + 2, ey0 + 54))
    # browser
    phone = v.get("phone"); bw_ = 470 if phone else bx1 - bx0; bxa = bx0 + ((bx1 - bx0) - bw_) // 2 if phone else bx0
    if v["shot"] not in _imc: _imc[v["shot"]] = Image.open(v["shot"]).convert("RGBA")
    src = _imc[v["shot"]]; iw = bw_ - 24; ih = int(src.height * iw / src.width)
    by1 = min(ey1, ey0 + 52 + 56 + ih + 12); byy0 = ey0 if not phone else max(ey0, (ey0 + ey1) // 2 - (by1 - ey0) // 2); by1 += byy0 - ey0
    window(img, [bxa, byy0, bxa + bw_, by1], v.get("tab", "Sam Rivera"), kind="term")
    dr = ImageDraw.Draw(img); ay = byy0 + 62
    dr.rounded_rectangle([bxa + 14, ay, bxa + bw_ - 14, ay + 40], 20, fill=(38, 42, 52))
    url = v.get("url", "file:///C:/my-site/index.html"); fu = F(19, "mono")
    while fu.getlength(url) > bw_ - 90 and len(url) > 10: url = "…" + url[2:]
    dr.text((bxa + 40, ay + 20), url, font=fu, fill=DIM, anchor="lm")
    k = ease((t - dur - 0.15) / 0.5) if typ else ease((t - 0.2) / 0.5)
    py = ay + 50; ph = by1 - py - 12; pic = src.resize((iw, ih), Image.LANCZOS).crop((0, 0, iw, min(ih, ph)))
    dr.rectangle([bxa + 12, py, bxa + 12 + iw, py + pic.height], fill=(255, 255, 255))
    if v.get("prev") and k < 1:  # previous version stays until the reload
        if v["prev"] not in _imc: _imc[v["prev"]] = Image.open(v["prev"]).convert("RGBA")
        pp = _imc[v["prev"]]; img.alpha_composite(pp.resize((iw, int(pp.height * iw / pp.width)), Image.LANCZOS).crop((0, 0, iw, pic.height)), (bxa + 12, py))
    if k > 0:
        ch = max(1, int(pic.height * k)); img.alpha_composite(pic.crop((0, 0, iw, ch)), (bxa + 12, py))
        if k < 1: dr.rectangle([bxa + 12, py + ch - 2, bxa + 12 + iw, py + ch + 3], fill=ACC)
    rk = 1 - abs(((t - dur - 0.15) / 0.5) - 0.5) * 2 if typ else 0  # reload chip pulses during the sweep
    if rk > 0:
        lab = v.get("reload", "Ctrl+S, then F5"); fl = F(24, "monob"); lw = fl.getlength(lab) + 40
        dr.rounded_rectangle([bxa + bw_ / 2 - lw / 2, by1 - 70, bxa + bw_ / 2 + lw / 2, by1 - 22], 24, fill=mix(BG, ACC, rk)); dr.text((bxa + bw_ / 2, by1 - 46), lab, font=fl, fill=BG, anchor="mm")
    if v.get("note"):
        a = ease((t - dur - 0.9) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if a > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 1012, W / 2 + tw / 2 + 30, 1066], 27, fill=mix(BG, v.get("notecol", ACC), a)); dr.text((W / 2, 1039), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP10: pdfx - a REAL rendered PDF page (left, PDF viewer) with a scan beam sweeping down; every box pdfplumber really found
#      (text lines / table rows, page fractions from demo/ep10/boxes.json) lights up as the beam passes it, and its extracted text
#      lands in the output panel on the right - as plain lines (mode "text") or as a cell grid (mode "table"). pick = boxes in accent color.
def sc_pdfx(img, v, t, d):
    if v["page"] not in _imc: _imc[v["page"]] = Image.open(v["page"]).convert("RGBA")
    src = _imc[v["page"]]; ph = 800; pw = int(src.width * ph / src.height)
    x0, y0 = 90, 150; box = [x0, y0, x0 + pw + 40, y0 + 52 + ph + 40]
    if v.get("title"): text_a(img, (1360, 175), v["title"], F(40, "Bold"), TXT, ease(t / 0.4), "mm")
    window(img, box, v.get("win", "invoice_1042.pdf"), kind="term")
    px, py = x0 + 20, y0 + 72; pic = src.resize((pw, ph), Image.LANCZOS); img.alpha_composite(pic, (px, py))
    span = d * v.get("span", 0.55); k = max(0.0, min(1.0, (t - 0.4) / span)); beam = py + ph * k
    dr = ImageDraw.Draw(img)
    boxes = v.get("boxes", []); pick = v.get("pick", ())
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); done = 0
    for i, b in enumerate(boxes):
        bx0, by0, bx1, by1 = px + b[0] * pw - 4, py + b[1] * ph - 3, px + b[2] * pw + 4, py + b[3] * ph + 3
        if beam < by1: continue
        done += 1; col = ACC if (i in pick or not pick) else SKY
        dl.rectangle([bx0, by0, bx1, by1], fill=col + (60 if i in pick else 34,), outline=col + (255 if i in pick else 150,), width=3 if i in pick else 1)
    img.alpha_composite(lay)
    if 0 < k < 1:
        g = Image.new("RGBA", img.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(g)
        for j in range(26): dg.line([px, beam - j, px + pw, beam - j], fill=ACC + (int(110 * (1 - j / 26)),))
        img.alpha_composite(g); dr.line([px, beam, px + pw, beam], fill=ACC, width=3)
    # output panel
    ox0, ox1 = box[2] + 50, W - 70; oy0 = 230 if v.get("title") else 150; oy1 = box[3]
    window(img, [ox0, oy0, ox1, oy1], v.get("outwin", "extracted"), kind="term")
    out = v.get("out", []); oy = oy0 + 80
    if v.get("mode") == "table":
        cols = len(out[0]); cw = (ox1 - ox0 - 60) / cols; rh = min(66, (oy1 - oy - 30) / max(1, len(out)))
        fr = F(26, "mono")
        for r, row in enumerate(out):
            if r >= done: break
            ry = oy + r * rh
            for c, cell in enumerate(row):
                cx = ox0 + 30 + c * cw
                dr.rectangle([cx, ry, cx + cw - 6, ry + rh - 6], fill=mix(PANEL, ACC, 0.3) if r == 0 else (PANEL if r % 2 else PANEL2), outline=LINE)
                dr.text((cx + 14, ry + (rh - 6) / 2), cell, font=F(26, "monob") if r == 0 else fr, fill=BG if False else (ACC if r == 0 else TXT), anchor="lm")
    else:
        fo = F(v.get("size", 25), "mono"); lh = int(v.get("size", 25) * 1.6); maxw = ox1 - ox0 - 60; n = 0
        for i, ln in enumerate(out):
            if i >= done and boxes: break
            while fo.getlength(ln) > maxw and len(ln) > 4: ln = ln[:-2] + "…"
            dr.text((ox0 + 30, oy + n * lh), ln, font=fo, fill=ACC if (i in pick) else (200, 206, 216)); n += 1
        if not boxes and k >= 1:  # nothing found on the page (scanned image / no table)
            fe = F(40, "monob"); dr.text(((ox0 + ox1) / 2, (oy0 + oy1) / 2 - 30), v.get("empty", "''"), font=fe, fill=CORAL, anchor="mm")
            if v.get("empty_sub"): dr.text(((ox0 + ox1) / 2, (oy0 + oy1) / 2 + 40), v["empty_sub"], font=F(28, "Medium"), fill=DIM, anchor="mm")
    if v.get("note"):
        a = ease((t - 0.6 - span) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if a > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 1012, W / 2 + tw / 2 + 30, 1066], 27, fill=mix(BG, v.get("notecol", ACC), a)); dr.text((W / 2, 1039), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP11: rx - regex lab. Pattern bar (parts colored + explanation chips), then the text where each real re.finditer match lights up
#      in order (groups tinted with GROUPC), a live "N matches" counter, optional sub= replacement shown after the sweep.
GROUPC = [(108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89)]
def sc_rx(img, v, t, d):
    pat = v["pattern"]; parts = v.get("parts") or [(pat, "", ACC)]; flags = re.I if v.get("ignorecase") else 0
    lines = v["text"] if isinstance(v["text"], list) else v["text"].split("\n"); text = "\n".join(lines)
    dr = ImageDraw.Draw(img); span = d * v.get("span", 0.7)
    tp = span * (0.45 if v.get("parts") else 0.1)  # time spent on the chips
    # pattern bar
    fp = F(v.get("psize", 50), "monob"); full = "".join(p[0] for p in parts); pw = fp.getlength(full) + fp.getlength("r\"\"")
    x = W / 2 - pw / 2; yb = 190; a0 = ease(t / 0.4)
    dr.rounded_rectangle([x - 40, yb - 50, x + pw + 40, yb + 50], 22, fill=mix(BG, PANEL, a0), outline=mix(BG, ACC, a0), width=3)
    text_a(img, (x - 40, yb - 72), v.get("label", "PATTERN"), F(22, "Bold"), ACC, a0, "ls")
    text_a(img, (x, yb), "r\"", fp, DIM, a0, "lm"); x += fp.getlength("r\"")
    n = len(parts); cur = int((t - 0.4) / max(0.01, tp / n)) if t > 0.4 else -1
    for i, (tok, expl, col) in enumerate(parts):
        wl = fp.getlength(tok)
        if i == cur and v.get("parts") and t < 0.4 + tp: dr.rounded_rectangle([x - 4, yb - 36, x + wl + 4, yb + 36], 8, fill=mix(PANEL, col, 0.3))
        text_a(img, (x, yb), tok, fp, col if (i <= cur or not v.get("parts")) else (200, 206, 216), a0, "lm"); x += wl
    text_a(img, (x, yb), "\"", fp, DIM, a0, "lm")
    y = 300
    if v.get("parts"):  # explanation chips, flowing left to right
        fc, fe = F(30, "monob"), F(24, "Medium"); ws = [max(fc.getlength(p[0]), fe.getlength(p[1])) + 44 for p in parts]
        rows, row, rw = [], [], 0
        for i, w_ in enumerate(ws):
            if row and rw + w_ + 20 > 1760: rows.append(row); row, rw = [], 0
            row.append(i); rw += w_ + 20
        rows.append(row)
        for r, row in enumerate(rows):
            tw = sum(ws[i] + 20 for i in row) - 20; cx = W / 2 - tw / 2
            for i in row:
                a = ease((t - 0.4 - tp * i / n) / 0.35); tok, expl, col = parts[i]
                if a > 0:
                    cy = y + r * 106 + (1 - a) * 20
                    dr.rounded_rectangle([cx, cy, cx + ws[i], cy + 92], 16, fill=mix(BG, mix(PANEL, col, 0.14), a), outline=mix(BG, col, a), width=2)
                    text_a(img, (cx + ws[i] / 2, cy + 30), tok, fc, col, a, "mm"); text_a(img, (cx + ws[i] / 2, cy + 68), expl, fe, (200, 206, 216), a, "mm")
                cx += ws[i] + 20
        y += len(rows) * 106 + 20
    # text window
    ft = F(v.get("size", 28), "mono"); cw = ft.getlength("M"); lh = int(v.get("size", 28) * 1.6)
    hgt = 52 + 40 + len(lines) * lh + 20; wy0 = max(y, min(1010 - hgt, y + 20)); box = [90, wy0, W - 90, wy0 + hgt]
    window(img, box, v.get("file", "inbox.txt"), kind="term")
    ms = list(re.finditer(pat, text, flags)); t1 = 0.4 + tp; gap = max(0.05, (span - tp) / max(1, len(ms)))
    shown = sum(1 for k, _ in enumerate(ms) if t >= t1 + k * gap)
    subbed = v.get("sub") is not None and t > 0.4 + span + 0.3
    if subbed: lines = re.sub(pat, v["sub"], text, flags=flags).split("\n")
    lx, ly = 130, wy0 + 76; offs = [0]
    for ln in lines[:-1]: offs.append(offs[-1] + len(ln) + 1)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    if not subbed:
        for k, m in enumerate(ms[:shown]):
            hot = k == shown - 1 and t < t1 + shown * gap + 0.3
            for li, o in enumerate(offs):
                s0, s1 = max(m.start(), o), min(m.end(), o + len(lines[li]))
                if s0 >= s1: continue
                yy = ly + li * lh
                dl.rounded_rectangle([lx + cw * (s0 - o) - 3, yy - 5, lx + cw * (s1 - o) + 3, yy + lh - 9], 6, fill=ACC + (110 if hot else 70,), outline=ACC + (255,), width=2)
                for g in range(1, (m.lastindex or 0) + 1):
                    g0, g1 = max(m.start(g), o), min(m.end(g), o + len(lines[li]))
                    if g0 < g1: dl.rectangle([lx + cw * (g0 - o), yy + lh - 14, lx + cw * (g1 - o), yy + lh - 9], fill=GROUPC[(g - 1) % 4] + (255,))
    img.alpha_composite(lay)
    for li, ln in enumerate(lines): dr.text((lx, ly + li * lh), ln, font=ft, fill=TXT if not subbed else (200, 206, 216))
    if subbed:  # tint the replaced pieces
        rs = list(re.finditer(re.escape(v.get("subshow", "")), "\n".join(lines))) if v.get("subshow") else []
        for m in rs:
            for li, o in enumerate(offs):
                if o <= m.start() < o + len(lines[li]) + 1: dr.text((lx + cw * (m.start() - o), ly + li * lh), m.group(0), font=ft, fill=ACC)
    # counter chip
    lab = (f"{shown} match" + ("" if shown == 1 else "es")) if not subbed else v.get("sublabel", "re.sub() done")
    fl = F(26, "Bold"); lw = fl.getlength(lab) + 44
    dr.rounded_rectangle([box[2] - lw - 20, box[1] + 9, box[2] - 20, box[1] + 45], 18, fill=ACC if shown or subbed else LINE); dr.text((box[2] - 20 - lw / 2, box[1] + 27), lab, font=fl, fill=BG, anchor="mm")
    if v.get("note"):
        a = ease((t - 0.6 - span) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if a > 0:
            ny = min(1012, box[3] + 14); dr.rounded_rectangle([W / 2 - tw / 2 - 30, ny, W / 2 + tw / 2 + 30, ny + 54], 27, fill=mix(BG, v.get("notecol", ACC), a)); dr.text((W / 2, ny + 27), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP12: cron - a crontab line decoded: its five time fields pop in as big colored tiles (label + plain meaning under each),
# then a 7-day x 24-hour calendar where a time cursor sweeps left to right and every REAL run time (computed at render time by a
# small cron matcher: *, */n, a-b, a,b, dom/dow OR rule) drops a dot; a counter chip shows the runs found that week
CRON_NAMES = ["MINUTE", "HOUR", "DAY OF MONTH", "MONTH", "DAY OF WEEK"]
def _cron_set(f, lo, hi):
    out = set()
    for part in f.split(","):
        rng, _, step = part.partition("/"); step = int(step or 1)
        if rng == "*": a, b = lo, hi
        elif "-" in rng: a, b = map(int, rng.split("-"))
        else: a = b = int(rng)
        out |= set(range(a, b + 1, step))
    return out
def cron_runs(expr, start="2026-11-16", days=7):
    import datetime as _dt
    mi, ho, dm, mo, dw = expr.split()[:5]
    M, Hh, D, Mo = _cron_set(mi, 0, 59), _cron_set(ho, 0, 23), _cron_set(dm, 1, 31), _cron_set(mo, 1, 12)
    Wd = {x % 7 for x in _cron_set(dw, 0, 7)}
    t0 = _dt.datetime.fromisoformat(start); runs = []
    for k in range(days * 24 * 60):
        t = t0 + _dt.timedelta(minutes=k)
        if t.minute not in M or t.hour not in Hh or t.month not in Mo: continue
        dom_ok, dow_ok = t.day in D, (t.isoweekday() % 7) in Wd
        ok = (dom_ok or dow_ok) if (dm != "*" and dw != "*") else (dom_ok and dow_ok)
        if ok: runs.append(t)
    return runs
def sc_cron(img, v, t, d):
    expr = v["expr"]; flds = expr.split()[:5]; cols = v.get("colors", [SKY, YEL, (80, 220, 190), CORAL, VIO])
    dr = ImageDraw.Draw(img); span = d * v.get("span", 0.75); tp = span * 0.4
    if v.get("title"): text_a(img, (W / 2, 150), v["title"], F(44, "Bold"), TXT, ease(t / 0.4), "mm")
    fb = F(64, "monob"); tw, gap = 300, 26; x0 = W / 2 - (5 * tw + 4 * gap) / 2; y0 = 210
    for i, f in enumerate(flds):
        a = ease((t - 0.3 - tp * i / 5) / 0.35); col = cols[i]
        if a <= 0: continue
        x = x0 + i * (tw + gap); yy = y0 + (1 - a) * 24
        dr.rounded_rectangle([x, yy, x + tw, yy + 110], 18, fill=mix(BG, mix(PANEL, col, 0.16), a), outline=mix(BG, col, a), width=3)
        text_a(img, (x + tw / 2, yy + 55), f, fb, col, a, "mm")
        text_a(img, (x + tw / 2, yy + 140), CRON_NAMES[i], F(22, "Bold"), DIM, a, "mm")
        if v.get("means"): text_a(img, (x + tw / 2, yy + 176), v["means"][i], F(28, "SemiBold"), TXT, a, "mm")
    if v.get("cmd"):
        a = ease((t - 0.3 - tp) / 0.4); fc = F(24, "mono")
        text_a(img, (W / 2, y0 + 222), "then runs:  " + v["cmd"], fc, (200, 206, 216), a, "mm")
    # week calendar
    runs = cron_runs(expr, v.get("start", "2026-11-16")); gx0, gx1, gy0, rh = 330, 1730, 500, 56
    a = ease((t - tp) / 0.4)
    if a > 0:
        fd, fh = F(26, "SemiBold"), F(20, "mono")
        for h in range(0, 25, 3):
            x = gx0 + (gx1 - gx0) * h / 24; text_a(img, (x, gy0 - 22), f"{h:02d}:00" if h < 24 else "", fh, DIM, a, "mm")
        for r, nm in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
            y = gy0 + r * rh
            dr.rounded_rectangle([gx0, y + 8, gx1, y + rh - 8], 10, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=1)
            text_a(img, (gx0 - 30, y + rh / 2), nm, fd, (200, 206, 216), a, "rm")
        frac = max(0.0, min(1.0, (t - tp - 0.3) / max(0.5, span - tp)))
        if 0 < frac < 1: cx = gx0 + (gx1 - gx0) * frac; dr.line([cx, gy0, cx, gy0 + 7 * rh], fill=ACC, width=3)
        n = 0; dense = len(runs) > 7 * 60
        for rt in runs:
            fx = (rt.hour * 60 + rt.minute) / 1440
            if fx > frac: continue
            n += 1; x = gx0 + (gx1 - gx0) * fx; y = gy0 + rt.weekday() * rh + rh / 2
            if dense: dr.line([x, y - 12, x, y + 12], fill=ACC, width=2)
            else:
                rr = 11 if fx > frac - 0.03 else 9; dr.ellipse([x - rr, y - rr, x + rr, y + rr], fill=ACC, outline=BG, width=2)
                if len(runs) <= 10: dr.text((x + 20, y), rt.strftime("%H:%M"), font=F(20, "mono"), fill=TXT, anchor="lm")
        lab = f"{n} run" + ("" if n == 1 else "s") + " this week"; fl = F(26, "Bold"); lw = fl.getlength(lab) + 44
        dr.rounded_rectangle([gx1 - lw, gy0 + 7 * rh + 14, gx1, gy0 + 7 * rh + 60], 23, fill=ACC); dr.text((gx1 - lw / 2, gy0 + 7 * rh + 37), lab, font=fl, fill=BG, anchor="mm")
    if v.get("english"):
        a = ease((t - span) / 0.5); fe = F(32, "SemiBold")
        text_a(img, (gx0, gy0 + 7 * rh + 37), v["english"], fe, v.get("engcol", TXT), a, "lm")

# ---- EP13: "vsc" - a code editor driven by REAL keyboard-shortcut semantics. Each op = Windows/Linux keys + Mac keys + a list of
# primitive actions (cursor, add-next-match, select-all-matches, cursor below, move/copy/delete line, toggle comment, F2 rename,
# go to line, quick-open/command-palette filter, terminal panel). The edit engine runs at render time (vsc_apply), so the code
# on screen at the end is exactly what the engine produced - ep13 writes those final files out and runs them for the terminal shots.
# Multi-cursor carets glow, a keycap HUD on the right shows the shortcut being pressed + a history of the last ones, status bar
# shows Ln/Col and "N selections".
VS_WORD = re.compile(r"[A-Za-z_]\w*|\d+")
def _wordat(ln, c):
    for m in VS_WORD.finditer(ln):
        if m.start() <= c <= m.end(): return m.start(), m.end()
    return c, c
def _instr(ln, c):  # True if column c is inside a "..." / '...' literal
    q = None
    for i, ch in enumerate(ln[:c]):
        if q is None and ch in "\"'": q = ch
        elif q == ch: q = None
    return q is not None
def vsc_apply(st, act, frac=1.0):
    """st = {"lines": [...], "car": [(row, c0, c1)], ...}; rows 0-based. Returns new state (frac < 1 only matters for typing)."""
    L = list(st["lines"]); car = list(st["car"]); st = dict(st, lines=L, car=car, changed=set())
    op = act[0]
    if op == "cur": st["car"] = [(act[1] - 1, act[2], act[2])]
    elif op == "add": st["car"] = car + [(act[1] - 1, act[2], act[2])]
    elif op == "sel": st["car"] = [(act[1] - 1, act[2], act[3])]
    elif op == "selend": st["car"] = [(r, c0, len(L[r])) for r, c0, c1 in car]
    elif op == "esc": st["car"] = car[:1]  # Escape keeps the primary (first) cursor
    elif op == "upper":
        for r, c0, c1 in car: L[r] = L[r][:c0] + L[r][c0:c1].upper() + L[r][c1:]; st["changed"].add(r)
    elif op == "bs":  # Backspace; on indentation it removes one tab stop (4 spaces)
        new = []
        for r, c0, c1 in car:
            n = 4 if L[r][:c1].strip() == "" and c1 % 4 == 0 and c1 > 0 else 1
            L[r] = L[r][:c1 - n] + L[r][c1:]; new.append((r, c1 - n, c1 - n)); st["changed"].add(r)
        st["car"] = new
    elif op == "word": st["car"] = [(r,) + _wordat(L[r], c0) for r, c0, c1 in car]
    elif op in ("next", "all"):
        r, c0, c1 = car[-1]; w = L[r][c0:c1]
        pat = re.compile(re.escape(w), re.I) if "loose" in act else re.compile(r"(?<!\w)" + re.escape(w) + r"(?!\w)")  # loose = selection made by hand (default find options)
        hits = [(i, m.start(), m.end()) for i, ln in enumerate(L) for m in pat.finditer(ln)]
        if op == "all": st["car"] = hits
        else:
            after = [h for h in hits if (h[0], h[1]) > (r, c0) and h not in car] or [h for h in hits if h not in car]
            st["car"] = car + after[:1]
    elif op == "type":
        s = act[1][:int(round(len(act[1]) * frac))]; new = []; shift = {}
        for r, c0, c1 in sorted(car):
            k = shift.get(r, 0); a, b = c0 + k, c1 + k
            L[r] = L[r][:a] + s + L[r][b:]; shift[r] = k + len(s) - (b - a); new.append((r, a + len(s), a + len(s))); st["changed"].add(r)
        st["car"] = new
    elif op == "end": st["car"] = [(r, len(L[r]), len(L[r])) for r, c0, c1 in car]
    elif op == "home": st["car"] = [(r, len(L[r]) - len(L[r].lstrip()), len(L[r]) - len(L[r].lstrip())) for r, c0, c1 in car]
    elif op == "below":
        r, c0, c1 = car[-1]; st["car"] = car + [(r + 1, min(c1, len(L[r + 1])), min(c1, len(L[r + 1])))]
    elif op in ("mvu", "mvd"):
        r, c0, c1 = car[-1]; j = r - 1 if op == "mvu" else r + 1
        L[r], L[j] = L[j], L[r]; st["car"] = [(j, c0, c1)]; st["changed"] = {j}
    elif op == "cpd":
        r, c0, c1 = car[-1]; L.insert(r + 1, L[r]); st["car"] = [(r + 1, c0, c1)]; st["changed"] = {r + 1}
    elif op == "del":
        r = car[-1][0]; L.pop(r); r = min(r, len(L) - 1); st["car"] = [(r, 0, 0)]; st["changed"] = {r}
    elif op in ("below_line", "above_line"):  # Ctrl+Enter / Ctrl+Shift+Enter: new line keeping indentation
        r = car[-1][0]; ind = L[r][:len(L[r]) - len(L[r].lstrip())]; j = r + 1 if op == "below_line" else r
        L.insert(j, ind); st["car"] = [(j, len(ind), len(ind))]; st["changed"] = {j}
    elif op == "cmt":
        rows = sorted({r for r, _, _ in car}); ind = min(len(L[r]) - len(L[r].lstrip()) for r in rows)
        if all(L[r].lstrip().startswith("# ") for r in rows):
            for r in rows: L[r] = L[r].replace("# ", "", 1)
            st["car"] = [(r, max(0, c0 - 2), max(0, c1 - 2)) for r, c0, c1 in car]
        else:
            for r in rows: L[r] = L[r][:ind] + "# " + L[r][ind:]
            st["car"] = [(r, c0 + 2, c1 + 2) for r, c0, c1 in car]
        st["changed"] = set(rows)
    elif op == "rename":  # F2: identifiers only (strings and comments untouched)
        r, c0, c1 = car[-1]; a, b = _wordat(L[r], c0); old = L[r][a:b]; pat = re.compile(r"(?<!\w)" + re.escape(old) + r"(?!\w)")
        for i, ln in enumerate(L):
            cut = ln.find("#") if "#" in ln and not _instr(ln, ln.find("#")) else len(ln)
            out, last = "", 0
            for m in pat.finditer(ln):
                if m.start() >= cut or _instr(ln, m.start()): continue
                out += ln[last:m.start()] + act[1]; last = m.end(); st["changed"].add(i)
            L[i] = out + ln[last:]
        st["car"] = [(r, a, a + len(act[1]))]; st["renamed"] = (old, act[1])
    elif op == "goto": st["car"] = [(act[1] - 1, 0, 0)]
    elif op == "open": st.update(lines=act[2].strip("\n").split("\n"), file=act[1], car=[(0, 0, 0)])
    elif op == "term": st["term"] = None if st.get("term") else act[1]
    elif op == "side": st["side"] = None if st.get("side") else act[1]
    return st

def vsc_ops(v):
    ops = v["ops"]; ws = [o.get("w", 1.0) + sum(len(a[1]) / 14 for a in o["do"] if a[0] == "type") for o in ops]
    return ops, ws

def vsc_state(v, upto, frac=1.0):
    st = dict(lines=v["code"].strip("\n").split("\n"), car=[tuple(c) for c in v.get("car", [(1, 0, 0)])], file=v.get("file", "main.py"))
    st["car"] = [(r - 1, c0, c1) for r, c0, c1 in st["car"]]
    ops = v["ops"]
    for k in range(min(upto, len(ops))):
        for a in ops[k]["do"]: st = vsc_apply(st, a)
    if upto < len(ops) and frac > 0:
        types = [a for a in ops[upto]["do"] if a[0] == "type"]; nt = len(types); ti = 0
        for a in ops[upto]["do"]:
            if a[0] in ("type",):
                f = max(0.0, min(1.0, frac * nt - ti)); ti += 1
                if f <= 0: break
                st = vsc_apply(st, a, f)
                if f < 1: break
            elif a[0] in ("rename", "goto", "open", "palette", "upper"):
                if frac >= 1: st = vsc_apply(st, a)
            else:
                if frac * max(1, nt) >= ti: st = vsc_apply(st, a)
    return st

def vsc_final(v):
    st = vsc_state(v, len(v["ops"])); return "\n".join(st["lines"]) + "\n"

def _keycaps(img, x, y, keys, size, col, a=1.0, press=0.0, maxw=440):
    dr = ImageDraw.Draw(img); groups = keys.split(" "); f = F(size, "SemiBold"); fm = F(size, "monob")
    ARW = {"Up": "↑", "Down": "↓", "Left": "←", "Right": "→"}
    caps = []
    for gi, g in enumerate(groups):
        for ki, k in enumerate(g.split("+") if g != "+" else ["+"]):
            lab = ARW.get(k, k); ff = fm if lab in ARW.values() or lab in "`/" else f
            caps.append((lab, ff, ki > 0)); 
        caps.append((None, None, False))
    caps = caps[:-1]
    xx = x
    for lab, ff, plus in caps:
        if lab is None: xx += size * 0.6; continue
        if plus: text_a(img, (xx + size * 0.35, y + size * 0.9), "+", F(size * 0.8, "Bold"), DIM, a, "mm"); xx += size * 0.7
        w = max(size * 1.7, ff.getlength(lab) + size * 1.0); p = press * 5
        dr.rounded_rectangle([xx, y + 8, xx + w, y + size * 1.8 + 8], 12, fill=mix(BG, (8, 9, 12), a))
        dr.rounded_rectangle([xx, y + p, xx + w, y + size * 1.8 + p], 12, fill=mix(BG, PANEL2, a), outline=mix(BG, col, a), width=3)
        text_a(img, (xx + w / 2, y + size * 0.9 + p), lab, ff, TXT, a, "mm"); xx += w
    return xx - x

def _fuzzy(q, s):
    it = iter(s.lower()); return all(ch in it for ch in q.lower())

def sc_vsc(img, v, t, d):
    ops, ws = vsc_ops(v); span = d * v.get("span", 0.82); t0 = v.get("delay", 0.6); tot = sum(ws)
    k, frac, acc = len(ops), 1.0, t0
    for i, w in enumerate(ws):
        dur = (span - t0) * w / tot
        if t < acc + dur: k, frac = i, (t - acc) / dur; break
        acc += dur
    if t < t0: k, frac = 0, 0.0
    pf = max(0.0, (frac - 0.28) / 0.62) if k < len(ops) else 1.0  # keys first, then the edit happens
    st = vsc_state(v, k, pf); prev_changed = st.get("changed", set())
    dr = ImageDraw.Draw(img); side = st.get("side"); term = st.get("term")
    box = [60, 130, 1300, 1000]; window(img, box, st.get("file", "main.py"))
    ex0 = box[0]
    if side:  # explorer column
        dr.rectangle([box[0] + 2, box[1] + 52, box[0] + 300, box[3] - 40], fill=(20, 22, 28))
        text_a(img, (box[0] + 24, box[1] + 76), "EXPLORER", F(18, "Bold"), DIM)
        for i, n in enumerate(side):
            y = box[1] + 120 + i * 40; on = n == st.get("file")
            if on: dr.rectangle([box[0] + 2, y - 6, box[0] + 300, y + 30], fill=mix(PANEL2, ACC, 0.18))
            text_a(img, (box[0] + 30, y), n, F(20, "mono"), TXT if on else (190, 196, 206))
        ex0 = box[0] + 300
    size = v.get("size", 26); f = F(size, "mono"); cw = f.getlength("M"); lh = v.get("lh", 44)
    x = ex0 + 90; y0 = box[1] + 80; rows = st["lines"]
    th = 0 if not term else min(330, 70 + 36 * len(term))
    maxrows = int((box[3] - 40 - th - y0) // lh)
    top = 0
    if st["car"]:
        r = st["car"][-1][0]
        if r >= maxrows: top = r - maxrows + 2
    flash = 1 - min(1.0, max(0.0, (frac - 0.9) / 0.1)) if k < len(ops) else 0
    for i in range(top, min(len(rows), top + maxrows)):
        yy = y0 + (i - top) * lh; ln = rows[i]
        if i in prev_changed and k < len(ops) and pf > 0: dr.rectangle([ex0 + 4, yy - 6, box[2] - 4, yy + lh - 8], fill=mix(PANEL, ACC, 0.13))
        if any(r == i for r, _, _ in st["car"]): dr.rectangle([ex0 + 4, yy - 6, box[2] - 4, yy + lh - 8], outline=(44, 49, 60), width=2)
        dr.text((x - 64, yy), f"{i + 1:>2}", font=f, fill=TXT if any(r == i for r, _, _ in st["car"]) else (78, 86, 102))
        for r, c0, c1 in st["car"]:
            if r == i and c1 > c0: dr.rectangle([x + c0 * cw, yy - 4, x + c1 * cw, yy + size + 8], fill=mix(PANEL, ACC, 0.42))
        cx = x
        for s, c in colorize(ln, v.get("lang", "py")): dr.text((cx, yy), s, font=f, fill=c); cx += f.getlength(s)
        for r, c0, c1 in st["car"]:
            if r == i and (int(t * 2.5) % 2 == 0 or len(st["car"]) > 1):
                cxx = x + c1 * cw; dr.rectangle([cxx - 1, yy - 4, cxx + 2, yy + size + 8], fill=ACC)
    # mouse pointer for clicks
    if k < len(ops) and ops[k].get("mouse"):
        r, c = ops[k]["mouse"]; px, py = x + c * cw + 4, y0 + (r - 1 - top) * lh + 14
        dr.polygon([(px, py), (px, py + 34), (px + 9, py + 26), (px + 16, py + 40), (px + 22, py + 37), (px + 15, py + 24), (px + 26, py + 24)], fill=(255, 255, 255), outline=BG)
    # terminal panel
    if term:
        ty = box[3] - 40 - th; dr.rectangle([ex0 + 2, ty, box[2] - 2, box[3] - 40], fill=(12, 13, 16)); dr.line([ex0 + 2, ty, box[2] - 2, ty], fill=LINE, width=2)
        text_a(img, (ex0 + 30, ty + 18), "TERMINAL", F(18, "Bold"), TXT); dr.line([ex0 + 30, ty + 44, ex0 + 128, ty + 44], fill=ACC, width=2)
        for i, ln in enumerate(term[-int((th - 70) // 36):]):
            cx = ex0 + 30
            for s, c in colorize(ln, "sh"): dr.text((cx, ty + 62 + i * 36), s, font=F(22, "mono"), fill=c); cx += F(22, "mono").getlength(s)
    # status bar
    dr.rectangle([box[0] + 2, box[3] - 40, box[2] - 2, box[3] - 2], fill=mix(PANEL2, ACC, 0.25))
    if st["car"]:
        r, c0, c1 = st["car"][-1]; sb = f"Ln {r + 1}, Col {c1 + 1}"
        if len(st["car"]) > 1: sb += f"   ({len(st['car'])} selections)"
        elif c1 > c0: sb += f"   ({c1 - c0} selected)"
        text_a(img, (box[2] - 30, box[3] - 21), sb + "    Python", F(20, "Medium"), TXT, 1, "rm")
    # quick-open / command-palette overlay
    if k < len(ops):
        pal = [a for a in ops[k]["do"] if a[0] == "palette"]
        if pal and 0 < frac < 0.9:
            _, mode, q, items = pal[0]; qq = q[:int(len(q) * min(1, max(0, (frac - 0.25) / 0.45)))]
            shown = [it for it in items if _fuzzy(qq, it)][:6]
            px0, px1 = (box[0] + box[2]) / 2 - 420, (box[0] + box[2]) / 2 + 420; py = box[1] + 60
            sh = 70 + 50 * max(1, len(shown))
            dr.rounded_rectangle([px0 + 8, py + 12, px1 + 8, py + sh + 12], 14, fill=(5, 6, 8))
            dr.rounded_rectangle([px0, py, px1, py + sh], 14, fill=(30, 33, 41), outline=ACC, width=2)
            dr.rounded_rectangle([px0 + 16, py + 14, px1 - 16, py + 58], 8, fill=(18, 20, 25), outline=LINE)
            dr.text((px0 + 32, py + 36), (mode + qq) if mode else qq, font=F(24, "mono"), fill=TXT, anchor="lm")
            for i, it in enumerate(shown):
                yy = py + 70 + i * 50
                if i == 0: dr.rectangle([px0 + 6, yy, px1 - 6, yy + 46], fill=mix((30, 33, 41), ACC, 0.3))
                dr.text((px0 + 32, yy + 23), it, font=F(24, "Medium"), fill=TXT, anchor="lm")
        gt = [a for a in ops[k]["do"] if a[0] == "goto"]
        if gt and 0 < frac < 0.9:
            px0 = (box[0] + box[2]) / 2 - 360; py = box[1] + 60; q = str(gt[0][1])[:int(len(str(gt[0][1])) * min(1, max(0, (frac - 0.25) / 0.3)) + 0.999)] if frac > 0.25 else ""
            dr.rounded_rectangle([px0, py, px0 + 720, py + 110], 14, fill=(30, 33, 41), outline=ACC, width=2)
            dr.rounded_rectangle([px0 + 16, py + 14, px0 + 704, py + 58], 8, fill=(18, 20, 25), outline=LINE)
            dr.text((px0 + 32, py + 36), ":" + q, font=F(24, "mono"), fill=TXT, anchor="lm")
            dr.text((px0 + 32, py + 84), f"Go to line {q}." if q else "Type a line number to go to.", font=F(22, "Medium"), fill=DIM, anchor="lm")
        rn = [a for a in ops[k]["do"] if a[0] == "rename"]
        if rn and 0.2 < frac < 0.9:
            r, c0, _ = st["car"][-1]; nm = rn[0][1][:int(len(rn[0][1]) * min(1, (frac - 0.3) / 0.45))] if frac > 0.3 else rows[r][slice(*_wordat(rows[r], c0))]
            bx, by = x + c0 * cw - 10, y0 + (r - top) * lh + lh
            dr.rounded_rectangle([bx, by, bx + 420, by + 96], 10, fill=(30, 33, 41), outline=ACC, width=2)
            dr.rounded_rectangle([bx + 12, by + 12, bx + 408, by + 52], 6, fill=(18, 20, 25), outline=ACC)
            dr.text((bx + 24, by + 32), nm, font=F(22, "mono"), fill=TXT, anchor="lm")
            dr.text((bx + 24, by + 74), "Enter to Rename", font=F(18, "Medium"), fill=DIM, anchor="lm")
    # HUD
    hx = 1340; dr.rounded_rectangle([hx, 130, 1860, 1000], 20, fill=PANEL, outline=LINE, width=2)
    text_a(img, (hx + 36, 176), v.get("hud", "SHORTCUT"), F(22, "Bold"), ACC)
    if k < len(ops) and t >= t0:
        o = ops[k]; a = ease(frac / 0.12); press = 1.0 if 0.12 < frac < 0.3 else 0.0
        text_a(img, (hx + 36, 228), "Windows / Linux", F(20, "Medium"), DIM, a)
        _keycaps(img, hx + 36, 262, o["keys"], 30, ACC, a, press)
        text_a(img, (hx + 36, 352), "Mac", F(20, "Medium"), DIM, a)
        _keycaps(img, hx + 36, 386, o.get("mac", o["keys"]), 24, SKY, a, press)
        for i, ln in enumerate(wrap(o.get("name", ""), F(34, "Bold"), 450)[:2]): text_a(img, (hx + 36, 470 + i * 46), ln, F(34, "Bold"), TXT, a)
        if o.get("count"): text_a(img, (hx + 460, 176), o["count"], F(24, "Bold"), TXT, a, "ra")
    done = ops[:k] if k < len(ops) else ops
    if done:
        text_a(img, (hx + 36, 600), "HISTORY", F(18, "Bold"), DIM)
        hist = []
        for o in done:
            if hist and hist[-1][0] == o["keys"]: hist[-1][1] += 1
            else: hist.append([o["keys"], 1, o.get("name", "")])
        for i, (kk, n, nm) in enumerate(hist[-6:]):
            yy = 640 + i * 56; txt = kk + (f"  ×{n}" if n > 1 else "")
            dr.rounded_rectangle([hx + 30, yy, hx + 490, yy + 46], 10, fill=PANEL2)
            dr.text((hx + 46, yy + 23), txt, font=F(20, "monob"), fill=ACC, anchor="lm")
            dr.text((hx + 476, yy + 23), nm[:22], font=F(18, "Medium"), fill=DIM, anchor="rm")

# ---- EP14: merge - a folder window with one tile per REAL workbook (left) feeding a combined sheet (right). Files are read in order
# (slow at first, then accelerating), each one flies into the sheet as a chip; the sheet keeps the newest blocks (real first row of the
# file + "... N more rows") with a colored Source stripe, and live counters add the REAL row counts. flags: "qty" (column named Qty ->
# Units shows NaN when naive=True), "lock" (Excel lock file: stops the run with an error banner unless skip=True)
MCOL = [(108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 160, 200), (190, 150, 255), (255, 170, 90)]
def sc_merge(img, v, t, d):
    files = v["files"]; n = len(files); dr = ImageDraw.Draw(img)
    span = d * v.get("span", 0.7); acc = v.get("accel", 2.0); t0 = 0.5
    def t_of(i): return t0 + span * ((i + 1) / n) ** (1 / acc)
    p = max(0.0, min(1.0, (t - t0) / span)); k = int(n * p ** acc + 1e-9)  # files fully read
    stop = None
    for i, f in enumerate(files):
        if f.get("flag") == "lock" and not v.get("skip"): stop = i; break
    if stop is not None: k = min(k, stop)
    a = ease(t / 0.4)
    # left: folder window + tile grid
    lx0, ly0, lx1, ly1 = 90, 150, 900, 990; window(img, [lx0, ly0, lx1, ly1], v.get("folder", "reports/"), kind="term")
    cols = v.get("cols", 16); rows = (n + cols - 1) // cols; gw, gh = lx1 - lx0 - 80, ly1 - ly0 - 190
    tw = min(gw / cols, 110); th = min(gh / rows, tw * 1.1); gx = lx0 + 40 + (gw - tw * cols) / 2; gy = ly0 + 90
    pos = []
    for i, f in enumerate(files):
        r, c = divmod(i, cols); x, y = gx + c * tw, gy + r * th; pos.append((x + tw / 2, y + th / 2))
        fl = f.get("flag", ""); done = i < k; err = stop is not None and i == stop and t >= t_of(i) - 0.05
        col = CORAL if (fl == "lock") else (YEL if fl == "qty" and v.get("naive") else ACC)
        if fl == "lock" and v.get("skip"): col = DIM
        fill = mix(PANEL2, col, 0.75) if done or err else PANEL2
        if fl == "lock" and v.get("skip") and done: fill = PANEL
        dr.rounded_rectangle([x + 3, y + 3, x + tw - 3, y + th - 3], max(3, int(tw / 9)), fill=mix(BG, fill, a), outline=mix(BG, col if (done or err) else LINE, a), width=1 if tw < 60 else 2)
        if tw >= 30:  # tiny spreadsheet glyph
            gc = mix(fill, BG, 0.45)
            for j in range(3): dr.line([x + tw * 0.25, y + th * (0.32 + j * 0.18), x + tw * 0.75, y + th * (0.32 + j * 0.18)], fill=gc, width=max(1, int(tw / 22)))
        if (err or (fl == "lock" and v.get("skip") and done)) and tw >= 20:
            dr.line([x + 7, y + 7, x + tw - 7, y + th - 7], fill=CORAL, width=3); dr.line([x + tw - 7, y + 7, x + 7, y + th - 7], fill=CORAL, width=3)
        if tw >= 90: text_a(img, (x + tw / 2, y + th - 14), f["name"][:12], F(14, "mono"), TXT, a, "mm")
    text_a(img, ((lx0 + lx1) / 2, ly1 - 60), f"{n} files", F(26, "SemiBold"), DIM, a, "mm")
    # right: combined sheet
    rx0, ry0, rx1, ry1 = 960, 150, 1840, 990; window(img, [rx0, ry0, rx1, ry1], v.get("out", "all_sales.xlsx"), kind="term")
    hdr = ["Date", "Product", "Units", "Price", "Source"]; cw = [150, 150, 90, 90, 330]; cx = [rx0 + 30]
    for w_ in cw: cx.append(cx[-1] + w_)
    hy = ry0 + 72; rh = 40
    dr.rectangle([rx0 + 20, hy, rx1 - 20, hy + rh], fill=mix(BG, PANEL2, a))
    for j, h_ in enumerate(hdr): text_a(img, (cx[j] + 10, hy + rh / 2), h_, F(22, "SemiBold"), ACC, a, "lm")
    if v.get("naive") and k > 0 and any(f.get("flag") == "qty" for f in files[:k]):
        dr.rectangle([rx1 - 110, hy, rx1 - 20, hy + rh], fill=mix(PANEL2, YEL, 0.3)); text_a(img, (rx1 - 65, hy + rh / 2), "Qty", F(22, "SemiBold"), YEL, 1, "mm")
    nb = 7; blocks = [b for b in range(k) if files[b].get("flag") != "lock"][-nb:]; fs = F(21, "mono"); y = hy + rh + 6
    for b in blocks:
        f = files[b]; s = f["sample"][0]; col = MCOL[b % len(MCOL)]; fresh = max(0.0, min(1.0, (t - t_of(b)) / 0.25))
        dr.rectangle([rx0 + 20, y, rx0 + 26, y + rh * 2 - 8], fill=col)
        units = "NaN" if (f.get("flag") == "qty" and v.get("naive")) else str(s[2])
        vals = [s[0], s[1], units, f"{s[3]:.2f}", f["name"]]
        for j, val in enumerate(vals):
            c = YEL if (val == "NaN") else (col if j == 4 else TXT)
            if j in (2, 3): text_a(img, (cx[j + 1] - 12, y + rh / 2 - 4), val, fs, c, fresh, "rm")
            else: text_a(img, (cx[j] + 10, y + rh / 2 - 4), val, fs, c, fresh, "lm")
        if v.get("naive") and f.get("flag") == "qty": text_a(img, (rx1 - 65, y + rh / 2 - 4), str(s[2]), fs, YEL, fresh, "mm")
        text_a(img, (cx[0] + 10, y + rh * 1.5 - 6), f"... {f['rows'] - 1} more rows from this file", F(18, "Medium"), DIM, fresh)
        y += rh * 2
    # counters
    rows_now = sum(f.get("rows", 0) for f in files[:k]); real_n = sum(1 for f in files if f.get("flag") != "lock")
    by = ry1 - 92; dr.rounded_rectangle([rx0 + 20, by, rx1 - 20, by + 66], 14, fill=mix(BG, PANEL2, a))
    nf = sum(1 for f in files[:k] if not (f.get("flag") == "lock"))
    text_a(img, (rx0 + 50, by + 33), f"files read  {nf} / {real_n}", F(26, "monob"), TXT, a, "lm")
    text_a(img, (rx1 - 50, by + 33), f"rows  {rows_now:,}", F(26, "monob"), ACC, a, "rm")
    # flying chips (files read during the last 0.45 s)
    for i in range(max(0, k - 30), min(n, k + 1)):
        if stop is not None and i >= stop: break
        ft = t - (t_of(i) - 0.45); u = ft / 0.45
        if not (0 <= u <= 1): continue
        sx, sy = pos[i]; ex, ey = rx0 + 40, hy + rh + 6 + min(nb, max(1, len(blocks))) * rh * 2 - rh; ue = ease(u)
        mx, my = (sx + ex) / 2, min(sy, ey) - 140
        X = (1 - ue) ** 2 * sx + 2 * (1 - ue) * ue * mx + ue ** 2 * ex; Y = (1 - ue) ** 2 * sy + 2 * (1 - ue) * ue * my + ue ** 2 * ey
        col = MCOL[i % len(MCOL)]
        if span / n > 0.25:
            fw = F(18, "mono").getlength(files[i]["name"]) + 24
            dr.rounded_rectangle([X - fw / 2, Y - 16, X + fw / 2, Y + 16], 16, fill=mix(PANEL, col, 0.35), outline=col, width=2)
            dr.text((X, Y), files[i]["name"], font=F(18, "mono"), fill=TXT, anchor="mm")
        else: dr.ellipse([X - 7, Y - 7, X + 7, Y + 7], fill=col)
    if stop is not None and t >= t_of(stop):
        e = v.get("error", "Error"); fe = F(26, "SemiBold"); ew = fe.getlength(e) + 60; ey0 = 1000
        ka = ease((t - t_of(stop)) / 0.3)
        dr.rounded_rectangle([W / 2 - ew / 2, ey0, W / 2 + ew / 2, ey0 + 56], 28, fill=mix(BG, CORAL, ka)); dr.text((W / 2, ey0 + 28), e, font=fe, fill=BG, anchor="mm")
    elif v.get("note") and t > t0 + span:
        ka = ease((t - t0 - span) / 0.4); fe = F(28, "SemiBold"); ew = fe.getlength(v["note"]) + 60
        dr.rounded_rectangle([W / 2 - ew / 2, 1000, W / 2 + ew / 2, 1056], 28, fill=mix(BG, ACC, ka)); dr.text((W / 2, 1028), v["note"], font=fe, fill=BG, anchor="mm")

# ---- EP15: clean - a REAL messy table (rows from clean.json) on the right, the cleaning steps on a rail at the left. Each step
# lights its chip, a scan bar sweeps the columns it touches: every cell that really changes flashes and morphs old -> new,
# extra spaces are drawn as visible dots, NaN cells glow, removed rows get struck through and collapse; per-step badges and the
# bottom counters show the REAL whole-file numbers (cells changed, rows removed, rows left).
def _vis_spaces(s):
    if s == "NaN" or s.strip() == s: return s, 0, 0
    l = len(s) - len(s.lstrip(" ")); r = len(s) - len(s.rstrip(" ")); return "·" * l + s.strip() + "·" * r, l, r
def sc_clean(img, v, t, d):
    data = v["data"]; steps = data["steps"]; cols = data["cols"]; rows = data["rows"]
    frm, upto = v.get("frm", 0), v.get("upto", len(steps)); ns = max(1, upto - frm)
    t0 = 0.6; span = d * v.get("span", 0.75); slot = span / ns
    cur = frm + int(max(0, t - t0) // slot) if t > t0 else frm; u = ((t - t0) % slot) / slot if t > t0 else 0.0
    if t >= t0 + span: cur, u = upto, 0.0
    a = ease(t / 0.4); dr = ImageDraw.Draw(img); col_hi = v.get("color", ACC)
    # left rail
    text_a(img, (60, 165), v.get("rail", "CLEANING STEPS"), F(24, "Bold"), DIM, a)
    for i, st in enumerate(steps):
        y = 210 + i * 128; done = i < cur; act = i == cur and cur < upto and t > t0
        on = done or act; c = col_hi if on else LINE
        dr.rounded_rectangle([50, y, 510, y + 112], 16, fill=mix(BG, mix(PANEL, col_hi, 0.16) if act else PANEL, a), outline=mix(BG, c, a), width=3 if act else 2)
        dr.ellipse([70, y + 18, 110, y + 58], fill=mix(BG, col_hi if on else PANEL2, a))
        text_a(img, (90, y + 38), "✓" if done else str(i + 1), F(22, "monob"), BG if on else DIM, a, "mm")
        text_a(img, (126, y + 38), st["name"], F(25, "SemiBold"), TXT if on or i >= frm else DIM, a, "lm")
        fc = 17
        while F(fc, "mono").getlength(st["code"]) > 420 and fc > 12: fc -= 1
        text_a(img, (72, y + 86), st["code"], F(fc, "mono"), mix(DIM, col_hi, 0.5) if on else (90, 98, 115), a, "lm")
        if done or (act and u > 0.7):
            k = 1.0 if done else ease((u - 0.7) / 0.2)
            lab = (f"-{st['removed']} rows" if st["removed"] and not st["changed"] else
                   f"{st['changed']:,} cells" + (f" · -{st['removed']} rows" if st["removed"] else ""))
            fb = F(18, "Bold"); bw = fb.getlength(lab) + 24
            dr.rounded_rectangle([490 - bw, y - 12, 490, y + 18], 15, fill=mix(BG, CORAL if st["removed"] else col_hi, k))
            text_a(img, (490 - bw / 2, y + 3), lab, fb, BG, k, "mm")
    # table window
    x0, y0, x1, y1 = 560, 150, 1870, 990; window(img, [x0, y0, x1, y1], v.get("file", "orders.csv"), kind="term")
    fs = F(22, "mono"); cw = fs.getlength("M")
    widths = [cw * 4 + 20]
    for j, c in enumerate(cols):
        m = max([len(c)] + [len(_vis_spaces(r["vals"][k][j])[0]) for r in rows for k in range(len(r["vals"])) if r["vals"][k]])
        widths.append(cw * m + 26)
    sc = min(1.0, (x1 - x0 - 50) / sum(widths)); widths = [w_ * sc for w_ in widths]
    cx = [x0 + 25]
    for w_ in widths: cx.append(cx[-1] + w_)
    hy = y0 + 70; rh = 52
    touched = steps[cur]["cols"] if cur < upto and t > t0 else []
    for j, c in enumerate(cols):
        if c in touched:
            dr.rectangle([cx[j + 1] + 2, hy, cx[j + 2] - 2, hy + rh * 12], fill=mix(PANEL, col_hi, 0.10))
    dr.rectangle([x0 + 20, hy, x1 - 20, hy + rh - 10], fill=PANEL2)
    text_a(img, (cx[0] + 8, hy + rh / 2 - 5), "", fs, DIM)
    for j, c in enumerate(cols): text_a(img, (cx[j + 1] + 12, hy + rh / 2 - 5), c, F(22, "monob"), col_hi if c in touched else TXT, 1, "lm")
    def alive(r, k): return r["vals"][min(k, len(r["vals"]) - 1)] is not None
    k0 = cur; k1 = min(cur + 1, len(steps)) if cur < upto else cur
    coll = ease((u - 0.72) / 0.25) if (cur < upto and t > t0) else 0.0
    scan_y = hy + rh + u / 0.7 * rh * 11 if u < 0.7 else None
    pa = pb = 0
    for r in rows:
        if not alive(r, k0): continue
        ya = hy + rh + pa * rh; yb = hy + rh + pb * rh
        gone = not alive(r, k1)
        y = ya if not coll else (ya + (yb - ya) * coll)
        passed = (u >= 0.7) or (scan_y is not None and scan_y > ya + rh / 2) or cur >= upto
        if cur >= upto: passed = False
        before = r["vals"][k0]; after = r["vals"][k1] if not gone else before
        ra = 1.0 - (coll if gone else 0)
        if ra <= 0.02: pa += 1; continue
        text_a(img, (cx[0] + 8, y + rh / 2 - 5), str(r["idx"]), fs, (90, 98, 115), ra, "lm")
        for j, c in enumerate(cols):
            old, new = before[j], after[j]; ch = passed and old != new
            k = ease((t - t0 - (cur - frm) * slot - slot * min(0.7, max(0, (ya - hy - rh) / (rh * 11)) * 0.7)) / 0.35) if ch else 0
            val = new if (ch and k > 0.5) else old
            sv, l, rr = _vis_spaces(val)
            if ch:
                fl = 1 - abs(k - 0.5) * 2
                dr.rounded_rectangle([cx[j + 1] + 4, y + 4, cx[j + 2] - 4, y + rh - 14], 8, fill=mix(PANEL, col_hi if k > 0.5 else CORAL, 0.25 + 0.35 * fl))
            base = TXT if not ch else (col_hi if k > 0.5 else CORAL)
            if val == "NaN": base = mix(CORAL, YEL, 0.5) if not ch else base
            xx = cx[j + 1] + 12
            if l or rr:
                text_a(img, (xx, y + rh / 2 - 5), "·" * l, fs, CORAL, ra, "lm"); xx2 = xx + fs.getlength("·" * l)
                text_a(img, (xx2, y + rh / 2 - 5), val.strip(), fs, base, ra, "lm"); xx3 = xx2 + fs.getlength(val.strip())
                text_a(img, (xx3, y + rh / 2 - 5), "·" * rr, fs, CORAL, ra, "lm")
            else:
                text_a(img, (xx, y + rh / 2 - 5), sv, fs, base, ra * (1 if not (ch and abs(k - 0.5) < 0.12) else 0.4), "lm")
        if gone and passed:
            ka = ease((u - (ya - hy - rh) / (rh * 11) * 0.7) / 0.1) if u < 0.72 else 1
            dr.line([cx[0], y + rh / 2 - 5, cx[0] + (cx[-1] - cx[0]) * ka, y + rh / 2 - 5], fill=CORAL, width=3)
        pa += 1
        if not gone: pb += 1
    if scan_y is not None and cur < upto and t > t0:
        dr.rectangle([x0 + 20, scan_y - 2, x1 - 20, scan_y + 2], fill=col_hi)
    # counters (REAL whole-file numbers)
    nrows = data["rows0"] if cur == 0 else steps[cur - 1]["rows"]
    fixed = sum(s_["changed"] for s_ in steps[:cur]); by = y1 - 90
    dr.rounded_rectangle([x0 + 20, by, x1 - 20, by + 66], 14, fill=PANEL2)
    text_a(img, (x0 + 50, by + 33), f"rows  {data['rows0']:,}  →  {nrows:,}", F(26, "monob"), TXT, a, "lm")
    text_a(img, (x1 - 50, by + 33), f"cells fixed  {fixed:,}", F(26, "monob"), col_hi, a, "rm")
    text_a(img, ((x0 + x1) / 2 + 60, by - 22), f"showing {len(rows)} of the {data['rows0']:,} rows  ·  real values", F(18, "Medium"), DIM, a, "mm")
    if v.get("note") and t > t0 + span:
        ka = ease((t - t0 - span) / 0.4); fe = F(28, "SemiBold"); ew = fe.getlength(v["note"]) + 60
        dr.rounded_rectangle([W / 2 - ew / 2, 1000, W / 2 + ew / 2, 1056], 28, fill=mix(BG, col_hi, ka)); dr.text((W / 2, 1028), v["note"], font=fe, fill=BG, anchor="mm")

# ---- EP16: xlsx - a REAL workbook read back with openpyxl (demo/ep16/xlsx.json): formula bar (name box + formula of the selected cell),
#      column letters / row numbers, the real column widths, bold / font color / fill of every cell, number formats, frozen header line,
#      sheet tabs at the bottom (active one in accent). build=True drops rows in top-down; morph=<plain book> morphs the unformatted
#      workbook into the formatted one (widths grow, header fills fade in, numbers switch to their format); sel="B9" selects a cell.
def _hexrgb(s, dflt):
    if not s or len(s) < 6: return dflt
    s = s[-6:]; return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))
def sc_xlsx(img, v, t, d):
    book = v["data"][v.get("book", "report.xlsx")]; sh = book[v["sheet"]]; plain = v["data"][v["morph"]][v["sheet"]] if v.get("morph") else None
    span = d * v.get("span", 0.5); k = ease((t - 0.6) / span) if plain else 1.0
    rows = sh["rows"]; nr = min(len(rows), v.get("rows", 12)); nc = min(max(len(r) for r in rows), v.get("cols", 9))
    a = ease(t / 0.4); dr = ImageDraw.Draw(img)
    if v.get("title"): text_a(img, (W / 2, 150), v["title"], F(44, "Bold"), TXT, a, "mm")
    X0, X1 = 130, W - 130; Y0 = 200 if v.get("title") else 150; Y1 = 1000
    window(img, [X0, Y0, X1, Y1], v.get("win", v.get("book", "report.xlsx")), kind="term", a=a)
    # formula bar
    sel = v.get("sel"); scell = None
    if sel:
        cc = ord(sel[0]) - 65; rr = int(sel[1:]) - 1
        if rr < len(rows) and cc < len(rows[rr]): scell = rows[rr][cc]
    fy = Y0 + 66; dr.rounded_rectangle([X0 + 20, fy, X1 - 20, fy + 50], 8, fill=PANEL, outline=LINE, width=2)
    dr.rectangle([X0 + 22, fy + 2, X0 + 140, fy + 48], fill=PANEL2); dr.text((X0 + 81, fy + 25), sel or "A1", font=F(22, "monob"), fill=TXT, anchor="mm")
    dr.text((X0 + 172, fy + 25), "fx", font=F(24, "Medium"), fill=DIM, anchor="mm")
    if scell is not None:
        ftxt = scell["formula"] or scell["v"]; kk = ease((t - 0.8) / 0.5)
        dr.text((X0 + 214, fy + 25), ftxt[:int(len(ftxt) * kk + 0.999)] if kk > 0 else "", font=F(26, "mono"), fill=ACC if scell["formula"] else TXT, anchor="lm")
    # grid geometry: real widths (Excel default 8.43) lerp from the plain book while morphing
    def wcol(b, L): return (b["widths"].get(L) or 8.43) if b else 8.43
    letters = [chr(65 + i) for i in range(nc)]
    ws_ = [wcol(plain, L) * (1 - k) + wcol(sh, L) * k for L in letters]
    wmax = [max(wcol(plain, L), wcol(sh, L)) for L in letters]  # zoom fixed by the widest version, so columns visibly grow while morphing
    gx0, gy0 = X0 + 20 + 64, fy + 70; avail = X1 - 20 - gx0; zoom = min(v.get("zoom", 13.5), avail / sum(wmax))
    xs = [gx0]
    for w_ in ws_: xs.append(xs[-1] + w_ * zoom)
    rh = min(v.get("rh", 52), (Y1 - 70 - gy0 - 40) / (nr + 0.5)); fs = int(min(36, rh * 0.52, zoom * 0.95 * 100 / F(100, "Regular").getlength("0")))
    gx1 = min(xs[-1], X1 - 20)
    dr.rectangle([X0 + 20, gy0, gx1, gy0 + 36], fill=PANEL2)
    for i, L in enumerate(letters):
        if xs[i] >= X1 - 20: break
        hl = sel and sel[0] == L
        dr.rectangle([xs[i], gy0, min(xs[i + 1], X1 - 20), gy0 + 36], fill=mix(PANEL2, ACC, 0.35) if hl else PANEL2, outline=LINE)
        dr.text(((xs[i] + min(xs[i + 1], X1 - 20)) / 2, gy0 + 18), L, font=F(20, "Medium"), fill=TXT if hl else DIM, anchor="mm")
    step = span / max(1, nr) if v.get("build") else 0
    for r in range(nr):
        ry = gy0 + 36 + r * rh; ra = ease((t - 0.4 - r * step) / 0.3) if v.get("build") else 1.0
        dr.rectangle([X0 + 20, ry, gx0, ry + rh], fill=PANEL2, outline=LINE)
        dr.text((X0 + 20 + 32, ry + rh / 2), str(r + 1), font=F(19, "Medium"), fill=DIM, anchor="mm")
        for c in range(nc):
            if xs[c] >= X1 - 20: break
            cx0, cx1 = xs[c], min(xs[c + 1], X1 - 20)
            cell = rows[r][c] if c < len(rows[r]) else None; pc = plain["rows"][r][c] if plain and r < len(plain["rows"]) and c < len(plain["rows"][r]) else None
            fillc = _hexrgb(cell and cell["fill"], None) if cell else None
            base = (250, 250, 248); bg = base
            if fillc: bg = mix(base, fillc, k)
            if sel and r == rr and c == cc and t > 0.6: bg = mix(bg, ACC, 0.25)
            dr.rectangle([cx0, ry, cx1, ry + rh], fill=mix(BG, bg, ra), outline=mix(BG, (214, 216, 220), ra))
            if ra <= 0.05 or cell is None: continue
            if plain and pc is None and k < 0.5: continue  # cell only exists in the formatted file (e.g. the Total row)
            show = cell if (k >= 0.5 or not pc) else pc
            txt = show["v"]
            if not txt: continue
            bold = show["b"]; col = _hexrgb(show["fc"], (30, 32, 36)) if show["fc"] and (fillc or k >= 0.5) and show["fc"][-6:] != "000000" else (30, 32, 36)
            if col == (255, 255, 255) and not (fillc and k >= 0.3): col = (30, 32, 36)
            f = F(fs, "Bold" if bold else "Regular"); room = cx1 - cx0 - 12
            if show["num"]:  # fit in Excel width units (width of "0"): General numbers lose decimals, formatted numbers/dates become ####
                wch = (cx1 - cx0) / zoom; u = lambda s_: f.getlength(s_) / f.getlength("0")
                if show["nf"] == "General" and "." in txt and ":" not in txt:
                    x_ = float(txt.replace(",", "")); dec = len(txt.split(".")[1])
                    while u(txt) > wch - 0.6 and dec > 0: dec -= 1; txt = f"{round(x_, dec):.{dec}f}"  # Excel rounds General numbers to fit
                if u(txt) > wch - 0.6: txt = "#" * max(1, int(wch - 0.6))
            while f.getlength(txt) > room and len(txt) > 1: txt = txt[:-1]
            if show["num"]: dr.text((cx1 - 6, ry + rh / 2), txt, font=f, fill=mix(BG, col, ra), anchor="rm")
            else: dr.text((cx0 + 6, ry + rh / 2), txt, font=f, fill=mix(BG, col, ra), anchor="lm")
        if sel and r == rr and t > 0.6 and cc < nc:
            dr.rectangle([xs[cc], ry, min(xs[cc + 1], X1 - 20), ry + rh], outline=ACC, width=4)
    if sh.get("freeze") == "A2" and k > 0.5:
        yy = gy0 + 36 + rh; dr.line([X0 + 20, yy, gx1, yy], fill=mix((214, 216, 220), (90, 96, 108), k), width=3)
    if sh["max_row"] > nr:
        text_a(img, (gx0 + 10, gy0 + 36 + nr * rh + 6), f"… {sh['max_row'] - nr} more rows", F(20, "Medium"), DIM, a)
    # sheet tabs
    ty = Y1 - 56; tx = X0 + 30
    for name in v["data"][v.get("book", "report.xlsx")].keys():
        on = name == v["sheet"]; tw = F(22, "SemiBold").getlength(name) + 44
        dr.rounded_rectangle([tx, ty, tx + tw, ty + 40], 8, fill=mix(PANEL, ACC, 0.9) if on else PANEL2, outline=ACC if on else LINE, width=2)
        dr.text((tx + tw / 2, ty + 20), name, font=F(22, "SemiBold"), fill=BG if on else DIM, anchor="mm"); tx += tw + 10
    if v.get("note"):
        na = ease((t - 0.8 - span) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if na > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 1012, W / 2 + tw / 2 + 30, 1066], 27, fill=mix(BG, v.get("notecol", ACC), na)); dr.text((W / 2, 1039), v["note"], font=fn, fill=BG, anchor="mm")

# ---- EP16: group - groupby made visible. Left: the REAL rows of the table streaming by (order, city, revenue); each row's revenue flies
#      as a chip into its city bucket on the right, where a bar and a running total grow. Slow for the first rows, then fast-forward to
#      the end; the running totals are the REAL cumulative sums (row order of the file) and end exactly at the real groupby result.
def sc_group(img, v, t, d):
    S = v["stream"]; N = len(S); tot = v["totals"]; cities = list(tot.keys()); dr = ImageDraw.Draw(img)
    span = d * v.get("span", 0.7); slow = v.get("slow", 8); ts_ = min(span * 0.45, slow * 0.55); t0 = 0.6
    if t < t0: p = 0.0
    elif t < t0 + ts_: p = slow * (t - t0) / ts_
    else: p = slow + (N - slow) * ease(min(1.0, (t - t0 - ts_) / max(0.1, span - ts_)) ) ** 1.0
    n = int(min(N, p)); frac = p - n
    a = ease(t / 0.4)
    code = v.get("code", 'df.groupby("City")["Revenue"].sum()'); fc = F(32, "mono"); cw = fc.getlength(code)
    dr.rounded_rectangle([W / 2 - cw / 2 - 30, 128, W / 2 + cw / 2 + 30, 192], 14, fill=mix(BG, PANEL, a), outline=mix(BG, ACC, a), width=2)
    cx = W / 2 - cw / 2
    for s_, c_ in colorize(code): dr.text((cx, 160), s_, font=fc, fill=c_, anchor="lm"); cx += fc.getlength(s_)
    # left: table rows
    LX0, LX1, LY0, LY1 = 90, 760, 230, 1000; window(img, [LX0, LY0, LX1, LY1], v.get("win", "orders_clean.csv"), kind="term", a=a)
    fr = F(24, "mono"); rh = 46; vis = 13; top = max(0, n - vis + 3)
    dr.text((LX0 + 30, LY0 + 76), "Order   City      Revenue", font=F(24, "monob"), fill=DIM, anchor="lm")
    for j in range(vis):
        i = top + j
        if i >= N: break
        y = LY0 + 116 + j * rh; city, rev, oid = S[i][0], S[i][1], S[i][2]
        cur = i == n and n < N; done = i < n
        if cur: dr.rounded_rectangle([LX0 + 16, y - 20, LX1 - 16, y + 20], 8, fill=mix(PANEL, ACC, 0.28))
        col = ACC if cur else (DIM if done else TXT)
        dr.text((LX0 + 30, y), f"{oid:<7} {city:<9} {rev:>9,.2f}", font=fr, fill=col, anchor="lm")
    dr.text(((LX0 + LX1) / 2, LY1 - 34), f"rows read: {n:,} / {N:,}", font=F(26, "SemiBold"), fill=ACC if n >= N else TXT, anchor="mm")
    # right: buckets with running real totals
    cum = {c: 0.0 for c in cities}
    for i in range(n): cum[S[i][0]] += S[i][1]
    mx = max(tot.values()); BX0, BX1 = 860, 1820; by0 = 250; bh = min(96, 740 / len(cities))
    for j, c in enumerate(cities):
        y = by0 + j * bh; ca = ease((t - 0.2 - j * 0.06) / 0.4)
        text_a(img, (BX0, y + bh / 2 - 6), c, F(30, "SemiBold"), TXT, ca, "lm")
        x0 = BX0 + 190; full = BX1 - 230 - x0
        dr.rounded_rectangle([x0, y + bh / 2 - 26, x0 + full, y + bh / 2 + 14], 10, fill=mix(BG, PANEL, ca))
        wv = full * cum[c] / mx
        if wv > 2: dr.rounded_rectangle([x0, y + bh / 2 - 26, x0 + wv, y + bh / 2 + 14], 10, fill=ACC if n >= N else mix(ACC, SKY, 0.35))
        hit = n < N and n > 0 and S[n - 1][0] == c and frac < 0.5
        dr.text((BX1, y + bh / 2 - 6), f"{cum[c]:,.2f}", font=F(28, "monob"), fill=(YEL if hit else (ACC if n >= N else TXT)), anchor="rm")
    # flying chip (only during the slow part)
    if n < min(N, slow + 1) and t > t0:
        city, rev = S[n][0], S[n][1]; j = top and (n - top) or n
        sy = LY0 + 116 + (n - top) * rh; ty_ = by0 + cities.index(city) * bh + bh / 2 - 6
        q = ease(frac); x = LX1 - 140 + (BX0 + 190 - (LX1 - 140)) * q; y = sy + (ty_ - sy) * q
        lab = f"+{rev:,.2f}"; fl = F(24, "monob"); lw = fl.getlength(lab) + 28
        dr.rounded_rectangle([x - lw / 2, y - 20, x + lw / 2, y + 20], 20, fill=ACC); dr.text((x, y), lab, font=fl, fill=BG, anchor="mm")
    if v.get("note"):
        na = ease((t - 0.6 - span - 0.3) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if na > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, 1012, W / 2 + tw / 2 + 30, 1066], 27, fill=mix(BG, ACC, na)); dr.text((W / 2, 1039), v["note"], font=fn, fill=BG, anchor="mm")


# ---- EP17: scrape - a REAL Chromium screenshot of the page in a browser window (left), a CSS selector bar on top; every element the
#      selector REALLY matches (bounding boxes measured by Playwright, demo/ep17/boxes.json) lights up one by one with a numbered badge,
#      while the value BeautifulSoup really extracted from it lands as a row in the "Python sees" table on the right (live counter).
#      inner= a second selector outlined inside the boxes in another color. mode="inspect": DevTools-style - one element hovered on the
#      page, its HTML source on the right with the element's lines highlighted. mode="nojs": right side shows what requests downloads
#      (a second REAL screenshot taken with JavaScript off) next to what the browser shows.
def _browser(img, box, shot, url, crop=None, a=1.0):
    x0, y0, x1, y1 = box
    window(img, box, "Pine Street Books", kind="term")
    dr = ImageDraw.Draw(img); ay = y0 + 62
    dr.rounded_rectangle([x0 + 14, ay, x1 - 14, ay + 40], 20, fill=(38, 42, 52)); dr.text((x0 + 40, ay + 20), url, font=F(19, "mono"), fill=DIM, anchor="lm")
    if shot not in _imc: _imc[shot] = Image.open(shot).convert("RGBA")
    src = _imc[shot]
    if crop: src = src.crop((0, int(crop[0] * src.height), src.width, int(crop[1] * src.height)))
    iw = x1 - x0 - 24; ih = int(src.height * iw / src.width); py = ay + 52; ph = y1 - py - 12
    pic = src.resize((iw, ih), Image.LANCZOS).crop((0, 0, iw, min(ih, ph))); img.alpha_composite(pic, (x0 + 12, py))
    return x0 + 12, py, iw, ih

def sc_scrape(img, v, t, d):
    BX = v["boxes"]; mode = v.get("mode", "select"); dr = ImageDraw.Draw(img); a0 = ease(t / 0.4)
    # selector bar
    sel = v.get("code", f'soup.select("{v.get("sel", "")}")'); fs = F(40, "monob"); sw = fs.getlength(sel)
    dr.rounded_rectangle([W / 2 - sw / 2 - 36, 112, W / 2 + sw / 2 + 36, 192], 20, fill=mix(BG, PANEL, a0), outline=mix(BG, ACC, a0), width=3)
    text_a(img, (W / 2 - sw / 2 - 36, 104), v.get("label", "CSS SELECTOR"), F(20, "Bold"), ACC, a0, "ls")
    cx = W / 2 - sw / 2; sl = v.get("hilite", v.get("sel", ""))
    i0 = sel.find(sl) if sl else -1
    for k, ch in enumerate(sel):
        col = ACC if (i0 >= 0 and i0 <= k < i0 + len(sl)) else (200, 206, 216)
        text_a(img, (cx, 152), ch, fs, col, a0, "lm"); cx += fs.getlength(ch)
    url = v.get("url", "localhost:8000/catalog/page-1.html")
    wide = mode == "inspect" or mode == "nojs"
    bbox = [50, 230, 1010 if not wide else 960, 1012]
    if v.get("bcrop"): bbox[3] = v.get("bh", 1012)
    px, py, iw, ih = _browser(img, bbox, v["shot"], url, crop=v.get("bcrop"))
    c0, c1 = v.get("bcrop", (0, 1))
    def R(b):  # page fraction box -> screen rect (respecting the vertical crop)
        fy0, fy1 = (b[1] - c0) / (c1 - c0), (b[1] + b[3] - c0) / (c1 - c0)
        return [px + b[0] * iw, py + fy0 * ih, px + (b[0] + b[2]) * iw, py + fy1 * ih]
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    clip = py + min(ih, bbox[3] - 12 - py)
    if mode == "inspect":
        r = R(BX[v["sel"]][v.get("pick", 0)]); k = ease((t - 0.5) / 0.4)
        if k > 0 and r[1] < clip:
            dl.rectangle(r, fill=SKY + (int(70 * k),), outline=SKY + (255,), width=3)
            tag = v.get("tag", v["sel"]); ft = F(20, "monob"); tw = ft.getlength(tag) + 24
            dl.rounded_rectangle([r[0], r[1] - 34, r[0] + tw, r[1] - 4], 8, fill=(20, 22, 28, int(235 * k))); dl.text((r[0] + 12, r[1] - 19), tag, font=ft, fill=SKY + (255,), anchor="lm")
        img.alpha_composite(lay)
        hl = v.get("hl", ()); box = [990, 230, 1870, 1012]; window(img, box, "Elements  (right-click > Inspect)", kind="term")
        size = 22; f = F(size, "mono"); lh = int(size * 1.55); mc = int((box[2] - box[0] - 70) // f.getlength("M"))
        vis = []  # long source lines wrap like DevTools (continuation indented), highlight follows the source line
        for i, ln in enumerate(v["src"]):
            ind = len(ln) - len(ln.lstrip()) + 4; first = True
            while ln:
                cut = len(ln) if len(ln) <= mc else (ln.rfind(" ", 0, mc) if ln.rfind(" ", ind + 1, mc) > 0 else mc)
                vis.append((i + 1, ln[:cut], first)); ln = ln[cut:].lstrip(); first = False
                if ln: ln = " " * ind + ln
        for j, (i, ln, first) in enumerate(vis):
            yy = 306 + j * lh
            if i in hl and t > 0.9: dr.rectangle([box[0] + 4, yy - 5, box[2] - 4, yy + lh - 6], fill=mix(PANEL, SKY, 0.28)); dr.rectangle([box[0] + 4, yy - 5, box[0] + 10, yy + lh - 6], fill=SKY)
            xx = box[0] + 30
            for s_, c_ in colorize(ln, "html"): dr.text((xx, yy), s_, font=f, fill=c_); xx += f.getlength(s_)
    elif mode == "nojs":
        img.alpha_composite(lay)
        box = [990, 230, 1870, bbox[3]]
        x0, y0, iw2, ih2 = _browser(img, box, v["shot2"], url, crop=v.get("bcrop"))
        for (bx, lab, col) in ((bbox, "BROWSER (runs JavaScript)", LIME), (box, "requests (raw HTML only)", CORAL)):
            fl = F(22, "Bold"); lw = fl.getlength(lab) + 40; mx = (bx[0] + bx[2]) / 2
            dr.rounded_rectangle([mx - lw / 2, bx[3] - 56, mx + lw / 2, bx[3] - 14], 21, fill=col); dr.text((mx, bx[3] - 35), lab, font=fl, fill=BG, anchor="mm")
        if v.get("ring"):
            k = ease((t - 0.8) / 0.4)
            if k > 0:
                for (xx0, yy0, ww, hh, col) in ((px, py, iw, ih, LIME), (x0, y0, iw2, ih2, CORAL)):
                    b = BX[v["ring"]][0]; fy0 = (b[1] - c0) / (c1 - c0); fy1 = (b[1] + b[3] - c0) / (c1 - c0)
                    dr.rounded_rectangle([xx0 + b[0] * ww - 6, yy0 + fy0 * hh - 6, xx0 + (b[0] + b[2]) * ww + 6, yy0 + fy1 * hh + 6], 10, outline=col, width=4)
    else:
        boxes = BX[v["sel"]]; rows = v.get("rows", []); n = len(boxes); span = d * v.get("span", 0.62); t1 = 0.7
        gap = span / max(1, n); shown = sum(1 for k in range(n) if t >= t1 + k * gap)
        for k in range(shown):
            r = R(boxes[k]); hot = k == shown - 1 and t < t1 + shown * gap + 0.25
            if r[1] > clip: continue
            r[3] = min(r[3], clip)
            dl.rectangle(r, fill=ACC + (90 if hot else 38,), outline=ACC + (255,), width=4 if hot else 3)
            if v.get("inner"):
                for b in BX[v["inner"]]:
                    if boxes[k][0] <= b[0] <= boxes[k][0] + boxes[k][2] and boxes[k][1] <= b[1] <= boxes[k][1] + boxes[k][3]:
                        ri = R(b); dl.rectangle([ri[0] - 3, ri[1] - 3, ri[2] + 3, min(clip, ri[3] + 3)], outline=YEL + (255,), width=3)
            fb = F(22, "Bold"); dl.ellipse([r[0] - 14, r[1] - 14, r[0] + 22, r[1] + 22], fill=ACC + (255,)); dl.text((r[0] + 4, r[1] + 4), str(k + 1), font=fb, fill=BG + (255,), anchor="mm")
        img.alpha_composite(lay)
        # "Python sees" table
        box = [1040, 230, 1870, 1012]; dr.rounded_rectangle(box, 18, fill=PANEL, outline=LINE, width=2)
        dr.text((box[0] + 30, box[1] + 36), v.get("panel", "What Python gets"), font=F(26, "SemiBold"), fill=TXT, anchor="lm")
        lab = f"{shown} matched"; fl = F(24, "Bold"); lw = fl.getlength(lab) + 40
        dr.rounded_rectangle([box[2] - lw - 24, box[1] + 16, box[2] - 24, box[1] + 56], 20, fill=ACC if shown else LINE); dr.text((box[2] - 24 - lw / 2, box[1] + 36), lab, font=fl, fill=BG, anchor="mm")
        cols = v.get("cols", ["#", "value"]); fr = F(v.get("tsize", 24), "mono"); rh = min(76, (box[3] - box[1] - 150) / max(1, len(rows)))
        cw = [max([fr.getlength(str(c))] + [fr.getlength(str(r_[j])) for r_ in rows]) + 34 for j, c in enumerate(cols)]
        sc = min(1.0, (box[2] - box[0] - 60) / sum(cw)); cw = [c * sc for c in cw]
        yh = box[1] + 90; xx = box[0] + 30
        for j, c in enumerate(cols): dr.text((xx + 6, yh), str(c), font=F(20, "Bold"), fill=DIM, anchor="lm"); xx += cw[j]
        dr.line([box[0] + 24, yh + 22, box[2] - 24, yh + 22], fill=LINE, width=2)
        for k, r_ in enumerate(rows[:shown]):
            age = t - (t1 + k * gap); a = ease(age / 0.3); yy = yh + 52 + k * rh; xx = box[0] + 30 + (1 - a) * -60
            if age < 0.6: dr.rounded_rectangle([box[0] + 20, yy - rh / 2 + 4, box[2] - 20, yy + rh / 2 - 4], 10, fill=mix(PANEL, ACC, 0.25 * (1 - age / 0.6)))
            for j, cell in enumerate(r_):
                col = ACC if j == 0 else (TXT if j == 1 else YEL if j == 2 else SKY)
                text_a(img, (xx + 6, yy), str(cell), fr, col, a, "lm"); xx += cw[j]
    if v.get("note"):
        a = ease((t - d * v.get("notet", 0.7)) / 0.5); fn = F(30, "SemiBold"); tw = fn.getlength(v["note"])
        if a > 0: dr.rounded_rectangle([W / 2 - tw / 2 - 30, 1018, W / 2 + tw / 2 + 30, 1068], 25, fill=mix(BG, v.get("notecol", ACC), a)); dr.text((W / 2, 1043), v["note"], font=fn, fill=BG, anchor="mm")

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
