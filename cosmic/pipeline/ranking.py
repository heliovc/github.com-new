"""Cosmic Scale — Shorts de ranking "Top 5" (vertical nativo 1080x1920 30fps).
Uso: python3 -I ranking.py rankXX_algo.py out/rankXX [--preview]
Roteiro: TITLE, THEME {accent, accent2, star_col}, HOOK {say, top, sub}, ITEMS [{rank, name, num, unit, source, say, vis{...}}], OUTRO {say}
Visual por item:
  vis.type == "orbits": desenho do Sistema Solar (órbitas em escala) com a estrela crescendo no lugar do Sol até raio vis.au (UA);
                        vis.note = texto curto sobre o que ela engole.
  vis.type == "bignum": só o número grande animado.
  vis.type == "speed": raias de velocidade em escala log (1 km/s -> luz); vis.kms = km/s; item.short = rótulo curto (rank02).
THEME.hook == "streaks": gancho com rastros de velocidade em vez da estrela gigante (rank02).
Tudo desenhado por código; narração Kokoro (VOICE, padrão af_heart); legenda grande queimada.
"""
import sys, os, re, math, json, subprocess, importlib.util, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFilter
import render as R

W, H, FPS = 1080, 1920, 30
HANDLE = "@universeinscale"
F, ease, easeio, mix, lerp = R.F, R.ease, R.easeio, R.mix, R.lerp
ORB = [("Mercury", 0.387), ("Venus", 0.723), ("Earth", 1.0), ("Mars", 1.524), ("Jupiter", 5.203), ("Saturn", 9.537)]
CX, CY, PX_AU = W / 2, 860, 42.0

def load(path):
    spec = importlib.util.spec_from_file_location("rk", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

_bg = None
def bg(t, theme):
    global _bg
    if _bg is None:
        im = R.make_starfield(W, H + 200, 2600, 33).convert("RGBA")
        g = np.zeros((H + 200, W, 4), np.uint8); yy = np.linspace(0, 1, H + 200)[:, None]
        c = np.array(theme.get("tint", (90, 20, 40)), np.float32)
        g[..., :3] = c; g[..., 3] = (np.clip(1 - np.abs(yy - 0.5) * 2, 0, 1) * 70).astype(np.uint8)
        im.alpha_composite(Image.fromarray(g, "RGBA")); _bg = im
    oy = int(t * 8) % 200
    return _bg.crop((0, oy, W, oy + H))

_star = {}
def star_sprite(r, col):
    r = max(2, int(r)); key = (r, col)
    if key not in _star:
        size = int(r * 2.8) + 8
        c0 = tuple(min(255, int(v * 1.25 + 40)) for v in col)
        spr = R.radial(size, [(0, c0 + (255,)), (0.55 / 1.4, col + (255,)), (0.98 / 1.4, tuple(int(v * 0.7) for v in col) + (255,)),
                              (1.0 / 1.4, tuple(int(v * 0.7) for v in col) + (255,)), (1.08 / 1.4, col + (110,)), (1.0, col + (0,))])
        if r > 30:  # convective cells
            rng = np.random.default_rng(r); n = Image.fromarray((rng.random((44, 44)) * 255).astype(np.uint8)).resize((size, size), Image.BICUBIC).filter(ImageFilter.GaussianBlur(max(1, size // 120)))
            a = np.asarray(spr, np.float32); nz = np.asarray(n, np.float32)[..., None] / 255
            yy, xx = np.mgrid[0:size, 0:size]; inside = (np.hypot(xx - size / 2, yy - size / 2) < r)[..., None]
            a[..., :3] = np.where(inside, a[..., :3] * (0.86 + 0.24 * nz), a[..., :3])
            spr = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
        _star[key] = spr
    return _star[key]

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def text(img, xy, s, size, col, w="Black", a=1.0, anchor="mm", stroke=0):
    if a <= 0: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text((xy[0] + 4, xy[1] + 6), s, font=F(size, w), fill=(0, 0, 0, int(170 * a)), anchor=anchor)
    d.text(xy, s, font=F(size, w), fill=tuple(col) + (int(255 * a),), anchor=anchor, stroke_width=stroke, stroke_fill=(0, 0, 0, int(255 * a)))
    img.alpha_composite(lay)

def orbits(img, star_au, prog, col, accent, t):
    d = ImageDraw.Draw(img)
    rs = star_au * PX_AU * ease(prog)
    for name, au in ORB:
        rr = au * PX_AU; eaten = rs >= rr
        oc = (150, 60, 50) if eaten else (90, 110, 160)
        for k in range(0, 360, 4 if au > 2 else 8):
            d.arc([CX - rr, CY - rr, CX + rr, CY + rr], k, k + 2.5, fill=oc, width=2)
    # asteroid belt
    rng = random.Random(5)
    for _ in range(260):
        a = rng.uniform(0, 6.283); au = rng.uniform(2.2, 3.3); x, y = CX + au * PX_AU * math.cos(a), CY + au * PX_AU * math.sin(a)
        d.point((x, y), fill=(120, 110, 100))
    if rs > 1: R.paste_c(img, star_sprite(rs, col), CX, CY)
    else: R.paste_c(img, R.sun_sprite(6), CX, CY)
    d = ImageDraw.Draw(img)
    for i, (name, au) in enumerate(ORB):
        rr = au * PX_AU; ang = -2.2 + i * 0.95 + t * 0.15 / max(0.4, au)
        x, y = CX + rr * math.cos(ang), CY + rr * math.sin(ang)
        eaten = rs >= rr
        if not eaten:
            R.paste_c(img, R.planet_sprite(max(4, R.PRAD[name] // 3), R.PCOL[name], light=(math.cos(ang + math.pi), math.sin(ang + math.pi)), earth=(name == "Earth")), x, y)
        d = ImageDraw.Draw(img)
        if au >= 1.5 or not eaten:
            lab = name + (" (inside)" if eaten else "")
            if au >= 5:
                d.text((CX + rr * 0.72 + 4, CY - rr * 0.72 - 6), lab, font=F(30, "Bold"), fill=(255, 120, 100) if eaten else (200, 210, 235), anchor="lm")
        if eaten and au < 2:
            pass
    # little "Sun" reference marker
    d.text((W - 60, 430), "orbits to scale", font=F(26, "SemiBold"), fill=(150, 160, 190), anchor="rm")

ALL_ITEMS = []
C_KMS = 299792.458
def speed_lanes(img, it, th, t, dur):
    acc = tuple(th["accent"]); acc2 = tuple(th["accent2"])
    x0, x1 = 120, W - 110
    lx = lambda kms: x0 + (x1 - x0) * math.log10(max(1, kms)) / math.log10(C_KMS)
    d = ImageDraw.Draw(img)
    # light line
    d.line([(x1, 450), (x1, 1200)], fill=(255, 240, 160), width=4)
    d.text((x1, 425), "LIGHT", font=F(30, "Black"), fill=(255, 240, 160), anchor="rm")
    for k, lab in [(1, "1 km/s"), (100, "100"), (10000, "10,000")]:
        xx = lx(k); d.line([(xx, 1200), (xx, 1215)], fill=(120, 140, 170), width=2)
        d.text((xx, 1232), lab, font=F(24, "SemiBold"), fill=(120, 140, 170), anchor="mm")
    d.text((W / 2, 1268), "log scale: each tick = 100x faster", font=F(24, "SemiBold"), fill=(120, 140, 170), anchor="mm")
    for o in sorted(ALL_ITEMS, key=lambda x: x["rank"]):
        r = o["rank"]
        if r < it["rank"]: continue
        y = 510 + (r - 1) * 145; cur = r == it["rank"]
        tgt = lx(o["vis"]["kms"])
        p = ease((t - 0.4) / 1.6) if cur else 1.0
        xe = lerp(x0, tgt, p)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.rounded_rectangle([x0, y - 20, x1, y + 20], 20, fill=(20, 40, 70, 150))
        col = acc if cur else (70, 110, 150)
        d2.rounded_rectangle([x0, y - 20, max(x0 + 40, xe), y + 20], 20, fill=col + (255 if cur else 190,))
        if cur:
            for k in range(10):
                xx = xe - 26 * k
                if xx > x0: d2.ellipse([xx - 9, y - 9, xx + 9, y + 9], fill=(255, 255, 255, int(220 * (1 - k / 10))))
        img.alpha_composite(lay)
        d = ImageDraw.Draw(img)
        d.text((x0 + 10, y - 46), f"#{r}  {o.get('short', o['name'])}", font=F(32 if cur else 28, "ExtraBold" if cur else "Bold"), fill=(255, 255, 255) if cur else (150, 170, 200), anchor="lm")

def caption_chunks(say, t0, dur):
    words = say.split(); groups, g = [], []
    for w in words:
        g.append(w)
        if len(g) >= 3 or re.search(r"[.?!,:]$", w): groups.append(" ".join(g)); g = []
    if g: groups.append(" ".join(g))
    total = sum(len(x) for x in groups); t = t0 + 0.2; usable = dur - 0.6; out = []
    for x in groups:
        dd = usable * len(x) / total; out.append((t, t + dd, x.upper().rstrip(".,"))); t += dd
    return out

def draw_caption(img, chunks, gt, y=1585):
    for a, b, s in chunks:
        if a <= gt < b:
            f = F(74, "Black"); lines = wrap(s, f, W - 140)
            for i, l in enumerate(lines):
                d = ImageDraw.Draw(img)
                d.text((W / 2, y + i * 86 - (len(lines) - 1) * 43), l, font=f, fill=(255, 255, 255), anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
            return

def seg_hook(img, sc, th, t, dur):
    col = tuple(th["star_col"]); acc = tuple(th["accent"])
    if th.get("hook") == "streaks":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rng = random.Random(8)
        for i in range(90):
            y = rng.uniform(560, 1500); sp = rng.uniform(900, 2600); L = rng.uniform(120, 520)
            x = (rng.uniform(0, W + L) + t * sp) % (W + L) - L
            d.line([(x, y), (x + L, y)], fill=col + (int(rng.uniform(60, 200)),), width=rng.choice([2, 3, 5]))
        img.alpha_composite(lay)
        bx = W / 2 + 250 * math.sin(t * 0.8); by = 1150
        R.paste_c(img, R.radial(120, [(0, (255, 255, 255, 255)), (0.3, (200, 240, 255, 200)), (1, (90, 200, 255, 0))]), bx, by)
        a = ease(t / 0.4)
        text(img, (W / 2, 250), "TOP 5", 150, acc, a=a)
        for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
            text(img, (W / 2, 390 + i * 96), l, 84, (255, 255, 255), a=ease((t - 0.2) / 0.4))
        text(img, (W / 2, 1000), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.8) / 0.4))
        return
    r = 1400 + 30 * math.sin(t)
    R.paste_c(img, star_sprite(220, col).resize((int(r * 2.8), int(r * 2.8)), Image.BILINEAR), W / 2, H + r - 520 + 60 * (1 - ease(t / 1.2)))
    R.paste_c(img, R.sun_sprite(5), W / 2 + 330, 760)
    d = ImageDraw.Draw(img); d.line([(W / 2 + 330, 740), (W / 2 + 330, 640)], fill=(255, 220, 160), width=3)
    d.text((W / 2 + 330, 610), "our Sun", font=F(36, "Bold"), fill=(255, 230, 190), anchor="mm")
    a = ease(t / 0.4)
    text(img, (W / 2, 250), "TOP 5", 150, acc, a=a)
    for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
        text(img, (W / 2, 390 + i * 96), l, 84, (255, 255, 255), a=ease((t - 0.2) / 0.4))
    text(img, (W / 2, 1000), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.8) / 0.4))

def seg_item(img, it, th, t, dur):
    col = tuple(it.get("col", th["star_col"])); acc = tuple(th["accent"]); acc2 = tuple(th["accent2"])
    a = ease(t / 0.35)
    # header: rank badge + name
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([60, 170, 260, 370], 36, fill=acc + (int(235 * a),))
    img.alpha_composite(lay)
    text(img, (160, 272), f"#{it['rank']}", 120, (15, 10, 20), a=a)
    nm = it["name"]; size = 84 if F(84, "Black").getlength(nm) < 740 else 64
    text(img, (300, 240), nm, size, (255, 255, 255), a=a, anchor="lm")
    text(img, (302, 320), it.get("tag", ""), 38, acc2, w="Bold", a=ease((t - 0.3) / 0.4), anchor="lm")
    v = it["vis"]
    if v["type"] == "orbits":
        prog = (t - 0.6) / max(1.0, dur * 0.55)
        orbits(img, v["au"], prog, col, acc, t)
        if prog > 0.98 and v.get("note"):
            text(img, (W / 2, 1300), v["note"], 44, (255, 225, 200), w="ExtraBold", a=ease((prog - 0.98) * 4))
    if v["type"] == "speed":
        speed_lanes(img, it, th, t, dur)
    # number
    p = easeio((t - 0.5) / 1.6)
    num = it["num"]
    if isinstance(num, (int, float)):
        val = num * p; s = f"{val:,.0f}" + it.get("suffix", "")
    else: s = num
    text(img, (W / 2, 1395), s, 130, acc, a=ease((t - 0.4) / 0.4))
    text(img, (W / 2, 1472), it["unit"], 40, (235, 235, 245), w="Bold", a=ease((t - 0.6) / 0.4))
    text(img, (W / 2, 1745), "Source: " + it["source"], 28, (150, 160, 190), w="SemiBold", a=ease((t - 0.8) / 0.4))

def seg_outro(img, sc, th, t, dur):
    a = ease(t / 0.5)
    if th.get("outro_note"):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        xe = lerp(-100, W + 100, (t * 0.9) % 1.0)
        d.line([(0, 700), (W, 700)], fill=(255, 240, 160, int(90 * a)), width=3)
        for k in range(14): d.ellipse([xe - 40 * k - 12, 688, xe - 40 * k + 12, 712], fill=(255, 245, 190, int(230 * (1 - k / 14) * a)))
        img.alpha_composite(lay)
        text(img, (W / 2, 790), th["outro_note"], 48, (255, 240, 170), w="ExtraBold", a=a)
    else:
        R.paste_c(img, R.sun_sprite(4), W / 2, 700, a)
        d = ImageDraw.Draw(img); d.ellipse([W / 2 - 40, 660, W / 2 + 40, 740], outline=(255, 220, 160), width=3)
        text(img, (W / 2, 800), "our Sun, on the same scale", 44, (255, 230, 190), w="Bold", a=a)
    R.paste_c(img, R.logo_img(220), W / 2, 1080, ease((t - 0.6) / 0.5))
    text(img, (W / 2, 1260), "SUBSCRIBE", 110, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
    text(img, (W / 2, 1360), "to Cosmic Scale", 56, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))

def chrome(img, th, gt, total):
    d = ImageDraw.Draw(img)
    d.text((W / 2, 92), th.get("bar", "TOP 5"), font=F(34, "ExtraBold"), fill=(220, 225, 240), anchor="mm")
    d.rectangle([0, 0, int(W * gt / total), 10], fill=tuple(th["accent"]))
    d.text((W / 2, 1690), HANDLE, font=F(34, "Bold"), fill=R.CYAN, anchor="mm")

def build(m):
    ALL_ITEMS[:] = m.ITEMS
    segs = [("hook", m.HOOK)] + [("item", it) for it in sorted(m.ITEMS, key=lambda x: -x["rank"])] + [("outro", m.OUTRO)]
    return segs

def tts(segs, outdir, voice):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(R.HERE, "models/kokoro.onnx"), os.path.join(R.HERE, "models/voices.bin"))
    durs, chunks = [], []
    speed = float(os.environ.get("SPEED", "1.05"))
    for i, (_, s) in enumerate(segs):
        cache = os.path.join(outdir, f"seg_{i:02d}.wav"); key = f"{voice}|{speed}|{s['say']}"
        if os.path.exists(cache) and open(cache + ".txt").read() == key: a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(s["say"], voice=voice, speed=speed, lang="en-us"); sf.write(cache, a, sr); open(cache + ".txt", "w").write(key)
        a = np.concatenate([np.zeros(int(sr * 0.1)), a, np.zeros(int(sr * 0.35))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    tt = np.arange(len(audio)) / sr
    pulse = (np.sin(2 * np.pi * 49 * tt) * 0.5 + np.sin(2 * np.pi * 73.5 * tt) * 0.3) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.5 * tt) ** 2) * 0.04
    audio = (audio + pulse).astype(np.float32); audio /= max(1.0, np.abs(audio).max() / 0.95)
    sf.write(os.path.join(outdir, "voice.wav"), audio, sr)
    return durs

def frame(segs, durs, th, gt, chunks):
    total = sum(durs); acc = 0
    for (kind, s), d in zip(segs, durs):
        if gt < acc + d: break
        acc += d
    t = gt - acc
    img = bg(gt, th)
    {"hook": seg_hook, "item": seg_item, "outro": seg_outro}[kind](img, s, th, t, d)
    chrome(img, th, gt, total)
    draw_caption(img, chunks, gt)
    if t < 0.2: img = Image.blend(bg(gt, th), img, ease(t / 0.2))
    return img

def main():
    m = load(sys.argv[1]); outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    th = m.THEME; segs = build(m)
    if "--preview" in sys.argv:
        durs = [10.0] * len(segs); chunks = []
        for i in range(len(segs)):
            for k, tt in enumerate((2.0, 8.5)):
                frame(segs, durs, th, i * 10 + tt, chunks).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}_{k}.jpg"), quality=80)
        print("preview ok"); return
    durs = tts(segs, outdir, os.environ.get("VOICE", "af_heart"))
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
    total = sum(durs); print("total", round(total, 1), "s")
    chunks = []; acc = 0
    for (_, s), d in zip(segs, durs): chunks += caption_chunks(s["say"], acc, d); acc += d
    out = os.path.join(outdir, "ranking.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voice.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        p.stdin.write(frame(segs, durs, th, f / FPS, chunks).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    main()
