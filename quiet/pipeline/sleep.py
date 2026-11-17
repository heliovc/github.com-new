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
Scene types: city, road, temple, interior, sea, hills, cloister (EP02), nile (EP03),
  longhouse / hearth / fjord (EP04: snowy turf longhouse with rising smoke, long-hearth interior with live flames,
  fjord with animated aurora; new "snow" particles; palette key "snow").
  dunes / oasis / camp (EP05 Silk Road: moonlit dune sea with a seamless walking camel caravan (draw_camel, dune_layer
  with lit lee faces), the crescent spring among tall dunes with reeds, a desert halt with felt awning, kneeling camels,
  travellers around a fire and a beacon tower; new "sand" drift particles; palette key "sand").
  canal / campo / rialto / lagoon (EP06 Venice: palazzi with pointed lit windows whose light trembles on the water
  (_wlights), a black gondola with gondolier, iron prow blade, felze cabin and bow lantern gliding across each loop
  (_gondola); a campo with a carved wellhead, cat, altana with washing, campanile and a lamp before a corner shrine;
  the old wooden Rialto bridge with shop rows and a raised centre; open lagoon with tied mooring posts, a heron, an
  island church and the far Murano furnace glow (glowspot); new "mist" particles; palette key "brick").
  headland / lantern / rocktower / watchroom (EP07 Lighthouse Keepers: white tower on a cliff with keepers' cottages,
  walled garden, chimney smoke and a sweeping beam (_tower, _beam: cone reaches far side-on, flashes and widens when it
  swings towards the viewer, two turns per loop); breathing foam lines on the rocks (_foam); inside the lantern a
  beehive Fresnel lens with bull's-eye panels turning round the belt and glare when one faces us (_lens) behind
  diagonal astragals; a flared granite rock tower out at sea with a two-masted schooner crossing, stern lantern and
  sidelights (_ship); the round watch room with curved box bunk, stove, kettle steam, clock, logbook and oil lamp, the
  beam sweeping the sea in the deep window (_winbeam); new "spray" particles; palette key "chalk").
Compilations: comp01.py (COMP01 = EP01-EP03 re-rendered via comp01_pNN.py wrappers) adds "candle haze" text cards that
  dissolve into the next part's first scene, one long ambient tail at the end, one loudness pass; thumb_comp.py = 3-scene
  blended thumbnail.
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


def mountains(y_base, amp, seed, col, snowcol, x0=0, x1=W, base=3, snow_thr=0.45):
    """Jagged snow-capped ridge between x0..x1: returns RGBA layer."""
    n = noise1d(W + 1, seed, 5, base); n = (n - n.min()) / max(1e-6, n.max() - n.min())
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    xs = list(range(int(x0), int(x1) + 1, 4)); top = [y_base - n[min(W, x)] * amp for x in xs]
    d.polygon(list(zip(xs, top)) + [(x1, H), (x0, H)], fill=col + (255,))
    lim = y_base - amp * snow_thr
    low = [t + max(0.0, (lim - t)) * 0.55 + 4 for t in top]
    d.polygon(list(zip(xs, top)) + list(zip(xs[::-1], low[::-1])), fill=snowcol + (255,))
    return lay

def dune_layer(y0, amp, seed, col, litcol, peaks=5, lit_dir=1, x0=0, x1=W, spec=None):
    """EP05: sand dunes with gentle windward slopes, steep lee faces lit by the moon, a bright crest line.
    Returns (RGBA layer, crest y per column)."""
    rng = np.random.default_rng(seed); xs = np.arange(W, dtype=np.float32); crest = np.zeros(W, np.float32)
    if spec is None:
        spec = [(c, rng.uniform(0.5, 1.0) * amp, rng.uniform(0.16, 0.3) * W, None) for c in np.sort(rng.uniform(x0 - 0.1 * W, x1 + 0.1 * W, peaks))]
    for c, h, wl, wr in spec:
        wr = wr or wl * rng.uniform(0.45, 0.7)
        if lit_dir < 0: wl, wr = wr, wl
        u = np.clip(np.where(xs < c, (c - xs) / wl, (xs - c) / wr), 0, 1)
        gentle = 1 - u * u * (3 - 2 * u); steep = (1 - u) ** 1.25                            # windward: smooth; lee: straight-ish
        prof = np.where(xs < c, gentle if lit_dir > 0 else steep, steep if lit_dir > 0 else gentle)
        crest = np.maximum(crest, prof * h)
    kk = np.ones(17, np.float32) / 17; crest = np.convolve(np.pad(crest, 8, mode="edge"), kk, mode="valid")[:W]  # soften crests
    crest += noise1d(W + 1, seed + 1, 3, 4)[:W] * amp * 0.04
    top = y0 - crest
    slope = np.gradient(top) * lit_dir
    lit = np.clip(slope * 2.2, 0, 1) ** 0.6
    kl = np.ones(91, np.float32) / 91; lit = np.convolve(np.pad(lit, 45, mode="edge"), kl, mode="valid")[:W] * 0.7 + 0.07  # soft terminator
    yy = np.arange(H, dtype=np.float32)[:, None]; d = yy - top[None, :]
    shade = lit[None, :] * np.exp(-np.clip(d, 0, None) / (amp * 0.7 + 30))
    shade = np.clip(shade + np.exp(-(np.clip(d, 0, None) / 2.2) ** 2) * 0.35, 0, 1)
    c0, c1 = np.array(col, np.float32), np.array(litcol, np.float32)
    rgb = c0 * (1 - shade[..., None]) + c1 * shade[..., None]
    a = np.clip(d + 1, 0, 1) * 255
    if x0 > 0 or x1 < W: a = a * ((xs >= x0) & (xs <= x1))[None, :]
    arr = np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8)
    return Image.fromarray(arr, "RGBA"), top

def draw_camel(d, x, yg, s, col, ph, loadcol=None, kneel=False):
    """EP05: Bactrian camel silhouette facing right; ph = stride phase (legs swing, body bobs)."""
    c = col + (255,); bob = 0 if kneel else 2.2 * s * math.sin(2 * ph)
    by = yg - (34 if kneel else 74) * s + bob                                              # body centre
    d.ellipse([x - 56 * s, by - 24 * s, x + 54 * s, by + 22 * s], fill=c)
    for hx in (-24, 16):                                                                    # two humps
        d.ellipse([x + (hx - 19) * s, by - 52 * s, x + (hx + 19) * s, by - 4 * s], fill=c)
    if loadcol:                                                                             # bales slung between the humps
        lc = loadcol + (255,)
        d.rounded_rectangle([x - 14 * s, by - 34 * s, x + 6 * s, by + 14 * s], radius=4 * s, fill=lc)
        d.rounded_rectangle([x - 44 * s, by - 6 * s, x - 18 * s, by + 18 * s], radius=4 * s, fill=lc)
        d.line([(x - 40 * s, by - 10 * s), (x + 4 * s, by - 30 * s)], fill=c, width=max(1, int(2 * s)))
    nk = [(x + 46 * s, by - 6 * s), (x + 66 * s, by + 4 * s), (x + 80 * s, by - 14 * s), (x + 86 * s, by - 40 * s), (x + 90 * s, by - 52 * s)]
    if kneel: nk = [(px, py - 10 * s) for px, py in nk]
    d.line(nk, fill=c, width=max(2, int(15 * s)), joint="curve")
    hx, hy = nk[-1]
    d.ellipse([hx - 9 * s, hy - 9 * s, hx + 15 * s, hy + 6 * s], fill=c)
    d.polygon([(hx + 8 * s, hy - 6 * s), (hx + 26 * s, hy - 1 * s), (hx + 24 * s, hy + 7 * s), (hx + 6 * s, hy + 6 * s)], fill=c)
    d.line([(hx - 2 * s, hy - 8 * s), (hx - 6 * s, hy - 15 * s)], fill=c, width=max(1, int(3 * s)))  # ear
    d.line([(x - 54 * s, by - 4 * s), (x - 62 * s, by + 22 * s)], fill=c, width=max(1, int(3 * s)))  # tail
    if kneel:
        d.ellipse([x - 60 * s, yg - 18 * s, x + 56 * s, yg + 2 * s], fill=c)
        return (hx + 20 * s, hy + 4 * s)
    w = max(2, int(7 * s))
    for lx, off in ((-40, 0.0), (-30, math.pi), (34, math.pi), (44, 0.0)):                # legs, diagonal pairs
        sw = 13 * s * math.sin(ph + off); kx = x + lx * s + sw * 0.4
        d.line([(x + lx * s, by + 10 * s), (kx, (by + yg) / 2 + 6 * s), (x + lx * s + sw, yg)], fill=c, width=w, joint="curve")
        d.ellipse([x + lx * s + sw - 6 * s, yg - 3 * s, x + lx * s + sw + 6 * s, yg + 1 * s], fill=c)
    return (hx + 20 * s, hy + 4 * s)

def draw_figure(d, x, yg, s, col, seated=True, hat=True, lute=False):
    """EP05: seated traveller in a long coat (cloak triangle + head + felt hat)."""
    c = col + (255,); h = (58 if seated else 96) * s
    d.polygon([(x - 26 * s, yg), (x + 26 * s, yg), (x + 9 * s, yg - h), (x - 9 * s, yg - h)], fill=c)
    d.ellipse([x - 10 * s, yg - h - 20 * s, x + 10 * s, yg - h + 2 * s], fill=c)
    if hat: d.polygon([(x - 12 * s, yg - h - 12 * s), (x, yg - h - 34 * s), (x + 12 * s, yg - h - 12 * s)], fill=c)
    if lute:
        d.ellipse([x + 4 * s, yg - h * 0.62, x + 34 * s, yg - h * 0.18], fill=c)
        d.line([(x + 22 * s, yg - h * 0.5), (x + 40 * s, yg - h * 1.05), (x + 32 * s, yg - h * 1.12)], fill=c, width=max(2, int(4 * s)))

# ---------------------------------------------------------------- scenes
class Scene:
    """Static layers + animated parts, all periodic in LOOP_S so loops are seamless."""
    def __init__(self, kind, p, seed):
        self.kind, self.p, self.rng = kind, p, np.random.default_rng(seed)
        self.windows, self.stars_tw, self.lamp, self.reflect = [], [], None, None
        self.particles = "embers"; self.fog_y = 0.72 * H; self.fog_a = 0.22
        self.smoke, self.fires, self.aurora, self.caravan = None, [], None, None
        self.gondola, self.wlights, self.glowspot, self.water_y = None, [], None, None
        self.beam, self.beam_src, self.foam, self.lensp, self.win, self.ship = None, None, [], None, None, None
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


    def build_cloister(self):
        """Monastery: bell tower and chapel beyond a cloister arcade (foreground arches frame the sky)."""
        p, rng = self.p, self.rng; hy = int(H * 0.68)
        self.back = self.sky(hy, (0.66, 0.2), 40)
        self.back.alpha_composite(hills(hy - 40, 45, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.35), blur=3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); c = p["mid"] + (255,)
        cx, base = W * 0.5, hy + 60
        d.rectangle([cx - 260, base - 170, cx + 200, base], fill=c)                       # nave
        d.polygon([(cx - 275, base - 170), (cx - 30, base - 270), (cx + 215, base - 170)], fill=c)  # roof
        d.rectangle([cx + 200, base - 330, cx + 290, base], fill=c)                         # bell tower
        d.polygon([(cx + 190, base - 330), (cx + 245, base - 450), (cx + 300, base - 330)], fill=c)
        d.rectangle([cx + 232, base - 316, cx + 258, base - 270], fill=(0, 0, 0, 0))        # belfry opening
        d.pieslice([cx + 232, base - 330, cx + 258, base - 304], 180, 360, fill=(0, 0, 0, 0))
        for k in range(4): self.windows.append((cx - 210 + k * 110, base - 95, 12, 30, k * 0.9, 1 + k % 2))
        d.rectangle([cx - 600, base - 90, cx - 290, base], fill=c)                          # dormitory range
        d.polygon([(cx - 610, base - 90), (cx - 445, base - 140), (cx - 280, base - 90)], fill=c)
        for k in range(5): self.windows.append((cx - 560 + k * 62, base - 50, 6, 12, k * 1.7, 2))
        d.rectangle([0, base, W, H], fill=c)
        r2 = random.Random(int(rng.integers(1e6)))
        for _ in range(5): cypress(d, r2.uniform(W * 0.62, W), base, r2.uniform(120, 200), p["mid"])
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 255)); dn = ImageDraw.Draw(near)
        aw, gap, top = 300, 70, 170                                                          # arcade: carve arches out of a dark wall
        x = -120
        while x < W:
            dn.rectangle([x + gap, top + aw / 2, x + gap + aw, H - 120], fill=(0, 0, 0, 0))
            dn.pieslice([x + gap, top, x + gap + aw, top + aw], 180, 360, fill=(0, 0, 0, 0))
            x += aw + gap
        dn.rectangle([0, H - 120, W, H], fill=p["near"] + (255,))
        arr = np.array(near); arr[..., :3] = p["near"]; near = Image.fromarray(arr, "RGBA")
        self.near = near; self.fog_y = base - 10; self.fog_a = 0.14; self.particles = "dust"

    def build_nile(self):
        """Wide river at night: palms on the near bank, a small boat with a tall sail, pyramids far downriver."""
        p, rng = self.p, self.rng; hy = int(H * 0.58)
        self.back = self.sky(hy, (0.7, 0.18), 50)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far); fc = mix(p["far"], p["horizon"], 0.45) + (255,)
        df.rectangle([0, hy - 14, W, hy + 4], fill=fc)                                      # far bank
        for px, s in ((W * 0.18, 1.0), (W * 0.27, 0.7), (W * 0.33, 0.45)):                  # pyramids
            df.polygon([(px - 120 * s, hy - 10), (px, hy - 125 * s), (px + 120 * s, hy - 10)], fill=fc)
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1.5)))
        river = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(river)
        for y in range(hy + 4, H):
            f = (y - hy) / (H - hy); dr.line([(0, y), (W, y)], fill=mix(mix(p["sea"], p["horizon"], 0.3), p["sea"], f ** 0.6) + (255,))
        self.back.alpha_composite(river)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); c = p["mid"] + (255,)
        bx, by = W * 0.52, hy + 70                                                           # boat
        d.polygon([(bx - 110, by - 14), (bx + 120, by - 20), (bx + 80, by + 10), (bx - 80, by + 10)], fill=c)
        d.line([(bx, by - 14), (bx + 6, by - 230)], fill=c, width=5)
        d.polygon([(bx + 6, by - 228), (bx + 120, by - 40), (bx - 70, by - 40)], fill=mix(p["mid"], p["far"], 0.35) + (255,))
        self.windows.append((bx - 40, by - 4, 5, 5, 0.5, 2))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"] + (255,)
        dn.polygon([(0, H), (0, H - 190), (W * 0.22, H - 150), (W * 0.36, H - 90), (W * 0.42, H)], fill=nc)
        r2 = random.Random(int(rng.integers(1e6)))
        for k in range(6):                                                                    # papyrus reeds
            x = W * 0.05 + k * 70; dn.line([(x, H - 140), (x + 10, H - 300 - k * 8)], fill=nc, width=4)
            hx, hy2 = x + 10, H - 300 - k * 8
            for a in range(-4, 5): dn.line([(hx, hy2), (hx + a * 9, hy2 - 30 + abs(a) * 4)], fill=nc, width=2)
        for px, h in ((W * 0.86, 420), (W * 0.94, 340)):                                    # date palms on the right bank
            dn.polygon([(W * 0.72, H), (W * 0.8, H - 120), (W, H - 160), (W, H)], fill=nc)
            dn.line([(px, H - 110), (px - 18, H - 110 - h)], fill=nc, width=14)
            tx, ty = px - 18, H - 110 - h
            for a in range(9):
                ang = math.pi * (0.05 + a / 8 * 0.9); L = r2.uniform(120, 170)
                ex, ey = tx + math.cos(ang) * L * (1 if a % 2 else -1), ty + abs(math.sin(ang)) * 40 + r2.uniform(10, 60)
                dn.line([(tx, ty), ((tx + ex) / 2, ty - 25), (ex, ey)], fill=nc, width=10, joint="curve")
        self.near = near
        mx, my, mr = self.moon; self.reflect = (mx, hy + 6, mr)
        self.fog_y = hy + 10; self.fog_a = 0.12; self.particles = "fireflies"


    def build_fjord(self):
        """EP04: steep snow-capped walls of a fjord, still black water with mirrored peaks, aurora curtains overhead."""
        p, rng = self.p, self.rng; hy = int(H * 0.6); sn = p.get("snow", (180, 192, 212))
        self.back = self.sky(hy, (0.8, 0.14), 34)
        water = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dw = ImageDraw.Draw(water)
        for y in range(hy, H):
            f = (y - hy) / (H - hy); dw.line([(0, y), (W, y)], fill=mix(mix(p["sea"], p["horizon"], 0.25), p["sea"], f ** 0.5) + (255,))
        self.back.alpha_composite(water)
        m = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        far = mountains(hy + 2, 150, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.35), mix(sn, p["horizon"], 0.45), W * 0.25, W * 0.78, 3)
        fa = np.array(far); fa[hy + 3:, :, 3] = 0; m.alpha_composite(Image.fromarray(fa, "RGBA"))
        def wall(side, height, seed, col, scol, reach):
            n = noise1d(W + 1, seed, 5, 5); xs = np.arange(0, W + 1, 4)
            u = np.clip((xs if side < 0 else W - xs) / (W * reach), 0, 1)              # 0 at the frame edge -> 1 at the water
            top = hy - height * (1 - u) ** 0.9 - 26 * n[xs] * (1 - u)
            ok = u < 1; xs, top = xs[ok], top[ok]
            pts = list(zip(xs.tolist(), top.tolist())); edge = (xs[-1] if side < 0 else xs[0])
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
            poly = pts + ([(edge + 30, hy + 4), (0, hy + 4)] if side < 0 else [(W, hy + 4), (edge - 30, hy + 4)])
            d.polygon(poly, fill=col + (255,))
            lim = hy - height * 0.42; low = [t + max(0.0, lim - t) * 0.5 + 6 for t in top.tolist()]
            d.polygon(pts + list(zip(xs.tolist()[::-1], low[::-1])), fill=scol + (255,))
            for k in range(9):                                                           # a few snow gullies down the face
                x = float(rng.uniform(xs.min(), xs.max())); i = int(np.argmin(abs(xs - x))); y = top[i]
                d.line([(x, y + 6), (x + side * -rng.uniform(4, 16), y + rng.uniform(40, 90))], fill=mix(scol, col, 0.7) + (255,), width=2)
            return lay
        m.alpha_composite(wall(-1, 470, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.45), mix(sn, p["far"], 0.32), 0.47))
        m.alpha_composite(wall(1, 400, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.6), mix(sn, p["far"], 0.42), 0.38))
        top = m.crop((0, hy - (H - hy), W, hy + 4)).transpose(Image.FLIP_TOP_BOTTOM)  # mirror on the still water
        ref = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ref.alpha_composite(top, (0, hy + 2))
        a = np.array(ref); a[..., 3] = (a[..., 3] * 0.18).astype(np.uint8); ref = Image.fromarray(a, "RGBA").filter(ImageFilter.GaussianBlur(2))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); mid.alpha_composite(ref); mid.alpha_composite(m)
        dmid = ImageDraw.Draw(mid)                                               # a farm light far down the shore
        self.windows.append((W * 0.53, hy - 6, 5, 4, 0.4, 1))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"] + (255,)
        dn.polygon([(0, H), (0, H - 170), (W * 0.18, H - 130), (W * 0.34, H - 70), (W * 0.4, H)], fill=nc)
        dn.polygon([(0, H - 170), (W * 0.18, H - 130), (W * 0.3, H - 92), (W * 0.2, H - 112), (0, H - 150)], fill=mix(sn, p["near"], 0.55) + (255,))
        bx, by = W * 0.17, H - 128                                               # overturned boat on the stones
        dn.chord([bx - 120, by - 46, bx + 120, by + 30], 180, 360, fill=mix(sn, p["near"], 0.7) + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        for k in range(5):                                                       # birches on the right shore
            x = W * 0.78 + k * 80 + r2.uniform(-20, 20); h = r2.uniform(260, 420)
            dn.polygon([(W * 0.7, H), (W * 0.76, H - 90), (W, H - 140), (W, H)], fill=nc)
            dn.line([(x, H - 100), (x + r2.uniform(-12, 12), H - 100 - h)], fill=nc, width=6)
            for j in range(9):
                yy = H - 100 - h * (0.35 + j * 0.07); L = 30 + j * 4
                dn.line([(x, yy), (x + (L if j % 2 else -L), yy - 26)], fill=nc, width=2)
        self.near = near
        self.aurora = dict(y=hy * 0.36, depth=hy * 0.34, x0=W * 0.05, x1=W * 0.95, hy=hy)
        self.fog_y = hy - 6; self.fog_a = 0.10; self.particles = "snow"

    def build_longhouse(self):
        """EP04: long, boat-sided Norse house with a snowy turf roof, smoke from the roof-hole, outbuildings, mountains."""
        p, rng = self.p, self.rng; hy = int(H * 0.56); sn = p.get("snow", (180, 192, 212))
        self.back = self.sky(hy, (0.2, 0.17), 38)
        self.back.alpha_composite(mountains(hy + 30, 330, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.25), mix(sn, p["horizon"], 0.4), 0, W, 3, 0.55).filter(ImageFilter.GaussianBlur(1.5)))
        fj = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(fj).rectangle([0, hy + 22, W, hy + 44], fill=mix(p["sea"], p["horizon"], 0.3) + (255,))
        self.back.alpha_composite(fj)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        gnd = hills(hy + 60, 18, int(rng.integers(1e6)), mix(sn, p["mid"], 0.62)); mid.alpha_composite(gnd)
        x0, x1, base = W * 0.28, W * 0.8, hy + 230
        ridge = [(lerp(x0 + 30, x1 - 30, u / 40), base - 165 - 46 * math.sin(math.pi * u / 40) ** 0.7) for u in range(41)]
        eave = [(lerp(x1 + 16, x0 - 16, u / 40), base - 52 + 14 * math.sin(math.pi * u / 40)) for u in range(41)]
        wall = [(lerp(x0, x1, u / 40), base - 52 + 14 * math.sin(math.pi * u / 40)) for u in range(41)]
        d.polygon(wall + [(x1 - 6, base + 4), (x0 + 6, base + 4)], fill=p["mid"] + (255,))      # bowed timber wall
        for k in range(1, 26): xx = lerp(x0, x1, k / 26); d.line([(xx, base - 50), (xx, base)], fill=mix(p["mid"], p["near"], 0.4) + (255,), width=2)
        d.polygon(ridge + eave, fill=mix(sn, p["far"], 0.3) + (255,))                       # snow on the turf roof
        d.line(eave, fill=mix(p["mid"], sn, 0.25) + (255,), width=10)                         # turf edge at the eaves
        dx = W * 0.47; d.rectangle([dx - 22, base - 58, dx + 22, base], fill=mix(p["mid"], p["near"], 0.5) + (255,))
        self.windows.append((dx, base - 30, 30, 50, 0.3, 1))                                 # half-open door, firelight
        for (cx, w, h) in ((W * 0.13, 170, 70), (W * 0.9, 150, 60)):                         # storehouse and sheep shed
            bb = base - 10 + (cx > W / 2) * 20
            d.rectangle([cx - w / 2, bb - h * 0.5, cx + w / 2, bb], fill=p["mid"] + (255,))
            d.polygon([(cx - w / 2 - 12, bb - h * 0.5), (cx, bb - h * 1.15), (cx + w / 2 + 12, bb - h * 0.5)], fill=mix(sn, p["far"], 0.2) + (255,))
        self.windows.append((W * 0.13, base - 30, 6, 8, 2.1, 2))
        d.polygon([(0, base + 4), (W, base + 4), (W, H), (0, H)], fill=mix(sn, p["mid"], 0.6) + (255,))
        self.mid = mid
        near = hills(H - 110, 26, int(rng.integers(1e6)), mix(sn, p["near"], 0.72)); dn = ImageDraw.Draw(near)
        r2 = random.Random(int(rng.integers(1e6)))
        for k in range(16):                                                                  # a fence of stakes in the snow
            x = W * 0.02 + k * 46; y = H - 120 + k * 3
            dn.line([(x, y), (x + 3, y - 70 - r2.uniform(0, 12))], fill=p["near"] + (255,), width=6)
        for x, h in ((W * 0.93, 520), (W * 0.985, 400)):                                     # dark spruce
            for j in range(9):
                f = j / 9; w = h * 0.24 * (1 - f * 0.85); yy = H - 60 - h * f
                dn.polygon([(x - w, yy), (x, yy - h * 0.18), (x + w, yy)], fill=p["near"] + (255,))
                dn.line([(x - w * 0.9, yy - 2), (x, yy - h * 0.14)], fill=mix(sn, p["near"], 0.5) + (255,), width=3)
        self.near = near
        self.smoke = (lerp(x0, x1, 0.5), base - 205, 560)
        self.fog_y = hy + 40; self.fog_a = 0.12; self.particles = "snow"

    def build_hearth(self):
        """EP04: inside the longhouse - two rows of roof posts receding, benches, the long hearth with live flames."""
        p, rng = self.p, self.rng; vx, vy = W * 0.5, H * 0.4
        base = np.zeros((H, W, 3), np.float32) + np.array(mix(p["near"], p["mid"], 0.6), np.float32)
        base += radial_glow(vx, H * 0.7, 700, p["light"], 0.16) + radial_glow(vx, H * 0.62, 260, p["light"], 0.12)
        img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA"); d = ImageDraw.Draw(img)
        sk = self.sky(int(H * 0.5), (0.53, 0.06), 14)                                      # smoke hole shows a scrap of sky
        hole = Image.new("L", (W, H), 0); ImageDraw.Draw(hole).polygon([(vx - 70, 40), (vx + 70, 40), (vx + 52, 120), (vx - 52, 120)], fill=255)
        img.paste(sk, (0, 0), hole)
        self.stars_tw = [s for s in self.stars_tw if vx - 60 < s[0] < vx + 60 and 45 < s[1] < 115]
        wood = lambda z: mix(mix(p["mid"], p["light"], 0.10 / z), p["near"], min(0.8, 0.2 * z)) + (255,)
        for z in (5.5, 4.4, 3.5, 2.7, 2.0, 1.45):                                          # posts, far to near
            s_ = 1 / z
            d.line([(vx - 760 * s_, vy - 640 * s_), (vx + 760 * s_, vy - 640 * s_)], fill=wood(z), width=max(2, int(28 * s_)))
            for side in (-1, 1):
                x = vx + side * 560 * s_
                d.rectangle([x - 34 * s_, vy - 640 * s_, x + 34 * s_, vy + 520 * s_], fill=wood(z))
                d.line([(x, vy - 640 * s_), (vx + side * 980 * s_, vy - 340 * s_)], fill=wood(z), width=max(2, int(20 * s_)))
        d.rectangle([vx - 560 / 6, vy - 640 / 6, vx + 560 / 6, vy + 520 / 6], fill=mix(p["near"], p["mid"], 0.3) + (255,))  # far partition
        for side in (-1, 1):                                                                 # bench platforms
            d.polygon([(vx + side * 600 / 6, vy + 420 / 6), (vx + side * 1500, H * 0.86), (vx + side * 1500, H), (vx + side * 600 / 6, vy + 520 / 6)], fill=mix(p["mid"], p["light"], 0.07) + (255,))
            d.line([(vx + side * 600 / 6, vy + 420 / 6), (vx + side * 1500, H * 0.86)], fill=mix(p["mid"], p["light"], 0.22) + (255,), width=4)
        d.polygon([(vx - 30, vy + 520 / 5.5), (vx + 30, vy + 520 / 5.5), (vx + 300, H), (vx - 300, H)], fill=mix(p["near"], p["mid"], 0.3) + (255,))  # hearth stones
        for k in range(14):
            f = (k + 1) / 15; y = vy + 520 / 5.5 + f ** 1.8 * (H - vy - 520 / 5.5); hw = 30 + f ** 1.8 * 270
            d.line([(vx - hw, y), (vx + hw, y)], fill=mix(p["mid"], p["light"], 0.18) + (255,), width=2)
        for z in (4.2, 3.0, 2.2, 1.6):                                                     # fire spots along the hearth
            f = ((vy + 520 / z) - (vy + 520 / 5.5)) / (H - vy - 520 / 5.5)
            self.fires.append((vx, vy + 520 / z + 6, 1.15 / z ** 0.9))
        self.back = img
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"] + (255,)
        for x in (60, W - 60): dn.rectangle([x - 70, 0, x + 70, H], fill=nc)              # nearest posts frame the shot
        dn.rectangle([0, 0, W, 34], fill=nc)
        dn.polygon([(0, H * 0.84), (W * 0.3, H * 0.93), (W * 0.3, H), (0, H)], fill=nc)     # near bench edge with a lamp
        lx, ly = W * 0.2, H * 0.88
        dn.ellipse([lx - 46, ly - 22, lx + 46, ly + 6], fill=mix(p["near"], p["accent"], 0.25) + (255,))
        dn.rectangle([W * 0.08, H * 0.8, W * 0.14, H * 0.9], fill=mix(p["near"], p["accent"], 0.1) + (255,))  # a basket of wool
        self.lamp = (lx + 30, ly - 22)
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); self.near = near
        self.particles = "embers"; self.fog_a = 0

    def build_dunes(self):
        """EP05: moonlit sand sea; a caravan of Bactrian camels walks slowly along a long dune ridge (seamless loop:
        each camel advances exactly one spacing per loop); dark dune shoulders hide where the line enters and leaves."""
        p, rng = self.p, self.rng; hy = int(H * 0.6); sd = p.get("sand", (168, 128, 92))
        self.back = self.sky(hy, (0.76, 0.17), 44)
        far, _ = dune_layer(hy + 8, 70, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.5), mix(sd, p["moon"], 0.25), 7)
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1.5)))
        mid1, _ = dune_layer(hy + 70, 110, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.35), mix(sd, p["far"], 0.35), 5)
        path_lay, top = dune_layer(hy + 170, 46, int(rng.integers(1e6)), mix(p["mid"], p["far"], 0.35), mix(sd, p["mid"], 0.45), 2)
        k = np.ones(81, np.float32) / 81; top = np.convolve(np.pad(top, 40, mode="edge"), k, mode="valid")[:W]   # smooth walking line
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); mid.alpha_composite(mid1); mid.alpha_composite(path_lay)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sh_l, _ = dune_layer(hy + 300, 250, int(rng.integers(1e6)), p["near"], mix(sd, p["near"], 0.62), 1, 1, spec=[(-W * 0.02, 250, W * 0.2, W * 0.32)])
        sh_r, _ = dune_layer(H + 10, 380, int(rng.integers(1e6)), p["near"], mix(sd, p["near"], 0.66), 1, -1, spec=[(W * 1.02, 380, W * 0.36, W * 0.2)])
        fl, _ = dune_layer(H - 40, 40, int(rng.integers(1e6)), mix(p["near"], p["mid"], 0.4), mix(sd, p["near"], 0.55), 3)
        near.alpha_composite(fl); near.alpha_composite(sh_l); near.alpha_composite(sh_r)
        dn = ImageDraw.Draw(near)
        for j in range(7):                                                                    # wind ripples on the near sand
            y = H - 30 + j * 4; dn.arc([W * 0.32 + j * 40, y - 30, W * 0.62 + j * 50, y + 30], 200, 340, fill=mix(sd, p["near"], 0.7) + (255,), width=2)
        self.near = near
        self.caravan = dict(top=top, s=0.62, spacing=168, n=14, col=mix(p["near"], p["mid"], 0.25), load=mix(p["near"], p["accent"], 0.12), x_in=W * 0.12, x_out=W * 0.86)
        self.fog_y = hy + 40; self.fog_a = 0.08; self.particles = "sand"

    def build_oasis(self):
        """EP05: the crescent spring - a curved pool among tall dunes, reeds along its rim, doubled stars and moon."""
        p, rng = self.p, self.rng; hy = int(H * 0.5); sd = p.get("sand", (168, 128, 92))
        self.back = self.sky(hy, (0.5, 0.15), 40)
        lake = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lake)
        for y in range(int(H * 0.6), H):
            f = (y - H * 0.6) / (H * 0.4); dl.line([(0, y), (W, y)], fill=mix(mix(p["sea"], (120, 142, 196), 0.42), p["sea"], f ** 0.8) + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        for _ in range(70):                                                                   # stars mirrored in the still water
            x, y = r2.uniform(W * 0.2, W * 0.8), r2.uniform(H * 0.64, H * 0.84)
            dl.point((x, y), fill=mix(p["sea"], p["moon"], r2.uniform(0.2, 0.6)) + (255,))
        self.back.alpha_composite(lake)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        big_l, _ = dune_layer(H * 0.62, 340, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.3), mix(sd, p["moon"], 0.1), 1, 1, spec=[(W * 0.2, 330, W * 0.4, W * 0.24)])
        big_r, _ = dune_layer(H * 0.62, 260, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.45), mix(sd, p["far"], 0.2), 1, -1, spec=[(W * 0.84, 250, W * 0.36, W * 0.2)])
        for lay_ in (big_r, big_l):
            a_ = np.array(lay_); a_[int(H * 0.61):, :, 3] = 0; mid.alpha_composite(Image.fromarray(a_, "RGBA"))
        rim = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(rim); rc = mix(p["mid"], sd, 0.22) + (255,)
        dr.rectangle([0, H * 0.6, W, H], fill=rc)
        cx, cy = W * 0.5, H * 0.71                                                            # carve the crescent pool
        dr.ellipse([cx - 600, cy - 95, cx + 600, cy + 165], fill=(0, 0, 0, 0))
        dr.ellipse([cx - 480, cy - 118, cx + 480, cy + 60], fill=rc)
        dr.arc([cx - 480, cy - 118, cx + 480, cy + 60], 15, 165, fill=mix(rc[:3], p["moon"], 0.16) + (255,), width=3)
        mid.alpha_composite(rim)
        dm = ImageDraw.Draw(mid); nc = mix(p["near"], p["mid"], 0.45) + (255,)
        for _ in range(170):                                                                  # reeds along the outer rim
            a = r2.uniform(0.04, 0.96) * math.pi; x = cx - math.cos(a) * 560 * r2.uniform(0.96, 1.04); y = cy + math.sin(a) * 140 + r2.uniform(-4, 8)
            hgt = r2.uniform(26, 70) * (0.6 + 0.6 * math.sin(a)); lean = r2.uniform(-12, 12)
            dm.line([(x, y), (x + lean, y - hgt)], fill=nc, width=2)
            if r2.random() < 0.3: dm.ellipse([x + lean - 3, y - hgt - 12, x + lean + 3, y - hgt + 2], fill=nc)
        for tx in (W * 0.12, W * 0.86):                                                       # tamarisk bushes
            for _ in range(40):
                a = r2.uniform(0.15, 0.85) * math.pi; L = r2.uniform(40, 110)
                dm.line([(tx, H * 0.66), (tx + math.cos(a) * L, H * 0.66 - math.sin(a) * L)], fill=nc, width=2)
        self.windows.append((W * 0.78, H * 0.6, 4, 4, 0.8, 1))                                # a traveller's lamp far off
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); n2 = p["near"] + (255,)
        dn.polygon([(0, H), (0, H - 120), (W * 0.2, H - 60), (W * 0.42, H - 20), (W * 0.5, H)], fill=n2)
        for k in range(26):                                                                   # foreground reeds, left
            x = 20 + k * 22 + r2.uniform(-6, 6); hgt = r2.uniform(160, 330)
            dn.line([(x, H - 90 + k * 2), (x + r2.uniform(-30, 30), H - 90 - hgt)], fill=n2, width=3)
        self.near = near
        mx, my, mr = self.moon; self.reflect = (mx, H * 0.7, mr)
        self.fog_y = H * 0.6; self.fog_a = 0.14; self.particles = "fireflies"

    def build_camp(self):
        """EP05: caravan halt in a hollow - felt awning on poles, kneeling camels, stacked bales, travellers around
        a small fire (one with a lute), an old beacon tower on the horizon."""
        p, rng = self.p, self.rng; hy = int(H * 0.6); sd = p.get("sand", (168, 128, 92))
        self.back = self.sky(hy, (0.18, 0.16), 36)
        far, _ = dune_layer(hy + 6, 80, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.45), mix(sd, p["moon"], 0.2), 6, -1)
        df = ImageDraw.Draw(far); tx, ty = W * 0.7, hy - 8                                  # beacon tower of earth and reeds
        tc = mix(p["far"], p["horizon"], 0.3) + (255,)
        df.polygon([(tx - 30, ty), (tx + 30, ty), (tx + 21, ty - 120), (tx - 21, ty - 120)], fill=tc)
        for j in range(1, 8): df.line([(tx - 30 + j * 1.2, ty - j * 15), (tx + 30 - j * 1.2, ty - j * 15)], fill=mix(p["far"], p["moon"], 0.12) + (255,), width=1)
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        g, _ = dune_layer(hy + 120, 60, int(rng.integers(1e6)), mix(p["mid"], p["far"], 0.25), mix(sd, p["mid"], 0.4), 3, -1)
        mid.alpha_composite(g); d = ImageDraw.Draw(mid)
        d.rectangle([0, hy + 150, W, H], fill=mix(p["mid"], sd, 0.12) + (255,))
        cc = mix(p["near"], p["mid"], 0.55)
        for i, (x, s) in enumerate(((W * 0.1, 0.9), (W * 0.24, 0.78), (W * 0.78, 0.82), (W * 0.9, 0.95))):  # kneeling camels
            draw_camel(d, x, hy + 230 + s * 40, s, cc, 0, None, kneel=True)
        ax0, ax1, ay = W * 0.3, W * 0.62, hy + 70                                           # felt awning on poles
        d.polygon([(ax0 - 30, ay + 30), (ax0 + 40, ay - 40), (ax1 - 40, ay - 50), (ax1 + 30, ay + 22), (ax1, ay + 34), (ax0, ay + 42)], fill=mix(p["mid"], p["accent"], 0.16) + (255,))
        for x in (ax0, ax1): d.line([(x, ay + 40), (x, ay + 210)], fill=cc + (255,), width=6)
        for j in range(4):                                                                    # stacked bales
            d.rounded_rectangle([W * 0.64 + j * 46, hy + 196 - (j % 2) * 30, W * 0.64 + j * 46 + 54, hy + 236 - (j % 2) * 30], radius=6, fill=mix(mix(p["near"], p["mid"], 0.6), p["accent"], 0.06 + 0.02 * j) + (255,))
        self.mid = mid
        fx, fy = W * 0.47, H * 0.83
        self.fires.append((fx, fy, 0.42))
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); fc = p["near"]
        for x, s, lute in ((fx - 210, 1.25, False), (fx - 120, 1.05, False), (fx + 150, 1.15, True), (fx + 260, 1.35, False)):
            draw_figure(dn, x, H * 0.88 + s * 6, s, fc, True, x != fx - 120, lute)          # travellers around the fire
        dn.chord([fx + 62, H * 0.835, fx + 104, H * 0.87], 0, 180, fill=fc + (255,))         # the iron pot, set aside on the sand
        sn, _ = dune_layer(H - 10, 70, int(rng.integers(1e6)), p["near"], mix(sd, p["near"], 0.6), 2, -1)
        near.alpha_composite(sn)
        self.near = near
        self.fog_y = hy + 30; self.fog_a = 0.08; self.particles = "embers"

    # --- EP06 Venice: canal / campo / rialto / lagoon
    def _water(self, hy, tint=0.3):
        p = self.p; w = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dw = ImageDraw.Draw(w)
        for y in range(hy, H):
            f = (y - hy) / max(1, H - hy)
            dw.line([(0, y), (W, y)], fill=mix(mix(p["sea"], p["horizon"], tint), p["sea"], f ** 0.55) + (255,))
        for k in range(60):                                                                   # faint static ripples
            y = hy + 6 + (H - hy) * (k / 60) ** 1.6; x = self.rng.uniform(0, W); L = 30 + 260 * (k / 60)
            dw.line([(x - L, y), (x + L, y)], fill=mix(p["sea"], p["moon"], 0.07) + (90,), width=1)
        self.back.alpha_composite(w); self.water_y = hy

    def _palazzi(self, d, x0, x1, base, col, s=1.0, lit=0.3, reflect=True, maxh=420):
        """Venetian facades: pointed-arch windows in rows, a joined group of arches on the main floor with a balcony,
        a water gate at the base, bell-shaped chimneys on the roof. Lit windows feed self.windows and the water lights."""
        p, rng = self.p, self.rng; x = x0
        while x < x1:
            w = rng.uniform(170, 320) * s; h = rng.uniform(0.55, 1.0) * maxh * s
            fc = mix(col, p.get("brick", (110, 60, 50)), rng.uniform(0.04, 0.22)); dark = mix(fc, (0, 0, 0), 0.35)
            d.rectangle([x, base - h, x + w, base], fill=fc + (255,))
            d.rectangle([x - 5 * s, base - h - 9 * s, x + w + 5 * s, base - h], fill=dark + (255,))
            for _ in range(int(rng.integers(1, 3))):                                         # bell (funnel) chimneys
                cx = x + rng.uniform(0.15, 0.85) * w; ch = rng.uniform(40, 70) * s
                d.rectangle([cx - 5 * s, base - h - ch, cx + 5 * s, base - h], fill=dark + (255,))
                d.polygon([(cx - 5 * s, base - h - ch), (cx - 17 * s, base - h - ch - 26 * s), (cx + 17 * s, base - h - ch - 26 * s), (cx + 5 * s, base - h - ch)], fill=dark + (255,))
            gw = min(70 * s, w * 0.3); gx = x + w / 2                                         # water gate
            d.rectangle([gx - gw / 2, base - 70 * s, gx + gw / 2, base], fill=mix(fc, (0, 0, 0), 0.6) + (255,))
            d.pieslice([gx - gw / 2, base - 70 * s - gw / 2, gx + gw / 2, base - 70 * s + gw / 2], 180, 360, fill=mix(fc, (0, 0, 0), 0.6) + (255,))
            floors = max(2, int(h / (92 * s))); ww = 16 * s; wh = 36 * s
            for fl in range(1, floors):
                yb = base - 110 * s - (fl - 1) * 88 * s
                if yb - wh < base - h + 14 * s: break
                group = fl == 1 and w > 200 * s
                n = max(2, int(w / (60 * s)))
                xs_ = [x + w * (i + 0.5) / n for i in range(n)]
                if group:                                                                     # joined arches of the main floor
                    gc = int(rng.integers(3, 6)); gx0 = x + w / 2 - gc * ww * 0.75
                    xs_ = [gx0 + ww * 0.75 + i * ww * 1.5 for i in range(gc)]
                    d.rectangle([gx0 - 6 * s, yb + 2 * s, gx0 + gc * ww * 1.5 + 6 * s, yb + 8 * s], fill=dark + (255,))
                for wx in xs_:
                    wc = mix(fc, (0, 0, 0), 0.62)
                    d.rectangle([wx - ww / 2, yb - wh, wx + ww / 2, yb], fill=wc + (255,))
                    d.polygon([(wx - ww / 2, yb - wh), (wx, yb - wh - ww * 0.95), (wx + ww / 2, yb - wh)], fill=wc + (255,))
                    if rng.random() < lit:
                        self.windows.append((wx, yb - wh * 0.45, ww * 0.62, wh * 0.8, rng.uniform(0, TAU), int(rng.integers(1, 3))))
                        if reflect and getattr(self, "water_y", None): self.wlights.append((wx, ww * 1.6, 120 * s ** 0.5, rng.uniform(0, TAU)))
            x += w + rng.uniform(-4, 10) * s

    def _lantern_post(self, d, x, base, h, col):
        d.line([(x, base), (x, base - h)], fill=col + (255,), width=6)
        d.line([(x, base - h), (x + 26, base - h)], fill=col + (255,), width=4)
        d.rectangle([x + 18, base - h + 4, x + 34, base - h + 26], fill=col + (255,))
        self.windows.append((x + 26, base - h + 15, 9, 14, 0.4, 2))

    def build_canal(self):
        """Across a broad canal at night: a row of palazzi on the far bank with lit pointed windows whose light trembles
        in the water, a striped mooring pole and a stone landing in front, a black gondola with a bow lantern gliding past."""
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy - 260, (0.8, 0.14), 40)
        self._water(hy, 0.22)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)               # campanile far behind
        cx = W * 0.3; fcol = mix(p["far"], p["horizon"], 0.35) + (255,)
        df.rectangle([cx - 30, hy - 520, cx + 30, hy - 200], fill=fcol)
        df.polygon([(cx - 34, hy - 520), (cx, hy - 610), (cx + 34, hy - 520)], fill=fcol)
        for k in range(3): df.rectangle([cx - 22 + k * 17, hy - 500, cx - 14 + k * 17, hy - 465], fill=mix(p["far"], p["sky_mid"], 0.7) + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1.2)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        self._palazzi(d, -60, W + 60, hy, mix(p["mid"], p["far"], 0.35), 1.0, 0.32)
        d.rectangle([0, hy - 6, W, hy + 3], fill=mix(p["mid"], (0, 0, 0), 0.3) + (255,))      # waterline of the far bank
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(W * 0.7, H), (W * 0.76, H - 120), (W, H - 150), (W, H)], fill=nc + (255,))   # stone landing
        for k in range(3): dn.line([(W * 0.74 + k * 14, H - 100 + k * 34), (W, H - 128 + k * 34)], fill=mix(nc, p["moon"], 0.1) + (255,), width=2)
        px = W * 0.12                                                                         # striped mooring pole
        for k in range(9):
            dn.rectangle([px - 13, H - 560 + k * 62, px + 13, H - 560 + (k + 1) * 62], fill=(mix(nc, p["accent"], 0.22) if k % 2 else nc) + (255,))
        dn.ellipse([px - 15, H - 576, px + 15, H - 548], fill=nc + (255,))
        self._lantern_post(dn, W * 0.86, H - 140, 300, nc); self.windows.pop()
        self.lamp = (W * 0.86 + 26, H - 440 + 22); self.lamp_r = 300
        self.near = near
        self.gondola = dict(y=hy + 210, s=0.95, dir=1)
        self.fog_y = hy - 10; self.fog_a = 0.12; self.particles = "mist"

    def build_campo(self):
        """A small Venetian square: herringbone brick paving, a carved stone wellhead with a cat on its rim, houses with
        balconies, an altana with washing on a roof, a brick campanile, and a lamp before a corner shrine."""
        p, rng = self.p, self.rng; gy = int(H * 0.74)
        self.back = self.sky(gy - 200, (0.56, 0.13), 34)
        br = p.get("brick", (110, 60, 50))
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)
        tc = mix(mix(p["mid"], br, 0.22), p["far"], 0.35) + (255,); tx = W * 0.6           # campanile
        df.rectangle([tx - 52, 170, tx + 52, gy], fill=tc)
        df.rectangle([tx - 62, 150, tx + 62, 176], fill=tc)
        for k in range(3): df.pieslice([tx - 44 + k * 32, 186, tx - 20 + k * 32, 214], 180, 360, fill=mix(p["sky_top"], p["far"], 0.2) + (255,))
        for k in range(3): df.rectangle([tx - 44 + k * 32, 200, tx - 20 + k * 32, 250], fill=mix(p["sky_top"], p["far"], 0.2) + (255,))
        df.rectangle([tx - 62, 254, tx + 62, 266], fill=tc)
        df.polygon([(tx - 56, 150), (tx, 40), (tx + 56, 150)], fill=tc)
        for k in range(7): df.line([(tx - 52, 300 + k * 60), (tx + 52, 300 + k * 60)], fill=mix(tc[:3], (0, 0, 0), 0.2) + (255,), width=2)
        cx0, cx1 = W * 0.36, W * 0.56                                                         # church front
        df.rectangle([cx0, gy - 330, cx1, gy], fill=mix(tc[:3], p["mid"], 0.45) + (255,))
        df.polygon([(cx0 - 10, gy - 330), ((cx0 + cx1) / 2, gy - 420), (cx1 + 10, gy - 330)], fill=mix(tc[:3], p["mid"], 0.45) + (255,))
        df.ellipse([(cx0 + cx1) / 2 - 34, gy - 300, (cx0 + cx1) / 2 + 34, gy - 232], fill=mix(p["mid"], p["light"], 0.25) + (255,))
        df.rectangle([(cx0 + cx1) / 2 - 40, gy - 130, (cx0 + cx1) / 2 + 40, gy], fill=mix(p["mid"], (0, 0, 0), 0.4) + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(0.8)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        hc = mix(p["mid"], br, 0.18)
        for (x0, x1, top) in ((-20, W * 0.3, 260), (W * 0.72, W + 20, 220)):                  # houses framing the square
            d.rectangle([x0, top, x1, gy + 40], fill=hc + (255,))
            d.rectangle([x0 - 6, top - 12, x1 + 6, top], fill=mix(hc, (0, 0, 0), 0.35) + (255,))
            for fl in range(4):
                y = top + 70 + fl * 120
                if y > gy - 60: break
                for wx in np.arange(x0 + 60, x1 - 30, 115):
                    sc = mix(hc, p["accent"], 0.12) if rng.random() < 0.6 else mix(hc, (0, 0, 0), 0.5)
                    d.rectangle([wx - 30, y - 34, wx - 12, y + 30], fill=sc + (255,)); d.rectangle([wx + 12, y - 34, wx + 30, y + 30], fill=sc + (255,))
                    d.rectangle([wx - 11, y - 34, wx + 11, y + 30], fill=mix(hc, (0, 0, 0), 0.6) + (255,))
                    d.pieslice([wx - 11, y - 46, wx + 11, y - 22], 180, 360, fill=mix(hc, (0, 0, 0), 0.6) + (255,))
                    if rng.random() < 0.3: self.windows.append((wx, y - 2, 14, 46, rng.uniform(0, TAU), int(rng.integers(1, 3))))
                    if fl == 1 and rng.random() < 0.5:                                        # little balcony
                        d.rectangle([wx - 40, y + 30, wx + 40, y + 38], fill=mix(hc, (0, 0, 0), 0.4) + (255,))
                        for b in range(-36, 40, 9): d.line([(wx + b, y + 30), (wx + b, y + 10)], fill=mix(hc, (0, 0, 0), 0.4) + (255,), width=2)
            for k in range(2):                                                                # chimneys
                cx = x0 + (x1 - x0) * (0.3 + 0.4 * k)
                d.rectangle([cx - 6, top - 70, cx + 6, top - 12], fill=mix(hc, (0, 0, 0), 0.35) + (255,))
                d.polygon([(cx - 6, top - 70), (cx - 20, top - 98), (cx + 20, top - 98), (cx + 6, top - 70)], fill=mix(hc, (0, 0, 0), 0.35) + (255,))
        ax = W * 0.8; at = 220                                                                # altana with sheets
        d.rectangle([ax - 90, at - 70, ax + 90, at - 62], fill=mix(hc, (0, 0, 0), 0.4) + (255,))
        for k in range(5): d.line([(ax - 90 + k * 45, at - 12), (ax - 90 + k * 45, at - 112)], fill=mix(hc, (0, 0, 0), 0.4) + (255,), width=4)
        d.line([(ax - 90, at - 110), (ax + 90, at - 110)], fill=mix(hc, (0, 0, 0), 0.4) + (255,), width=2)
        for k in range(3): d.rectangle([ax - 80 + k * 55, at - 108, ax - 42 + k * 55, at - 74 + (k % 2) * 8], fill=mix(p["moon"], hc, 0.72) + (255,))
        pv = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dp = ImageDraw.Draw(pv)               # herringbone paving in perspective
        dp.rectangle([0, gy, W, H], fill=mix(p["mid"], br, 0.12) + (255,))
        vx = W * 0.5
        for k in range(-16, 17):
            dp.line([(vx + k * 40, gy), (vx + k * 260, H)], fill=mix(p["mid"], p["moon"], 0.06) + (255,), width=1)
        for j in range(12):
            y = gy + (H - gy) * (j / 12) ** 1.5; dp.line([(0, y), (W, y)], fill=mix(p["mid"], p["moon"], 0.05) + (255,), width=1)
        self.back.alpha_composite(pv)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = mix(p["near"], p["mid"], 0.35)
        wx, wy = W * 0.47, H * 0.9                                                            # wellhead
        dn.rectangle([wx - 130, wy - 150, wx + 130, wy], fill=nc + (255,))
        dn.ellipse([wx - 130, wy - 30, wx + 130, wy + 24], fill=nc + (255,))
        dn.ellipse([wx - 136, wy - 174, wx + 136, wy - 128], fill=mix(nc, p["moon"], 0.16) + (255,))
        dn.ellipse([wx - 104, wy - 166, wx + 104, wy - 136], fill=mix(nc, (0, 0, 0), 0.3) + (255,))
        dn.chord([wx - 96, wy - 196, wx + 96, wy - 140], 180, 360, fill=mix(nc, (0, 0, 0), 0.25) + (255,))   # iron lid
        for k in range(6):                                                                    # carved leaves and shield
            ex = wx - 105 + k * 42; dn.ellipse([ex - 14, wy - 104, ex + 14, wy - 64], outline=mix(nc, p["moon"], 0.12) + (255,), width=2)
        dn.polygon([(wx - 20, wy - 112), (wx + 20, wy - 112), (wx + 20, wy - 80), (wx, wy - 62), (wx - 20, wy - 80)], fill=mix(nc, p["accent"], 0.15) + (255,))
        dn.rectangle([wx - 134, wy - 150, wx - 116, wy], fill=mix(nc, p["moon"], 0.1) + (255,))
        cx_, cy_ = wx + 70, wy - 170                                                          # cat on the rim
        dn.ellipse([cx_ - 22, cy_ - 30, cx_ + 18, cy_ + 4], fill=p["near"] + (255,))
        dn.ellipse([cx_ + 8, cy_ - 46, cx_ + 30, cy_ - 24], fill=p["near"] + (255,))
        dn.polygon([(cx_ + 10, cy_ - 40), (cx_ + 13, cy_ - 54), (cx_ + 18, cy_ - 42)], fill=p["near"] + (255,))
        dn.polygon([(cx_ + 21, cy_ - 42), (cx_ + 27, cy_ - 54), (cx_ + 29, cy_ - 38)], fill=p["near"] + (255,))
        dn.line([(cx_ - 20, cy_ - 2), (cx_ - 42, cy_ + 6), (cx_ - 50, cy_ + 30)], fill=p["near"] + (255,), width=5, joint="curve")
        draw_figure(dn, W * 0.82, gy + 70, 1.15, p["near"], True, False)                      # old woman on her doorstep
        dn.rectangle([W * 0.79, gy + 70, W * 0.85, gy + 84], fill=p["near"] + (255,))
        sx, sy = W * 0.2, 470                                                                 # corner shrine with its lamp
        dn.rectangle([sx - 46, sy - 70, sx + 46, sy + 40], fill=mix(hc, (0, 0, 0), 0.2) + (255,))
        dn.polygon([(sx - 58, sy - 70), (sx, sy - 104), (sx + 58, sy - 70)], fill=mix(hc, (0, 0, 0), 0.4) + (255,))
        dn.rectangle([sx - 32, sy - 58, sx + 32, sy + 26], fill=mix(p["accent"], p["mid"], 0.45) + (255,))
        dn.ellipse([sx - 14, sy - 46, sx + 14, sy - 18], fill=mix(p["accent"], p["moon"], 0.35) + (255,))
        dn.polygon([(sx - 20, sy + 24), (sx - 8, sy - 14), (sx + 8, sy - 14), (sx + 20, sy + 24)], fill=mix(p["accent"], (40, 50, 90), 0.4) + (255,))
        dn.rectangle([sx - 40, sy + 40, sx + 40, sy + 48], fill=mix(hc, (0, 0, 0), 0.4) + (255,))
        dn.chord([sx - 12, sy + 48, sx + 12, sy + 74], 0, 180, fill=mix(p["accent"], p["near"], 0.4) + (255,))
        self.near = near; self.lamp = (sx, sy + 58); self.lamp_r = 520
        self.fog_y = gy + 20; self.fog_a = 0.1; self.particles = "mist"

    def build_rialto(self):
        """The old wooden bridge at Rialto: two timber ramps lined with small shuttered shops rising to a raised
        centre section that could be lifted for tall masts, piers in the water, palazzi on both banks."""
        p, rng = self.p, self.rng; hy = int(H * 0.62)
        self.back = self.sky(hy - 300, (0.24, 0.15), 38)
        self._water(hy, 0.25)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        self._palazzi(d, -40, W + 40, hy - 4, mix(p["mid"], p["far"], 0.5), 0.72, 0.26, maxh=480)
        d.rectangle([0, hy - 6, W, hy + 2], fill=mix(p["mid"], (0, 0, 0), 0.3) + (255,))
        br = Image.new("RGBA", (W, H), (0, 0, 0, 0)); db = ImageDraw.Draw(br)
        wc = mix(p["near"], p["mid"], 0.55); wl = mix(wc, p["moon"], 0.1)
        c0, c1 = W * 0.44, W * 0.56; ytop = hy - 230; yend = hy - 40
        def deck(x):
            if c0 <= x <= c1: return ytop
            u = (c0 - x) / c0 if x < c0 else (x - c1) / (W - c1)
            return ytop + (yend - ytop) * min(1, max(0, u)) ** 0.9
        xs_ = np.linspace(-20, W + 20, 120)
        top = [(x, deck(x)) for x in xs_]
        db.polygon(top + [(W + 20, deck(W + 20) + 40), (c1 + 10, ytop + 52)] + [(c0 - 10, ytop + 52), (-20, deck(-20) + 40)], fill=wc + (255,))
        db.line(top, fill=wl + (255,), width=3)
        for x in np.arange(60, W, 150):                                                       # timber piers and braces
            if c0 - 30 < x < c1 + 30: continue
            y0 = deck(x) + 36; db.rectangle([x - 9, y0, x + 9, hy + 26], fill=wc + (255,))
            db.line([(x, hy + 10), (x + 70 * (1 if x < W / 2 else -1), y0 + 6)], fill=wc + (255,), width=6)
        for x in (c0 - 24, c1 + 24):                                                          # heavy posts beside the lifting span
            db.rectangle([x - 16, ytop - 30, x + 16, hy + 30], fill=wc + (255,))
        for x0, x1 in ((W * 0.05, c0 - 60), (c1 + 60, W * 0.95)):                             # rows of little shops on the ramps
            n = int((x1 - x0) / 92)
            for i in range(n):
                sx = x0 + (i + 0.5) * (x1 - x0) / n; y = deck(sx)
                db.rectangle([sx - 42, y - 78, sx + 42, y + 2], fill=mix(wc, p.get("brick", (110, 60, 50)), 0.15) + (255,))
                db.polygon([(sx - 48, y - 76), (sx, y - 108), (sx + 48, y - 76)], fill=mix(wc, (0, 0, 0), 0.25) + (255,))
                db.rectangle([sx - 26, y - 62, sx + 26, y - 8], fill=mix(wc, p["accent"], 0.12) + (255,))
                for k in range(4): db.line([(sx - 26, y - 62 + k * 14), (sx + 26, y - 62 + k * 14)], fill=wc + (255,), width=1)
        db.line([(c0 - 10, ytop - 30), (c1 + 10, ytop - 30)], fill=wc + (255,), width=5)        # rail over the centre
        for x in np.arange(c0, c1 + 1, 24): db.line([(x, ytop - 30), (x, ytop)], fill=wc + (255,), width=3)
        for x in (c0 - 24, c1 + 24):
            self.windows.append((x, ytop - 46, 10, 16, 0.3 + x, 2)); self.wlights.append((x, 26, 150, 0.5 * x))
        mid.alpha_composite(br)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, H), (0, H - 170), (W * 0.18, H - 140), (W * 0.22, H)], fill=nc + (255,))   # fondamenta corner
        for k in range(4): dn.ellipse([W * 0.03 + k * 70, H - 186, W * 0.03 + k * 70 + 34, H - 160], fill=mix(nc, p["accent"], 0.15) + (255,))  # baskets
        dn.rectangle([W * 0.94, H - 420, W * 0.94 + 22, H], fill=nc + (255,))
        self.near = near
        self.gondola = dict(y=hy + 150, s=0.6, dir=-1)
        self.fog_y = hy + 10; self.fog_a = 0.1; self.particles = "mist"

    def build_lagoon(self):
        """Open lagoon: the low skyline of the city, a domed island church with its campanile, leaning bundles of
        mooring posts with a heron, the warm far glow of the Murano furnaces trembling on the water."""
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy, (0.6, 0.2), 44)
        self._water(hy, 0.35)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)
        fc = mix(p["far"], p["horizon"], 0.42); r2 = random.Random(int(rng.integers(1e6)))
        x = W * 0.22
        while x < W * 0.66:                                                                   # low city skyline
            w = r2.uniform(20, 60); h = r2.uniform(14, 40)
            df.rectangle([x, hy - h, x + w, hy], fill=fc + (255,))
            if r2.random() < 0.18:
                df.rectangle([x + w / 2 - 6, hy - h - r2.uniform(50, 110), x + w / 2 + 6, hy - h], fill=fc + (255,))
            if r2.random() < 0.1: df.chord([x, hy - h - 26, x + w, hy - h + 20], 180, 360, fill=fc + (255,))
            if r2.random() < 0.35: self.windows.append((x + w / 2, hy - h / 2, 3, 3, r2.uniform(0, TAU), 1)); self.wlights.append((x + w / 2, 6, 70, r2.uniform(0, TAU)))
            x += w
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1.2)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        ic = mix(p["far"], p["mid"], 0.45); ix = W * 0.8                                     # island church: dome, front, campanile
        d.rectangle([ix - 230, hy - 26, ix + 230, hy + 4], fill=ic + (255,))
        d.rectangle([ix - 110, hy - 150, ix + 60, hy - 26], fill=ic + (255,))
        d.polygon([(ix - 120, hy - 150), (ix - 25, hy - 200), (ix + 70, hy - 150)], fill=ic + (255,))
        for k in range(4): d.rectangle([ix - 96 + k * 44, hy - 146, ix - 88 + k * 44, hy - 30], fill=mix(ic, p["moon"], 0.12) + (255,))
        d.rectangle([ix + 50, hy - 210, ix + 120, hy - 26], fill=ic + (255,))
        d.chord([ix + 40, hy - 290, ix + 130, hy - 140], 180, 360, fill=ic + (255,))
        d.line([(ix + 85, hy - 290), (ix + 85, hy - 316)], fill=ic + (255,), width=3)
        d.rectangle([ix + 150, hy - 300, ix + 186, hy - 26], fill=ic + (255,))
        d.polygon([(ix + 146, hy - 300), (ix + 168, hy - 360), (ix + 190, hy - 300)], fill=ic + (255,))
        self.windows.append((ix - 25, hy - 60, 6, 9, 1.1, 1)); self.wlights.append((ix - 25, 14, 110, 1.1))
        rf = mid.crop((0, hy - 380, W, hy)).transpose(Image.FLIP_TOP_BOTTOM)                  # still reflection of the island
        a = np.array(rf); a[..., 3] = (a[..., 3] * np.linspace(0.32, 0.0, a.shape[0])[:, None]).astype(np.uint8)
        rfl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rfl.alpha_composite(Image.fromarray(a, "RGBA"), (0, hy + 4))
        self.back.alpha_composite(rfl.filter(ImageFilter.GaussianBlur(2)))
        self.mid = mid
        gx = W * 0.07; self.glowspot = (gx, hy - 6, 420)                                      # Murano furnaces
        self.wlights.append((gx + 60, 120, 120, 0.2)); self.wlights.append((gx + 160, 60, 90, 2.0))
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        for bx, base, h, s in ((W * 0.16, H - 40, 470, 1.0), (W * 0.42, hy + 210, 230, 0.55), (W * 0.62, hy + 120, 130, 0.35)):
            for k, lean in enumerate((-0.07, 0.0, 0.08)):                                  # bundle of three posts, tied at the top
                x0 = bx + (k - 1) * 30 * s; xt = bx + (k - 1) * 8 * s + lean * h * 0.3
                dn.line([(x0, base), (xt, base - h)], fill=nc + (255,), width=max(3, int(16 * s)))
            dn.rectangle([bx - 22 * s, base - h * 0.86, bx + 22 * s, base - h * 0.82], fill=mix(nc, p["moon"], 0.12) + (255,))
            for j in range(6):                                                                # wobbly reflection
                y = base + 8 + j * 14 * s; dn.line([(bx - 20 * s + (j % 2) * 8 * s, y), (bx + 20 * s + (j % 2) * 8 * s, y)], fill=nc + (int(150 - j * 22),), width=max(2, int(6 * s)))
        hx, hb = W * 0.21, H - 120                                                            # heron on one leg on a low post
        dn.rectangle([hx - 10, hb, hx + 10, H], fill=nc + (255,))
        dn.line([(hx, hb), (hx + 2, hb - 70)], fill=nc + (255,), width=4)
        dn.ellipse([hx - 40, hb - 112, hx + 34, hb - 64], fill=nc + (255,))
        dn.line([(hx + 24, hb - 100), (hx + 40, hb - 140), (hx + 30, hb - 168), (hx + 44, hb - 182)], fill=nc + (255,), width=9, joint="curve")
        dn.ellipse([hx + 36, hb - 192, hx + 58, hb - 174], fill=nc + (255,))
        dn.polygon([(hx + 56, hb - 186), (hx + 96, hb - 180), (hx + 56, hb - 178)], fill=nc + (255,))
        self.near = near
        mx, my, mr = self.moon; self.reflect = (mx, hy + 4, mr)
        self.gondola = dict(y=hy + 60, s=0.3, dir=1)
        self.fog_y = hy + 6; self.fog_a = 0.2; self.particles = "mist"

    # --- EP07 Lighthouse keepers: headland / lantern / rocktower / watchroom
    def _tower(self, d, cx, base, h, wb, wt, s=1.0, flare=0.0, lit=True):
        """Tapered white tower, shaded from the moonlit side; optional concave flare at the foot (rock towers).
        Gallery with railing, lantern with diagonal astragals, dome and ventilator ball. Returns the lamp centre."""
        p = self.p; chalk = p.get("chalk", (206, 208, 200)); n = 28
        lit_c = mix(chalk, p["moon"], 0.1); dark_c = mix(chalk, p["mid"], 0.72)
        def half(v):  # half-width at height fraction v (0 = foot)
            hw = wb / 2 + (wt / 2 - wb / 2) * v
            if flare: hw += flare * wb * 0.5 * max(0.0, 1 - v / 0.3) ** 2.2
            return hw
        vs = np.linspace(0, 1, 30)
        for i in range(n):
            u0, u1 = i / n, (i + 1) / n
            sh = smooth(1 - abs((u0 + u1) / 2 - 0.7) / 0.7)                                   # moon from the right
            col = mix(dark_c, lit_c, 0.15 + 0.85 * sh)
            left = [(cx - half(v) + 2 * half(v) * u0, base - v * h) for v in vs]
            right = [(cx - half(v) + 2 * half(v) * u1, base - v * h) for v in vs[::-1]]
            d.polygon(left + right, fill=col + (255,))
        for k in range(1, 5):                                                                 # small windows up the stair
            v = k / 5.4; y = base - v * h; x = cx + half(v) * (0.25 if k % 2 else -0.2)
            d.rectangle([x - 4 * s, y - 9 * s, x + 4 * s, y + 9 * s], fill=mix(dark_c, (0, 0, 0), 0.5) + (255,))
            if lit and k == 4: self.windows.append((x, y, 6 * s, 14 * s, 0.7, 1))
        top = base - h; gw = wt / 2 + 22 * s; ic = (14, 15, 19)
        d.rectangle([cx - gw, top - 10 * s, cx + gw, top + 6 * s], fill=ic + (255,))          # gallery deck + railing
        d.line([(cx - gw, top - 30 * s), (cx + gw, top - 30 * s)], fill=ic + (255,), width=max(1, int(3 * s)))
        for k in range(9): d.line([(cx - gw + k * gw / 4, top - 30 * s), (cx - gw + k * gw / 4, top - 10 * s)], fill=ic + (255,), width=max(1, int(2 * s)))
        lw, lh = wt / 2 - 4 * s, 64 * s; ly0 = top - 10 * s - lh
        d.rectangle([cx - lw, ly0, cx + lw, top - 10 * s], fill=mix(p["light"], (255, 250, 236), 0.4) + (255,))
        for k in range(-3, 4):                                                                # diagonal astragals (Scottish lanterns)
            x0 = cx + k * lw / 2.2; d.line([(x0 - lw / 3, top - 10 * s), (x0 + lw / 3, ly0)], fill=ic + (255,), width=max(1, int(3 * s)))
        d.line([(cx - lw, ly0), (cx - lw, top - 10 * s)], fill=ic + (255,), width=max(1, int(4 * s)))
        d.line([(cx + lw, ly0), (cx + lw, top - 10 * s)], fill=ic + (255,), width=max(1, int(4 * s)))
        d.chord([cx - lw - 4 * s, ly0 - 40 * s, cx + lw + 4 * s, ly0 + 26 * s], 180, 360, fill=ic + (255,))  # dome
        d.line([(cx, ly0 - 40 * s), (cx, ly0 - 58 * s)], fill=ic + (255,), width=max(1, int(3 * s)))
        d.ellipse([cx - 7 * s, ly0 - 70 * s, cx + 7 * s, ly0 - 56 * s], fill=ic + (255,))
        return (cx, ly0 + lh * 0.5)

    def _foam_line(self, pts, n=1):
        """Foam along the rocks: stored as polylines that brighten and fade like slow breathing."""
        self.foam.append((pts, self.rng.uniform(0, TAU), n))

    def build_headland(self):
        """White tower on a dark cliff, keepers' cottages and walled garden beside it, smoke from a chimney, a slow
        lighthouse beam sweeping over the sea (two turns per loop), moon path on the water, foam at the cliff foot."""
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy, (0.2, 0.18), 40)
        self._water(hy, 0.3)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)               # far coast across a firth
        fc = mix(p["far"], p["horizon"], 0.4); xs = np.arange(0, W * 0.42, 6)
        nz = noise1d(len(xs), int(rng.integers(1e6)), 4, 3)
        df.polygon([(0, hy)] + [(x, hy - 26 - 22 * v - 40 * max(0, 1 - x / (W * 0.25))) for x, v in zip(xs, nz)] + [(W * 0.42, hy)], fill=fc + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1.5)))
        self.wlights.append((W * 0.08, 8, 60, 0.4))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); cc = p["mid"]
        r3 = random.Random(int(rng.integers(1e6))); gy = hy - 120                           # ground level on top
        face = [(W * 0.36 + 0.2 * W * (k / 16) ** 0.8 + r3.uniform(-14, 14), H - (H - gy + 4) * (k / 16) ** 0.9 + r3.uniform(-10, 10)) for k in range(17)]
        cl = [(W * 0.3, H)] + face + [(W * 0.7, gy - 4), (W * 0.86, gy - 8), (W, gy - 16), (W, H)]
        d.polygon(cl, fill=cc + (255,))                                                       # the headland
        for k in range(7):                                                                    # rock strata catching moonlight
            fx, fy = face[2 + k * 2]; d.line([(fx + 6, fy), (fx + 160, fy - 30), (W, fy - 60)], fill=mix(cc, p["moon"], 0.07) + (255,), width=2)
        chalk = p.get("chalk", (206, 208, 200)); cot = mix(chalk, p["mid"], 0.45); roof = mix(p["mid"], (0, 0, 0), 0.35)
        d.rectangle([W * 0.6, gy - 34, W * 0.98, gy + 4], fill=mix(cot, p["mid"], 0.35) + (255,))  # garden wall
        for k in range(30): d.line([(W * 0.6 + k * 24, gy - 34), (W * 0.6 + k * 24 + 12, gy - 34)], fill=mix(cot, p["moon"], 0.2) + (255,), width=3)
        for x0, w, h in ((W * 0.66, 210, 70), (W * 0.79, 160, 60)):                          # two cottages
            d.rectangle([x0, gy - h, x0 + w, gy], fill=cot + (255,))
            d.polygon([(x0 - 10, gy - h), (x0 + w / 2, gy - h - 56), (x0 + w + 10, gy - h)], fill=roof + (255,))
            d.rectangle([x0 + w - 30, gy - h - 74, x0 + w - 12, gy - h - 30], fill=roof + (255,))   # chimney
            d.rectangle([x0 + w * 0.42, gy - 38, x0 + w * 0.58, gy], fill=mix(roof, (0, 0, 0), 0.4) + (255,))
            for wx in (x0 + w * 0.2, x0 + w * 0.8):
                d.rectangle([wx - 12, gy - 50, wx + 12, gy - 22], fill=mix(roof, (0, 0, 0), 0.3) + (255,))
                if rng.random() < 0.7: self.windows.append((wx, gy - 36, 18, 22, rng.uniform(0, TAU), 1))
        self.smoke = (W * 0.66 + 210 - 21, gy - 70 - 74, 260)
        d.line([(W * 0.95, gy), (W * 0.95, gy - 190)], fill=roof + (255,), width=4)          # flagstaff
        d.line([(W * 0.95, gy - 170), (W * 0.975, gy - 170)], fill=roof + (255,), width=2)
        self.beam_src = self._tower(d, W * 0.6, gy + 6, 330, 92, 62, 1.0)
        self.mid = mid
        mx, my, mr = self.moon; self.reflect = (mx, hy + 4, mr)
        self.foam = []
        for k in range(3):                                                                    # foam along the foot of the cliff
            y0 = hy + 30 + k * 150; xs_ = [x for x, y in face if abs(y - y0) < 90] or [W * 0.45]
            xe = min(xs_); self._foam_line([(xe - 220 + j * 34, y0 + 26 + 5 * math.sin(j * 1.3 + k) + j * 2) for j in range(7)], k % 3 + 1)
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, H), (0, H - 120), (W * 0.1, H - 150), (W * 0.22, H - 110), (W * 0.32, H - 40), (W * 0.36, H)], fill=nc + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        for _ in range(60):                                                                   # grass tussocks and sea pinks
            x = r2.uniform(0, W * 0.3); yb = H - 110 - 40 * math.sin(x / W * 9) + r2.uniform(0, 40)
            for j in range(4): dn.line([(x, yb), (x + r2.uniform(-14, 14), yb - r2.uniform(18, 46))], fill=nc + (255,), width=2)
            if r2.random() < 0.3: dn.ellipse([x - 5, yb - 52, x + 5, yb - 42], fill=mix(nc, (200, 150, 170), 0.18) + (255,))
        self.near = near
        self.beam = dict(L=2300, spread=210, a=0.3)
        self.fog_y = hy + 4; self.fog_a = 0.1; self.particles = "spray"

    def build_rocktower(self):
        """A tall granite rock tower far out at sea (curved, flared foot) on a low reef ringed with foam, its beam
        turning; a two-masted schooner with stern lantern and sidelights sails across each loop; dark rocks in front."""
        p, rng = self.p, self.rng; hy = int(H * 0.63)
        self.back = self.sky(hy, (0.78, 0.17), 38)
        self._water(hy, 0.32)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)
        df.polygon([(W * 0.0, hy), (W * 0.06, hy - 18), (W * 0.15, hy - 10), (W * 0.2, hy)], fill=mix(p["far"], p["horizon"], 0.5) + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(2)))
        self.windows.append((W * 0.09, hy - 20, 3, 3, 0.0, 3))                                 # a far light on the island
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        tx = W * 0.4; rb = hy + 18
        d.polygon([(tx - 150, rb + 8), (tx - 110, rb - 10), (tx - 40, rb - 16), (tx + 60, rb - 14), (tx + 140, rb - 4), (tx + 170, rb + 8)], fill=p["mid"] + (255,))
        self.beam_src = self._tower(d, tx, rb - 12, 330, 54, 36, 0.62, flare=1.1)
        self.mid = mid
        mx, my, mr = self.moon; self.reflect = (mx, hy + 4, mr)
        self.foam = []
        self._foam_line([(tx - 170 + j * 30, rb + 10 + 3 * math.sin(j)) for j in range(12)], 2)
        self._foam_line([(tx - 120 + j * 26, rb + 22 + 3 * math.sin(j * 2)) for j in range(9)], 1)
        self.wlights.append((tx, 10, 90, 0.9))
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(W * 0.72, H), (W * 0.78, H - 90), (W * 0.86, H - 120), (W * 0.95, H - 96), (W, H - 140), (W, H)], fill=nc + (255,))
        dn.polygon([(0, H), (0, H - 60), (W * 0.08, H - 74), (W * 0.15, H - 30), (W * 0.18, H)], fill=nc + (255,))
        for k in range(18):                                                                   # seaweed fringe
            x = W * 0.74 + k * 26; dn.line([(x, H - 70 - 30 * math.sin(k)), (x + 6, H - 40)], fill=mix(nc, (40, 50, 30), 0.3) + (255,), width=3)
        self._foam_line([(W * 0.7 + j * 40, H - 40 + 6 * math.sin(j)) for j in range(8)], 3)
        self.near = near
        self.ship = dict(y=hy + 70, s=0.42, dir=1)
        self.beam = dict(L=1900, spread=150, a=0.28)
        self.fog_y = hy - 4; self.fog_a = 0.12; self.particles = "spray"

    def build_lantern(self):
        """Inside the lantern: the beehive Fresnel lens (prism rings above and below a belt of bull's-eye panels,
        brass frame) glowing round its lamp; panels turn slowly; diagonal storm panes with sky and sea behind."""
        p, rng = self.p, self.rng; hy = int(H * 0.66)
        sky = self.sky(hy, (0.86, 0.2), 30)
        sea = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sea)
        for y in range(hy, H): ds.line([(0, y), (W, y)], fill=mix(mix(p["sea"], p["horizon"], 0.3), p["sea"], ((y - hy) / (H - hy)) ** 0.5) + (255,))
        sky.alpha_composite(sea)
        base = np.array(sky.convert("RGB"), np.float32)
        cx, cy = W * 0.5, H * 0.5
        base += radial_glow(cx, cy, 720, p["light"], 0.20) + radial_glow(cx, cy, 300, p["light"], 0.18)
        img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA"); d = ImageDraw.Draw(img)
        fr = (16, 16, 20, 255); fr2 = mix((16, 16, 20), p["light"], 0.25) + (255,)
        for k in range(-9, 10):                                                               # diagonal astragals of the glazing
            x0 = W / 2 + k * 230; d.line([(x0 - 260, H * 0.86), (x0 + 260, H * 0.08)], fill=fr, width=10)
        d.rectangle([0, 0, W, H * 0.1], fill=fr); d.rectangle([0, H * 0.84, W, H], fill=fr)
        for k in range(8): d.line([(W * k / 7, H * 0.1), (W * k / 7, H * 0.84)], fill=fr, width=22)   # mullions
        d.line([(0, H * 0.1), (W, H * 0.1)], fill=fr2, width=3)
        self.stars_tw = [s for s in self.stars_tw if s[1] > H * 0.12]
        lw, top, bot = 250, H * 0.13, H * 0.86                                                # the lens: a glass beehive
        belt0, belt1 = cy - 110, cy + 110; ht = (bot - 70 - top - 30) / 2; lc = (top + 30 + bot - 70) / 2
        prof = lambda y: lw * max(0.0, 1 - ((y - lc) / (ht * 1.08)) ** 2) ** 0.42
        d.ellipse([cx - lw * 0.8, belt0 - 160, cx + lw * 0.8, belt1 + 160], fill=mix(p["mid"], p["light"], 0.3) + (255,))
        y = top + 34; i = 0
        while y < bot - 80:
            if belt0 - 8 < y < belt1 + 8: y = belt1 + 10; continue
            hgt = 15 if y < belt0 else 17; w0, w1 = prof(y), prof(y + hgt)
            v = 0.5 + 0.5 * math.sin(i * 1.7)
            gc = mix(mix(p["mid"], p["light"], 0.28 + 0.22 * v), (255, 246, 226), 0.06 + 0.1 * (1 - abs(y - cy) / (bot - cy)))
            d.polygon([(cx - w0, y), (cx + w0, y), (cx + w1, y + hgt - 3), (cx - w1, y + hgt - 3)], fill=gc + (255,))
            hl = (y + 1) if y < belt0 else (y + hgt - 4)
            d.line([(cx - w0 * 0.8, hl), (cx + w0 * 0.8, hl)], fill=mix(p["light"], (255, 255, 255), 0.7) + (int(110 + 90 * v),), width=2)
            y += hgt; i += 1
        d.rectangle([cx - lw, belt0, cx + lw, belt1], fill=mix(p["mid"], p["light"], 0.38) + (255,))
        for k in range(-4, 5):                                                                # brass frame bars
            x = cx + lw * math.sin(k / 4 * math.pi / 2.2) * 0.97
            ys_ = [yy for yy in range(int(top + 34), int(bot - 74), 4) if prof(yy) > abs(x - cx) + 3 or belt0 <= yy <= belt1]
            if ys_: d.line([(x, ys_[0]), (x, ys_[-1])], fill=(70, 54, 30, 255), width=4)
        d.rectangle([cx - lw - 8, belt0 - 6, cx + lw + 8, belt0 + 3], fill=(96, 74, 40, 255))
        d.rectangle([cx - lw - 8, belt1 - 3, cx + lw + 8, belt1 + 6], fill=(96, 74, 40, 255))
        d.chord([cx - 60, top + 4, cx + 60, top + 56], 180, 360, fill=(70, 54, 30, 255))
        d.rectangle([cx - 150, bot - 70, cx + 150, H], fill=(30, 26, 22, 255))               # pedestal
        d.rectangle([cx - 190, bot - 76, cx + 190, bot - 56], fill=(60, 48, 30, 255))
        self.back = img
        self.lensp = dict(cx=cx, lw=lw, y0=belt0, y1=belt1)
        self.lamp = (cx, cy + 30); self.lamp_r = 440
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"] + (255,)
        dn.rectangle([0, H * 0.9, W, H], fill=nc)                                             # floor
        for k in range(12): dn.line([(k * 170, H * 0.9), (k * 170 - 60, H)], fill=mix(p["near"], p["light"], 0.08) + (255,), width=2)
        dn.line([(W * 0.06, H), (W * 0.06, H * 0.42)], fill=nc, width=14)                      # hatch ladder rail
        dn.line([(W * 0.1, H), (W * 0.1, H * 0.42)], fill=nc, width=14)
        for k in range(6): dn.line([(W * 0.06, H * 0.48 + k * 90), (W * 0.1, H * 0.48 + k * 90)], fill=nc, width=10)
        ox, oy = W * 0.84, H * 0.9                                                            # oil can and folded cloth
        dn.rectangle([ox - 36, oy - 70, ox + 36, oy], fill=mix(p["near"], p["accent"], 0.18) + (255,))
        dn.line([(ox + 30, oy - 60), (ox + 80, oy - 100)], fill=mix(p["near"], p["accent"], 0.18) + (255,), width=6)
        dn.rectangle([ox - 160, oy - 22, ox - 70, oy], fill=mix(p["near"], (220, 214, 196), 0.25) + (255,))
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); self.near = near
        self.particles = "dust"; self.fog_a = 0

    def build_watchroom(self):
        """The keepers' round room in the tower: curved stone courses, a curved box bunk with a curtain, a cast-iron
        stove with glowing door and kettle, a wall clock, the table with open logbook and oil lamp, and a deep round
        window where the beam sweeps across the sea."""
        p, rng = self.p, self.rng; vx = W * 0.5
        wallc = mix(p["mid"], p["light"], 0.12)
        base = np.zeros((H, W, 3), np.float32) + np.array(wallc, np.float32)
        xx = np.arange(W, dtype=np.float32)[None, :, None]
        base *= (0.55 + 0.45 * np.cos((xx - vx) / W * math.pi * 0.95))                        # curvature shading
        base += radial_glow(W * 0.6, H * 0.72, 650, p["light"], 0.10)
        img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")
        wx, wy, wr = vx - 10, H * 0.34, 150                                                   # deep round window
        sky = self.sky(int(H * 0.4), (0.47, 0.25), 16)
        sea = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sea)
        for y in range(int(H * 0.4), H): ds.line([(0, y), (W, y)], fill=mix(p["sea"], p["horizon"], 0.25) + (255,))
        sky.alpha_composite(sea)
        m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([wx - wr, wy - wr, wx + wr, wy + wr], fill=255)
        img.paste(sky, (0, 0), m)
        self.stars_tw = [s for s in self.stars_tw if math.hypot(s[0] - wx, s[1] - wy) < wr - 10]
        self.win = (wx, wy, wr)
        d = ImageDraw.Draw(img)
        d.ellipse([wx - wr - 34, wy - wr - 34, wx + wr + 34, wy + wr + 34], outline=mix(wallc, (0, 0, 0), 0.5) + (255,), width=34)
        d.line([(wx - wr, wy), (wx + wr, wy)], fill=(20, 18, 18, 255), width=6); d.line([(wx, wy - wr), (wx, wy + wr)], fill=(20, 18, 18, 255), width=6)
        for k in range(9):                                                                    # curved stone courses
            y = H * 0.06 + k * 110
            pts = [(x, y + 26 * math.cos((x - vx) / W * math.pi)) for x in range(0, W + 1, 40)]
            d.line(pts, fill=mix(wallc, (0, 0, 0), 0.32) + (255,), width=2)
        cx_, cy_ = W * 0.74, H * 0.2                                                          # wall clock
        d.ellipse([cx_ - 46, cy_ - 46, cx_ + 46, cy_ + 46], fill=(40, 30, 22, 255)); d.ellipse([cx_ - 36, cy_ - 36, cx_ + 36, cy_ + 36], fill=mix((230, 220, 196), p["mid"], 0.4) + (255,))
        d.line([(cx_, cy_), (cx_ + 4, cy_ - 26)], fill=(20, 18, 16, 255), width=3); d.line([(cx_, cy_), (cx_ + 20, cy_ + 8)], fill=(20, 18, 16, 255), width=3)
        bk = mix(p["near"], p["light"], 0.08)                                                 # curved box bunk, left
        d.polygon([(0, H * 0.3), (W * 0.26, H * 0.36), (W * 0.26, H * 0.66), (0, H * 0.72)], fill=bk + (255,))
        d.polygon([(10, H * 0.34), (W * 0.24, H * 0.39), (W * 0.24, H * 0.6), (10, H * 0.64)], fill=mix(bk, (0, 0, 0), 0.5) + (255,))
        cur = mix(mix(p["accent"], (120, 60, 50), 0.4), p["near"], 0.62)
        for k in range(9):                                                                    # half-drawn curtain folds
            x = 10 + k * 26; d.polygon([(x, H * 0.34 + k * 2), (x + 26, H * 0.34 + k * 2.4), (x + 22, H * 0.62 - k * 2), (x - 4, H * 0.63 - k * 2)], fill=mix(cur, (0, 0, 0), 0.15 * (k % 2)) + (255,))
        d.rectangle([W * 0.11, H * 0.52, W * 0.23, H * 0.6], fill=mix((150, 120, 96), p["near"], 0.55) + (255,))   # folded blanket
        sx, sy = W * 0.8, H * 0.86                                                            # stove, right
        sc = (22, 20, 20, 255)
        d.rectangle([sx - 110, sy - 230, sx + 110, sy], fill=sc)
        d.rectangle([sx - 124, sy - 246, sx + 124, sy - 226], fill=sc)
        d.rectangle([sx - 20, 0, sx + 20, sy - 246], fill=sc)
        d.rounded_rectangle([sx - 60, sy - 170, sx + 60, sy - 90], radius=10, fill=(255, 150, 70, 255))
        for k in range(5): d.line([(sx - 50 + k * 25, sy - 168), (sx - 50 + k * 25, sy - 92)], fill=sc, width=6)
        self.glowspot = (sx, sy - 130, 230)
        kx = sx - 40; d.ellipse([kx - 52, sy - 300, kx + 52, sy - 240], fill=(36, 32, 30, 255))  # kettle
        d.rectangle([kx - 46, sy - 272, kx + 46, sy - 246], fill=(36, 32, 30, 255))
        d.arc([kx - 34, sy - 332, kx + 34, sy - 270], 180, 360, fill=(36, 32, 30, 255), width=6)
        d.line([(kx + 46, sy - 268), (kx + 84, sy - 292)], fill=(36, 32, 30, 255), width=10)
        self.smoke = (kx + 86, sy - 300, 140)
        self.back = img
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(W * 0.18, H), (W * 0.24, H * 0.78), (W * 0.66, H * 0.78), (W * 0.7, H)], fill=mix(nc, p["light"], 0.1) + (255,))   # table
        dn.line([(W * 0.24, H * 0.78), (W * 0.66, H * 0.78)], fill=mix(nc, p["light"], 0.25) + (255,), width=4)
        bx, by = W * 0.38, H * 0.84                                                           # open logbook with ruled lines
        dn.polygon([(bx - 160, by + 40), (bx - 140, by - 34), (bx, by - 26), (bx, by + 46)], fill=mix((232, 222, 196), p["mid"], 0.25) + (255,))
        dn.polygon([(bx, by + 46), (bx, by - 26), (bx + 140, by - 34), (bx + 160, by + 40)], fill=mix((232, 222, 196), p["mid"], 0.2) + (255,))
        for k in range(6):
            y = by - 18 + k * 10; dn.line([(bx - 136 + k * 2, y), (bx - 12, y + 2)], fill=mix((120, 110, 100), p["mid"], 0.3) + (255,), width=1)
            dn.line([(bx + 12, y + 2), (bx + 136 - k * 2, y)], fill=mix((120, 110, 100), p["mid"], 0.3) + (255,), width=1)
        dn.line([(bx + 60, by - 4), (bx + 180, by - 50)], fill=(30, 26, 22, 255), width=4)       # pen
        mg = (W * 0.22, H * 0.8)                                                              # mug
        dn.rectangle([W * 0.27, H * 0.77, W * 0.3, H * 0.83], fill=mix(nc, p["accent"], 0.3) + (255,))
        lx, ly = W * 0.56, H * 0.79                                                           # oil lamp with glass chimney
        dn.ellipse([lx - 46, ly - 22, lx + 46, ly + 8], fill=mix(nc, p["accent"], 0.35) + (255,))
        dn.rectangle([lx - 8, ly - 50, lx + 8, ly - 18], fill=mix(nc, p["accent"], 0.35) + (255,))
        self.lamp = (lx, ly - 66); self.lamp_r = 380
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); self.near = near
        self.particles = "dust"; self.fog_a = 0

    def _beam(self, img, ph):
        """EP07: the light turning twice per loop. The cone reaches far when it points across the view, widens and
        brightens as it swings towards us (the flash), and dims as it turns away. Drawn at 1/4 size, then blurred."""
        B = self.beam; lx, ly = self.beam_src; p = self.p
        th = ph * 2; c, s = math.cos(th), math.sin(th)
        q = 4; lay = Image.new("RGBA", (W // q, H // q), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        toward = max(0.0, s); away = max(0.0, -s)
        L = B["L"] * (abs(c) * 0.9 + 0.1); hw = B["spread"] * (0.25 + 1.6 * toward ** 2)
        ex, ey = lx + c * L, ly + 14 + L * 0.02
        a = B["a"] * (0.35 + 0.65 * toward) * (1 - 0.6 * away)
        col = mix(p["light"], (255, 250, 236), 0.55)
        N = 14                                                                                # fades out along its length
        for i in range(N):
            f0, f1 = i / N, (i + 1) / N; fade = (1 - (f0 + f1) / 2) ** 1.3
            for k, f in enumerate((1.0, 0.55, 0.25)):
                pts = [(lx + (ex - lx) * g, ly + (ey - ly) * g + sg * (3 + (hw * f - 3) * g)) for g, sg in ((f0, -1), (f1, -1), (f1, 1), (f0, 1))]
                d.polygon([(x_ / q, y_ / q) for x_, y_ in pts], fill=col + (int(255 * a * (0.35 + k * 0.3) * fade),))
        lay = lay.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(10))
        img.alpha_composite(lay)
        fl = 0.25 + 0.75 * toward ** 6                                                        # the flash at the lantern
        R = int(70 + 260 * toward ** 4)
        img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R * 2)), (255, 244, 220), 0.75 * fl), (int(lx - R), int(ly - R)))

    def _foam(self, img, ph):
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); p = self.p
        for pts, f, n in self.foam:
            br = 0.5 + 0.5 * math.sin(ph * n + f)
            sh = 8 * math.sin(ph * n + f)
            d.line([(x + sh, y + br * 3) for x, y in pts], fill=mix(p["moon"], p["sea"], 0.15) + (int(60 + 150 * br),), width=4, joint="curve")
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.6)))

    def _lens(self, img, ph):
        """EP07: bull's-eye panels sliding round the belt of the lens (one turn per loop, 8 panels); the one facing
        us blazes; soft bands of light drift across the glazing behind."""
        L = self.lensp; cx, lw, y0, y1 = L["cx"], L["lw"], L["y0"], L["y1"]; p = self.p
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); r = (y1 - y0) / 2 - 8; cy = (y0 + y1) / 2
        for k in range(8):
            a = ph + k * TAU / 8; z = math.cos(a)
            if z <= 0: continue
            x = cx + lw * math.sin(a) * 0.96; rx = r * z ** 0.8
            b = z ** 10
            for j in range(5, 0, -1):
                rr = j / 5
                d.ellipse([x - rx * rr, cy - r * rr, x + rx * rr, cy + r * rr], outline=mix(p["light"], (255, 255, 255), 0.6) + (int(60 + 150 * z),), width=2)
            d.ellipse([x - rx * 0.2, cy - r * 0.2, x + rx * 0.2, cy + r * 0.2], fill=(255, 244, 214, int(70 + 185 * b)))
        img.alpha_composite(lay)
        for k in range(8):                                                                    # glare of the facing panel
            a = ph + k * TAU / 8; z = math.cos(a)
            if z > 0.8:
                x = cx + lw * math.sin(a) * 0.96; R = int(120 + 560 * ((z - 0.8) / 0.2) ** 3)
                img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R * 2)), (255, 246, 226), 0.55 * ((z - 0.8) / 0.2) ** 2), (int(x - R), int(cy - R)))
        for k in range(8):                                                                    # beams out the back crossing the glazing
            a = ph + k * TAU / 8 + math.pi; x = cx + math.sin(a) * W * 0.62
            if math.cos(a) < 0.2: continue
            band = Image.new("RGBA", (W // 8, H // 8), (0, 0, 0, 0)); bd = ImageDraw.Draw(band)
            bd.rectangle([(x - 60) / 8, H * 0.1 / 8, (x + 60) / 8, H * 0.84 / 8], fill=p["light"] + (int(40 * math.cos(a)),))
            img.alpha_composite(band.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(16)))

    def _winbeam(self, img, ph):
        """EP07 watchroom: the beam from above sweeps across the sea seen through the window, twice per loop."""
        wx, wy, wr = self.win; th = ph * 2; s = math.sin(th)
        x = wx + wr * 1.6 * math.cos(th); a = max(0.0, s) ** 2
        if a < 0.02: return
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        d.polygon([(x - 30, wy - wr), (x + 30, wy - wr), (x + 120, wy + wr), (x - 120, wy + wr)], fill=mix(self.p["light"], (255, 255, 255), 0.5) + (int(110 * a),))
        m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([wx - wr, wy - wr, wx + wr, wy + wr], fill=255)
        lay.putalpha(Image.fromarray(np.minimum(np.array(lay.getchannel("A")), np.array(m))))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(8)))

    def _ship(self, img, t, ph):
        """EP07: two-masted schooner crossing once per loop: pale gaff sails and jibs, stern lantern, red/green sidelights."""
        S_ = self.ship; s = S_["s"]; p = self.p; L = 420 * s; span = W + L * 2; u = t / LOOP_S
        x = -L + u * span; y = S_["y"] + 4 * s * math.sin(ph * 3)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); c = (8, 9, 12, 255)
        hull = [(x - L / 2, y - 26 * s), (x + L / 2 + 30 * s, y - 34 * s), (x + L / 2 - 10 * s, y + 6 * s), (x - L / 2 + 16 * s, y + 8 * s)]
        d.polygon([(px, 2 * y - py + 14 * s) for px, py in hull], fill=(4, 6, 10, 60))
        d.polygon(hull, fill=c)
        sail = mix(p["moon"], p["far"], 0.72) + (205,)
        for mxo, mh in ((-0.18, 300), (0.16, 340)):
            m0 = x + mxo * L
            d.line([(m0, y - 28 * s), (m0, y - mh * s)], fill=c, width=max(2, int(5 * s)))
            d.polygon([(m0 - 6 * s, y - (mh - 20) * s), (m0 - 150 * s, y - (mh - 80) * s), (m0 - 150 * s, y - 50 * s), (m0 - 6 * s, y - 44 * s)], fill=sail)
        bx = x + L / 2 + 30 * s
        d.line([(bx, y - 34 * s), (bx + 110 * s, y - 70 * s)], fill=c, width=max(2, int(4 * s)))         # bowsprit
        d.polygon([(x + 0.16 * L + 8 * s, y - 320 * s), (bx + 100 * s, y - 70 * s), (x + 0.16 * L + 14 * s, y - 50 * s)], fill=sail)
        img.alpha_composite(lay)
        fl = 0.85 + 0.15 * math.sin(ph * 5)
        for lx, ly, col, R in ((x - L / 2 + 6 * s, y - 40 * s, (255, 214, 150), 40), (x + L / 2, y - 40 * s, (120, 255, 150), 18)):
            img.alpha_composite(self.tint(self.glow_sm.resize((R * 2, R * 2)), col, 0.8 * fl), (int(lx - R), int(ly - R)))
            ImageDraw.Draw(img).ellipse([lx - 3, ly - 3, lx + 3, ly + 3], fill=col + (255,))
        d2 = ImageDraw.Draw(img); lx = x - L / 2 + 6 * s
        for j in range(5):
            yy = y + 16 * s + j * 8; ww = (12 - j * 2) * (0.7 + 0.3 * math.sin(ph * 5 + j))
            d2.line([(lx - ww, yy), (lx + ww, yy)], fill=(255, 214, 150, int(120 - j * 22)), width=2)

    def _wlights(self, img, ph):
        """EP06: lamplight trembling on the water below each lit window (periodic in LOOP_S)."""
        p = self.p; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); wy = self.water_y
        for x, w, a, f in self.wlights:
            n = max(4, int(a / 9))
            for j in range(n):
                y = wy + 5 + j * (6 + j * 0.9)
                off = 5 * math.sin(ph * 2 + j * 0.9 + f) + 3 * math.sin(ph * 5 + j * 1.7 + f)
                ww = w * (0.55 + 0.45 * math.sin(ph * 3 + j * 1.3 + f)) * (1 + j * 0.05)
                al = a * (1 - j / n) * (0.7 + 0.3 * math.sin(ph * 4 + j + f))
                if al > 2: dl.line([(x - ww / 2 + off, y), (x + ww / 2 + off, y)], fill=p["light"] + (int(al),), width=3)
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.3)))

    def _gondola(self, img, t, ph):
        """EP06: black gondola gliding across once per loop; gondolier rowing at the stern, iron prow blade,
        felze cabin, bow lantern with its reflection. dir=1 moves right, -1 left (mirrored)."""
        G = self.gondola; s = G["s"]; p = self.p; L = 640 * s
        span = W + L * 1.6; u = t / LOOP_S
        x = -L * 0.8 + u * span if G["dir"] > 0 else W + L * 0.8 - u * span
        y = G["y"] + 2 * s * math.sin(ph * 4)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); c = (6, 6, 9, 255); dr = G["dir"]
        X = lambda v: x + v * dr                                                              # local coords, bow at +L/2
        def top(v): q = v / (L / 2); return y - 16 * s - 58 * s * abs(q) ** 3.2
        vs = np.linspace(-L / 2, L / 2, 40)
        hull = [(X(v), top(v)) for v in vs] + [(X(v), y + 8 * s * (1 - (v / (L / 2)) ** 2) ** 0.5) for v in vs[::-1]]
        rl = [(px, 2 * y - py + 10 * s) for px, py in hull]                                   # reflection (soft, below)
        d.polygon(rl, fill=(4, 6, 10, 70))
        d.polygon(hull, fill=c)
        d.line([(X(v), top(v)) for v in vs], fill=mix((6, 6, 9), p["moon"], 0.25) + (255,), width=max(1, int(2 * s)))
        bx, by = X(L / 2), top(L / 2)                                                         # ferro (iron blade) at the prow
        fe = [(bx, by), (X(L / 2 + 14 * s), by - 30 * s), (X(L / 2 + 10 * s), by - 82 * s), (X(L / 2 - 8 * s), by - 92 * s), (X(L / 2 - 10 * s), by - 20 * s)]
        d.polygon(fe, fill=mix((6, 6, 9), p["moon"], 0.2) + (255,))
        for k in range(6): d.line([(X(L / 2 + 6 * s), by - 24 * s - k * 9 * s), (X(L / 2 + 22 * s), by - 26 * s - k * 9 * s)], fill=mix((6, 6, 9), p["moon"], 0.2) + (255,), width=max(1, int(3 * s)))
        sx_, sy_ = X(-L / 2), top(-L / 2)                                                     # small curl at the stern
        d.line([(sx_, sy_), (X(-L / 2 - 8 * s), sy_ - 18 * s), (X(-L / 2 + 2 * s), sy_ - 26 * s)], fill=c, width=max(2, int(5 * s)), joint="curve")
        f0, f1 = sorted((X(-40 * s), X(80 * s))); ft = top(0) - 64 * s                         # felze cabin
        d.rounded_rectangle([f0, ft, f1, top(0) + 2], radius=int(10 * s), fill=(14, 12, 16, 255))
        wx = X(20 * s); d.rectangle([wx - 9 * s, ft + 18 * s, wx + 9 * s, ft + 34 * s], fill=mix((14, 12, 16), p["light"], 0.35) + (255,))
        gx = X(-L / 2 + 70 * s); gy = top(-L / 2 + 70 * s); st = math.sin(ph * 8)              # gondolier, one stroke every 4 s
        lean = 10 * s * st
        hip = (gx + lean * 0.3 * dr, gy - 70 * s); sh = (gx + lean * dr, gy - 132 * s)
        d.line([(gx - 8 * s, gy), hip, (gx + 10 * s, gy)], fill=c, width=max(2, int(9 * s)))
        d.line([hip, sh], fill=c, width=max(3, int(20 * s)))
        d.ellipse([sh[0] - 11 * s, sh[1] - 30 * s, sh[0] + 11 * s, sh[1] - 6 * s], fill=c)
        d.ellipse([sh[0] - 15 * s, sh[1] - 30 * s, sh[0] + 15 * s, sh[1] - 24 * s], fill=c)    # cap
        hand = (sh[0] + 26 * s * dr, sh[1] + 22 * s)
        d.line([sh, hand], fill=c, width=max(2, int(7 * s)))
        ob = (gx + (150 + 30 * st) * s * dr, y + 16 * s)                                      # oar into the water
        d.line([(hand[0] - (hand[0] - ob[0]) * -0.25, hand[1] - (ob[1] - hand[1]) * 0.25), ob], fill=c, width=max(2, int(6 * s)))
        d.ellipse([gx + 60 * s * dr - 6 * s, gy - 30 * s, gx + 60 * s * dr + 6 * s, gy - 4 * s], fill=c)   # forcola
        lx, ly = X(L / 2 - 60 * s), top(L / 2 - 60 * s) - 64 * s                              # bow lantern on a short pole
        d.line([(lx, ly + 10 * s), (lx, top(L / 2 - 60 * s))], fill=c, width=max(2, int(4 * s)))
        img.alpha_composite(lay)
        fl = 0.86 + 0.14 * math.sin(ph * 6)
        R = int(130 * s + 20); g = self.tint(self.glow_sm.resize((R * 2, R * 2)), p["light"], 0.55 * fl)
        img.alpha_composite(g, (int(lx - R), int(ly - R)))
        d2 = ImageDraw.Draw(img)
        d2.rectangle([lx - 7 * s, ly - 8 * s, lx + 7 * s, ly + 10 * s], fill=(255, 214, 150, 255))
        for j in range(7):
            yy = y + 18 * s + j * 9 * s; ww = (16 - j) * s * (0.7 + 0.3 * math.sin(ph * 5 + j))
            d2.line([(lx - ww + 3 * s * math.sin(ph * 3 + j), yy), (lx + ww + 3 * s * math.sin(ph * 3 + j), yy)], fill=p["light"] + (int(140 - j * 18),), width=max(1, int(3 * s)))

    def _caravan(self, img, t):
        C = self.caravan; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        L = C["n"] * C["spacing"]; s = C["s"]; prev = None
        pos = sorted(((i * C["spacing"] + t / LOOP_S * C["spacing"]) % L - 260 for i in range(C["n"])), reverse=True)
        for x in pos:                                                                         # leader first, so ropes go back
            if x < -200 or x > W + 200: prev = None; continue
            xi = int(min(W - 1, max(0, x))); yg = C["top"][xi] + 4
            ph = TAU * 16 * t / LOOP_S + x / C["spacing"] * 1.7
            head = draw_camel(d, x, yg, s, C["col"], ph, C["load"])
            if prev is not None:                                                              # lead rope to the camel ahead
                px, py = prev; mx_ = (head[0] + px) / 2
                d.line([head, (mx_, max(head[1], py) + 10 * s), (px, py)], fill=C["col"] + (255,), width=2, joint="curve")
            prev = (x - 58 * s, yg - 70 * s)
        a = np.array(lay); xs = np.arange(W, dtype=np.float32)
        fade = np.clip((xs - C["x_in"]) / 160, 0, 1) * np.clip((C["x_out"] - xs) / 160, 0, 1)
        a[..., 3] = (a[..., 3] * fade[None, :]).astype(np.uint8)
        img.alpha_composite(Image.fromarray(a, "RGBA"))

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
        n = {"embers": 26, "fireflies": 22, "dust": 34, "snow": 90, "sand": 70, "mist": 16, "spray": 40}[self.particles]
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

    def _aurora(self, img, ph):
        """Soft green curtain computed at 1/4 resolution: rays rise from a wavy lower edge; periodic in LOOP_S."""
        A = self.aurora; w, h = W // 4, H // 4
        xs = np.arange(w, dtype=np.float32) * 4; ys = np.arange(h, dtype=np.float32)[:, None] * 4
        edge = A["y"] + A["depth"] * 0.45 + 40 * np.sin(xs / 260 + ph) + 26 * np.sin(xs / 120 - 2 * ph + 1.3)
        rays = 0.55 + 0.45 * np.sin(xs / 23 + 3 * ph) * np.sin(xs / 61 - ph + 0.7)
        env = np.clip((xs - A["x0"]) / 300, 0, 1) * np.clip((A["x1"] - xs) / 300, 0, 1) * (0.7 + 0.3 * np.sin(ph + xs / 400))
        dy = edge[None, :] - ys
        a = np.where(dy > 0, np.exp(-dy / (A["depth"] * 0.55)), np.exp(-(dy / 14) ** 2)) * rays[None, :] * env[None, :]
        a = np.clip(a * 0.34, 0, 1); a[ys[:, 0] > A["hy"] - 20] = 0
        top = np.clip(dy / A["depth"], 0, 1)[..., None]
        col = np.array([80, 236, 160], np.float32) * (1 - top) + np.array([150, 110, 210], np.float32) * top
        lay = np.zeros((h, w, 4), np.uint8); lay[..., :3] = col.astype(np.uint8); lay[..., 3] = (a * 255).astype(np.uint8)
        img.alpha_composite(Image.fromarray(lay, "RGBA").resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(3)))

    def _smoke(self, img, t):
        sx, sy, rise = self.smoke; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); n = 14
        for i in range(n):
            u = (t / LOOP_S * 2 + i / n) % 1.0
            x = sx + 18 * math.sin(TAU * u * 1.5 + i) + u * 40; y = sy - u * rise; r = 14 + u * 70
            a = 0.42 * math.sin(math.pi * min(1, u * 1.3)) * (1 - u) ** 0.6
            g = self.tint(self.glow_sm.resize((int(r * 2), int(r * 2))), mix(self.p["horizon"], self.p["moon"], 0.4), a)
            lay.alpha_composite(g, (int(x - r), int(y - r)))
        img.alpha_composite(lay)

    def _fires(self, img, ph):
        p = self.p; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for fi, (x, y, s) in enumerate(self.fires):
            fl = 0.85 + 0.1 * math.sin(ph * 7 + fi) + 0.05 * math.sin(ph * 17 + fi * 2)
            R = int(420 * s); g = self.tint(self.glow_lg.resize((R * 2, R * 2)), p["light"], 0.30 * fl)
            img.alpha_composite(g, (int(x - R), int(y - R * 1.1)))
            for k in range(-2, 3):                                                          # rounded tongues of flame
                fx = x + k * 52 * s; hh = (120 - abs(k) * 26) * s * (0.72 + 0.28 * math.sin(ph * (5 + abs(k) * 2) + k * 1.7 + fi))
                sway = 10 * s * math.sin(ph * 3 + k); hw = (34 - abs(k) * 4) * s
                outer = [(fx + sway * v ** 2 + (1 if sd > 0 else -1) * hw * math.sin(math.pi * (0.15 + 0.85 * (1 - v)) ) * (1 - v) ** 0.35, y - hh * v)
                         for sd in (-1, 1) for v in ([i / 10 for i in range(11)] if sd < 0 else [1 - i / 10 for i in range(11)])]
                d.polygon(outer, fill=p["ember"] + (170,))
                d.polygon([(fx + (q[0] - fx) * 0.5, y - (y - q[1]) * 0.6) for q in outer], fill=(255, 210, 130, 210))
            d.ellipse([x - 150 * s, y - 14 * s, x + 150 * s, y + 16 * s], fill=mix(p["ember"], (90, 30, 10), 0.4) + (230,))  # bed of embers
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3)))

    def frame(self, t):
        p = self.p; ph = TAU * t / LOOP_S
        img = self.back.copy(); d = ImageDraw.Draw(img)
        for x, y, b, f, k in self.stars_tw:
            bb = b * (0.55 + 0.45 * math.sin(ph * k + f))
            d.point((x, y), fill=mix(p["sky_top"], (240, 232, 214), bb) + (255,))
            if b > 0.3: d.point((x + 1, y), fill=mix(p["sky_top"], (240, 232, 214), bb * 0.6) + (255,))
        if self.aurora: self._aurora(img, ph)
        if self.reflect:
            mx, ry, mr = self.reflect; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            for i in range(26):
                y = ry + 6 + i * 13; hw = mr * (0.6 + i * 0.09) * (0.65 + 0.35 * math.sin(ph * (1 + i % 3) + i * 1.9))
                off = 14 * math.sin(ph * 2 + i * 0.8)
                dl.line([(mx - hw + off, y), (mx + hw + off, y)], fill=p["moon"] + (int(120 - i * 3.6),), width=3)
            img.alpha_composite(lay)
        if self.glowspot:                                                                    # EP06: far furnace glow
            gx, gy, R = self.glowspot; fl = 0.8 + 0.12 * math.sin(ph * 3) + 0.08 * math.sin(ph * 7 + 1)
            img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R)), p["light"], 0.5 * fl), (int(gx - R), int(gy - R // 2)))
        if self.wlights: self._wlights(img, ph)
        if self.win: self._winbeam(img, ph)
        if self.lensp: self._lens(img, ph)
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
        if self.foam: self._foam(img, ph)
        if self.beam: self._beam(img, ph)
        if self.ship: self._ship(img, t, ph)
        if self.smoke: self._smoke(img, t)
        if self.caravan: self._caravan(img, t)
        if self.gondola: self._gondola(img, t, ph)
        img.alpha_composite(self.near)
        if self.fires: self._fires(img, ph)
        if self.lamp:
            lx, ly = self.lamp; fl = 0.85 + 0.1 * math.sin(ph * 5) + 0.05 * math.sin(ph * 13 + 1)
            R = getattr(self, "lamp_r", 450); g = self.tint(self.glow_lg.resize((R * 2, R * 2)), p["light"], 0.33 * fl); img.alpha_composite(g, (int(lx - R), int(ly - R)))
            dl = ImageDraw.Draw(img); fh = 30 * fl
            dl.polygon([(lx - 8, ly), (lx, ly - fh), (lx + 8, ly), (lx, ly + 6)], fill=(255, 214, 140, 255))
            dl.polygon([(lx - 4, ly), (lx, ly - fh * 0.6), (lx + 4, ly)], fill=(255, 246, 220, 255))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for x0, y0, f, k, s in self.parts:
            if self.particles == "embers":
                y = (y0 - (H + 60) * t / LOOP_S * k) % (H + 60) - 30; x = x0 + 30 * math.sin(ph * 2 + f)
                a = 0.55 * s * (0.6 + 0.4 * math.sin(ph * 4 + f)) * min(1, y / (H * 0.4)); col = p["ember"]; sz = 4 + 3 * s
            elif self.particles == "snow":
                x = x0 + 26 * math.sin(ph * k + f); y = (y0 + (H + 40) * t / LOOP_S * k) % (H + 40) - 20
                a = 0.5 * s; col = (232, 238, 248); sz = 2 + 3 * s * (1 if k == 2 else 0.7)
            elif self.particles == "sand":                                                 # EP05: fine sand drifting on the breeze
                x = (x0 + (W + 40) * t / LOOP_S * k) % (W + 40) - 20; y = H * 0.55 + (y0 % (H * 0.45)) + 12 * math.sin(ph * 2 * k + f)
                a = 0.16 * s * (0.6 + 0.4 * math.sin(ph * 3 + f)); col = mix(p.get("sand", (200, 170, 130)), (255, 255, 255), 0.3); sz = 1.5 + 1.5 * s
            elif self.particles == "mist":                                                 # EP06: slow banks of lagoon mist
                x = x0 + 140 * math.sin(ph + f) * k; y = H * 0.5 + (y0 % (H * 0.45)) + 10 * math.sin(ph * 2 + f)
                a = 0.07 * s * (0.6 + 0.4 * math.sin(ph * 2 * k + f)); col = mix(p["moon"], p["horizon"], 0.3); sz = 50 + 60 * s
            elif self.particles == "spray":                                                # EP07: fine salt spray drifting landward
                x = (x0 - (W + 80) * t / LOOP_S * k) % (W + 80) - 40; y = H * 0.6 + (y0 % (H * 0.4)) + 18 * math.sin(ph * 2 * k + f)
                a = 0.13 * s * (0.5 + 0.5 * math.sin(ph * 3 * k + f)); col = mix(p["moon"], p["sea"], 0.2); sz = 2 + 3 * s
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
        t = max(t + 3.0, start + LOOP_S + 2)
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
    zi_b = np.zeros(1); zi_l = np.zeros(1)
    path = os.path.join(outdir, "mix.wav")
    seg_cache = {}
    with sf.SoundFile(path, "w", sr, 1, "PCM_16") as fo:
        for c0 in range(0, N, chunk):
            n = min(chunk, N - c0); tt = (np.arange(n) + c0) / sr
            w = rng.standard_normal(n)
            brown, zi_b = lfilter([1.0], [1, -0.997], w, zi=zi_b)  # rain/wind bed
            brown, zi_l = lfilter([0.06, 0.06], [1, -0.88], brown, zi=zi_l)
            bed = brown * 0.0017 * (0.85 + 0.15 * np.sin(TAU * tt / 41))
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
                    "-c:a", "aac", "-b:a", "64k", "-ac", "1", "-t", f"{total:.2f}", "-movflags", "+faststart",
                    os.path.join(outdir, "final.mp4")], check=True)
    print("ok", os.path.getsize(os.path.join(outdir, "final.mp4")) // 1_000_000, "MB")
