"""Shortcut Lab - software/AI tutorials, drawn 100% by code.
Script (scenes: say + vis) -> Kokoro voice (en-us, am_eric) -> editor / terminal / file-explorer / chat animations -> MP4 1080p24 + SRT.
Usage:
  python3 -I tutor.py ep01.py out/ep01 --preview        # one still per scene (at 85% of the scene)
  python3 -I tutor.py ep01.py out/ep01                  # full render -> final.mp4, subtitles.srt, chapters.txt
  python3 -I tutor.py ep01.py out/ep01 --vertical "0,3,5" "TITLE"   # Short 1080x1920 from scenes (uses cached voice)
Scene types: title, steps, code, term, files, tip, keys, compare, chat, outro
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

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def mix(a, b, t): t = max(0, min(1, t)); return tuple(int(x + (y - x) * t) for x, y in zip(a, b))

# ---------------- background
def make_bg(w=W, h=H):
    img = Image.new("RGB", (w, h), BG); d = ImageDraw.Draw(img)
    for x in range(0, w, 48):
        for y in range(0, h, 48): d.point((x, y), fill=(34, 38, 47))
    g = Image.new("L", (w, h), 0); dg = ImageDraw.Draw(g); dg.ellipse([-w * 0.3, -h * 0.6, w * 0.6, h * 0.5], fill=40)
    g = g.filter(ImageFilter.GaussianBlur(160))
    img = Image.composite(Image.new("RGB", (w, h), (40, 58, 30)), img, g)
    return img.convert("RGBA")

def chrome(img, prog, label=""):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([56, 40, 96, 80], 9, fill=LIME); d.text((76, 60), "⌘", font=F(28, "monob"), fill=BG, anchor="mm")
    d.text((110, 60), BRAND, font=F(22, "SemiBold"), fill=TXT, anchor="lm")
    if label: d.text((W - 60, 60), label, font=F(20, "Medium"), fill=DIM, anchor="rm")
    d.rectangle([0, H - 6, W * prog, H], fill=LIME)

def text_a(img, xy, s, font, fill, a=1.0, anchor="la"):
    if a <= 0: return
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
        d.rectangle([x0 + 110, y0 + 8, x0 + 110 + tw, y0 + 52], fill=PANEL); d.line([x0 + 110, y0 + 8, x0 + 110 + tw, y0 + 8], fill=LIME, width=3)
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

def draw_code(img, x, y, lines, chars, lang, hl=(), lh=44, size=26, a=1.0, cursor=True, t=0, numbers=True):
    d = ImageDraw.Draw(img); f = F(size, "mono"); cw = f.getlength("M"); left = chars
    for i, ln in enumerate(lines):
        yy = y + i * lh
        if (i + 1) in hl and left > 0:
            d.rectangle([x - 16, yy - 6, x + 1474, yy + lh - 8], fill=(46, 60, 34))
            d.rectangle([x - 16, yy - 6, x - 10, yy + lh - 8], fill=LIME)
        if numbers: d.text((x - 70, yy), f"{i + 1:>2}", font=f, fill=(78, 86, 102))
        if left <= 0: continue
        show = ln[:max(0, left)]; left -= len(ln) + 1
        cx = x
        for s, c in colorize(show, lang):
            d.text((cx, yy), s, font=f, fill=c); cx += f.getlength(s)
        if cursor and 0 <= left < 1 + 0 and (int(t * 2) % 2 == 0):
            d.rectangle([cx + 2, yy, cx + 4 + cw * 0.12, yy + size + 6], fill=LIME)
    return left

# ---------------- scenes  (each: sc_x(img, v, t, d))
def sc_title(img, v, t, d):
    a = ease(t / 0.6)
    text_a(img, (W / 2, 330), v.get("kicker", "TUTORIAL").upper(), F(30, "SemiBold"), LIME, a, "mm")
    lines = wrap(v["text"], F(96, "Bold"), 1500)
    for i, ln in enumerate(lines): text_a(img, (W / 2, 450 + i * 116 + (1 - a) * 30), ln, F(96, "Bold"), TXT, a, "mm")
    if v.get("sub"): text_a(img, (W / 2, 470 + len(lines) * 116), v["sub"], F(40, "Regular"), DIM, ease((t - 0.5) / 0.6), "mm")

def sc_steps(img, v, t, d):
    text_a(img, (160, 190), v["title"], F(60, "Bold"), TXT, ease(t / 0.4))
    n = len(v["items"]); per = max(0.6, (d * 0.75) / n)
    for i, it in enumerate(v["items"]):
        a = ease((t - 0.4 - i * per) / 0.4); y = 330 + i * 120
        if a <= 0: continue
        dr = ImageDraw.Draw(img)
        dr.rounded_rectangle([160, y, 1760, y + 96], 18, fill=mix(BG, PANEL, a), outline=mix(BG, LINE, a), width=2)
        dr.rounded_rectangle([184, y + 20, 240, y + 76], 12, fill=mix(BG, LIME, a)); dr.text((212, y + 48), str(i + 1), font=F(32, "Bold"), fill=BG, anchor="mm")
        text_a(img, (272, y + 48), it, F(38, "Medium"), TXT, a, "lm")

def sc_code(img, v, t, d):
    lines = v["code"].strip("\n").split("\n"); lh = v.get("lh", 46); size = v.get("size", 28)
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
    draw_code(img, 270, y0 + 82, lines, int(chars), v.get("lang", "py"), hl, lh, size, t=t)
    if v.get("note"):
        a = ease((t - dur) / 0.5); dr = ImageDraw.Draw(img)
        f = F(32, "SemiBold"); tw = f.getlength(v["note"])
        if a > 0:
            dr.rounded_rectangle([W / 2 - tw / 2 - 30, box[3] + 24, W / 2 + tw / 2 + 30, box[3] + 88], 32, fill=mix(BG, LIME, a))
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
        i = len(shown) - 1; cx = 240 + f.getlength(shown[-1]); dr.rectangle([cx + 2, y0 + 76 + i * lh, cx + 16, y0 + 76 + i * lh + 30], fill=LIME)

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
        col(1040, after, v.get("hdr2", "AFTER"), k, LIME)
        if k > 0: text_a(img, (960, 360 + 35 * len(before)), "→", F(80, "monob"), LIME, k, "mm")
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
        dr.rounded_rectangle([x, 470 + press, x + w, 610 + press], 22, fill=mix(BG, PANEL2, a), outline=mix(BG, LIME, a), width=3)
        text_a(img, (x + w / 2, 540 + press), k, f, TXT, a, "mm")
        if i < len(keys) - 1: text_a(img, (x + w + 35, 540), "+", F(54, "Bold"), DIM, a, "mm")
        x += w + 70
    if v.get("sub"): text_a(img, (W / 2, 720), v["sub"], F(36, "Regular"), DIM, ease((t - 1) / 0.5), "mm")

def sc_compare(img, v, t, d):
    text_a(img, (W / 2, 200), v.get("title", ""), F(56, "Bold"), TXT, ease(t / 0.4), "mm")
    for j, (hdr, items, col) in enumerate([(v["left"][0], v["left"][1], CORAL), (v["right"][0], v["right"][1], LIME)]):
        a = ease((t - 0.3 - j * d * 0.3) / 0.5); x = 200 + j * 800; dr = ImageDraw.Draw(img)
        dr.rounded_rectangle([x, 300, x + 720, 860], 24, fill=mix(BG, PANEL, a), outline=mix(BG, col, a), width=3)
        text_a(img, (x + 40, 350), hdr, F(40, "Bold"), col, a)
        for i, it in enumerate(items):
            for k, ln in enumerate(wrap(it, F(32, "Medium"), 600)[:2]):
                text_a(img, (x + 50, 440 + i * 100 + k * 40), ("• " if k == 0 else "  ") + ln, F(32, "Medium"), TXT, a)

def sc_chat(img, v, t, d):
    box = [260, 150, 1660, 960]; window(img, box, v.get("title", "AI assistant"), kind="term")
    dr = ImageDraw.Draw(img); y = 240
    for k, (who, msg) in enumerate(v["msgs"]):
        start = k * d * 0.35; a = ease((t - start) / 0.4)
        if a <= 0: break
        f = F(30, "Regular"); lines = wrap(msg, f, 980)
        if who == "ai":
            n = int(sum(len(l) for l in lines) * min(1, (t - start) / max(0.5, d * 0.3))); show = []
            for l in lines:
                show.append(l[:max(0, n)]); n -= len(l)
            lines = [l for l in show if l]
        bw = max(f.getlength(l) for l in lines) + 60 if lines else 100; bh = 40 + 44 * max(1, len(lines))
        x = box[2] - 50 - bw if who == "you" else box[0] + 50
        dr.rounded_rectangle([x, y, x + bw, y + bh], 22, fill=mix(PANEL, (54, 70, 36) if who == "you" else PANEL2, a))
        for i, l in enumerate(lines): text_a(img, (x + 30, y + 22 + i * 44), l, f, TXT, a)
        y += bh + 30

def sc_outro(img, v, t, d):
    a = ease(t / 0.6)
    text_a(img, (W / 2, 330), "NEXT ON SHORTCUT LAB", F(30, "SemiBold"), LIME, a, "mm")
    for i, ln in enumerate(wrap(v["next"], F(72, "Bold"), 1500)): text_a(img, (W / 2, 440 + i * 90), ln, F(72, "Bold"), TXT, a, "mm")
    k = ease((t - 0.8) / 0.5); dr = ImageDraw.Draw(img)
    if k > 0:
        dr.rounded_rectangle([W / 2 - 230, 700, W / 2 + 230, 790], 45, fill=mix(BG, CORAL, k)); text_a(img, (W / 2, 745), "SUBSCRIBE", F(40, "Bold"), (255, 255, 255), k, "mm")
        text_a(img, (W / 2, 850), v.get("sub", "One useful tutorial every day."), F(34, "Regular"), DIM, k, "mm")

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
        d.rounded_rectangle([VW / 2 - 150, 90, VW / 2 + 150, 140], 25, fill=LIME); d.text((VW / 2, 115), BRAND, font=F(26, "Bold"), fill=BG, anchor="mm")
        acc = 0
        for s, dd in sel:
            if gt < acc + dd: break
            acc += dd
        sents = [x.strip() for x in re.split(r"(?<=[.?!,])\s+", s["say"]) if x.strip()]; tot_c = sum(len(x) for x in sents); tl = (gt - acc - 0.25) / max(0.1, dd - 0.7) * tot_c; cur = sents[-1]
        for x in sents:
            if tl < len(x): cur = x; break
            tl -= len(x)
        for i, ln in enumerate(wrap(cur, F(56, "Bold"), 940)[:3]): d.text((VW / 2, 1260 + i * 72), ln, font=F(56, "Bold"), fill=YEL if i == 0 else TXT, anchor="mm", stroke_width=3, stroke_fill=BG)
        d.rectangle([0, VH - 10, VW * gt / tot, VH], fill=LIME)
        p.stdin.write(img.convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("vertical ok", round(tot, 1), "s")

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    voice = os.environ.get("VOICE", getattr(ep, "VOICE", "am_eric")); speed = float(os.environ.get("SPEED", getattr(ep, "SPEED", 1.0)))
    scenes = ep.SCENES; BGIMG = make_bg()
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
