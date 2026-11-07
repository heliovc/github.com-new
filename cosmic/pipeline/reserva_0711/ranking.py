"""Cosmic Scale — Shorts de ranking "Top 5" (vertical nativo 1080x1920 30fps).
Uso: python3 -I ranking.py rankXX_algo.py out/rankXX [--preview]
Roteiro: TITLE, THEME {accent, accent2, star_col}, HOOK {say, top, sub}, ITEMS [{rank, name, num, unit, source, say, vis{...}}], OUTRO {say}
Visual por item:
  vis.type == "orbits": desenho do Sistema Solar (órbitas em escala) com a estrela crescendo no lugar do Sol até raio vis.au (UA);
                        vis.note = texto curto sobre o que ela engole.
  vis.type == "bignum": só o número grande animado.
  vis.type == "speed": raias de velocidade em escala log (1 km/s -> luz); vis.kms = km/s; item.short = rótulo curto (rank02).
THEME.hook == "streaks": gancho com rastros de velocidade em vez da estrela gigante (rank02).
  vis.type == "moons": lua atual grande em escala + contorno tracejado de Mercúrio + fila das 5 em escala (não reveladas = silhueta "?"); vis.moon, vis.km (rank03).
vis.type == "thermo" / THEME.hook == "thermo": termômetro vertical 0–6.000 °C com marcas de referência + planeta brilhando na cor da temperatura (rank04).
THEME.hook == "moons": silhueta "?" do nº 1 dentro do contorno de Mercúrio + as 5 luas orbitando (rank03).
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


# ---------- rank03: moons to scale ----------
MOON_LOOK = {  # base colour, spot colour, spot count, spot size range, style
 "Moon": ((150, 150, 155), (95, 95, 105), 26, (0.05, 0.22), "maria"),
 "Io": ((225, 200, 95), (160, 70, 30), 60, (0.02, 0.08), "volcano"),
 "Callisto": ((95, 80, 65), (210, 205, 195), 140, (0.01, 0.05), "craters"),
 "Titan": ((215, 150, 60), (190, 120, 45), 0, (0, 0), "haze"),
 "Ganymede": ((140, 128, 112), (185, 175, 160), 40, (0.04, 0.18), "grooves"),
}
_moon = {}
def moon_sprite(name, r, dim=False):
    r = max(4, int(r)); key = (name, r, dim)
    if key in _moon: return _moon[key]
    base, spot, n, (s0, s1), style = MOON_LOOK[name]
    pad = int(r * 0.25) + 4; size = 2 * r + 2 * pad
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    nx, ny = (xx - size / 2) / r, (yy - size / 2) / r
    rr = nx ** 2 + ny ** 2; inside = rr <= 1; nz = np.sqrt(np.clip(1 - rr, 0, 1))
    shade = np.clip((nx * -0.7 + ny * -0.45 + nz * 0.6) / 1.04, 0, 1) * 0.9 + 0.1
    rgb = np.zeros((size, size, 3), np.float32); rgb[:] = base
    rng = np.random.default_rng(len(name) * 7 + 3)
    lo = Image.fromarray((rng.random((24, 24)) * 255).astype(np.uint8)).resize((size, size), Image.BICUBIC)
    noise = np.asarray(lo, np.float32)[..., None] / 255
    rgb *= 0.82 + 0.3 * noise
    for _ in range(n):
        cx, cy = rng.uniform(-0.9, 0.9, 2); s = rng.uniform(s0, s1)
        dd = np.hypot(nx - cx, ny - cy)
        if style == "craters":
            m = np.clip(1 - dd / s, 0, 1) ** 0.6; rgb = rgb * (1 - m[..., None] * 0.8) + np.array(spot) * m[..., None] * 0.8
        elif style == "volcano":
            m = np.clip(1 - dd / s, 0, 1); col = spot if rng.random() < 0.6 else (40, 30, 25)
            rgb = rgb * (1 - m[..., None]) + np.array(col) * m[..., None]
        elif style == "grooves":
            m = np.clip(1 - dd / s, 0, 1) ** 1.5; rgb = rgb * (1 - m[..., None] * 0.55) + np.array(spot) * m[..., None] * 0.55
        else:
            m = np.clip(1 - dd / s, 0, 1) ** 1.2; rgb = rgb * (1 - m[..., None] * 0.6) + np.array(spot) * m[..., None] * 0.6
    if style == "haze":
        band = (np.sin(ny * 9 + noise[..., 0] * 2) * 0.5 + 0.5)[..., None]
        rgb = rgb * (0.9 + 0.12 * band)
    rgb = rgb * shade[..., None]
    a = np.where(inside, 255, 0).astype(np.float32)
    if style == "haze":  # thick atmosphere halo
        dd = np.sqrt(rr); gl = np.clip((1.12 - dd) / 0.12, 0, 1) * (dd > 1)
        rgb = np.where((dd > 1)[..., None], np.array((235, 170, 80), np.float32), rgb); a = np.maximum(a, gl * 150)
    if dim: rgb = rgb * 0.0 + 18; a = np.where(inside, 255, 0).astype(np.float32)
    img = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8), "RGBA")
    _moon[key] = img; return img

MERCURY_KM = 4879
def dashed_circle(d, cx, cy, r, col, w=3, step=6):
    for k in range(0, 360, step): d.arc([cx - r, cy - r, cx + r, cy + r], k, k + step * 0.55, fill=col, width=w)

def moons_vis(img, it, th, t, dur):
    acc = tuple(th["accent"]); acc2 = tuple(th["accent2"])
    km = it["vis"]["km"]; KM1 = max(o["vis"]["km"] for o in ALL_ITEMS)
    # big moon (radius proportional to its true size) + Mercury dashed outline as reference
    cx, cy = W / 2, 700; R1 = 255
    rr = R1 * km / KM1 * (0.85 + 0.15 * ease((t - 0.2) / 1.2))
    R.paste_c(img, moon_sprite(it["vis"]["moon"], rr), cx, cy, ease(t / 0.4))
    d = ImageDraw.Draw(img)
    rm = R1 * MERCURY_KM / KM1; q = ease((t - 1.0) / 0.6)
    if q > 0:
        dashed_circle(d, cx, cy, rm, mix((5, 7, 15), (255, 255, 255), q * 0.85), 3)
        d.text((cx + rm * 0.72 + 14, cy - rm * 0.72 - 14), "Mercury", font=F(30, "Bold"), fill=mix((5, 7, 15), (230, 230, 240), q), anchor="lb")
    # lineup to scale (unrevealed = silhouettes with "?")
    order = sorted(ALL_ITEMS, key=lambda o: o["vis"]["km"]); tot = sum(o["vis"]["km"] for o in order); gap = 34
    s = (W - 140 - gap * (len(order) - 1)) / tot; x = 70
    for o in order:
        r = o["vis"]["km"] * s / 2; xc = x + r; yc = 1190 - r; x += 2 * r + gap
        revealed = o["rank"] >= it["rank"]; cur = o["rank"] == it["rank"]
        R.paste_c(img, moon_sprite(o["vis"]["moon"], r, dim=not revealed), xc, yc)
        d = ImageDraw.Draw(img)
        if not revealed:
            d.ellipse([xc - r, yc - r, xc + r, yc + r], outline=(90, 100, 120), width=2)
            d.text((xc, yc), "?", font=F(int(r * 0.9), "Black"), fill=(110, 120, 140), anchor="mm")
        if cur: d.ellipse([xc - r - 8, yc - r - 8, xc + r + 8, yc + r + 8], outline=acc, width=5)
        d.text((xc, 1222), o.get("short", o["name"]) if revealed else f"#{o['rank']}", font=F(26, "ExtraBold" if cur else "Bold"),
               fill=acc if cur else ((200, 205, 220) if revealed else (110, 120, 140)), anchor="mm")
    d.line([(70, 1192), (W - 70, 1192)], fill=(70, 80, 100), width=2)

# ---- 07/11: vis "thermo" (vertical thermometer 0–6,000 °C with reference marks + glowing planet) ----
TH_MAX = 6000
TH_REF = [(327, "lead melts"), (1200, "lava"), (1538, "iron melts"), (5500, "Sun's surface")]
def temp_col(c):
    stops = [(0, (120, 60, 40)), (500, (230, 90, 40)), (2000, (255, 150, 50)), (3500, (255, 220, 140)), (5000, (230, 240, 255))]
    for (a, ca), (b, cb) in zip(stops, stops[1:]):
        if c <= b: return mix(ca, cb, (c - a) / (b - a))
    return stops[-1][1]

def thermo(img, temp, th, t, revealed=(), show_q=False):
    acc = tuple(th["accent"]); x, y0, y1 = 190, 1240, 480
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x - 34, y1 - 30, x + 34, y0 + 20], 34, fill=(25, 22, 30), outline=(200, 200, 215), width=4)
    d.ellipse([x - 62, y0 - 20, x + 62, y0 + 104], fill=(25, 22, 30), outline=(200, 200, 215), width=4)
    yt = lerp(y0, y1, min(1, temp / TH_MAX))
    for k in range(int(y0) + 40, int(yt), -6):
        c = temp_col(lerp(0, TH_MAX, (y0 - k) / (y0 - y1))); d.rectangle([x - 20, k - 6, x + 20, k], fill=c)
    d.ellipse([x - 46, y0 - 4, x + 46, y0 + 88], fill=temp_col(temp))
    for c, lab in TH_REF:
        yy = lerp(y0, y1, c / TH_MAX); d.line([(x + 40, yy), (x + 70, yy)], fill=(160, 165, 185), width=3)
        d.text((x + 80, yy), f"{lab} · {c:,} °C", font=F(26, "SemiBold"), fill=(170, 175, 195), anchor="lm")
    for name, c in revealed:
        yy = lerp(y0, y1, c / TH_MAX); d.line([(x - 70, yy), (x - 40, yy)], fill=acc, width=4)
    return yt

def planet_glow(img, cx, cy, r, temp, t):
    col = temp_col(temp)
    R.paste_c(img, R.radial(int(r * 3.2), [(0, col + (110,)), (0.5, col + (40,)), (1, col + (0,))]), cx, cy)
    spr = R.planet_sprite(int(r), col, light=(-0.9, -0.5))
    R.paste_c(img, spr, cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rng = random.Random(int(temp))
    for i in range(10):  # heat bands
        yy = cy - r + (i + 0.5) * 2 * r / 10 + 4 * math.sin(t * 2 + i)
        hw = math.sqrt(max(0, r * r - (yy - cy) ** 2))
        d.line([(cx - hw, yy), (cx + hw, yy)], fill=mix(col, (255, 255, 255), 0.4) + (40,), width=3)
    img.alpha_composite(lay)

def thermo_vis(img, it, th, t, dur):
    temp = it["vis"]["c"] * easeio((t - 0.4) / 1.6)
    rev = [(o["short"], o["vis"]["c"]) for o in ALL_ITEMS if o["rank"] > it["rank"]]
    yt = thermo(img, temp, th, t, rev)
    d = ImageDraw.Draw(img)
    d.line([(234, yt), (420, yt)], fill=tuple(th["accent"]), width=3)
    planet_glow(img, 760, 820, it["vis"].get("r", 190), it["vis"]["c"], t)
    if it["vis"].get("note"):
        for i, l in enumerate(wrap(it["vis"]["note"], F(36, "ExtraBold"), 440)):
            text(img, (800, 1085 + i * 46), l, 36, (255, 225, 200), w="ExtraBold", a=ease((t - 1.5) / 0.5))

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
    if th.get("hook") == "thermo":
        thermo(img, TH_MAX * 0.72 * (0.97 + 0.03 * math.sin(t * 4)), th, t)
        planet_glow(img, 700, 860, 200, 4300, t)
        d = ImageDraw.Draw(img); d.text((700, 860), "?", font=F(220, "Black"), fill=(40, 20, 10), anchor="mm")
        text(img, (W / 2, 210), "TOP 5", 150, acc)
        for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
            text(img, (W / 2, 340 + i * 96), l, 84, (255, 255, 255))
        text(img, (W / 2, 1440), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "moons":
        order = sorted(ALL_ITEMS, key=lambda o: o["vis"]["km"]); KM1 = order[-1]["vis"]["km"]
        cx, cy = W / 2, 930; R1 = 280
        rm = R1 * MERCURY_KM / KM1
        # Ganymede silhouette "?" pulsing against Mercury outline + slow orbiting lineup
        for i, o in enumerate(order):
            ang = t * 0.6 + i * 2 * math.pi / len(order); r = 70 * o["vis"]["km"] / KM1
            R.paste_c(img, moon_sprite(o["vis"]["moon"], r), cx + 400 * math.cos(ang), cy + 120 * math.sin(ang))
        R.paste_c(img, moon_sprite(order[-1]["vis"]["moon"], R1 * (0.96 + 0.04 * math.sin(t * 3)), dim=True), cx, cy)
        d = ImageDraw.Draw(img); d.ellipse([cx - R1, cy - R1, cx + R1, cy + R1], outline=acc, width=5)
        dashed_circle(d, cx, cy, rm, (235, 235, 245), 4)
        d.text((cx, cy + rm - 40), "Mercury", font=F(32, "Bold"), fill=(230, 230, 240), anchor="mm")
        d.text((cx, cy - R1 - 30), "#1 vs the planet Mercury", font=F(36, "Bold"), fill=acc, anchor="mm")
        d.text((cx, cy), "?", font=F(220, "Black"), fill=acc, anchor="mm")
        text(img, (W / 2, 210), "TOP 5", 150, acc)
        for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
            text(img, (W / 2, 340 + i * 96), l, 84, (255, 255, 255))
        text(img, (W / 2, 1320), sc["sub"], 54, tuple(th["accent2"]), w="ExtraBold")
        return
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
    if v["type"] == "moons":
        moons_vis(img, it, th, t, dur)
    if v["type"] == "thermo":
        thermo_vis(img, it, th, t, dur)
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
    if th.get("outro") == "moons":
        order = sorted(ALL_ITEMS, key=lambda o: o["vis"]["km"]); tot = sum(o["vis"]["km"] for o in order)
        s = (W - 140) / tot; x = 70; ex = 12742 * s
        R.paste_c(img, R.earth_sprite(int(ex / 2), glow=None), W / 2, 470, a)
        text(img, (W / 2, 470 - ex / 2 - 36), "Earth", 40, (200, 225, 255), w="Bold", a=a)
        p = ease((t - 0.5) / 1.2)
        for o in order:
            r = o["vis"]["km"] * s / 2
            R.paste_c(img, moon_sprite(o["vis"]["moon"], r), lerp(W / 2, x + r, p), 880, ease((t - 0.3) / 0.5)); x += 2 * r
        if th.get("outro_note"): text(img, (W / 2, 1040), th["outro_note"], 46, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.4) / 0.5))
    elif th.get("outro_note"):
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
    if th.get("outro") != "moons": R.paste_c(img, R.logo_img(220), W / 2, 1080, ease((t - 0.6) / 0.5))
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
    if t < 0.2 and gt > 0.5: img = Image.blend(bg(gt, th), img, ease(t / 0.2))
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
