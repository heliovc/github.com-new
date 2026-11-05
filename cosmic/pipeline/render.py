"""Cosmic Scale pipeline: script -> voice (Kokoro offline, EN) -> code-drawn space visuals -> MP4 1080p30 + SRT.
Usage: python3 -I render.py ep01_sun.py out/ep01 [--preview]
EP02 added scenes: clock, escape, sky, thermo, energy, ocean, galaxy
EP03 added scenes: zoom, stretch, horizons, deepfield, shrink (violet/magenta palette)
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
        if p > 0.05: d.text((640 + max(4, bw) + 24, y), f"{val * p:.0f}" + v.get("suffix", ""), font=F(52, "Bold"), fill=WHITE, anchor="lm")

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
