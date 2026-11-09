"""Cosmic Scale pipeline: script -> voice (Kokoro offline, EN) -> code-drawn space visuals -> MP4 1080p30 + SRT.
Usage: python3 -I render.py ep01_sun.py out/ep01 [--preview]
EP02 added scenes: clock, escape, sky, thermo, energy, ocean, galaxy
EP03 added scenes: zoom, stretch, horizons, deepfield, shrink (violet/magenta palette)
EP04 added scenes: blackhole, spaghetti, twoclocks, horizonsize, inside (ember orange / pale cyan palette)
EP05 added scenes: inflate, flight, measure, density, heavyvsbig, balance (crimson / cream palette)
EP07 added scenes: teaspoon, pulsechart, crush, ladder (log scale), layers, lensing, pulsar, merger (electric blue / coral palette)
EP06 added scenes: spinglobe (globe + speed by latitude; top=True rings; slow=True), pendulum, fling, bulge, yearday, dayclock (teal / amber palette)
"""
import sys, os, re, math, subprocess, importlib.util, json, random, hashlib
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/opentype/inter/"
_fc = {}
def F(size, w="Bold"):
    k = (int(size), w)
    if k not in _fc: _fc[k] = ImageFont.truetype(FONT_DIR + f"Inter-{w}.otf", int(size))
    return _fc[k]

SPACE = (5, 7, 15)
WHITE, DIM, GOLD, CYAN, RED, BLUE, VIOLET = (238, 242, 250), (125, 138, 165), (255, 194, 75), (79, 209, 255), (240, 104, 90), (91, 141, 239), (160, 120, 255)
ICE, FROST = (170, 225, 255), (210, 240, 255)
BRAND = "COSMIC SCALE"

def hexc(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def easeio(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): t = max(0, min(1, t)); return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))

# ---------------- assets ----------------
def make_starfield(w, h, n, seed, big=False):
    rng = np.random.default_rng(seed)
    img = np.zeros((h, w, 3), np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    for _ in range(3):
        cx, cy, s = rng.uniform(0, w), rng.uniform(0, h), rng.uniform(300, 700)
        col = np.array([[40, 30, 90], [20, 50, 90], [70, 25, 70]][rng.integers(0, 3)], np.float32)
        g = np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s * s)))[..., None]
        img += g * col * 0.22
    img += np.array(SPACE, np.float32)
    base = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(base)
    for _ in range(n):
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        b = rng.uniform(0.25, 1.0) ** 2
        c = mix((150, 170, 255), (255, 230, 200), rng.uniform())
        c = tuple(int(v * b + 10) for v in c)
        r = 0.6 if rng.uniform() < 0.9 else 1.2
        d.ellipse([x - r, y - r, x + r, y + r], fill=c)
    if big:
        for _ in range(40):
            x, y = rng.uniform(0, w), rng.uniform(0, h)
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(255, 255, 255))
    return base

def radial(size, stops):
    """stops: list of (r_frac, (r,g,b,a))"""
    yy, xx = np.mgrid[0:size, 0:size]
    d = np.sqrt((xx - size / 2) ** 2 + (yy - size / 2) ** 2) / (size / 2)
    out = np.zeros((size, size, 4), np.float32)
    rs = [s[0] for s in stops]; cs = np.array([s[1] for s in stops], np.float32)
    for ch in range(4):
        out[..., ch] = np.interp(d, rs, cs[:, ch])
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")

_sun = {}
def sun_sprite(r):
    r = int(r)
    if r not in _sun:
        size = r * 6
        k = 1 / 3
        _sun[r] = radial(size, [(0, (255, 250, 225, 255)), (k * 0.7, (255, 225, 140, 255)), (k * 0.97, (255, 170, 60, 255)), (k, (255, 160, 50, 255)),
                                (k * 1.05, (255, 150, 40, 150)), (k * 1.6, (255, 120, 30, 45)), (1.0, (255, 100, 20, 0))])
    return _sun[r]

def paste_c(base, spr, cx, cy, a=1.0):
    if a <= 0: return
    if a < 1:
        spr = spr.copy(); al = spr.getchannel("A").point(lambda v: int(v * a)); spr.putalpha(al)
    base.alpha_composite(spr, (int(cx - spr.width / 2), int(cy - spr.height / 2)))

_pl = {}
def planet_sprite(r, col, light=(-1, -0.3), earth=False, glow=None):
    key = (int(r), col, light, earth, glow)
    if key in _pl: return _pl[key]
    r = int(r); pad = int(r * 0.6) + 4; size = 2 * r + 2 * pad
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    nx, ny = (xx - size / 2) / r, (yy - size / 2) / r
    rr = nx ** 2 + ny ** 2; inside = rr <= 1
    nz = np.sqrt(np.clip(1 - rr, 0, 1))
    lx, ly = light; lz = 0.35; ln = math.sqrt(lx * lx + ly * ly + lz * lz)
    shade = np.clip((nx * lx + ny * ly + nz * lz) / ln, 0, 1) * 0.95 + 0.05
    rgb = np.zeros((size, size, 3), np.float32); rgb[:] = col
    if earth:
        def fbm(seed, oct=5):
            r2 = np.random.default_rng(seed); acc = np.zeros((size, size), np.float32)
            for k in range(oct):
                n = 4 * 2 ** k
                lo = Image.fromarray((r2.random((n, n)) * 255).astype(np.uint8)).resize((size, size), Image.BICUBIC)
                acc += (np.asarray(lo, np.float32) / 255 - 0.5) / (1.7 ** k)
            return acc
        land_n = fbm(11); cl = fbm(29)
        land = land_n > 0.12
        rgb[land] = (58, 128, 70)
        rgb[land_n > 0.3] = (140, 125, 85)
        rgb[np.abs(ny) > 0.86] = (235, 240, 245)
        cw = np.clip((cl - 0.02) / 0.22, 0, 1)[..., None]
        rgb = rgb * (1 - cw * 0.85) + 250 * cw * 0.85
    rgb = rgb * shade[..., None]
    a = np.where(inside, 255, 0).astype(np.float32)
    if glow:
        dd = np.sqrt(rr); rim = np.clip(1 - np.abs(dd - 1) / 0.12, 0, 1) * (dd > 0.9)
        gl = np.clip((1.25 - dd) / 0.25, 0, 1) * (dd > 1)
        rgb = rgb * (1 - rim[..., None] * 0.5) + np.array(glow, np.float32) * rim[..., None] * 0.5
        rgb = np.where((dd > 1)[..., None], np.array(glow, np.float32), rgb)
        a = np.maximum(a, gl * 90)
    img = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8), "RGBA")
    _pl[key] = img
    return img

def earth_sprite(r, light=(-1, -0.2), glow=(120, 180, 255)):
    return planet_sprite(r, (70, 130, 230), light=light, earth=True, glow=glow)

# ---------------- text helpers ----------------
def alpha_text(base, xy, txt, font, fill, a, anchor="mm", dy=0, shadow=True):
    if a <= 0: return
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    if shadow: d.text((xy[0] + 3, xy[1] + dy + 4), txt, font=font, fill=(0, 0, 0, int(160 * a)), anchor=anchor)
    d.text((xy[0], xy[1] + dy), txt, font=font, fill=fill + (int(255 * a),), anchor=anchor)
    base.alpha_composite(layer)

def caption(img, txt, a, y=H - 120, col=None):
    if not txt or a <= 0: return
    f = F(42, "SemiBold"); tw = f.getlength(txt)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([W / 2 - tw / 2 - 34, y - 42, W / 2 + tw / 2 + 34, y + 42], 20, fill=(8, 12, 26, int(200 * a)), outline=(79, 209, 255, int(120 * a)), width=2)
    img.alpha_composite(lay)
    alpha_text(img, (W / 2, y), txt, f, col or WHITE, a, shadow=False)

def logo_img(size):
    s = size; img = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    pl = planet_sprite(int(s * 0.28), (90, 120, 255), light=(-0.8, -0.6))
    box = [s * 0.06, s * 0.36, s * 0.94, s * 0.64]
    d.arc(box, 180, 360, fill=GOLD, width=max(2, int(s * 0.045)))
    img.alpha_composite(pl, (int(s / 2 - pl.width / 2), int(s / 2 - pl.height / 2)))
    d = ImageDraw.Draw(img); d.arc(box, 0, 180, fill=GOLD, width=max(2, int(s * 0.045)))
    return img

_logo_small = None
def chrome(img, prog):
    global _logo_small
    if _logo_small is None: _logo_small = logo_img(46)
    img.alpha_composite(_logo_small, (52, 40))
    d = ImageDraw.Draw(img)
    d.text((108, 63), BRAND, font=F(22, "SemiBold"), fill=DIM, anchor="lm")
    d.rectangle([0, H - 5, int(W * prog), H], fill=CYAN)

# ---------------- background ----------------
SF1 = SF2 = None
def background(t):
    ox = int(t * 6) % 400
    img = SF1.crop((ox, 0, ox + W, H)).convert("RGBA")
    ox2 = int(t * 14) % 400
    img.alpha_composite(SF2.crop((ox2, 0, ox2 + W, H)))
    return img

# ---------------- scenes (EP01) ----------------
def sc_sun(img, v, t, dur):
    t0 = v.get("vanish_at", 0.6) * dur; gone = t0 <= t < t0 + v.get("gone_for", 1.0)
    forever = v.get("forever", False)
    r = 230 + 8 * math.sin(t * 1.3)
    if forever and t >= t0: gone = True
    if not gone:
        a = 1.0
        if t >= t0 + 1.0: a = ease((t - t0 - 1.0) / 0.25)
        paste_c(img, sun_sprite(int(r)), W / 2, H / 2 - 40, a)
    else:
        d = ImageDraw.Draw(img)
        if forever:
            fl = max(0.0, 1 - (t - t0) / 0.35)
            if fl > 0: paste_c(img, sun_sprite(int(r)), W / 2, H / 2 - 40, fl)
            for k in range(0, 360, 10):
                d.arc([W / 2 - r, H / 2 - 40 - r, W / 2 + r, H / 2 - 40 + r], k, k + 5, fill=(90, 100, 130), width=3)
            alpha_text(img, (W / 2, H / 2 - 40), v.get("label", "GONE"), F(80, "ExtraBold"), WHITE, ease((t - t0 - 0.3) / 0.4))
        else:
            d.ellipse([W / 2 - r, H / 2 - 40 - r, W / 2 + r, H / 2 - 40 + r], outline=(80, 90, 120), width=3)
            alpha_text(img, (W / 2, H / 2 - 40), "1 second", F(80, "ExtraBold"), WHITE, 1)
    if t > t0 + 1.2: caption(img, v.get("caption"), ease((t - t0 - 1.2) / 0.5))

def sc_title(img, v, t, dur):
    a1, a2 = ease(t / 0.6), ease((t - 0.35) / 0.6)
    lines = v["title"].split("\n")
    size = 108 if max(len(l) for l in lines) < 24 else 86
    f = F(size, "ExtraBold"); lh = size * 1.18
    y0 = H / 2 - (len(lines) - 1) * lh / 2 - (40 if v.get("sub") else 0)
    if v.get("brand"):
        y0 += 70
        lg = logo_img(200); paste_c(img, lg, W / 2, y0 - lh / 2 - 130, a1)
    for i, l in enumerate(lines):
        alpha_text(img, (W / 2, y0 + i * lh), l, f, WHITE, a1, dy=(1 - a1) * 40)
    if v.get("sub"):
        alpha_text(img, (W / 2, y0 + (len(lines) - 1) * lh + lh * 0.85), v["sub"], F(50, "SemiBold"), v.get("subcol") and tuple(v["subcol"]) or GOLD, a2, dy=(1 - a2) * 30)

def fmt_num(x, dec):
    return f"{x:,.{dec}f}"

def sc_bignumber(img, v, t, dur):
    p = easeio((t - 0.3) / 2.0)
    val = lerp(v["from"], v["to"], p); dec = v.get("decimals", 0)
    txt = v.get("prefix", "") + fmt_num(val, dec) + v.get("suffix", "")
    a = ease(t / 0.4)
    size = 230 if len(txt) < 9 else 170
    alpha_text(img, (W / 2, H / 2 - 50), txt, F(size, "Black"), mix(WHITE, tuple(v.get("col", GOLD)), p), a)
    alpha_text(img, (W / 2, H / 2 + 130), v.get("caption", ""), F(44, "Medium"), DIM, ease((t - 0.8) / 0.6))

SUNX = 640
def draw_orbit(img, t, dur, v, ex_angle):
    d = ImageDraw.Draw(img); cy = H / 2 - 20; R = 820
    d.ellipse([SUNX - R, cy - R, SUNX + R, cy + R], outline=(50, 70, 110), width=2)
    if v.get("ghost_sun"):
        r = 110
        d.ellipse([SUNX - r, cy - r, SUNX + r, cy + r], outline=(110, 120, 150), width=3)
        for k in range(0, 360, 20):
            a1 = math.radians(k); d.line([(SUNX + r * math.cos(a1), cy + r * math.sin(a1)), (SUNX + (r + 10) * math.cos(a1), cy + (r + 10) * math.sin(a1))], fill=(110, 120, 150), width=3)
        d.text((SUNX, cy), "?", font=F(90, "Black"), fill=(110, 120, 150), anchor="mm")
    else:
        paste_c(img, sun_sprite(110), SUNX, cy)
    ex, ey = SUNX + R * math.cos(ex_angle), cy + R * math.sin(ex_angle)
    paste_c(img, earth_sprite(34, light=(-1, 0)), ex, ey)
    d = ImageDraw.Draw(img); d.text((ex, ey + 70), "Earth", font=F(34, "SemiBold"), fill=WHITE, anchor="mm")
    return ex, ey, cy, R

def sc_orbit(img, v, t, dur):
    ang = -0.08 + t * 0.006
    ex, ey, cy, R = draw_orbit(img, t, dur, v, ang)
    if v.get("wave"):
        period = 4.0
        for k in range(3):
            ph = ((t + k * period / 3) % period) / period
            rr = 110 + ph * (R + 200)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            d2.ellipse([SUNX - rr, cy - rr, SUNX + rr, cy + rr], outline=GOLD + (int(170 * (1 - ph)),), width=4)
            img.alpha_composite(lay)
    if v.get("clock"):
        p = min(1, t / max(1, dur * 0.8)); s = int(499 * p)
        alpha_text(img, (W - 330, 200), f"{s // 60:02d}:{s % 60:02d}", F(96, "Black"), GOLD, ease(t / 0.5))
        alpha_text(img, (W - 330, 275), "light travel time", F(30, "Medium"), DIM, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

def sc_countdown(img, v, t, dur):
    p = min(1, t / (dur * 0.85)); s = int(round(v["seconds"] * (1 - p)))
    a = ease(t / 0.4)
    alpha_text(img, (W / 2, H / 2 - 60), f"{s // 60:02d}:{s % 60:02d}", F(250, "Black"), GOLD if s > 0 else RED, a)
    alpha_text(img, (W / 2, H / 2 + 120), v["label"], F(46, "SemiBold"), WHITE, a)
    paste_c(img, sun_sprite(50), W / 2, 220, a)

def sc_race(img, v, t, dur):
    d = ImageDraw.Draw(img); x0, x1 = 260, W - 260
    p = easeio(t / (dur * 0.8))
    for i, (lab, col, lag) in enumerate([(v["a"], VIOLET, 0.0), (v["b"], GOLD, 0.012)]):
        y = 400 + i * 220
        d.line([(x0, y), (x1, y)], fill=(50, 65, 100), width=4)
        d.text((x0, y - 60), lab, font=F(40, "SemiBold"), fill=col, anchor="lm")
        px = lerp(x0, x1, max(0, p - lag * (1 - p)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        for k in range(14):
            d2.ellipse([px - 30 * k - 10, y - 10, px - 30 * k + 10, y + 10], fill=col + (int(220 * (1 - k / 14)),))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.ellipse([px - 18, y - 18, px + 18, y + 18], fill=col)
    d.text((x1, 280), v.get("dist", "130 million light-years"), font=F(30, "Medium"), fill=DIM, anchor="rm")
    d.line([(x1, 300), (x1, 700)], fill=WHITE, width=3)
    caption(img, v.get("caption"), ease((t - dur * 0.8) / 0.5))

def sc_gap(img, v, t, dur):
    cy = H / 2 - 20; x0, x1 = 300, W - 300
    d = ImageDraw.Draw(img)
    r = 90; d.ellipse([x0 - r, cy - r, x0 + r, cy + r], outline=(110, 120, 150), width=3)
    p = easeio(t / (dur * 0.75)); gw = 140
    gx = lerp(x0 + 60, x1 - 40, p)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    for x in range(x0 + r, x1 - 40, 6):
        if gx - gw / 2 < x < gx + gw / 2: continue
        aa = 120 if x > gx else 80
        d2.line([(x, cy - 70), (x, cy + 70)], fill=GOLD + (aa,), width=4)
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2)))
    paste_c(img, sun_sprite(90), x0, cy, 1.0 if t > 0.5 else 0.0)
    lit = 0.25 if abs(gx - x1) < gw * 0.6 else 1.0
    paste_c(img, earth_sprite(60, light=(-1, 0)), x1, cy, 1.0)
    if lit < 1:
        dk = Image.new("RGBA", (180, 180), (0, 0, 0, 0)); ImageDraw.Draw(dk).ellipse([28, 28, 152, 152], fill=(0, 0, 0, 200)); paste_c(img, dk, x1, cy)
    d = ImageDraw.Draw(img)
    d.text((gx, cy - 120), "1 s gap", font=F(36, "Bold"), fill=WHITE, anchor="mm")
    d.text((x1, cy + 120), "Earth", font=F(34, "SemiBold"), fill=WHITE, anchor="mm")
    caption(img, v.get("caption"), ease((t - 0.6) / 0.5))

def sc_earth(img, v, t, dur):
    r = 330; cx, cy = W / 2, H / 2 - 30
    paste_c(img, earth_sprite(r), cx, cy)
    mid = dur * 0.45
    if v.get("blink") and mid <= t < mid + 1.0:
        dk = Image.new("RGBA", (2 * r + 20, 2 * r + 20), (0, 0, 0, 0)); dd = ImageDraw.Draw(dk)
        dd.ellipse([10, 10, 2 * r + 10, 2 * r + 10], fill=(2, 4, 12, 235))
        rng = random.Random(5)
        for _ in range(260):
            a = rng.uniform(0, 6.28); rr = r * math.sqrt(rng.uniform(0, 0.95))
            x, y = r + 10 + rr * math.cos(a), r + 10 + rr * math.sin(a)
            dd.ellipse([x - 1.5, y - 1.5, x + 1.5, y + 1.5], fill=(255, 200, 120, 220))
        paste_c(img, dk, cx, cy)
        alpha_text(img, (cx, cy), "12:00 — DARK", F(70, "Black"), WHITE, 1)
    caption(img, v.get("caption"), ease((t - 0.6) / 0.5))

def sc_bullets(img, v, t, dur):
    alpha_text(img, (160, 210), v["title"], F(76, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    items = v["items"]; hl = v.get("highlight", -1); acc = tuple(v.get("col", CYAN))
    span = max(0.8, dur * 0.6) / len(items)
    for i, it in enumerate(items):
        a = ease((t - 0.3 - i * span) / 0.5)
        col = acc if (hl < 0 or i == hl) else WHITE
        y = 380 + i * 130
        if a > 0:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            d2.ellipse([160, y + 6, 190, y + 36], fill=col + (int(255 * a),))
            d2.text((220 + (1 - a) * 30, y + 22), it, font=F(54, "SemiBold"), fill=WHITE + (int(255 * a),), anchor="lm")
            img.alpha_composite(lay)

def sc_bars(img, v, t, dur):
    alpha_text(img, (160, 200), v["title"], F(64, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    mx = max(i[1] for i in v["items"]); d = ImageDraw.Draw(img)
    for i, (lab, val, c) in enumerate(v["items"]):
        p = ease((t - 0.5 - i * 0.7) / 0.9); y = 400 + i * 170
        d.text((160, y), lab, font=F(44, "SemiBold"), fill=mix(SPACE, WHITE, p), anchor="lm")
        bw = 1000 * val / mx * p
        d.rounded_rectangle([640, y - 42, 640 + max(4, bw), y + 42], 14, fill=hexc(c))
        sfx = v.get("suffix", ""); sfx = sfx[:-1] if round(val * p) == 1 and sfx.endswith("s") else sfx
        if p > 0.05: d.text((640 + max(4, bw) + 24, y), f"{val * p:.0f}" + sfx, font=F(52, "Bold"), fill=WHITE, anchor="lm")

def sc_compare(img, v, t, dur):
    d = ImageDraw.Draw(img)
    cl, cr = [tuple(c) for c in v.get("cols", [RED, CYAN])]; strike = v.get("strike", True)
    for k, (col, side, x) in enumerate([(cl, v["left"], W * 0.27), (cr, v["right"], W * 0.73)]):
        a = ease((t - k * 1.2) / 0.6)
        if a <= 0: continue
        d.rounded_rectangle([x - 380, 200, x + 380, 880], 30, fill=mix(SPACE, (16, 24, 48), a), outline=mix(SPACE, col, a), width=4)
        d.text((x, 290), side[0], font=F(80, "ExtraBold"), fill=mix(SPACE, col, a), anchor="mm")
        for i, s in enumerate(side[1:]):
            tc = mix(SPACE, WHITE, a)
            d.text((x, 450 + i * 120), s, font=F(46, "SemiBold"), fill=tc, anchor="mm")
            if k == 0 and strike: d.line([(x - F(46, "SemiBold").getlength(s) / 2, 450 + i * 120), (x + F(46, "SemiBold").getlength(s) / 2, 450 + i * 120)], fill=mix(SPACE, RED, a), width=4)

PCOL = {"Mercury": (170, 160, 150), "Venus": (230, 200, 140), "Earth": (70, 130, 230), "Mars": (210, 100, 70), "Jupiter": (215, 175, 130),
        "Saturn": (225, 205, 150), "Uranus": (150, 215, 225), "Neptune": (80, 110, 230)}
PRAD = {"Mercury": 10, "Venus": 16, "Earth": 17, "Mars": 12, "Jupiter": 40, "Saturn": 34, "Uranus": 24, "Neptune": 23}

def sc_scale(img, v, t, dur):
    pts = v["points"]; n = len(pts); x0, x1, y = 200, W - 200, H / 2 + 20
    d = ImageDraw.Draw(img)
    p = ease(t / (dur * 0.7))
    d.line([(x0, y), (lerp(x0, x1, p), y)], fill=(70, 90, 130), width=4)
    d.text((W / 2, 200), v.get("title", "How long until they see the blink?"), font=F(56, "ExtraBold"), fill=WHITE, anchor="mm")
    d.text((W / 2, 262), v.get("sub", "logarithmic scale — each step is a giant leap"), font=F(28, "Medium"), fill=DIM, anchor="mm")
    for i, (lab, tm) in enumerate(pts):
        x = lerp(x0, x1, i / (n - 1)); a = ease((t - i * dur * 0.7 / n) / 0.5)
        if a <= 0: continue
        c = mix(SPACE, GOLD if i == n - 1 else tuple(v.get("col", CYAN)), a)
        d.ellipse([x - 16, y - 16, x + 16, y + 16], fill=c)
        d.text((x, y - 70), lab, font=F(36, "Bold"), fill=mix(SPACE, WHITE, a), anchor="mm")
        d.text((x, y + 70), tm, font=F(38, "Black"), fill=c, anchor="mm")

def sc_tangent(img, v, t, dur):
    d = ImageDraw.Draw(img)
    cx, cy, R = W / 2, H + 1700, 2200
    d.arc([cx - R, cy - R, cx + R, cy + R], 240, 300, fill=(60, 90, 140), width=4)
    ang = math.radians(270)
    ex, ey = cx + R * math.cos(ang), cy + R * math.sin(ang)
    p = ease((t - 1.0) / 1.5)
    if p > 0:
        L = 760 * p
        for k in range(0, int(L), 30):
            d.line([(ex + k, ey), (ex + min(k + 18, L), ey)], fill=CYAN, width=5)
        d.text((ex + 380, ey - 50), "straight line: 30 km in 1 s", font=F(36, "SemiBold"), fill=CYAN, anchor="mm")
        d.text((ex + 520, ey + 120), "orbit curves away", font=F(32, "Medium"), fill=DIM, anchor="mm")
    paste_c(img, earth_sprite(46, light=(0, 1)), ex, ey)
    q = ease((t - dur * 0.55) / 0.7)
    if q > 0:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        bx, by = 1450, 300
        d2.rounded_rectangle([bx - 240, by - 110, bx + 240, by + 110], 24, fill=(10, 16, 34, int(230 * q)), outline=GOLD + (int(255 * q),), width=3)
        img.alpha_composite(lay)
        alpha_text(img, (bx, by - 35), "Off-orbit drift", F(36, "SemiBold"), DIM, q)
        alpha_text(img, (bx, by + 35), "≈ 3 mm", F(80, "Black"), GOLD, q)
    caption(img, v.get("caption"), ease((t - 0.5) / 0.5))

def sc_lightrace(img, v, t, dur):
    pl = v["planets"]; x0, x1, y = 230, W - 120, H / 2 - 20
    pos = lambda au: x0 + (x1 - x0) * math.sqrt(au / 30.07) * 0.97 + 40
    paste_c(img, sun_sprite(70), x0 - 60, y)
    d = ImageDraw.Draw(img); d.line([(x0, y), (x1, y)], fill=(40, 55, 90), width=2)
    p = min(1.0, t / (dur * 0.88)); gx = lerp(x0, pos(30.07) + 30, p)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    if gx - 20 > x0: d2.rectangle([x0, y - 6, gx - 20, y + 6], fill=GOLD + (60,))
    d2.rectangle([gx - 20, y - 60, gx, y + 60], fill=(0, 0, 0, 230), outline=(200, 200, 220, 200))
    img.alpha_composite(lay)
    for i, (name, au, lbl) in enumerate(pl):
        x = pos(au); passed = gx > x
        recent = 0 <= gx - x < 60
        spr = planet_sprite(PRAD[name], PCOL[name], light=(-1, 0), earth=(name == "Earth"))
        paste_c(img, spr, x, y, 0.35 if recent else 1.0)
        d = ImageDraw.Draw(img)
        off = (i * 42) if i < 4 else ((i % 2) * 40)
        d.text((x, y - 85 - off), name, font=F(28, "SemiBold"), fill=WHITE, anchor="mm")
        if i < 4: d.line([(x, y - 70 - off), (x, y - 30)], fill=(70, 85, 120), width=1)
        d.text((x, y + 85 + off), lbl, font=F(30, "Bold"), fill=GOLD if passed else DIM, anchor="mm")
    d.text((W / 2, 170), v.get("title", "When each planet sees the dark second"), font=F(48, "ExtraBold"), fill=WHITE, anchor="mm")
    d.text((W / 2, H - 90), "distances not to scale (square-root scale)", font=F(26, "Medium"), fill=DIM, anchor="mm")

def sc_voyager(img, v, t, dur):
    y = H / 2 - 20; x0, x1 = 240, W - 260
    paste_c(img, sun_sprite(40), x0, y)
    paste_c(img, planet_sprite(14, (70, 130, 230), light=(-1, 0), earth=True), x0 + 60, y)
    d = ImageDraw.Draw(img)
    for x in range(x0 + 90, int(x1) - 40, 26): d.line([(x, y), (x + 12, y)], fill=(80, 100, 140), width=3)
    vx = x1
    d.ellipse([vx - 34, y - 34, vx + 34, y + 34], outline=WHITE, width=5)
    d.line([(vx, y), (vx + 90, y - 60)], fill=WHITE, width=4); d.line([(vx, y), (vx - 70, y + 70)], fill=WHITE, width=3)
    d.rectangle([vx - 10, y - 10, vx + 10, y + 10], fill=GOLD)
    d.text((vx, y - 90), "Voyager 1", font=F(40, "Bold"), fill=WHITE, anchor="mm")
    d.text((x0 + 30, y + 80), "Earth", font=F(30, "SemiBold"), fill=WHITE, anchor="mm")
    period = 6.0; ph = (t % period) / period
    px = lerp(x0 + 70, vx - 40, ph)
    d.ellipse([px - 12, y - 12, px + 12, y + 12], fill=CYAN)
    d.text((W / 2, y + 150), v.get("line", "25.9 billion km  •  signal time: 24 hours"), font=F(44, "SemiBold"), fill=GOLD, anchor="mm")
    caption(img, v.get("caption"), ease((t - 0.6) / 0.5))

def sc_stars(img, v, t, dur):
    rng = random.Random(11); d = ImageDraw.Draw(img)
    for i in range(70):
        x, y = rng.uniform(100, W - 100), rng.uniform(120, H - 220); ph = rng.uniform(0, 6.28); sp = rng.uniform(0.8, 2.5)
        b = 0.5 + 0.5 * math.sin(t * sp + ph)
        gone = i % 9 == 0 and t > dur * 0.5 + (i % 5) * 0.4
        if gone: b = max(0, 1 - (t - dur * 0.5 - (i % 5) * 0.4) / 0.8) * b
        r = 2 + 3 * b
        c = mix((150, 170, 255), (255, 240, 210), rng.random())
        d.ellipse([x - r, y - r, x + r, y + r], fill=mix(SPACE, c, 0.3 + 0.7 * b))
    caption(img, v.get("caption"), ease((t - 0.6) / 0.5))

# ---------------- scenes (EP02: cold palette, new types) ----------------
CLOCK_MARKS = ["0 s", "8 min", "1 day", "1 week", "1 year", "1,000 yrs", "millions"]
def sc_clock(img, v, t, dur):
    """mission clock card: big T+ stamp, timeline ribbon with current stage lit"""
    a = ease(t / 0.5); idx = v["idx"]
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rectangle([0, 0, W, H], fill=(2, 6, 16, int(150 * a)))
    img.alpha_composite(lay)
    alpha_text(img, (W / 2, 330), "ELAPSED SINCE THE SUN VANISHED", F(34, "SemiBold"), DIM, a)
    stamp = v["stamp"]; f = F(190 if len(stamp) < 12 else 150, "Black")
    alpha_text(img, (W / 2, 470), stamp, f, ICE, a, dy=(1 - a) * 30)
    if v.get("sub"): alpha_text(img, (W / 2, 610), v["sub"], F(48, "SemiBold"), WHITE, ease((t - 0.5) / 0.5))
    x0, x1, y = 220, W - 220, 820; n = len(CLOCK_MARKS)
    d = ImageDraw.Draw(img)
    d.line([(x0, y), (x1, y)], fill=(50, 70, 105), width=4)
    fill_to = lerp(x0, x1, (idx - 1 + ease((t - 0.3) / 1.2)) / (n - 1)) if idx > 0 else x0
    d.line([(x0, y), (fill_to, y)], fill=ICE, width=6)
    for i, m in enumerate(CLOCK_MARKS):
        x = lerp(x0, x1, i / (n - 1)); on = i <= idx
        r = 16 if i == idx else 10
        col = ICE if on else (70, 85, 120)
        if i == idx:
            pulse = 0.5 + 0.5 * math.sin(t * 4)
            d.ellipse([x - r - 10 * pulse, y - r - 10 * pulse, x + r + 10 * pulse, y + r + 10 * pulse], outline=ICE, width=2)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
        d.text((x, y + 50), m, font=F(30, "Bold" if i == idx else "Medium"), fill=WHITE if i == idx else DIM, anchor="mm")

def sc_escape(img, v, t, dur):
    """Earth leaves on a straight line from the empty spot where the Sun was; Moon stays with it"""
    cx, cy = 360, 640; R = 150  # scaled: 1 AU = 150 px
    d = ImageDraw.Draw(img)
    for k in range(0, 360, 6): d.arc([cx - R, cy - R, cx + R, cy + R], k, k + 3, fill=(70, 90, 130), width=2)
    if v.get("jupiter"):
        RJ = 5.2 * R
        d.arc([cx - RJ, cy - RJ, cx + RJ, cy + RJ], 270, 360, fill=(150, 120, 90), width=2)
        d.text((cx + RJ * math.cos(math.radians(330)) + 20, cy + RJ * math.sin(math.radians(330)) - 10), "Jupiter's orbit", font=F(28, "Medium"), fill=(190, 160, 120), anchor="lm")
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], outline=(130, 140, 170), width=2)
    d.text((cx, cy + 40), "where the Sun was", font=F(26, "Medium"), fill=DIM, anchor="mm")
    au_max = v.get("au", 6.28)
    p = easeio(t / (dur * 0.85)); s_au = au_max * p
    sx, sy = cx, cy - R  # Earth at top of orbit moving right (tangent)
    ex, ey = sx + s_au * R, sy
    d.line([(sx, sy), (ex, ey)], fill=CYAN, width=3)
    dist = math.hypot(1, s_au)
    paste_c(img, earth_sprite(22, light=(0, 0)), ex, ey)
    ma = t * 1.6; mx, my = ex + 46 * math.cos(ma), ey + 46 * math.sin(ma) * 0.6
    paste_c(img, planet_sprite(8, (150, 150, 150), light=(0, 0)), mx, my)
    d = ImageDraw.Draw(img)
    d.text((ex, ey - 52), "Earth + Moon", font=F(28, "SemiBold"), fill=WHITE, anchor="mm")
    bx, by = W - 330, 250
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.rounded_rectangle([bx - 300, by - 120, bx + 300, by + 130], 26, fill=(8, 14, 30, 220), outline=ICE + (200,), width=3)
    img.alpha_composite(lay)
    alpha_text(img, (bx, by - 70), v.get("label", "distance from the Sun's old spot"), F(28, "Medium"), DIM, 1, shadow=False)
    alpha_text(img, (bx, by + 5), f"{dist * 149.6:,.0f} million km", F(58, "Black"), ICE, 1, shadow=False)
    alpha_text(img, (bx, by + 78), f"{dist:.1f} AU  •  {v.get('time', '1 year')}", F(32, "SemiBold"), WHITE, 1, shadow=False)
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

def sc_sky(img, v, t, dur):
    """landscape: blue day sky drains to black, stars appear, the Moon fades to a black disc"""
    p = easeio((t - v.get("start", 0.15) * dur) / (dur * v.get("speed", 0.45)))
    if v.get("night_only"): p = 1.0
    sky = np.zeros((H, W, 3), np.float32)
    g = np.linspace(0, 1, H)[:, None]
    day = np.array([70, 140, 230], np.float32) * (1 - g) + np.array([170, 210, 245], np.float32) * g
    night = np.array([3, 5, 12], np.float32) * (1 - g) + np.array([10, 14, 30], np.float32) * g
    sky[:] = (day * (1 - p) + night * p)[:, None, :]
    base = Image.fromarray(sky.astype(np.uint8)).convert("RGBA")
    if p > 0.3:
        st = SF1.crop((0, 0, W, H)).convert("RGBA"); st.putalpha(int(255 * min(1, (p - 0.3) / 0.5)))
        base.alpha_composite(st)
    mx, my, mr = 1400, 300, 70
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    moon_lit = 1 - ease((t - v.get("moon_off", 0.55) * dur) / 1.0) if v.get("moon") else 0
    if v.get("moon"):
        mc = mix((6, 8, 16), (235, 235, 225), moon_lit)
        d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=mc + (255,))
        if moon_lit < 0.2: d.ellipse([mx - mr, my - mr, mx + mr, my + mr], outline=(40, 50, 80, 200), width=2)
    base.alpha_composite(lay)
    d = ImageDraw.Draw(base)
    rng = random.Random(3); pts = [(0, H)]
    for x in range(0, W + 40, 40): pts.append((x, 860 + 50 * math.sin(x / 210) + rng.uniform(-14, 14)))
    pts.append((W, H)); d.polygon(pts, fill=(4, 6, 10))
    for tx in (300, 360, 1650):
        d.polygon([(tx, 880), (tx - 40, 980), (tx + 40, 980)], fill=(4, 6, 10)); d.polygon([(tx, 830), (tx - 32, 920), (tx + 32, 920)], fill=(4, 6, 10))
    img.paste(base, (0, 0))
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

_frost = {}
def frost_layer(fr):
    q = round(fr, 2)
    if q not in _frost:
        if "base" not in _frost:
            yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
            dx = np.minimum(xx, W - xx) / 420; dy = np.minimum(yy, H - yy) / 300
            e = np.clip(1 - np.minimum(dx, dy), 0, 1) ** 2
            rng = np.random.default_rng(3); n = Image.fromarray((rng.random((H // 8, W // 8)) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
            _frost["base"] = e * (0.6 + 0.4 * np.asarray(n, np.float32) / 255)
        a = (_frost["base"] * 110 * q).astype(np.uint8)
        im = Image.new("RGBA", (W, H), FROST + (0,)); im.putalpha(Image.fromarray(a))
        _frost[q] = im
    return _frost[q]

def sc_thermo(img, v, t, dur):
    """thermometer dropping from 'from' to 'to' °C with milestone tags; frost creeps in"""
    tf, tt = v["from"], v["to"]; lo, hi = -260, 40
    p = easeio((t - 0.4) / (dur * 0.7)); T = lerp(tf, tt, p)
    fr = min(1, (15 - T) / 260)
    if fr > 0:
        img.alpha_composite(frost_layer(fr))
    d = ImageDraw.Draw(img)
    x, y0, y1 = 620, 150, 760
    yv = lambda c: lerp(y1, y0, (c - lo) / (hi - lo))
    d.rounded_rectangle([x - 34, y0 - 30, x + 34, y1 + 10], 34, fill=(20, 28, 50), outline=(120, 140, 180), width=4)
    d.ellipse([x - 70, y1 - 30, x + 70, y1 + 110], fill=(20, 28, 50), outline=(120, 140, 180), width=4)
    col = mix(RED, ICE, min(1, (20 - T) / 120))
    d.ellipse([x - 54, y1 - 14, x + 54, y1 + 94], fill=col)
    d.rounded_rectangle([x - 18, yv(T), x + 18, y1 + 20], 18, fill=col)
    for c in range(-250, 41, 50):
        d.line([(x - 60, yv(c)), (x - 40, yv(c))], fill=(120, 140, 180), width=3)
        d.text((x - 75, yv(c)), f"{c}°", font=F(26, "Medium"), fill=DIM, anchor="rm")
    for i, (c, lab) in enumerate(v.get("marks", [])):
        a = ease((t - 0.6 - i * 0.9) / 0.5)
        if a <= 0: continue
        yy = yv(c)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.line([(x + 50, yy), (x + 140, yy)], fill=ICE + (int(255 * a),), width=3)
        d2.text((x + 160, yy), lab, font=F(40, "SemiBold"), fill=WHITE + (int(255 * a),), anchor="lm")
        img.alpha_composite(lay)
    alpha_text(img, (W - 300, 170), f"{T:+.0f} °C", F(96, "Black"), col, ease(t / 0.4))
    alpha_text(img, (W - 300, 245), v.get("label", "average surface"), F(30, "Medium"), DIM, ease(t / 0.4))
    caption(img, v.get("caption"), ease((t - 1.0) / 0.5))

def sc_energy(img, v, t, dur):
    """area comparison: sunlight vs Earth's own internal heat (squares with true area ratio)"""
    a = ease(t / 0.6)
    big = 600; ratio = v.get("ratio", 3690)
    small = big / math.sqrt(ratio)
    x0, y0 = 300, 140
    big = 560
    d = ImageDraw.Draw(img)
    d.rectangle([x0, y0, x0 + big, y0 + big], fill=mix(SPACE, (230, 165, 50), a))
    d.text((x0 + big / 2, y0 + big + 50), v.get("a_lab", "Sunlight hitting Earth"), font=F(38, "Bold"), fill=GOLD, anchor="mm")
    d.text((x0 + big / 2, y0 + big + 100), v.get("a_val", "≈ 173,000 TW"), font=F(34, "Medium"), fill=WHITE, anchor="mm")
    q = ease((t - 1.5) / 0.6)
    if q > 0:
        sx, sy = x0 + big - small - 6, y0 + big - small - 6
        d.rectangle([sx, sy, sx + small, sy + small], fill=RED)
        zx, zy, zs = 1200, 260, 380
        d.line([(sx + small, sy), (zx, zy)], fill=RED, width=2); d.line([(sx + small, sy + small), (zx, zy + zs)], fill=RED, width=2)
        d.rectangle([zx, zy, zx + zs, zy + zs], outline=RED, width=3)
        k = zs / (small * 6)
        d.rectangle([zx + zs / 2 - small * k / 2, zy + zs / 2 - small * k / 2, zx + zs / 2 + small * k / 2, zy + zs / 2 + small * k / 2], fill=RED)
        d.text((zx + zs / 2, zy + zs + 50), v.get("b_lab", "Earth's own inner heat"), font=F(38, "Bold"), fill=RED, anchor="mm")
        d.text((zx + zs / 2, zy + zs + 100), v.get("b_val", "≈ 47 TW (zoomed 6×)"), font=F(34, "Medium"), fill=WHITE, anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.2) / 0.5))

def sc_ocean(img, v, t, dur):
    """cross-section: frozen surface, thickening ice, dark liquid ocean, glowing hydrothermal vents"""
    top, sea_floor = 300, 900
    p = ease((t - 0.3) / (dur * 0.6)); ice_h = lerp(v.get("ice0", 10), v.get("ice1", 120), p)
    d = ImageDraw.Draw(img)
    g = np.linspace(0, 1, sea_floor - top)[:, None, None]
    water = (np.array([10, 40, 80], np.float32) * (1 - g) + np.array([2, 8, 20], np.float32) * g) * np.ones((1, W, 3), np.float32)
    img.paste(Image.fromarray(water.astype(np.uint8)).convert("RGBA"), (0, top))
    d = ImageDraw.Draw(img)
    rng = random.Random(9)
    d.rectangle([0, top, W, top + ice_h], fill=(200, 230, 250))
    for _ in range(40):
        x = rng.uniform(0, W); d.line([(x, top), (x + rng.uniform(-30, 30), top + ice_h * rng.uniform(0.3, 1))], fill=(160, 200, 230), width=2)
    pts = [(0, H)] + [(x, sea_floor + 30 * math.sin(x / 150) + rng.uniform(-6, 6)) for x in range(0, W + 30, 30)] + [(W, H)]
    d.polygon(pts, fill=(28, 22, 20))
    if v.get("vents", True):
        for vx in (560, 1380):
            vy = sea_floor - 10
            d.polygon([(vx - 40, vy + 40), (vx - 12, vy - 70), (vx + 12, vy - 70), (vx + 40, vy + 40)], fill=(45, 35, 30))
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            for k in range(12):
                ph = ((t * 0.6 + k / 12) % 1.0)
                yy = vy - 80 - ph * 300; rr = 14 + ph * 40
                d2.ellipse([vx - rr + 10 * math.sin(ph * 6 + k), yy - rr, vx + rr + 10 * math.sin(ph * 6 + k), yy + rr], fill=(255, 140, 60, int(110 * (1 - ph))))
            img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(6)))
            d = ImageDraw.Draw(img)
            for j in range(6):
                bx = vx + 60 + j * 14; by = vy + 10 - (j % 3) * 10
                d.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill=(240, 220, 200))
    d.text((80, top - 40), "frozen surface — air at " + v.get("air", "−70 °C"), font=F(34, "SemiBold"), fill=WHITE, anchor="lm")
    d.text((W - 80, top + ice_h + 50), f"ice: {v.get('ice_lab', 'thickening')}", font=F(32, "SemiBold"), fill=FROST, anchor="rm")
    d.text((W / 2, (top + sea_floor) / 2 + 40), v.get("water", "liquid water, kept warm from below"), font=F(40, "SemiBold"), fill=CYAN, anchor="mm")
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

_gal = None
def galaxy_sprite():
    global _gal
    if _gal is None:
        S = 900; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im); rng = random.Random(21)
        for i in range(9000):
            arm = i % 2; r = rng.random() ** 0.7 * 420
            th = r / 70 + arm * math.pi + rng.gauss(0, 0.35)
            x, y = S / 2 + r * math.cos(th), S / 2 + r * math.sin(th) * 0.55
            c = mix((255, 220, 170), (150, 180, 255), r / 420)
            al = int(200 * (1 - r / 460))
            d.ellipse([x - 1.2, y - 1.2, x + 1.2, y + 1.2], fill=c + (max(30, al),))
        core = radial(260, [(0, (255, 235, 200, 230)), (0.4, (255, 210, 150, 90)), (1, (255, 200, 140, 0))])
        im.alpha_composite(core, (S // 2 - 130, S // 2 - 130))
        _gal = im.filter(ImageFilter.GaussianBlur(0.6))
    return _gal

def sc_galaxy(img, v, t, dur):
    a = ease(t / 0.8)
    paste_c(img, galaxy_sprite(), W / 2, H / 2 - 40, a)
    d = ImageDraw.Draw(img)
    ang = 0.9 + t * 0.03; r = 250
    ex, ey = W / 2 + r * math.cos(ang), H / 2 - 40 + r * math.sin(ang) * 0.55
    pulse = 0.5 + 0.5 * math.sin(t * 3)
    d.ellipse([ex - 10 - 8 * pulse, ey - 10 - 8 * pulse, ex + 10 + 8 * pulse, ey + 10 + 8 * pulse], outline=CYAN, width=3)
    d.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=CYAN)
    d.line([(ex + 14, ey - 14), (ex + 120, ey - 120)], fill=CYAN, width=2)
    d.text((ex + 130, ey - 130), v.get("label", "Earth — a rogue planet"), font=F(34, "Bold"), fill=WHITE, anchor="lm")
    if v.get("rogues"):
        rng = random.Random(4)
        for i in range(60):
            rx, ry = rng.uniform(300, W - 300), rng.uniform(150, H - 250)
            rx += math.sin(t * 0.3 + i) * 12
            q = ease((t - 1 - i * 0.03) / 0.4)
            if q > 0: d.ellipse([rx - 3, ry - 3, rx + 3, ry + 3], fill=mix(SPACE, (120, 140, 190), q))
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

def sc_planetsdark(img, v, t, dur):
    """the planets keep going on their own straight lines, all dark"""
    cx, cy = W / 2, H / 2 - 20; d = ImageDraw.Draw(img)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], outline=(130, 140, 170), width=2)
    p = easeio(t / (dur * 0.9))
    orb = [("Mercury", 0.39, 1.6), ("Venus", 0.72, 1.18), ("Earth", 1.0, 1.0), ("Mars", 1.52, 0.81), ("Jupiter", 5.2, 0.44)]
    sc = 120
    for i, (n, au, spd) in enumerate(orb):
        R = min(au, 3.4) * sc if n != "Jupiter" else 430
        ang0 = 0.7 + i * 1.3
        for k in range(0, 360, 8):
            d.arc([cx - R, cy - R, cx + R, cy + R], k, k + 3, fill=(50, 65, 100), width=1)
        sx, sy = cx + R * math.cos(ang0), cy + R * math.sin(ang0)
        tx, ty = -math.sin(ang0), math.cos(ang0)
        L = p * spd * 300
        ex, ey = sx + tx * L, sy + ty * L
        d.line([(sx, sy), (ex, ey)], fill=(80, 100, 150), width=2)
        paste_c(img, planet_sprite(PRAD[n] * 0.8, tuple(int(c * 0.6) for c in PCOL[n]), light=(0, 0)), ex, ey)
        d = ImageDraw.Draw(img); d.text((ex, ey - PRAD[n] - 24), n, font=F(32, "SemiBold"), fill=WHITE, anchor="mm")
    caption(img, v.get("caption"), ease((t - 0.8) / 0.5))

# ---------------- scenes (EP03: violet / magenta, zoom-out ladder) ----------------
VIO, MAG = (186, 140, 255), (255, 120, 200)
LADDER = ["Moon", "Sun", "Neptune", "Voyager 1", "Proxima", "Milky Way", "Andromeda", "Laniakea", "Edge"]

def _cloud(seed, n, rx, ry, cx, cy, col, rmin=1.0, rmax=2.4, clump=0):
    """procedural point cloud (filaments when clump>0) -> list of (x, y, r, col)"""
    rng = random.Random(seed); pts = []
    nodes = [(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(max(1, clump))]
    for i in range(n):
        if clump:
            a, b = nodes[rng.randrange(len(nodes))], nodes[rng.randrange(len(nodes))]
            k = rng.random(); x, y = lerp(a[0], b[0], k) + rng.gauss(0, 0.05), lerp(a[1], b[1], k) + rng.gauss(0, 0.05)
        else:
            x, y = rng.gauss(0, 0.45), rng.gauss(0, 0.45)
        if x * x + y * y > 1: continue
        pts.append((cx + x * rx, cy + y * ry, rng.uniform(rmin, rmax), mix(col, WHITE, rng.random() * 0.5)))
    return pts

_web = {}
def web_layer(kind):
    if kind not in _web:
        S = 760; im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        if kind == "super":
            for x, y, r, c in _cloud(7, 2600, 360, 360, S / 2, S / 2, VIO, 0.8, 2.2, clump=14): d.ellipse([x - r, y - r, x + r, y + r], fill=c + (210,))
        else:  # universe: cosmic web inside a glowing sphere
            for x, y, r, c in _cloud(9, 5200, 370, 370, S / 2, S / 2, MAG, 0.6, 1.6, clump=40): d.ellipse([x - r, y - r, x + r, y + r], fill=c + (170,))
            g = radial(S, [(0, (0, 0, 0, 0)), (0.9, (0, 0, 0, 0)), (0.97, MAG + (150,)), (1.0, MAG + (0,))]); im.alpha_composite(g)
        _web[kind] = im.filter(ImageFilter.GaussianBlur(0.5))
    return _web[kind]

def zoom_object(img, kind, cx, cy, a, t):
    d = ImageDraw.Draw(img)
    if kind == "moon":
        paste_c(img, earth_sprite(120, light=(-1, -0.2)), cx - 330, cy, a)
        d.line([(cx - 190, cy), (cx + 290, cy)], fill=mix(SPACE, (110, 120, 160), a), width=2)
        paste_c(img, planet_sprite(33, (175, 175, 170), light=(-1, -0.2)), cx + 330, cy, a)
        alpha_text(img, (cx + 330, cy + 80), "Moon", F(32, "SemiBold"), WHITE, a)
    elif kind == "sun":
        paste_c(img, sun_sprite(70), cx, cy, a); R = 330
        for k in range(0, 360, 5): d.arc([cx - R, cy - R, cx + R, cy + R], k, k + 2.5, fill=mix(SPACE, (90, 110, 160), a), width=2)
        ang = -0.6 + t * 0.03; paste_c(img, earth_sprite(16, light=(-math.cos(ang), -math.sin(ang))), cx + R * math.cos(ang), cy + R * math.sin(ang), a)
    elif kind in ("solar", "voyager"):
        paste_c(img, sun_sprite(18 if kind == "solar" else 8), cx, cy, a)
        sc = 11.5 if kind == "solar" else 2.0
        for i, (n, au) in enumerate([("Mercury", .39), ("Venus", .72), ("Earth", 1), ("Mars", 1.52), ("Jupiter", 5.2), ("Saturn", 9.54), ("Uranus", 19.2), ("Neptune", 30.07)]):
            R = au * sc
            if R < 4: continue
            d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=mix(SPACE, (70, 90, 140) if n != "Neptune" else VIO, a), width=2 if n == "Neptune" else 1)
            if kind == "solar" and au > 4:
                ang = 0.4 + i * 1.1 + t * 0.02 / au
                paste_c(img, planet_sprite(max(5, PRAD[n] // 3), PCOL[n], light=(-math.cos(ang), -math.sin(ang))), cx + R * math.cos(ang), cy + R * math.sin(ang), a)
        if kind == "solar": alpha_text(img, (cx + 30.07 * sc * 0.72 + 20, cy - 30.07 * sc * 0.72 - 10), "Neptune's orbit", F(30, "SemiBold"), VIO, a, anchor="lm")
        else:
            vx = cx + 169 * sc * 0.94; vy = cy - 169 * sc * 0.34
            d.line([(cx, cy), (vx, vy)], fill=mix(SPACE, MAG, a * 0.8), width=2)
            d.ellipse([vx - 7, vy - 7, vx + 7, vy + 7], fill=mix(SPACE, MAG, a))
            alpha_text(img, (vx, vy - 40), "Voyager 1 — 1 light-day", F(32, "Bold"), MAG, a)
            alpha_text(img, (cx, cy + 90), "planets", F(26, "Medium"), DIM, a)
    elif kind == "stars":
        paste_c(img, sun_sprite(10), cx - 170, cy + 60, a)
        alpha_text(img, (cx - 170, cy + 110), "Sun", F(30, "SemiBold"), WHITE, a)
        rng = random.Random(13)
        for i in range(22):
            x, y = cx + rng.uniform(-620, 620), cy + rng.uniform(-330, 330); r = rng.uniform(2, 5)
            d.ellipse([x - r, y - r, x + r, y + r], fill=mix(SPACE, mix((255, 200, 160), (170, 190, 255), rng.random()), a))
        px, py = cx + 260, cy - 120
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=mix(SPACE, (255, 120, 90), a))
        d.line([(cx - 160, cy + 55), (px - 8, py + 5)], fill=mix(SPACE, VIO, a), width=2)
        alpha_text(img, (px + 20, py - 34), "Proxima Centauri", F(34, "Bold"), (255, 160, 130), a, anchor="lm")
    elif kind == "galaxy":
        paste_c(img, galaxy_sprite(), cx, cy, a)
        ex, ey = cx + 250 * math.cos(0.9), cy + 250 * math.sin(0.9) * 0.55
        d = ImageDraw.Draw(img); d.ellipse([ex - 8, ey - 8, ex + 8, ey + 8], outline=mix(SPACE, MAG, a), width=3)
        alpha_text(img, (ex + 24, ey + 30), "you are here", F(30, "Bold"), MAG, a, anchor="lm")
    elif kind == "local":
        g = galaxy_sprite().resize((300, 300), Image.BILINEAR); paste_c(img, g, cx - 380, cy + 40, a)
        g2 = galaxy_sprite().resize((380, 380), Image.BILINEAR).rotate(35, resample=Image.BILINEAR); paste_c(img, g2, cx + 380, cy - 60, a)
        d = ImageDraw.Draw(img)
        for x in range(int(cx - 210), int(cx + 170), 22): d.line([(x, cy + 30 - (x - cx + 210) * 0.24), (x + 10, cy + 30 - (x + 10 - cx + 210) * 0.24)], fill=mix(SPACE, VIO, a), width=2)
        alpha_text(img, (cx - 380, cy + 160), "Milky Way", F(32, "Bold"), WHITE, a)
        alpha_text(img, (cx + 380, cy + 110), "Andromeda", F(32, "Bold"), WHITE, a)
    elif kind in ("super", "universe"):
        paste_c(img, web_layer(kind), cx, cy, a)
        if kind == "super":
            d = ImageDraw.Draw(img); d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=mix(SPACE, MAG, a))
            alpha_text(img, (cx + 14, cy - 26), "Milky Way", F(26, "Bold"), MAG, a, anchor="lm")
        else:
            alpha_text(img, (cx, cy), "you", F(28, "Black"), WHITE, a)

def sc_zoom(img, v, t, dur):
    """zoom-out ladder: previous scale shrinks to a dot, the new scale fades in; vertical ladder + light-time odometer"""
    cx, cy = 1040, 520; a = ease((t - 0.25) / 0.8)
    zoom_object(img, v["kind"], cx, cy, a, t)
    if v.get("prev"):
        q = ease(t / 1.2); rr = lerp(330, 3, q)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=WHITE + (int(220 * (1 - q * 0.6)),), width=3)
        img.alpha_composite(lay)
        if q < 0.9: alpha_text(img, (cx, cy - rr - 30), v["prev"], F(30, "SemiBold"), WHITE, 1 - q)
    # ladder (left)
    d = ImageDraw.Draw(img); x, y0, step = 120, 190, 82; rung = v["rung"]
    d.line([(x, y0), (x, y0 + step * (len(LADDER) - 1))], fill=(60, 60, 100), width=3)
    d.line([(x, y0 + step * (len(LADDER) - 1)), (x, y0 + step * (len(LADDER) - 1 - rung - ease(t / 0.8) + 1))], fill=VIO, width=5)
    for i, name in enumerate(LADDER):
        yy = y0 + step * (len(LADDER) - 1 - i); on = i <= rung; cur = i == rung
        r = 13 if cur else 8
        d.ellipse([x - r, yy - r, x + r, yy + r], fill=MAG if cur else (VIO if on else (60, 60, 100)))
        d.text((x + 30, yy), name, font=F(30 if cur else 26, "Bold" if cur else "Medium"), fill=WHITE if cur else (DIM if on else (80, 85, 115)), anchor="lm")
    # odometer card (bottom)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    bx0, by0, bx1, by1 = 560, 840, 1520, 1010
    d2.rounded_rectangle([bx0, by0, bx1, by1], 26, fill=(14, 8, 30, 225), outline=VIO + (200,), width=3)
    img.alpha_composite(lay)
    k = ease((t - 0.3) / 0.6)
    alpha_text(img, (bx0 + 40, by0 + 42), v["name"].upper(), F(30, "Bold"), VIO, k, anchor="lm", shadow=False)
    alpha_text(img, (bx1 - 40, by0 + 42), v["dist"], F(30, "SemiBold"), MAG, k, anchor="rm", shadow=False)
    fl = F(76, "Black"); alpha_text(img, (bx0 + 40, by0 + 112), v["lt"], fl, WHITE, k, anchor="lm", shadow=False)
    lab = v.get("ltlab", "LIGHT TRAVEL TIME")
    if fl.getlength(v["lt"]) + F(24, "SemiBold").getlength(lab) < (bx1 - bx0) - 120:
        alpha_text(img, (bx1 - 40, by0 + 118), lab, F(24, "SemiBold"), DIM, k, anchor="rm", shadow=False)

def sc_stretch(img, v, t, dur):
    """expanding lattice of galaxies; a photon crawls from the source to us while space stretches under it"""
    p = easeio((t - 0.3) / (dur * 0.8)); a0 = v.get("a0", 0.1)
    vis_scale = lerp(0.22, 1.0, p)  # visual scale factor (compressed so it stays readable)
    ux, uy = 1560, 520; src_c = -1.0  # comoving units: us at 0, source at -1 (screen width ~1300 px at scale 1)
    S = 1320
    d = ImageDraw.Draw(img)
    for i in range(-7, 3):
        for j in range(-3, 4):
            x, y = ux + i * 0.18 * S * vis_scale, uy + j * 0.18 * S * vis_scale
            if -40 < x < W + 40 and 60 < y < 900:
                rr = 3 + 2 * vis_scale
                d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=mix((60, 50, 100), VIO, 0.6))
    for j in range(-3, 4):
        y = uy + j * 0.18 * S * vis_scale
        if 60 < y < 900: d.line([(0, y), (W, y)], fill=(40, 34, 70), width=1)
    sx = ux + src_c * S * vis_scale
    # photon path: wavy line from source to photon position, wavelength stretches with scale
    ph = p; px = lerp(sx, ux, ph)
    pts = []; lam = 18 + 60 * vis_scale
    for k in range(0, int(max(1, px - sx)), 4):
        xx = sx + k; pts.append((xx, uy + 14 * math.sin((xx - sx) / lam * 2 * math.pi)))
    col = mix((130, 170, 255), (255, 90, 80), p)
    if len(pts) > 1: d.line(pts, fill=col, width=4)
    d.ellipse([px - 10, uy - 10, px + 10, uy + 10], fill=col)
    if v.get("cmb"):
        g = radial(140, [(0, (255, 200, 150, 200)), (1, (255, 160, 100, 0))]); paste_c(img, g, sx, uy, 1 - 0.6 * p)
    else:
        g = galaxy_sprite().resize((110, 110), Image.BILINEAR); paste_c(img, g, sx, uy)
    d = ImageDraw.Draw(img)
    d.text((sx, uy + 80), v.get("src", "source"), font=F(30, "Bold"), fill=WHITE, anchor="mm")
    paste_c(img, galaxy_sprite().resize((90, 90), Image.BILINEAR), ux, uy)
    d.text((ux, uy + 72), "us", font=F(30, "Bold"), fill=MAG, anchor="mm")
    # counters
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.rounded_rectangle([120, 120, 760, 330], 24, fill=(14, 8, 30, 220), outline=VIO + (190,), width=3)
    img.alpha_composite(lay)
    alpha_text(img, (150, 165), "LIGHT HAS TRAVELED", F(26, "SemiBold"), DIM, 1, anchor="lm", shadow=False)
    alpha_text(img, (150, 225), f"{v['light'] * p:.1f} billion years", F(54, "Black"), WHITE, 1, anchor="lm", shadow=False)
    now = lerp(v["now"] * a0 * 1.0, v["now"], p)
    alpha_text(img, (150, 290), f"source is now {now:.1f} billion ly away", F(32, "SemiBold"), MAG, 1, anchor="lm", shadow=False)
    caption(img, v.get("caption"), ease((t - 1.0) / 0.5), col=None)

def sc_horizons(img, v, t, dur):
    """nested borders around us: faster-than-light sphere (14), event horizon (16.5), observable (46 bn ly radius)"""
    cx, cy = 760, 520; k = 9.6  # px per billion ly
    show = v.get("show", 3); fade = v.get("fade", False)
    rng = random.Random(17); d = ImageDraw.Draw(img)
    for i in range(420):
        ang = rng.uniform(0, 6.283); r0 = 46 * k * math.sqrt(rng.random())
        r = r0 * (1 + 0.04 * t / max(1, dur))
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        unreachable = r0 > 16.6 * k and show >= 3
        b = 1.0
        if fade and r0 > 3 * k: b = max(0.0, 1 - ease((t - 1.0 - (r0 / (46 * k)) * dur * 0.3) / 1.2))
        if b <= 0: continue
        c = (110, 110, 140) if unreachable else VIO
        d.ellipse([x - 2.2, y - 2.2, x + 2.2, y + 2.2], fill=mix(SPACE, c, b))
    rings = [(46, MAG, "observable universe — 46 bn ly radius", 3), (14.4, (255, 194, 75), "faster than light — beyond ~14 bn ly", 1), (16.6, CYAN, "event horizon — 16.5 bn ly: never reachable", 2)]
    lab_y = {3: 260, 1: 520, 2: 700}
    for R, col, lab, need in rings:
        if show < need and not (need == 3 and show >= 3): continue
        if need > show: continue
        a = ease((t - 0.3) / 0.6) if need == show else 1.0
        rr = R * k
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=col + (int(255 * a),), width=4)
        ly = lab_y[need]; lx = 1290
        ex = cx + rr * 0.97; ey = cy - rr * 0.25 if need == 3 else cy - rr * 0.6 if need == 1 else cy + rr * 0.7
        d2.line([(ex, ey), (lx - 20, ly)], fill=col + (int(200 * a),), width=2)
        img.alpha_composite(lay)
        words = lab.split(" — ") if " — " in lab else [lab]
        alpha_text(img, (lx, ly - 20), words[0], F(34, "Bold"), col, a, anchor="lm")
        if len(words) > 1: alpha_text(img, (lx, ly + 24), words[1], F(28, "SemiBold"), WHITE, a, anchor="lm")
    d = ImageDraw.Draw(img); d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=WHITE)
    d.text((cx, cy + 26), "us", font=F(26, "Bold"), fill=WHITE, anchor="mm")
    caption(img, v.get("caption"), ease((t - 1.0) / 0.5))

_deep = None
def deep_sprite():
    global _deep
    if _deep is None:
        S = (2400, 1350); im = Image.new("RGBA", S, (0, 0, 0, 0)); d = ImageDraw.Draw(im); rng = random.Random(31)
        for i in range(1500):
            x, y = rng.uniform(0, S[0]), rng.uniform(0, S[1]); sz = rng.random() ** 3 * 26 + 2
            col = mix((255, 210, 160), (150, 170, 255), rng.random()); col = mix(col, (255, 120, 90), rng.random() ** 4)
            if sz > 12 and rng.random() < 0.6:
                sp = Image.new("RGBA", (int(sz * 4), int(sz * 4)), (0, 0, 0, 0)); ds = ImageDraw.Draw(sp)
                for k in range(160):
                    r = (k / 160) * sz * 1.6; th = r / sz * 3.2 + (k % 2) * math.pi
                    ds.ellipse([sz * 2 + r * math.cos(th) - 1.2, sz * 2 + r * math.sin(th) * 0.6 - 1.2, sz * 2 + r * math.cos(th) + 1.2, sz * 2 + r * math.sin(th) * 0.6 + 1.2], fill=col + (180,))
                ds.ellipse([sz * 2 - sz * 0.3, sz * 2 - sz * 0.2, sz * 2 + sz * 0.3, sz * 2 + sz * 0.2], fill=(255, 235, 210, 230))
                sp = sp.rotate(rng.uniform(0, 180), resample=Image.BILINEAR); im.alpha_composite(sp, (int(x), int(y)))
            else:
                e = rng.uniform(0.4, 1.0)
                d.ellipse([x - sz / 2, y - sz * e / 2, x + sz / 2, y + sz * e / 2], fill=col + (int(120 + 100 * rng.random()),))
        _deep = im.filter(ImageFilter.GaussianBlur(0.8))
    return _deep

def sc_deepfield(img, v, t, dur):
    """procedural deep field (no real imagery), slow zoom, galaxy counter"""
    p = t / max(1, dur); z = lerp(1.0, 1.25, p)
    ds = deep_sprite(); cw, ch = 2400 / z * 0.8, 1350 / z * 0.8
    ox, oy = (2400 - cw) / 2, (1350 - ch) / 2
    crop = ds.crop((int(ox), int(oy), int(ox + cw), int(oy + ch))).resize((W, H), Image.BILINEAR)
    img.alpha_composite(crop)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.rounded_rectangle([W / 2 - 520, 130, W / 2 + 520, 330], 28, fill=(10, 6, 24, 215), outline=MAG + (200,), width=3)
    img.alpha_composite(lay)
    alpha_text(img, (W / 2, 180), "GALAXIES IN THE OBSERVABLE UNIVERSE", F(30, "Bold"), VIO, 1, shadow=False)
    cnt = int(200e9 * easeio((t - 0.4) / (dur * 0.6)))
    alpha_text(img, (W / 2, 265), f"{cnt:,}+" if cnt < 200e9 else v.get("count", "200,000,000,000+"), F(78, "Black"), WHITE, 1, shadow=False)
    caption(img, v.get("caption"), ease((t - dur * 0.55) / 0.5))

def sc_shrink(img, v, t, dur):
    """shrink the observable universe to the size of Earth"""
    cx, cy = 470, 540; a = ease(t / 0.6)
    paste_c(img, earth_sprite(270, glow=MAG), cx, cy, a)
    alpha_text(img, (cx, cy + 340), "observable universe = Earth", F(36, "Bold"), MAG, a)
    alpha_text(img, (cx, cy + 385), "93 billion ly → 12,742 km", F(28, "SemiBold"), DIM, a)
    rows = [("Milky Way", "≈ 14 m", "a city bus"), ("Andromeda", "≈ 340 m away", "a few blocks"), ("Proxima Centauri", "≈ 0.6 mm from the Sun", "a grain of sand"), ("The Sun", "≈ 0.02 nm wide", "smaller than an atom")]
    n = v.get("rows", 4)
    if n == 0:
        alpha_text(img, (1340, 470), "Squeeze it all", F(72, "Black"), WHITE, ease((t - 0.4) / 0.6))
        alpha_text(img, (1340, 560), "down to one planet", F(56, "ExtraBold"), VIO, ease((t - 0.8) / 0.6))
        return
    span = dur * 0.8 / n
    for i, (nm, val, like) in enumerate(rows[:n]):
        q = ease((t - 0.4 - i * span) / 0.5)
        if q <= 0: continue
        y = 210 + i * 190
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.rounded_rectangle([900, y - 70, 1800, y + 80], 22, fill=(14, 8, 30, int(215 * q)), outline=VIO + (int(170 * q),), width=2)
        img.alpha_composite(lay)
        alpha_text(img, (940, y - 28), nm, F(36, "Bold"), VIO, q, anchor="lm", shadow=False)
        alpha_text(img, (940, y + 30), val, F(48, "Black"), WHITE, q, anchor="lm", shadow=False)
        alpha_text(img, (1770, y + 30), like, F(32, "SemiBold"), MAG, q, anchor="rm", shadow=False)
        if i == 0:  # tiny bus icon
            d = ImageDraw.Draw(img); bx, by = 1560, y - 40
            d.rounded_rectangle([bx, by, bx + 150, by + 44], 8, fill=mix(SPACE, (255, 194, 75), q))
            for w in range(5): d.rectangle([bx + 10 + w * 27, by + 8, bx + 30 + w * 27, by + 22], fill=mix(SPACE, (40, 50, 80), q))
            d.ellipse([bx + 20, by + 36, bx + 40, by + 56], fill=mix(SPACE, (30, 30, 40), q)); d.ellipse([bx + 110, by + 36, bx + 130, by + 56], fill=mix(SPACE, (30, 30, 40), q))

# ---------------- scenes (EP04: black holes — ember orange / pale cyan) ----------------
EMBER, HOT, PALE = (255, 138, 61), (255, 214, 150), (159, 232, 255)
_bh = {}
def bh_static(rh):
    """black hole sprite: lensed back of the disk (halo), shadow, photon ring; front disk drawn separately"""
    rh = int(rh)
    if rh in _bh: return _bh[rh]
    S = int(rh * 7); c = S / 2
    yy, xx = np.mgrid[0:S, 0:S].astype(np.float32); dx, dy = (xx - c) / rh, (yy - c) / rh
    d = np.sqrt(dx * dx + dy * dy)
    out = np.zeros((S, S, 4), np.float32)
    # lensed halo: ring 1.55..2.6 rh, brighter on top and left (beaming)
    halo = np.clip(1 - np.abs(d - 1.9) / 0.65, 0, 1) ** 1.6 * (0.55 + 0.45 * np.clip(-dy / np.maximum(d, 1e-3), -1, 1) * 0.5 + 0.25 * np.clip(-dx / np.maximum(d, 1e-3), -1, 1))
    halo = np.clip(halo, 0, 1)
    col = np.array(EMBER, np.float32) * (1 - halo[..., None] * 0.5) + np.array(HOT, np.float32) * halo[..., None] * 0.5
    out[..., :3] = col; out[..., 3] = halo * 235
    # glow
    gl = np.clip(1 - (d - 1.3) / 2.2, 0, 1) ** 2 * 0.35
    out[..., 3] = np.maximum(out[..., 3], gl * 255 * (d > 1.3))
    # photon ring
    pr = np.clip(1 - np.abs(d - 1.5) / 0.05, 0, 1)
    out[..., :3] = out[..., :3] * (1 - pr[..., None]) + np.array((255, 245, 225), np.float32) * pr[..., None]
    out[..., 3] = np.maximum(out[..., 3], pr * 255)
    # shadow
    sh = d < 1.42
    out[sh] = (2, 2, 4, 255)
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")
    _bh[rh] = img; return img

def bh_front_disk(img, cx, cy, rh, t, a=1.0):
    """front half of the accretion disk (flattened ellipse in front of the shadow) + faint orbiting streaks"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(40):
        f = k / 39; rx = rh * (1.6 + 2.6 * f); ry = rx * 0.16
        c = mix(HOT, EMBER, f ** 0.7) + (int(235 * (1 - f) ** 1.1 * a),)
        d.arc([cx - rx, cy - ry, cx + rx, cy + ry], 0, 180, fill=c, width=max(2, int(rh * 0.07)))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.0)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    rng = random.Random(4)
    for i in range(140):
        rr = rh * rng.uniform(1.7, 4.0); ph0 = rng.uniform(0, 6.283); w = 1.6 * (2.0 / (rr / rh)) ** 1.5
        for j in range(5):
            ph = ph0 + t * w - j * 0.025
            if math.sin(ph) < 0.05: continue
            x, y = cx + rr * math.cos(ph), cy + rr * 0.16 * math.sin(ph)
            beam = 0.35 + 0.65 * (0.5 - 0.5 * math.cos(ph))
            s_ = rh * 0.012 + 0.8
            d.ellipse([x - s_ * 2, y - s_, x + s_ * 2, y + s_], fill=(255, 236, 200, int(130 * beam * a * (1 - j / 5))))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.0)))

def draw_bh(img, cx, cy, rh, t, a=1.0):
    paste_c(img, bh_static(rh), cx, cy, a)
    bh_front_disk(img, cx, cy, rh, t, a)

_astro = {}
def astro_base():
    if "b" in _astro: return _astro["b"]
    s = Image.new("RGBA", (80, 200), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    suit, vis = (235, 238, 245, 255), (60, 120, 200, 255)
    d.rounded_rectangle([22, 58, 58, 128], 12, fill=suit)          # torso
    d.rounded_rectangle([8, 64, 22, 116], 7, fill=suit); d.rounded_rectangle([58, 64, 72, 116], 7, fill=suit)  # arms
    d.rounded_rectangle([24, 124, 38, 190], 7, fill=suit); d.rounded_rectangle([42, 124, 56, 190], 7, fill=suit)  # legs
    d.ellipse([18, 8, 62, 56], fill=suit); d.ellipse([26, 18, 56, 44], fill=vis)  # helmet + visor
    d.rectangle([30, 74, 50, 88], fill=(255, 138, 61, 255))
    _astro["b"] = s; return s

def draw_astro(img, x, y, scale=1.0, sx=1.0, sy=1.0, rot=0, tint=None, a=1.0):
    s = astro_base()
    if tint is not None:
        arr = np.asarray(s, np.float32).copy(); arr[..., :3] = arr[..., :3] * 0.25 + np.array(tint, np.float32) * 0.75
        s = Image.fromarray(arr.astype(np.uint8), "RGBA")
    s = s.resize((max(2, int(80 * scale * sx)), max(2, int(200 * scale * sy))), Image.BILINEAR)
    if rot: s = s.rotate(rot, expand=True, resample=Image.BILINEAR)
    paste_c(img, s, x, y, a)

def sc_blackhole(img, v, t, dur):
    """drawn black hole (lensed disk, photon ring, shadow) + optional labels / falling astronaut / headline"""
    cx, cy = v.get("x", W / 2), v.get("y", H / 2 - 20); rh = v.get("r", 120)
    zoom = 1 + v.get("zoom", 0.06) * t / max(1, dur)
    draw_bh(img, cx, cy, int(rh * zoom), t, ease(t / 0.8))
    if v.get("faller"):
        p = (t / dur); ang = -0.6 + p * 7.5; rr = rh * zoom * lerp(4.4, 1.45, ease(p * 1.1))
        draw_astro(img, cx + rr * math.cos(ang), cy + rr * 0.45 * math.sin(ang), 0.32 * (1 - 0.4 * p), rot=-math.degrees(ang) - 90, a=max(0, 1 - max(0, p - 0.85) / 0.15))
    for i, (lab, frac, side) in enumerate(v.get("labels", [])):
        q = ease((t - 1.0 - i * 2.5) / 0.6)
        if q <= 0: continue
        r = rh * zoom * frac; ex, ey = cx + r * 0.71 * side, cy - r * 0.71
        lx = cx + side * (rh * zoom * 2.6 + 40); ly = ey - 90 - i * 40
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.line([(ex, ey), (lx, ly)], fill=PALE + (int(220 * q),), width=3); d2.ellipse([ex - 7, ey - 7, ex + 7, ey + 7], fill=PALE + (int(255 * q),))
        img.alpha_composite(lay)
        alpha_text(img, (lx + side * 14, ly), lab[0], F(44, "ExtraBold"), PALE, q, anchor="lm" if side > 0 else "rm")
        if len(lab) > 1: alpha_text(img, (lx + side * 14, ly + 48), lab[1], F(30, "SemiBold"), WHITE, q, anchor="lm" if side > 0 else "rm")
    if v.get("head"):
        alpha_text(img, (W / 2, 150), v["head"], F(64, "Black"), WHITE, ease(t / 0.4))
    caption(img, v.get("caption"), ease((t - 1.2) / 0.5))

G_, C_, MSUN, GE = 6.674e-11, 2.998e8, 1.989e30, 9.81
def tidal_g(msun, r_km, L=2.0): return 2 * G_ * msun * MSUN * L / (r_km * 1e3) ** 3 / GE
def fmt_g(g):
    if g >= 1e6: return f"{g / 1e6:,.0f} million g"
    if g >= 100: return f"{g:,.0f} g"
    if g >= 1: return f"{g:,.1f} g"
    if g >= 0.01: return f"{g:.2f} g"
    return f"1/{1 / g:,.0f} g"

def sc_spaghetti(img, v, t, dur):
    """feet-first fall toward a black hole: distance odometer (log) + tidal stretch on a 2 m body, body stretches with it"""
    M = v["msun"]; r0, r1 = v["r_from"], v["r_to"]; big = v.get("big", False)
    p = easeio((t - 0.6) / max(1, dur * 0.8))
    r = math.exp(lerp(math.log(r0), math.log(r1), p)); g = tidal_g(M, r)
    # black hole on the right: small = whole hole; big = huge curved edge
    if big:
        R0 = 2600; bx = W + R0 - 360
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        for k in range(18): d2.ellipse([bx - R0 - 40 - k * 6, H / 2 - R0 - 40 - k * 6, bx + R0 + 40 + k * 6, H / 2 + R0 + 40 + k * 6], outline=EMBER + (int(60 * (1 - k / 18)),), width=6)
        d2.ellipse([bx - R0, H / 2 - R0, bx + R0, H / 2 + R0], fill=(2, 2, 4, 255), outline=(255, 245, 225, 255), width=4)
        img.alpha_composite(lay); edge = bx - R0
    else:
        draw_bh(img, 1600, H / 2, 80, t); edge = 1600 - 80 * 1.42 - 140
    # astronaut position (log distance), feet toward the hole
    x = lerp(560, edge - 90, (math.log(r0) - math.log(r)) / (math.log(r0) - math.log(max(r1, 1))))
    st = 1 + min(5.5, max(0, math.log10(max(g, 1e-9)) + 0.0) * 0.9) if g > 1 else 1.0
    draw_astro(img, x, H / 2, 0.9, sx=1 / math.sqrt(st), sy=st, rot=90)
    # left panel odometer
    d = ImageDraw.Draw(img)
    alpha_text(img, (90, 190), v["title"], F(54, "ExtraBold"), EMBER, ease(t / 0.4), anchor="lm")
    alpha_text(img, (90, 245), v.get("sub", ""), F(32, "SemiBold"), DIM, ease(t / 0.4), anchor="lm")
    alpha_text(img, (90, 760), "distance to center", F(30, "SemiBold"), DIM, 1, anchor="lm")
    alpha_text(img, (90, 815), f"{r:,.0f} km", F(64, "Black"), WHITE, 1, anchor="lm")
    alpha_text(img, (90, 890), "stretch on a 2 m body", F(30, "SemiBold"), DIM, 1, anchor="lm")
    gc = mix(PALE, (255, 80, 60), min(1, max(0, math.log10(max(g, 1e-9)) / 6)))
    alpha_text(img, (90, 950), fmt_g(g), F(72, "Black"), gc, 1, anchor="lm")
    if v.get("verdict") and p > 0.98: caption(img, v["verdict"], ease((t - 0.6 - dur * 0.8) / 0.5))

def sc_twoclocks(img, v, t, dur):
    """split view: your own watch ticks normally; your friend sees you slow, redden and freeze at the horizon"""
    a = ease(t / 0.5); d = ImageDraw.Draw(img)
    d.line([(W / 2, 140), (W / 2, H - 200)], fill=(60, 70, 100), width=2)
    alpha_text(img, (W / 4, 150), "YOUR WATCH", F(48, "Black"), PALE, a)
    alpha_text(img, (3 * W / 4, 150), "WHAT YOUR FRIEND SEES", F(48, "Black"), EMBER, a)
    tau = t  # proper time, seconds
    # left: analog watch
    cx, cy, R = W / 4, 520, 210
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=PALE, width=6)
    for k in range(60):
        ang = k / 60 * 2 * math.pi; l = 26 if k % 5 == 0 else 10
        d.line([(cx + (R - 12) * math.sin(ang), cy - (R - 12) * math.cos(ang)), (cx + (R - 12 - l) * math.sin(ang), cy - (R - 12 - l) * math.cos(ang))], fill=WHITE, width=3 if k % 5 == 0 else 1)
    ang = tau / 60 * 2 * math.pi
    d.line([(cx, cy), (cx + (R - 40) * math.sin(ang), cy - (R - 40) * math.cos(ang))], fill=EMBER, width=6)
    d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=EMBER)
    alpha_text(img, (cx, cy + R + 70), f"00:{int(tau):02d}", F(64, "Black"), WHITE, a)
    alpha_text(img, (cx, cy + R + 125), "ticks normally — you cross the horizon", F(30, "SemiBold"), DIM, a)
    # right: hole edge + astronaut approaching asymptotically, redshifting & fading
    ex = W - 80
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.rectangle([ex, 200, W, H - 220], fill=(2, 2, 4, 255)); d2.line([(ex, 200), (ex, H - 220)], fill=(255, 245, 225, 255), width=3)
    for k in range(10): d2.line([(ex - 6 - k * 5, 200), (ex - 6 - k * 5, H - 220)], fill=EMBER + (int(40 * (1 - k / 10)),), width=5)
    img.alpha_composite(lay)
    k = v.get("k", 5.0); q = 1 - math.exp(-t / k)
    x = lerp(W / 2 + 160, ex - 60, q)
    red = min(1, t / (dur * 0.7)); fade = max(0.05, 1 - max(0, t - dur * 0.45) / (dur * 0.5))
    tint = mix((240, 240, 250), (200, 30, 20), red)
    draw_astro(img, x, 520, 0.95, rot=90, tint=tint, a=fade)
    seen = 12 * q  # the friend sees your watch creep toward a frozen reading
    alpha_text(img, (3 * W / 4 - 40, 520 + 260), f"00:{seen:05.2f}", F(64, "Black"), mix(WHITE, (255, 80, 60), red), a * max(0.3, fade))
    alpha_text(img, (3 * W / 4 - 40, 520 + 315), "slows… reddens… freezes at the edge", F(30, "SemiBold"), DIM, a)
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5))

AU_KM = 1.496e8
def sc_horizonsize(img, v, t, dur):
    """event horizon drawn to scale over our solar system ('sun': the Sun crushed to a 6 km hole; 'sgr'; 'm87')"""
    kind = v["kind"]; cx, cy = 640, 540; d = ImageDraw.Draw(img); g = ease((t - 0.8) / 2.0); TX = 1440
    def orbit(rpx, name, col=(120, 135, 170), lab_ang=-40):
        for k in range(0, 360, 5): d.arc([cx - rpx, cy - rpx, cx + rpx, cy + rpx], k, k + 2.5, fill=col, width=2)
        a = math.radians(lab_ang); d.text((cx + rpx * math.cos(a) + 8, cy + rpx * math.sin(a) - 8), name, font=F(28, "Bold"), fill=col, anchor="lb")
    if kind == "sun":
        rs = lerp(230, 3, g)
        paste_c(img, sun_sprite(int(max(3, rs))), cx, cy, max(0, 1 - g * 1.1))
        if g > 0.85:
            q = ease((g - 0.85) / 0.15); d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(2, 2, 4), outline=(255, 245, 225), width=2)
        ang = t * 0.35; ex, ey = cx + 400 * math.cos(ang), cy + 400 * math.sin(ang)
        orbit(400, "Earth's orbit — unchanged", PALE, 30)
        paste_c(img, earth_sprite(22, light=(cx - ex, cy - ey), glow=None), ex, ey)
        alpha_text(img, (1500, 400), "Sun", F(44, "Bold"), GOLD, 1 - g, anchor="mm")
        alpha_text(img, (1500, 455), "1.39 million km wide", F(36, "SemiBold"), WHITE, 1 - g, anchor="mm")
        alpha_text(img, (1500, 400), "Same mass, as a black hole", F(40, "Bold"), EMBER, g, anchor="mm")
        alpha_text(img, (1500, 470), "≈ 6 km wide", F(64, "Black"), WHITE, g, anchor="mm")
    else:
        if kind == "sgr":
            hr = 12.7e6; scale = 400 / 57.9e6
            orbs = [(57.9e6, "Mercury", -50), (108.2e6, "Venus", -30)]
            head, sub, cmp = "Sagittarius A*", "4 million Suns · horizon ≈ 25 million km wide", "fits inside Mercury's orbit"
        else:
            hr = 19.2e9; scale = 390 / 19.2e9
            orbs = [(5.2 * AU_KM, "Jupiter", -70), (30.1 * AU_KM, "Neptune", -45), (39.5 * AU_KM, "Pluto", -20)]
            head, sub, cmp = "M87*", "6.5 billion Suns · horizon ≈ 38 billion km wide", "swallows Pluto's orbit 3 times over"
        rp = hr * scale * g
        if rp > 2:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            for k in range(14): d2.ellipse([cx - rp - k * 4, cy - rp - k * 4, cx + rp + k * 4, cy + rp + k * 4], outline=EMBER + (int(70 * (1 - k / 14)),), width=4)
            d2.ellipse([cx - rp, cy - rp, cx + rp, cy + rp], fill=(2, 2, 4, 235), outline=(255, 245, 225, 255), width=3)
            img.alpha_composite(lay); d = ImageDraw.Draw(img)
        for r_, n_, la in orbs:
            if r_ * scale < 520: orbit(r_ * scale, n_, (150, 165, 200), la)
        paste_c(img, sun_sprite(4 if kind == "sgr" else 2), cx, cy)
        d.text((cx, cy + 18), "Sun", font=F(22, "Bold"), fill=GOLD, anchor="mt")
        alpha_text(img, (TX, 360), head, F(72, "Black"), EMBER, ease(t / 0.5))
        alpha_text(img, (TX, 440), sub, F(30, "SemiBold"), WHITE, ease((t - 0.3) / 0.5))
        alpha_text(img, (TX, 600), "its event horizon…", F(40, "SemiBold"), DIM, ease((t - 1.0) / 0.5))
        alpha_text(img, (TX, 670), cmp, F(42, "ExtraBold"), PALE, ease((t - 2.8) / 0.5))
    caption(img, v.get("caption"), ease((t - 3.0) / 0.5))

def sc_inside(img, v, t, dur):
    """inside the horizon: every possible path (little light cones) tips toward the singularity; clock of time left"""
    cx, cy, Rh = 640, 540, 400; d = ImageDraw.Draw(img)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    for k in range(30): d2.ellipse([cx - Rh + k * 6, cy - Rh + k * 6, cx + Rh - k * 6, cy + Rh - k * 6], fill=(40 + k * 2, 8, 6, 20))
    d2.ellipse([cx - Rh, cy - Rh, cx + Rh, cy + Rh], outline=(255, 245, 225, 255), width=3)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    rng = random.Random(9)
    for i in range(46):
        ang = rng.uniform(0, 6.283); r0 = rng.uniform(0.25, 0.98)
        r = (r0 - 0.08 * t) % 0.75 + 0.22; x, y = cx + Rh * r * math.cos(ang), cy + Rh * r * math.sin(ang)
        ux, uy = -math.cos(ang), -math.sin(ang); px, py = -uy, ux; L = 34; wdt = 14 * r
        tip = (x + ux * L, y + uy * L)
        d.polygon([tip, (x + px * wdt, y + py * wdt), (x - px * wdt, y - py * wdt)], fill=mix(SPACE, PALE, 0.35 + 0.65 * r))
    paste_c(img, radial(70, [(0, (255, 255, 255, 255)), (0.3, (255, 200, 150, 220)), (1, (255, 120, 60, 0))]), cx, cy)
    alpha_text(img, (cx, cy - Rh - 36), "event horizon", F(32, "Bold"), (255, 245, 225), 1)
    alpha_text(img, (cx, cy + 62), "singularity", F(28, "Bold"), HOT, 1)
    tx = 1460
    alpha_text(img, (tx, 260), v.get("head", "Inside, every path points in"), F(48, "ExtraBold"), WHITE, ease(t / 0.5))
    if v.get("timer") is not None:
        T = v["timer"]; left = max(0.0, T - max(0, t - 1.0)) if v.get("count", False) else T
        s = v.get("timer_fmt", "{:.0f} s").format(left)
        alpha_text(img, (tx, 470), v.get("timer_lab", "max time left (your clock)"), F(34, "SemiBold"), DIM, ease((t - 0.5) / 0.5))
        alpha_text(img, (tx, 580), s, F(130, "Black"), EMBER, ease((t - 0.7) / 0.5))
        if v.get("timer_sub"): alpha_text(img, (tx, 690), v["timer_sub"], F(34, "SemiBold"), PALE, ease((t - 1.5) / 0.5))
    else:
        for i, l in enumerate(v.get("lines", [])):
            alpha_text(img, (tx, 420 + i * 90), l, F(44, "Bold"), PALE if i % 2 else WHITE, ease((t - 1.0 - i * 2.2) / 0.5))
    caption(img, v.get("caption"), ease((t - 1.5) / 0.5))


# ---------------- scenes (EP05: crimson / cream palette) ----------------
CRIM, CREAM, YEL = (255, 77, 109), (255, 226, 154), (255, 214, 90)
RSUN_AU = 696000 / 1.496e8
ORB_AU = [("Mercury", 0.387), ("Venus", 0.723), ("Earth", 1.0), ("Mars", 1.524), ("Jupiter", 5.2), ("Saturn", 9.54)]

def draw_star(img, cx, cy, r, col, a=1.0):
    """big star drawn with concentric ellipses (limb darkening + soft glow) — cheap at any radius"""
    if r < 0.6 or a <= 0: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(10, 0, -1):
        rr = r * (1 + 0.05 * k); d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col + (int(14 * a),))
    n = 14 if r > 30 else 5
    for k in range(n):
        f = k / n; rr = r * (1 - f * 0.92)
        c = mix(mix(col, (40, 10, 10), 0.35), mix(col, (255, 250, 235), 0.55), f ** 0.8)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c + (int(255 * a),))
    img.alpha_composite(lay)

def sc_inflate(img, v, t, dur):
    """star grows (or shrinks) in the Sun's place, drawn to scale over planetary orbits; odometer of × Sun's width; swallowed list"""
    cx, cy = v.get("cx", 640), 540
    r0, r1 = v.get("r0", 1), v["r1"]; c0 = tuple(v.get("col0", v.get("col", CRIM))); c1 = tuple(v.get("col1", v.get("col", CRIM)))
    maxau = v.get("maxau", max(r0, r1) * RSUN_AU * 1.12); scale = 470 / maxau
    p = easeio((t - 0.6) / max(1.0, dur * 0.55))
    rs = math.exp(lerp(math.log(r0), math.log(r1), p)); col = mix(c0, c1, p)
    rpx = rs * RSUN_AU * scale
    d = ImageDraw.Draw(img)
    for name, au in ORB_AU:
        rp = au * scale
        if rp > 900 or rp < 6: continue
        inside = rpx > rp
        oc = (150, 165, 200)
        for k in range(0, 360, 5): d.arc([cx - rp, cy - rp, cx + rp, cy + rp], k, k + 2.5, fill=oc, width=2)
        ang = t * 0.25 / math.sqrt(au) + au * 2.1; px, py = cx + rp * math.cos(ang), cy + rp * math.sin(ang)
        if not inside:
            paste_c(img, planet_sprite(9 if name != "Jupiter" and name != "Saturn" else 14, PCOL.get(name, (200, 200, 200)), light=(cx - px, cy - py)), px, py)
    draw_star(img, cx, cy, max(1.0, rpx), col)
    if rpx < 8: paste_c(img, sun_sprite(4), cx, cy)
    d = ImageDraw.Draw(img)
    prev = -99
    for name, au in ORB_AU:
        rp = au * scale
        if rp > 900 or rp < 6 or rpx > rp or rp - prev < 34: continue
        prev = rp
        a = math.radians(-35 - au * 6); lx, ly = cx + rp * math.cos(a) + 8, cy + rp * math.sin(a) - 8
        if 0 < lx < 1180 and 30 < ly < 1050:
            ins = rpx > rp
            alpha_text(img, (lx, ly), name, F(28, "Bold"), (255, 255, 255) if ins else (150, 165, 200), 1, anchor="lb", shadow=True)
    if v.get("companion"):
        rp = v["companion"] * scale; ang = t * 0.5
        for k in range(0, 360, 6): d.arc([cx - rp, cy - rp, cx + rp, cy + rp], k, k + 3, fill=CREAM, width=2)
        qx, qy = cx + rp * math.cos(ang), cy + rp * math.sin(ang)
        paste_c(img, radial(40, [(0, (255, 255, 255, 255)), (0.35, (200, 225, 255, 230)), (1, (150, 190, 255, 0))]), qx, qy)
        alpha_text(img, (qx, qy - 30), "companion", F(26, "Bold"), CREAM, 1)
    TX = 1500
    alpha_text(img, (TX, 250), v.get("name", ""), F(66 if len(v.get("name", "")) < 16 else 50, "Black"), col, ease(t / 0.5))
    if v.get("sub"): alpha_text(img, (TX, 318), v["sub"], F(30, "SemiBold"), DIM, ease((t - 0.3) / 0.5))
    alpha_text(img, (TX, 470), f"{rs:,.0f}×", F(150, "Black"), WHITE, ease((t - 0.4) / 0.5))
    alpha_text(img, (TX, 570), "the Sun's width", F(38, "SemiBold"), CREAM, ease((t - 0.4) / 0.5))
    sw = [n for n, au in ORB_AU if rpx > au * scale]
    if sw and not v.get("hide_swallowed"):
        alpha_text(img, (TX, 680), "inside the star:", F(32, "SemiBold"), DIM, 1)
        line = " · ".join(sw[:3]); alpha_text(img, (TX, 735), line, F(36, "Bold"), CRIM, 1)
        if len(sw) > 3: alpha_text(img, (TX, 785), " · ".join(sw[3:]), F(36, "Bold"), CRIM, 1)
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(48, "ExtraBold"), WHITE, ease((t - 0.2) / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_flight(img, v, t, dur):
    """a jet circling a star nonstop at 900 km/h; counter of how long the trip takes"""
    cx, cy, R0 = 640, 560, 330; col = tuple(v.get("col", CRIM))
    draw_star(img, cx, cy, R0, col)
    d = ImageDraw.Draw(img); Rp = R0 + 60
    for k in range(0, 360, 4): d.arc([cx - Rp, cy - Rp, cx + Rp, cy + Rp], k, k + 2, fill=(200, 210, 235), width=2)
    ang = -math.pi / 2 + t * 0.9; x, y = cx + Rp * math.cos(ang), cy + Rp * math.sin(ang)
    ux, uy = -math.sin(ang), math.cos(ang); px, py = -uy, ux
    pts = [(x + ux * 30, y + uy * 30), (x - ux * 18 + px * 22, y - uy * 18 + py * 22), (x - ux * 8, y - uy * 8), (x - ux * 18 - px * 22, y - uy * 18 - py * 22)]
    d.polygon(pts, fill=WHITE)
    for k in range(1, 12):
        a2 = ang - k * 0.035; d.ellipse([cx + Rp * math.cos(a2) - 3, cy + Rp * math.sin(a2) - 3, cx + Rp * math.cos(a2) + 3, cy + Rp * math.sin(a2) + 3], fill=mix(SPACE, WHITE, 1 - k / 12))
    alpha_text(img, (cx, cy), v.get("name", ""), F(54, "Black"), (30, 10, 10), 1, shadow=False)
    TX = 1460
    alpha_text(img, (TX, 250), "Fly around it nonstop", F(52, "ExtraBold"), WHITE, ease(t / 0.5))
    alpha_text(img, (TX, 315), "passenger jet · 900 km/h", F(32, "SemiBold"), DIM, ease((t - 0.3) / 0.5))
    p = easeio((t - 0.8) / max(1.0, dur * 0.45)); val = v["value"] * p
    alpha_text(img, (TX, 490), f"{val:,.0f}", F(170, "Black"), mix(WHITE, col, p), ease((t - 0.5) / 0.4))
    alpha_text(img, (TX, 600), v.get("unit", "years"), F(54, "Bold"), CREAM, ease((t - 0.5) / 0.4))
    for i, l in enumerate(v.get("notes", [])):
        alpha_text(img, (TX, 720 + i * 62), l, F(34, "SemiBold"), PALE if i % 2 == 0 else WHITE, ease((t - dur * 0.55 - i * 1.2) / 0.5))
    caption(img, v.get("caption"), ease((t - 3.0) / 0.5))

def sc_measure(img, v, t, dur):
    """how to measure a dot: linked telescopes (interferometry) + brightness & temperature -> size"""
    d = ImageDraw.Draw(img); sx, sy = 560, 230
    paste_c(img, radial(60, [(0, (255, 255, 255, 255)), (0.3, CRIM + (230,)), (1, CRIM + (0,))]), sx, sy)
    alpha_text(img, (sx, sy - 50), "a dot of light", F(30, "Bold"), CREAM, 1)
    base = [(200, 860), (440, 880), (680, 880), (920, 860)]
    for i, (x, y) in enumerate(base):
        a = ease((t - 0.5 - i * 0.4) / 0.5)
        if a <= 0: continue
        d.pieslice([x - 60, y - 60, x + 60, y + 60], 200, 340, fill=mix(SPACE, (200, 210, 235), a))
        d.rectangle([x - 8, y - 10, x + 8, y + 50], fill=mix(SPACE, (150, 160, 190), a))
        for k in range(8):
            f = ((t * 0.6 + k / 8) % 1.0); qx, qy = lerp(sx, x, f), lerp(sy, y - 40, f)
            d.ellipse([qx - 3, qy - 3, qx + 3, qy + 3], fill=mix(SPACE, CREAM, a * (1 - abs(f - 0.5))))
    if t > 2.0:
        q = ease((t - 2.0) / 0.6)
        d.line([(200, 960), (920, 960)], fill=mix(SPACE, CRIM, q), width=4)
        alpha_text(img, (560, 1000), "linked telescopes act like one giant mirror", F(30, "SemiBold"), WHITE, q)
    TX = 1440
    alpha_text(img, (TX, 220), v.get("head", "How do you measure a dot?"), F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    for i, l in enumerate(v.get("lines", [])):
        alpha_text(img, (TX, 380 + i * 90), l, F(42, "Bold"), CREAM if i % 2 else WHITE, ease((t - 1.0 - i * dur * 0.15) / 0.5))
    if v.get("formula"):
        q = ease((t - dur * 0.55) / 0.6)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.rounded_rectangle([TX - 330, 760, TX + 330, 900], 24, fill=(20, 10, 18, int(220 * q)), outline=CRIM + (int(255 * q),), width=3)
        img.alpha_composite(lay)
        alpha_text(img, (TX, 810), "L = 4π R² σ T⁴", F(56, "Black"), CRIM, q, shadow=False)
        alpha_text(img, (TX, 868), "brightness + temperature → size", F(28, "SemiBold"), WHITE, q, shadow=False)

def sc_density(img, v, t, dur):
    """log ruler of average densities (kg/m³), markers appear one by one"""
    x0, x1, y = 180, 1740, 600; lo, hi = -6, 4
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 190), v.get("title", "Average density"), F(64, "ExtraBold"), WHITE, ease(t / 0.5))
    alpha_text(img, (W / 2, 255), "kilograms per cubic meter · each tick = 10× more", F(30, "SemiBold"), DIM, ease((t - 0.2) / 0.5))
    d.line([(x0, y), (x1, y)], fill=(90, 105, 140), width=4)
    for e in range(lo, hi + 1):
        x = lerp(x0, x1, (e - lo) / (hi - lo)); d.line([(x, y - 14), (x, y + 14)], fill=(90, 105, 140), width=3)
        lab = f"{10.0 ** e:g}" if -3 <= e <= 3 else f"10^{e}"
        d.text((x, y + 40), lab, font=F(24, "Medium"), fill=DIM, anchor="mm")
    items = v["items"]; span = dur * 0.6 / len(items)
    for i, (lab, val, c) in enumerate(items):
        a = ease((t - 0.8 - i * span) / 0.5)
        if a <= 0: continue
        x = lerp(x0, x1, (math.log10(val) - lo) / (hi - lo)); up = i % 2 == 0; c = tuple(c)
        yy = y - 120 if up else y + 150
        d = ImageDraw.Draw(img); d.line([(x, y), (x, yy + (30 if up else -30))], fill=mix(SPACE, c, a), width=3)
        d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=mix(SPACE, c, a))
        alpha_text(img, (x, yy - (10 if up else -10)), lab, F(36, "ExtraBold"), c, a)
    if v.get("verdict"):
        q = ease((t - dur * 0.72) / 0.5)
        alpha_text(img, (W / 2, 900), v["verdict"], F(60, "Black"), CREAM, q)

def sc_heavyvsbig(img, v, t, dur):
    """biggest ≠ heaviest: Betelgeuse limb (700 Sun widths) vs R136a1 (≈35) vs the Sun, same scale"""
    s = 1.05; a1 = ease(t / 0.8); a2 = ease((t - 1.6) / 0.6); a3 = ease((t - 3.0) / 0.6)
    draw_star(img, -620, 600, 700 * s * a1 + 1, CRIM)
    alpha_text(img, (150, 170), "Betelgeuse", F(56, "Black"), CRIM, a1, anchor="lm")
    alpha_text(img, (150, 230), "≈ 700× the Sun's width · ≈ 18 Suns of mass", F(30, "SemiBold"), WHITE, a1, anchor="lm")
    cx = 1380
    if a2 > 0:
        draw_star(img, cx, 520, 35 * s * 2.0, (170, 205, 255), a2)
        alpha_text(img, (cx, 380), "R136a1", F(56, "Black"), (170, 205, 255), a2)
        alpha_text(img, (cx, 650), "≈ 35× the Sun's width", F(32, "SemiBold"), WHITE, a2)
        alpha_text(img, (cx, 700), "≈ 200 Suns of mass", F(44, "ExtraBold"), CREAM, a2)
    if a3 > 0:
        paste_c(img, sun_sprite(3), 1700, 520, a3); alpha_text(img, (1700, 560), "Sun", F(26, "Bold"), GOLD, a3)
        alpha_text(img, (1380, 860), "(R136a1 and Sun drawn 2× for visibility)", F(24, "Medium"), DIM, a3)
    caption(img, v.get("caption"), ease((t - 3.5) / 0.5))

def sc_balance(img, v, t, dur):
    """a star as a tug of war: gravity arrows in, pressure arrows out; optional outer layers blowing away"""
    cx, cy, R0 = 640, 540, 250; draw_star(img, cx, cy, R0 + 6 * math.sin(t * 2), CRIM)
    d = ImageDraw.Draw(img)
    for k in range(12):
        ang = k * math.pi / 6 + 0.26
        ux, uy = math.cos(ang), math.sin(ang)
        r1, r2 = R0 + 140, R0 + 40
        d.line([(cx + ux * r1, cy + uy * r1), (cx + ux * r2, cy + uy * r2)], fill=PALE, width=6)
        tip = (cx + ux * r2, cy + uy * r2); px, py = -uy, ux
        d.polygon([tip, (tip[0] + ux * 26 + px * 14, tip[1] + uy * 26 + py * 14), (tip[0] + ux * 26 - px * 14, tip[1] + uy * 26 - py * 14)], fill=PALE)
        ang2 = ang + math.pi / 12; ux, uy = math.cos(ang2), math.sin(ang2); px, py = -uy, ux
        a1, a2 = R0 * 0.45, R0 * 0.9; tip = (cx + ux * a2, cy + uy * a2)
        d.line([(cx + ux * a1, cy + uy * a1), tip], fill=CREAM, width=6)
        d.polygon([(tip[0] + ux * 22, tip[1] + uy * 22), (tip[0] + px * 13, tip[1] + py * 13), (tip[0] - px * 13, tip[1] - py * 13)], fill=CREAM)
    if v.get("blow"):
        rng = random.Random(4); q = ease((t - dur * 0.45) / 1.0)
        for i in range(140):
            ang = rng.uniform(0, 6.283); sp = rng.uniform(40, 120); ph = rng.random()
            r = R0 + ((t * sp + ph * 400) % 420)
            al = q * max(0, 1 - (r - R0) / 420)
            x, y = cx + r * math.cos(ang), cy + r * math.sin(ang); c = mix(SPACE, CRIM, al)
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=c)
    TX = 1460
    alpha_text(img, (TX, 230), v.get("head", "A star is a tug of war"), F(52, "ExtraBold"), WHITE, ease(t / 0.5))
    alpha_text(img, (TX, 360), "gravity pulls in", F(42, "Bold"), PALE, ease((t - 0.8) / 0.5))
    alpha_text(img, (TX, 430), "heat and light push out", F(42, "Bold"), CREAM, ease((t - 1.6) / 0.5))
    for i, l in enumerate(v.get("lines", [])):
        alpha_text(img, (TX, 580 + i * 80), l, F(40, "Bold"), CRIM if i == len(v["lines"]) - 1 else WHITE, ease((t - dur * 0.4 - i * dur * 0.12) / 0.5))
    caption(img, v.get("caption"), ease((t - 3.0) / 0.5))


# ---------------- scenes (EP06: teal / amber) ----------------
TEAL6, AMB6, SEA6 = (46, 230, 197), (255, 170, 60), (60, 140, 255)
_land6 = None
def land_blobs():
    global _land6
    if _land6 is None:
        rng = random.Random(606); _land6 = []
        for _ in range(9):
            la0, lo0, rad = rng.uniform(-55, 65), rng.uniform(0, 360), rng.uniform(12, 26)
            pts = []
            for k in range(18):
                a = k / 18 * 2 * math.pi; rr = rad * rng.uniform(0.6, 1.15)
                pts.append((la0 + rr * math.sin(a) * 0.8, lo0 + rr * math.cos(a) / max(0.3, math.cos(math.radians(la0)))))
            _land6.append(pts)
    return _land6

def proj6(lat, lon, rot, R, cx, cy, tilt=0.38):
    la, lo = math.radians(lat), math.radians(lon + rot)
    x = math.cos(la) * math.sin(lo); y0 = math.sin(la); z0 = math.cos(la) * math.cos(lo)
    y = y0 * math.cos(tilt) - z0 * math.sin(tilt); z = z0 * math.cos(tilt) + y0 * math.sin(tilt)
    return cx + R * x, cy - R * y, z

def arrow6(d, x, y, L, col, w=8):
    d.line([(x, y), (x + L, y)], fill=col, width=w)
    d.polygon([(x + L + 22, y), (x + L, y - 14), (x + L, y + 14)], fill=col)

def sc_spinglobe(img, v, t, dur):
    """rotating globe with speed-by-latitude arrows; top=True: seen from above the pole (speed rings); slow=True: spin winds down"""
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(60, "ExtraBold"), WHITE, ease(t / 0.5))
    marks = v.get("marks", [])
    if v.get("top"):
        cx, cy, R = 620, 590, 400
        paste_c(img, planet_sprite(R, (30, 80, 150), light=(-0.6, -0.6)), cx, cy)
        d = ImageDraw.Draw(img); rot = t * 0.35
        for k in range(12):
            a = rot + k * math.pi / 6
            d.line([(cx, cy), (cx + R * math.cos(a), cy + R * math.sin(a))], fill=(90, 160, 200), width=2)
        for i, (lat, lab) in enumerate(marks):
            q = ease((t - 0.8 - i * 1.6) / 0.6)
            if q <= 0: continue
            rr = R * math.cos(math.radians(lat)); col = mix(AMB6, TEAL6, i / max(1, len(marks) - 1))
            if rr > 4:
                d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=col + (int(255 * q),), width=4)
                a = rot * 1.0 - math.pi / 2
                px, py = cx + rr * math.cos(a), cy + rr * math.sin(a)
                L = 150 * math.cos(math.radians(lat)) * q; ux, uy = -math.sin(a), math.cos(a)
                d.line([(px, py), (px - ux * L, py - uy * L)], fill=col, width=7)
                tip = (px - ux * (L + 20), py - uy * (L + 20)); nx, ny = -uy, ux
                d.polygon([tip, (px - ux * L + nx * 12, py - uy * L + ny * 12), (px - ux * L - nx * 12, py - uy * L - ny * 12)], fill=col)
            else:
                g = 18 + 6 * math.sin(t * 4); d.ellipse([cx - g, cy - g, cx + g, cy + g], fill=TEAL6)
            y = 330 + i * 120
            d.line([(1200, y), (1250, y)], fill=col, width=6)
            alpha_text(img, (1275, y), lab, F(52, "Bold"), col if lat >= 89 else WHITE, q, anchor="lm")
        alpha_text(img, (cx, cy + R + 50), "North Pole at the center", F(34, "SemiBold"), DIM, ease((t - 1) / 0.5))
        caption(img, v.get("caption"), ease((t - 2) / 0.5))
        return
    cx, cy, R = 640, 600, 380
    speed = 22.0
    if v.get("slow"): rot = speed * 2.2 * (1 - math.exp(-t / 2.2)) + 3 * t
    else: rot = speed * t
    paste_c(img, planet_sprite(R, (32, 86, 160), light=(-0.9, -0.4), glow=(110, 190, 255)), cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for blob in land_blobs():
        pp = [proj6(la, lo, rot, R, cx, cy) for la, lo in blob]
        if sum(1 for p in pp if p[2] > 0.05) == len(pp):
            dl.polygon([(p[0], p[1]) for p in pp], fill=(70, 140, 85, 200))
    for lat in range(-60, 90, 30):
        pts = [proj6(lat, lo, 0, R, cx, cy) for lo in range(-180, 181, 6)]
        seg = [(p[0], p[1]) for p in pts if p[2] > 0]
        if len(seg) > 1: dl.line(seg, fill=(150, 220, 255, 110 if lat else 220), width=2 if lat else 4)
    for lo in range(0, 360, 30):
        pts = [proj6(la, lo, rot, R, cx, cy) for la in range(-90, 91, 6)]
        seg = []
        for p in pts:
            if p[2] > 0: seg.append((p[0], p[1]))
            elif len(seg) > 1: dl.line(seg, fill=(150, 220, 255, 90), width=2); seg = []
            else: seg = []
        if len(seg) > 1: dl.line(seg, fill=(150, 220, 255, 90), width=2)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    np_ = proj6(90, 0, 0, R, cx, cy); d.ellipse([np_[0] - 9, np_[1] - 9, np_[0] + 9, np_[1] + 9], fill=WHITE)
    for i, (lat, lab) in enumerate(marks):
        q = ease((t - 1.0 - i * min(2.2, dur * 0.6 / max(1, len(marks)))) / 0.6)
        if q <= 0: continue
        x, y, z = proj6(lat, 0, 0, R, cx, cy)
        col = mix(AMB6, TEAL6, i / max(1, len(marks) - 1))
        L = 190 * math.cos(math.radians(lat)) * q
        if v.get("slow"): L *= max(0.15, math.exp(-t / 3.0))
        if L > 6: arrow6(d, x, y, L, col)
        else: d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=col)
        ty = 300 + i * 130
        d.line([(x + max(L, 0) + 30, y), (1180, ty)], fill=col + (140,), width=2)
        alpha_text(img, (1200, ty), lab, F(50, "Bold"), WHITE, q, anchor="lm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_pendulum(img, v, t, dur):
    """Foucault pendulum seen from above: the swing plane slowly turns (sped up) while the bob swings"""
    cx, cy, R = 620, 600, 360
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(60, "ExtraBold"), WHITE, ease(t / 0.5))
    d.ellipse([cx - R - 20, cy - R - 20, cx + R + 20, cy + R + 20], fill=(18, 26, 44), outline=(90, 110, 150), width=4)
    for k in range(0, 360, 10):
        a = math.radians(k); r1 = R - (26 if k % 30 == 0 else 12)
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], fill=(120, 140, 180), width=3)
    rate = 0.09  # radians per second of video (sped up)
    for k in range(1, 9):  # ghost lines of earlier swings
        th = -(t - k * 0.9) * rate
        if t - k * 0.9 < 0: break
        d.line([(cx - R * 0.92 * math.cos(th), cy - R * 0.92 * math.sin(th)), (cx + R * 0.92 * math.cos(th), cy + R * 0.92 * math.sin(th))], fill=mix(SPACE, AMB6, 0.5 - k * 0.05), width=2)
    th = -t * rate; sw = math.sin(t * 2.2) * R * 0.88
    bx, by = cx + sw * math.cos(th), cy + sw * math.sin(th)
    d.line([(cx - R * 0.92 * math.cos(th), cy - R * 0.92 * math.sin(th)), (cx + R * 0.92 * math.cos(th), cy + R * 0.92 * math.sin(th))], fill=AMB6, width=4)
    d.line([(cx, cy), (bx, by)], fill=(200, 205, 220), width=3)
    paste_c(img, planet_sprite(34, (180, 170, 150), light=(-0.7, -0.7)), bx, by)
    d = ImageDraw.Draw(img); d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=WHITE)
    alpha_text(img, (cx, cy + R + 60), "seen from above · sped up", F(30, "SemiBold"), DIM, ease((t - 1) / 0.5))
    for i, (a_, b_) in enumerate(v.get("notes", [])):
        q = ease((t - dur * 0.45 - i * 2.0) / 0.6)
        alpha_text(img, (1180, 360 + i * 150), a_, F(40, "SemiBold"), DIM, q, anchor="lm")
        alpha_text(img, (1180, 412 + i * 150), b_, F(64, "Black"), TEAL6 if i else AMB6, q, anchor="lm")

def house6(d, x, y, s, col):
    d.rectangle([x - 40 * s, y - 60 * s, x + 40 * s, y], fill=col)
    d.polygon([(x - 52 * s, y - 60 * s), (x, y - 100 * s), (x + 52 * s, y - 60 * s)], fill=mix(col, (40, 20, 10), 0.4))
    d.rectangle([x - 10 * s, y - 30 * s, x + 10 * s, y], fill=(30, 30, 40))

def sc_fling(img, v, t, dur):
    """sudden stop: the ground halts, everything on it keeps flying east; two speed readouts"""
    d = ImageDraw.Draw(img); gy = 800; ts = v.get("stop_at", 0.1) * dur
    vpx = 900.0
    g_off = vpx * min(t, ts); o_off = vpx * t
    d.rectangle([0, gy, W, H], fill=(28, 34, 30))
    d.line([(0, gy), (W, gy)], fill=(120, 150, 120), width=4)
    for k in range(-1, 14):
        x = (k * 160 + g_off) % (W + 160) - 80
        d.line([(x, gy + 20), (x - 40, gy + 70)], fill=(70, 85, 70), width=4)
    after = t >= ts; sh = (t - ts) if after else 0
    objs = [("house", 0), ("tree", 300), ("car", 520), ("house", 780), ("tree", 1060), ("person", 1250), ("house", 1450), ("tree", 1700)]
    for kind, x0 in objs:
        x = (x0 + o_off) % (W + 400) - 200
        lift = -min(60, sh * 40) * (1 if kind in ("car", "person") else 0.3) if after else 0
        if after:
            for k in range(1, 7):
                d.line([(x - 60 - k * 40, gy - 30 - k * 9 + lift), (x - 60 - k * 40 - 80, gy - 30 - k * 9 + lift)], fill=(200, 220, 230, 90), width=3)
        if kind == "house": house6(d, x, gy + lift, 1.4, (200, 150, 110))
        elif kind == "tree":
            d.rectangle([x - 8, gy - 90 + lift, x + 8, gy + lift], fill=(110, 80, 50))
            ang = min(0.9, sh * 1.5) if after else 0
            d.ellipse([x - 50 + ang * 40, gy - 170 + lift + ang * 30, x + 50 + ang * 40, gy - 70 + lift + ang * 30], fill=(60, 150, 90))
        elif kind == "car":
            d.rounded_rectangle([x - 70, gy - 50 + lift, x + 70, gy - 12 + lift], 10, fill=(220, 80, 80))
            d.rounded_rectangle([x - 40, gy - 80 + lift, x + 35, gy - 48 + lift], 10, fill=(190, 60, 60))
            for wx in (-42, 42): d.ellipse([wx + x - 16, gy - 30 + lift, wx + x + 16, gy + 2 + lift], fill=(20, 20, 25))
        else:
            c = TEAL6; hx, hy = x, gy - 150 + lift
            d.ellipse([hx - 18, hy - 18, hx + 18, hy + 18], fill=c)
            lean = 30 if after else 0
            d.line([(hx, hy + 18), (hx - lean * 0.3, hy + 90)], fill=c, width=8)
            d.line([(hx - lean * 0.3, hy + 90), (hx - 25, gy + lift)], fill=c, width=8); d.line([(hx - lean * 0.3, hy + 90), (hx + 25, gy + lift)], fill=c, width=8)
            d.line([(hx, hy + 40), (hx + 40, hy + 20 - lean)], fill=c, width=7); d.line([(hx, hy + 40), (hx - 40, hy + 60)], fill=c, width=7)
    if after and v.get("debris"):
        rng = random.Random(int(t * 3))
        for k in range(40):
            x = (k * 97 + o_off * 1.1) % (W + 200) - 100; y = gy - 20 - (k * 53) % 260
            s = 6 + k % 10; d.rectangle([x - s, y - s / 2, x + s, y + s / 2], fill=(170, 150, 120))
    gv = v["speed"] if not after else max(0, v["speed"] * (1 - sh / 0.6))
    for i, (lab, val, col) in enumerate([("GROUND", gv, AMB6), ("YOU", v["speed"], TEAL6)]):
        x = W / 2 - 330 + i * 660
        d.rounded_rectangle([x - 280, 210, x + 280, 400], 24, fill=(10, 16, 30), outline=col, width=4)
        d.text((x, 250), lab, font=F(38, "Bold"), fill=col, anchor="mm")
        d.text((x, 330), f"{val:,.0f} km/h", font=F(80, "Black"), fill=WHITE, anchor="mm")
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(62, "ExtraBold"), WHITE, ease(t / 0.4))
    if after: caption(img, v.get("label", ""), ease((t - ts - 0.6) / 0.5), y=H - 80)

def sc_bulge(img, v, t, dur):
    """cross-section: spin bulge (phase 0) -> water runs to the poles, a ring continent rises at the equator (phase 1)"""
    cx, cy = 600, 610
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 110), v.get("head", ""), F(60, "ExtraBold"), WHITE, ease(t / 0.5))
    p = easeio((t - 1.5) / (dur * 0.45)) if v.get("phase") == 1 else 0.0
    lrx, lry = 372, 318
    wrx, wry = lerp(398, 352, p), lerp(344, 352, p)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([cx - wrx - 14, cy - wry - 14, cx + wrx + 14, cy + wry + 14], fill=(110, 180, 255, 40))
    dl.ellipse([cx - wrx, cy - wry, cx + wrx, cy + wry], fill=(40, 110, 220, 255))
    dl.ellipse([cx - lrx, cy - lry, cx + lrx, cy + lry], fill=(120, 96, 66, 255))
    dl.ellipse([cx - 200, cy - 180, cx + 200, cy + 180], fill=(150, 80, 40, 255))
    dl.ellipse([cx - 110, cy - 100, cx + 110, cy + 100], fill=(250, 190, 90, 255))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    if p > 0.6:
        q = (p - 0.6) / 0.4
        for s in (-1, 1):
            d.arc([cx - lrx - 6, cy - lry - 6, cx + lrx + 6, cy + lry + 6], (0 if s > 0 else 180) - 14, (0 if s > 0 else 180) + 14, fill=mix(SPACE, (120, 230, 120), q), width=12)
    d.line([(cx, cy - 395), (cx, cy + 395)], fill=(200, 210, 230), width=3)
    d.text((cx, cy - 418), "N", font=F(36, "Black"), fill=WHITE, anchor="mm"); d.text((cx, cy + 418), "S", font=F(36, "Black"), fill=WHITE, anchor="mm")
    for k in range(0, 1100, 30): d.line([(cx - 520 + k, cy), (cx - 505 + k, cy)], fill=(160, 170, 190), width=2)
    if v.get("phase") == 0:
        for s, yy in ((1, cy - 380), (-1, cy + 380)):
            a = (t * 2) % 1
            d.arc([cx - 90, yy - 22, cx + 90, yy + 22], 200, 340, fill=TEAL6, width=5)
        d.polygon([(cx + 86, cy - 392), (cx + 60, cy - 410), (cx + 66, cy - 380)], fill=TEAL6)
        pulse = 1 + 0.04 * math.sin(t * 3)
        for s in (-1, 1): arrow6(d, cx + s * 0 + (lrx + 40 if s > 0 else -lrx - 40 - 90 * pulse), cy - 40, 90 * pulse if s > 0 else 0, AMB6) if s > 0 else None
    else:
        q = ease((t - dur * 0.55) / 0.6)
        alpha_text(img, (cx, cy - 300), "polar ocean", F(34, "Bold"), (200, 230, 255), q)
        alpha_text(img, (cx, cy + 300), "polar ocean", F(34, "Bold"), (200, 230, 255), q)
        alpha_text(img, (cx + lrx + 24, cy + 50), "new land", F(34, "Bold"), (150, 240, 150), q, anchor="lm")
    alpha_text(img, (cx - lrx - 30, cy - 40), "equator", F(30, "SemiBold"), DIM, 1, anchor="rm")
    for i, n in enumerate(v.get("notes", [])):
        alpha_text(img, (1090, 380 + i * 100), n, F(38, "SemiBold"), WHITE if i else AMB6, ease((t - 1.2 - i * dur * 0.2) / 0.6), anchor="lm")
    alpha_text(img, (W - 60, H - 50), "not to scale — bulge exaggerated", F(26, "Medium"), DIM, ease((t - 1) / 0.5), anchor="rm")

def sc_yearday(img, v, t, dur):
    """a non-spinning Earth goes around the Sun: one spot gets ~6 months of day, then ~6 months of night"""
    cx, cy, R = 640, 590, 340
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(62, "ExtraBold"), WHITE, ease(t / 0.5))
    for k in range(0, 360, 3): d.arc([cx - R, cy - R * 0.92, cx + R, cy + R * 0.92], k, k + 1.5, fill=(80, 100, 140), width=2)
    paste_c(img, sun_sprite(80), cx, cy)
    frac = min(1.0, max(0.0, (t - 0.8) / (dur * 0.8)))
    ang = math.pi / 2 - frac * 2 * math.pi  # start below the Sun, go counterclockwise
    ex, ey = cx + R * math.cos(ang), cy + R * 0.92 * math.sin(ang)
    er = 46
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([ex - er, ey - er, ex + er, ey + er], fill=(14, 22, 44, 255))
    sa = math.degrees(math.atan2(cy - ey, cx - ex))
    dl.pieslice([ex - er, ey - er, ex + er, ey + er], sa - 90, sa + 90, fill=(70, 140, 230, 255))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    mx, my = ex, ey + er  # fixed spot: always points "down" (no spin)
    lit = ((cx - ex) * 0 + (cy - ey) * 1) > 0
    d.ellipse([mx - 11, my - 11, mx + 11, my + 11], fill=AMB6 if lit else (150, 160, 190), outline=WHITE, width=3)
    dayn = int(frac * 365) + 1
    TX = 1460
    alpha_text(img, (TX, 300), "your city", F(40, "SemiBold"), DIM, ease((t - 0.5) / 0.5))
    alpha_text(img, (TX, 420), "DAYLIGHT" if lit else "NIGHT", F(110, "Black"), AMB6 if lit else (150, 170, 230), ease((t - 0.5) / 0.5))
    alpha_text(img, (TX, 560), f"day {min(365, dayn)} of 365", F(56, "Bold"), WHITE, ease((t - 0.5) / 0.5))
    alpha_text(img, (TX, 680), "one sunrise per year", F(40, "SemiBold"), TEAL6, ease((t - dur * 0.5) / 0.5))

def sc_dayclock(img, v, t, dur):
    """24-hour dial: how long a day lasted at different moments of Earth's history"""
    cx, cy, R = 600, 600, 300
    d = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(60, "ExtraBold"), WHITE, ease(t / 0.5))
    items = v["items"]; n = len(items); seg = max(1.5, dur * 0.85 / n)
    k = min(n - 1, int(max(0, t - 0.6) // seg)); lt = (max(0, t - 0.6) - k * seg)
    prev = items[k - 1][1] if k > 0 else 0
    val = lerp(prev, items[k][1], easeio(lt / 1.4))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=(50, 64, 96), width=46)
    for h in range(24):
        a = math.radians(h * 15 - 90); r1 = R + 34; r2 = R + (52 if h % 6 == 0 else 44)
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], fill=(140, 150, 180), width=3)
        if h % 6 == 0: d.text((cx + (R + 84) * math.cos(a), cy + (R + 84) * math.sin(a)), f"{h}h" if h else "24h", font=F(30, "Bold"), fill=DIM, anchor="mm")
    if val > 0.05:
        d.arc([cx - R, cy - R, cx + R, cy + R], -90, -90 + val * 15, fill=TEAL6 if k == n - 1 else AMB6, width=46)
    d.text((cx, cy - 20), f"{val:.1f} h", font=F(120, "Black"), fill=WHITE, anchor="mm")
    d.text((cx, cy + 80), items[k][0], font=F(36, "SemiBold"), fill=AMB6 if k < n - 1 else TEAL6, anchor="mm")
    for i, (lab, hrs) in enumerate(items):
        a = ease((t - 0.6 - i * seg) / 0.5)
        if a <= 0: continue
        y = 360 + i * 150
        alpha_text(img, (1180, y), lab, F(40, "SemiBold"), DIM, a, anchor="lm")
        alpha_text(img, (1180, y + 52), f"{hrs:g} hours", F(56, "Black"), TEAL6 if i == n - 1 else AMB6, a, anchor="lm")
    caption(img, v.get("caption"), ease((t - 2) / 0.5))


# ---------------- scenes (EP07: neutron star) ----------------
NSB, CORAL7, PALE7, GOLD7 = (91, 140, 255), (255, 111, 145), (200, 220, 255), (255, 200, 80)
def ns_sprite(r, hot=True):
    return radial(int(r * 3.2) + 8, [(0, (255, 255, 255, 255)), (0.5 / 1.6, (225, 238, 255, 255)), (0.98 / 1.6, (150, 185, 255, 255)),
                                     (1.0 / 1.6, (120, 160, 255, 255)), (1.12 / 1.6, (91, 140, 255, 120)), (1.0, (91, 140, 255, 0))])
_ns = {}
def ns(r):
    r = max(3, int(r))
    if r not in _ns: _ns[r] = ns_sprite(r)
    return _ns[r]

def draw_spoon(d, x, y, s, col=(200, 206, 220)):
    d.ellipse([x - 170 * s, y - 95 * s, x + 170 * s, y + 95 * s], fill=col)
    d.ellipse([x - 150 * s, y - 78 * s, x + 150 * s, y + 70 * s], fill=(130, 136, 152))
    d.polygon([(x + 160 * s, y - 20 * s), (x + 560 * s, y - 50 * s), (x + 570 * s, y - 20 * s), (x + 165 * s, y + 18 * s)], fill=col)

def sc_teaspoon(img, v, t, dur):
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    d = ImageDraw.Draw(img); sx, sy = 640, 560
    if v.get("phase", 0) == 0:
        # industrial scale + spoon + glowing matter; readout counts up; humanity bar for comparison
        d.rounded_rectangle([300, 680, 980, 760], 18, fill=(40, 48, 70), outline=(110, 120, 150), width=3)
        d.rectangle([330, 640, 950, 680], fill=(70, 80, 105))
        draw_spoon(d, sx - 120, sy, 0.9)
        paste_c(img, ns(60 + 4 * math.sin(t * 5)), sx - 120, sy - 6)
        d = ImageDraw.Draw(img)
        p = easeio((t - 0.2) / 2.4); tons = 2e9 * p
        d.rounded_rectangle([300, 780, 980, 880], 14, fill=(8, 14, 10), outline=(80, 255, 140), width=3)
        d.text((640, 830), f"{tons:,.0f} t", font=F(56, "Black"), fill=(120, 255, 170), anchor="mm")
        # comparison bars
        x0 = 1120; bw = 470
        alpha_text(img, (x0, 380), "1 teaspoon", F(44, "Bold"), PALE7, ease((t - 1.0) / 0.5), anchor="lm")
        alpha_text(img, (x0, 560), "all 8 billion humans", F(44, "Bold"), CORAL7, ease((t - 1.6) / 0.5), anchor="lm")
        a1 = ease((t - 1.0) / 1.0); a2 = ease((t - 1.6) / 1.0)
        if a1 > 0: d.rounded_rectangle([x0, 420, x0 + bw * a1, 480], 12, fill=NSB)
        if a2 > 0: d.rounded_rectangle([x0, 600, x0 + bw * 0.26 * a2, 660], 12, fill=CORAL7)
        alpha_text(img, (x0 + bw + 20, 450), "≈ 2 billion t", F(36, "Bold"), WHITE, a1, anchor="lm", shadow=False)
        alpha_text(img, (x0 + bw * 0.26 + 20, 630), "≈ 0.5 billion t", F(36, "Bold"), WHITE, a2, anchor="lm", shadow=False)
        caption(img, "our calculation: average density ≈ 400 million tonnes per cm³", ease((t - 3) / 0.5))
    else:
        # the teaspoon "at home" vs on Earth: matter expands violently
        draw_spoon(d, sx - 120, sy, 0.9)
        te = max(2.0, dur * 0.45); p = max(0.0, t - te)
        if p <= 0:
            paste_c(img, ns(60), sx - 120, sy - 6)
            alpha_text(img, (sx, 820), "held together only by its star's gravity", F(42, "SemiBold"), PALE7, ease(t / 0.5))
        else:
            r = 60 + 900 * (1 - math.exp(-p * 1.4))
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            fa = max(0.18, 1 - p / 3)
            dl.ellipse([sx - 120 - r, sy - r, sx - 120 + r, sy + r], fill=(220, 235, 255, int(150 * fa)))
            for k in range(3):
                rr = r * (0.6 + 0.2 * k); dl.ellipse([sx - 120 - rr, sy - rr, sx - 120 + rr, sy + rr], outline=CORAL7 + (int(220 * fa),), width=6)
            rng = random.Random(7)
            for _ in range(160):
                ang = rng.uniform(0, 2 * math.pi); sp = rng.uniform(200, 900)
                x, y = sx - 120 + math.cos(ang) * sp * p, sy + math.sin(ang) * sp * p
                dl.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(255, 230, 200, int(255 * fa)))
            img.alpha_composite(lay)
        alpha_text(img, (1420, 400), "In the star:", F(46, "Bold"), DIM, ease((t - 0.4) / 0.5))
        alpha_text(img, (1420, 470), "gravity wins", F(64, "ExtraBold"), NSB, ease((t - 0.4) / 0.5))
        alpha_text(img, (1420, 600), "On Earth:", F(46, "Bold"), DIM, ease((t - te + 0.8) / 0.5))
        alpha_text(img, (1420, 670), "pressure wins", F(64, "ExtraBold"), CORAL7, ease((t - te + 0.8) / 0.5))

def sc_pulsechart(img, v, t, dur):
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    x0, x1, y0, y1 = 140, W - 140, 260, 820
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rectangle([x0, y0, x1, y1], fill=(236, 228, 205, 245))
    off = (t * 120) % 60
    for gx in np.arange(x0 - off + 60, x1, 60): d.line([(gx, y0), (gx, y1)], fill=(210, 180, 170, 255), width=1)
    for gy in range(y0 + 40, y1, 56): d.line([(x0, gy), (x1, gy)], fill=(210, 180, 170, 255), width=1)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    pxs = 360.0  # px per second of signal
    ph = v.get("phase", 0); per = v.get("period", 1.33); cy = (y0 + y1) / 2 + 60
    rng = np.random.default_rng(3)
    noise = rng.normal(0, 1, 4000)
    pts = []
    for x in range(x0, x1, 3):
        ts = (x - x0) / pxs + t * 0.33 * (1 + ph)
        n = noise[int(ts * 60) % 4000] * (14 if ph == 0 else 6)
        pk = math.exp(-((ts % per) - 0.05) ** 2 / 0.0012) * (70 if ph == 0 else 240)
        pts.append((x, cy - n - pk))
    d.line(pts, fill=(40, 40, 120), width=3)
    if ph == 1:
        # dimension marker between two peaks
        base = (t * 0.66) % per; xa = x0 + (per - base + 0.05) * pxs
        if xa + per * pxs < x1:
            d.line([(xa, y0 + 50), (xa + per * pxs, y0 + 50)], fill=(200, 40, 70), width=4)
            d.text((xa + per * pxs / 2, y0 + 28), f"{per} s", font=F(40, "ExtraBold"), fill=(200, 40, 70), anchor="mm")
        a = ease((t - 1.5) / 0.4)
        if a > 0:
            st = Image.new("RGBA", (520, 150), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
            ds.rounded_rectangle([6, 6, 514, 144], 16, outline=(200, 30, 60, int(230 * a)), width=8)
            ds.text((260, 75), "LGM-1 ?", font=F(84, "Black"), fill=(200, 30, 60, int(230 * a)), anchor="mm")
            st = st.rotate(8, expand=True, resample=Image.BICUBIC); img.alpha_composite(st, (W - 760, y1 - 260))
    else:
        a = ease((t - 2) / 0.5)
        if a > 0: d.ellipse([x0 + 600, cy - 140, x0 + 900, cy + 60], outline=(200, 40, 70), width=int(1 + 4 * a))
        alpha_text(img, (x0 + 750, cy - 175), "\"scruff\"", F(44, "ExtraBold"), (200, 40, 70), a, shadow=False)
    caption(img, v.get("caption", "radio chart recorder, Cambridge"), ease((t - 1) / 0.5))

def sc_crush(img, v, t, dur):
    alpha_text(img, (W / 2, 120), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    cx, cy = 760, 570; R0 = 300
    if v.get("phase", 0) == 0:
        pl = planet_sprite(R0, (150, 120, 100), light=(-0.8, -0.5))
        paste_c(img, pl, cx, cy, ease(t / 0.6))
        d = ImageDraw.Draw(img)
        for k in range(0, 360, 12):
            a0 = k + t * 6; d.arc([cx - R0 - 40, cy - R0 - 40, cx + R0 + 40, cy + R0 + 40], a0, a0 + 6, fill=(255, 150, 80), width=4)
        alpha_text(img, (1480, 430), "iron core", F(48, "Bold"), DIM, ease((t - 0.8) / 0.5))
        alpha_text(img, (1480, 510), "≈ Earth-sized", F(64, "ExtraBold"), (255, 170, 110), ease((t - 0.8) / 0.5))
        alpha_text(img, (1480, 640), "mass", F(48, "Bold"), DIM, ease((t - 1.6) / 0.5))
        alpha_text(img, (1480, 720), "≈ 1.5 Suns", F(64, "ExtraBold"), (255, 170, 110), ease((t - 1.6) / 0.5))
        caption(img, "iron can't be burned for energy", ease((t - 3) / 0.5))
    else:
        p = easeio((t - 0.6) / 3.0)
        diam = math.exp(lerp(math.log(12700), math.log(30), p)); r = max(4, R0 * diam / 12700 * (1 if p < 1 else 1))
        rr = max(8, r)
        if p < 1: paste_c(img, planet_sprite(int(max(6, r)), (150, 120, 100), light=(-0.8, -0.5)), cx, cy)
        else: paste_c(img, ns(10), cx, cy)
        q = max(0.0, (t - 3.8) / 3.0)
        if q > 0:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            for k in range(3):
                R2 = (q * 500 + k * 60) % 560
                dl.ellipse([cx - R2, cy - R2, cx + R2, cy + R2], outline=(255, 160, 90, int(200 * max(0, 1 - R2 / 560))), width=10 - 2 * k)
            img.alpha_composite(lay)
        d = ImageDraw.Draw(img)
        d.text((1480, 430), "diameter", font=F(46, "Bold"), fill=DIM, anchor="mm")
        d.text((1480, 510), f"{diam:,.0f} km", font=F(84, "Black"), fill=NSB if p > 0.95 else WHITE, anchor="mm")
        d.text((1480, 640), "time", font=F(46, "Bold"), fill=DIM, anchor="mm")
        d.text((1480, 720), f"{0.5 * p:.2f} s", font=F(84, "Black"), fill=CORAL7, anchor="mm")
        alpha_text(img, (cx, 980), "collapse speed ≈ 1/4 of light speed" if q <= 0 else "the rest of the star blasts out: supernova", F(42, "SemiBold"), PALE7, 1.0)

def sc_ladder(img, v, t, dur):
    """log-scale ladder: items [[label, exp_lo, exp_hi, col]]"""
    alpha_text(img, (160, 200), v["title"], F(64, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    x0, x1, mx = 640, 1780, v.get("max", 15); d = ImageDraw.Draw(img)
    for k in range(0, mx + 1, 3):
        x = lerp(x0, x1, k / mx); d.line([(x, 320), (x, 880)], fill=(40, 50, 75), width=2)
        d.text((x, 290), "1" if k == 0 else f"10{''.join('⁰¹²³⁴⁵⁶⁷⁸⁹'[int(c)] for c in str(k))}", font=F(36, "Bold"), fill=DIM, anchor="mm")
    for i, (lab, lo, hi, c) in enumerate(v["items"]):
        p = ease((t - 0.5 - i * 1.0) / 1.2); y = 410 + i * 180
        d.text((160, y), lab, font=F(46, "SemiBold"), fill=mix(SPACE, WHITE, p), anchor="lm")
        if p <= 0: continue
        xa = lerp(x0, x1, lo / mx * p); xb = lerp(x0, x1, hi / mx * p)
        d.rounded_rectangle([x0, y - 34, max(x0 + 12, xb), y + 34], 14, fill=hexc(c) if lo == hi else mix(SPACE, hexc(c), 0.45))
        if hi > lo: d.rounded_rectangle([xa, y - 34, max(xa + 12, xb), y + 34], 14, fill=hexc(c))
        if v.get("notes") and i < len(v["notes"]): alpha_text(img, (max(x0 + 12, xb) + 20 if xb < 1500 else xb - 20, y), v["notes"][i], F(36, "Bold"), WHITE, p, anchor="lm" if xb < 1500 else "rm")
    caption(img, v.get("caption"), ease((t - 3) / 0.5))

def sc_layers(img, v, t, dur):
    alpha_text(img, (W / 2, 110), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    cx, cy, R0 = 640, 620, 360
    lays = v["items"]  # [label, frac_outer_radius, col, note]
    glow = ns(R0); paste_c(img, glow, cx, cy)
    d = ImageDraw.Draw(img)
    for i, (lab, fr, c, *_) in enumerate(lays):
        r = R0 * fr; d.pieslice([cx - r, cy - r, cx + r, cy + r], -90, 90, fill=hexc(c))
    d.line([(cx, cy - R0), (cx, cy + R0)], fill=(255, 255, 255), width=3)
    n = len(lays); span = max(1.0, dur * 0.7) / n
    for i, (lab, fr, c, *rest) in enumerate(lays):
        a = ease((t - 0.5 - i * span) / 0.5)
        if a <= 0: continue
        nxt = lays[i + 1][1] if i + 1 < n else 0
        rm = R0 * (fr + nxt) / 2; ang = math.radians(-50 + i * 30)
        px, py = cx + rm * math.cos(ang), cy + rm * math.sin(ang)
        ly = 330 + i * 150; tc = hexc(c) if sum(hexc(c)) > 250 else (150, 165, 220)
        d.line([(px, py), (1150, ly), (1190, ly)], fill=tc, width=3); d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=WHITE)
        alpha_text(img, (1210, ly), lab, F(50, "ExtraBold"), tc, a, anchor="lm")
        if rest: alpha_text(img, (1210, ly + 52), rest[0], F(34, "SemiBold"), DIM, a, anchor="lm")
    caption(img, v.get("caption"), ease((t - 3) / 0.5))

def sc_lensing(img, v, t, dur):
    alpha_text(img, (W / 2, 110), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    cx, cy, r = 760, 580, 190
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ex, ey = 1640, 580
    # bent rays from the far side to the eye
    for k in range(-5, 6):
        if k == 0: continue
        ang = math.radians(180 - k * 15); sxp, syp = cx + r * math.cos(ang), cy + r * math.sin(ang)
        bend = 1 if k > 0 else -1
        pts = []
        p = ease((t - 0.4 - abs(k) * 0.12) / 1.4)
        for j in range(41):
            u = j / 40 * p
            bx = (1 - u) ** 2 * sxp + 2 * (1 - u) * u * cx + u ** 2 * ex
            by = (1 - u) ** 2 * syp + 2 * (1 - u) * u * (cy - bend * (r + 120 + abs(k) * 22)) + u ** 2 * ey
            pts.append((bx, by))
        if len(pts) > 1: d.line(pts, fill=(255, 210, 120, 170), width=3)
    img.alpha_composite(lay)
    paste_c(img, ns(r), cx, cy)
    d = ImageDraw.Draw(img)
    for k, (a0, a1) in enumerate([(200, 235), (40, 70)]):
        st = (t * 40) % 360
        d.arc([cx - r * 0.9, cy - r * 0.9, cx + r * 0.9, cy + r * 0.9], a0 + st, a1 + st, fill=(255, 150, 120), width=16)
    # eye
    d.ellipse([ex - 60, ey - 30, ex + 60, ey + 30], outline=WHITE, width=5); d.ellipse([ex - 16, ey - 16, ex + 16, ey + 16], fill=NSB)
    d.text((ex, ey + 70), "you", font=F(40, "Bold"), fill=WHITE, anchor="mm")
    alpha_text(img, (W / 2, 200), "you see more than half of the surface at once", F(44, "SemiBold"), PALE7, ease((t - 1.8) / 0.5))
    caption(img, "NICER (NASA): PSR J0030+0451 ≈ 26 km wide, ≈ 1.4 Suns", ease((t - 4) / 0.5))

def sc_pulsar(img, v, t, dur):
    alpha_text(img, (W / 2, 110), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    cx, cy = 700, 560; ang = t * 2 * math.pi * 0.45
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for s in (0, math.pi):
        a = ang + s; L = 900; wdt = 0.12
        pts = [(cx, cy), (cx + L * math.cos(a - wdt), cy + 0.55 * L * math.sin(a - wdt)), (cx + L * math.cos(a + wdt), cy + 0.55 * L * math.sin(a + wdt))]
        d.polygon(pts, fill=(160, 200, 255, 70))
        pts2 = [(cx, cy), (cx + L * math.cos(a - wdt / 3), cy + 0.55 * L * math.sin(a - wdt / 3)), (cx + L * math.cos(a + wdt / 3), cy + 0.55 * L * math.sin(a + wdt / 3))]
        d.polygon(pts2, fill=(230, 240, 255, 110))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(6)))
    paste_c(img, ns(70), cx, cy)
    d = ImageDraw.Draw(img)
    d.text((cx, cy + 300), "animation slowed about 1,600×", font=F(32, "SemiBold"), fill=DIM, anchor="mm")
    pl = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(pl).rounded_rectangle([1150, 340, 1850, 850], 30, fill=(8, 10, 24, 225), outline=NSB + (160,), width=3)
    img.alpha_composite(pl); d = ImageDraw.Draw(img)
    turns = max(0.0, t - 0.5) * v.get("hz", 716)
    d.text((1500, 420), "turns so far", font=F(44, "Bold"), fill=DIM, anchor="mm")
    d.text((1500, 510), f"{turns:,.0f}", font=F(110, "Black"), fill=NSB, anchor="mm")
    # pulse train: one tick per turn (dense)
    y = 760; d.line([(1180, y), (1820, y)], fill=(60, 70, 100), width=2)
    for k in range(0, 640, 9):
        x = 1180 + (k - (t * 300) % 9); d.line([(x, y), (x, y - 70)], fill=CORAL7, width=3)
    d.text((1500, 810), "one pulse per turn", font=F(32, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("sub"), ease((t - 1.5) / 0.5))

def sc_merger(img, v, t, dur):
    alpha_text(img, (W / 2, 110), v.get("head", ""), F(64, "ExtraBold"), WHITE, ease(t / 0.4))
    cx, cy = W / 2, 560
    if v.get("phase", 0) == 0:
        T = max(1.0, dur - 1.5); u = min(1.0, t / T)
        sep = 300 * (1 - u) ** 0.25 if u < 1 else 0
        ph = 2 * math.pi * (1 - (1 - min(u, 0.999)) ** 0.62) * 9
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for k in range(8):
            R2 = ((t * 160 + k * 110) % 880)
            d.ellipse([cx - R2, cy - R2 * 0.6, cx + R2, cy + R2 * 0.6], outline=(120, 160, 255, int(120 * (1 - R2 / 880))), width=4)
        img.alpha_composite(lay)
        if u < 1:
            for s in (0, math.pi):
                paste_c(img, ns(34), cx + sep * math.cos(ph + s), cy + 0.6 * sep * math.sin(ph + s))
        else:
            paste_c(img, radial(500, [(0, (255, 255, 255, 255)), (0.3, (255, 230, 170, 230)), (1, (255, 180, 80, 0))]), cx, cy)
        # chirp waveform
        d = ImageDraw.Draw(img); pts = []
        for x in range(260, W - 260, 3):
            q = (x - 260) / (W - 520) * u
            amp = 10 + 110 * q ** 3; f = 6 + 120 * q ** 3
            pts.append((x, 930 + amp * math.sin(f * q * 6)))
        if len(pts) > 2: d.line(pts, fill=CORAL7, width=4)
        d.text((W / 2, 1010), "gravitational waves: the 'chirp'", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
        alpha_text(img, (W / 2, 205), "NGC 4993 · ≈ 130 million light-years away", F(40, "SemiBold"), PALE7, ease((t - 1) / 0.5))
    else:
        fb = 220 + 30 * math.sin(t * 2)
        paste_c(img, radial(int(fb * 3), [(0, (255, 250, 230, 255)), (0.25, (255, 210, 120, 230)), (0.6, (255, 120, 80, 120)), (1, (255, 80, 60, 0))]), 560, cy)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(4)
        for _ in range(140):
            a = rng.uniform(0, 2 * math.pi); sp = rng.uniform(40, 260); ph = (t * rng.uniform(0.2, 0.6) + rng.random()) % 1
            x, y = 560 + math.cos(a) * sp * (1 + ph * 2), cy + math.sin(a) * sp * (1 + ph * 2)
            dl.ellipse([x - 4, y - 4, x + 4, y + 4], fill=GOLD7 + (int(230 * (1 - ph)),))
        img.alpha_composite(lay)
        n = 10; k = int(min(n, max(0, (t - 0.8) / 0.35)))
        for i in range(n):
            x = 1150 + (i % 5) * 130; y = 470 + (i // 5) * 150
            if i < k: paste_c(img, planet_sprite(48, (255, 196, 70), light=(-0.7, -0.6)), x, y)
            else:
                d = ImageDraw.Draw(img); d.ellipse([x - 48, y - 48, x + 48, y + 48], outline=(90, 90, 110), width=3)
        d = ImageDraw.Draw(img)
        d.text((1410, 340), "Earth masses of gold + platinum", font=F(38, "Bold"), fill=GOLD7, anchor="mm")
        d.text((1410, 760), f"≈ {k}", font=F(96, "Black"), fill=GOLD7, anchor="mm")
        caption(img, "estimate: Edo Berger (Harvard), GW170817", ease((t - 3) / 0.5))

SC = {k[3:]: f for k, f in globals().items() if k.startswith("sc_")}

# ---------------- voice ----------------
def tts(scenes, outdir, voice, speed):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(HERE, "models/kokoro.onnx"), os.path.join(HERE, "models/voices.bin"))
    durs, chunks, sr = [], [], 24000
    lang = "en-us" if voice[0] == "a" else "en-gb"
    for i, s in enumerate(scenes):
        key = f"{voice}|{speed}|{s['say']}"; cache = os.path.join(outdir, "tts_" + hashlib.md5(key.encode()).hexdigest()[:12] + ".wav")
        if os.path.exists(cache) and open(cache + ".txt").read() == key:
            a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(s["say"], voice=voice, speed=speed, lang=lang)
            sf.write(cache, a, sr); open(cache + ".txt", "w").write(key)
        a = np.concatenate([np.zeros(int(sr * 0.2)), a, np.zeros(int(sr * 0.5))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
        print(f"tts {i+1}/{len(scenes)} {durs[-1]:.1f}s", flush=True)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    tt = np.arange(len(audio)) / sr
    f0 = float(os.environ.get("PAD_HZ", "55"))
    pad = (np.sin(2 * np.pi * f0 * tt) * 0.5 + np.sin(2 * np.pi * f0 * 1.5 * tt) * 0.3 + np.sin(2 * np.pi * f0 * 2.005 * tt) * 0.2)
    pad *= (0.6 + 0.4 * np.sin(2 * np.pi * 0.05 * tt)) * 0.035
    audio = (audio + pad).astype(np.float32); audio /= max(1.0, np.abs(audio).max() / 0.95)
    sf.write(os.path.join(outdir, "voice.wav"), audio, sr)
    return durs

def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"

def write_srt(scenes, durs, path):
    out, t0, n = [], 0.0, 1
    for s, d in zip(scenes, durs):
        sents = [x.strip() for x in re.split(r"(?<=[.?!])\s+", s["say"]) if x.strip()]
        total = sum(len(x) for x in sents); t = t0 + 0.2; usable = d - 0.7
        for x in sents:
            dd = usable * len(x) / total
            out.append(f"{n}\n{srt_time(t)} --> {srt_time(t + dd)}\n{x}\n"); n += 1; t += dd
        t0 += d
    open(path, "w").write("\n".join(out))

def frame(scenes, durs, gt):
    total = sum(durs); acc = 0
    for s, d in zip(scenes, durs):
        if gt < acc + d: break
        acc += d
    t = gt - acc
    img = background(gt)
    SC[s["vis"]["type"]](img, s["vis"], t, d)
    chrome(img, gt / total)
    if t < 0.3:
        img = Image.blend(background(gt), img, ease(t / 0.3))
    return img

def init():
    global SF1, SF2
    SF1 = make_starfield(W + 400, H, 1400, 1).convert("RGBA")
    SF2 = Image.new("RGBA", (W + 400, H), (0, 0, 0, 0)); d = ImageDraw.Draw(SF2); rng = random.Random(2)
    for _ in range(170):
        x, y = rng.uniform(0, W + 400), rng.uniform(0, H); r = rng.choice([1.0, 1.4, 2.0])
        c = mix((170, 190, 255), (255, 235, 210), rng.random()); d.ellipse([x - r, y - r, x + r, y + r], fill=c + (230,))

def render(scenes, durs, outdir):
    total = sum(durs)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voice.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", os.path.join(outdir, "video.mp4")]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    nf = int(total * FPS)
    for f in range(nf):
        p.stdin.write(frame(scenes, durs, f / FPS).convert("RGB").tobytes())
        if f % 900 == 0: print(f"frame {f}/{nf}", flush=True)
    p.stdin.close(); p.wait()
    src = os.path.join(outdir, "video.mp4"); dst = os.path.join(outdir, "final.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", dst], check=True)

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    voice = os.environ.get("VOICE", "af_heart"); speed = float(os.environ.get("SPEED", "1.0"))
    scenes = ep.SCENES; init()
    if "--preview" in sys.argv:
        durs = [8.0] * len(scenes)
        for i, s in enumerate(scenes):
            frame(scenes, durs, i * 8 + 5.5).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}.jpg"), quality=80)
        print("preview ok"); sys.exit()
    if "--tts" in sys.argv:
        durs = tts(scenes, outdir, voice, speed); json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
        print("total:", round(sum(durs), 1), "s"); sys.exit()
    durs = tts(scenes, outdir, voice, speed)
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
    write_srt(scenes, durs, os.path.join(outdir, "subtitles.srt"))
    print("total:", round(sum(durs), 1), "s")
    render(scenes, durs, outdir)
    print("ok")
