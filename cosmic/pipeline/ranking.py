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
vis.type == "horizons" / THEME.hook/outro == "horizons": horizontes de eventos em escala fixa contra o Sistema Solar e a Voyager 1 (rank05).
vis.type == "thermo" / THEME.hook == "thermo": termômetro vertical 0–6.000 °C com marcas de referência + planeta brilhando na cor da temperatura (rank04).
THEME.hook == "moons": silhueta "?" do nº 1 dentro do contorno de Mercúrio + as 5 luas orbitando (rank03).
vis.type == "lightyears" / THEME.hook/outro == "lightyears": régua vertical em anos-luz (Sol embaixo, 0–9 a.l.), pulso de luz descendo, estrela grande
  + "a luz que você vê hoje saiu em AAAA" (rank07). HOOK.big = número grande no 1º frame.
vis.type == "glow" / THEME.hook/outro == "glow": horizonte noturno com a estrela no brilho aparente (magnitude) + régua log "quão potente é de verdade" (× Sol);
  vis.lum, vis.ly, vis.col (rank08).
vis.type == "daylight" / THEME.hook/outro == "daylight": planeta com dia/noite e Sol girando em volta (1 volta = 1 dia solar) + contador de dias terrestres + régua linear 0–180 dias com os mundos revelados (rank06).
vis.type == "kelvin" / THEME.hook/outro == "kelvin": régua Kelvin 0–60 K com parede de gelo no zero absoluto e a linha de 2,7 K do espaço vazio;
  o lugar desliza até a sua temperatura e o objeto congela (vis.kind = planet | crater | nebula; vis.k, vis.col) (rank09).
vis.type == "peaks" / THEME.hook/outro == "peaks": régua vertical 0–26 km com Everest e a linha dos aviões (11 km); o perfil da montanha sobe
  da base (vis.kind = shield | central | ridge | block | ocean; vis.km, vis.sea = nível do mar em km, vis.world, vis.world_col) (rank10).
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

# ---- rank05: event horizons to one fixed scale vs the Solar System ----
HZ_CX, HZ_CY, HZ_PX = W / 2, 850, 375 / 1974.0
_bhring = {}
def bh_disk(img, cx, cy, r, t, a=1.0, col=(255, 170, 90), acc=(185, 140, 255)):
    r = max(3, r); k = int(r)
    if k not in _bhring:
        size = int(r * 2.9) + 8
        _bhring[k] = R.radial(size, [(0, (0, 0, 0, 255)), (0.98 / 1.45, (0, 0, 0, 255)), (1.0 / 1.45, (255, 235, 200, 255)),
                                      (1.06 / 1.45, col + (230,)), (1.25 / 1.45, acc + (90,)), (1.0, acc + (0,))])
    R.paste_c(img, _bhring[k], cx, cy, a)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i in range(3):  # shimmering photon-ring arcs
        st = (t * 60 + i * 120) % 360
        d.arc([cx - r * 1.03, cy - r * 1.03, cx + r * 1.03, cy + r * 1.03], st, st + 50, fill=(255, 250, 235, int(200 * a)), width=max(2, int(r * 0.03)))
    img.alpha_composite(lay)

def solar_ref(img, t, a=1.0, labels=True, cy=None):
    d = ImageDraw.Draw(img); cx, cy = HZ_CX, (cy or HZ_CY)
    rv = 171 * HZ_PX; rn = 30 * HZ_PX
    for k in range(0, 360, 10): d.arc([cx - rv, cy - rv, cx + rv, cy + rv], k, k + 5, fill=(120, 230, 255, int(255 * a)), width=3)
    d.ellipse([cx - rn, cy - rn, cx + rn, cy + rn], fill=(255, 200, 90))
    if labels:
        d.line([(cx + rv * 0.7, cy - rv * 0.7), (cx + 230, cy - 210)], fill=(120, 230, 255), width=2)
        d.text((cx + 240, cy - 230), "Voyager 1 · 49 years of flight", font=F(30, "Bold"), fill=(120, 230, 255), anchor="lm")
        d.line([(cx, cy + rn), (cx - 200, cy + 230)], fill=(255, 200, 90), width=2)
        d.text((cx - 200, cy + 255), "our whole solar system", font=F(30, "Bold"), fill=(255, 210, 120), anchor="mm")

def horizons_vis(img, it, th, t, dur):
    acc = tuple(th["accent"]); d = ImageDraw.Draw(img)
    prev = sorted([o for o in ALL_ITEMS if o["rank"] > it["rank"]], key=lambda o: o["vis"]["au"])
    r = it["vis"]["au"] * HZ_PX * easeio((t - 0.4) / 1.6)
    if r > 3: bh_disk(img, HZ_CX, HZ_CY, r, t, col=tuple(th["star_col"]), acc=acc)
    d = ImageDraw.Draw(img)
    for o in prev:
        r = o["vis"]["au"] * HZ_PX
        for k in range(0, 360, 6): d.arc([HZ_CX - r, HZ_CY - r, HZ_CX + r, HZ_CY + r], k, k + 3, fill=(170, 150, 220), width=3)
        d.text((HZ_CX, HZ_CY - r + 22), o["short"], font=F(24, "Bold"), fill=(200, 185, 245), anchor="mm")
    solar_ref(img, t, labels=(it["rank"] >= 4 or t < 3))
    if it["vis"].get("note"):
        for i, l in enumerate(wrap(it["vis"]["note"], F(40, "ExtraBold"), W - 160)):
            text(img, (W / 2, 1300 + i * 50 - 40), l, 40, (235, 225, 255), w="ExtraBold", a=ease((t - 1.8) / 0.5))


# ---------------- rank06: "daylight" (length of a solar day) ----------------
_tex = {}
def world_tex(name, r, col):
    key = (name, int(r))
    if key not in _tex:
        r = int(r); size = 2 * r + 4
        yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
        nx, ny = (xx - size / 2) / r, (yy - size / 2) / r; rr = nx ** 2 + ny ** 2
        rng = np.random.default_rng(sum(map(ord, name)))
        def noise(n, blur):
            im = Image.fromarray((rng.random((n, n)) * 255).astype(np.uint8)).resize((size, size), Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))
            return np.asarray(im, np.float32) / 255 - 0.5
        base = np.zeros((size, size, 3), np.float32); base[:] = col
        if name == "Venus":   # cloud bands
            band = np.sin(ny * 9 + noise(8, 3) * 5) * 0.12
            base *= (1 + band)[..., None]
        elif name == "Iapetus":  # two-tone: dark leading half
            dark = (nx + noise(10, 4) * 0.6) < -0.1
            base[dark] = (52, 40, 30)
        else:  # cratered rock / ice
            n2 = noise(24, 1.5) * 0.35 + noise(8, 4) * 0.25
            base *= (1 + n2)[..., None]
            for _ in range(int(r / 6)):
                cx, cy, cr = rng.uniform(-0.8, 0.8), rng.uniform(-0.8, 0.8), rng.uniform(0.03, 0.12)
                m = ((nx - cx) ** 2 + (ny - cy) ** 2) < cr ** 2; base[m] *= 0.82
        nz = np.sqrt(np.clip(1 - rr, 0, 1))
        _tex[key] = (np.clip(base, 0, 255), nx, ny, nz, rr <= 1)
    return _tex[key]

def day_planet(img, name, cx, cy, r, col, ang, a=1.0):
    """planet lit by a Sun at angle ang (radians, screen plane, slightly from the viewer) -> day/night terminator"""
    base, nx, ny, nz, inside = world_tex(name, r, col)
    lx, ly, lz = math.cos(ang), math.sin(ang), 0.25; ln = math.sqrt(lx * lx + ly * ly + lz * lz)
    sh = np.clip((nx * lx + ny * ly + nz * lz) / ln, 0, 1)
    sh = np.clip(sh * 1.6, 0, 1) ** 0.7 * 0.94 + 0.06
    rgb = base * sh[..., None]
    al = np.where(inside, 255 * a, 0)
    spr = Image.fromarray(np.dstack([rgb, al]).astype(np.uint8), "RGBA")
    img.alpha_composite(spr, (int(cx - spr.width / 2), int(cy - spr.height / 2)))

DL_CX, DL_CY, DL_R = W / 2, 760, 230
DL_X0, DL_X1, DL_Y, DL_MAX = 110, W - 110, 1215, 180.0

def day_ruler(img, th, cur=None, prog=1.0, a=1.0):
    d = ImageDraw.Draw(img); acc = tuple(th["accent"])
    d.line([(DL_X0, DL_Y), (DL_X1, DL_Y)], fill=(110, 118, 130), width=4)
    for k in range(0, 181, 30):
        x = lerp(DL_X0, DL_X1, k / DL_MAX); d.line([(x, DL_Y - 10), (x, DL_Y + 10)], fill=(140, 148, 160), width=3)
        d.text((x, DL_Y + 34), f"{k}", font=F(26, "Bold"), fill=(150, 158, 170), anchor="mm")
    d.text((DL_X1, DL_Y - 34), "Earth days", font=F(26, "Bold"), fill=(150, 158, 170), anchor="rm")
    for j, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["vis"]["days"])):
        if cur is not None and o["rank"] < cur["rank"]: continue
        v = o["vis"]; days = v["days"] * (prog if o is cur else 1)
        x = lerp(DL_X0, DL_X1, days / DL_MAX); c = tuple(v["col"]) if o is cur else (150, 158, 170)
        d.rounded_rectangle([DL_X0, DL_Y - 7, x, DL_Y + 7], 7, fill=c if o is cur else None)
        d.ellipse([x - 13, DL_Y - 13, x + 13, DL_Y + 13], fill=c, outline=(20, 22, 26), width=3)
        if o is not cur: d.text((x, DL_Y - 34 - 28 * (j % 2)), o["short"], font=F(22, "Bold"), fill=(170, 176, 188), anchor="mm")

def sun_around(img, ang, rad, a=1.0):
    sx, sy = DL_CX + rad * math.cos(ang), DL_CY + rad * math.sin(ang)
    R.paste_c(img, R.sun_sprite(16), sx, sy, a)
    return sx, sy

def daylight_vis(img, it, th, t, dur):
    v = it["vis"]; acc = tuple(th["accent"])
    p = easeio((t - 0.5) / max(1.5, dur * 0.7))          # one full Sun loop = one solar day, over the segment
    ang = -math.pi / 2 + p * 2 * math.pi
    d = ImageDraw.Draw(img); orb = DL_R + 95
    for k in range(0, 360, 8): d.arc([DL_CX - orb, DL_CY - orb, DL_CX + orb, DL_CY + orb], k, k + 4, fill=(90, 96, 110), width=2)
    d.arc([DL_CX - orb, DL_CY - orb, DL_CX + orb, DL_CY + orb], -90, -90 + 360 * p, fill=acc, width=6)
    sun_around(img, ang, orb)
    day_planet(img, it["short"], DL_CX, DL_CY, DL_R, tuple(v["col"]), ang)
    d = ImageDraw.Draw(img)
    d.text((DL_CX, DL_CY - orb - 46), "sunrise → sunrise", font=F(30, "Bold"), fill=(205, 210, 220), anchor="mm")
    day_ruler(img, th, it, prog=p)
    if v.get("note"):
        text(img, (W / 2, 1300), v["note"], 40, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.6) / 0.5))


# ---- rank07: "lightyears" — vertical light-year ruler from the Sun (bottom) up to 9 ly; light pulse climbing; year the light left
LY_X, LY_Y0, LY_Y1, LY_MAX = 250, 1190, 480, 9.0
def ly_y(d): return lerp(LY_Y0, LY_Y1, d / LY_MAX)
def ly_ruler(img, th, shown, cur=None, t=0.0, pulse=None, labels=True):
    acc = tuple(th["accent"]); d = ImageDraw.Draw(img)
    d.line([(LY_X, LY_Y0), (LY_X, LY_Y1 - 20)], fill=(110, 120, 150), width=4)
    for k in range(0, 10):
        y = ly_y(k); d.line([(LY_X - 18, y), (LY_X, y)], fill=(110, 120, 150), width=3)
        d.text((LY_X - 30, y), f"{k}", font=F(30, "Bold"), fill=(150, 160, 190), anchor="rm")
    d.text((LY_X - 30, LY_Y1 - 60), "light-years", font=F(28, "Bold"), fill=(150, 160, 190), anchor="lm")
    R.paste_c(img, R.sun_sprite(14), LY_X, LY_Y0)
    d = ImageDraw.Draw(img)
    if labels: d.text((LY_X + 40, LY_Y0 + 4), "the Sun (you are here)", font=F(30, "Bold"), fill=(255, 220, 160), anchor="lm")
    if pulse is not None:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); y = ly_y(pulse)
        for k in range(16): dl.ellipse([LY_X - 9, y + k * 9 - 9, LY_X + 9, y + k * 9 + 9], fill=acc + (int(220 * (1 - k / 16)),))
        img.alpha_composite(lay)
    for o in shown:
        y = ly_y(o["vis"]["ly"]); c = tuple(o["vis"]["col"]); big = cur is not None and o is cur
        d = ImageDraw.Draw(img); d.line([(LY_X, y), (LY_X + 60, y)], fill=c, width=3)
        R.paste_c(img, star_sprite(13 if big else 8, c), LY_X + 80, y)
        d = ImageDraw.Draw(img); ly = o["vis"]["ly"]; yo = 16 if 4.2 < ly < 4.3 else (-14 if 4.3 <= ly < 4.4 else 0)
        if labels: d.text((LY_X + 110, y + yo), f'{o["short"]}  {o["vis"]["ly"]:g}', font=F(34 if big else 28, "ExtraBold" if big else "Bold"), fill=acc if big else (200, 205, 220), anchor="lm")

def lightyears_vis(img, it, th, t, dur):
    v = it["vis"]; order = sorted(ALL_ITEMS, key=lambda o: -o["rank"])
    shown = order[:order.index(it) + 1]
    p = easeio((t - 0.4) / max(1.2, dur * 0.6))
    ly_ruler(img, th, shown, cur=it, t=t, pulse=v["ly"] * (1 - p))
    cx, cy = 850, 760; rr = v.get("r", 120) * (0.97 + 0.03 * math.sin(t * 3))
    R.paste_c(img, star_sprite(int(rr), tuple(v["col"])), cx, cy)
    if v.get("pair"):
        cx -= 50; R.paste_c(img, star_sprite(int(rr * 0.75), tuple(v["pair"])), cx + rr * 0.95, cy + rr * 0.75)
    yr = 2026.86 - v["ly"]
    text(img, (cx, cy + 260), "the light you see tonight", 34, (205, 210, 225), w="Bold", a=ease((t - 1.0) / 0.4))
    text(img, (cx, cy + 320), f"left it in {int(yr)}", 58, tuple(th["accent"]), a=ease((t - 1.2) / 0.4))
    if v.get("note"): text(img, (W / 2, 1300), v["note"], 38, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.8) / 0.5))

# ---- rank08: "glow" — night horizon with the star shining at its apparent brightness + two meters: LOOKS (magnitude) vs REALLY IS (× Sun, log)
GL_LMAX = 5.0  # log10 of 100,000 × Sun
def horizon(img, t, col=(14, 12, 30)):
    d = ImageDraw.Draw(img)
    pts = [(0, H)] + [(x, 1120 - 40 * math.sin(x / 170 + 1.2) - 18 * math.sin(x / 61)) for x in range(0, W + 30, 30)] + [(W, H)]
    d.polygon(pts, fill=col)
    for tx in (140, 175, 930):
        d.polygon([(tx, 1110), (tx - 22, 1110), (tx - 11, 1020)], fill=col)
def lum_meter(img, th, items, cur=None, prog=1.0, y=1220, a=1.0):
    d = ImageDraw.Draw(img); x0, x1 = 90, W - 90
    d.rounded_rectangle([x0, y - 14, x1, y + 14], 14, fill=(40, 44, 70))
    for k in range(0, 6):
        x = lerp(x0, x1, k / GL_LMAX); d.line([(x, y + 18), (x, y + 34)], fill=(150, 160, 190), width=3)
        d.text((x, y + 56), ["1", "10", "100", "1,000", "10,000", "100,000"][k] + ("× Sun" if k == 0 else ""), font=F(26, "Bold"), fill=(150, 160, 190), anchor="mm")
    for o in items:
        L = o["vis"]["lum"] if o is not cur else 10 ** (math.log10(o["vis"]["lum"]) * prog)
        x = lerp(x0, x1, max(0, math.log10(L)) / GL_LMAX); c = tuple(o["vis"]["col"]); big = o is cur
        d.ellipse([x - (20 if big else 12), y - (20 if big else 12), x + (20 if big else 12), y + (20 if big else 12)], fill=c, outline=(255, 255, 255) if big else None, width=3)
        if not big: d.text((x, y - 36), o["short"], font=F(24, "Bold"), fill=(200, 205, 220), anchor="mm")
    d.text((x0, y - 60), "HOW POWERFUL IT REALLY IS", font=F(30, "ExtraBold"), fill=tuple(th["accent2"]), anchor="lm")
def glow_vis(img, it, th, t, dur):
    v = it["vis"]; order = sorted(ALL_ITEMS, key=lambda o: -o["rank"]); shown = order[:order.index(it) + 1]
    horizon(img, t)
    flux = 10 ** (-0.4 * (it["num"] - 0.03))   # relative to Vega
    rr = 30 + 46 * flux ** 0.5; tw = 1 + 0.05 * math.sin(t * 7) + 0.03 * math.sin(t * 11.3)
    halo = R.radial(int(rr * 8), [(0, tuple(v["col"]) + (120,)), (0.3, tuple(v["col"]) + (40,)), (1, tuple(v["col"]) + (0,))])
    R.paste_c(img, halo, W / 2, 720); R.paste_c(img, star_sprite(int(rr * tw), tuple(v["col"])), W / 2, 720)
    d = ImageDraw.Draw(img)
    for k in range(4):
        ang = math.pi / 4 * k * 2 + math.pi / 4; L = rr * 3.2 * tw
        d.line([(W / 2 - L * math.cos(ang), 720 - L * math.sin(ang)), (W / 2 + L * math.cos(ang), 720 + L * math.sin(ang))], fill=tuple(v["col"]), width=2)
    text(img, (W / 2, 470), f'{v["ly"]:g} light-years away', 42, (220, 225, 240), w="ExtraBold", a=ease((t - 0.6) / 0.4))
    p = easeio((t - 1.0) / max(1.2, dur * 0.5))
    lum_meter(img, th, shown, cur=it, prog=p)
    text(img, (W / 2, 1060), f'{v["lum"] * 1:,.0f}× the Sun' if p > 0.98 else "", 60, tuple(th["accent"]), a=ease((t - 1.0 - dur * 0.5) / 0.3))

# ---- rank09: "kelvin" — Kelvin ruler 0–60 K with an ice wall at absolute zero and the 2.7 K line of empty space (CMB);
# the current place slides down to its temperature; the object (planet / shadowed crater / bow-tie nebula) frosts over as it gets colder.
KV_X0, KV_X1, KV_MAX = 120, 980, 60.0
def kv_x(k): return lerp(KV_X0, KV_X1, k / KV_MAX)
_kfrost = {}
def kv_frost(q):
    q = round(max(0, min(1, q)), 1)
    if q not in _kfrost:
        if "b" not in _kfrost:
            yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
            e = np.clip(1 - np.minimum(np.minimum(xx, W - xx) / 300, np.minimum(yy, H - yy) / 420), 0, 1) ** 2
            rng = np.random.default_rng(9); n = Image.fromarray((rng.random((H // 10, W // 10)) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
            _kfrost["b"] = e * (0.55 + 0.45 * np.asarray(n, np.float32) / 255)
        im = Image.new("RGBA", (W, H), (215, 240, 255, 0)); im.putalpha(Image.fromarray((_kfrost["b"] * 150 * q).astype(np.uint8)))
        _kfrost[q] = im
    return _kfrost[q]
def kv_ruler(img, th, shown, cur=None, curk=None, y=1150, labels=True, cmb=True, q=None):
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); d = ImageDraw.Draw(img)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for i in range(10): dl.rectangle([KV_X0 - 46 + i * 3, y - 120, KV_X0 - 16, y + 60], fill=(200, 235, 255, 40 + i * 18))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.text((KV_X0 - 30, y - 150), "ABSOLUTE ZERO", font=F(26, "Black"), fill=(220, 240, 255), anchor="lm")
    d.rounded_rectangle([KV_X0, y - 10, KV_X1, y + 10], 10, fill=(45, 55, 85))
    for k in range(0, 61, 10):
        x = kv_x(k); d.line([(x, y + 14), (x, y + 32)], fill=(150, 165, 200), width=3)
        d.text((x, y + 54), f"{k} K" if k in (0, 60) else f"{k}", font=F(26, "Bold"), fill=(150, 165, 200), anchor="mm")
    if cmb:
        x = kv_x(2.725)
        for yy in range(int(y - 110), int(y + 10), 14): d.line([(x, yy), (x, yy + 7)], fill=acc2, width=3)
        d.text((x + 10, y - 124), "empty space: 2.7 K", font=F(26, "ExtraBold"), fill=acc2, anchor="lm")
    for j, o in enumerate(shown):
        k = curk if (o is cur and curk is not None) else o["vis"]["k"]; x = kv_x(k); c = tuple(o["vis"]["col"]); big = o is cur
        r = 18 if big else 11
        d.ellipse([x - r, y - r, x + r, y + r], fill=c, outline=(255, 255, 255) if big else None, width=3)
        if labels:
            yo = {5: -44, 4: 92, 3: -84, 2: 92, 1: -44}.get(o["rank"], -44)
            d.text((x, y + yo), o["short"], font=F(26 if not big else 30, "ExtraBold"), fill=c if not big else acc, anchor="mm")
    if q is not None:
        x = kv_x(1.0); d.ellipse([x - 18, y - 18, x + 18, y + 18], fill=acc); d.text((x, y - 50), "?", font=F(54, "Black"), fill=acc, anchor="mm")
def kv_object(img, v, cx, cy, r, t, q):
    kind = v.get("kind", "planet"); c = tuple(v["col"])
    if kind == "planet":
        R.paste_c(img, R.planet_sprite(int(r), c, light=(-0.8, -0.4), glow=tuple(min(255, x + 40) for x in c)), cx, cy)
        if v.get("ring"):
            d = ImageDraw.Draw(img); d.ellipse([cx - r * 0.25, cy - r * 1.25, cx + r * 0.25, cy + r * 1.25], outline=c + (160,), width=3)
    elif kind == "crater":
        R.paste_c(img, R.planet_sprite(int(r), (175, 175, 180), light=(-0.2, -1.0)), cx, cy)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for (dx, dy, rr) in [(-0.35, -0.55, 0.28), (0.25, -0.62, 0.2), (0.0, -0.3, 0.16)]:
            dl.ellipse([cx + dx * r - rr * r, cy + dy * r - rr * r * 0.7, cx + dx * r + rr * r, cy + dy * r + rr * r * 0.7], fill=(10, 12, 22, 235))
        img.alpha_composite(lay)
        d = ImageDraw.Draw(img); d.line([(cx - 0.35 * r, cy - 0.55 * r), (cx + 120, cy - r - 40)], fill=(220, 240, 255), width=3)
        d.text((cx + 130, cy - r - 40), "never sees the Sun", font=F(30, "ExtraBold"), fill=(220, 240, 255), anchor="lm")
    else:  # bow-tie nebula
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for i in range(26):
            f = 1 - i / 26; w_ = r * 1.25 * f; h_ = r * 0.55 * f; sp = math.sin(t * 0.8 + i) * 4
            col = R.mix((60, 110, 220), (190, 230, 255), 1 - f) + (int(26 + 30 * (1 - f)),)
            for sgn in (-1, 1): dl.ellipse([cx + sgn * w_ * 0.85 - w_ * 0.75, cy - h_ + sp, cx + sgn * w_ * 0.85 + w_ * 0.75, cy + h_ + sp], fill=col)
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(6)))
        R.paste_c(img, star_sprite(16, (255, 245, 230)), cx, cy)
    if q > 0.05:
        d = ImageDraw.Draw(img); rng = random.Random(int(r))
        for i in range(int(40 * q)):  # ice sparkles
            a = rng.uniform(0, 2 * math.pi); rr = r * rng.uniform(0.3, 1.25); x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
            s = 3 + 3 * math.sin(t * 5 + i); d.line([(x - s, y), (x + s, y)], fill=(230, 245, 255), width=2); d.line([(x, y - s), (x, y + s)], fill=(230, 245, 255), width=2)
def kelvin_vis(img, it, th, t, dur):
    v = it["vis"]; order = sorted(ALL_ITEMS, key=lambda o: -o["rank"]); shown = order[:order.index(it) + 1]
    p = easeio((t - 0.4) / max(1.2, dur * 0.55)); k = lerp(KV_MAX, v["k"], p); q = 1 - k / KV_MAX
    img.alpha_composite(kv_frost(0.25 + 0.75 * q))
    kv_object(img, v, W / 2, 700, v.get("r", 220), t, q)
    kv_ruler(img, th, shown, cur=it, curk=k, cmb=it["rank"] <= 2)
    text(img, (W / 2, 950), f"{k:,.0f} K above absolute zero" if v["k"] >= 2 else f"{k:,.1f} K above absolute zero", 40, (220, 235, 255), w="ExtraBold", a=ease((t - 0.6) / 0.4))
    if v.get("note"): text(img, (W / 2, 1290), v["note"], 38, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.8) / 0.5))

# ---- rank10: "peaks" — heights TO SCALE on a vertical km ruler (0–26 km), Everest + airliner cruising line as references;
# the mountain's profile rises from its base (shield | central | ridge | block | ocean); its world as a small sphere in the corner.
PK_Y0, PK_Y1, PK_MAX, PK_X = 1290, 470, 26.0, 120
def pk_y(km): return lerp(PK_Y0, PK_Y1, km / PK_MAX)
def pk_profile(kind, u):
    """u in [-1, 1] -> height fraction 0..1"""
    a = abs(u)
    if kind == "shield":  # broad gentle dome with escarpment cliffs at the base
        return max(0.0, 0.78 * (1 - a ** 1.6) + (0.22 if a < 0.92 else 0.22 * max(0, (1 - a) / 0.08)))
    if kind == "central":  # crater floor, rim walls at the edges, central peak
        rim = 0.32 * math.exp(-((a - 0.95) / 0.06) ** 2)
        return max(0.0, math.exp(-(u / 0.22) ** 2) * 1.0 + rim)
    if kind == "ridge":  # sharp equatorial ridge
        return max(0.0, 1 - a / 0.42) ** 1.2
    if kind == "block":  # tilted tectonic block: steep on one side
        return max(0.0, min(1.0, (u + 0.8) / 0.95) if u < 0.15 else max(0.0, 1 - (u - 0.15) / 0.35))
    return max(0.0, 1 - a ** 1.1)  # ocean: cone from the sea floor
def pk_mountain(img, kind, km, col, prog, x0=200, x1=930, sea=None):
    pts = [(x0, PK_Y0)]
    for i in range(121):
        u = -1 + 2 * i / 120; x = lerp(x0, x1, i / 120)
        pts.append((x, pk_y(km * prog * pk_profile(kind, u))))
    pts.append((x1, PK_Y0))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.polygon(pts, fill=col + (255,))
    mid = (x0 + x1) / 2
    dl.polygon([(mid, pk_y(km * prog * pk_profile(kind, 0)))] + [p for p in pts if p[0] >= mid], fill=tuple(int(c * 0.72) for c in col) + (255,))
    if sea is not None:
        dl.rectangle([x0 - 60, pk_y(sea), x1 + 60, PK_Y0], fill=(40, 110, 200, 150))
        dl.line([(x0 - 60, pk_y(sea)), (x1 + 60, pk_y(sea))], fill=(120, 200, 255, 255), width=3)
    img.alpha_composite(lay)
def pk_ruler(img, th, a=1.0):
    d = ImageDraw.Draw(img); c = (150, 160, 190)
    d.line([(PK_X, PK_Y0), (PK_X, PK_Y1)], fill=c, width=4)
    for k in range(0, 27, 5):
        y = pk_y(k); d.line([(PK_X, y), (PK_X + 22, y)], fill=c, width=3)
        d.text((PK_X - 14, y), f"{k}", font=F(28, "Bold"), fill=c, anchor="rm")
    d.text((PK_X - 14, PK_Y1 - 40), "km", font=F(28, "Bold"), fill=c, anchor="rm")
    d.line([(PK_X - 30, PK_Y0), (W - 40, PK_Y0)], fill=(90, 96, 120), width=3)
def pk_refs(img, th, a=1.0):
    d = ImageDraw.Draw(img); y = pk_y(11)
    for x in range(PK_X + 30, W - 40, 26): d.line([(x, y), (x + 12, y)], fill=(170, 180, 210), width=2)
    d.text((W - 50, y - 22), "airliners cruise ≈ 11 km", font=F(26, "Bold"), fill=(170, 180, 210), anchor="rm")
    ex0, ex1 = 960, 1050; pts = [(ex0, PK_Y0), (ex0 + 30, pk_y(6)), (ex0 + 44, pk_y(8.849)), (ex0 + 58, pk_y(7)), (ex1, PK_Y0)]
    d.polygon(pts, fill=(205, 215, 235)); d.polygon([(ex0 + 44, pk_y(8.849)), (ex0 + 36, pk_y(7.6)), (ex0 + 52, pk_y(7.6))], fill=(255, 255, 255))
    d.text(((ex0 + ex1) / 2, PK_Y0 + 30), "Everest", font=F(26, "ExtraBold"), fill=(205, 215, 235), anchor="mm")
def peaks_vis(img, it, th, t, dur):
    v = it["vis"]; col = tuple(v["col"]); p = easeio((t - 0.4) / max(1.2, dur * 0.55))
    R.paste_c(img, R.planet_sprite(70, tuple(v.get("world_col", col)), light=(-0.8, -0.5)), W - 130, 470)
    text(img, (W - 130, 570), v.get("world", ""), 30, (230, 232, 240), w="ExtraBold")
    pk_ruler(img, th); pk_refs(img, th)
    pk_mountain(img, v["kind"], v["km"], col, p, sea=v.get("sea"))
    d = ImageDraw.Draw(img); top = pk_y(v["km"] * p)
    d.line([(PK_X, top), (PK_X + 70, top)], fill=tuple(th["accent"]), width=5)
    if v.get("note"): text(img, (W / 2, 412), v["note"], 36, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.8) / 0.5))

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
    if th.get("hook") == "peaks":
        # frame 0: the big height + a "?" mountain already towering over Everest and the airliner line
        pk_ruler(img, th); pk_refs(img, th)
        pk_mountain(img, "shield", 25, (200, 110, 80), 0.97 + 0.03 * math.sin(t * 3))
        d = ImageDraw.Draw(img); d.text((615, pk_y(14)), "?", font=F(200, "Black"), fill=(40, 16, 10), anchor="mm")
        text(img, (W / 2, 200), sc.get("big", ""), 150, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 320), sc["top"].upper(), 58, (255, 255, 255))
        text(img, (W / 2, 1380), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "kelvin":
        # frame 0: the big temperature + "colder than empty space" + a frosted "?" nebula sitting below the 2.7 K line
        img.alpha_composite(kv_frost(0.9))
        kv_object(img, {"kind": "nebula", "col": (150, 200, 255)}, W / 2, 760, 230, t, 1.0)
        d = ImageDraw.Draw(img); d.text((W / 2, 760), "?", font=F(200, "Black"), fill=tuple(th["accent"]), anchor="mm")
        kv_ruler(img, th, [], q=True)
        text(img, (W / 2, 210), sc.get("big", ""), 150, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 330), sc["top"].upper(), 60, (255, 255, 255))
        text(img, (W / 2, 1330), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "glow":
        # frame 0: the big claim + five unnamed stars over a dark horizon, #2 pulsing
        horizon(img, t)
        rng = random.Random(8)
        for i, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["rank"])):
            x, y = 180 + i * 180, 640 + 110 * math.sin(i * 1.7)
            f = 10 ** (-0.4 * (o["num"] - 0.03)); r = 14 + 20 * f ** 0.5
            if o["rank"] == 2: r *= 1 + 0.25 * (0.5 + 0.5 * math.sin(t * 5))
            R.paste_c(img, star_sprite(int(r), tuple(o["vis"]["col"])), x, y)
            text(img, (x, y + 70), "?", 54, (200, 205, 230))
        text(img, (W / 2, 210), sc.get("big", ""), 104, tuple(th["accent"]))
        text(img, (W / 2, 315), sc["top"].upper(), 54, (255, 255, 255))
        text(img, (W / 2, 1370), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "lightyears":
        # frame 0: the big distance + a "?" star at 4.24 ly with light crawling down toward the Sun
        order = sorted(ALL_ITEMS, key=lambda o: o["rank"])
        ly_ruler(img, th, [], pulse=4.24 * (1 - (t * 0.35) % 1))
        y = ly_y(4.24); R.paste_c(img, star_sprite(60, (255, 120, 90)), 760, y)
        d = ImageDraw.Draw(img); d.line([(LY_X, y), (700, y)], fill=(255, 120, 90), width=3)
        d.text((760, y), "?", font=F(90, "Black"), fill=(30, 10, 10), anchor="mm")
        text(img, (W / 2, 200), sc.get("big", ""), 118, tuple(th["accent"]))
        text(img, (W / 2, 300), sc["top"].upper(), 60, (255, 255, 255))
        text(img, (W / 2, 1400), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "daylight":
        # tiny Earth spinning madly vs the #1 world barely turning: frame 0 already has both + the claim
        ang = -math.pi / 2 + t * 0.12
        d = ImageDraw.Draw(img); orb = DL_R + 95
        for k in range(0, 360, 8): d.arc([DL_CX - orb, 860 - orb, DL_CX + orb, 860 + orb], k, k + 4, fill=(90, 96, 110), width=2)
        R.paste_c(img, R.sun_sprite(16), DL_CX + orb * math.cos(ang), 860 + orb * math.sin(ang))
        day_planet(img, "Mercury", DL_CX, 860, DL_R, (150, 140, 130), ang)
        d = ImageDraw.Draw(img); d.text((DL_CX, 860), "?", font=F(220, "Black"), fill=tuple(th["accent"]), anchor="mm")
        ea = t * 9.0; ex, ey = 190, 1210
        R.paste_c(img, R.earth_sprite(34, glow=None), ex, ey)
        d.arc([ex - 60, ey - 60, ex + 60, ey + 60], math.degrees(ea) % 360, math.degrees(ea) % 360 + 300, fill=(120, 200, 255), width=5)
        d.text((ex + 90, ey - 18), "Earth: 1 day", font=F(34, "Bold"), fill=(120, 200, 255), anchor="lm")
        d.text((ex + 90, ey + 24), "#1: 176 Earth days", font=F(34, "Bold"), fill=tuple(th["accent"]), anchor="lm")
        text(img, (W / 2, 210), "TOP 5", 150, tuple(th["accent"]))
        for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
            text(img, (W / 2, 340 + i * 96), l, 84, (255, 255, 255))
        text(img, (W / 2, 1400), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "horizons":
        r1 = 1974 * HZ_PX * (0.97 + 0.03 * math.sin(t * 3)); hy = 905
        bh_disk(img, HZ_CX, hy, r1, t, col=col, acc=acc)
        solar_ref(img, t, labels=False, cy=hy)
        d = ImageDraw.Draw(img); d.text((HZ_CX, hy - 120), "?", font=F(200, "Black"), fill=acc, anchor="mm")
        d.text((HZ_CX + 40, hy + 14), "← our solar system", font=F(30, "Bold"), fill=(255, 210, 120), anchor="lm")
        text(img, (W / 2, 210), "TOP 5", 150, acc)
        for i, l in enumerate(wrap(sc["top"].upper(), F(84, "Black"), W - 120)):
            text(img, (W / 2, 340 + i * 96), l, 84, (255, 255, 255))
        text(img, (W / 2, 1400), sc["sub"], 50, tuple(th["accent2"]), w="ExtraBold")
        return
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
    if v["type"] == "horizons":
        horizons_vis(img, it, th, t, dur)
    if v["type"] == "daylight":
        daylight_vis(img, it, th, t, dur)
    if v["type"] == "lightyears":
        lightyears_vis(img, it, th, t, dur)
    if v["type"] == "glow":
        glow_vis(img, it, th, t, dur)
    if v["type"] == "kelvin":
        kelvin_vis(img, it, th, t, dur)
    if v["type"] == "peaks":
        peaks_vis(img, it, th, t, dur)
    # number
    p = easeio((t - 0.5) / 1.6)
    num = it["num"]
    if isinstance(num, (int, float)):
        val = num * p; s = f"{val:,.{it.get('dec', 0)}f}" + it.get("suffix", "")
    else: s = num
    text(img, (W / 2, 1395), s, 130, acc, a=ease((t - 0.4) / 0.4))
    text(img, (W / 2, 1472), it["unit"], 40, (235, 235, 245), w="Bold", a=ease((t - 0.6) / 0.4))
    text(img, (W / 2, 1745), "Source: " + it["source"], 28, (150, 160, 190), w="SemiBold", a=ease((t - 0.8) / 0.4))

def seg_outro(img, sc, th, t, dur):
    a = ease(t / 0.5)
    if th.get("outro") == "peaks":
        pk_ruler(img, th); pk_refs(img, th)
        order = sorted(ALL_ITEMS, key=lambda o: -o["rank"]); n = len(order); span = (940 - 190) / n
        for i, o in enumerate(order):
            x0 = 190 + i * span; v = o["vis"]
            pk_mountain(img, v["kind"], v["km"], tuple(v["col"]), ease((t - i * 0.12) / 0.6), x0=x0, x1=x0 + span - 14)
            text(img, (x0 + span / 2, pk_y(v["km"]) - 34), f'{v["km"]:g}', 34, (255, 255, 255), w="Black")
        text(img, (W / 2, 360), "WHICH MOUNTAIN", 84, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 445), "SHOULD WE PUT NEXT?", 56, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1390), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1480), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "kelvin":
        img.alpha_composite(kv_frost(0.6))
        kv_ruler(img, th, sorted(ALL_ITEMS, key=lambda o: -o["rank"]), y=560)
        if th.get("outro_note"): text(img, (W / 2, 780), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 950), "WHICH PLACE", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1040), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1300), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1390), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "glow":
        horizon(img, t)
        lum_meter(img, th, ALL_ITEMS, cur=None, y=640)
        if th.get("outro_note"): text(img, (W / 2, 820), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 960), "WHICH STAR", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1050), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1330), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1420), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "lightyears":
        ly_ruler(img, th, sorted(ALL_ITEMS, key=lambda o: -o["rank"]), pulse=4.24 * (1 - (t * 0.35) % 1), labels=False)
        if th.get("outro_note"): text(img, (W / 2 + 120, 640), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2 + 120, 860), "WHICH STAR", 90, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2 + 120, 960), "SHOULD WE PUT NEXT?", 54, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2 + 120, 1180), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2 + 120, 1270), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "daylight":
        order = sorted(ALL_ITEMS, key=lambda o: o["vis"]["days"])
        d = ImageDraw.Draw(img); x0, x1 = 110, W - 110
        for i, o in enumerate(order):
            y = 420 + i * 120; p = ease((t - i * 0.15) / 0.6); x = lerp(x0, x1, o["vis"]["days"] / DL_MAX * p)
            d.rounded_rectangle([x0, y - 26, max(x0 + 52, x), y + 26], 26, fill=tuple(o["vis"]["col"]))
            d.text((x0 + 16, y - 52), o["short"], font=F(32, "ExtraBold"), fill=(230, 232, 238), anchor="lm")
            d.text((x1, y - 52), f'{o["vis"]["days"]:g} days', font=F(32, "ExtraBold"), fill=tuple(th["accent"]), anchor="rm")
        if th.get("outro_note"): text(img, (W / 2, 1060), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.6) / 0.5))
        text(img, (W / 2, 1220), "SUBSCRIBE", 110, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1320), "to Cosmic Scale", 56, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "horizons":
        d = ImageDraw.Draw(img)
        for i, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["vis"]["au"])):
            r = o["vis"]["au"] * HZ_PX * 0.62 * ease((t - i * 0.15) / 0.5)
            if r > 2: d.ellipse([W / 2 - r, 640 - r, W / 2 + r, 640 + r], outline=mix((120, 90, 200), tuple(th["accent"]), i / 4), width=5)
        d.ellipse([W / 2 - 4, 636, W / 2 + 4, 644], fill=(255, 200, 90))
        if th.get("outro_note"): text(img, (W / 2, 960), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.6) / 0.5))
        text(img, (W / 2, 1180), "SUBSCRIBE", 110, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1280), "to Cosmic Scale", 56, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
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
