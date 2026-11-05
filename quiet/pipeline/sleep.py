"""The Quiet Archive - calm history for sleep.
Pipeline: script (chapters -> paragraphs) -> Kokoro voice (offline, en-gb) -> ambient bed (rain + warm pad + hearth)
-> code-painted nocturnal scenes rendered as seamless loops -> concat (no re-encode) -> final.mp4 + subtitles.srt + chapters.txt

Usage:
  python3 -I sleep.py ep01_rome.py out/ep01 --preview   # one still per chapter scene (+ title card)
  python3 -I sleep.py ep01_rome.py out/ep01 --tts       # voice only (cached per paragraph) -> timeline.json
  python3 -I sleep.py ep01_rome.py out/ep01             # full build
Env: VOICE (default bm_george), SPEED (default 0.80)

Identity (keep distinct from the other channels): warm candle/moonlight palette, Lora serif, no captions on screen,
slow loops, quiet mix (-19 LUFS), long ambient tail. Each episode may override PALETTE and pick scene types.
Scene types: city, road, temple, interior, sea, hills.
"""
import sys, os, re, math, json, hashlib, subprocess, importlib.util, random
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 12
LOOP_S = 32
INTRO_S = 16
HERE = os.path.dirname(os.path.abspath(__file__))
FD = "/usr/share/fonts/truetype/google-fonts/"
BRAND = "THE QUIET ARCHIVE"

_fc = {}
def F(size, wght=400, italic=False):
    k = (int(size), wght, italic)
    if k not in _fc:
        f = ImageFont.truetype(FD + ("Lora-Italic-Variable.ttf" if italic else "Lora-Variable.ttf"), int(size))
        try: f.set_variation_by_axes([wght])
        except Exception: pass
        _fc[k] = f
    return _fc[k]

PAL = dict(sky_top=(9, 8, 20), sky_mid=(30, 22, 38), horizon=(128, 80, 58), moon=(247, 230, 196),
           far=(66, 44, 48), mid=(33, 23, 28), near=(12, 9, 11), light=(255, 176, 92), ember=(255, 150, 72),
           text=(240, 226, 200), accent=(214, 178, 116), sea=(18, 22, 36))

def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): t = max(0.0, min(1.0, t)); return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))
def smooth(x): x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)
TAU = 2 * math.pi

# ---------------------------------------------------------------- painting helpers
def gradient_sky(p, horizon_y):
    y = np.arange(H, dtype=np.float32)[:, None]
    top, mid, hor = [np.array(p[k], np.float32) for k in ("sky_top", "sky_mid", "horizon")]
    t1 = np.clip(y / (horizon_y * 0.62), 0, 1)
    t2 = np.clip((y - horizon_y * 0.62) / (horizon_y * 0.38), 0, 1) ** 1.6
    c = top * (1 - t1) + mid * t1
    c = c * (1 - t2) + hor * t2
    c = np.repeat(c[:, None, :], W, axis=1)
    return c

def radial_glow(cx, cy, r, col, strength):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    g = np.exp(-d * d) * strength
    return g[..., None] * np.array(col, np.float32)[None, None, :]

def noise1d(n, seed, octaves=5, base=6):
    rng = np.random.default_rng(seed); out = np.zeros(n, np.float32)
    for k in range(octaves):
        pts = base * 2 ** k
        v = rng.uniform(-1, 1, pts + 1)
        out += np.interp(np.linspace(0, pts, n), np.arange(pts + 1), v) / (1.9 ** k)
    return out

def poly_layer(points, col, blur=0):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.polygon(points, fill=col + (255,))
    return lay.filter(ImageFilter.GaussianBlur(blur)) if blur else lay

def hills(y0, amp, seed, col, blur=0, base=4):
    n = noise1d(W + 1, seed, 4, base)
    pts = [(x, y0 + n[x] * amp) for x in range(0, W + 1, 4)] + [(W, H), (0, H)]
    return poly_layer(pts, col, blur)

def cypress(d, x, base, h, col):
    w = h * 0.13
    pts = [(x, base - h)]
    for i in range(1, 9):
        f = i / 8; yy = base - h + h * f
        ww = w * math.sin(min(1, f * 1.25) * math.pi * 0.62) * (0.9 + 0.1 * math.sin(i * 2.3))
        pts.append((x + ww, yy))
    pts.append((x + w * 0.15, base)); pts.append((x - w * 0.15, base))
    for i in range(8, 0, -1):
        f = i / 8; yy = base - h + h * f
        ww = w * math.sin(min(1, f * 1.25) * math.pi * 0.62) * (0.9 + 0.1 * math.cos(i * 1.7))
        pts.append((x - ww, yy))
    d.polygon(pts, fill=col + (255,))

def stone_pine(d, x, base, h, col, rng):
    d.line([(x, base), (x + h * 0.05, base - h * 0.75)], fill=col + (255,), width=max(2, int(h * 0.035)))
    cx, cy = x + h * 0.05, base - h * 0.8
    for _ in range(9):
        ox = rng.uniform(-h * 0.42, h * 0.42); oy = rng.uniform(-h * 0.1, h * 0.05)
        rx = rng.uniform(h * 0.14, h * 0.24); ry = rx * 0.38
        d.ellipse([cx + ox - rx, cy + oy - ry, cx + ox + rx, cy + oy + ry], fill=col + (255,))

def buildings(d, x0, x1, base, rng, col, scale=1.0, windows=None, domes=True, cols_=True):
    x = x0
    while x < x1:
        bw = rng.uniform(70, 190) * scale; bh = rng.uniform(60, 190) * scale
        kind = rng.random()
        d.rectangle([x, base - bh, x + bw, base], fill=col + (255,))
        if kind < 0.55:  # low-pitched tiled roof
            d.polygon([(x - 6 * scale, base - bh), (x + bw / 2, base - bh - bw * 0.16), (x + bw + 6 * scale, base - bh)], fill=col + (255,))
        elif kind < 0.7 and domes:
            r = bw * 0.38; d.pieslice([x + bw / 2 - r, base - bh - r, x + bw / 2 + r, base - bh + r], 180, 360, fill=col + (255,))
        elif kind < 0.8 and cols_:  # small temple front
            d.polygon([(x - 4, base - bh), (x + bw / 2, base - bh - bw * 0.22), (x + bw + 4, base - bh)], fill=col + (255,))
        if windows is not None:
            for _ in range(int(rng.integers(0, 3))):
                wx = x + rng.uniform(0.15, 0.8) * bw; wy = base - rng.uniform(0.25, 0.85) * bh
                windows.append((wx, wy, 5 * scale, 8 * scale, rng.uniform(0, TAU), int(rng.integers(1, 4))))
        x += bw + rng.uniform(-10, 25) * scale

def aqueduct(lay, y_top, height, col, x0=0, x1=W, span=110, tiers=2):
    d = ImageDraw.Draw(lay)
    d.rectangle([x0, y_top, x1, y_top + height], fill=col + (255,))
    th = height / tiers
    for t in range(tiers):
        sp = span / (1 + t * 0.0)
        top = y_top + t * th + th * 0.22
        x = x0 + sp * 0.18
        while x + sp * 0.64 < x1:
            aw = sp * 0.64
            d.rectangle([x, top + aw / 2, x + aw, y_top + (t + 1) * th - 2], fill=(0, 0, 0, 0))
            d.pieslice([x, top, x + aw, top + aw], 180, 360, fill=(0, 0, 0, 0))
            x += sp

# ---------------------------------------------------------------- scenes
class Scene:
    """Static layers + animated parts, all periodic in LOOP_S so loops are seamless."""
    def __init__(self, kind, p, seed):
        self.kind, self.p, self.rng = kind, p, np.random.default_rng(seed)
        self.windows, self.stars_tw, self.lamp, self.reflect = [], [], None, None
        self.particles = "embers"; self.fog_y = 0.72 * H; self.fog_a = 0.22
        getattr(self, "build_" + kind)()
        self.prepare()

    def sky(self, hy, moon=(0.72, 0.2), moon_r=46):
        p = self.p; c = gradient_sky(p, hy)
        mx, my = moon[0] * W, moon[1] * H
        c += radial_glow(mx, my, moon_r * 7, p["moon"], 0.10)
        c += radial_glow(mx, my, moon_r * 2.2, p["moon"], 0.22)
        img = Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).convert("RGBA")
        d = ImageDraw.Draw(img)
        rng = self.rng
        for _ in range(260):
            x, y = rng.uniform(0, W), rng.uniform(0, hy * 0.85)
            b = rng.uniform(0.15, 0.7) ** 2
            if math.hypot(x - mx, y - my) < moon_r * 3: continue
            col = mix(p["sky_top"], (235, 228, 210), b)
            if rng.random() < 0.15: self.stars_tw.append((x, y, b, rng.uniform(0, TAU), int(rng.integers(1, 4))))
            else: d.point((x, y), fill=col + (255,))
        # moon disc with soft craters
        mr = moon_r; ms = Image.new("RGBA", (mr * 2 + 4, mr * 2 + 4), (0, 0, 0, 0)); md = ImageDraw.Draw(ms)
        md.ellipse([2, 2, mr * 2 + 2, mr * 2 + 2], fill=p["moon"] + (255,))
        for _ in range(7):
            cx, cy, rr = rng.uniform(mr * 0.5, mr * 1.5), rng.uniform(mr * 0.5, mr * 1.5), rng.uniform(mr * 0.08, mr * 0.22)
            md.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=mix(p["moon"], (170, 150, 130), 0.35) + (255,))
        ms = ms.filter(ImageFilter.GaussianBlur(1.2))
        img.alpha_composite(ms, (int(mx - mr - 2), int(my - mr - 2)))
        self.moon = (mx, my, mr)
        return img

    # --- kinds
    def build_city(self):
        p, rng = self.p, self.rng; hy = int(H * 0.66)
        self.back = self.sky(hy, (0.74, 0.19))
        far = hills(hy - 40, 50, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.25), blur=2)
        self.back.alpha_composite(far)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        r2 = random.Random(int(rng.integers(1e6)))
        buildings(d, -40, W + 40, hy + 70, rng, p["mid"], 1.0, self.windows)
        d.rectangle([0, hy + 70, W, H], fill=p["mid"] + (255,))
        for _ in range(7): cypress(d, r2.uniform(0, W), hy + 70, r2.uniform(130, 220), p["mid"])
        aq = Image.new("RGBA", (W, H), (0, 0, 0, 0)); aqueduct(aq, hy - 70, 120, mix(p["far"], p["mid"], 0.55), 0, W * 0.62, 120)
        self.mid = Image.alpha_composite(aq, mid)
        near = hills(H - 150, 30, int(rng.integers(1e6)), p["near"])
        dn = ImageDraw.Draw(near)
        for x in (90, 1780): stone_pine(dn, x, H - 120, 330, p["near"], r2)
        self.near = near; self.fog_y = hy + 20

    def build_road(self):
        p, rng = self.p, self.rng; hy = int(H * 0.62)
        self.back = self.sky(hy, (0.3, 0.22), 40)
        self.back.alpha_composite(hills(hy - 20, 35, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.35), blur=3))
        mid = hills(hy + 30, 18, int(rng.integers(1e6)), p["mid"]); d = ImageDraw.Draw(mid)
        r2 = random.Random(int(rng.integers(1e6)))
        vx = W * 0.56  # vanishing point of the road
        for i in range(9):  # tombs and pines receding along the road
            f = (i + 1) / 10; s = 0.25 + f ** 1.6 * 1.6
            for side in (-1, 1):
                x = vx + side * (40 + f ** 1.7 * 900); base = hy + 30 + f ** 1.6 * 300
                if r2.random() < 0.5: stone_pine(d, x, base, 120 * s, p["mid"], r2)
                else:
                    d.rectangle([x - 22 * s, base - 46 * s, x + 22 * s, base], fill=p["mid"] + (255,))
                    d.ellipse([x - 24 * s, base - 66 * s, x + 24 * s, base - 30 * s], fill=p["mid"] + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near)
        dn.polygon([(vx - 10, hy + 32), (vx + 10, hy + 32), (W * 0.95, H), (W * 0.05, H)], fill=mix(p["mid"], p["horizon"], 0.18) + (255,))
        for k in range(14):  # paving stones catching moonlight
            f = (k + 1) / 15; y = hy + 32 + f ** 2 * (H - hy - 32); hw = 10 + f ** 2 * (W * 0.45)
            dn.line([(vx - hw, y), (vx + hw, y)], fill=mix(p["mid"], p["moon"], 0.08) + (255,), width=1 + int(f * 2))
        dn.polygon([(0, H - 60), (W * 0.18, H - 120), (W * 0.22, H)], fill=p["near"] + (255,))
        stone_pine(dn, 120, H - 40, 420, p["near"], r2); cypress(dn, W - 140, H, 520, p["near"])
        self.near = near; self.fog_y = hy + 60; self.particles = "fireflies"

    def build_temple(self):
        p, rng = self.p, self.rng; hy = int(H * 0.7)
        self.back = self.sky(hy, (0.5, 0.24), 52)
        self.back.alpha_composite(hills(hy - 30, 40, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.3), blur=3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        buildings(d, -20, W + 20, hy + 40, rng, p["mid"], 0.8, self.windows)
        d.rectangle([0, hy + 40, W, H], fill=p["mid"] + (255,))
        # distant temple on a podium, centre
        cx, base = W * 0.5, hy + 10; tw = 360
        d.rectangle([cx - tw / 2 - 20, base - 30, cx + tw / 2 + 20, base + 30], fill=p["mid"] + (255,))
        for i in range(7):
            x = cx - tw / 2 + i * tw / 6; d.rectangle([x - 9, base - 190, x + 9, base - 30], fill=p["mid"] + (255,))
        d.rectangle([cx - tw / 2 - 14, base - 214, cx + tw / 2 + 14, base - 188], fill=p["mid"] + (255,))
        d.polygon([(cx - tw / 2 - 18, base - 214), (cx, base - 280), (cx + tw / 2 + 18, base - 214)], fill=p["mid"] + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near)
        col = p["near"]
        for x in (150, 360, W - 360, W - 150):  # foreground colonnade framing the view
            dn.rectangle([x - 44, 90, x + 44, H], fill=col + (255,))
            dn.rectangle([x - 62, 60, x + 62, 96], fill=col + (255,)); dn.rectangle([x - 60, H - 70, x + 60, H], fill=col + (255,))
            for k in range(-3, 4): dn.line([(x + k * 11, 100), (x + k * 11, H - 70)], fill=mix(col, p["mid"], 0.4) + (255,), width=2)
        dn.rectangle([0, 0, W, 64], fill=col + (255,))
        dn.rectangle([0, H - 40, W, H], fill=col + (255,))
        self.near = near; self.fog_y = hy + 30; self.fog_a = 0.16

    def build_interior(self):
        p, rng = self.p, self.rng
        wall = np.zeros((H, W, 3), np.float32) + np.array(mix(p["near"], p["mid"], 0.55), np.float32)
        # window in the wall shows the night sky
        sky = self.sky(int(H * 0.62), (0.5, 0.3), 30)
        win = Image.new("L", (W, H), 0); dw = ImageDraw.Draw(win)
        wx0, wx1, wy0, wy1 = W * 0.36, W * 0.64, H * 0.12, H * 0.62
        dw.rectangle([wx0, wy0 + (wx1 - wx0) / 2, wx1, wy1], fill=255); dw.pieslice([wx0, wy0, wx1, wy0 + (wx1 - wx0)], 180, 360, fill=255)
        hill = hills(int(H * 0.56), 22, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.2), blur=2)
        r2 = random.Random(int(rng.integers(1e6))); dh = ImageDraw.Draw(hill)
        for _ in range(4): cypress(dh, r2.uniform(wx0, wx1), H * 0.6, r2.uniform(70, 120), p["mid"])
        sky.alpha_composite(hill)
        base = Image.fromarray(wall.astype(np.uint8)).convert("RGBA")
        base.paste(sky, (0, 0), win)
        self.stars_tw = [s for s in self.stars_tw if wx0 < s[0] < wx1 and wy0 + 40 < s[1] < wy1]
        self.back = base
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(near)
        col = p["near"]
        d.rectangle([0, H * 0.78, W, H], fill=col + (255,))  # table
        d.rectangle([W * 0.06, H * 0.2, W * 0.24, H * 0.78], fill=mix(col, p["mid"], 0.25) + (255,))  # shelf of scrolls
        for r in range(5):
            y = H * 0.24 + r * H * 0.1
            d.line([(W * 0.06, y + H * 0.085), (W * 0.24, y + H * 0.085)], fill=col + (255,), width=6)
            for k in range(7):
                cx = W * 0.075 + k * W * 0.024
                d.ellipse([cx - 16, y + 40, cx + 16, y + 76], fill=mix(col, p["accent"], 0.18 + 0.05 * (k % 3)) + (255,))
        # oil lamp
        lx, ly = W * 0.7, H * 0.78
        d.ellipse([lx - 70, ly - 34, lx + 70, ly + 4], fill=mix(col, p["accent"], 0.22) + (255,))
        d.polygon([(lx + 60, ly - 22), (lx + 104, ly - 30), (lx + 100, ly - 18)], fill=mix(col, p["accent"], 0.22) + (255,))
        d.rectangle([W * 0.46, H * 0.74, W * 0.6, H * 0.78], fill=mix(col, p["accent"], 0.12) + (255,))  # a scroll on the table
        self.lamp = (lx + 102, ly - 36)
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); self.near = near
        self.particles = "dust"; self.fog_a = 0

    def build_sea(self):
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy, (0.62, 0.2), 48)
        sea = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(sea)
        for y in range(hy, H):
            f = (y - hy) / (H - hy); d.line([(0, y), (W, y)], fill=mix(mix(p["sea"], p["horizon"], 0.35), p["sea"], f ** 0.5) + (255,))
        self.back.alpha_composite(sea)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        # far headland with lighthouse
        d.polygon([(W * 0.0, hy), (W * 0.05, hy - 60), (W * 0.2, hy - 40), (W * 0.28, hy)], fill=mix(p["far"], p["mid"], 0.4) + (255,))
        lx = W * 0.12; d.rectangle([lx - 14, hy - 150, lx + 14, hy - 50], fill=mix(p["far"], p["mid"], 0.4) + (255,))
        self.windows.append((lx, hy - 160, 9, 10, 0.0, 1))
        # merchant ship with square sail
        sx, sy = W * 0.36, hy + 14
        d.polygon([(sx - 120, sy - 20), (sx + 120, sy - 20), (sx + 90, sy + 14), (sx - 96, sy + 14)], fill=p["mid"] + (255,))
        d.line([(sx, sy - 20), (sx, sy - 190)], fill=p["mid"] + (255,), width=5)
        d.polygon([(sx - 80, sy - 175), (sx + 80, sy - 175), (sx + 74, sy - 60), (sx - 74, sy - 60)], fill=mix(p["mid"], p["far"], 0.4) + (255,))
        d.polygon([(sx + 120, sy - 20), (sx + 150, sy - 70), (sx + 135, sy - 18)], fill=p["mid"] + (255,))
        self.windows.append((sx - 60, sy - 6, 4, 4, 1.0, 2))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near)
        dn.polygon([(W * 0.62, H), (W * 0.7, H - 140), (W * 0.84, H - 170), (W, H - 210), (W, H)], fill=p["near"] + (255,))
        for k in range(10):  # harbour mole with bollards
            x = W * 0.72 + k * 52; dn.rectangle([x, H - 190 - k * 4, x + 14, H - 160 - k * 4], fill=p["near"] + (255,))
        r2 = random.Random(int(rng.integers(1e6))); cypress(dn, W * 0.93, H - 180, 300, p["near"])
        self.near = near
        mx, my, mr = self.moon
        self.reflect = (mx, hy + 4, mr)
        self.fog_y = hy - 10; self.fog_a = 0.12

    def build_hills(self):
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy, (0.22, 0.2), 44)
        for i, (y, a, b) in enumerate([(hy - 30, 60, 0.5), (hy + 30, 50, 0.3)]):
            self.back.alpha_composite(hills(y, a, int(rng.integers(1e6)), mix(p["far"], p["horizon"], b), blur=3 - i))
        mid = hills(hy + 110, 45, int(rng.integers(1e6)), p["mid"]); d = ImageDraw.Draw(mid)
        r2 = random.Random(int(rng.integers(1e6)))
        vx, vy = W * 0.62, hy + 70  # villa on the slope
        d.rectangle([vx - 130, vy - 60, vx + 130, vy + 40], fill=p["mid"] + (255,))
        d.polygon([(vx - 140, vy - 60), (vx, vy - 96), (vx + 140, vy - 60)], fill=p["mid"] + (255,))
        for k in range(3): self.windows.append((vx - 80 + k * 70, vy - 25, 7, 11, k * 1.3, k + 1))
        for _ in range(9): cypress(d, r2.uniform(0, W), hy + 140 + r2.uniform(-20, 40), r2.uniform(90, 160), p["mid"])
        self.mid = mid
        near = hills(H - 120, 40, int(rng.integers(1e6)), p["near"]); dn = ImageDraw.Draw(near)
        stone_pine(dn, W * 0.08, H - 90, 380, p["near"], r2); cypress(dn, W * 0.9, H - 60, 460, p["near"])
        self.near = near; self.fog_y = hy + 120; self.particles = "fireflies"

    # --- per-frame
    def prepare(self):
        p = self.p
        fx = np.arange(W * 2, dtype=np.float32)
        band = sum(np.sin(fx * TAU / (W / k) + k * 1.7) / k for k in (1, 2, 3, 5)) * 0.25 + 0.6
        yy = np.arange(H, dtype=np.float32)
        prof = np.exp(-((yy - self.fog_y) / 90.0) ** 2)
        a = np.clip(prof[:, None] * band[None, :], 0, 1) * self.fog_a * 255
        fog = np.zeros((H, W * 2, 4), np.uint8); fog[..., :3] = mix(p["horizon"], p["moon"], 0.35); fog[..., 3] = a.astype(np.uint8)
        self.fog = Image.fromarray(fog, "RGBA")
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        v = 1 - np.clip(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2, 0, 1) ** 1.5 * 0.0
        r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        vig = np.clip(1 - (r - 0.55) * 0.75, 0.35, 1)
        self.vig = Image.fromarray((vig * 255).astype(np.uint8), "L")
        rng = np.random.default_rng(7)
        n = {"embers": 26, "fireflies": 22, "dust": 34}[self.particles]
        self.parts = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0, TAU), int(rng.integers(1, 3)), rng.uniform(0.4, 1.0)) for _ in range(n)]
        self.glow_sm = self._glow(16); self.glow_lg = self._glow(90)

    def _glow(self, r):
        s = r * 2; yy, xx = np.mgrid[0:s, 0:s].astype(np.float32)
        d = np.sqrt((xx - r) ** 2 + (yy - r) ** 2) / r
        a = np.clip(np.exp(-d * d * 3.2) - 0.02, 0, 1)
        img = np.zeros((s, s, 4), np.uint8); img[..., :3] = 255; img[..., 3] = (a * 255).astype(np.uint8)
        return Image.fromarray(img, "RGBA")

    def tint(self, spr, col, a):
        s = spr.copy(); s2 = Image.new("RGBA", s.size, col + (0,)); s2.putalpha(s.getchannel("A").point(lambda v: int(v * a)))
        return s2

    def frame(self, t):
        p = self.p; ph = TAU * t / LOOP_S
        img = self.back.copy(); d = ImageDraw.Draw(img)
        for x, y, b, f, k in self.stars_tw:
            bb = b * (0.55 + 0.45 * math.sin(ph * k + f))
            d.point((x, y), fill=mix(p["sky_top"], (240, 232, 214), bb) + (255,))
            if b > 0.3: d.point((x + 1, y), fill=mix(p["sky_top"], (240, 232, 214), bb * 0.6) + (255,))
        if self.reflect:
            mx, ry, mr = self.reflect; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            for i in range(26):
                y = ry + 6 + i * 13; hw = mr * (0.6 + i * 0.09) * (0.65 + 0.35 * math.sin(ph * (1 + i % 3) + i * 1.9))
                off = 14 * math.sin(ph * 2 + i * 0.8)
                dl.line([(mx - hw + off, y), (mx + hw + off, y)], fill=p["moon"] + (int(120 - i * 3.6),), width=3)
            img.alpha_composite(lay)
        if self.fog_a:
            off = int(W / 2 + 160 * math.sin(ph))
            img.alpha_composite(self.fog.crop((off, 0, off + W, H)))
        img.alpha_composite(self.mid)
        if self.windows:
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            for x, y, w, h, f, k in self.windows:
                fl = 0.78 + 0.22 * math.sin(ph * k * 3 + f) * math.sin(ph * k + f * 2)
                lay.alpha_composite(self.tint(self.glow_sm, p["light"], 0.35 * fl), (int(x - 16), int(y - 16)))
                dl.rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], fill=mix(p["mid"], p["light"], fl) + (255,))
            img.alpha_composite(lay)
        img.alpha_composite(self.near)
        if self.lamp:
            lx, ly = self.lamp; fl = 0.85 + 0.1 * math.sin(ph * 5) + 0.05 * math.sin(ph * 13 + 1)
            g = self.tint(self.glow_lg.resize((900, 900)), p["light"], 0.33 * fl); img.alpha_composite(g, (int(lx - 450), int(ly - 450)))
            dl = ImageDraw.Draw(img); fh = 30 * fl
            dl.polygon([(lx - 8, ly), (lx, ly - fh), (lx + 8, ly), (lx, ly + 6)], fill=(255, 214, 140, 255))
            dl.polygon([(lx - 4, ly), (lx, ly - fh * 0.6), (lx + 4, ly)], fill=(255, 246, 220, 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for x0, y0, f, k, s in self.parts:
            if self.particles == "embers":
                y = (y0 - (H + 60) * t / LOOP_S * k) % (H + 60) - 30; x = x0 + 30 * math.sin(ph * 2 + f)
                a = 0.55 * s * (0.6 + 0.4 * math.sin(ph * 4 + f)) * min(1, y / (H * 0.4)); col = p["ember"]; sz = 4 + 3 * s
            elif self.particles == "fireflies":
                x = x0 + 60 * math.sin(ph * k + f); y = H * 0.55 + (y0 % (H * 0.45)) + 30 * math.cos(ph * (3 - k) + f)
                a = max(0, math.sin(ph * 3 * k + f)) ** 2 * 0.8 * s; col = (230, 240, 160); sz = 4 + 2 * s
            else:
                x = x0 + 40 * math.sin(ph + f); y = (y0 + (H + 40) * t / LOOP_S) % (H + 40) - 20
                a = 0.22 * s; col = p["accent"]; sz = 2 + 2 * s
            if a <= 0.01: continue
            g = self.tint(self.glow_sm.resize((int(sz * 4), int(sz * 4))), col, a)
            lay.alpha_composite(g, (int(x - sz * 2), int(y - sz * 2)))
        img.alpha_composite(lay)
        dark = Image.new("RGBA", (W, H), (0, 0, 0, 255)); dark.putalpha(self.vig.point(lambda v: 255 - v))
        img.alpha_composite(dark)
        return img

# ---------------------------------------------------------------- text overlays
def brand(img, a=0.42, p=PAL):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = F(22, 500); x, y = 60, H - 56
    txt = " ".join(BRAND)
    d.text((x, y), txt, font=f, fill=p["accent"] + (int(255 * a),), anchor="lm")
    img.alpha_composite(lay)

def title_card(img, kicker, title, a, big=False, p=PAL):
    if a <= 0: return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    shade = Image.new("RGBA", (W, H), (0, 0, 0, int(110 * a))); img.alpha_composite(shade)
    cy = H * 0.44
    d.text((W / 2, cy - (110 if big else 80)), " ".join(kicker.upper()), font=F(30, 500), fill=p["accent"] + (int(255 * a),), anchor="mm")
    lines = wrap(title, F(96 if big else 78, 400, True), W * 0.78)
    fs = F(96 if big else 78, 400, True); lh = (110 if big else 92)
    y = cy + 10 - (len(lines) - 1) * lh / 2
    for ln in lines:
        d.text((W / 2 + 3, y + 4), ln, font=fs, fill=(0, 0, 0, int(150 * a)), anchor="mm")
        d.text((W / 2, y), ln, font=fs, fill=p["text"] + (int(255 * a),), anchor="mm"); y += lh
    yl = y - lh / 2 + 40
    d.line([(W / 2 - 120, yl), (W / 2 - 18, yl)], fill=p["accent"] + (int(200 * a),), width=2)
    d.line([(W / 2 + 18, yl), (W / 2 + 120, yl)], fill=p["accent"] + (int(200 * a),), width=2)
    d.regular_polygon((W / 2, yl, 7), 4, fill=p["accent"] + (int(220 * a),))
    img.alpha_composite(lay)

def wrap(txt, font, maxw):
    words, lines, cur = txt.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) > maxw and cur: lines.append(cur); cur = w
        else: cur = t
    return lines + [cur] if cur else lines

ROMAN = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]

# ---------------------------------------------------------------- audio
def tts_all(ep, outdir, voice, speed):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(HERE, "models/kokoro.onnx"), os.path.join(HERE, "models/voices.bin"))
    lang = "en-us" if voice[0] == "a" else "en-gb"
    os.makedirs(os.path.join(outdir, "tts"), exist_ok=True)
    items, n = [], sum(len(c["paras"]) for c in ep.CHAPTERS); i = 0
    for ci, ch in enumerate(ep.CHAPTERS):
        for pi, para in enumerate(ch["paras"]):
            key = f"{voice}|{speed}|{para}"; path = os.path.join(outdir, "tts", hashlib.md5(key.encode()).hexdigest()[:14] + ".wav")
            if not os.path.exists(path):
                a, sr = k.create(para, voice=voice, speed=speed, lang=lang)
                a = a / max(1e-6, np.abs(a).max()) * 0.8
                sf.write(path, a.astype(np.float32), sr)
            i += 1; dur = sf.info(path).duration
            items.append(dict(ch=ci, para=pi, path=path, dur=dur, text=para))
            print(f"tts {i}/{n} {dur:.1f}s", flush=True)
    return items

def timeline(ep, items):
    """Chapter = INTRO_S of title (voice starts at 5 s) ... paragraphs with gaps ... 3 s rest."""
    t, chapters, segs = 0.0, [], []
    for ci, ch in enumerate(ep.CHAPTERS):
        start = t; t += 5.0 if ci else 7.0
        for it in [x for x in items if x["ch"] == ci]:
            segs.append(dict(start=t, **it)); t += it["dur"] + float(getattr(ep, "PARA_GAP", 1.3))
        t = max(t + 3.0, start + INTRO_S + 2)
        chapters.append(dict(start=start, end=t, title=ch["title"], scene=ch["scene"]))
    tail = float(getattr(ep, "TAIL_MIN", 10)) * 60
    chapters.append(dict(start=t, end=t + tail, title="Rest", scene=getattr(ep, "TAIL_SCENE", "hills"), tail=True))
    return chapters, segs, t + tail

def write_srt(segs, path):
    out, n = [], 1
    for s in segs:
        sents = [x.strip() for x in re.split(r"(?<=[.?!;])\s+", s["text"]) if x.strip()]
        total = sum(len(x) for x in sents); t = s["start"]
        for x in sents:
            dd = s["dur"] * len(x) / total
            out.append(f"{n}\n{ts(t)} --> {ts(t + dd)}\n{x}\n"); n += 1; t += dd
    open(path, "w").write("\n".join(out))

def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"

def mmss(x):
    x = int(x); h, m, s = x // 3600, x % 3600 // 60, x % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def mix_audio(segs, total, outdir, tail_start):
    from scipy.signal import lfilter
    sr = 24000; N = int(total * sr) + sr; chunk = sr * 30
    rng = np.random.default_rng(3)
    zi_b = np.zeros(1); zi_l = np.zeros(2)
    path = os.path.join(outdir, "mix.wav")
    seg_cache = {}
    with sf.SoundFile(path, "w", sr, 1, "PCM_16") as fo:
        for c0 in range(0, N, chunk):
            n = min(chunk, N - c0); tt = (np.arange(n) + c0) / sr
            w = rng.standard_normal(n)
            brown, zi_b = lfilter([1.0], [1, -0.997], w, zi=zi_b)  # rain/wind bed
            brown, zi_l = lfilter([0.06, 0.06], [1, -0.88], brown, zi=zi_l)
            bed = brown * 0.012 * (0.85 + 0.15 * np.sin(TAU * tt / 41))
            pad = np.zeros(n)
            for f, a in ((110.0, 0.5), (164.81, 0.32), (220.0, 0.22), (277.18, 0.12)):  # warm A-major, very soft
                pad += a * np.sin(TAU * f * tt + f) * (0.6 + 0.4 * np.sin(TAU * tt / (23 + f % 7)))
            pad *= 0.010
            crack = (rng.random(n) < 0.00035) * rng.uniform(-1, 1, n) * 0.05  # distant hearth
            crack = lfilter([1, -0.6], [1], crack)
            y = bed + pad + crack
            fade = np.clip((tail_start + 600 - tt) / 60, 0, 1) if total - tail_start > 120 else 1.0
            y = y * np.where(tt > total - 60, np.clip((total - tt) / 60, 0, 1), 1.0)
            for s in segs:
                s0 = int(s["start"] * sr); s1 = s0 + int(s["dur"] * sr)
                if s1 <= c0 or s0 >= c0 + n: continue
                if s["path"] not in seg_cache:
                    seg_cache.clear(); seg_cache[s["path"]] = sf.read(s["path"], dtype="float32")[0]
                a = seg_cache[s["path"]]
                lo, hi = max(s0, c0), min(s0 + len(a), c0 + n)
                y[lo - c0:hi - c0] += a[lo - s0:hi - s0]
            fo.write(np.clip(y, -1, 1).astype(np.float32))
    return path

# ---------------------------------------------------------------- video
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "27", "-tune", "stillimage", "-pix_fmt", "yuv420p", "-g", str(FPS * 8), "-r", str(FPS)]

def encode(frames_iter, nframes, path):
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + ENC + [path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(nframes): p.stdin.write(next(frames_iter).convert("RGB").tobytes())
    p.stdin.close(); p.wait()

def build_video(ep, chapters, outdir, pal):
    vd = os.path.join(outdir, "v"); os.makedirs(vd, exist_ok=True)
    scenes, lst = {}, []
    for ci, ch in enumerate(chapters):
        key = (ch["scene"], ci % 2 if not ch.get("tail") else 9)
        if key not in scenes: scenes[key] = Scene(ch["scene"], pal, 100 + len(scenes) * 17 + getattr(ep, "SEED", 0))
        sc = scenes[key]; dur = ch["end"] - ch["start"]
        loop = os.path.join(vd, f"loop_{ch['scene']}_{key[1]}.mp4")
        if not os.path.exists(loop):
            def gen():
                for f in range(LOOP_S * FPS):
                    im = sc.frame(f / FPS); brand(im, p=pal); yield im
            encode(gen(), LOOP_S * FPS, loop); print("loop", loop, flush=True)
        intro_len = 0
        if not ch.get("tail"):
            intro = os.path.join(vd, f"intro_{ci:02d}.mp4")
            kick = getattr(ep, "KICKER", "The Quiet Archive") if ci == 0 else f"Chapter {ROMAN[ci - 1] if ci else ''}"
            ttl = ep.TITLE if ci == 0 else ch["title"]
            if ci == 0: kick = ep.KICKER
            def gen_i():
                for f in range(INTRO_S * FPS):
                    t = f / FPS; im = sc.frame(t % LOOP_S); brand(im, p=pal)
                    a = smooth((t - 1.0) / 2.5) * (1 - smooth((t - (INTRO_S - 4)) / 3.5))
                    title_card(im, kick, ttl, a, big=(ci == 0), p=pal); yield im
            if not os.path.exists(intro): encode(gen_i(), INTRO_S * FPS, intro)
            lst.append(intro); intro_len = INTRO_S
            # second half of the loop so the cut after the intro is seamless: intro covers t in [0,16) -> continue at 16
            half = os.path.join(vd, f"half_{ch['scene']}_{key[1]}.mp4")
            if not os.path.exists(half):
                def gen_h():
                    for f in range((LOOP_S - INTRO_S) * FPS):
                        im = sc.frame(INTRO_S + f / FPS); brand(im, p=pal); yield im
                encode(gen_h(), (LOOP_S - INTRO_S) * FPS, half)
            lst.append(half); intro_len = LOOP_S
        rest = dur - intro_len
        nloops = int(rest // LOOP_S); rem = rest - nloops * LOOP_S
        lst += [loop] * nloops
        if rem > 0.5:
            part = os.path.join(vd, f"part_{ci:02d}.mp4"); nf = int(round(rem * FPS))
            last = ch.get("tail")
            def gen_p():
                for f in range(nf):
                    im = sc.frame(f / FPS); brand(im, p=pal)
                    if last:
                        k = 1 - smooth((f / FPS - (rem - 20)) / 18); blk = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - k)))); im.alpha_composite(blk)
                    yield im
            encode(gen_p(), nf, part); lst.append(part)
        print(f"chapter {ci} {mmss(dur)} -> {nloops} loops", flush=True)
    listf = os.path.join(vd, "list.txt")
    open(listf, "w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in lst))
    return listf

def preview(ep, outdir, pal):
    for ci, ch in enumerate(ep.CHAPTERS + [dict(title="Rest", scene=getattr(ep, "TAIL_SCENE", "hills"))]):
        sc = Scene(ch["scene"], pal, 100 + ci * 17 + getattr(ep, "SEED", 0)); im = sc.frame(9.3); brand(im, p=pal)
        if ci == 0: title_card(im, ep.KICKER, ep.TITLE, 1, True, p=pal)
        elif ci < len(ep.CHAPTERS): title_card(im, f"Chapter {ROMAN[ci - 1]}", ch["title"], 1, p=pal)
        im.convert("RGB").save(os.path.join(outdir, f"prev_{ci:02d}_{ch['scene']}.jpg"), quality=82)
    print("preview ok")

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    pal = dict(PAL); pal.update(getattr(ep, "PALETTE", {}))
    voice = os.environ.get("VOICE", getattr(ep, "VOICE", "bm_george")); speed = float(os.environ.get("SPEED", getattr(ep, "SPEED", 0.80)))
    if "--preview" in sys.argv: preview(ep, outdir, pal); sys.exit()
    items = tts_all(ep, outdir, voice, speed)
    chapters, segs, total = timeline(ep, items)
    json.dump(dict(chapters=chapters, total=total), open(os.path.join(outdir, "timeline.json"), "w"), indent=1)
    write_srt(segs, os.path.join(outdir, "subtitles.srt"))
    open(os.path.join(outdir, "chapters.txt"), "w").write("".join(f"{mmss(c['start'])} {c['title']}\n" for c in chapters))
    words = sum(len(c.split()) for ch in ep.CHAPTERS for c in ch["paras"])
    print(f"words {words} | narration ends {mmss(chapters[-1]['start'])} | total {mmss(total)}")
    if "--tts" in sys.argv: sys.exit()
    tail_start = chapters[-1]["start"]
    mix_audio(segs, total, outdir, tail_start); print("audio mixed", flush=True)
    listf = build_video(ep, chapters, outdir, pal)
    silent = os.path.join(outdir, "silent.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", listf, "-c", "copy", silent], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", os.path.join(outdir, "mix.wav"),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-19:TP=-2:LRA=9", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "96k", "-ac", "1", "-t", f"{total:.2f}", "-movflags", "+faststart",
                    os.path.join(outdir, "final.mp4")], check=True)
    print("ok", os.path.getsize(os.path.join(outdir, "final.mp4")) // 1_000_000, "MB")
