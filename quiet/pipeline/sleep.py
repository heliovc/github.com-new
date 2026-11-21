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
  acropolis / pnyx / stoa / courtyard / andron (EP08 Ancient Athens: the Acropolis rock with an irregular cliff (_rock)
  and a three-quarter Parthenon (_parthenon: lit front with pediment, shaded long side), the bronze Athena with a slow
  glint on the spear tip (_glints), low mudbrick houses with tiled or flat roofs and lit doors (_greek_houses), olive
  trees (_olive), a little owl gliding across the sky with a few soft wingbeats (_owl); the Pnyx view with violet
  Hymettus, the Long Walls to the harbour lights, and a perched owl whose eyes blink (_eyes); a Doric stoa in
  perspective with lamps on chains, painted panels, the Tholos and a wreathed herm; a house courtyard with loom and clay
  weights, altar with a thread of incense (_incense), well, hydria, fig tree and a lamplit doorway spilling light; the
  andron with couches, reclining garlanded guests, a lyre, a bell krater, tall lampstands (_lamps); new "moths"
  particles circling the lamps; palette keys "terra" and "marble").
  nihonbashi / sumida / lanes / pagoda / tatami (EP09 Edo Japan: the arched wooden Nihonbashi with capped railing posts,
  figures with lanterns, Fuji with snow tongues and the castle keep (_jroof = Japanese roof with upswept eaves, _kura =
  white storehouses, _boat = moored cargo boats, a boatman's pipe glowing (_pipe)); the Sumida with a lit roofed pleasure
  boat and poling boatman drifting across (_yakata), a weeping willow whose strands sway (_willow) and a noodle stall with
  a wind chime; a merchant lane in true one-point perspective (_proj) with lattice fronts, indigo shop curtains, paper
  lanterns swinging from the eaves (_chochin), the ward gate, a fire-watch ladder tower and the bathhouse chimney; the
  five-storey pagoda with ringed spire, stone lanterns (_toro), belfry, maple bough and pampas grass (_plume); a row-house
  room with moonlit shoji and pine shadow, ink heron scroll, andon, brazier with kettle steam and live coals (_steam);
  new "leaves" particles (turning maple leaves); palette keys "lacquer" and "washi").
  castle / bailey / hall / wallwalk / solar (EP10 Medieval Castle: across the moat at dusk - curtain wall with shaded round
  towers (_rtower, _crenels, _courses), twin-towered gatehouse with lit arch, raised portcullis, torch and the drawbridge
  down, the old square keep, the hall roof with its louvre smoking, pennants unrolling in the breeze (_banners), lit slits
  trembling in the moat; the outer courtyard with the portcullis down, lean-to stables with a nodding horse, the
  bakehouse oven glowing through the door (_oven), dovecote, cobbles, well-head with windlass and a cat, the watchman
  crossing with a swinging lantern (_walker/_figure); the great hall in one-point perspective with arch-braced trusses,
  moonlit windows, central hearth, dais and high table, painted hunting cloth with a white hart, trestle boards stacked,
  sleepers on pallets and a hound; the wall walk with battlements receding to a tower, a brazier, the moonlit countryside
  (river, village, church, windmill) and the watchman pacing away and back in perspective (_sentry); the lady's chamber
  with painted flowers, window embrasure with benches, curtained tester bed with fur coverlet and truckle bed, candle niche,
  hooded fireplace, chest, little dog and a woven garden cloth swaying (_hanging); new "thistledown" particles; palette
  keys "stone" and "banner").
  fogstreet / embankment / cabstand / parlour (EP11 Victorian London in the Fog: starless fog sky (_fogback), layers pushed
  back into the fog by colour (_fogtint), slow fog banks swaying at several heights (_mkbanks), gaslight as great soft
  halos with a bright core (_halos) on cast-iron lamp posts (_gaspost); a terrace of sooty brick houses with sash windows,
  fanlights, steps, area railings, smoking chimney stacks, pillar box and a mottled plane tree, the lamplighter walking with
  his pole and its bobbing flame (_lighter/_man); the river wall in perspective with dolphin lamp standards fading into the
  fog, Cleopatra's Needle, the clock tower with its lit dial, a railway bridge, landward trees and windows, a steam tug with
  lit wheelhouse and trailing smoke (_tug); a cab rank with the green cabmen's shelter, a hansom with its lamps and the
  driver up behind, the horse in a rug nodding at its nosebag and breathing steam, a chestnut brazier glowing (_hansom);
  a gaslit parlour with coal fire, overmantel mirror, glass-domed clock, china dogs, a wall clock with swinging pendulum,
  kettle steam on the hob (_pendulum), lace curtains and the fog outside; new "drizzle" particles; palette keys "fog",
  "gas" and "brick").
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
        self.owl, self.incense, self.lamps, self.eyes, self.glints = None, None, [], [], []
        self.chochin, self.yakata, self.willow, self.steam, self.pipe = [], None, None, None, None
        self.banners, self.oven, self.walker, self.sentry, self.hanging = [], None, None, None, None
        self.halos, self.banks, self.lighter, self.tug, self.hansom, self.pend, self.kettle, self.brazier = [], [], None, None, None, None, None, None
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

    # ------------------------------------------------------------ EP08 Athens
    def _olive(self, d, x, base, h, col, rng, silver=0.12):
        """Gnarled olive: twisted twin trunk, clumpy canopy of overlapping ellipses with silvery highlights."""
        p = self.p; c = col + (255,)
        for k in (-1, 1):
            d.line([(x, base), (x + k * 0.08 * h, base - 0.25 * h), (x + k * 0.03 * h, base - 0.45 * h)], fill=c, width=max(2, int(h * 0.05)))
        for _ in range(9):
            cx = x + rng.uniform(-0.38, 0.38) * h; cy = base - h * rng.uniform(0.5, 0.9); rx = h * rng.uniform(0.16, 0.28); ry = rx * 0.62
            d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=c)
        for _ in range(6):
            cx = x + rng.uniform(-0.32, 0.32) * h; cy = base - h * rng.uniform(0.62, 0.92); rx = h * rng.uniform(0.05, 0.1)
            d.ellipse([cx - rx, cy - rx * 0.5, cx + rx, cy + rx * 0.5], fill=mix(col, p["moon"], silver) + (255,))

    def _greek_houses(self, d, x0, x1, base, s, lit, col, jitter=6):
        """Low mudbrick houses: plastered walls in pale washes, shallow tiled roofs or flat roofs with a parapet,
        small high windows; lit ones (doors and windows) feed self.windows."""
        p, rng = self.p, self.rng; x = x0; terra = p.get("terra", (150, 78, 52)); marble = p.get("marble", (222, 214, 196))
        while x < x1:
            w = rng.uniform(70, 150) * s; h = rng.uniform(38, 84) * s; b = base + rng.uniform(-jitter, jitter) * s
            wall = mix(col, marble, rng.uniform(0.04, 0.16))
            d.rectangle([x, b - h, x + w, b + 30 * s], fill=wall + (255,))
            if rng.random() < 0.62:
                d.polygon([(x - 4 * s, b - h), (x + w * rng.uniform(0.3, 0.7), b - h - 20 * s), (x + w + 4 * s, b - h)], fill=mix(terra, col, 0.62) + (255,))
            else:
                d.rectangle([x - 2 * s, b - h - 6 * s, x + w + 2 * s, b - h], fill=mix(wall, (0, 0, 0), 0.25) + (255,))
            if rng.random() < lit:
                door = rng.random() < 0.5; wx = x + rng.uniform(0.2, 0.8) * w
                ww, wh = (9 * s, 18 * s) if door else (6 * s, 6 * s); wy = b - wh / 2 if door else b - h * 0.62
                self.windows.append((wx, wy, ww, wh, rng.uniform(0, TAU), int(rng.integers(1, 3))))
            x += w + rng.uniform(-14, 3) * s

    def _parthenon(self, d, x0, yb, wf, ws, ch, s=1.0):
        """Three-quarter view of a peripteral Doric temple: lit west front (8 columns, pediment) and shaded long side
        (14 columns, roof receding), dark cella behind the colonnades, three steps. Returns the apex point."""
        p = self.p; marble = p.get("marble", (222, 214, 196))
        lit = mix(marble, p["moon"], 0.2); sh = mix(marble, p["mid"], 0.52); dark = mix(p["mid"], (0, 0, 0), 0.4)
        ent = ch * 0.3; top = yb - ch; apex = top - ent - ch * 0.26
        d.polygon([(x0 + wf, top - ent), (x0 + wf / 2, apex), (x0 + wf / 2 + ws, apex - ch * 0.06), (x0 + wf + ws, top - ent - ch * 0.04)], fill=mix(sh, p["mid"], 0.3) + (255,))
        d.rectangle([x0, top, x0 + wf + ws, yb], fill=dark + (255,))
        for k, (c, w_) in enumerate(((lit, wf), (sh, ws))):                                   # 3 steps
            xa = x0 if k == 0 else x0 + wf
            for j in range(3): d.rectangle([xa - (3 - j) * 3 * s, yb + j * 5 * s, xa + w_ + (3 - j) * 3 * s, yb + (j + 1) * 5 * s], fill=mix(c, (0, 0, 0), 0.08 * j) + (255,))
        for n, xa, w_, c in ((8, x0, wf, lit), (14, x0 + wf, ws, sh)):
            cw = w_ / n * 0.56
            for i in range(n):
                cx = xa + (i + 0.5) * w_ / n
                d.polygon([(cx - cw / 2, yb), (cx + cw / 2, yb), (cx + cw * 0.4, top + 4 * s), (cx - cw * 0.4, top + 4 * s)], fill=c + (255,))
                d.rectangle([cx - cw * 0.62, top, cx + cw * 0.62, top + 5 * s], fill=c + (255,))
                d.line([(cx - cw * 0.12, yb), (cx - cw * 0.1, top + 6 * s)], fill=mix(c, (0, 0, 0), 0.18) + (255,), width=1)  # fluting shadow
        d.rectangle([x0 - 2 * s, top - ent, x0 + wf, top], fill=lit + (255,))
        d.rectangle([x0 + wf, top - ent + ch * 0.02, x0 + wf + ws, top], fill=sh + (255,))
        for i in range(int(wf / (9 * s))):                                                     # triglyph rhythm
            xx = x0 + i * 9 * s; d.line([(xx, top - ent * 0.55), (xx, top - ent * 0.1)], fill=mix(lit, (0, 0, 0), 0.2) + (255,), width=max(1, int(2 * s)))
        d.polygon([(x0 - 4 * s, top - ent), (x0 + wf / 2, apex), (x0 + wf + 4 * s, top - ent)], fill=lit + (255,))
        d.polygon([(x0 + 8 * s, top - ent - 3 * s), (x0 + wf / 2, apex + 8 * s), (x0 + wf - 8 * s, top - ent - 3 * s)], fill=mix(lit, p["mid"], 0.22) + (255,))
        for i in range(7):                                                                    # pediment figures, just shapes
            fx = x0 + wf * (0.22 + i * 0.093); fh = (apex + 8 * s - (top - ent)) * (1 - abs(i - 3) / 4.2) * 0.8
            d.ellipse([fx - 4 * s, top - ent - 4 * s + fh, fx + 4 * s, top - ent - 4 * s], fill=mix(lit, p["mid"], 0.1) + (255,))
        return (x0 + wf / 2, apex)

    def _rock(self, d, x0, x1, top, base, col, seed):
        """The Acropolis: a flat-topped limestone mass with irregular cliffs and a circuit wall along its rim."""
        r = random.Random(seed); p = self.p
        sp = (base - top) * 0.06
        lp = [(x0 - 140, base)] + [(x0 - 140 * (1 - k / 8) ** 2 + r.uniform(-14, 14) + (24 if k == 5 else 0), top + (base - top) * (1 - k / 8) ** 1.3 + r.uniform(-sp, sp) * (k < 8)) for k in range(9)]
        tp = [(x0 + (x1 - x0) * k / 10, top - r.uniform(0, 7)) for k in range(1, 10)]
        rp = [(x1 + 170 * (1 - k / 8) ** 1.6 + r.uniform(-14, 14) - (20 if k == 4 else 0), top + (base - top) * (1 - k / 8) ** 1.1 + r.uniform(-sp, sp) * (k < 8)) for k in range(9)][::-1] + [(x1 + 170, base)]
        d.polygon(lp + tp + rp, fill=col + (255,))
        for k in range(5):                                                                    # darker clefts in the cliff
            cx = r.uniform(x0, x1); d.polygon([(cx, top + 30), (cx + r.uniform(8, 20), top + r.uniform(60, 140)), (cx - r.uniform(4, 10), top + r.uniform(80, 160))], fill=mix(col, (0, 0, 0), 0.25) + (255,))
        for k in range(9):                                                                    # moonlit ledges
            y = top + 14 + k * (base - top) / 10; xa = x0 + r.uniform(0, 60) + k * 6; xb = x1 - r.uniform(0, 80) - k * 4
            d.line([(xa, y), (xa + (xb - xa) * r.uniform(0.2, 0.5), y + r.uniform(-6, 6))], fill=mix(col, p["moon"], 0.08) + (255,), width=2)
        wc = mix(col, p.get("marble", (220, 210, 190)), 0.22)
        d.rectangle([x0 + 10, top - 16, x1 - 10, top + 2], fill=wc + (255,))

    def build_acropolis(self):
        """From the lower town at dusk: the Acropolis rock with the Parthenon pale in the moonlight, the bronze Athena
        with a glinting spear tip, terraced houses with lit doors on the slopes, olive trees, an owl gliding across."""
        p, rng = self.p, self.rng; hy = int(H * 0.68)
        self.back = self.sky(hy, (0.8, 0.16), 44)
        self.back.alpha_composite(hills(hy - 10, 40, int(rng.integers(1e6)), mix(p["far"], (150, 100, 170), 0.35), blur=3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        rtop = int(H * 0.47); rc = mix(p["far"], p["mid"], 0.55)
        self._rock(d, W * 0.2, W * 0.78, rtop, hy + 60, rc, int(rng.integers(1e6)))
        self._parthenon(d, W * 0.43, rtop - 16, 150, 230, 96, 1.0)
        px = W * 0.33; d.rectangle([px - 10, rtop - 46, px + 10, rtop - 16], fill=mix(rc, (0, 0, 0), 0.3) + (255,))
        bz = mix(p["mid"], (60, 50, 40), 0.3)
        draw_figure(d, px, rtop - 46, 0.62, bz, seated=False, hat=True)
        d.line([(px + 12, rtop - 40), (px + 20, rtop - 150)], fill=bz + (255,), width=3)
        self.glints = [(px + 20, rtop - 150)]
        d.rectangle([W * 0.26, rtop - 40, W * 0.3, rtop - 14], fill=mix(rc, p["marble"], 0.25) + (255,))   # gateway hint
        for k in range(4): d.rectangle([W * 0.262 + k * 14, rtop - 38, W * 0.262 + k * 14 + 6, rtop - 16], fill=mix(rc, p["marble"], 0.5) + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near)
        for row, (base, s, lit) in enumerate(((hy + 40, 0.55, 0.35), (hy + 110, 0.8, 0.3), (hy + 200, 1.1, 0.25))):
            self._greek_houses(dn, -40, W + 40, base, s, lit, mix(p["mid"], p["near"], row * 0.3))
        dn.rectangle([0, hy + 230, W, H], fill=p["near"] + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        for x in (W * 0.06, W * 0.9, W * 0.97): self._olive(dn, x, H - 30, r2.uniform(230, 300), p["near"], r2, 0.1)
        cypress(dn, W * 0.14, H, 380, p["near"])
        self.near = near
        self.owl = dict(y=H * 0.3, s=0.9)
        self.fog_y = hy + 20; self.fog_a = 0.14; self.particles = "moths"

    def build_pnyx(self):
        """From the rock of the Pnyx: the city below with lamplit doors, the Acropolis to the left, the Long Walls
        running to the harbour lights at Piraeus, Hymettus violet in the distance, a little owl on a boulder."""
        p, rng = self.p, self.rng; hy = int(H * 0.5)
        self.back = self.sky(hy, (0.36, 0.14), 36)
        self._water(hy, 0.35)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)
        xs = np.arange(0, W * 0.62, 6); nz = noise1d(len(xs), int(rng.integers(1e6)), 4, 3)
        vio = mix(mix(p["far"], (156, 104, 176), 0.32), p["sky_mid"], 0.25)
        df.polygon([(0, hy + 6)] + [(x, hy - 30 - 56 * smooth(1 - abs(x / (W * 0.31) - 1)) ** 0.7 - 22 * v) for x, v in zip(xs, nz)] + [(W * 0.62, hy + 6)], fill=vio + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(2)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); pl = mix(p["mid"], p["far"], 0.35)
        d.polygon([(0, hy + 6), (W * 0.64, hy + 6), (W * 0.78, hy + 14), (W, hy + 30), (W, H), (0, H)], fill=pl + (255,))   # plain
        lw = mix(pl, p["marble"], 0.25)
        for off in (0, 26):                                                                    # the Long Walls
            d.line([(W * 0.5 + off, hy + 230), (W * 0.83 + off * 0.3, hy + 18)], fill=lw + (255,), width=4)
        for k in range(12):
            f = k / 12; self.windows.append((W * 0.83 + rng.uniform(-30, 70), hy + 10 + rng.uniform(-4, 10), 3, 3, rng.uniform(0, TAU), 2))
        for k in range(5): self.wlights.append((W * 0.86 + rng.uniform(-40, 80), 6, 40, rng.uniform(0, TAU)))
        rc = mix(p["far"], p["mid"], 0.6)
        self._rock(d, W * 0.06, W * 0.25, int(hy - 34), hy + 170, rc, int(rng.integers(1e6)))
        self._parthenon(d, W * 0.12, hy - 46, 54, 82, 36, 0.4)
        for row, (base, s, lit) in enumerate(((hy + 120, 0.4, 0.28), (hy + 170, 0.5, 0.26), (hy + 230, 0.62, 0.22), (hy + 300, 0.75, 0.2))):
            self._greek_houses(d, -30, W * (0.74 - row * 0.05), base, s, lit, mix(pl, p["mid"], 0.4 + row * 0.15), 10)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        r2 = random.Random(int(rng.integers(1e6)))
        pts = [(W * 0.3, H)] + [(W * (0.36 + 0.64 * k / 14), H - 150 - 70 * smooth(k / 14) + r2.uniform(-12, 12)) for k in range(15)] + [(W, H)]
        dn.polygon(pts, fill=nc + (255,))
        for k in range(10):                                                                    # worn rock steps catching moonlight
            y = H - 120 + k * 12; dn.line([(W * 0.45 + k * 20, y), (W * 0.95, y - 50)], fill=mix(nc, p["moon"], 0.06) + (255,), width=2)
        bx, by = W * 0.8, H - 250                                                              # boulder + perched owl
        dn.ellipse([bx - 110, by - 40, bx + 110, by + 80], fill=mix(nc, p["mid"], 0.25) + (255,))
        oc = mix(nc, (60, 50, 40), 0.25) + (255,)
        dn.ellipse([bx - 24, by - 92, bx + 24, by - 30], fill=oc); dn.ellipse([bx - 20, by - 122, bx + 20, by - 82], fill=oc)
        dn.polygon([(bx - 16, by - 116), (bx - 20, by - 128), (bx - 8, by - 120)], fill=oc); dn.polygon([(bx + 16, by - 116), (bx + 20, by - 128), (bx + 8, by - 120)], fill=oc)
        self.eyes = [(bx - 8, by - 104), (bx + 8, by - 104)]
        for _ in range(26):
            x = r2.uniform(W * 0.35, W); yb = H - 150 + r2.uniform(0, 140)
            for j in range(3): dn.line([(x, yb), (x + r2.uniform(-10, 10), yb - r2.uniform(14, 34))], fill=nc + (255,), width=2)
        self.near = near
        self.fog_y = hy + 40; self.fog_a = 0.12; self.particles = "moths"

    def build_stoa(self):
        """The Agora at lamplighting: a long Doric colonnade receding in perspective with lamps hung between the
        columns and faded panel paintings on the back wall; the round Tholos with a lit door far off; plane trees, a herm."""
        p, rng = self.p, self.rng; hy = int(H * 0.56); vx = W * 0.66
        self.back = self.sky(hy, (0.84, 0.14), 34)
        self.back.alpha_composite(hills(hy - 8, 26, int(rng.integers(1e6)), mix(p["far"], (150, 100, 170), 0.3), blur=3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); marble = p["marble"]
        d.rectangle([0, hy, W, H], fill=mix(p["mid"], p["horizon"], 0.12) + (255,))             # beaten earth
        tx, tb = W * 0.74, hy + 16                                                            # Tholos
        d.rectangle([tx - 70, tb - 50, tx + 70, tb], fill=mix(p["mid"], marble, 0.25) + (255,))
        d.polygon([(tx - 80, tb - 50), (tx, tb - 92), (tx + 80, tb - 50)], fill=mix(p.get("terra", (150, 78, 52)), p["mid"], 0.6) + (255,))
        self.windows.append((tx + 8, tb - 18, 16, 30, 0.3, 1))
        self._greek_houses(d, W * 0.8, W + 40, hy + 22, 0.45, 0.3, mix(p["mid"], p["far"], 0.3))
        def P(X, Y, z): return (vx + X / z, hy + Y / z)
        X0, Yb, Hc = -900.0, 520.0, 1250.0
        zs = [1.15 * 1.22 ** i for i in range(14)]
        wallc = mix(p["mid"], p.get("terra", (150, 78, 52)), 0.25); dark = mix(p["mid"], (0, 0, 0), 0.35)
        far_z, near_z = zs[-1], 0.9
        d.polygon([P(X0 - 700, Yb, near_z), P(X0 - 700, Yb, far_z), P(X0 - 700, Yb - Hc * 1.1, far_z), P(X0 - 700, Yb - Hc * 1.1, near_z)], fill=wallc + (255,))
        for i in range(len(zs) - 1):                                                          # faded painted panels
            za, zb = zs[i], zs[i + 1]; c = mix(wallc, [(140, 70, 50), (60, 70, 90), (120, 100, 60)][i % 3], 0.25)
            d.polygon([P(X0 - 700, Yb - Hc * 0.3, za * 1.05), P(X0 - 700, Yb - Hc * 0.3, zb * 0.95), P(X0 - 700, Yb - Hc * 0.8, zb * 0.95), P(X0 - 700, Yb - Hc * 0.8, za * 1.05)], fill=c + (255,))
        d.polygon([P(X0 - 700, Yb, near_z), P(X0 + 60, Yb, near_z), P(X0 + 60, Yb, far_z), P(X0 - 700, Yb, far_z)], fill=mix(p["mid"], p["moon"], 0.06) + (255,))
        d.polygon([P(X0 - 700, Yb - Hc * 1.1, near_z), P(X0 + 80, Yb - Hc * 1.02, near_z), P(X0 + 80, Yb - Hc * 1.02, far_z), P(X0 - 700, Yb - Hc * 1.1, far_z)], fill=dark + (255,))
        d.polygon([P(X0 + 80, Yb - Hc * 1.02, near_z), P(X0 + 80, Yb - Hc * 1.2, near_z), P(X0 - 700, Yb - Hc * 1.45, near_z * 1.3), P(X0 - 700, Yb - Hc * 1.45, far_z), P(X0 + 80, Yb - Hc * 1.2, far_z)], fill=mix(p.get("terra", (150, 78, 52)), p["mid"], 0.55) + (255,))
        d.polygon([P(X0 + 80, Yb - Hc * 1.02, near_z), P(X0 + 80, Yb - Hc * 1.2, near_z), P(X0 + 80, Yb - Hc * 1.2, far_z), P(X0 + 80, Yb - Hc * 1.02, far_z)], fill=mix(marble, p["mid"], 0.35) + (255,))
        for z in zs[::-1]:
            cw = 110 / z; (bx, by), (_, ty) = P(X0, Yb, z), P(X0, Yb - Hc, z)
            c = mix(marble, p["mid"], 0.25 + 0.4 * min(1, z / 8))
            d.polygon([(bx - cw / 2, by), (bx + cw / 2, by), (bx + cw * 0.4, ty), (bx - cw * 0.4, ty)], fill=c + (255,))
            d.rectangle([bx - cw * 0.65, ty - 30 / z, bx + cw * 0.65, ty], fill=c + (255,))
            d.line([(bx + cw * 0.15, by), (bx + cw * 0.12, ty)], fill=mix(c, (0, 0, 0), 0.25) + (255,), width=max(1, int(6 / z)))
        for i in range(len(zs) - 1):                                                          # lamps on chains between columns
            z = (zs[i] * zs[i + 1]) ** 0.5; (lx, ly) = P(X0 - 20, Yb - Hc * 0.62, z); (_, cy) = P(X0, Yb - Hc, z)
            d.line([(lx, cy), (lx, ly - 10 / z)], fill=dark + (255,), width=max(1, int(4 / z)))
            self.windows.append((lx, ly, max(3, 26 / z), max(2, 14 / z), rng.uniform(0, TAU), 1))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        r2 = random.Random(int(rng.integers(1e6)))
        dn.rectangle([W * 0.92, H * 0.18, W * 0.95, H], fill=nc + (255,))                     # plane tree
        dn.line([(W * 0.935, H * 0.4), (W * 0.82, H * 0.2)], fill=nc + (255,), width=16)
        for _ in range(26):
            cx = W * r2.uniform(0.74, 1.05); cy = H * r2.uniform(-0.05, 0.25); rr = r2.uniform(60, 130)
            dn.ellipse([cx - rr, cy - rr * 0.7, cx + rr, cy + rr * 0.7], fill=nc + (255,))
        hx, hb = W * 0.56, H - 70                                                              # herm with a wreath
        hc = mix(nc, p["marble"], 0.18)
        dn.rectangle([hx - 26, hb - 230, hx + 26, hb], fill=hc + (255,)); dn.rectangle([hx - 34, hb - 238, hx + 34, hb - 222], fill=hc + (255,))
        dn.ellipse([hx - 30, hb - 310, hx + 30, hb - 236], fill=hc + (255,)); dn.polygon([(hx - 24, hb - 262), (hx + 24, hb - 262), (hx, hb - 214)], fill=hc + (255,))
        for k in range(10): a = k / 10 * math.pi; dn.ellipse([hx + 34 * math.cos(a) - 7, hb - 236 + 16 * math.sin(a) - 4, hx + 34 * math.cos(a) + 7, hb - 236 + 16 * math.sin(a) + 4], fill=mix(nc, (60, 90, 50), 0.35) + (255,))
        for x0 in (W * 0.3, W * 0.4):                                                          # trestles and a folded awning
            dn.line([(x0, H - 40), (x0 + 30, H - 130), (x0 + 60, H - 40)], fill=nc + (255,), width=6)
            dn.line([(x0 + 130, H - 40), (x0 + 160, H - 130), (x0 + 190, H - 40)], fill=nc + (255,), width=6)
            dn.rectangle([x0 + 10, H - 136, x0 + 185, H - 124], fill=nc + (255,))
        dn.polygon([(W * 0.3, H - 150), (W * 0.48, H - 150), (W * 0.47, H - 170), (W * 0.31, H - 166)], fill=mix(nc, (120, 60, 50), 0.25) + (255,))
        dn.rectangle([0, H - 40, W, H], fill=nc + (255,))
        self.near = near
        self.fog_y = hy + 10; self.fog_a = 0.1; self.particles = "moths"

    def build_courtyard(self):
        """An Athenian house courtyard: whitewashed walls with doorways (one lamplit), tiled eaves, a porch with an
        upright loom and clay weights, a small altar with rising incense, a well with a beam, a hydria, a fig tree."""
        p, rng = self.p, self.rng; wt = int(H * 0.36); gy = int(H * 0.84)
        self.back = self.sky(wt + 40, (0.66, 0.11), 32)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); marble = p["marble"]; terra = p.get("terra", (150, 78, 52))
        wall = mix(marble, p["mid"], 0.66); shade = mix(wall, p["mid"], 0.45)
        d.rectangle([0, wt, W, gy], fill=wall + (255,))
        d.rectangle([0, wt - 18, W, wt + 8], fill=mix(terra, p["mid"], 0.5) + (255,))         # tiled eaves
        for k in range(0, W, 22): d.ellipse([k, wt + 2, k + 18, wt + 14], fill=mix(terra, p["mid"], 0.35) + (255,))
        for x0, lit in ((W * 0.36, True), (W * 0.58, False), (W * 0.76, False)):              # doorways
            d.rectangle([x0, gy - 230, x0 + 110, gy], fill=mix(p["mid"], (0, 0, 0), 0.5) + (255,))
            d.rectangle([x0 - 8, gy - 240, x0 + 118, gy - 228], fill=shade + (255,))
            if lit:
                self.windows.append((x0 + 55, gy - 115, 100, 222, 0.2, 1))
                spill = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(spill).polygon([(x0, gy), (x0 + 110, gy), (x0 + 190, H), (x0 - 80, H)], fill=p["light"] + (46,))
                self.spill = spill.filter(ImageFilter.GaussianBlur(14))
        d.rectangle([W * 0.66, wt + 60, W * 0.7, wt + 90], fill=mix(p["mid"], (0, 0, 0), 0.5) + (255,))  # small high window
        d.rectangle([0, gy, W, H], fill=mix(p["mid"], p["horizon"], 0.15) + (255,))
        for _ in range(40):                                                                   # earth texture
            x, y = rng.uniform(0, W), rng.uniform(gy + 10, H); d.line([(x, y), (x + rng.uniform(10, 40), y)], fill=mix(p["mid"], p["moon"], 0.05) + (255,), width=1)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, wt - 70), (W * 0.3, wt + 40), (W * 0.3, wt + 64), (0, wt - 30)], fill=mix(terra, nc, 0.6) + (255,))  # porch roof
        for x in (W * 0.03, W * 0.28): dn.rectangle([x - 9, wt + 50 - (0 if x > W * 0.1 else 60), x + 9, gy + 30], fill=mix(nc, p["mid"], 0.3) + (255,))
        lx0, lx1, ly0, ly1 = W * 0.08, W * 0.22, gy - 330, gy - 40                             # upright loom
        lc = mix(nc, (90, 60, 40), 0.35)
        dn.line([(lx0, gy), (lx0 + 10, ly0 - 20)], fill=lc + (255,), width=8); dn.line([(lx1, gy), (lx1 - 10, ly0 - 20)], fill=lc + (255,), width=8)
        dn.line([(lx0, ly0), (lx1, ly0)], fill=lc + (255,), width=10)
        dn.rectangle([lx0 + 10, ly0 + 6, lx1 - 10, ly0 + 140], fill=mix(p.get("terra", (150, 78, 52)), (120, 20, 30), 0.4) + (255,))  # madder cloth
        dn.line([(lx0 + 10, ly0 + 130), (lx1 - 10, ly0 + 130)], fill=mix(p["accent"], nc, 0.4) + (255,), width=4)
        for k in range(22):
            x = lx0 + 14 + k * (lx1 - lx0 - 28) / 21; dn.line([(x, ly0 + 140), (x, ly1 - 20)], fill=mix(nc, p["marble"], 0.25) + (200,), width=1)
            dn.polygon([(x - 5, ly1 - 4), (x + 5, ly1 - 4), (x, ly1 - 22)], fill=mix(nc, terra, 0.4) + (255,))
        tx = W * 0.25; dn.rectangle([tx - 40, gy - 70, tx + 40, gy - 62], fill=lc + (255,)); dn.line([(tx, gy - 62), (tx, gy + 10)], fill=lc + (255,), width=6)
        dn.ellipse([tx - 18, gy - 82, tx + 14, gy - 70], fill=mix(nc, terra, 0.5) + (255,))
        self.lamp = (tx + 18, gy - 82); self.lamp_r = 360
        ax, ab = W * 0.5, gy + 60                                                             # altar of Zeus Herkeios
        ac = mix(nc, p["marble"], 0.25)
        dn.rectangle([ax - 50, ab - 90, ax + 50, ab], fill=ac + (255,)); dn.rectangle([ax - 60, ab - 100, ax + 60, ab - 88], fill=ac + (255,))
        dn.rectangle([ax - 60, ab - 112, ax - 44, ab - 100], fill=ac + (255,)); dn.rectangle([ax + 44, ab - 112, ax + 60, ab - 100], fill=ac + (255,))
        self.incense = (ax, ab - 102, 300)
        self.fires = []; self.embers_pt = (ax, ab - 102)
        wx, wb = W * 0.83, gy + 90                                                            # well, beam, rope, hydria
        dn.rectangle([wx - 70, wb - 70, wx + 70, wb], fill=ac + (255,)); dn.ellipse([wx - 72, wb - 86, wx + 72, wb - 56], fill=mix(ac, (0, 0, 0), 0.4) + (255,))
        dn.line([(wx - 64, wb - 70), (wx - 64, wb - 250)], fill=lc + (255,), width=8); dn.line([(wx + 64, wb - 70), (wx + 64, wb - 250)], fill=lc + (255,), width=8)
        dn.line([(wx - 74, wb - 246), (wx + 74, wb - 246)], fill=lc + (255,), width=9); dn.line([(wx, wb - 246), (wx, wb - 110)], fill=mix(lc, p["marble"], 0.3) + (255,), width=2)
        dn.polygon([(wx - 8, wb - 110), (wx + 8, wb - 110), (wx + 12, wb - 90), (wx - 12, wb - 90)], fill=lc + (255,))
        hx, hb = W * 0.71, gy + 50; hc = mix(nc, terra, 0.45)
        dn.ellipse([hx - 40, hb - 100, hx + 40, hb - 10], fill=hc + (255,)); dn.polygon([(hx - 22, hb - 20), (hx + 22, hb - 20), (hx + 16, hb), (hx - 16, hb)], fill=hc + (255,))
        dn.rectangle([hx - 12, hb - 130, hx + 12, hb - 92], fill=hc + (255,)); dn.rectangle([hx - 20, hb - 136, hx + 20, hb - 126], fill=hc + (255,))
        dn.arc([hx - 56, hb - 92, hx - 26, hb - 56], 90, 270, fill=hc + (255,), width=6); dn.arc([hx + 26, hb - 92, hx + 56, hb - 56], 270, 90, fill=hc + (255,), width=6)
        dn.line([(hx - 4, hb - 128), (hx - 4, hb - 30)], fill=mix(hc, p["moon"], 0.15) + (255,), width=3)  # sheen
        for k in range(3):                                                                   # storage jars along the right wall
            jx = W * 0.92 + k * 40; dn.ellipse([jx - 34, gy - 150, jx + 34, gy + 20], fill=mix(nc, terra, 0.3 - k * 0.05) + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        dn.line([(W * 0.98, gy), (W * 0.93, wt + 40), (W * 0.86, wt - 60)], fill=nc + (255,), width=22)   # fig tree
        for _ in range(34):
            cx = W * r2.uniform(0.74, 1.04); cy = r2.uniform(wt - 230, wt + 40); rr = r2.uniform(26, 50)
            for j in range(3):
                a = j * TAU / 3 + r2.uniform(0, 1); dn.ellipse([cx + rr * 0.5 * math.cos(a) - rr * 0.55, cy + rr * 0.5 * math.sin(a) - rr * 0.55, cx + rr * 0.5 * math.cos(a) + rr * 0.55, cy + rr * 0.5 * math.sin(a) + rr * 0.55], fill=nc + (255,))
        for _ in range(6):
            fx, fy = W * r2.uniform(0.78, 0.98), r2.uniform(wt - 150, wt + 30); dn.ellipse([fx - 9, fy - 11, fx + 9, fy + 11], fill=mix(nc, (90, 40, 80), 0.45) + (255,))
        self.near = near
        self.fog_a = 0.0; self.particles = "moths"

    def build_andron(self):
        """The men's dining room: plastered walls with a red-and-black meander frieze, couches on a raised border with
        reclining guests, a painted mixing bowl on a stand, tall bronze lampstands, a doorway onto the moonlit court."""
        p, rng = self.p, self.rng
        terra = p.get("terra", (150, 78, 52)); wall = mix(terra, p["mid"], 0.62); dark = mix(p["mid"], (0, 0, 0), 0.45)
        sky = self.sky(int(H * 0.7), (0.86, 0.3), 24)
        base = Image.new("RGBA", (W, H), wall + (255,)); dB = ImageDraw.Draw(base)
        fx0, fx1, fy0, fy1 = W * 0.78, W * 0.92, H * 0.22, H * 0.72                           # doorway onto the court
        m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rectangle([fx0, fy0, fx1, fy1], fill=255)
        court = sky.copy(); dc = ImageDraw.Draw(court)
        dc.rectangle([fx0, H * 0.5, fx1, fy1], fill=mix(p["marble"], p["mid"], 0.55) + (255,))
        dc.rectangle([fx0, H * 0.62, fx1, fy1], fill=mix(p["mid"], p["horizon"], 0.15) + (255,))
        base.paste(court, (0, 0), m)
        self.stars_tw = [s for s in self.stars_tw if fx0 < s[0] < fx1 and fy0 < s[1] < H * 0.48]
        dB.rectangle([fx0 - 14, fy0 - 14, fx1 + 14, fy0], fill=dark + (255,))
        dB.rectangle([0, H * 0.08, W, H * 0.13], fill=mix(terra, (120, 30, 20), 0.3) + (255,))   # frieze band
        y0, y1 = H * 0.08 + 6, H * 0.13 - 6
        for k in range(int(W / 36)):                                                          # meander
            x = k * 36; c = mix(p["mid"], (0, 0, 0), 0.5) + (255,)
            dB.line([(x, y1), (x, y0), (x + 24, y0), (x + 24, y1 - 14), (x + 10, y1 - 14), (x + 10, y1 - 26 + 14), (x + 36, y1)], fill=c, width=3)
        dB.rectangle([0, H * 0.13, W, H * 0.16], fill=mix(wall, (0, 0, 0), 0.15) + (255,))
        dB.rectangle([0, H * 0.72, W, H], fill=mix(p["mid"], (0, 0, 0), 0.2) + (255,))        # floor
        dB.ellipse([W * 0.25, H * 0.8, W * 0.65, H * 1.05], outline=mix(p["mid"], p["marble"], 0.12) + (255,), width=4)  # pebble mosaic ring
        dB.rectangle([0, H * 0.66, W * 0.76, H * 0.73], fill=mix(wall, p["marble"], 0.18) + (255,))  # raised plaster border
        self.back = base
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); cc = mix(p["mid"], (70, 45, 30), 0.3)
        fig = mix(p["near"], p["mid"], 0.45); cushion = mix(terra, p["mid"], 0.35)
        for k, cx in enumerate((W * 0.14, W * 0.38, W * 0.62)):                                # three couches with guests
            d.rectangle([cx - 140, H * 0.56, cx + 140, H * 0.6], fill=cc + (255,))
            d.rectangle([cx - 132, H * 0.6, cx - 120, H * 0.67], fill=cc + (255,)); d.rectangle([cx + 120, H * 0.6, cx + 132, H * 0.67], fill=cc + (255,))
            d.rectangle([cx - 150, H * 0.47, cx - 130, H * 0.58], fill=cc + (255,))
            d.ellipse([cx - 135, H * 0.5, cx - 70, H * 0.57], fill=cushion + (255,))
            d.polygon([(cx - 118, H * 0.43), (cx - 74, H * 0.43), (cx - 52, H * 0.54), (cx - 124, H * 0.555)], fill=fig + (255,))       # torso on the elbow
            d.polygon([(cx - 70, H * 0.515), (cx - 10, H * 0.49), (cx + 40, H * 0.515), (cx + 124, H * 0.535), (cx + 128, H * 0.56), (cx - 70, H * 0.562)], fill=fig + (255,))  # cloaked legs
            d.ellipse([cx - 112, H * 0.375, cx - 80, H * 0.432], fill=fig + (255,))
            d.polygon([(cx - 108, H * 0.405), (cx - 84, H * 0.405), (cx - 88, H * 0.44), (cx - 104, H * 0.44)], fill=fig + (255,))   # beard/neck
            for j in range(7): a = math.pi * (0.95 + j * 0.18); d.ellipse([cx - 96 + 17 * math.cos(a) - 5, H * 0.392 + 9 * math.sin(a) - 4, cx - 96 + 17 * math.cos(a) + 5, H * 0.392 + 9 * math.sin(a) + 4], fill=mix(fig, (60, 96, 50), 0.35) + (255,))  # myrtle garland
            d.line([(cx - 80, H * 0.45), (cx - 40, H * 0.47)], fill=fig + (255,), width=10)                                           # forearm
            if k == 1:
                d.ellipse([cx - 40, H * 0.43, cx + 6, H * 0.5], outline=fig + (255,), width=5)                # lyre
                d.line([(cx - 34, H * 0.44), (cx - 44, H * 0.37)], fill=fig + (255,), width=4); d.line([(cx, H * 0.44), (cx + 8, H * 0.37)], fill=fig + (255,), width=4)
                d.line([(cx - 46, H * 0.37), (cx + 10, H * 0.37)], fill=fig + (255,), width=4)
            else:
                d.ellipse([cx - 40, H * 0.45, cx - 4, H * 0.47], fill=mix(fig, (0, 0, 0), 0.3) + (255,))      # cup
            d.rectangle([cx - 60, H * 0.63, cx + 60, H * 0.645], fill=cc + (255,)); d.line([(cx - 50, H * 0.645), (cx - 50, H * 0.7)], fill=cc + (255,), width=5); d.line([(cx + 50, H * 0.645), (cx + 50, H * 0.7)], fill=cc + (255,), width=5)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        kx, kb = W * 0.47, H * 0.9                                                            # krater on a stand
        st = mix(nc, (70, 60, 40), 0.3)
        for dx in (-50, 0, 50): dn.line([(kx + dx, kb + 60), (kx + dx * 0.4, kb)], fill=st + (255,), width=6)
        kc = mix(nc, (20, 18, 18), 0.3); band = mix(terra, nc, 0.2)
        prof = [(30 if v < 0.12 else 16 if v < 0.2 else 16 + 98 * math.sin((v - 0.2) / 0.8 * math.pi / 2) ** 0.8, kb - v * 190) for v in np.linspace(0, 1, 24)]
        dn.polygon([(kx - w_, y_) for w_, y_ in prof] + [(kx + w_, y_) for w_, y_ in prof[::-1]], fill=kc + (255,))
        dn.polygon([(kx - 92, kb - 150), (kx + 92, kb - 150), (kx + 104, kb - 178), (kx - 104, kb - 178)], fill=band + (255,))
        for j in range(5): dn.ellipse([kx - 70 + j * 32, kb - 172, kx - 54 + j * 32, kb - 156], fill=kc + (255,))   # figures on the band
        dn.rectangle([kx - 120, kb - 200, kx + 120, kb - 188], fill=kc + (255,))
        dn.arc([kx - 150, kb - 120, kx - 80, kb - 60], 90, 270, fill=kc + (255,), width=10); dn.arc([kx + 80, kb - 120, kx + 150, kb - 60], 270, 90, fill=kc + (255,), width=10)
        self.lamps = []
        for lx in (W * 0.27, W * 0.72):                                                        # tall lampstands
            dn.line([(lx, H * 0.95), (lx, H * 0.36)], fill=st + (255,), width=6)
            for dx in (-34, 0, 34): dn.line([(lx, H * 0.9), (lx + dx, H * 0.97)], fill=st + (255,), width=5)
            dn.ellipse([lx - 30, H * 0.35, lx + 30, H * 0.37], fill=st + (255,))
            self.lamps.append((lx + 20, H * 0.345, 1.0))
        dn.rectangle([0, H * 0.97, W, H], fill=nc + (255,))
        self.near = near
        self.mid_glow = True; self.fog_a = 0.0; self.particles = "moths"

    # ------------------------------------------------------------------ EP09 Edo Japan
    def _jroof(self, d, x0, x1, y, rise, col, curl=0.5, inset=0.18, tiles=None):
        """Japanese roof seen side-on: a long eave whose ends sweep upward (curl, as a fraction of rise), sloping up to
        a shorter ridge with raised ends. Optional tile lines. Returns the ridge y."""
        xc, hw = (x0 + x1) / 2, (x1 - x0) / 2; n = 24
        eave = [(x0 + (x1 - x0) * k / n, y - rise * curl * abs((k / n) * 2 - 1) ** 5) for k in range(n + 1)]
        ry = y - rise; ri = hw * inset
        top = [(x1 - ri, ry), (x1 - ri * 0.6, ry - rise * 0.16), (x1 - ri * 0.85, ry - rise * 0.05),
               (x0 + ri * 0.85, ry - rise * 0.05), (x0 + ri * 0.6, ry - rise * 0.16), (x0 + ri, ry)]
        d.polygon(eave + top, fill=col + (255,))
        if tiles:
            for k in range(1, int((x1 - x0) / 12)):
                xa = x0 + k * 12; f = (xa - x0) / (x1 - x0)
                if ri * 0.6 < xa - x0 < (x1 - x0) - ri * 0.6:
                    ya = y - rise * curl * abs(f * 2 - 1) ** 5 - 2; xb = xc + (xa - xc) * (1 - inset * 0.9)
                    d.line([(xa, ya), (xb, ry + 2)], fill=tiles + (255,), width=1)
        d.line(eave, fill=mix(col, self.p["moon"], 0.16) + (255,), width=2)
        return ry

    def _kura(self, d, x, base, w, h, col, s=1.0):
        """Storehouse: thick white plaster walls, dark tiled roof, black skirt of tiles in a lattice, one shuttered window."""
        p = self.p; wall = mix(col, p.get("washi", (236, 222, 190)), 0.38)
        d.rectangle([x, base - h, x + w, base], fill=wall + (255,))
        sk = mix(col, (0, 0, 0), 0.35)
        d.rectangle([x, base - h * 0.32, x + w, base], fill=sk + (255,))
        for k in range(int(w / (10 * s)) + 1):
            xx = x + k * 10 * s; d.line([(xx, base - h * 0.32), (xx + h * 0.32, base)], fill=mix(sk, wall, 0.25) + (255,), width=1)
        d.rectangle([x + w * 0.4, base - h * 0.78, x + w * 0.6, base - h * 0.56], fill=mix(sk, (0, 0, 0), 0.3) + (255,))
        self._jroof(d, x - 10 * s, x + w + 10 * s, base - h, 26 * s, mix(col, (0, 0, 0), 0.45), 0.4, 0.12)

    def _boat(self, d, x, y, L, s, col, load=True):
        """A low flat cargo boat moored side-on, with straw rice bales and barrels; returns nothing."""
        d.polygon([(x, y - 10 * s), (x + L, y - 10 * s), (x + L + 24 * s, y - 26 * s), (x + L - 6 * s, y + 6 * s), (x + 10 * s, y + 6 * s)], fill=col + (255,))
        if load:
            bc = mix(col, self.p.get("washi", (236, 222, 190)), 0.22)
            for k in range(int(L / (40 * s))):
                bx = x + 20 * s + k * 38 * s
                d.ellipse([bx, y - 40 * s, bx + 36 * s, y - 10 * s], fill=bc + (255,))
                d.line([(bx + 12 * s, y - 38 * s), (bx + 12 * s, y - 12 * s)], fill=mix(bc, (0, 0, 0), 0.3) + (255,), width=1)
                d.line([(bx + 24 * s, y - 38 * s), (bx + 24 * s, y - 12 * s)], fill=mix(bc, (0, 0, 0), 0.3) + (255,), width=1)

    def build_nihonbashi(self):
        """The arched wooden Nihonbashi bridge from the riverbank at dusk: Fuji pale in the afterglow, the castle keep,
        white storehouses on the far bank, figures with lanterns crossing, moored cargo boats, lamplight on the water."""
        p, rng = self.p, self.rng; hy = int(H * 0.6)
        self.back = self.sky(hy - 120, (0.84, 0.15), 38)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far)
        fx, ftop, fw = W * 0.3, hy - 330, 470                                                 # Mount Fuji
        prof = lambda u: ftop + (hy - 40 - ftop) * (1 - (1 - u) ** 1.7)
        left = [(fx - fw * u, prof(u)) for u in np.linspace(0.04, 1, 30)]
        fcol = mix(p["far"], p["horizon"], 0.42)
        df.polygon([(fx - fw * 0.04, ftop)] + left + [(fx + fw * u, prof(u)) for u in np.linspace(1, 0.04, 30)] + [(fx + fw * 0.04, ftop)], fill=fcol + (255,))
        sc_ = mix(p["moon"], p["horizon"], 0.35)
        rs = random.Random(int(rng.integers(1e6))); sb = prof(0.3)
        snow = [(fx - fw * 0.04, ftop)] + [(fx - fw * u, prof(u)) for u in np.linspace(0.04, 0.3, 8)]
        for i in range(1, 14):                                                                # snow tongues reaching down the slopes
            xx = fx - fw * 0.3 + fw * 0.6 * i / 14; up = (fx - fw * 0.3 + fw * 0.6 * i / 14 - fx) / fw
            snow.append((xx, sb - 34 * (1 - abs(up) / 0.3) * 0.0 + (rs.uniform(26, 60) if i % 2 else rs.uniform(-6, 6))))
        snow += [(fx + fw * u, prof(u)) for u in np.linspace(0.3, 0.04, 8)] + [(fx + fw * 0.04, ftop)]
        df.polygon(snow, fill=sc_ + (255,))
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(2.2)))
        self.back.alpha_composite(hills(hy - 30, 36, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.4), blur=2))
        cas = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dc = ImageDraw.Draw(cas); cc = mix(p["far"], p["mid"], 0.6)
        cx, cb = W * 0.58, hy - 46                                                            # castle keep on its stone base
        dc.polygon([(cx - 120, cb + 10), (cx + 120, cb + 10), (cx + 96, cb - 40), (cx - 96, cb - 40)], fill=mix(cc, (0, 0, 0), 0.2) + (255,))
        y = cb - 40
        for k, w in enumerate((170, 140, 112, 84, 60)):
            d_h = 34 - k * 3
            dc.rectangle([cx - w / 2, y - d_h, cx + w / 2, y], fill=mix(cc, p["washi"], 0.12) + (255,))
            y = self._jroof(dc, cx - w / 2 - 22, cx + w / 2 + 22, y - d_h + 6, 22, mix(cc, (0, 0, 0), 0.3), 0.5, 0.25)
        for k in range(10): dc.ellipse([W * 0.47 + k * 26 - 26, cb - 30 - (k % 3) * 8, W * 0.47 + k * 26 + 26, cb + 20], fill=mix(cc, (20, 30, 20), 0.2) + (255,))
        self.back.alpha_composite(cas.filter(ImageFilter.GaussianBlur(1.2)))
        self._water(hy, 0.3)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); bank = mix(p["mid"], p["far"], 0.3)
        d.rectangle([0, hy - 14, W, hy + 4], fill=mix(bank, (0, 0, 0), 0.2) + (255,))       # stone embankment of the far bank
        x = W * 0.66
        while x < W + 40:                                                                     # storehouses on the far bank
            w = rng.uniform(110, 160); h = rng.uniform(90, 130); self._kura(d, x, hy - 12, w, h, bank, 1.0)
            if rng.random() < 0.5:
                gx = x + w + 6; d.rectangle([gx, hy - 70, gx + 40, hy - 12], fill=mix(bank, (0, 0, 0), 0.3) + (255,))
                self.windows.append((gx + 20, hy - 40, 22, 26, rng.uniform(0, TAU), 1)); self.wlights.append((gx + 20, 26, 60, rng.uniform(0, TAU)))
                x += 50
            x += w + rng.uniform(16, 40)
        for k in range(18):                                                                   # faint reflection of the far bank
            d.line([(W * 0.66, hy + 8 + k * 5), (W, hy + 8 + k * 5)], fill=mix(p["sea"], p["washi"], 0.1) + (int(40 - k * 2),), width=2)
        # the bridge: a long low arch on rows of wooden legs, railings with capped posts
        x0, x1, top = -80, W * 0.7, hy - 150; wood = mix(p["mid"], (70, 52, 40), 0.35)
        deck = lambda xx: hy - 26 - (hy - 26 - top) * math.sin(math.pi * min(1, max(0, (xx - x0) / (x1 - x0))))
        xs = np.linspace(x0, x1, 80)
        d.polygon([(xx, deck(xx)) for xx in xs] + [(xx, deck(xx) + 22) for xx in xs[::-1]], fill=wood + (255,))
        for k in range(1, 12):                                                                # legs and cross-braces
            xx = x0 + (x1 - x0) * k / 12; yt = deck(xx) + 20
            for dx in (-14, 14): d.line([(xx + dx, yt), (xx + dx * 1.3, hy + 26)], fill=mix(wood, (0, 0, 0), 0.25) + (255,), width=7)
            d.line([(xx - 16, yt + (hy - yt) * 0.35), (xx + 18, yt + (hy - yt) * 0.75)], fill=mix(wood, (0, 0, 0), 0.3) + (255,), width=3)
            d.line([(xx + 16, yt + (hy - yt) * 0.35), (xx - 18, yt + (hy - yt) * 0.75)], fill=mix(wood, (0, 0, 0), 0.3) + (255,), width=3)
            refl = [(xx - 14, hy + 30), (xx - 18, hy + 30 + (hy + 26 - yt) * 0.5), (xx + 18, hy + 30 + (hy + 26 - yt) * 0.5), (xx + 14, hy + 30)]
            d.polygon(refl, fill=mix(p["sea"], (0, 0, 0), 0.4) + (70,))
        d.line([(xx, deck(xx) - 26) for xx in xs], fill=mix(wood, p["moon"], 0.1) + (255,), width=5)   # handrail
        d.line([(xx, deck(xx) - 12) for xx in xs], fill=wood + (255,), width=2)
        bronze = mix(p["mid"], (150, 120, 70), 0.45)
        for k in range(0, 21):
            xx = x0 + (x1 - x0) * k / 20; yy = deck(xx)
            d.line([(xx, yy), (xx, yy - 30)], fill=wood + (255,), width=5)
            if k in (0, 4, 8, 12, 16, 20):                                                    # bronze onion caps (giboshi)
                d.ellipse([xx - 8, yy - 44, xx + 8, yy - 28], fill=bronze + (255,)); d.polygon([(xx - 3, yy - 42), (xx, yy - 54), (xx + 3, yy - 42)], fill=bronze + (255,))
        fig = mix(p["near"], p["mid"], 0.35)
        for k, u in enumerate((0.18, 0.31, 0.47, 0.63, 0.78)):                              # people crossing, some with lanterns
            xx = x0 + (x1 - x0) * u; yy = deck(xx) - 2; s_ = 0.62
            draw_figure(d, xx, yy, s_, fig, seated=False, hat=(k % 2 == 0))
            if k in (1, 3, 4):
                self.windows.append((xx + 14, yy - 32, 8, 11, rng.uniform(0, TAU), 2))
                self.wlights.append((xx + 14, 10, 42, rng.uniform(0, TAU)))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, H - 150), (W * 0.18, H - 120), (W * 0.32, H - 70), (W * 0.42, H), (0, H)], fill=nc + (255,))   # near bank
        for k in range(5): dn.line([(0, H - 132 + k * 26), (W * 0.2 + k * 30, H - 104 + k * 26)], fill=mix(nc, p["moon"], 0.07) + (255,), width=2)
        self._boat(dn, W * 0.46, H - 120, 420, 1.0, mix(nc, p["mid"], 0.25))
        self._boat(dn, W * 0.78, H - 210, 300, 0.7, mix(nc, p["mid"], 0.4))
        dn.line([(W * 0.06, H - 140), (W * 0.06, H - 330)], fill=nc + (255,), width=10)       # mooring post with rope
        dn.line([(W * 0.06, H - 300), (W * 0.46, H - 128)], fill=mix(nc, p["washi"], 0.15) + (255,), width=2)
        bx, by = W * 0.62, H - 168                                                            # boatman with pipe on the boat
        draw_figure(dn, bx, by, 0.9, mix(nc, p["mid"], 0.1), seated=True, hat=False)
        self.embers_pt = (bx + 26, by - 66)
        self.near = near
        self.pipe = (bx + 26, by - 66)
        self.fog_y = hy - 20; self.fog_a = 0.14; self.particles = "mist"

    def build_sumida(self):
        """The wide Sumida by moonlight: a lit pleasure boat with a boatman poling drifts across, a long low bridge on
        many legs in the distance, a weeping willow swaying on the near bank, a noodle stall with lantern and wind chime."""
        p, rng = self.p, self.rng; hy = int(H * 0.55)
        self.back = self.sky(hy, (0.6, 0.17), 44)
        self.back.alpha_composite(hills(hy - 6, 22, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.2), blur=3, base=6))
        self._water(hy, 0.26)
        mx, my, mr = self.moon; self.reflect = (mx, hy, mr)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid); fb = mix(p["far"], p["mid"], 0.5)
        d.rectangle([0, hy - 12, W, hy + 2], fill=fb + (255,))                              # far bank with low roofs and trees
        x = -20
        while x < W:
            w = rng.uniform(40, 110)
            if rng.random() < 0.45: d.ellipse([x, hy - rng.uniform(40, 70), x + w, hy + 4], fill=mix(fb, (10, 24, 16), 0.2) + (255,))
            else:
                self._jroof(d, x, x + w, hy - rng.uniform(14, 24), 12, mix(fb, (0, 0, 0), 0.2), 0.4, 0.15)
                if rng.random() < 0.3: self.windows.append((x + w / 2, hy - 8, 4, 4, rng.uniform(0, TAU), 1))
            x += w * rng.uniform(0.7, 1.1)
        bc = mix(p["far"], p["mid"], 0.35); x0, x1 = W * 0.38, W * 1.05                      # long bridge on many thin legs
        dk = lambda xx: hy - 30 - 14 * math.sin(math.pi * (xx - x0) / (x1 - x0))
        xs = np.linspace(x0, x1, 60)
        d.polygon([(xx, dk(xx)) for xx in xs] + [(xx, dk(xx) + 5) for xx in xs[::-1]], fill=bc + (255,))
        d.line([(xx, dk(xx) - 7) for xx in xs], fill=bc + (255,), width=2)
        for k in range(46):
            xx = x0 + (x1 - x0) * k / 45; d.line([(xx, dk(xx) + 4), (xx, hy + 8)], fill=bc + (255,), width=2)
        for u in (0.12, 0.3, 0.55, 0.8):
            xx = x0 + (x1 - x0) * u; self.windows.append((xx, dk(xx) - 6, 3, 4, rng.uniform(0, TAU), 2)); self.wlights.append((xx, 6, 34, rng.uniform(0, TAU)))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, H - 210), (W * 0.2, H - 190), (W * 0.42, H - 140), (W * 0.5, H), (0, H)], fill=nc + (255,))
        for k in range(4): dn.line([(0, H - 190 + k * 30), (W * 0.24 + k * 40, H - 160 + k * 30)], fill=mix(nc, p["moon"], 0.06) + (255,), width=2)
        tx, tb = W * 0.12, H - 196                                                            # willow trunk (strands animate)
        dn.line([(tx - 20, tb), (tx - 6, tb - 160), (tx + 30, tb - 300), (tx + 90, tb - 420)], fill=nc + (255,), width=30, joint="curve")
        dn.line([(tx + 12, tb - 240), (tx - 60, tb - 360), (tx - 110, tb - 430)], fill=nc + (255,), width=16, joint="curve")
        dn.line([(tx + 60, tb - 380), (tx + 200, tb - 460)], fill=nc + (255,), width=12)
        r2 = random.Random(int(rng.integers(1e6)))
        for k in range(9):                                                                    # thin arching boughs
            ex = tx + 90 + r2.uniform(-300, 260); ey = tb - r2.uniform(400, 470)
            dn.line([(tx + 90, tb - 420), ((tx + 90 + ex) / 2, ey - 50), (ex, ey)], fill=nc + (255,), width=4, joint="curve")
        self.willow = [(tx + r2.uniform(-200, 330), tb - r2.uniform(400, 490), r2.uniform(160, 400), r2.uniform(0, TAU)) for _ in range(150)]
        sx, sb = W * 0.31, H - 150; sc_ = mix(nc, (60, 44, 32), 0.3)                          # noodle stall
        dn.rectangle([sx - 70, sb - 90, sx + 70, sb], fill=sc_ + (255,))
        for k in range(4): dn.rectangle([sx - 62, sb - 84 + k * 21, sx + 62, sb - 70 + k * 21], fill=mix(sc_, (0, 0, 0), 0.25) + (255,))
        dn.line([(sx - 66, sb - 90), (sx - 66, sb - 190)], fill=sc_ + (255,), width=6); dn.line([(sx + 66, sb - 90), (sx + 66, sb - 190)], fill=sc_ + (255,), width=6)
        self._jroof(dn, sx - 100, sx + 100, sb - 186, 34, mix(nc, (0, 0, 0), 0.1), 0.25, 0.08)
        dn.line([(sx - 130, sb - 10), (sx + 160, sb - 260)], fill=sc_ + (255,), width=7)      # carrying pole resting on it
        draw_figure(dn, sx + 120, sb - 4, 0.95, mix(nc, p["mid"], 0.15), seated=True, hat=False)
        self.lamp = (sx + 40, sb - 128); self.lamp_r = 280
        dn.ellipse([sx + 26, sb - 150, sx + 54, sb - 112], fill=mix(p["washi"], p["light"], 0.5) + (255,))   # its round lantern
        self.chime = (sx - 80, sb - 178)
        self.near = near
        self.yakata = dict(y=hy + 150, s=0.95)
        self.fog_y = hy + 10; self.fog_a = 0.13; self.particles = "mist"

    def _proj(self, X, Y, z):
        vx, vy, f = self.vp; return (vx + f * X / z, vy - f * Y / z)

    def build_lanes(self):
        """A merchant lane in one-point perspective: two-storey shophouses with glowing lattice fronts and indigo shop
        curtains, paper lanterns swinging from the eaves, the ward gate at the end, a fire-watch ladder tower with its
        bell, and the bathhouse chimney breathing steam."""
        p, rng = self.p, self.rng; self.vp = (W * 0.6, H * 0.5, 900); P = self._proj
        self.back = self.sky(int(H * 0.56), (0.82, 0.12), 34)
        far = Image.new("RGBA", (W, H), (0, 0, 0, 0)); df = ImageDraw.Draw(far); fc = mix(p["far"], p["mid"], 0.45)
        x = -20
        while x < W:                                                                          # distant roofs at the lane's end
            w = rng.uniform(60, 140); self._jroof(df, x, x + w, H * 0.5 + rng.uniform(-10, 16), 24, fc, 0.35, 0.16); x += w * 0.8
        df.rectangle([0, H * 0.5 + 10, W, H * 0.6], fill=fc + (255,))
        cx = W * 0.53; df.rectangle([cx - 12, H * 0.25, cx + 12, H * 0.52], fill=mix(fc, (0, 0, 0), 0.25) + (255,))   # bathhouse chimney
        self.smoke = (cx, H * 0.24, 300)
        tx = W * 0.665; tb = H * 0.5; tc = mix(fc, (0, 0, 0), 0.3)                              # fire-watch ladder tower
        for dx in (-26, 26): df.line([(tx + dx * 1.4, tb), (tx + dx * 0.7, H * 0.16)], fill=tc + (255,), width=6)
        for k in range(16):
            yy = tb - k * (tb - H * 0.17) / 16; ww = 26 * (1.4 - 0.7 * k / 16); df.line([(tx - ww, yy), (tx + ww, yy)], fill=tc + (255,), width=3)
        df.rectangle([tx - 34, H * 0.15, tx + 34, H * 0.163], fill=tc + (255,))
        for dx in (-32, 32): df.line([(tx + dx, H * 0.15), (tx + dx, H * 0.11)], fill=tc + (255,), width=3)
        df.line([(tx - 34, H * 0.11), (tx + 34, H * 0.11)], fill=tc + (255,), width=3)
        df.line([(tx, H * 0.11), (tx, H * 0.08)], fill=tc + (255,), width=4); df.ellipse([tx - 9, H * 0.08 - 2, tx + 9, H * 0.08 + 18], fill=mix(tc, (150, 120, 70), 0.35) + (255,))
        self.glints = [(tx, H * 0.09)]
        self.back.alpha_composite(far.filter(ImageFilter.GaussianBlur(1)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        g = mix(p["mid"], p["moon"], 0.07)                                                    # the packed-earth lane
        d.polygon([P(-4, -1.6, 2.2), P(4, -1.6, 2.2), P(4, -1.6, 70), P(-4, -1.6, 70)], fill=g + (255,))
        for k in range(30):
            z = rng.uniform(3, 50); X = rng.uniform(-3.5, 3.5); a, b = P(X, -1.6, z), P(X + 0.6, -1.6, z)
            d.line([a, b], fill=mix(g, p["moon"], 0.06) + (255,), width=1)
        d.polygon([P(-4, -1.6, 0.6), P(-4, -1.6, 3.6), P(-4, 4.6, 3.6), P(-4, 4.6, 0.6)], fill=mix(p["near"], p["mid"], 0.3) + (255,))   # nearest wall
        d.polygon([P(4, -1.6, 0.6), P(4, -1.6, 3.6), P(4, 4.6, 3.6), P(4, 4.6, 0.6)], fill=mix(p["near"], p["mid"], 0.2) + (255,))
        gz = 58; gc = mix(p["mid"], (0, 0, 0), 0.25)                                           # ward gate
        for X in (-2.4, 2.4): d.polygon([P(X - 0.15, -1.6, gz), P(X + 0.15, -1.6, gz), P(X + 0.15, 2.6, gz), P(X - 0.15, 2.6, gz)], fill=gc + (255,))
        d.polygon([P(-3.0, 2.6, gz), P(3.0, 2.6, gz), P(3.0, 2.9, gz), P(-3.0, 2.9, gz)], fill=gc + (255,))
        a, b = P(-3.4, 2.9, gz), P(3.4, 2.9, gz); self._jroof(d, a[0], b[0], a[1], 14, gc, 0.4, 0.12)
        d.polygon([P(-2.25, -1.6, gz), P(-0.1, -1.6, gz), P(-0.1, 2.5, gz), P(-2.25, 2.5, gz)], fill=mix(gc, (0, 0, 0), 0.2) + (255,))   # one door shut
        hb = P(3.6, 0.2, gz - 2); self.windows.append((hb[0], hb[1], 6, 5, 0.4, 1))          # gatekeeper's hut window
        washi, lac, indigo = p["washi"], p["lacquer"], (34, 42, 78)
        self.chochin = []
        for side in (-1, 1):
            zs = [3.6] + [3.6 + 4.6 * (k + 1) for k in range(12)]
            for i in range(len(zs) - 1):
                z0, z1 = zs[i], zs[i + 1] - 0.15; X = 4.0 * side
                if z0 > gz - 3: break
                wallc = mix(p["mid"], (0, 0, 0), 0.15 + (0.15 if side > 0 else 0))
                d.polygon([P(X, -1.6, z0), P(X, -1.6, z1), P(X, 4.4, z1), P(X, 4.4, z0)], fill=wallc + (255,))
                lit = (side < 0 and rng.random() < 0.8) or (side > 0 and rng.random() < 0.3)
                fr = [P(X, -1.4, z0 + 0.4), P(X, -1.4, z1 - 0.4), P(X, 1.2, z1 - 0.4), P(X, 1.2, z0 + 0.4)]
                d.polygon(fr, fill=(mix(p["mid"], p["light"], 0.55) if lit else mix(wallc, (0, 0, 0), 0.25)) + (255,))
                if lit:
                    q = P(X, -0.1, (z0 + z1) / 2); self.windows.append((q[0], q[1], 2, 2, rng.uniform(0, TAU), 1))
                nl = int((z1 - z0) * 6)
                for k in range(nl + 1):                                                       # vertical lattice bars
                    z = z0 + 0.4 + (z1 - z0 - 0.8) * k / nl; d.line([P(X, -1.4, z), P(X, 1.2, z)], fill=mix(wallc, (0, 0, 0), 0.2) + (255,), width=max(1, int(9 / z)))
                if side < 0 and rng.random() < 0.75:                                          # shop curtain in panels
                    for k in range(4):
                        za = z0 + 0.6 + (z1 - z0 - 1.2) * k / 4; zb = za + (z1 - z0 - 1.2) / 4 - 0.08
                        d.polygon([P(X + 0.05, 0.4, za), P(X + 0.05, 0.4, zb), P(X + 0.05, 1.25, zb), P(X + 0.05, 1.25, za)], fill=indigo + (255,))
                    m = P(X + 0.05, 0.85, (z0 + z1) / 2); r_ = 70 / ((z0 + z1) / 2)
                    d.ellipse([m[0] - r_ * 0.5, m[1] - r_, m[0] + r_ * 0.5, m[1] + r_], outline=mix(indigo, washi, 0.7) + (255,), width=max(1, int(r_ / 6)))
                ec = mix(p["near"], p["mid"], 0.4)                                            # ground-floor eave and upper eave
                d.polygon([P(X, 1.35, z0 - 0.1), P(X, 1.35, z1 + 0.1), P(X - 0.9 * side, 1.6, z1 + 0.1), P(X - 0.9 * side, 1.6, z0 - 0.1)], fill=ec + (255,))
                d.polygon([P(X, 1.6, z0 - 0.1), P(X, 1.6, z1 + 0.1), P(X - 0.9 * side, 1.75, z1 + 0.1), P(X - 0.9 * side, 1.75, z0 - 0.1)], fill=mix(ec, p["moon"], 0.12) + (255,))
                wl = rng.random() < (0.35 if side < 0 else 0.15)                              # upper-floor slatted window
                d.polygon([P(X, 2.3, z0 + 1.0), P(X, 2.3, z1 - 1.0), P(X, 3.3, z1 - 1.0), P(X, 3.3, z0 + 1.0)], fill=(mix(p["mid"], p["light"], 0.45) if wl else mix(wallc, (0, 0, 0), 0.3)) + (255,))
                for k in range(9):
                    z = z0 + 1.0 + (z1 - z0 - 2.0) * k / 8; d.line([P(X, 2.3, z), P(X, 3.3, z)], fill=wallc + (255,), width=max(1, int(12 / z)))
                d.polygon([P(X, 4.3, z0 - 0.1), P(X, 4.3, z1 + 0.1), P(X - 1.0 * side, 4.55, z1 + 0.1), P(X - 1.0 * side, 4.55, z0 - 0.1)], fill=ec + (255,))
                for zz in (z0 + 0.35, z1 - 0.35):
                    if side < 0 or rng.random() < 0.4:
                        if z0 < 40: self.chochin.append((X - 0.5 * side, 1.32, zz, rng.uniform(0, TAU), int(rng.integers(1, 3)), lit or side < 0))
                if lit and z0 < 30:
                    q0, q1 = P(X, -1.6, z0 + 0.4), P(X, -1.6, z1 - 0.4); q2, q3 = P(X - 2.4 * side, -1.6, z1), P(X - 2.4 * side, -1.6, z0)
                    sp = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sp).polygon([q0, q1, q2, q3], fill=p["light"] + (40,))
                    mid.alpha_composite(sp.filter(ImageFilter.GaussianBlur(10)))
        cat = P(-3.4, 4.6, 17); cs = 60 / 17                                                  # a cat on the near roof edge
        d.ellipse([cat[0] - 4 * cs, cat[1] - 4 * cs, cat[0] + 4 * cs, cat[1]], fill=p["near"] + (255,))
        d.ellipse([cat[0] + 2 * cs, cat[1] - 6.5 * cs, cat[0] + 6 * cs, cat[1] - 2.5 * cs], fill=p["near"] + (255,))
        d.line([(cat[0] - 4 * cs, cat[1] - 1 * cs), (cat[0] - 7 * cs, cat[1] + 3 * cs)], fill=p["near"] + (255,), width=max(2, int(cs)))
        self.mid = mid
        self.chochin.sort(key=lambda c: -c[2])
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, 0), (W * 0.2, 0), (W * 0.12, H * 0.06), (0, H * 0.1)], fill=nc + (255,))   # nearest eave corner
        dn.polygon([(W, 0), (W * 0.86, 0), (W * 0.93, H * 0.05), (W, H * 0.07)], fill=nc + (255,))
        self.near = near
        self.fog_y = H * 0.56; self.fog_a = 0.12; self.particles = "leaves"

    def _plume(self, d, tip, bend, col, r2, s):
        """Pampas-grass plume: a drooping spray of fine silky lines hanging from the stem tip."""
        lean = 1 if bend >= 0 else -1
        for j in range(22):
            v = j / 21; ox, oy = tip[0] + lean * 6 * v * s, tip[1] + v * 70 * s
            L = (16 + 22 * math.sin(math.pi * v)) * s; a = math.pi / 2 + lean * r2.uniform(0.25, 0.9)
            d.line([(ox, oy), (ox + L * math.cos(a) * 0.9, oy + L * math.sin(a) * 0.5)], fill=col + (150,), width=1)
            d.line([(ox, oy), (ox - L * math.cos(a) * 0.5, oy + L * math.sin(a) * 0.4)], fill=col + (120,), width=1)

    def _toro(self, d, x, base, s, col, lit=True):
        """Stone lantern: plinth, stout pillar, middle platform, fire box with a lit window, a cap with curled corners, jewel."""
        c = col + (255,)
        d.polygon([(x - 34 * s, base), (x + 34 * s, base), (x + 26 * s, base - 16 * s), (x - 26 * s, base - 16 * s)], fill=c)
        d.rectangle([x - 11 * s, base - 80 * s, x + 11 * s, base - 16 * s], fill=c)
        d.polygon([(x - 30 * s, base - 80 * s), (x + 30 * s, base - 80 * s), (x + 24 * s, base - 94 * s), (x - 24 * s, base - 94 * s)], fill=c)
        d.rectangle([x - 20 * s, base - 136 * s, x + 20 * s, base - 94 * s], fill=c)
        if lit: self.windows.append((x, base - 115 * s, 16 * s, 20 * s, self.rng.uniform(0, TAU), 1))
        self._jroof(d, x - 46 * s, x + 46 * s, base - 136 * s, 30 * s, col, 0.55, 0.3)
        d.ellipse([x - 9 * s, base - 186 * s, x + 9 * s, base - 164 * s], fill=c)

    def build_pagoda(self):
        """Asakusa at night: the five-storey pagoda with sweeping roofs and a ringed bronze spire, part of the great hall,
        stone lanterns lit along the gravel, the bell in its open belfry, a maple and pampas grass in front."""
        p, rng = self.p, self.rng; hy = int(H * 0.74)
        self.back = self.sky(hy - 100, (0.24, 0.15), 40)
        self.back.alpha_composite(hills(hy - 60, 30, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.45), blur=3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        lac = p["lacquer"]; body = mix(lac, p["mid"], 0.62); rc = mix(p["mid"], (0, 0, 0), 0.25); tile = mix(rc, p["moon"], 0.08)
        px, y = W * 0.6, hy - 30
        d.polygon([(px - 190, hy + 6), (px + 190, hy + 6), (px + 170, y), (px - 170, y)], fill=mix(p["mid"], p["washi"], 0.12) + (255,))   # stone podium
        for k in range(5):                                                                    # five storeys
            bw = 196 * (1 - 0.1 * k); bh = 76 - k * 4
            d.rectangle([px - bw / 2, y - bh, px + bw / 2, y], fill=body + (255,))
            for j in range(4): d.line([(px - bw / 2 + bw * (j + 0.5) / 4, y - bh), (px - bw / 2 + bw * (j + 0.5) / 4, y)], fill=mix(body, (0, 0, 0), 0.3) + (255,), width=3)
            d.rectangle([px - bw * 0.14, y - bh * 0.75, px + bw * 0.14, y], fill=mix(body, (0, 0, 0), 0.4) + (255,))
            d.line([(px - bw / 2 - 6, y - bh * 0.45), (px + bw / 2 + 6, y - bh * 0.45)], fill=mix(body, p["washi"], 0.2) + (255,), width=3)   # balcony rail
            rw = bw * 1.9; y = self._jroof(d, px - rw / 2, px + rw / 2, y - bh + 12, 46, rc, 0.62, 0.3, tiles=tile) + 6
        bz = mix(p["mid"], (150, 120, 70), 0.42)                                              # the spire with nine rings
        d.rectangle([px - 6, y - 230, px + 6, y], fill=bz + (255,))
        for k in range(9): d.ellipse([px - 20 + k * 0.8, y - 40 - k * 17, px + 20 - k * 0.8, y - 32 - k * 17], fill=mix(bz, p["moon"], 0.12) + (255,))
        d.ellipse([px - 11, y - 246, px + 11, y - 224], fill=bz + (255,))
        self.glints = [(px, y - 236)]
        hall = mix(p["mid"], (0, 0, 0), 0.1)                                                  # great hall, left edge
        d.rectangle([-40, hy - 250, W * 0.26, hy], fill=mix(lac, p["mid"], 0.7) + (255,))
        for k in range(6): d.rectangle([W * 0.02 + k * 80, hy - 240, W * 0.02 + k * 80 + 18, hy], fill=mix(lac, p["mid"], 0.5) + (255,))
        self._jroof(d, -300, W * 0.33, hy - 240, 230, hall, 0.4, 0.05, tiles=mix(hall, p["moon"], 0.06))
        bx = W * 0.88; bc = mix(p["mid"], (0, 0, 0), 0.2)                                    # belfry with the bell
        d.polygon([(bx - 110, hy), (bx + 110, hy), (bx + 96, hy - 50), (bx - 96, hy - 50)], fill=mix(p["mid"], p["washi"], 0.1) + (255,))
        for dx in (-80, 80): d.rectangle([bx + dx - 8, hy - 250, bx + dx + 8, hy - 50], fill=bc + (255,))
        self._jroof(d, bx - 150, bx + 150, hy - 250, 70, rc, 0.55, 0.2)
        bell = mix(p["mid"], (110, 100, 70), 0.4)
        d.line([(bx, hy - 250), (bx, hy - 220)], fill=bc + (255,), width=4)
        d.polygon([(bx - 30, hy - 220), (bx + 30, hy - 220), (bx + 42, hy - 108), (bx - 42, hy - 108)], fill=bell + (255,))
        d.ellipse([bx - 30, hy - 232, bx + 30, hy - 208], fill=bell + (255,))
        for k in range(3): d.line([(bx - 32 - k * 3, hy - 190 + k * 30), (bx + 32 + k * 3, hy - 190 + k * 30)], fill=mix(bell, (0, 0, 0), 0.3) + (255,), width=2)
        d.line([(bx - 140, hy - 140), (bx - 50, hy - 140)], fill=mix(bc, p["washi"], 0.1) + (255,), width=10)   # striking beam
        d.line([(bx - 130, hy - 140), (bx - 130, hy - 230)], fill=bc + (255,), width=2); d.line([(bx - 60, hy - 140), (bx - 60, hy - 230)], fill=bc + (255,), width=2)
        g = mix(p["mid"], p["moon"], 0.1)                                                     # gravel courtyard with raked lines
        d.rectangle([0, hy, W, H], fill=g + (255,))
        for k in range(14):
            yy = hy + 8 + k * (H - hy) / 14 * (0.5 + k / 28); d.line([(0, yy), (W, yy)], fill=mix(g, p["moon"], 0.05) + (255,), width=1)
        shp = [(px - 170, hy + 6), (px + 170, hy + 6), (px + 520, H), (px + 80, H)]          # moon shadow of the pagoda
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).polygon(shp, fill=(0, 0, 0, 60)); mid.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
        sc = mix(p["mid"], p["washi"], 0.22)
        for x, s in ((W * 0.4, 0.75), (W * 0.76, 0.75)): self._toro(d, x, hy + 30, s, sc)
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        self._toro(dn, W * 0.3, H - 40, 1.3, mix(nc, p["washi"], 0.12), lit=False)
        dn.rectangle([W * 0.3 - 13, H - 40 - 128, W * 0.3 + 13, H - 40 - 102], fill=mix(p["light"], p["mid"], 0.3) + (255,))
        self.lamp = (W * 0.3, H - 40 - 108); self.lamp_r = 240
        r2 = random.Random(int(rng.integers(1e6)))
        dn.line([(-20, H * 0.34), (W * 0.1, H * 0.24), (W * 0.2, H * 0.18), (W * 0.3, H * 0.15)], fill=nc + (255,), width=26, joint="curve")   # maple bough
        dn.line([(W * 0.1, H * 0.24), (W * 0.16, H * 0.33), (W * 0.24, H * 0.36)], fill=nc + (255,), width=12)
        dn.line([(-20, H * 0.1), (W * 0.06, H * 0.08), (W * 0.17, H * 0.03)], fill=nc + (255,), width=14)
        mc = mix(nc, p["lacquer"], 0.42)
        for _ in range(140):                                                                  # five-pointed maple leaves
            cx, cy = r2.uniform(-20, W * 0.34), r2.uniform(-10, H * 0.4)
            if cy > H * 0.08 + cx * 0.7 and cx > W * 0.22: continue
            rr = r2.uniform(9, 17); a0 = r2.uniform(0, TAU); col = mix(mc, p["ember"], r2.uniform(0, 0.25)) if r2.random() < 0.4 else mc
            pts = []
            for j in range(10):
                a = a0 + j * TAU / 10; R = rr if j % 2 == 0 else rr * 0.42; pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
            dn.polygon(pts, fill=col + (255,))
        for _ in range(26):                                                                   # pampas grass, bottom right
            bx_ = W * r2.uniform(0.82, 1.02); by_ = H + 10; L = r2.uniform(260, 420); bend = r2.uniform(-90, 30)
            pts = [(bx_ + bend * (v ** 2), by_ - L * v) for v in np.linspace(0, 1, 10)]
            dn.line(pts, fill=nc + (255,), width=2)
            self._plume(dn, pts[-1], bend, mix(nc, p["washi"], r2.uniform(0.25, 0.45)), r2, 1.0)
        self.near = near
        self.fog_y = hy - 10; self.fog_a = 0.1; self.particles = "leaves"

    def build_tatami(self):
        """Inside a row-house room: moonlit paper screens with a pine shadow, a hanging ink scroll and ancestor shelf,
        tatami in perspective, a paper floor lamp glowing, a brazier with a steaming iron kettle, a tiny insect cage,
        folded bedding and a vase of pampas grass."""
        p, rng = self.p, self.rng; wy = int(H * 0.62); washi = p["washi"]
        wall = mix(p["mid"], (96, 84, 70), 0.25)
        bg = np.zeros((H, W, 4), np.uint8); bg[..., :3] = mix(wall, (0, 0, 0), 0.25); bg[..., 3] = 255
        self.back = Image.fromarray(bg, "RGBA"); d = ImageDraw.Draw(self.back)
        d.rectangle([0, 0, W, int(H * 0.08)], fill=mix(wall, (0, 0, 0), 0.5) + (255,))      # ceiling beam
        sx0, sx1, sy0 = W * 0.42, W * 1.0, H * 0.1                                           # moonlit shoji
        moonpaper = mix(washi, (120, 150, 210), 0.4); moonpaper = mix(moonpaper, p["mid"], 0.42)
        d.rectangle([sx0, sy0, sx1, wy], fill=moonpaper + (255,))
        pine = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dp = ImageDraw.Draw(pine); r2 = random.Random(int(rng.integers(1e6)))
        pc = mix(moonpaper, p["mid"], 0.55)
        dp.line([(W * 1.02, H * 0.18), (W * 0.86, H * 0.22), (W * 0.72, H * 0.2), (W * 0.6, H * 0.27)], fill=pc + (255,), width=16, joint="curve")
        dp.line([(W * 0.86, H * 0.22), (W * 0.8, H * 0.34), (W * 0.7, H * 0.4)], fill=pc + (255,), width=9)
        for _ in range(16):                                                                   # needle clouds
            cx, cy = r2.uniform(W * 0.58, W * 1.0), r2.uniform(H * 0.12, H * 0.42)
            for j in range(18):
                a = r2.uniform(-0.5, 0.5) + math.pi * (1.5 if j % 2 else 0.5); L = r2.uniform(18, 40)
                dp.line([(cx, cy), (cx + L * math.cos(a) * 1.8, cy + L * math.sin(a) * 0.5)], fill=pc + (255,), width=2)
            dp.ellipse([cx - 50, cy - 14, cx + 50, cy + 10], fill=pc + (255,))
        self.back.alpha_composite(pine.filter(ImageFilter.GaussianBlur(5)))
        d = ImageDraw.Draw(self.back); fr = mix(p["mid"], (60, 44, 30), 0.35)
        for k in range(4):                                                                    # screen frames and fine lattice
            xa = sx0 + (sx1 - sx0) * k / 4; d.rectangle([xa, sy0, xa + 10, wy], fill=fr + (255,))
            for j in range(1, 4): d.line([(xa + (sx1 - sx0) / 4 * j / 4, sy0), (xa + (sx1 - sx0) / 4 * j / 4, wy)], fill=fr + (255,), width=2)
        for j in range(1, 9): d.line([(sx0, sy0 + (wy - sy0) * j / 9), (sx1, sy0 + (wy - sy0) * j / 9)], fill=fr + (255,), width=2)
        d.rectangle([sx0, sy0 - 12, sx1, sy0], fill=fr + (255,)); d.rectangle([sx0, wy - 30, sx1, wy], fill=mix(fr, (0, 0, 0), 0.2) + (255,))
        d.rectangle([W * 0.04, H * 0.1, W * 0.4, wy], fill=wall + (255,))                   # plaster wall + post
        d.rectangle([W * 0.4, H * 0.08, W * 0.43, wy], fill=fr + (255,))
        scx = W * 0.2; d.rectangle([scx - 80, H * 0.13, scx + 80, H * 0.48], fill=mix(washi, wall, 0.45) + (255,))   # hanging scroll
        d.rectangle([scx - 86, H * 0.12, scx + 86, H * 0.135], fill=fr + (255,)); d.rectangle([scx - 86, H * 0.48, scx + 86, H * 0.495], fill=fr + (255,))
        ink = mix(washi, (30, 30, 34), 0.62)
        d.polygon([(scx - 40, H * 0.31), (scx - 4, H * 0.27), (scx + 22, H * 0.28), (scx + 10, H * 0.33), (scx - 20, H * 0.335)], fill=ink + (255,))   # heron body
        d.line([(scx + 16, H * 0.285), (scx + 30, H * 0.24), (scx + 18, H * 0.205), (scx + 26, H * 0.18)], fill=ink + (255,), width=5, joint="curve")   # S-neck
        d.ellipse([scx + 20, H * 0.17, scx + 36, H * 0.19], fill=ink + (255,)); d.line([(scx + 34, H * 0.18), (scx + 66, H * 0.188)], fill=ink + (255,), width=3)   # head, beak
        d.line([(scx - 30, H * 0.31), (scx - 62, H * 0.335)], fill=ink + (255,), width=3)   # tail
        for lx in (scx - 8, scx + 2): d.line([(lx, H * 0.33), (lx + 2, H * 0.43)], fill=ink + (255,), width=2)
        for k in range(7): d.line([(scx - 70 + k * 18, H * 0.46), (scx - 74 + k * 18 + r2.uniform(-10, 10), H * 0.38)], fill=mix(ink, washi, 0.3) + (255,), width=2)
        d.rectangle([W * 0.07, H * 0.53, W * 0.33, H * 0.545], fill=fr + (255,))             # ancestor shelf
        d.ellipse([W * 0.1, H * 0.5, W * 0.13, H * 0.53], fill=mix(washi, wall, 0.3) + (255,)); d.rectangle([W * 0.15, H * 0.505, W * 0.17, H * 0.53], fill=mix(wall, (0, 0, 0), 0.2) + (255,))
        self.incense = (W * 0.29, H * 0.52, 220); self.embers_pt = (W * 0.29, H * 0.52)
        d.line([(W * 0.29, H * 0.53), (W * 0.29, H * 0.52)], fill=(200, 120, 60, 255), width=2)
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dm = ImageDraw.Draw(self.mid)
        vx, vy = W * 0.55, -H * 0.9; floor = mix(p["mid"], (160, 146, 92), 0.34)             # tatami in perspective
        dm.rectangle([0, wy, W, H], fill=floor + (255,))
        edge = mix(p["mid"], (20, 22, 26), 0.4)
        for k in range(-4, 7):
            x0_ = W * 0.5 + k * 420; t_ = (wy - vy) / (H - vy); xt = vx + (x0_ - vx) * t_
            dm.line([(xt, wy), (x0_, H)], fill=edge + (255,), width=6)
        for yy in (wy + 70, wy + 230):
            dm.line([(0, yy), (W, yy)], fill=edge + (255,), width=5)
        for _ in range(400):                                                                  # woven rush texture
            x, y = rng.uniform(0, W), rng.uniform(wy, H); dm.line([(x, y), (x + rng.uniform(8, 24), y)], fill=mix(floor, washi, 0.06) + (255,), width=1)
        ml = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(ml).polygon([(sx0, wy), (W, wy), (W, H), (sx0 - 300, H)], fill=(170, 190, 240, 22))
        self.mid.alpha_composite(ml.filter(ImageFilter.GaussianBlur(30)))
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        ax, ab = W * 0.12, H - 60; afr = mix(nc, (60, 40, 26), 0.35)                          # andon floor lamp
        glowpaper = mix(washi, p["light"], 0.62)
        dn.rectangle([ax - 70, ab - 360, ax + 70, ab - 110], fill=glowpaper + (255,))
        for xx in (ax - 72, ax - 24, ax + 24, ax + 68): dn.rectangle([xx, ab - 368, xx + 6, ab], fill=afr + (255,))
        for yy in (ab - 368, ab - 240, ab - 110): dn.rectangle([ax - 74, yy, ax + 74, yy + 7], fill=afr + (255,))
        dn.rectangle([ax - 80, ab - 10, ax + 80, ab + 6], fill=afr + (255,))
        self.lamp = (ax, ab - 150); self.lamp_r = 640
        hx, hb = W * 0.52, H - 70; hc = mix(nc, p["sea"], 0.35)                               # brazier, charcoal, kettle
        dn.ellipse([hx - 150, hb - 60, hx + 150, hb + 30], fill=hc + (255,))
        dn.rectangle([hx - 150, hb - 150, hx + 150, hb - 15], fill=hc + (255,))
        dn.ellipse([hx - 150, hb - 190, hx + 150, hb - 110], fill=mix(hc, washi, 0.12) + (255,))
        dn.ellipse([hx - 130, hb - 178, hx + 130, hb - 122], fill=mix(washi, (90, 86, 80), 0.6) + (255,))   # ash
        for k in range(9):
            cx = hx + r2.uniform(-60, 60); cy = hb - 150 + r2.uniform(-10, 6); rw, rh = r2.uniform(10, 18), r2.uniform(6, 10)
            dn.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=mix(p["ember"], (40, 14, 8), r2.uniform(0.3, 0.7)) + (255,))
        self.coals = (hx, hb - 150)
        kc = mix(nc, (40, 36, 34), 0.3)
        dn.ellipse([hx - 70, hb - 290, hx + 70, hb - 170], fill=kc + (255,))
        dn.rectangle([hx - 26, hb - 300, hx + 26, hb - 284], fill=kc + (255,))
        dn.line([(hx + 60, hb - 240), (hx + 118, hb - 290)], fill=kc + (255,), width=14)      # spout
        dn.arc([hx - 64, hb - 380, hx + 64, hb - 230], 200, 340, fill=kc + (255,), width=6)  # handle
        dn.line([(hx - 30, hb - 270), (hx - 36, hb - 200)], fill=mix(kc, p["moon"], 0.12) + (255,), width=3)
        self.steam = (hx + 120, hb - 296, 260)
        cx_, cb = W * 0.36, H - 260; cg = mix(nc, (120, 100, 60), 0.35)                       # insect cage on a low shelf
        dn.rectangle([W * 0.3, cb, W * 0.47, cb + 14], fill=afr + (255,)); dn.rectangle([W * 0.31, cb + 14, W * 0.32, H], fill=afr + (255,)); dn.rectangle([W * 0.45, cb + 14, W * 0.46, H], fill=afr + (255,))
        dn.polygon([(cx_ - 40, cb), (cx_ + 40, cb), (cx_ + 34, cb - 70), (cx_, cb - 92), (cx_ - 34, cb - 70)], outline=cg + (255,), width=3)
        for k in range(9): dn.line([(cx_ - 34 + k * 8.5, cb), (cx_ - 34 + k * 8.5, cb - 70 + (abs(k - 4) * -4 if False else 0))], fill=cg + (255,), width=2)
        vx_ = W * 0.43; dn.polygon([(vx_ - 22, cb), (vx_ + 22, cb), (vx_ + 14, cb - 70), (vx_ - 14, cb - 70)], fill=mix(nc, p["sea"], 0.4) + (255,))   # vase + grass
        for _ in range(9):
            bend = r2.uniform(-140, 120); L = r2.uniform(160, 260)
            pts = [(vx_ + bend * v ** 2, cb - 70 - L * v) for v in np.linspace(0, 1, 9)]; dn.line(pts, fill=nc + (255,), width=2)
            self._plume(dn, pts[-1], bend, mix(nc, washi, 0.35), r2, 0.7)
        fx = W * 0.8; fc = mix(nc, (90, 60, 50), 0.35)                                        # folded bedding
        for k, (h, c) in enumerate(((70, fc), (60, mix(fc, (60, 70, 110), 0.4)), (54, mix(fc, washi, 0.15)))):
            yb = H - 40 - k * 64; dn.rounded_rectangle([fx - 190 + k * 8, yb - h, fx + 190 - k * 8, yb], radius=22, fill=c + (255,))
        dn.rounded_rectangle([fx - 70, H - 40 - 3 * 64 - 40, fx + 70, H - 40 - 3 * 64 + 4], radius=16, fill=mix(fc, washi, 0.3) + (255,))   # buckwheat pillow
        self.near = near
        self.fog_a = 0.0; self.particles = "dust"

    def _chochin(self, img, ph):
        """EP09: round paper lanterns hanging from the eaves, each swinging gently on its hook at its own rhythm."""
        p = self.p; P = self._proj; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for X, Y, z, f, k, lit in self.chochin:
            hx, hy_ = P(X, Y + 0.25, z); s = 900 / z * 0.42
            ang = 0.09 * math.sin(ph * k + f) + 0.03 * math.sin(ph * 3 + f * 2)
            L = s * 0.5; cx, cy = hx + L * math.sin(ang) * 1.6, hy_ + L + s * 0.55
            d.line([(hx, hy_), (cx, cy - s * 0.55)], fill=(20, 16, 14, 255), width=max(1, int(s / 30)))
            if lit:
                fl = 0.85 + 0.1 * math.sin(ph * 5 + f) + 0.05 * math.sin(ph * 13 + f)
                R = int(s * 2.2) + 4; img.alpha_composite(self.tint(self.glow_sm.resize((R * 2, R * 2)), p["light"], 0.42 * fl), (int(cx - R), int(cy - R)))
                body = mix(p["washi"], p["light"], 0.4 + 0.15 * fl) if k == 1 else mix(p["lacquer"], p["light"], 0.35 * fl)
            else: body = mix(p["washi"], p["mid"], 0.7)
            rw, rh = s * 0.42, s * 0.55
            d.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=body + (255,))
            for j in range(1, 6):
                yy = cy - rh + 2 * rh * j / 6; ww = rw * math.sqrt(max(0, 1 - ((yy - cy) / rh) ** 2))
                d.line([(cx - ww, yy), (cx + ww, yy)], fill=mix(body, (0, 0, 0), 0.22) + (255,), width=max(1, int(s / 40)))
            d.rectangle([cx - rw * 0.5, cy - rh - s * 0.06, cx + rw * 0.5, cy - rh + s * 0.04], fill=(18, 14, 12, 255))
            d.rectangle([cx - rw * 0.5, cy + rh - s * 0.04, cx + rw * 0.5, cy + rh + s * 0.06], fill=(18, 14, 12, 255))
        img.alpha_composite(lay)

    def _yakata(self, img, t, ph):
        """EP09: a roofed pleasure boat with glowing paper walls drifting right-to-left once per loop, boatman poling at
        the stern, its gold reflection trembling on the river."""
        Y = self.yakata; s = Y["s"]; p = self.p; L = 520 * s; u = t / LOOP_S
        x = W + L * 0.7 - u * (W + L * 1.6); y = Y["y"] + 2 * s * math.sin(ph * 3)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); c = (8, 8, 12, 255)
        x0, x1 = x - L / 2, x + L / 2
        for j in range(10):                                                                   # reflection of the lit cabin
            yy = y + 14 * s + j * 9 * s; wob = 6 * s * math.sin(ph * 3 + j * 1.1)
            d.line([(x0 + 70 * s + wob, yy), (x1 - 110 * s + wob, yy)], fill=p["light"] + (int(120 - j * 11),), width=max(2, int(4 * s)))
        d.polygon([(x0 - 30 * s, y - 30 * s), (x1 + 20 * s, y - 24 * s), (x1, y + 10 * s), (x0 + 10 * s, y + 12 * s)], fill=c)   # hull
        cx0, cx1, ct = x0 + 60 * s, x1 - 100 * s, y - 120 * s
        paper = mix(p["washi"], p["light"], 0.55 + 0.06 * math.sin(ph * 5))
        d.rectangle([cx0, ct, cx1, y - 28 * s], fill=paper + (255,))
        for k in range(9): xx = cx0 + (cx1 - cx0) * k / 8; d.line([(xx, ct), (xx, y - 28 * s)], fill=(40, 26, 18, 255), width=max(2, int(4 * s)))
        d.line([(cx0, ct + 40 * s), (cx1, ct + 40 * s)], fill=(40, 26, 18, 160), width=max(1, int(2 * s)))
        for k, gx in enumerate((0.3, 0.62)):                                                  # shadows of guests on the paper
            fx = cx0 + (cx1 - cx0) * gx; d.ellipse([fx - 16 * s, ct + 36 * s, fx + 16 * s, ct + 64 * s], fill=mix(paper, (40, 26, 18), 0.45) + (255,))
            d.polygon([(fx - 30 * s, y - 28 * s), (fx + 30 * s, y - 28 * s), (fx + 18 * s, ct + 62 * s), (fx - 18 * s, ct + 62 * s)], fill=mix(paper, (40, 26, 18), 0.45) + (255,))
        d.polygon([(cx0 - 40 * s, ct + 6 * s), (cx1 + 40 * s, ct + 6 * s), (cx1 + 10 * s, ct - 26 * s), (cx0 - 10 * s, ct - 26 * s)], fill=c)   # roof
        d.line([(cx0 - 40 * s, ct + 6 * s), (cx1 + 40 * s, ct + 6 * s)], fill=mix((8, 8, 12), p["moon"], 0.25) + (255,), width=max(1, int(2 * s)))
        st = math.sin(ph * 4); bx = x1 - 50 * s; by = y - 26 * s                               # boatman at the stern, poling
        hip = (bx + 6 * s * st, by - 62 * s); sh = (bx - 10 * s + 14 * s * st, by - 116 * s)
        d.line([(bx - 8 * s, by), hip, (bx + 10 * s, by)], fill=c, width=max(2, int(9 * s)))
        d.line([hip, sh], fill=c, width=max(3, int(18 * s)))
        d.ellipse([sh[0] - 10 * s, sh[1] - 28 * s, sh[0] + 10 * s, sh[1] - 6 * s], fill=c)
        d.polygon([(sh[0] - 22 * s, sh[1] - 14 * s), (sh[0], sh[1] - 34 * s), (sh[0] + 22 * s, sh[1] - 14 * s)], fill=c)   # straw hat
        top = (sh[0] - 40 * s - 20 * s * st, sh[1] - 120 * s); bot = (sh[0] + 90 * s + 30 * s * st, y + 40 * s)
        d.line([top, bot], fill=c, width=max(2, int(5 * s)))
        img.alpha_composite(lay)
        R = int(300 * s); g = self.tint(self.glow_lg.resize((R * 2, R)), p["light"], 0.22)
        img.alpha_composite(g, (int((cx0 + cx1) / 2 - R), int(ct + 40 * s - R // 2)))

    def _willow(self, img, ph):
        """EP09: willow strands hanging from the boughs, swaying together in a slow breeze (stronger towards the tips)."""
        nc = self.p["near"]; d = ImageDraw.Draw(img)
        for x, y, L, f in self.willow:
            sw = 26 * math.sin(ph + x / 400) + 8 * math.sin(ph * 3 + f)
            pts = [(x + sw * v ** 1.8 + 6 * math.sin(f + v * 3), y + L * v) for v in np.linspace(0, 1, 9)]
            d.line(pts, fill=nc + (255,), width=3)
        cx, cy = self.chime; a = 0.18 * math.sin(ph * 2) + 0.08 * math.sin(ph * 7)          # wind chime and its paper strip
        d.line([(cx, cy), (cx, cy + 16)], fill=nc + (255,), width=2)
        d.pieslice([cx - 12, cy + 10, cx + 12, cy + 34], 180, 360, fill=mix(nc, (90, 80, 60), 0.4) + (255,))
        tx, ty = cx + 60 * math.sin(a), cy + 22 + 60 * math.cos(a)
        d.line([(cx, cy + 22), (tx, ty)], fill=mix(nc, (90, 80, 60), 0.4) + (255,), width=1)
        d.polygon([(tx - 6, ty), (tx + 6, ty), (tx + 6 + 10 * math.sin(a * 3), ty + 46), (tx - 6 + 10 * math.sin(a * 3), ty + 46)], fill=mix(self.p["washi"], self.p["light"], 0.3) + (255,))

    def _steam(self, img, ph):
        """EP09: steam curling from the kettle spout and the red breath of the charcoal beneath it."""
        x, y, h = self.steam; p = self.p; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for s_ in range(2):
            pts = []
            for j in range(50):
                v = j / 49; pts.append((x + 10 * v + (6 + 50 * v ** 1.5) * math.sin(v * 7 - ph * 2 + s_ * 2.5) - 30 * v, y - v * h))
            for j in range(49):
                v = j / 49; d.line([pts[j], pts[j + 1]], fill=mix(p["washi"], p["moon"], 0.4) + (int(120 * (1 - v) ** 1.2 * min(1, v * 6)),), width=max(3, int(4 + 14 * v)))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(4)))
        cx, cy = self.coals; fl = 0.7 + 0.2 * math.sin(ph * 3) + 0.1 * math.sin(ph * 11)
        img.alpha_composite(self.tint(self.glow_lg.resize((300, 120)), p["ember"], 0.55 * fl), (int(cx - 150), int(cy - 60)))

    def _pipe(self, img, ph):
        """EP09: the moored boatman's pipe bowl brightening as he draws on it, twice a loop, with a wisp of smoke."""
        x, y = self.pipe; u = (ph / TAU * 2) % 1; a = 0.35 + 0.65 * math.exp(-((u - 0.2) / 0.06) ** 2)
        img.alpha_composite(self.tint(self.glow_sm.resize((24, 24)), self.p["ember"], a), (int(x - 12), int(y - 12)))
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for j in range(20):
            v = j / 19; q = (x + 30 * v + 8 * math.sin(v * 6 + ph * 2), y - 6 - 120 * v)
            d.ellipse([q[0] - 3 - 8 * v, q[1] - 3 - 8 * v, q[0] + 3 + 8 * v, q[1] + 3 + 8 * v], fill=(200, 196, 190, int(40 * (1 - v))))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3)))

    def _owl(self, img, t):
        """EP08: a little owl crossing the sky once per loop - long glides broken by a few soft wingbeats."""
        O = self.owl; u = t / LOOP_S; s = O["s"]
        x = -120 + (W + 240) * u; y = O["y"] + 40 * math.sin(TAU * u) + 10 * math.sin(TAU * u * 3)
        beat = math.sin(TAU * u * 22) if (u * 4) % 1 < 0.35 else 0.15 * math.sin(TAU * u * 8)
        c = mix(self.p["near"], self.p["mid"], 0.3) + (255,)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        d.ellipse([x - 18 * s, y - 9 * s, x + 16 * s, y + 9 * s], fill=c); d.ellipse([x + 8 * s, y - 12 * s, x + 26 * s, y + 6 * s], fill=c)
        d.polygon([(x - 18 * s, y - 2 * s), (x - 32 * s, y - 6 * s), (x - 30 * s, y + 4 * s)], fill=c)
        for k, a in ((1, 1.0), (-1, 0.55)):
            tip = (x - 6 * s, y - k * (8 + 44 * beat * a + 18) * s)
            d.polygon([(x - 12 * s, y), (x + 10 * s, y), (tip[0] + 14 * s, tip[1]), tip], fill=c)
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(0.8)))

    def _incense(self, img, ph):
        """EP08: a thin thread of incense smoke from the household altar, rising straight, then curling and fading."""
        x, y, h = self.incense; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        col = mix(self.p["moon"], self.p["horizon"], 0.3)
        pts = []
        for j in range(60):
            v = j / 59; pts.append((x + (4 + 40 * v ** 2) * math.sin(v * 9 - ph * 2) + 18 * v * math.sin(ph + v * 3), y - v * h))
        for j in range(59):
            v = j / 59; d.line([pts[j], pts[j + 1]], fill=col + (int(110 * (1 - v) ** 1.2),), width=max(2, int(2 + 6 * v)))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2.2)))
        ex, ey = self.embers_pt; fl = 0.7 + 0.3 * math.sin(ph * 5)
        img.alpha_composite(self.tint(self.glow_sm, self.p["ember"], 0.6 * fl), (int(ex - 16), int(ey - 16)))

    def _lamps(self, img, ph):
        """EP08: small oil-lamp flames on stands, each leaning and steadying on its own rhythm."""
        p = self.p; d = ImageDraw.Draw(img)
        for i, (lx, ly, s) in enumerate(self.lamps):
            fl = 0.86 + 0.09 * math.sin(ph * 5 + i * 2) + 0.05 * math.sin(ph * 11 + i)
            R = int(330 * s); img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R * 2)), p["light"], 0.3 * fl), (int(lx - R), int(ly - R)))
            lean = 4 * math.sin(ph * 3 + i); fh = 26 * s * fl
            d.polygon([(lx - 7 * s, ly), (lx + lean, ly - fh), (lx + 7 * s, ly), (lx, ly + 5 * s)], fill=(255, 210, 136, 255))
            d.polygon([(lx - 3 * s, ly), (lx + lean * 0.6, ly - fh * 0.6), (lx + 3 * s, ly)], fill=(255, 246, 222, 255))

    def _eyes(self, img, ph):
        """EP08: the perched owl's yellow eyes, blinking slowly twice per loop."""
        u = (ph / TAU) % 1; open_ = 0.0 if (abs(u - 0.31) < 0.012 or abs(u - 0.77) < 0.012) else 1.0
        d = ImageDraw.Draw(img)
        for x, y in self.eyes:
            if open_:
                img.alpha_composite(self.tint(self.glow_sm.resize((20, 20)), (255, 210, 90), 0.5), (int(x - 10), int(y - 10)))
                d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(236, 196, 80, 255)); d.ellipse([x - 1.5, y - 1.5, x + 1.5, y + 1.5], fill=(10, 8, 6, 255))
            else: d.line([(x - 4, y), (x + 4, y)], fill=(40, 34, 28, 255), width=2)

    def _glints(self, img, ph):
        """EP08: a slow glint of moonlight on the bronze spear tip."""
        for i, (x, y) in enumerate(self.glints):
            a = 0.25 + 0.75 * max(0.0, math.sin(ph + i)) ** 6; R = int(10 + 26 * a)
            img.alpha_composite(self.tint(self.glow_sm.resize((R * 2, R * 2)), (255, 248, 226), a), (int(x - R), int(y - R)))

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
        n = {"embers": 26, "fireflies": 22, "dust": 34, "snow": 90, "sand": 70, "mist": 16, "spray": 40, "moths": 14, "leaves": 16, "thistledown": 18, "drizzle": 110}[self.particles]
        self.parts = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0, TAU), int(rng.integers(1, 3)), rng.uniform(0.4, 1.0)) for _ in range(n)]
        self.glow_sm = self._glow(16); self.glow_lg = self._glow(90)
        self.moth_c = [(x, y) for x, y, _ in self.lamps] + ([self.lamp] if self.lamp else [])

    # ------------------------------------------------------------ EP10 medieval castle
    def _crenels(self, d, x0, x1, y, mh, mw, gw, col):
        """Battlements along a wall top at y: merlons mw wide rising mh, with crenels gw wide between them."""
        x = x0
        while x < x1:
            d.rectangle([x, y - mh, min(x + mw, x1), y + 1], fill=col + (255,)); x += mw + gw

    def _rtower(self, d, cx, top, base, w, col, slits=3, lit=0.0):
        """Round tower: a shaded cylinder (lit from the right), a corbelled parapet with battlements, arrow slits."""
        dark = mix(col, (0, 0, 0), 0.5)
        for i in range(int(w)):
            u = i / w; sh = (math.sin(math.pi * u) ** 0.6) * (0.75 + 0.25 * u)
            d.line([(cx - w / 2 + i, top), (cx - w / 2 + i, base)], fill=mix(dark, col, sh) + (255,))
        cw = w * 0.07
        d.rectangle([cx - w / 2 - cw, top - 16, cx + w / 2 + cw, top], fill=mix(dark, col, 0.8) + (255,))
        for k in range(7): d.rectangle([cx - w / 2 - cw + k * (w + 2 * cw) / 7 + 3, top, cx - w / 2 - cw + k * (w + 2 * cw) / 7 + 9, top + 8], fill=dark + (255,))
        n = 5; mw = (w + 2 * cw) / (n * 1.6)
        for k in range(n):
            x = cx - w / 2 - cw + k * mw * 1.6 + mw * 0.3; d.rectangle([x, top - 16 - 24, x + mw, top - 16], fill=mix(dark, col, 0.6 + 0.4 * k / n) + (255,))
        for j in range(slits):
            y = top + 40 + (base - top - 80) * (j + 0.5) / slits; x = cx + w * (0.1 if j % 2 else -0.08)
            if self.rng.random() < lit: self.windows.append((x, y, 6, 22, self.rng.uniform(0, TAU), 1))
            else: d.rectangle([x - 3, y - 12, x + 3, y + 12], fill=mix(dark, (0, 0, 0), 0.5) + (255,))

    def _courses(self, d, x0, x1, y0, y1, col, step=18):
        for y in np.arange(y0 + step, y1, step): d.line([(x0, y), (x1, y)], fill=col + (90,), width=1)

    def build_castle(self):
        """Across the moat at dusk: curtain wall with round towers, the twin-towered gatehouse with a lit arch and a torch,
        the old square keep behind, the great hall roof with its smoke louvre, banners on the towers, the drawbridge down
        across the moat, reflections of lit slits trembling on the water; a willow and reeds on the near bank."""
        p, rng = self.p, self.rng; hy = int(H * 0.6); wy = int(H * 0.75); st = p["stone"]
        self.back = self.sky(hy, (0.8, 0.16), 40)
        self.back.alpha_composite(hills(hy - 40, 42, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.3), blur=3))
        self.back.alpha_composite(hills(hy + 20, 20, int(rng.integers(1e6)), mix(p["far"], p["mid"], 0.55), blur=1))
        self._water(wy, 0.2)
        mx, my, mr = self.moon; self.reflect = (mx, wy + 4, mr)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        wc = mix(p["mid"], st, 0.26); tc = mix(p["mid"], st, 0.34); kc = mix(wc, p["far"], 0.4)
        d.polygon([(W * 0.06, wy), (W * 0.12, wy - 46), (W * 0.98, wy - 46), (W * 1.03, wy)], fill=mix(p["mid"], (44, 56, 44), 0.25) + (255,))
        kx, kw, kt = W * 0.68, 250, hy - 380                                                  # the old square keep
        d.rectangle([kx - kw / 2, kt, kx + kw / 2, wy - 46], fill=kc + (255,))
        d.rectangle([kx + kw * 0.1, kt, kx + kw / 2, wy - 46], fill=mix(kc, st, 0.12) + (255,))
        for sx in (-1, 1): d.rectangle([kx + sx * kw / 2 - 24, kt - 44, kx + sx * kw / 2 + 24, kt + 30], fill=mix(kc, st, 0.08) + (255,))
        self._crenels(d, kx - kw / 2, kx + kw / 2, kt, 20, 24, 16, kc)
        for sx in (-1, 1): self._crenels(d, kx + sx * kw / 2 - 24, kx + sx * kw / 2 + 24, kt - 44, 16, 12, 12, mix(kc, st, 0.08))
        for (x, y) in ((kx - 40, kt + 90), (kx + 50, kt + 170)): self.windows.append((x, y, 10, 26, rng.uniform(0, TAU), 1))
        d.rectangle([kx + 45, kt - 120, kx + 49, kt - 44], fill=kc + (255,)); self.banners.append((kx + 49, kt - 118, 92, 0.0))
        hx0, hx1, wt = W * 0.3, W * 0.45, hy - 80                                             # the hall roof with its louvre
        d.polygon([(hx0, wt + 4), (hx1, wt + 4), (hx1 - 40, wt - 120), (hx0 + 40, wt - 120)], fill=mix(p["mid"], (60, 44, 40), 0.3) + (255,))
        lx = (hx0 + hx1) / 2; d.rectangle([lx - 18, wt - 150, lx + 18, wt - 118], fill=mix(p["mid"], (60, 44, 40), 0.2) + (255,))
        d.polygon([(lx - 26, wt - 150), (lx + 26, wt - 150), (lx, wt - 176)], fill=mix(p["mid"], (60, 44, 40), 0.2) + (255,))
        self.smoke = (lx, wt - 170, 260)
        d.rectangle([W * 0.13, wt, W * 0.96, wy - 40], fill=wc + (255,))                     # the curtain wall
        self._crenels(d, W * 0.13, W * 0.96, wt, 20, 26, 17, wc)
        self._courses(d, W * 0.13, W * 0.96, wt, wy - 40, mix(wc, (0, 0, 0), 0.3), 22)
        for cx in (W * 0.13, W * 0.3, W * 0.81, W * 0.96): self._rtower(d, cx, hy - 160, wy - 34, 124, tc, 3, 0.35)
        gx = W * 0.545; gt = hy - 250                                                         # twin-towered gatehouse
        d.rectangle([gx - 60, gt + 40, gx + 60, wy - 34], fill=mix(tc, (0, 0, 0), 0.1) + (255,))
        self._crenels(d, gx - 60, gx + 60, gt + 40, 22, 20, 14, mix(tc, (0, 0, 0), 0.1))
        for sx in (-1, 1): self._rtower(d, gx + sx * 98, gt, wy - 26, 142, tc, 3, 0.5)
        for sx in (-1, 1):
            d.rectangle([gx + sx * 98 - 2, gt - 150, gx + sx * 98 + 2, gt - 40], fill=tc + (255,)); self.banners.append((gx + sx * 98 + 2, gt - 148, 110, 1.3 + sx))
        aw, at = 46, wy - 175
        archc = mix(p["light"], p["mid"], 0.45)
        d.rectangle([gx - aw, at, gx + aw, wy - 30], fill=archc + (255,)); d.pieslice([gx - aw, at - aw, gx + aw, at + aw], 180, 360, fill=archc + (255,))
        for k in range(6): d.line([(gx - aw + 6 + k * (2 * aw - 12) / 5, at - aw * 0.8), (gx - aw + 6 + k * (2 * aw - 12) / 5, at - 10)], fill=mix(p["mid"], (0, 0, 0), 0.4) + (255,), width=3)   # portcullis drawn up
        d.line([(gx - aw, at - 30), (gx + aw, at - 30)], fill=mix(p["mid"], (0, 0, 0), 0.4) + (255,), width=3)
        self.wlights.append((gx, 80, 150, 0.4))
        for x, y, w, h, f, k in list(self.windows):
            if y > hy - 200: self.wlights.append((x, 26, 70, f))
        bc = mix(p["mid"], (70, 52, 36), 0.35)                                                # the drawbridge, down
        d.polygon([(gx - aw, wy - 30), (gx + aw, wy - 30), (gx + 150, H - 70), (gx - 150, H - 70)], fill=bc + (255,))
        for k in range(1, 9):
            v = (k / 9) ** 1.4; y = wy - 30 + v * (H - 100 - wy); hw = aw + v * 104
            d.line([(gx - hw, y), (gx + hw, y)], fill=mix(bc, (0, 0, 0), 0.35) + (255,), width=2)
        for sx in (-1, 1): d.line([(gx + sx * aw, wy - 90), (gx + sx * 150, H - 120)], fill=mix(bc, (0, 0, 0), 0.5) + (255,), width=4)   # chains
        self.lamp = (gx + aw + 22, at - 6); self.lamp_r = 300
        d.line([(gx + aw + 22, at + 30), (gx + aw + 22, at + 4)], fill=(30, 22, 18, 255), width=6)
        self.mid = mid
        near = hills(H - 80, 16, int(rng.integers(1e6)), p["near"]); dn = ImageDraw.Draw(near); nc = p["near"]
        r2 = random.Random(int(rng.integers(1e6)))
        dn.polygon([(0, H), (0, H * 0.18), (40, H * 0.2), (70, H - 90), (110, H)], fill=nc + (255,))   # willow trunk, left edge
        for _ in range(70):
            x = r2.uniform(-40, 330); y = H * 0.12 + r2.uniform(0, 80) + abs(x - 60) * 0.25; L = r2.uniform(180, 460)
            dn.line([(x + 8 * math.sin(v * 3) * v + 20 * v ** 2, y + L * v) for v in np.linspace(0, 1, 8)], fill=nc + (255,), width=2)
        dn.line([(-20, H * 0.14), (120, H * 0.12), (300, H * 0.16)], fill=nc + (255,), width=16, joint="curve")
        for _ in range(60):                                                                   # reeds and bulrushes
            x = r2.uniform(W * 0.62, W * 1.02); L = r2.uniform(90, 230); bend = r2.uniform(-30, 30)
            dn.line([(x, H - 40), (x + bend, H - 40 - L)], fill=nc + (255,), width=3)
            if r2.random() < 0.3: dn.ellipse([x + bend - 5, H - 40 - L - 4, x + bend + 5, H - 40 - L + 30], fill=nc + (255,))
        self.near = near
        self.fog_y = wy - 20; self.fog_a = 0.16; self.particles = "thistledown"

    def build_bailey(self):
        """The outer courtyard from inside the gate: the inner face of the gatehouse with the portcullis down, lean-to
        stables with a horse looking out, the bakehouse with its oven glowing through the door and smoke from the
        chimney, a dovecote in the corner tower, cobbles, and the stone well-head with its roof and windlass."""
        p, rng = self.p, self.rng; hy = int(H * 0.5); gy = int(H * 0.79); st = p["stone"]
        r2 = random.Random(int(rng.integers(1e6)))
        self.back = self.sky(hy, (0.2, 0.15), 34)
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        wc = mix(mix(p["mid"], st, 0.26), p["far"], 0.25); wt = int(H * 0.37)
        d.rectangle([0, wt, W, gy], fill=wc + (255,)); self._crenels(d, 0, W, wt, 26, 30, 22, wc)
        self._courses(d, 0, W, wt, gy, mix(wc, (0, 0, 0), 0.3), 24)
        gx = W * 0.44; gc = mix(p["mid"], st, 0.32); gt = int(H * 0.18)                      # gatehouse, inner face
        d.rectangle([gx - 190, gt, gx + 190, gy], fill=gc + (255,)); self._crenels(d, gx - 190, gx + 190, gt, 28, 30, 20, gc)
        self._courses(d, gx - 190, gx + 190, gt, gy, mix(gc, (0, 0, 0), 0.3), 26)
        aw, at = 78, gy - 220
        road = mix(p["sea"], p["moon"], 0.18)
        d.rectangle([gx - aw, at, gx + aw, gy], fill=road + (255,)); d.pieslice([gx - aw, at - aw, gx + aw, at + aw], 180, 360, fill=road + (255,))
        ir = (12, 12, 16, 255)                                                                # the portcullis, down
        for k in range(9): x = gx - aw + 8 + k * (2 * aw - 16) / 8; d.line([(x, at - aw * 0.9), (x, gy)], fill=ir, width=6)
        for k in range(7): y = at - aw * 0.5 + k * 40; d.line([(gx - aw, y), (gx + aw, y)], fill=ir, width=5)
        for k in range(9): x = gx - aw + 8 + k * (2 * aw - 16) / 8; d.polygon([(x - 5, gy - 2), (x + 5, gy - 2), (x, gy + 10)], fill=ir)
        self.windows += [(gx - 140, gy - 120, 34, 46, 0.3, 1), (gx + 10, gt + 90, 22, 34, 1.7, 1)]   # porter's lodge, windlass room
        sc = mix(p["mid"], (78, 58, 40), 0.4); sx1 = W * 0.27                                # lean-to stables
        d.polygon([(-20, gy - 210), (sx1 + 24, gy - 210), (sx1, gy - 300), (-20, gy - 300)], fill=mix(sc, (0, 0, 0), 0.35) + (255,))
        for k in range(12): d.line([(-20 + k * 30, gy - 300), (-20 + k * 31, gy - 210)], fill=mix(sc, (0, 0, 0), 0.5) + (255,), width=2)
        d.rectangle([-20, gy - 210, sx1, gy], fill=sc + (255,))
        for k in range(20): d.line([(-20 + k * 26, gy - 210), (-20 + k * 26, gy)], fill=mix(sc, (0, 0, 0), 0.25) + (255,), width=2)
        for k, x in enumerate((60, 230, 400)):
            d.rectangle([x, gy - 170, x + 110, gy - 90], fill=(8, 8, 10, 255)); d.rectangle([x, gy - 90, x + 110, gy], fill=mix(sc, (0, 0, 0), 0.2) + (255,))
            d.line([(x, gy - 90), (x + 110, gy)], fill=mix(sc, (0, 0, 0), 0.45) + (255,), width=4)
        self.horse = (285, gy - 92)
        bx0, bx1 = W * 0.66, W * 0.9; bk = mix(p["mid"], st, 0.4)                            # the bakehouse
        d.polygon([(bx0 - 24, gy - 230), (bx1 + 24, gy - 230), ((bx0 + bx1) / 2, gy - 340)], fill=mix(p["mid"], (70, 50, 46), 0.35) + (255,))
        d.rectangle([bx1 - 80, gy - 440, bx1 - 40, gy - 260], fill=bk + (255,)); self.smoke = (bx1 - 60, gy - 450, 300)
        d.rectangle([bx0, gy - 230, bx1, gy], fill=bk + (255,)); self._courses(d, bx0, bx1, gy - 230, gy, mix(bk, (0, 0, 0), 0.3), 20)
        dx0, dx1 = bx0 + 70, bx0 + 170
        d.rectangle([dx0, gy - 160, dx1, gy], fill=mix(p["light"], p["mid"], 0.62) + (255,))
        d.polygon([(dx1, gy - 160), (dx1 + 40, gy - 150), (dx1 + 40, gy + 8), (dx1, gy)], fill=mix(sc, (0, 0, 0), 0.2) + (255,))   # door ajar
        self.oven = (dx0 + 50, gy - 60, 170)
        self.windows.append((bx1 - 90, gy - 140, 30, 36, 2.2, 1))
        self.spill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(self.spill).polygon([(dx0, gy), (dx1, gy), (dx1 + 160, H - 120), (dx0 - 120, H - 120)], fill=p["light"] + (40,))
        self.spill = self.spill.filter(ImageFilter.GaussianBlur(24))
        tx = W * 0.97; tcol = mix(p["mid"], st, 0.3)                                          # corner tower with dovecote
        d.rectangle([tx - 90, H * 0.12, W + 20, gy], fill=tcol + (255,)); self._crenels(d, tx - 90, W + 20, H * 0.12, 24, 22, 16, tcol)
        for r in range(6):
            for c in range(3):
                x = tx - 70 + c * 34; y = H * 0.2 + r * 30; d.rectangle([x, y, x + 16, y + 14], fill=(10, 10, 12, 255))
                if r2.random() < 0.4: d.ellipse([x + 3, y + 3, x + 13, y + 12], fill=mix(tcol, p["moon"], 0.3) + (255,))
        gcol = mix(p["mid"], st, 0.14)
        d.rectangle([0, gy, W, H], fill=gcol + (255,))
        for _ in range(500):
            y = gy + (H - gy) * r2.random() ** 1.3; s_ = 0.4 + (y - gy) / (H - gy) * 1.4; x = r2.uniform(0, W)
            d.ellipse([x - 12 * s_, y - 5 * s_, x + 12 * s_, y + 5 * s_], fill=mix(gcol, p["moon"] if r2.random() < 0.5 else (0, 0, 0), 0.09) + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        wx, wb = W * 0.56, H - 40; wl = mix(nc, st, 0.18)                                     # the well-head
        dn.rectangle([wx - 170, wb - 150, wx + 170, wb], fill=wl + (255,)); dn.ellipse([wx - 170, wb - 30, wx + 170, wb + 30], fill=wl + (255,))
        dn.ellipse([wx - 170, wb - 180, wx + 170, wb - 120], fill=mix(wl, p["moon"], 0.1) + (255,)); dn.ellipse([wx - 140, wb - 172, wx + 140, wb - 128], fill=(4, 4, 6, 255))
        for k in range(5): dn.line([(wx - 170, wb - 120 + k * 26), (wx + 170, wb - 120 + k * 26)], fill=mix(wl, (0, 0, 0), 0.3) + (255,), width=2)
        for sx in (-1, 1): dn.rectangle([wx + sx * 150 - 10, wb - 430, wx + sx * 150 + 10, wb - 150], fill=nc + (255,))
        dn.polygon([(wx - 220, wb - 420), (wx + 220, wb - 420), (wx, wb - 520)], fill=nc + (255,))
        dn.rectangle([wx - 150, wb - 330, wx + 150, wb - 306], fill=mix(nc, (60, 44, 30), 0.3) + (255,))   # windlass roller
        dn.line([(wx + 160, wb - 318), (wx + 200, wb - 318), (wx + 200, wb - 270)], fill=nc + (255,), width=6)
        dn.line([(wx - 20, wb - 306), (wx - 20, wb - 230)], fill=mix(nc, (90, 80, 60), 0.3) + (255,), width=2)
        dn.polygon([(wx - 44, wb - 230), (wx + 4, wb - 230), (wx - 2, wb - 188), (wx - 38, wb - 188)], fill=mix(nc, (70, 50, 30), 0.3) + (255,))   # bucket
        cx = wx + 90; cy = wb - 178                                                           # the cat on the rim
        dn.ellipse([cx - 22, cy - 40, cx + 22, cy + 4], fill=nc + (255,)); dn.ellipse([cx - 13, cy - 62, cx + 13, cy - 36], fill=nc + (255,))
        dn.polygon([(cx - 12, cy - 56), (cx - 9, cy - 72), (cx - 3, cy - 60)], fill=nc + (255,)); dn.polygon([(cx + 12, cy - 56), (cx + 9, cy - 72), (cx + 3, cy - 60)], fill=nc + (255,))
        dn.line([(cx + 18, cy), (cx + 40, cy + 10), (cx + 46, cy + 40)], fill=nc + (255,), width=6, joint="curve")
        self.near = near
        self.walker = dict(y=gy + 70, s=1.0)
        self.fog_y = gy; self.fog_a = 0.07; self.particles = "thistledown"

    def build_hall(self):
        """The great hall looking up towards the dais: arch-braced oak trusses receding into smoke-haze, tall windows with
        moonlight, the central hearth with live flames and smoke rising to the louvre, the high table and a painted hunting
        cloth on the end wall, trestle boards stacked against the wall, sleepers on pallets, a hound by the fire."""
        p, rng = self.p, self.rng; vx, vy, f = W * 0.5, H * 0.46, 560; st = p["stone"]
        P = lambda X, Y, z: (vx + X * f / z, vy + Y * f / z); q = lambda pts: [P(*a) for a in pts]
        wall = mix(p["mid"], st, 0.2); wood = mix(p["mid"], (78, 52, 32), 0.5); hz = 1.9
        img = Image.new("RGBA", (W, H), mix(p["near"], p["mid"], 0.5) + (255,)); d = ImageDraw.Draw(img)
        zn, zf = 0.55, 3.6
        d.polygon(q([(-1, -0.6, zn), (0, -1.75, zn), (0, -1.75, zf), (-1, -0.6, zf)]), fill=mix(p["near"], wood, 0.3) + (255,))
        d.polygon(q([(1, -0.6, zn), (0, -1.75, zn), (0, -1.75, zf), (1, -0.6, zf)]), fill=mix(p["near"], wood, 0.22) + (255,))
        d.polygon(q([(-1, -0.6, zn), (-1, -0.6, zf), (-1, 0.9, zf), (-1, 0.9, zn)]), fill=wall + (255,))
        d.polygon(q([(1, -0.6, zn), (1, -0.6, zf), (1, 0.9, zf), (1, 0.9, zn)]), fill=mix(wall, (0, 0, 0), 0.14) + (255,))
        fl = mix(p["mid"], (120, 110, 70), 0.24)
        d.polygon(q([(-1, 0.9, zn), (1, 0.9, zn), (1, 0.9, zf), (-1, 0.9, zf)]), fill=fl + (255,))
        for _ in range(900):                                                                  # rushes strewn on the floor
            z = rng.uniform(0.62, zf); X = rng.uniform(-1, 1); x, y = P(X, 0.9, z); L = 22 / z
            a = rng.uniform(0, TAU); d.line([(x, y), (x + L * math.cos(a), y + L * 0.3 * math.sin(a))], fill=mix(fl, (150, 150, 90), rng.uniform(0.1, 0.3)) + (255,), width=1)
        ew = mix(wall, (0, 0, 0), 0.06)
        d.polygon(q([(-1, -0.6, zf), (0, -1.75, zf), (1, -0.6, zf), (1, 0.9, zf), (-1, 0.9, zf)]), fill=ew + (255,))
        x0, y0 = P(-0.72, -0.5, zf); x1, y1 = P(0.72, 0.36, zf); cl = mix(p["mid"], (60, 90, 56), 0.45)   # painted hunting cloth
        d.rectangle([x0, y0, x1, y1], fill=cl + (255,)); d.rectangle([x0, y0, x1, y0 + 6], fill=mix(cl, (150, 60, 40), 0.4) + (255,))
        r2 = random.Random(int(rng.integers(1e6)))
        for k in range(9):
            tx = x0 + 10 + k * (x1 - x0 - 20) / 8; d.ellipse([tx - 14, y0 + 16 + r2.uniform(0, 14), tx + 14, y0 + 60], fill=mix(cl, (20, 40, 20), 0.4) + (255,))
            d.line([(tx, y0 + 50), (tx, y1 - 10)], fill=mix(cl, (40, 30, 20), 0.5) + (255,), width=3)
        hx, hy_ = (x0 + x1) / 2 + 20, y1 - 30; hc = mix(p["washi"] if "washi" in p else (230, 222, 200), p["mid"], 0.25)   # the white hart
        d.ellipse([hx - 20, hy_ - 10, hx + 18, hy_ + 6], fill=hc + (255,)); d.line([(hx + 14, hy_ - 4), (hx + 24, hy_ - 18)], fill=hc + (255,), width=5)
        d.ellipse([hx + 20, hy_ - 24, hx + 30, hy_ - 14], fill=hc + (255,))
        for lx in (hx - 16, hx - 8, hx + 8, hx + 14): d.line([(lx, hy_ + 2), (lx + 2, hy_ + 18)], fill=hc + (255,), width=2)
        d.line([(hx + 26, hy_ - 24), (hx + 20, hy_ - 36), (hx + 14, hy_ - 40)], fill=hc + (255,), width=2); d.line([(hx + 26, hy_ - 24), (hx + 34, hy_ - 38)], fill=hc + (255,), width=2)
        for k, gx in enumerate((x0 + 40, x0 + 76)):                                          # hounds chasing
            gc = mix(cl, (20, 18, 16), 0.6); gy_ = y1 - 22; d.ellipse([gx - 16, gy_ - 6, gx + 16, gy_ + 4], fill=gc + (255,)); d.ellipse([gx + 12, gy_ - 12, gx + 22, gy_ - 2], fill=gc + (255,))
        moonwin = mix(p["sea"], (120, 140, 200), 0.32)
        for z in (0.95, 1.55, 2.25, 2.95):                                                    # tall windows, moonlit on the left
            for sx, col in ((-1, moonwin), (1, mix(p["sea"], p["mid"], 0.4))):
                pts = q([(sx, 0.2, z), (sx, 0.2, z + 0.2), (sx, -0.32, z + 0.2), (sx, -0.46, z + 0.1), (sx, -0.32, z)])
                d.polygon(pts, fill=col + (255,))
                a, b = P(sx, -0.42, z + 0.1), P(sx, 0.2, z + 0.1); d.line([a, b], fill=mix(wall, (0, 0, 0), 0.3) + (255,), width=max(2, int(8 / z)))
        dz = 3.15; dc = mix(fl, (90, 70, 50), 0.3)                                            # the dais and high table
        d.polygon(q([(-1, 0.8, dz), (1, 0.8, dz), (1, 0.8, zf), (-1, 0.8, zf)]), fill=mix(dc, p["light"], 0.08) + (255,))
        d.polygon(q([(-1, 0.8, dz), (1, 0.8, dz), (1, 0.9, dz), (-1, 0.9, dz)]), fill=mix(dc, (0, 0, 0), 0.35) + (255,))
        cx_, cy_ = P(0, 0.12, 3.5); d.rectangle([cx_ - 22, cy_ - 30, cx_ + 22, P(0, 0.62, 3.5)[1]], fill=mix(wood, (0, 0, 0), 0.25) + (255,))   # the lord's chair
        d.pieslice([cx_ - 22, cy_ - 52, cx_ + 22, cy_ - 8], 180, 360, fill=mix(wood, (0, 0, 0), 0.25) + (255,))
        a, b = P(-0.62, 0.5, 3.35), P(0.62, 0.68, 3.35)
        d.rectangle([a[0], a[1], b[0], b[1]], fill=mix((214, 204, 184), p["mid"], 0.35) + (255,)); d.rectangle([a[0], a[1], b[0], a[1] + 4], fill=mix((214, 204, 184), p["mid"], 0.15) + (255,))
        for z in (0.75, 1.1, 1.5, 1.9, 2.3, 2.7, 3.1, 3.5)[::-1]:                              # arch-braced trusses
            c = mix(mix(wood, p["light"], 0.3 * math.exp(-abs(z - hz) * 1.2)), p["near"], min(0.6, z * 0.12)) + (255,)
            d.line(q([(-1, -0.6, z), (0, -1.75, z), (1, -0.6, z)]), fill=c, width=max(2, int(34 / z)), joint="curve")
            d.line(q([(-0.36, -1.3, z), (0.36, -1.3, z)]), fill=c, width=max(2, int(20 / z)))
            for sx in (-1, 1):
                d.line(q([(sx, -0.62, z), (sx, -0.05, z)]), fill=c, width=max(2, int(26 / z)))
                pts = [(sx * ((1 - u) ** 2 * 1 + 2 * (1 - u) * u * 0.95 + u * u * 0.34), (1 - u) ** 2 * -0.08 + 2 * (1 - u) * u * -1.2 + u * u * -1.3, z) for u in np.linspace(0, 1, 12)]
                d.line(q(pts), fill=c, width=max(2, int(18 / z)), joint="curve")
        for X, Y in ((-0.5, -1.17), (0.5, -1.17), (-0.76, -0.88), (0.76, -0.88)):
            d.line(q([(X, Y, zn), (X, Y, zf)]), fill=mix(wood, p["near"], 0.4) + (255,), width=4)
        hs = mix(fl, st, 0.4)                                                                 # the central hearth
        d.polygon(q([(-0.36, 0.9, hz - 0.22), (0.36, 0.9, hz - 0.22), (0.36, 0.9, hz + 0.22), (-0.36, 0.9, hz + 0.22)]), fill=hs + (255,))
        fx, fy = P(0, 0.9, hz); self.fires.append((fx, fy, 0.5)); self.smoke = (fx, fy - 80, 400)
        arr = np.asarray(img).astype(np.float32); arr[..., :3] += radial_glow(fx, fy - 50, 760, p["light"], 0.16)
        self.back = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA")
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dm = ImageDraw.Draw(mid)
        bd = mix(wood, (0, 0, 0), 0.2)
        for k, z in enumerate((1.05, 1.13, 1.21)):                                            # trestle boards against the right wall
            dm.polygon(q([(0.88 - k * 0.02, 0.9, z), (0.88 - k * 0.02, 0.9, z + 0.6), (0.99, -0.05, z + 0.6), (0.99, -0.05, z)]), fill=mix(bd, p["light"], 0.08 * k) + (255,))
        bl = mix(p["mid"], (86, 64, 52), 0.35)
        def bbox(X0, X1, Y0, Y1, z0, z1):
            pts = [P(X, Y, z) for X in (X0, X1) for Y in (Y0, Y1) for z in (z0, z1)]
            return [min(a for a, b in pts), min(b for a, b in pts), max(a for a, b in pts), max(b for a, b in pts)]
        for X0, z in ((-0.95, 1.2), (-0.95, 1.75), (-0.92, 2.2), (0.62, 1.2), (0.55, 2.55)):   # sleepers on straw pallets
            dm.polygon(q([(X0, 0.9, z), (X0 + 0.32, 0.9, z), (X0 + 0.32, 0.9, z + 0.5), (X0, 0.9, z + 0.5)]), fill=mix(bl, (150, 130, 80), 0.25) + (255,))
            dm.ellipse(bbox(X0 + 0.04, X0 + 0.28, 0.8, 0.9, z + 0.12, z + 0.46), fill=bl + (255,))
            dm.ellipse(bbox(X0 + 0.1, X0 + 0.22, 0.8, 0.88, z + 0.02, z + 0.1), fill=mix(bl, (0, 0, 0), 0.35) + (255,))
        gx, gy = P(0.5, 0.9, 1.75); g = mix(p["mid"], (120, 116, 110), 0.3)                    # the hound by the fire
        dm.ellipse([gx - 70, gy - 34, gx + 60, gy + 4], fill=g + (255,)); dm.ellipse([gx - 96, gy - 30, gx - 52, gy], fill=g + (255,))
        dm.polygon([(gx - 92, gy - 26), (gx - 78, gy - 40), (gx - 70, gy - 22)], fill=mix(g, (0, 0, 0), 0.3) + (255,))
        dm.line([(gx + 58, gy - 10), (gx + 100, gy - 2), (gx + 120, gy - 8)], fill=g + (255,), width=6, joint="curve")
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.polygon([(0, H - 150), (W * 0.36, H - 120), (W * 0.36, H - 96), (0, H - 120)], fill=nc + (255,))   # a bench in the foreground
        for x in (40, W * 0.33): dn.rectangle([x, H - 120, x + 18, H], fill=nc + (255,))
        self.near = near
        self.fog_a = 0.0; self.particles = "embers"

    def build_wallwalk(self):
        """On the wall walk: battlements receding to a round tower, a brazier glowing, the countryside under the moon
        with the river, a village and its church tower, a windmill, and the watchman pacing away and back."""
        p, rng = self.p, self.rng; vx, vy, f = W * 0.6, H * 0.42, 520; st = p["stone"]
        P = lambda X, Y, z: (vx + X * f / z, vy + Y * f / z); q = lambda pts: [P(*a) for a in pts]
        r2 = random.Random(int(rng.integers(1e6)))
        self.back = self.sky(int(vy), (0.24, 0.15), 40)
        self.back.alpha_composite(hills(int(vy) - 6, 22, int(rng.integers(1e6)), mix(p["far"], p["horizon"], 0.25), blur=2))
        land = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(land); gc = mix(p["mid"], (56, 70, 56), 0.2)
        dl.rectangle([0, vy + 4, W, H], fill=gc + (255,))
        for k in range(16):                                                                   # field strips
            x = -800 + k * 220; dl.line([(vx - 400, vy + 6), (x, H)], fill=mix(gc, p["moon"], 0.05 + 0.04 * (k % 2)) + (255,), width=2)
        dl.polygon([(0, vy + 10), (W * 0.5, vy + 6), (W * 0.5, vy + 26), (0, vy + 40)], fill=mix(gc, (0, 0, 0), 0.4) + (255,))   # woods on the hill
        rv = [(-20, vy + 330), (W * 0.1, vy + 250), (W * 0.2, vy + 150), (W * 0.32, vy + 90), (W * 0.44, vy + 40), (W * 0.52, vy + 16)]
        for k in range(len(rv) - 1):
            dl.line([rv[k], rv[k + 1]], fill=mix(p["sea"], p["moon"], 0.35) + (255,), width=int(60 - k * 11))
        vxl, vyl = W * 0.3, vy + 46; hc = mix(gc, (0, 0, 0), 0.45)                          # the village
        for k in range(9):
            x = vxl - 160 + k * 38 + r2.uniform(-8, 8); y = vyl + r2.uniform(-6, 10); s = 0.8 + r2.random() * 0.4
            dl.rectangle([x, y - 16 * s, x + 30 * s, y], fill=hc + (255,)); dl.polygon([(x - 4, y - 16 * s), (x + 34 * s, y - 16 * s), (x + 15 * s, y - 34 * s)], fill=mix(hc, (0, 0, 0), 0.3) + (255,))
        cx = vxl + 40; dl.rectangle([cx, vyl - 96, cx + 26, vyl], fill=hc + (255,)); self._crenels(dl, cx - 2, cx + 28, vyl - 96, 6, 6, 4, hc)
        dl.rectangle([cx + 26, vyl - 40, cx + 90, vyl], fill=hc + (255,)); dl.polygon([(cx + 24, vyl - 40), (cx + 92, vyl - 40), (cx + 58, vyl - 60)], fill=hc + (255,))
        self.windows.append((vxl - 70, vyl - 8, 5, 6, 0.9, 1))
        mx_, my_ = W * 0.06, vy + 40                                                          # windmill
        dl.polygon([(mx_ - 14, my_), (mx_ + 14, my_), (mx_ + 9, my_ - 40), (mx_ - 9, my_ - 40)], fill=hc + (255,))
        for a in (0.6, 0.6 + math.pi / 2, 0.6 + math.pi, 0.6 + 1.5 * math.pi): dl.line([(mx_, my_ - 38), (mx_ + 46 * math.cos(a), my_ - 38 + 46 * math.sin(a))], fill=hc + (255,), width=4)
        self.back.alpha_composite(land)
        kc = mix(p["mid"], st, 0.22); kx = W * 0.92                                           # the keep on the right
        self.back.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)))
        db = ImageDraw.Draw(self.back)
        db.rectangle([kx - 150, H * 0.06, W + 40, H], fill=kc + (255,)); self._crenels(db, kx - 150, W + 40, H * 0.06, 30, 32, 22, kc)
        self.windows.append((kx - 60, H * 0.22, 14, 34, 2.1, 1))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        zn, zf = 0.42, 7.0; wk = mix(p["mid"], st, 0.3)
        tcx, tt, tb = P(0.1, 0, zf)[0], P(0, -2.6, zf)[1], P(0, 1, zf)[1]                     # round tower at the end of the walk
        self._rtower(d, tcx, tt, tb, 3.4 * f / zf, mix(p["mid"], st, 0.36), 2, 0.6)
        da, db_ = P(-0.18, -0.15, zf), P(0.38, 1, zf)
        d.rectangle([da[0], da[1], db_[0], db_[1]], fill=mix(p["light"], p["mid"], 0.55) + (255,))
        d.pieslice([da[0], da[1] - (db_[0] - da[0]) / 2, db_[0], da[1] + (db_[0] - da[0]) / 2], 180, 360, fill=mix(p["light"], p["mid"], 0.55) + (255,))
        d.polygon(q([(-1, 1, zn), (1.2, 1, zn), (1.2, 1, zf), (-1, 1, zf)]), fill=wk + (255,))   # walk
        z = zn
        while z < zf: d.line(q([(-1, 1, z), (1.2, 1, z)]), fill=mix(wk, (0, 0, 0), 0.3) + (255,), width=max(1, int(4 / z))); z += 0.3
        d.line(q([(0.1, 1, zn), (0.1, 1, zf)]), fill=mix(wk, (0, 0, 0), 0.2) + (255,), width=2)
        d.polygon(q([(1.2, 1, zn), (1.2, 1, zf), (1.2, 0.58, zf), (1.2, 0.58, zn)]), fill=mix(wk, (0, 0, 0), 0.2) + (255,))   # low inner parapet
        d.polygon(q([(1.2, 0.58, zn), (1.2, 0.58, zf), (1.4, 0.58, zf), (1.4, 0.58, zn)]), fill=mix(wk, p["moon"], 0.12) + (255,))
        pc = mix(p["mid"], st, 0.22); sill = 0.52
        d.polygon(q([(-1, 1, zn), (-1, 1, zf), (-1, sill, zf), (-1, sill, zn)]), fill=pc + (255,))   # outer parapet
        d.polygon(q([(-1, sill, zn), (-1, sill, zf), (-1.3, sill, zf), (-1.3, sill, zn)]), fill=mix(pc, p["moon"], 0.2) + (255,))
        segs = []; z = zn + 0.75
        while z < zf: segs.append(z); z += 0.62 * (1 + 0.15 * z)
        for z in segs[::-1]:
            z1 = min(zf, z + 0.2)
            d.polygon(q([(-1.3, sill, z), (-1, sill, z), (-1, -0.16, z), (-1.3, -0.16, z)]), fill=mix(pc, (0, 0, 0), 0.4) + (255,))
            d.polygon(q([(-1, sill, z), (-1, sill, z1), (-1, -0.16, z1), (-1, -0.16, z)]), fill=mix(pc, p["moon"], 0.06) + (255,))
        bx, by = P(0.85, 1, 1.5); s = f / 1.5 / 520                                           # brazier
        for sx in (-1, 1): d.line([(bx + sx * 26 * s, by), (bx + sx * 12 * s, by - 60 * s)], fill=(16, 14, 14, 255), width=4)
        d.chord([bx - 34 * s, by - 90 * s, bx + 34 * s, by - 50 * s], 0, 180, fill=(20, 16, 16, 255))
        self.fires.append((bx, by - 70 * s, 0.22))
        self.mid = mid
        self.near = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        self.sentry = dict(v=(vx, vy, f), X=0.12)
        self.fog_y = vy + 60; self.fog_a = 0.14; self.particles = "thistledown"

    def build_solar(self):
        """The lady's chamber: painted plaster with little flowers, a deep window embrasure with stone benches and a
        moonlit two-light window, a hanging cloth with an enclosed garden, a candle in a wall niche, the great curtained
        bed with tester and fur coverlet, a truckle bed, a hooded fireplace, a chest and a little dog on a cushion."""
        p, rng = self.p, self.rng; r2 = random.Random(int(rng.integers(1e6))); st = p["stone"]
        wall = mix(p["mid"], (132, 58, 50), 0.36); fy = int(H * 0.74)
        self.back = Image.new("RGBA", (W, H), wall + (255,)); d = ImageDraw.Draw(self.back)
        fc = mix(wall, (232, 220, 200), 0.2)
        for yy in range(90, fy, 64):
            for xx in range(20 + (yy // 64 % 2) * 32, W, 64):
                for k in range(5): a = k * TAU / 5; d.ellipse([xx + 6 * math.cos(a) - 2, yy + 6 * math.sin(a) - 2, xx + 6 * math.cos(a) + 2, yy + 6 * math.sin(a) + 2], fill=fc + (255,))
        bw = mix(p["mid"], (60, 42, 28), 0.4); d.rectangle([0, 0, W, 64], fill=mix(bw, (0, 0, 0), 0.3) + (255,))
        for k in range(14): d.rectangle([k * 150, 50, k * 150 + 40, 76], fill=bw + (255,))
        ex0, ex1, et = W * 0.03, W * 0.25, H * 0.2; sc = mix(p["mid"], st, 0.3)              # window embrasure
        d.rectangle([ex0, et, ex1, fy - 20], fill=sc + (255,)); d.pieslice([ex0, et - (ex1 - ex0) / 2, ex1, et + (ex1 - ex0) / 2], 180, 360, fill=sc + (255,))
        ix0, ix1, it = ex0 + 90, ex1 - 90, et + 40
        d.rectangle([ex0 + 40, et + 10, ex1 - 40, fy - 20], fill=mix(sc, (0, 0, 0), 0.25) + (255,))
        sky = mix(p["sky_mid"], p["moon"], 0.28); lw = (ix1 - ix0 - 16) / 2
        for k in range(2):
            a = ix0 + k * (lw + 16); d.rectangle([a, it + 40, a + lw, fy - 170], fill=sky + (255,))
            d.polygon([(a, it + 40), (a + lw / 2, it - 10), (a + lw, it + 40)], fill=sky + (255,))
        d.ellipse([(ix0 + ix1) / 2 - 14, it - 44, (ix0 + ix1) / 2 + 14, it - 16], fill=sky + (255,))
        d.rectangle([ix0, it + 120, ix0 + lw, fy - 170], fill=mix(p["mid"], (70, 50, 32), 0.4) + (255,))   # left light shuttered below
        for k in range(1, 4): d.line([(ix0 + lw + 16, it + 40 + k * 60), (ix1, it + 40 + k * 60)], fill=mix(sc, (0, 0, 0), 0.4) + (255,), width=2)
        for sx, x in ((1, ex0 + 40), (-1, ex1 - 40)):                                         # stone window benches
            d.polygon([(x, fy - 20), (x + sx * 70, fy - 20), (x + sx * 70, fy - 110), (x, fy - 130)], fill=mix(sc, p["moon"], 0.1) + (255,))
        self.hanging = (W * 0.275, H * 0.14, W * 0.125, H * 0.4)
        d.rectangle([W * 0.27, H * 0.13, W * 0.405, H * 0.14], fill=bw + (255,))
        nx, ny = W * 0.335, H * 0.63                                                          # candle niche
        d.rectangle([nx - 34, ny - 50, nx + 34, ny + 40], fill=mix(wall, (0, 0, 0), 0.45) + (255,)); d.pieslice([nx - 34, ny - 84, nx + 34, ny - 16], 180, 360, fill=mix(wall, (0, 0, 0), 0.45) + (255,))
        d.rectangle([nx - 6, ny - 6, nx + 6, ny + 38], fill=(232, 214, 170, 255)); self.lamp = (nx, ny - 10); self.lamp_r = 280
        hx0, hx1 = W * 0.86, W * 1.0; hcol = mix(p["mid"], st, 0.22)                          # hooded fireplace
        d.polygon([(hx0 - 10, fy - 170), (W + 20, fy - 170), (W - 20, H * 0.26), (hx0 + 50, H * 0.26)], fill=hcol + (255,))
        d.rectangle([hx0 + 50, 60, W - 20, H * 0.26], fill=hcol + (255,))
        d.rectangle([hx0 + 10, fy - 170, W, fy + 10], fill=(12, 8, 8, 255)); d.rectangle([hx0 - 10, fy - 182, W + 20, fy - 166], fill=mix(hcol, p["moon"], 0.1) + (255,))
        self.fires.append((hx0 + 120, fy, 0.3))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dm = ImageDraw.Draw(mid)
        fl = mix(p["mid"], (110, 86, 58), 0.3); dm.rectangle([0, fy, W, H], fill=fl + (255,))
        for k in range(9): y = fy + (H - fy) * (k / 9) ** 1.3; dm.line([(0, y), (W, y)], fill=mix(fl, (0, 0, 0), 0.3) + (255,), width=2)
        mt = mix(fl, (170, 150, 90), 0.25); dm.polygon([(W * 0.3, fy + 40), (W * 0.86, fy + 40), (W * 0.92, H - 30), (W * 0.24, H - 30)], fill=mt + (255,))
        for k in range(40): x = W * 0.27 + k * (W * 0.62) / 40; dm.line([(x + 30, fy + 40), (x, H - 30)], fill=mix(mt, (0, 0, 0), 0.15) + (255,), width=1)
        mb = Image.new("RGBA", (W, H), (0, 0, 0, 0))                                          # bar of moonlight across the floor
        ImageDraw.Draw(mb).polygon([(ix0 + lw + 16, fy - 20), (ix1, fy - 20), (W * 0.56, H), (W * 0.36, H)], fill=(170, 190, 240, 46))
        mid.alpha_composite(mb.filter(ImageFilter.GaussianBlur(18)))
        b0, b1 = W * 0.43, W * 0.83; cur = mix(p["mid"], p["banner"], 0.55); tt = H * 0.1      # the great bed
        dm.rectangle([b0, tt + 70, b1, fy - 150], fill=mix(cur, (0, 0, 0), 0.25) + (255,))     # back curtain
        for k in range(26): x = b0 + k * (b1 - b0) / 26; dm.line([(x, tt + 70), (x, fy - 150)], fill=mix(cur, (0, 0, 0), 0.4) + (255,), width=3)
        vine = mix(cur, (190, 170, 110), 0.35)
        for k in range(30):
            x = b0 + 10 + k * (b1 - b0 - 20) / 30; dm.ellipse([x - 5, tt + 88 + 8 * math.sin(k), x + 5, tt + 98 + 8 * math.sin(k)], fill=vine + (255,))
        for x in (b0, b1): dm.rectangle([x - 12, tt, x + 12, fy + 50], fill=mix(bw, (0, 0, 0), 0.2) + (255,))
        dm.rectangle([b0 - 30, tt, b1 + 30, tt + 70], fill=cur + (255,))                     # tester and valance
        for k in range(18): x = b0 - 30 + k * (b1 - b0 + 60) / 18; dm.pieslice([x, tt + 50, x + (b1 - b0 + 60) / 18, tt + 90], 0, 180, fill=cur + (255,))
        dm.rectangle([b0 - 30, tt + 6, b1 + 30, tt + 14], fill=vine + (255,))
        dm.rectangle([b0 + 14, fy - 160, b1 - 14, fy - 30], fill=mix((214, 206, 190), p["mid"], 0.4) + (255,))   # mattress and sheet
        dm.rounded_rectangle([b1 - 170, fy - 200, b1 - 20, fy - 140], radius=26, fill=mix((230, 222, 206), p["mid"], 0.3) + (255,))   # bolster
        fur = mix(p["mid"], (150, 146, 140), 0.45)
        dm.polygon([(b0 + 10, fy - 170), (b1 - 180, fy - 176), (b1 - 160, fy - 20), (b0 + 6, fy - 10)], fill=fur + (255,))
        for k in range(160): x = r2.uniform(b0 + 10, b1 - 170); y = r2.uniform(fy - 170, fy - 14); dm.line([(x, y), (x + 3, y + 8)], fill=mix(fur, (240, 240, 240), 0.15) + (255,), width=1)
        for x0_, w_ in ((b0 + 12, 70), (b1 - 82, 70)):                                       # gathered side curtains
            for k in range(7): dm.line([(x0_ + k * 10, tt + 70), (x0_ + k * 10 + (5 if k % 2 else -5), fy + 30)], fill=mix(cur, (0, 0, 0), 0.1 + 0.25 * (k % 2)) + (255,), width=10)
        dm.rectangle([b0 + 120, fy - 30, b1 - 120, fy + 30], fill=mix(bw, (0, 0, 0), 0.35) + (255,))   # truckle bed underneath
        dm.rectangle([b0 + 130, fy - 30, b1 - 130, fy - 14], fill=mix((210, 200, 180), p["mid"], 0.5) + (255,))
        cx_, cy_ = W * 0.84, fy + 110                                                         # little dog asleep on a cushion
        dm.ellipse([cx_ - 90, cy_ - 30, cx_ + 90, cy_ + 30], fill=mix(p["mid"], (150, 40, 40), 0.45) + (255,))
        dg = mix((236, 232, 222), p["mid"], 0.3); dm.ellipse([cx_ - 52, cy_ - 50, cx_ + 52, cy_ + 6], fill=dg + (255,))
        dm.ellipse([cx_ + 10, cy_ - 46, cx_ + 52, cy_ - 12], fill=mix(dg, (0, 0, 0), 0.06) + (255,)); dm.polygon([(cx_ + 18, cy_ - 42), (cx_ + 30, cy_ - 60), (cx_ + 36, cy_ - 40)], fill=mix(dg, (0, 0, 0), 0.15) + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        ch = mix(nc, (70, 50, 32), 0.35)                                                      # carved chest at the foot of the bed
        dn.rectangle([W * 0.3, H - 230, W * 0.47, H - 40], fill=ch + (255,)); dn.rectangle([W * 0.295, H - 244, W * 0.475, H - 222], fill=mix(ch, (0, 0, 0), 0.2) + (255,))
        for k in range(4): x = W * 0.31 + k * (W * 0.15) / 4; dn.rectangle([x + 8, H - 205, x + (W * 0.15) / 4 - 8, H - 70], outline=mix(ch, (0, 0, 0), 0.35) + (255,), width=3)
        for k in range(4): x = W * 0.31 + k * (W * 0.15) / 4 + (W * 0.15) / 8; dn.arc([x - 18, H - 180, x + 18, H - 110], 200, 340, fill=mix(ch, (200, 180, 120), 0.2) + (255,), width=3)
        self.near = near
        self.fog_a = 0.0; self.particles = "dust"

    def _banners(self, img, ph):
        """EP10: long pennants unrolling and folding in the evening breeze, each with its own rhythm."""
        p = self.p; d = ImageDraw.Draw(img); col = mix(p["banner"], p["mid"], 0.2); st = mix(p["accent"], p["mid"], 0.3)
        for x, y, L, f in self.banners:
            top, bot = [], []
            for j in range(15):
                u = j / 14; wv = math.sin(ph * 2 + f - u * 5) * 9 * u + 3 * math.sin(ph * 5 + f - u * 7) * u
                xx = x + u * L * (0.9 + 0.08 * math.cos(ph * 2 + f)); hh = 34 * (1 - 0.55 * u)
                top.append((xx, y + wv)); bot.append((xx, y + hh + wv * 1.15))
            d.polygon(top + bot[::-1], fill=col + (255,))
            d.line([((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in zip(top, bot)], fill=st + (255,), width=3)

    def _oven(self, img, ph):
        """EP10: the bakehouse oven mouth breathing its red glow; the horse in the stable nodding slowly."""
        x, y, R = self.oven; p = self.p; fl = 0.78 + 0.14 * math.sin(ph * 3) + 0.08 * math.sin(ph * 7 + 1)
        d = ImageDraw.Draw(img)
        d.chord([x - 38, y - 40, x + 38, y + 34], 180, 360, fill=mix(p["ember"], (255, 220, 150), 0.25 * fl) + (255,)); d.rectangle([x - 38, y - 4, x + 38, y + 10], fill=mix(p["ember"], (90, 30, 10), 0.4) + (255,))
        img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R)), p["ember"], 0.55 * fl), (int(x - R), int(y - R // 2)))
        hx, hy_ = self.horse; nod = 6 * math.sin(ph * 2) + 2 * math.sin(ph * 5); c = mix(self.p["near"], (60, 44, 34), 0.25) + (255,)
        d.polygon([(hx - 40, hy_ - 78), (hx - 6, hy_ - 72), (hx + 4, hy_ - 58 + nod * 0.5), (hx - 22, hy_ - 2), (hx - 44, hy_ - 2)], fill=c)   # neck over the half-door
        d.polygon([(hx - 8, hy_ - 66 + nod * 0.5), (hx + 6, hy_ - 64 + nod * 0.5), (hx + 58, hy_ - 4 + nod), (hx + 52, hy_ + 14 + nod), (hx + 30, hy_ + 16 + nod), (hx - 10, hy_ - 30 + nod * 0.6)], fill=c)
        d.polygon([(hx - 6, hy_ - 64 + nod * 0.5), (hx - 2, hy_ - 86 + nod * 0.5), (hx + 6, hy_ - 62 + nod * 0.5)], fill=c)
        d.line([(hx - 40, hy_ - 78), (hx - 12, hy_ - 70)], fill=mix(self.p["near"], self.p["moon"], 0.2) + (255,), width=3)   # mane edge in moonlight

    def _walker(self, img, t, ph):
        """EP10: the watchman crossing the courtyard once per loop, cloak and hood, staff, lantern swinging."""
        Wk = self.walker; u = t / LOOP_S; s = Wk["s"]; x = -420 + (W + 840) * u; y = Wk["y"] - 3 * abs(math.sin(ph * 14))
        self._figure(img, x, y, 230 * s, ph * 14, 1)

    def _figure(self, img, x, y, h, step, side):
        p = self.p; c = (14, 13, 18, 255); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        sw = math.sin(step) * 0.04 * h
        d.polygon([(x - 0.16 * h, y), (x + 0.16 * h, y), (x + 0.09 * h, y - 0.8 * h), (x - 0.09 * h, y - 0.8 * h)], fill=c)
        d.line([(x - 0.06 * h + sw, y), (x - 0.06 * h + sw, y + 0.02 * h)], fill=c, width=max(2, int(h / 40)))
        d.ellipse([x - 0.08 * h, y - 0.97 * h, x + 0.08 * h, y - 0.78 * h], fill=c)
        d.polygon([(x - 0.08 * h, y - 0.86 * h), (x + 0.02 * h, y - 1.02 * h), (x + 0.1 * h, y - 0.84 * h)], fill=c)
        d.line([(x + side * 0.2 * h, y + 0.01 * h), (x + side * 0.23 * h, y - 1.15 * h)], fill=c, width=max(2, int(h / 45)))
        hx, hy_ = x - side * 0.15 * h, y - 0.46 * h; a = 0.18 * math.sin(step * 0.5)
        lx, ly = hx + 0.12 * h * math.sin(a), hy_ + 0.12 * h * math.cos(a)
        d.line([(hx, hy_), (lx, ly - 0.03 * h)], fill=c, width=max(1, int(h / 90)))
        img.alpha_composite(lay)
        R = int(h * 0.9); img.alpha_composite(self.tint(self.glow_lg.resize((R * 2, R * 2)), p["light"], 0.36), (int(lx - R), int(ly - R)))
        d = ImageDraw.Draw(img); d.rectangle([lx - 0.03 * h, ly - 0.03 * h, lx + 0.03 * h, ly + 0.05 * h], fill=(255, 206, 128, 255))
        d.rectangle([lx - 0.035 * h, ly - 0.045 * h, lx + 0.035 * h, ly - 0.03 * h], fill=c)

    def _sentry(self, img, t, ph):
        """EP10: the watchman walking slowly away along the wall walk towards the far tower, and back again."""
        S = self.sentry; vx, vy, f = S["v"]; u = t / LOOP_S
        z = 3.0 - 1.5 * math.cos(TAU * u); X = S["X"] + 0.04 * math.sin(TAU * u)
        fx, fy = vx + X * f / z, vy + 1.0 * f / z; h = 1.12 * f / z
        self._figure(img, fx, fy - 2 * abs(math.sin(ph * 12)) / z, h, ph * 12, -1)

    def _hanging(self, img, ph):
        """EP10: the woven cloth of an enclosed garden, swaying very slightly on its rail in the draught."""
        x0, y0, w, h = self.hanging; p = self.p; sway = 7 * math.sin(ph) + 2 * math.sin(ph * 3 + 1)
        M = lambda u, v: (x0 + u * w + sway * v ** 1.5 * (1 + 0.2 * u), y0 + v * h + 2 * math.sin(ph * 2 + u * 3) * v)
        d = ImageDraw.Draw(img); cl = mix(p["mid"], (54, 82, 60), 0.5)
        d.polygon([M(0, 0), M(1, 0), M(1, 1), M(0, 1)], fill=cl + (255,))
        bd = mix(cl, (160, 70, 50), 0.45)
        for a, b in (((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((0, 1), (0, 0))): d.line([M(*a), M(*b)], fill=bd + (255,), width=8)
        wl = mix(cl, (200, 190, 160), 0.35); d.line([M(0.08, 0.72), M(0.92, 0.72)], fill=wl + (255,), width=6)   # garden wall
        for u in (0.18, 0.5, 0.82):                                                           # fruit trees
            tx, ty = M(u, 0.42); d.line([M(u, 0.72), (tx, ty)], fill=mix(cl, (50, 36, 24), 0.6) + (255,), width=4)
            d.ellipse([tx - 26, ty - 34, tx + 26, ty + 14], fill=mix(cl, (20, 50, 26), 0.5) + (255,))
            for k in range(4): a = k * 1.7 + u * 5; d.ellipse([tx + 16 * math.cos(a) - 4, ty - 10 + 14 * math.sin(a) - 4, tx + 16 * math.cos(a) + 4, ty - 10 + 14 * math.sin(a) + 4], fill=mix(cl, p["ember"], 0.55) + (255,))
        fx, fy = M(0.5, 0.85); d.ellipse([fx - 22, fy - 8, fx + 22, fy + 8], fill=mix(cl, (150, 170, 200), 0.45) + (255,)); d.line([(fx, fy), (fx, fy - 28)], fill=mix(cl, (200, 210, 230), 0.5) + (255,), width=3)
        for u, v in ((0.3, 0.2), (0.66, 0.16), (0.4, 0.92), (0.75, 0.9)):
            bx, by = M(u, v); d.ellipse([bx - 5, by - 4, bx + 5, by + 4], fill=mix(cl, (230, 220, 200), 0.5) + (255,))

    # ------------------------------------------------------------ EP11 Victorian London in the fog
    def _fogback(self, hy, glow=(0.7, 0.2)):
        """Starless sky of a London fog: sooty brown above, thick yellow fog low down, the moon only a faint smudge."""
        p = self.p; y = np.arange(H, dtype=np.float32)[:, None]
        top, mid, fo = (np.array(p[k], np.float32) for k in ("sky_top", "sky_mid", "fog"))
        t1 = np.clip(y / (hy * 0.7), 0, 1); t2 = np.clip((y - hy * 0.45) / (hy * 0.55), 0, 1) ** 1.25
        c = top * (1 - t1) + mid * t1; c = c * (1 - t2) + fo * 0.82 * t2
        c = np.repeat(c[:, None, :], W, axis=1) + radial_glow(glow[0] * W, glow[1] * H, 260, p["moon"], 0.10)
        self.moon = (glow[0] * W, glow[1] * H, 0)
        return Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).convert("RGBA")

    def _fogtint(self, lay, a_top, a_bot, y0, y1):
        """Push a drawn layer back into the fog: blend its colours (not its alpha) towards the fog colour by height."""
        arr = np.array(lay).astype(np.float32); ys = np.arange(H, dtype=np.float32)[:, None, None]
        a = a_top + (a_bot - a_top) * np.clip((ys - y0) / max(1, y1 - y0), 0, 1)
        arr[..., :3] = arr[..., :3] * (1 - a) + np.array(self.p["fog"], np.float32) * a
        return Image.fromarray(arr.astype(np.uint8), "RGBA")

    def _mkbanks(self, specs):
        """Slow fog banks: soft horizontal textures that sway to and fro (periodic in LOOP_S) at different heights."""
        p = self.p; xs = np.arange(2 * W, dtype=np.float32)
        for yc, hh, a, amp in specs:
            n = sum(np.sin(TAU * m * xs / (2 * W) + self.rng.uniform(0, TAU)) / m ** 0.7 for m in (2, 3, 5, 7, 11, 17))
            n = np.clip(0.55 + 0.3 * n, 0, 1); y0 = int(max(0, yc - 2.2 * hh)); y1 = int(min(H, yc + 2.2 * hh))
            ys = np.arange(y0, y1, dtype=np.float32)[:, None]
            al = np.exp(-((ys - yc) / hh) ** 2) * n[None, :] * a * 255
            tex = np.zeros((y1 - y0, 2 * W, 4), np.uint8); tex[..., :3] = mix(p["fog"], p["moon"], 0.25); tex[..., 3] = al.astype(np.uint8)
            self.banks.append((Image.fromarray(tex, "RGBA"), y0, amp, self.rng.uniform(0, TAU)))

    def _gaspost(self, d, x, base, h, col, s=1.0, dolphin=False):
        """Cast-iron gas lamp post with ladder bar and a square lantern; dolphin=True gives the river-wall standard with
        two fish curled round the foot. Returns the flame point."""
        glass = mix(self.p["gas"], col, 0.3); c = col + (255,); top = base - h
        if dolphin:
            d.rectangle([x - 22 * s, base - 30 * s, x + 22 * s, base], fill=c)
            for sx in (-1, 1):                                                                # the two curled fish
                d.ellipse([x + sx * 9 * s - 9 * s, base - 112 * s, x + sx * 9 * s + 9 * s, base - 30 * s], fill=c)
                d.arc([x + sx * 22 * s - 16 * s, base - 140 * s, x + sx * 22 * s + 16 * s, base - 104 * s], 90 if sx < 0 else -90, 270 if sx < 0 else 90, fill=c, width=max(2, int(6 * s)))
                d.polygon([(x + sx * 22 * s, base - 140 * s), (x + sx * 34 * s, base - 154 * s), (x + sx * 30 * s, base - 134 * s)], fill=c)
            col0 = base - 110 * s
        else:
            d.rectangle([x - 15 * s, base - 46 * s, x + 15 * s, base], fill=c); col0 = base - 46 * s
        d.polygon([(x - 9 * s, col0), (x + 9 * s, col0), (x + 6 * s, top + 44 * s), (x - 6 * s, top + 44 * s)], fill=c)
        d.rectangle([x - 26 * s, top + 52 * s, x + 26 * s, top + 58 * s], fill=c)                   # ladder bar
        d.polygon([(x - 7 * s, top + 44 * s), (x + 7 * s, top + 44 * s), (x + 12 * s, top + 28 * s), (x - 12 * s, top + 28 * s)], fill=c)
        d.polygon([(x - 13 * s, top + 28 * s), (x + 13 * s, top + 28 * s), (x + 21 * s, top - 22 * s), (x - 21 * s, top - 22 * s)], fill=glass + (255,))
        for u in (-1, 0, 1): d.line([(x + u * 13 * s, top + 28 * s), (x + u * 21 * s, top - 22 * s)], fill=c, width=max(1, int(3 * s)))
        d.polygon([(x - 25 * s, top - 22 * s), (x + 25 * s, top - 22 * s), (x, top - 44 * s)], fill=c)
        d.ellipse([x - 4 * s, top - 54 * s, x + 4 * s, top - 42 * s], fill=c)
        return (x, top + 4 * s)

    def _halos(self, img, ph):
        """EP11: gaslight in fog - each lamp a great soft halo (cached sprite) with a small breathing bright core."""
        if not hasattr(self, "_hcache"):
            self._hcache = [(self.tint(self.glow_lg.resize((int(R * 2), int(R * 2))), self.p["gas"], 0.40 * st),
                             self.tint(self.glow_lg.resize((int(R * 0.7), int(R * 0.7))), mix(self.p["gas"], (255, 245, 220), 0.4), 0.55 * st)) for x, y, R, st in self.halos]
        for (x, y, R, st), (spr, core) in zip(self.halos, self._hcache):
            img.alpha_composite(spr, (int(x - R), int(y - R))); img.alpha_composite(core, (int(x - R * 0.35), int(y - R * 0.35)))
        d = ImageDraw.Draw(img)
        for i, (x, y, R, st) in enumerate(self.halos):
            br = 0.85 + 0.15 * math.sin(ph * 3 + i * 1.7); r = max(2.0, R * 0.035) * br
            d.ellipse([x - r, y - r * 1.3, x + r, y + r * 0.6], fill=mix(self.p["gas"], (255, 250, 230), 0.5 * st) + (int(220 * st),))

    def _man(self, img, x, y, h, step, hat="cap", pole=False, ph=0.0):
        """A walking man in a long coat (cap, top hat or police helmet); pole=True = the lamplighter's pole with its flame."""
        c = (16, 15, 15, 255); d = ImageDraw.Draw(img); sw = math.sin(step) * 0.07 * h
        d.line([(x - 0.03 * h, y - 0.36 * h), (x - 0.03 * h + sw, y)], fill=c, width=max(3, int(h / 22)))
        d.line([(x + 0.03 * h, y - 0.36 * h), (x + 0.03 * h - sw, y)], fill=c, width=max(3, int(h / 22)))
        d.polygon([(x - 0.13 * h, y - 0.3 * h), (x + 0.13 * h, y - 0.3 * h), (x + 0.09 * h, y - 0.8 * h), (x - 0.09 * h, y - 0.8 * h)], fill=c)
        d.ellipse([x - 0.065 * h, y - 0.95 * h, x + 0.065 * h, y - 0.8 * h], fill=c)
        if hat == "cap": d.rectangle([x - 0.07 * h, y - 0.96 * h, x + 0.07 * h, y - 0.91 * h], fill=c); d.rectangle([x, y - 0.93 * h, x + 0.11 * h, y - 0.91 * h], fill=c)
        elif hat == "top": d.rectangle([x - 0.055 * h, y - 1.08 * h, x + 0.055 * h, y - 0.92 * h], fill=c); d.rectangle([x - 0.09 * h, y - 0.93 * h, x + 0.09 * h, y - 0.91 * h], fill=c)
        elif hat == "helmet": d.chord([x - 0.07 * h, y - 1.1 * h, x + 0.07 * h, y - 0.86 * h], 180, 360, fill=c); d.rectangle([x - 0.07 * h, y - 0.98 * h, x + 0.07 * h, y - 0.9 * h], fill=c)
        if pole:
            hx, hy_ = x + 0.1 * h, y - 0.55 * h; bob = 0.02 * h * math.sin(step); tx, ty = x + 0.42 * h, y - 1.55 * h + bob
            d.line([(x - 0.05 * h, y - 0.42 * h), (tx, ty)], fill=c, width=max(2, int(h / 60)))
            d.line([(x + 0.08 * h, y - 0.72 * h), (hx, hy_)], fill=c, width=max(3, int(h / 26)))
            fl = 0.8 + 0.2 * math.sin(ph * 9); R = int(h * 0.35)
            img.alpha_composite(self.tint(self.glow_sm.resize((R * 2, R * 2)), self.p["gas"], 0.55 * fl), (int(tx - R), int(ty - R)))
            d = ImageDraw.Draw(img); d.ellipse([tx - 3, ty - 7 * fl, tx + 3, ty + 2], fill=(255, 232, 170, 255))

    def _lighter(self, img, t, ph):
        """EP11: the lamplighter walking along the pavement once per loop, pole on his shoulder, little flame bobbing."""
        L = self.lighter; u = t / LOOP_S; x = -300 + (W + 600) * u; y = L["y"] - 3 * abs(math.sin(ph * 13))
        self._man(img, x, y, L["h"], ph * 13, "cap", True, ph)

    def build_fogstreet(self):
        """A terrace of sooty brick houses in thick fog: sash windows (some lit, blinds half down), fanlights over the doors,
        steps, area railings, chimney stacks smoking, the far roofs and a spire almost gone; gas lamps at the kerb making
        great halos, a pillar box, a plane tree with mottled bark; the lamplighter walks the pavement with his pole."""
        p, rng = self.p, self.rng; r2 = random.Random(int(rng.integers(1e6))); fg = p["fog"]
        gy = int(H * 0.68); kb = gy + 112
        self.back = self._fogback(int(H * 0.6), (0.78, 0.14)); bd = ImageDraw.Draw(self.back)
        for y0, fade in ((gy - 520, 0.8), (gy - 450, 0.66)):                                  # far roofs, chimneys, spire
            col = mix(p["mid"], fg, fade); x = -40
            if fade > 0.7:
                sx = W * 0.36; bd.rectangle([sx - 34, y0 - 150, sx + 34, gy], fill=col + (255,)); bd.polygon([(sx - 34, y0 - 150), (sx + 34, y0 - 150), (sx, y0 - 390)], fill=col + (255,))
            while x < W + 40:
                w = r2.uniform(140, 280); hh = r2.uniform(0, 70); bd.rectangle([x, y0 - hh, x + w, gy], fill=col + (255,))
                for _ in range(r2.randint(1, 2)):
                    cx = x + r2.uniform(10, w - 50); bd.rectangle([cx, y0 - hh - 56, cx + 40, y0 - hh], fill=col + (255,))
                    for k in range(3): bd.rectangle([cx + 4 + k * 12, y0 - hh - 72, cx + 11 + k * 12, y0 - hh - 56], fill=col + (255,))
                if fade < 0.7 and r2.random() < 0.5:
                    bd.rectangle([x + w * 0.4, y0 - hh + 60, x + w * 0.4 + 26, y0 - hh + 100], fill=mix(col, p["gas"], 0.22) + (255,))
                x += w
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        top = gy - 650; brc = mix(p["brick"], fg, 0.3); dark = mix(brc, (0, 0, 0), 0.45); stuc = mix(fg, (214, 204, 182), 0.25)
        d.rectangle([0, top, W, gy], fill=brc + (255,))
        for y in range(top + 8, gy, 9): d.line([(0, y), (W, y)], fill=mix(brc, (0, 0, 0), 0.14) + (255,))
        d.rectangle([0, top - 34, W, top], fill=mix(brc, fg, 0.08) + (255,)); d.rectangle([0, top - 4, W, top + 10], fill=stuc + (255,))
        hw = 410; x0 = -150
        def window(x, y, w, h, lit):
            d.rectangle([x - 6, y - 8, x + w + 6, y], fill=stuc + (255,)); d.rectangle([x - 8, y + h, x + w + 8, y + h + 8], fill=stuc + (255,))
            if lit:
                d.rectangle([x, y, x + w, y + h], fill=mix(p["light"], brc, 0.3) + (255,))
                bl = y + h * r2.uniform(0.25, 0.55); d.rectangle([x, y, x + w, bl], fill=mix(p["light"], brc, 0.62) + (255,))
                gc = mix(p["light"], (0, 0, 0), 0.55)
            else:
                d.rectangle([x, y, x + w, y + h], fill=mix(dark, (0, 0, 0), 0.35) + (255,)); gc = mix(dark, fg, 0.25)
            d.line([(x, y + h / 2), (x + w, y + h / 2)], fill=gc + (255,), width=4); d.line([(x + w / 2, y), (x + w / 2, y + h)], fill=gc + (255,), width=2)
            for k in (1, 2): d.line([(x, y + h * k / 4 + (h / 4 if k == 2 else 0)), (x + w, y + h * k / 4 + (h / 4 if k == 2 else 0))], fill=gc + (255,), width=1)
        for i in range(6):
            hx = x0 + i * hw
            d.line([(hx, top - 34), (hx, gy)], fill=dark + (255,), width=3)
            d.rectangle([hx - 50, top - 140, hx + 50, top - 34], fill=mix(brc, fg, 0.12) + (255,))   # chimney stack on the party wall
            for k in range(4):
                px = hx - 42 + k * 23; d.rectangle([px, top - 172, px + 14, top - 140], fill=mix(brc, (60, 40, 30), 0.3) + (255,)); d.rectangle([px - 2, top - 176, px + 16, top - 170], fill=mix(brc, (60, 40, 30), 0.3) + (255,))
            if i == 3: self.smoke = (hx - 12, top - 180, 300)
            dx = hx + 40                                                                      # door, fanlight, steps
            d.rectangle([dx - 14, gy - 300, dx + 104, gy - 64], fill=stuc + (255,))
            d.rectangle([dx, gy - 250, dx + 90, gy - 64], fill=mix((24, 28, 30), fg, 0.15) + (255,))
            for k in range(2): d.rectangle([dx + 8 + k * 42, gy - 236, dx + 40 + k * 42, gy - 150], outline=mix((24, 28, 30), fg, 0.35) + (255,), width=2)
            fl = 0.2 + 0.4 * r2.random(); d.pieslice([dx, gy - 296, dx + 90, gy - 206], 180, 360, fill=mix(p["gas"], dark, 1 - fl) + (255,))
            for a in range(0, 181, 30): d.line([(dx + 45, gy - 251), (dx + 45 - 45 * math.cos(math.radians(a)), gy - 251 - 45 * math.sin(math.radians(a)))], fill=dark + (255,), width=2)
            d.ellipse([dx + 70, gy - 160, dx + 78, gy - 152], fill=mix(p["gas"], dark, 0.4) + (255,))
            for k in range(4): d.rectangle([dx - 20 - k * 8, gy - 64 + k * 22, dx + 110 + k * 8, gy - 64 + (k + 1) * 22], fill=mix(stuc, (0, 0, 0), 0.08 + 0.06 * k) + (255,))
            for (wx, wy_, ww, wh) in ((hx + 205, gy - 270, 72, 160), (hx + 310, gy - 270, 72, 160), (hx + 40, gy - 500, 76, 180), (hx + 205, gy - 500, 76, 180),
                                      (hx + 310, gy - 500, 76, 180), (hx + 50, gy - 625, 64, 100), (hx + 210, gy - 625, 64, 100), (hx + 315, gy - 625, 64, 100)):
                window(wx, wy_, ww, wh, r2.random() < 0.42)
            bx = hx + 210; d.rectangle([bx, gy - 30, bx + 160, gy + 6], fill=mix(p["light"], dark, 0.35) + (255,))   # basement kitchen glow
        d.rectangle([0, gy, W, kb], fill=mix(p["mid"], fg, 0.3) + (255,))                    # pavement flags
        for x in range(-40, W + 40, 130): d.line([(x, gy), (x - 40, kb)], fill=mix(p["mid"], (0, 0, 0), 0.2) + (255,), width=2)
        d.line([(0, gy + 50), (W, gy + 50)], fill=mix(p["mid"], (0, 0, 0), 0.2) + (255,), width=2)
        ir = (18, 18, 20, 255)                                                                # area railings
        for i in range(6):
            hx = x0 + i * hw; a0, a1 = hx + 160, hx + hw + 10
            d.line([(a0, gy - 70), (a1, gy - 70)], fill=ir, width=4); d.line([(a0, gy + 6), (a1, gy + 6)], fill=ir, width=4)
            for x in np.arange(a0, a1, 16):
                d.line([(x, gy - 82), (x, gy + 8)], fill=ir, width=3); d.polygon([(x - 4, gy - 80), (x + 4, gy - 80), (x, gy - 92)], fill=ir)
        mid = self._fogtint(mid, 0.5, 0.18, top - 180, gy)
        d = ImageDraw.Draw(mid); pc = (24, 22, 22)
        for lx in (W * 0.24, W * 0.71):
            f = self._gaspost(d, lx, kb - 6, 430, pc, 1.15); self.halos.append((f[0], f[1], 420, 1.0))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        dn.rectangle([0, kb, W, kb + 16], fill=mix(p["mid"], fg, 0.35) + (255,))                # kerb and the wet road
        rc = mix(p["sea"], p["mid"], 0.4); dn.rectangle([0, kb + 16, W, H], fill=rc + (255,))
        for _ in range(900):
            y = kb + 16 + (H - kb) * r2.random() ** 1.4; s_ = 0.4 + (y - kb) / (H - kb) * 1.3; x = r2.uniform(0, W)
            dn.ellipse([x - 10 * s_, y - 4 * s_, x + 10 * s_, y + 4 * s_], fill=mix(rc, p["moon"] if r2.random() < 0.5 else (0, 0, 0), 0.08) + (255,))
        refl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(refl)
        for lx in (W * 0.24, W * 0.71): dr.polygon([(lx - 30, kb + 18), (lx + 30, kb + 18), (lx + 70, H), (lx - 70, H)], fill=p["gas"] + (60,))
        near.alpha_composite(refl.filter(ImageFilter.GaussianBlur(26)))
        dn = ImageDraw.Draw(near); bx = W * 0.86; red = mix((150, 32, 28), fg, 0.18)       # pillar box
        dn.rectangle([bx - 38, kb - 200, bx + 38, kb - 6], fill=red + (255,)); dn.chord([bx - 44, kb - 236, bx + 44, kb - 170], 180, 360, fill=red + (255,))
        dn.rectangle([bx - 44, kb - 204, bx + 44, kb - 196], fill=mix(red, (0, 0, 0), 0.3) + (255,)); dn.rectangle([bx - 22, kb - 168, bx + 22, kb - 162], fill=(20, 8, 8, 255))
        dn.rectangle([bx - 44, kb - 18, bx + 44, kb - 4], fill=mix(red, (0, 0, 0), 0.4) + (255,)); dn.line([(bx + 28, kb - 200), (bx + 28, kb - 20)], fill=mix(red, (255, 220, 180), 0.25) + (255,), width=3)
        tx = 70                                                                               # plane tree, mottled bark
        dn.polygon([(tx - 46, H), (tx + 50, H), (tx + 30, H * 0.3), (tx - 20, H * 0.3)], fill=nc + (255,))
        for _ in range(26):
            yy = r2.uniform(H * 0.32, H - 20); ww = r2.uniform(10, 26); dn.ellipse([tx - 20 + r2.uniform(-10, 30), yy, tx + r2.uniform(-10, 30) + ww, yy + ww * 1.6], fill=mix(nc, fg, 0.22) + (255,))
        def branch(x, y, a, L, wd, n):
            if n == 0 or L < 14: return
            x2, y2 = x + L * math.cos(a), y - L * math.sin(a); dn.line([(x, y), (x2, y2)], fill=nc + (255,), width=max(1, int(wd)))
            for da in (-0.45, 0.4): branch(x2, y2, a + da + r2.uniform(-0.2, 0.2), L * 0.72, wd * 0.62, n - 1)
        for a in (1.25, 1.6, 0.85, 2.1): branch(tx, H * 0.32, a, 190, 16, 6)
        self.near = near
        self.lighter = dict(y=gy + 96, h=250)
        self._mkbanks([(gy - 330, 160, 0.34, 150), (gy + 40, 120, 0.24, 110), (top - 40, 170, 0.3, 190)])
        self.fog_y = gy - 120; self.fog_a = 0.2; self.particles = "drizzle"

    def _tug(self, img, t, ph):
        """EP11: a small steam tug coming down the river once per loop: lit wheelhouse, funnel breathing smoke, mast lamp."""
        T = self.tug; u = t / LOOP_S; s = T["s"]; x = T["x0"] + (T["x1"] - T["x0"]) * u; y = T["y"] + 2 * math.sin(ph * 4)
        p = self.p; c = mix(p["near"], p["fog"], 0.35) + (255,); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for k in range(10):                                                                   # funnel smoke trailing behind
            v = ((t / LOOP_S) * 6 + k / 10) % 1.0; r = (10 + 50 * v) * s
            sx = x + (60 + 260 * v) * s; sy = y - (150 + 90 * v ** 0.7) * s
            lay.alpha_composite(self.tint(self.glow_sm.resize((int(r * 2), int(r * 2))), mix(p["fog"], (40, 36, 32), 0.4), 0.5 * (1 - v)), (int(sx - r), int(sy - r)))
        d.polygon([(x - 170 * s, y - 34 * s), (x + 150 * s, y - 34 * s), (x + 132 * s, y), (x - 150 * s, y)], fill=c)
        d.rectangle([x - 80 * s, y - 84 * s, x + 20 * s, y - 34 * s], fill=c); d.rectangle([x + 40 * s, y - 150 * s, x + 66 * s, y - 34 * s], fill=c)
        d.rectangle([x + 36 * s, y - 158 * s, x + 70 * s, y - 148 * s], fill=c); d.line([(x - 110 * s, y - 34 * s), (x - 110 * s, y - 180 * s)], fill=c, width=max(2, int(4 * s)))
        for k in range(3): d.rectangle([x - 70 * s + k * 30 * s, y - 72 * s, x - 52 * s + k * 30 * s, y - 52 * s], fill=mix(p["gas"], p["near"], 0.15) + (255,))
        img.alpha_composite(lay)
        img.alpha_composite(self.tint(self.glow_sm.resize((int(120 * s), int(120 * s))), p["gas"], 0.7), (int(x - 110 * s - 60 * s), int(y - 180 * s - 60 * s)))
        img.alpha_composite(self.tint(self.glow_lg.resize((int(300 * s), int(200 * s))), p["gas"], 0.28), (int(x - 30 * s - 150 * s), int(y - 62 * s - 100 * s)))
        d = ImageDraw.Draw(img)
        for j in range(6):                                                                    # its light trembling on the water
            yy = y + 6 + j * 7; off = 5 * math.sin(ph * 3 + j); ww = (50 - j * 6) * s * (0.7 + 0.3 * math.sin(ph * 5 + j))
            d.line([(x - 30 * s - ww / 2 + off, yy), (x - 30 * s + ww / 2 + off, yy)], fill=p["gas"] + (int(90 - j * 13),), width=2)

    def build_embankment(self):
        """Looking down the river wall in the fog: the granite parapet running away from us with dolphin lamp standards,
        each fainter than the last; Cleopatra's Needle on the wall; across the water the clock tower with its lit dial and
        the long Gothic roofline, the railway bridge with its lamps; trees and lit windows on the landward side; a tug."""
        p, rng = self.p, self.rng; r2 = random.Random(int(rng.integers(1e6))); fg = p["fog"]
        hy = int(H * 0.5); vx, vy = W * 0.47, hy + 24
        self.back = self._fogback(hy, (0.3, 0.17)); self._water(hy + 2, 0.45); bd = ImageDraw.Draw(self.back)
        fc = mix(p["mid"], fg, 0.72); fc2 = mix(p["mid"], fg, 0.62)
        bd.rectangle([0, hy - 80, W * 0.44, hy + 3], fill=fc + (255,))                         # far roofline with pinnacles
        for x in range(0, int(W * 0.44), 34):
            bd.polygon([(x, hy - 80), (x + 8, hy - 80), (x + 4, hy - 108)], fill=fc + (255,))
            if (x // 34) % 3 == 1: bd.rectangle([x + 14, hy - 56, x + 22, hy - 36], fill=mix(fc, p["gas"], 0.25) + (255,))
        tx = W * 0.13                                                                         # the clock tower
        bd.rectangle([tx - 46, hy - 470, tx + 46, hy], fill=fc + (255,)); bd.rectangle([tx - 58, hy - 520, tx + 58, hy - 380], fill=fc + (255,))
        bd.polygon([(tx - 58, hy - 520), (tx + 58, hy - 520), (tx + 30, hy - 600), (tx - 30, hy - 600)], fill=fc + (255,))
        bd.polygon([(tx - 30, hy - 600), (tx + 30, hy - 600), (tx, hy - 720)], fill=fc + (255,))
        bd.ellipse([tx - 38, hy - 488, tx + 38, hy - 412], fill=mix(p["gas"], fc, 0.5) + (255,))
        for k in range(12): a = k * TAU / 12; bd.line([(tx + 30 * math.cos(a), hy - 450 + 30 * math.sin(a)), (tx + 36 * math.cos(a), hy - 450 + 36 * math.sin(a))], fill=fc + (255,), width=2)
        bd.line([(tx, hy - 450), (tx + 4, hy - 474)], fill=fc + (255,), width=3); bd.line([(tx, hy - 450), (tx + 18, hy - 446)], fill=fc + (255,), width=3)
        self.halos.append((tx, hy - 450, 190, 0.5))
        for x0 in np.arange(W * 0.2, W * 0.5, 170):                                           # railway bridge piers and girders
            bd.rectangle([x0, hy - 46, x0 + 30, hy + 8], fill=fc2 + (255,))
        bd.rectangle([W * 0.2, hy - 70, W * 0.5, hy - 46], fill=fc2 + (255,))
        for x0 in np.arange(W * 0.2, W * 0.5, 24): bd.line([(x0, hy - 70), (x0 + 24, hy - 46)], fill=mix(fc2, fg, 0.4) + (255,), width=2)
        for x0 in np.arange(W * 0.22, W * 0.5, 120): self.halos.append((x0, hy - 82, 46, 0.45)); self.wlights.append((x0, 16, 50, r2.uniform(0, TAU)))
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        bc = mix(p["mid"], fg, 0.55)                                                          # landward side: buildings, trees
        d.rectangle([vx + 20, hy - 280, W, vy + 6], fill=bc + (255,))
        x = vx + 20
        while x < W:
            w = r2.uniform(120, 220); hh = r2.uniform(0, 90); d.rectangle([x, hy - 280 - hh, x + w, hy - 270], fill=bc + (255,))
            for r in range(4):
                for c in range(int(w // 46)):
                    if r2.random() < 0.3: d.rectangle([x + 14 + c * 46, hy - 250 - hh * 0.5 + r * 60, x + 30 + c * 46, hy - 222 - hh * 0.5 + r * 60], fill=mix(bc, p["gas"], 0.4) + (255,))
            x += w
        mid = self._fogtint(mid, 0.42, 0.3, 0, H); d = ImageDraw.Draw(mid)
        def P(X, Y, z): return (vx + X / z, vy + Y / z)
        d.polygon([P(-900, 420, 0.5), P(-900, 420, 80), (W + 40, vy + 6), (W + 40, H)], fill=mix(p["mid"], fg, 0.25) + (255,))   # promenade
        for z in (1.0, 1.6, 2.6, 4.2, 7, 12):
            a, b = P(-900, 420, z), P(1200, 420, z); d.line([a, b], fill=mix(p["mid"], (0, 0, 0), 0.25) + (255,), width=max(1, int(3 / z ** 0.5)))
        for z in (30, 20, 13, 8.5, 5.6, 3.8, 2.6):                                            # plane trees along the road
            fd = 1 - math.exp(-z / 7); tc = mix(p["near"], fg, fd * 0.9); bx, by = P(700, 420, z); th = 1500 / z
            d.rectangle([bx - 18 / z ** 0.6, by - th, bx + 18 / z ** 0.6, by], fill=tc + (255,))
            for k in range(9):
                a = 0.5 + k * 0.25; L = th * r2.uniform(0.3, 0.5)
                d.line([(bx, by - th * 0.75), (bx + L * math.cos(a) * 0.8, by - th * 0.75 - L * math.sin(a))], fill=tc + (255,), width=max(1, int(8 / z ** 0.6)))
            f = self._gaspost(d, P(560, 420, z)[0], P(560, 420, z)[1], 1300 / z, mix(p["near"], fg, fd * 0.85), 3.0 / z); self.halos.append((f[0], f[1], 900 / z ** 0.8, 1 - 0.5 * fd))
        pc = mix(p["mid"], (150, 138, 120), 0.25)                                            # the granite parapet
        d.polygon([P(-900, 120, 0.5), P(-900, 120, 80), P(-900, 420, 80), P(-900, 420, 0.5)], fill=pc + (255,))
        d.polygon([P(-990, 100, 0.5), P(-990, 100, 80), P(-900, 120, 80), P(-900, 120, 0.5)], fill=mix(pc, p["moon"], 0.15) + (255,))
        for z in np.geomspace(0.6, 60, 40): d.line([P(-900, 120, z), P(-900, 420, z)], fill=mix(pc, (0, 0, 0), 0.22) + (255,), width=max(1, int(4 / z ** 0.5)))
        def needle():
            nb, nt = P(-1080, 104, 15), P(-1080, -5600, 15); nw = 900 / 15                      # Cleopatra's Needle
            ncol = mix(mix(p["mid"], (150, 110, 96), 0.25), fg, 0.5)
            d.rectangle([nb[0] - nw * 0.9, nb[1] - 60, nb[0] + nw * 0.9, nb[1] + 6], fill=ncol + (255,))
            d.polygon([(nb[0] - nw / 2, nb[1] - 60), (nb[0] + nw / 2, nb[1] - 60), (nt[0] + nw * 0.33, nt[1]), (nt[0] - nw * 0.33, nt[1])], fill=ncol + (255,))
            d.polygon([(nt[0] - nw * 0.33, nt[1]), (nt[0] + nw * 0.33, nt[1]), (nt[0], nt[1] - nw * 0.6)], fill=mix(ncol, p["gas"], 0.2) + (255,))
            for k in range(10): yk = nb[1] - 80 - k * (nb[1] - nt[1] - 100) / 10; d.line([(nb[0] - 6, yk), (nb[0] + 6, yk)], fill=mix(ncol, (0, 0, 0), 0.2) + (255,), width=2)
        for z in (24, 15.5, 10, 6.4, 4.1, 2.75, 1.9):                                    # dolphin lamps on the wall
            if z == 10: needle()
            fd = 1 - math.exp(-z / 6); col = mix((20, 20, 22), fg, fd * 0.85); bx, by = P(-930, 104, z)
            f = self._gaspost(d, bx, by, 1250 / z, col, 2.6 / z, dolphin=True); self.halos.append((f[0], f[1], min(560, 760 / z ** 0.75), 1 - 0.55 * fd))
            self.wlights.append((f[0] - 40 / z, 60 / z ** 0.5 + 6, 70 * (1 - fd * 0.7), r2.uniform(0, TAU)))
        self.mid = self._fogtint(mid, 0.12, 0.0, 0, H)
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]
        bx0 = W * 0.7; by0 = H - 40                                                           # a bench on the promenade
        dn.rectangle([bx0, by0 - 120, bx0 + 380, by0 - 104], fill=nc + (255,)); dn.rectangle([bx0, by0 - 190, bx0 + 380, by0 - 176], fill=nc + (255,)); dn.rectangle([bx0 + 6, by0 - 220, bx0 + 374, by0 - 206], fill=nc + (255,))
        for sx in (0, 330): dn.polygon([(bx0 + sx, by0), (bx0 + sx + 50, by0), (bx0 + sx + 46, by0 - 230), (bx0 + sx + 14, by0 - 230)], fill=nc + (255,))
        self.near = near
        self.tug = dict(x0=vx + 80, x1=-380, y=hy + 64, s=0.62)
        self._mkbanks([(hy + 20, 70, 0.32, 170), (hy - 120, 140, 0.22, 120), (vy + 220, 120, 0.12, 140)])
        self.fog_y = hy - 20; self.fog_a = 0.22; self.particles = "drizzle"

    def _hansom(self, img, ph):
        """EP11: the cab horse in its rug nodding over its nosebag and breathing out little clouds of steam; the chestnut
        brazier's coals breathing red through the holes in its sides."""
        p = self.p; hx, hy_, s = self.hansom; nod = (5 * math.sin(ph * 2) + 2 * math.sin(ph * 5)) * s
        c = mix(p["near"], (52, 40, 34), 0.3) + (255,); d = ImageDraw.Draw(img)
        d.polygon([(hx + 70 * s, hy_ - 10 * s), (hx + 20 * s, hy_ - 70 * s + nod * 0.4), (hx - 10 * s, hy_ - 60 * s + nod * 0.5), (hx + 10 * s, hy_ + 50 * s), (hx + 90 * s, hy_ + 60 * s)], fill=c)
        hd = [(hx - 10 * s, hy_ - 62 * s + nod), (hx + 14 * s, hy_ - 66 * s + nod), (hx - 30 * s, hy_ + 20 * s + nod), (hx - 60 * s, hy_ + 30 * s + nod), (hx - 66 * s, hy_ + 12 * s + nod)]
        d.polygon(hd, fill=c); d.polygon([(hx - 2 * s, hy_ - 62 * s + nod), (hx + 6 * s, hy_ - 92 * s + nod), (hx + 12 * s, hy_ - 64 * s + nod)], fill=c)
        d.polygon([(hx - 70 * s, hy_ + 6 * s + nod), (hx - 26 * s, hy_ + 22 * s + nod), (hx - 34 * s, hy_ + 64 * s + nod), (hx - 72 * s, hy_ + 52 * s + nod)], fill=mix(c[:3], (90, 76, 52), 0.35) + (255,))   # nosebag
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for k in range(2):                                                                    # breath: two puffs per loop
            v = ((ph / TAU) * 4 + k * 0.5) % 1.0
            if v < 0.7:
                r = (12 + 60 * v) * s; bx, by = hx - 80 * s - 70 * v * s, hy_ + 10 * s + nod - 50 * v * s
                lay.alpha_composite(self.tint(self.glow_sm.resize((int(r * 2), int(r * 2))), mix(p["fog"], p["moon"], 0.5), 0.45 * math.sin(math.pi * v / 0.7)), (int(bx - r), int(by - r)))
        img.alpha_composite(lay)
        x, y = self.brazier; fl = 0.75 + 0.15 * math.sin(ph * 3) + 0.1 * math.sin(ph * 8 + 1)
        img.alpha_composite(self.tint(self.glow_lg.resize((420, 300)), p["ember"], 0.42 * fl), (int(x - 210), int(y - 170)))
        d = ImageDraw.Draw(img)
        for k in range(5):
            for j in range(2): d.ellipse([x - 52 + k * 24, y - 30 + j * 30, x - 42 + k * 24, y - 20 + j * 30], fill=mix(p["ember"], (255, 220, 150), 0.3 * fl * (0.6 + 0.4 * math.sin(ph * 5 + k + j))) + (255,))

    def build_cabstand(self):
        """A cab rank in the fog: the green cabmen's shelter with lit windows and a smoking stove pipe, a hansom cab with lamps
        lit and the driver up on his high seat, the horse in a rug at its nosebag, a gas lamp on the far pavement, buildings
        across the street dissolving into fog, and a chestnut seller's brazier glowing in the foreground."""
        p, rng = self.p, self.rng; r2 = random.Random(int(rng.integers(1e6))); fg = p["fog"]; gy = int(H * 0.74)
        self.back = self._fogback(int(H * 0.6), (0.58, 0.13)); bd = ImageDraw.Draw(self.back)
        for y0, fade in ((gy - 560, 0.8), (gy - 470, 0.62)):
            col = mix(p["mid"], fg, fade); x = -30
            while x < W + 30:
                w = r2.uniform(200, 360); hh = r2.uniform(0, 80); bd.rectangle([x, y0 - hh, x + w, gy], fill=col + (255,))
                for r in range(5):
                    for cc in range(int(w // 60)):
                        if r2.random() < 0.28: bd.rectangle([x + 20 + cc * 60, y0 - hh + 40 + r * 80, x + 44 + cc * 60, y0 - hh + 84 + r * 80], fill=mix(col, p["gas"], 0.3 if fade > 0.7 else 0.42) + (255,))
                x += w
        mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(mid)
        pv = mix(p["mid"], fg, 0.45); d.rectangle([0, gy - 130, W, gy - 104], fill=pv + (255,)); d.rectangle([0, gy - 104, W, gy - 96], fill=mix(pv, p["moon"], 0.15) + (255,))
        rd = mix(p["sea"], p["mid"], 0.45); d.rectangle([0, gy - 96, W, H], fill=rd + (255,))
        for _ in range(1100):
            y = gy - 96 + (H - gy + 96) * r2.random() ** 1.3; s_ = 0.35 + (y - gy + 96) / (H - gy + 96) * 1.3; x = r2.uniform(0, W)
            d.ellipse([x - 11 * s_, y - 4 * s_, x + 11 * s_, y + 4 * s_], fill=mix(rd, p["moon"] if r2.random() < 0.5 else (0, 0, 0), 0.08) + (255,))
        mid = self._fogtint(mid, 0.3, 0.0, gy - 130, H); d = ImageDraw.Draw(mid)
        f = self._gaspost(d, W * 0.455, gy - 112, 400, mix((22, 22, 24), fg, 0.3), 1.0); self.halos.append((f[0], f[1], 400, 0.9))
        x0, x1, base = W * 0.52, W * 0.85, gy - 10; gr = mix((38, 72, 50), fg, 0.22); gd = mix(gr, (0, 0, 0), 0.35)
        for wx in (x0 + 40, x1 - 40): d.ellipse([wx - 20, base - 8, wx + 20, base + 32], fill=(16, 16, 16, 255))   # little wheels
        d.rectangle([x0, base - 240, x1, base], fill=gr + (255,))
        for k in range(9):
            px = x0 + 14 + k * (x1 - x0 - 28) / 9; d.rectangle([px, base - 100, px + (x1 - x0 - 28) / 9 - 10, base - 14], outline=gd + (255,), width=3)
        d.rectangle([x0, base - 110, x1, base - 100], fill=gd + (255,))
        for k in range(7):                                                                    # lit windows
            wx = x0 + 70 + k * (x1 - x0 - 100) / 7; d.rectangle([wx, base - 210, wx + (x1 - x0 - 100) / 7 - 16, base - 124], fill=mix(p["gas"], gr, 0.28) + (255,))
            d.line([(wx, base - 167), (wx + (x1 - x0 - 100) / 7 - 16, base - 167)], fill=gd + (255,), width=3)
        d.rectangle([x0 + 10, base - 214, x0 + 58, base - 8], fill=gd + (255,))
        d.polygon([(x0 - 30, base - 236), (x1 + 30, base - 236), (x1 - 4, base - 316), (x0 + 4, base - 316)], fill=mix(gd, fg, 0.15) + (255,))
        for k in range(18): kx = x0 + 10 + k * (x1 - x0 - 20) / 17; d.polygon([(kx - 5, base - 316), (kx + 5, base - 316), (kx, base - 334)], fill=mix(gd, fg, 0.15) + (255,))
        cx = x1 - 90; d.rectangle([cx - 9, base - 400, cx + 9, base - 300], fill=(26, 26, 26, 255)); d.polygon([(cx - 22, base - 400), (cx + 22, base - 400), (cx, base - 424)], fill=(26, 26, 26, 255))
        self.smoke = (cx, base - 420, 280)
        for k in range(3): self.halos.append((x0 + 160 + k * 210, base - 168, 170, 0.45))
        nc = mix(p["near"], fg, 0.1); c = nc + (255,); wy = gy + 70                          # the hansom cab
        wx = W * 0.335; R = 128
        d.ellipse([wx - R, wy - R, wx + R, wy + R], outline=c, width=9); d.ellipse([wx - 14, wy - 14, wx + 14, wy + 14], fill=c)
        for k in range(14): a = k * TAU / 14; d.line([(wx, wy), (wx + R * math.cos(a), wy + R * math.sin(a))], fill=c, width=4)
        d.polygon([(W * 0.27, wy - 230), (W * 0.385, wy - 250), (W * 0.39, wy - 60), (W * 0.29, wy - 40), (W * 0.262, wy - 120)], fill=c)
        d.polygon([(W * 0.262, wy - 240), (W * 0.39, wy - 262), (W * 0.385, wy - 250), (W * 0.27, wy - 230)], fill=c)
        d.line([(W * 0.385, wy - 200), (W * 0.41, wy - 262)], fill=c, width=6)                # iron stay up to the high seat
        d.line([(W * 0.29, wy - 60), (W * 0.12, wy - 95)], fill=c, width=8)                   # shaft
        self._man(mid, W * 0.42, wy - 236, 190, 0.0, "top"); d = ImageDraw.Draw(mid)
        d.rectangle([W * 0.392, wy - 330, W * 0.448, wy - 232], fill=mix(nc, (70, 50, 40), 0.3) + (255,))   # the driver's rug over his knees
        d.rectangle([W * 0.388, wy - 244, W * 0.452, wy - 232], fill=c)
        d = ImageDraw.Draw(mid); d.line([(W * 0.41, wy - 380), (W * 0.06, wy - 200)], fill=c, width=2)   # reins over the roof
        for lx, k in ((W * 0.085, -1), (W * 0.11, 1), (W * 0.2, -1), (W * 0.225, 1)):          # legs with a slight bend at the knee
            d.line([(lx, wy - 60), (lx + 3 * k, wy + 40), (lx + 6, wy + 118)], fill=c, width=15, joint="curve"); d.rectangle([lx - 4, wy + 110, lx + 18, wy + 126], fill=c)
        d.ellipse([W * 0.06, wy - 165, W * 0.245, wy - 25], fill=c)                           # horse body with rug
        d.chord([W * 0.08, wy - 172, W * 0.235, wy - 70], 180, 360, fill=mix(nc, (70, 40, 34), 0.35) + (255,))
        for k in range(6): d.line([(W * 0.095 + k * 38, wy - 164), (W * 0.095 + k * 38, wy - 122)], fill=mix(nc, (110, 80, 50), 0.3) + (255,), width=2)
        d.line([(W * 0.24, wy - 120), (W * 0.252, wy - 40), (W * 0.248, wy + 20)], fill=c, width=13, joint="curve")
        self.hansom = (W * 0.058, wy - 196, 1.25)
        for lx in (W * 0.265, W * 0.39): self.halos.append((lx, wy - 212, 120, 0.7)); d.rectangle([lx - 10, wy - 226, lx + 10, wy - 200], fill=mix(p["gas"], nc, 0.2) + (255,))
        self.mid = mid
        near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near); nc = p["near"]; c = nc + (255,)
        bx, by = W * 0.9, H - 150                                                             # the chestnut brazier and its seller
        for sx in (-50, 46): dn.line([(bx + sx, by + 40), (bx + sx * 1.3, H)], fill=c, width=8)
        dn.rectangle([bx - 64, by - 50, bx + 64, by + 44], fill=c); dn.polygon([(bx - 90, by - 50), (bx + 90, by - 50), (bx + 80, by - 64), (bx - 80, by - 64)], fill=c)
        for k in range(9): dn.ellipse([bx - 70 + k * 16, by - 78, bx - 58 + k * 16, by - 64], fill=mix(nc, (90, 60, 40), 0.3) + (255,))
        self.brazier = (bx, by)
        self._man(near, W * 0.975, H + 40, 420, 0.0, "cap")
        self.near = near
        self._mkbanks([(gy - 300, 160, 0.24, 140), (gy - 60, 90, 0.16, 100)])
        self.fog_y = gy - 200; self.fog_a = 0.2; self.particles = "drizzle"

    def _pendulum(self, img, ph):
        """EP11: the wall clock's brass pendulum swinging behind its little glass window (16 swings per loop), and steam
        curling from the kettle on the hob."""
        p = self.p; x, y, L = self.pend; a = 0.13 * math.sin(ph * 16); bx, by = x + L * math.sin(a), y + L * math.cos(a)
        d = ImageDraw.Draw(img); d.line([(x, y), (bx, by)], fill=(120, 96, 50, 255), width=3)
        d.ellipse([bx - 22, by - 22, bx + 22, by + 22], fill=(178, 140, 66, 255)); d.ellipse([bx - 12, by - 14, bx + 2, by - 2], fill=(236, 206, 140, 255))
        kx, ky, h = self.kettle; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for s_ in range(2):
            pts = [(kx + (6 + 40 * v ** 1.5) * math.sin(v * 6 - ph * 2 + s_ * 2.4) - 20 * v, ky - v * h) for v in np.linspace(0, 1, 40)]
            for j in range(39):
                v = j / 39; dl.line([pts[j], pts[j + 1]], fill=mix(p["fog"], p["moon"], 0.5) + (int(110 * (1 - v) ** 1.2 * min(1, v * 6)),), width=max(3, int(4 + 12 * v)))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(4)))

    def build_parlour(self):
        """A rented first-floor parlour: patterned wallpaper, a black marble chimney piece with a coal fire in the iron grate
        and a brass fender, overmantel mirror, a clock under a glass dome and china dogs, a wall clock with a swinging
        pendulum, a gas bracket with a tulip shade turned low, the sash window with lace curtains and heavy drapes, the
        fog and a street-lamp halo outside; armchair with antimacassar, an aspidistra, the landlady's cat on the rug."""
        p, rng = self.p, self.rng; r2 = random.Random(int(rng.integers(1e6)))
        wall = mix((96, 46, 40), p["mid"], 0.3); wd = mix(wall, (0, 0, 0), 0.25)
        self.back = Image.new("RGBA", (W, H), wall + (255,)); d = ImageDraw.Draw(self.back)
        for x in range(0, W, 64): d.rectangle([x, 0, x + 22, H], fill=mix(wall, (0, 0, 0), 0.08) + (255,))
        for y in range(40, int(H * 0.8), 90):
            for x in range(32, W, 64): d.ellipse([x - 7, y - 10, x + 7, y + 10], fill=mix(wall, p["accent"], 0.12) + (255,))
        d.rectangle([0, H * 0.16, W, H * 0.172], fill=mix(wall, (40, 26, 20), 0.5) + (255,))
        fl = mix((52, 34, 26), p["mid"], 0.3); d.rectangle([0, H * 0.8, W, H], fill=fl + (255,))
        for y in np.arange(H * 0.8, H, 22): d.line([(0, y), (W, y)], fill=mix(fl, (0, 0, 0), 0.25) + (255,))
        x0, x1, y0, y1 = W * 0.71, W * 0.93, H * 0.12, H * 0.72                                # the window and the fog beyond
        gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
        for y in range(int(y0), int(y1)): dg.line([(x0, y), (x1, y)], fill=mix(mix(p["fog"], p["sky_mid"], 0.45), p["fog"], (y - y0) / (y1 - y0)) + (255,))
        dg.rectangle([x0, H * 0.5, x1, y1], fill=mix(p["fog"], p["mid"], 0.45) + (90,))
        for k in range(14): dg.line([(x0 + 10 + k * 26, H * 0.58), (x0 + 10 + k * 26, H * 0.68)], fill=mix(p["fog"], p["mid"], 0.6) + (255,), width=3)
        dg.line([(x0, H * 0.58), (x1, H * 0.58)], fill=mix(p["fog"], p["mid"], 0.6) + (255,), width=3)
        self.back.alpha_composite(gl)
        self.back.alpha_composite(self.tint(self._glow(90).resize((560, 560)), p["gas"], 0.55), (int(W * 0.84 - 280), int(H * 0.36 - 280)))
        lg = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lg)                  # the lamp post outside
        dl.rectangle([W * 0.84 - 4, H * 0.36, W * 0.84 + 4, y1], fill=mix(p["fog"], p["mid"], 0.55) + (255,)); dl.polygon([(W * 0.84 - 12, H * 0.37), (W * 0.84 + 12, H * 0.37), (W * 0.84 + 17, H * 0.34), (W * 0.84 - 17, H * 0.34)], fill=mix(p["gas"], p["fog"], 0.3) + (255,))
        self.back.alpha_composite(lg)
        d = ImageDraw.Draw(self.back); fr = (226, 214, 190, 255)
        d.rectangle([x0 - 16, y0 - 16, x1 + 16, y1 + 22], outline=mix(wall, (230, 220, 200), 0.4) + (255,), width=16)
        d.line([(x0, (y0 + y1) / 2), (x1, (y0 + y1) / 2)], fill=fr, width=10); d.line([((x0 + x1) / 2, y0), ((x0 + x1) / 2, y1)], fill=fr, width=6)
        for u in (1 / 3, 2 / 3): d.line([(x0 + (x1 - x0) * u, y0), (x0 + (x1 - x0) * u, y1)], fill=fr, width=3)
        lace = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lace)
        dl.rectangle([x0, H * 0.3, x1, y1], fill=(236, 230, 214, 46))
        for yy in np.arange(H * 0.32, y1, 26):
            for xx in np.arange(x0 + 10, x1, 26): dl.ellipse([xx - 6, yy - 6, xx + 6, yy + 6], outline=(240, 236, 222, 70), width=2)
        for xx in np.arange(x0, x1, 18): dl.arc([xx - 9, y1 - 14, xx + 9, y1 + 4], 0, 180, fill=(240, 236, 222, 90), width=2)
        self.back.alpha_composite(lace); d = ImageDraw.Draw(self.back)
        dr = mix((70, 30, 34), p["mid"], 0.35)                                                # drapes and pelmet
        for sx0 in (x0 - 120, x1 - 10):
            d.polygon([(sx0, y0 - 40), (sx0 + 130, y0 - 40), (sx0 + 110 if sx0 < x0 else sx0 + 140, H * 0.82), (sx0 - 10 if sx0 < x0 else sx0 + 20, H * 0.82)], fill=dr + (255,))
            for k in range(5): d.line([(sx0 + 20 + k * 22, y0 - 30), (sx0 + 14 + k * 24 + (0 if sx0 < x0 else 10), H * 0.8)], fill=mix(dr, (0, 0, 0), 0.3) + (255,), width=4)
        d.rectangle([x0 - 140, y0 - 70, x1 + 140, y0 - 20], fill=mix(dr, (0, 0, 0), 0.15) + (255,))
        for xx in np.arange(x0 - 130, x1 + 130, 24): d.ellipse([xx, y0 - 26, xx + 16, y0 - 12], fill=mix(dr, p["accent"], 0.3) + (255,))
        cx = W * 0.36; d.rectangle([W * 0.2, 0, W * 0.52, H * 0.8], fill=mix(wall, (0, 0, 0), 0.06) + (255,))   # chimney breast
        for x in range(int(W * 0.2), int(W * 0.52), 64): d.rectangle([x, 0, x + 22, H * 0.8], fill=mix(wall, (0, 0, 0), 0.13) + (255,))
        d.rectangle([W * 0.26, H * 0.08, W * 0.46, H * 0.39], fill=(150, 112, 56, 255))      # overmantel mirror, gilt frame
        d.rectangle([W * 0.27, H * 0.1, W * 0.45, H * 0.375], fill=mix(wall, (20, 16, 18), 0.5) + (255,))
        self.back.alpha_composite(self.tint(self._glow(90).resize((300, 200)), p["light"], 0.25), (int(W * 0.36 - 150), int(H * 0.26 - 60)))
        d = ImageDraw.Draw(self.back); mk = (22, 20, 22, 255)
        d.rectangle([W * 0.235, H * 0.4, W * 0.485, H * 0.43], fill=mk); d.rectangle([W * 0.245, H * 0.43, W * 0.475, H * 0.8], fill=(30, 28, 30, 255))
        d.rectangle([cx - 150, H * 0.5, cx + 150, H * 0.8], fill=(10, 8, 8, 255)); d.chord([cx - 150, H * 0.44, cx + 150, H * 0.58], 180, 360, fill=(10, 8, 8, 255))
        for k in range(5): d.line([(cx - 110, H * 0.66 + k * 18), (cx + 110, H * 0.66 + k * 18)], fill=(46, 40, 38, 255), width=5)
        d.rectangle([cx - 230, H * 0.64, cx - 152, H * 0.66], fill=mk)                         # the hob, the kettle
        d.ellipse([cx - 222, H * 0.58, cx - 162, H * 0.645], fill=(66, 58, 54, 255)); d.line([(cx - 160, H * 0.6), (cx - 136, H * 0.575)], fill=(66, 58, 54, 255), width=7)
        d.arc([cx - 214, H * 0.55, cx - 170, H * 0.62], 180, 360, fill=(66, 58, 54, 255), width=4)
        self.kettle = (cx - 136, H * 0.57, 210)
        mantel = [(cx - 40, "dome"), (cx - 210, "dog"), (cx + 170, "dog"), (cx + 90, "candle")]
        for mx_, kind in mantel:
            yb = H * 0.4
            if kind == "dome":
                d.rectangle([mx_ - 50, yb - 12, mx_ + 50, yb], fill=(60, 44, 30, 255)); d.rectangle([mx_ - 28, yb - 90, mx_ + 28, yb - 12], fill=(96, 70, 40, 255))
                d.ellipse([mx_ - 20, yb - 84, mx_ + 20, yb - 44], fill=(222, 210, 184, 255)); d.line([(mx_, yb - 64), (mx_ + 2, yb - 80)], fill=(30, 26, 22, 255), width=2); d.line([(mx_, yb - 64), (mx_ + 12, yb - 62)], fill=(30, 26, 22, 255), width=2)
                gc_ = mix(wall, (220, 220, 220), 0.4) + (255,)
                d.arc([mx_ - 44, yb - 170, mx_ + 44, yb - 40], 180, 360, fill=gc_, width=2); d.line([(mx_ - 44, yb - 105), (mx_ - 44, yb - 12)], fill=gc_, width=2); d.line([(mx_ + 44, yb - 105), (mx_ + 44, yb - 12)], fill=gc_, width=2)
                d.line([(mx_ + 30, yb - 140), (mx_ + 36, yb - 40)], fill=mix(wall, (255, 255, 255), 0.5) + (255,), width=3)
            elif kind == "dog":
                sg = 1 if mx_ < cx else -1; dc = (210, 200, 182, 255)
                d.ellipse([mx_ - 24, yb - 60, mx_ + 24, yb], fill=dc); d.ellipse([mx_ - 16 + sg * 6, yb - 96, mx_ + 16 + sg * 6, yb - 58], fill=dc)
                d.ellipse([mx_ - 22 + sg * 4, yb - 92, mx_ - 12 + sg * 4, yb - 64], fill=(150, 96, 60, 255)); d.ellipse([mx_ + 12 + sg * 4, yb - 92, mx_ + 22 + sg * 4, yb - 64], fill=(150, 96, 60, 255))
            else:
                d.rectangle([mx_ - 4, yb - 80, mx_ + 4, yb - 8], fill=(170, 136, 70, 255)); d.ellipse([mx_ - 16, yb - 12, mx_ + 16, yb], fill=(170, 136, 70, 255)); d.rectangle([mx_ - 5, yb - 112, mx_ + 5, yb - 80], fill=(232, 222, 200, 255))
                d.polygon([(mx_ + 20, yb - 2), (mx_ + 56, yb - 2), (mx_ + 52, yb - 52), (mx_ + 26, yb - 48)], fill=(214, 204, 180, 255))   # letters tucked behind
        wx, wy_ = W * 0.59, H * 0.25                                                          # the wall clock
        d.ellipse([wx - 84, wy_ - 84, wx + 84, wy_ + 84], fill=(70, 46, 30, 255)); d.ellipse([wx - 70, wy_ - 70, wx + 70, wy_ + 70], fill=(226, 216, 192, 255))
        for k in range(12):
            a = k * TAU / 12; d.line([(wx + 58 * math.cos(a), wy_ + 58 * math.sin(a)), (wx + 66 * math.cos(a), wy_ + 66 * math.sin(a))], fill=(40, 32, 26, 255), width=4)
        d.line([(wx, wy_), (wx - 18, wy_ - 34)], fill=(30, 24, 20, 255), width=5); d.line([(wx, wy_), (wx + 46, wy_ + 8)], fill=(30, 24, 20, 255), width=3)
        d.polygon([(wx - 56, wy_ + 70), (wx + 56, wy_ + 70), (wx + 44, H * 0.56), (wx, H * 0.6), (wx - 44, H * 0.56)], fill=(70, 46, 30, 255))
        d.rectangle([wx - 34, wy_ + 104, wx + 34, H * 0.53], fill=(26, 18, 14, 255))
        self.pend = (wx, wy_ + 84, int(H * 0.53 - wy_ - 84 - 30))
        gx, gyy = W * 0.535, H * 0.42                                                         # the gas bracket, turned low
        d.line([(W * 0.52, gyy + 40), (gx, gyy + 40), (gx, gyy + 10)], fill=(150, 116, 60, 255), width=6)
        d.polygon([(gx - 26, gyy - 40), (gx + 26, gyy - 40), (gx + 14, gyy + 8), (gx - 14, gyy + 8)], fill=mix(p["gas"], (255, 255, 255), 0.25) + (255,))
        self.halos.append((gx, gyy - 14, 300, 0.55))
        self.fires.append((cx, H * 0.75, 0.52))
        self.back.alpha_composite(self.tint(self._glow(90).resize((1500, 1100)), p["light"], 0.2), (int(cx - 750), int(H * 0.72 - 550)))
        self.mid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dm = ImageDraw.Draw(self.mid)
        dm.rectangle([cx - 200, H * 0.79, cx + 200, H * 0.81], fill=(186, 146, 70, 255)); dm.line([(cx - 200, H * 0.79), (cx + 200, H * 0.79)], fill=(250, 210, 130, 255), width=2)
        rug = mix((120, 34, 30), p["mid"], 0.35); dm.polygon([(W * 0.12, H), (W * 0.62, H), (W * 0.56, H * 0.83), (W * 0.16, H * 0.83)], fill=rug + (255,))
        dm.polygon([(W * 0.15, H - 10), (W * 0.59, H - 10), (W * 0.545, H * 0.845), (W * 0.175, H * 0.845)], outline=mix(rug, p["accent"], 0.4) + (255,), width=5)
        nc = p["near"]; c = nc + (255,); near = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dn = ImageDraw.Draw(near)
        dn.polygon([(0, H * 0.3), (W * 0.1, H * 0.26), (W * 0.16, H * 0.34), (W * 0.15, H * 0.66), (W * 0.2, H * 0.68), (W * 0.2, H), (0, H)], fill=c)   # armchair
        dn.polygon([(W * 0.07, H * 0.3), (W * 0.13, H * 0.33), (W * 0.12, H * 0.45), (W * 0.05, H * 0.42)], fill=(206, 196, 178, 255))
        for k in range(6): dn.ellipse([W * 0.05 + k * 26, H * 0.42 + k * 4, W * 0.05 + k * 26 + 18, H * 0.42 + k * 4 + 18], fill=(206, 196, 178, 255))
        ax, ay = W * 0.685, H * 0.74                                                           # aspidistra on its stand
        dn.rectangle([ax - 8, ay, ax + 8, H * 0.94], fill=c); dn.ellipse([ax - 60, H * 0.93, ax + 60, H * 0.96], fill=c); dn.rectangle([ax - 70, ay - 10, ax + 70, ay + 4], fill=c)
        dn.polygon([(ax - 50, ay - 10), (ax + 50, ay - 10), (ax + 40, ay - 80), (ax - 40, ay - 80)], fill=mix(nc, (80, 50, 30), 0.3) + (255,))
        for k in range(13):
            a = math.radians(40 + k * 8 + r2.uniform(-4, 4)); L = r2.uniform(200, 320); lw = r2.uniform(14, 24)
            pts = [(ax + L * v * math.cos(a) * 0.9, ay - 80 - L * v * math.sin(a) + 60 * v * v) for v in np.linspace(0, 1, 9)]
            dn.line(pts, fill=mix(nc, (40, 70, 44), 0.35) + (255,), width=int(lw), joint="curve")
        kx, ky = cx + 160, H * 0.9                                                            # the cat, curled on the rug
        dn.ellipse([kx - 90, ky - 46, kx + 90, ky + 30], fill=c); dn.ellipse([kx + 40, ky - 60, kx + 100, ky - 10], fill=c)
        dn.polygon([(kx + 48, ky - 52), (kx + 54, ky - 82), (kx + 68, ky - 56)], fill=c); dn.polygon([(kx + 76, ky - 56), (kx + 88, ky - 82), (kx + 96, ky - 50)], fill=c)
        dn.arc([kx - 90, ky - 46, kx + 90, ky + 30], 190, 320, fill=mix(nc, p["ember"], 0.4) + (255,), width=4)
        dn.line([(kx - 80, ky + 10), (kx - 20, ky + 34), (kx + 50, ky + 26)], fill=c, width=16, joint="curve")
        self.near = near
        self.fog_a = 0.0; self.particles = "dust"

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
        if self.tug: self._tug(img, t, ph)
        img.alpha_composite(self.mid)
        if self.windows:
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            for x, y, w, h, f, k in self.windows:
                fl = 0.78 + 0.22 * math.sin(ph * k * 3 + f) * math.sin(ph * k + f * 2)
                lay.alpha_composite(self.tint(self.glow_sm, p["light"], 0.35 * fl), (int(x - 16), int(y - 16)))
                dl.rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], fill=mix(p["mid"], p["light"], fl) + (255,))
            img.alpha_composite(lay)
        if self.halos: self._halos(img, ph)
        if self.pend: self._pendulum(img, ph)
        if self.hansom: self._hansom(img, ph)
        if self.glints: self._glints(img, ph)
        if self.hanging: self._hanging(img, ph)
        if self.banners: self._banners(img, ph)
        if self.oven: self._oven(img, ph)
        if self.foam: self._foam(img, ph)
        if self.beam: self._beam(img, ph)
        if self.ship: self._ship(img, t, ph)
        if self.smoke: self._smoke(img, t)
        if self.owl: self._owl(img, t)
        if self.caravan: self._caravan(img, t)
        if self.gondola: self._gondola(img, t, ph)
        if self.yakata: self._yakata(img, t, ph)
        if self.chochin: self._chochin(img, ph)
        if self.pipe: self._pipe(img, ph)
        if self.walker: self._walker(img, t, ph)
        if self.sentry: self._sentry(img, t, ph)
        if self.lighter: self._lighter(img, t, ph)
        for tex, y0, amp, f in self.banks:                                                  # EP11: fog banks swaying to and fro
            off = int(W / 2 + amp * math.sin(ph + f)); img.alpha_composite(tex.crop((off, 0, off + W, tex.height)), (0, y0))
        img.alpha_composite(self.near)
        if getattr(self, "spill", None): img.alpha_composite(self.spill)
        if self.willow: self._willow(img, ph)
        if self.steam: self._steam(img, ph)
        if self.eyes: self._eyes(img, ph)
        if self.incense: self._incense(img, ph)
        if self.lamps: self._lamps(img, ph)
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
            elif self.particles == "moths":                                                # EP08: pale moths circling the lamps (or drifting)
                if self.moth_c:
                    cx, cy = self.moth_c[int(x0) % len(self.moth_c)]; R = 40 + 90 * s
                    x = cx + R * math.cos(ph * k + f); y = cy - 40 + R * 0.5 * math.sin(ph * k * 2 + f * 1.3)
                    a = 0.45 * s * (0.7 + 0.3 * math.sin(ph * 6 + f))
                else:
                    x = x0 + 120 * math.sin(ph * k + f); y = H * 0.25 + (y0 % (H * 0.6)) + 50 * math.sin(ph * 2 * k + f * 2)
                    a = 0.16 * s * (0.6 + 0.4 * math.sin(ph * 4 + f))
                col = (240, 230, 206); sz = 2 + 1.6 * s
            elif self.particles == "leaves":                                               # EP09: small maple leaves turning as they fall
                x = x0 + 90 * math.sin(ph * k + f) + 30 * math.sin(ph * 3 + f); y = (y0 + (H + 60) * t / LOOP_S * k) % (H + 60) - 30
                rot = ph * (k + 1) + f * 3; sz = 7 + 5 * s; sq = 0.35 + 0.65 * abs(math.cos(ph * 2 * k + f))
                col = mix(p.get("lacquer", (170, 44, 36)), p["ember"], 0.3 * s); dl = ImageDraw.Draw(lay); pts = []
                for j in range(10):
                    aa = j * TAU / 10; R = sz if j % 2 == 0 else sz * 0.45; lx, ly = R * math.cos(aa), R * math.sin(aa) * sq
                    pts.append((x + lx * math.cos(rot) - ly * math.sin(rot), y + lx * math.sin(rot) + ly * math.cos(rot)))
                dl.polygon(pts, fill=col + (int(170 * s),)); continue
            elif self.particles == "thistledown":                                          # EP10: seed tufts drifting sideways on the night air
                x = (x0 + (W + 80) * t / LOOP_S * k) % (W + 80) - 40; y = H * 0.2 + (y0 % (H * 0.65)) + 40 * math.sin(ph * k + f) - 16 * math.sin(ph * 3 + f)
                a = 0.24 * s * (0.7 + 0.3 * math.sin(ph * 2 + f)); col = mix(p["moon"], (255, 255, 255), 0.3); sz = 3 + 2 * s
            elif self.particles == "drizzle":                                              # EP11: fine wet fog drops drifting down through the gaslight
                x = x0 + 18 * math.sin(ph * k + f); y = (y0 + (H + 40) * t / LOOP_S * (k + 1)) % (H + 40) - 20; L = 8 + 8 * s
                ImageDraw.Draw(lay).line([(x, y), (x - L * 0.25, y + L)], fill=mix(p["gas"], p["moon"], 0.4) + (int(50 + 60 * s),), width=1); continue
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
