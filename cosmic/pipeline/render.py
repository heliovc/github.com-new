"""Cosmic Scale pipeline: script -> voice (Kokoro offline, EN) -> code-drawn space visuals -> MP4 1080p30 + SRT.
Usage: python3 -I render.py ep01_sun.py out/ep01 [--preview]
EP02 added scenes: clock, escape, sky, thermo, energy, ocean, galaxy
EP03 added scenes: zoom, stretch, horizons, deepfield, shrink (violet/magenta palette)
EP04 added scenes: blackhole, spaghetti, twoclocks, horizonsize, inside (ember orange / pale cyan palette)
EP05 added scenes: inflate, flight, measure, density, heavyvsbig, balance (crimson / cream palette)
EP07 added scenes: teaspoon, pulsechart, crush, ladder (log scale), layers, lensing, pulsar, merger (electric blue / coral palette)
EP08 added scenes: skyline (Moon seen from a coastal town, angular size grows; tide), fallpath (radial fall TO SCALE with day/distance/speed
  from a numeric free-fall table), tides (ocean bulge + 1/d³ multiplier), roche (top-down: "fall" = crosses in 22 min / "ring" = smears into a ring),
  theia (giant impact -> debris disk -> Moon). Palette moon silver / ultramarine / magma. Structure NEW: countdown (day counter) + 2 endings + twist.
  Learned: setup script pip may target another python -> use python3 -m pip.
EP09 added scenes: sightlines (top-down star "forest", rays stop at first star; limit= light-travel bubble), blaze (night sky fills
  with star discs into a white wall + Suns counter), suspects (case-board cards with CLEARED/GUILTY stamps), shells (onion shells: k² stars × 1/k²
  brightness = same light), lightbubble (light-travel bubble grows with a cosmic clock; lit vs grey galaxies), stretchwave (wave slides UV->visible
  ->IR->microwave, optional K counter). Palette starlight white / infrared crimson / microwave teal / indigo. Structure NEW: "case file" with 4 suspects.
EP10 added scenes: massdial (log gauge 1–100 Jupiter masses, body barely changes size, colour -> brown dwarf -> red star), sizeup
  (Jupiter vs smallest known star vs Saturn to scale, Sun as an arc), massbudget (planets bar / 80-cell grid of the mass needed), twosuns
  (night landscape lit by a red point + magnitude meter), barywobble (barycentre wobble with zoom on Mercury's orbit / stability zones),
  moonfall (Galilean moons, a ∝ 1/M as mass grows, sqrt distance scale). Palette Jupiter ochre / ember red / lime. Structure NEW: "recipe"
  (step 1..6 build a star). Helper jup10(r, s) = banded Jupiter -> red dwarf.
  Learned: python3 (3.11) can import a broken PIL from /usr/lib/python3/dist-packages -> python3 -m pip install --break-system-packages
  --ignore-installed pillow numpy. Narration ran short (6.6 min) on the first pass: aim ~1,350+ words for 8 min.
EP11 added scenes: ringsky (ground view at a latitude facing the equator; Saturn-scaled rings computed in 3D with a gnomonic camera, cached
  layer; day | night | dusk; shadow=True = Earth's shadow across the arch; city box with which rings are visible), orbitzones (top-down Earth
  TO SCALE with rings, Roche limits, ISS / GPS / geostationary / Moon, animated zoom), ringedge (log zoom on a ring's edge down to 10 m next
  to a 3-storey building), shadowmap (season chart day-of-year x latitude of the noon ring shadow, cities highlighted when shaded),
  craterbelt (ancient Earth with a debris ring and 21 crater markers inside ±30°). Palette ring cream / dusk rose / sea teal.
  Structure NEW: "postcards by latitude". Learned: never put ">" or "<" in SOURCES (they go into the description; the Studio refuses them);
  a horizontal drift of a cached full-frame layer leaves a blank strip at the edge -> keep drift 0; 1,336 words = 7.8 min, ~1,390 = 8.1 min.
EP12 added scenes: lagmeter (chapter card: log "lag meter" 0.1 ns -> billions of years + NEVER, one stamp per message), chiptick (processor die
  + 10 cm ruler, light pulse per 3 GHz tick), fiberrace (New York -> London lanes: vacuum vs glass fiber vs radio, ms timers, slow motion),
  marsdelay (mode moon = real-time 1.28 s radio round trip; range = Earth/Mars orbits to scale with live one-way light time 3 -> 22 min;
  landing = Perseverance timeline, Mars vs what Earth hears), randomwalk (Sun cross-section + random-walk path core -> surface, years counter),
  horizonrun (expanding line, photons x' = Hx - c: inside the horizon they arrive, beyond it they are carried away). Palette photon gold /
  signal green / fiber magenta / navy. Structure NEW: "7 messages, 1 stopwatch" (each chapter = a message and its lag).
EP13 added scenes: departures (split-flap board GATE / DESTINATION / CAR / JET / FASTEST PROBE [+ LIGHT]; rows flip in, hl row glows,
  detail line), roadtrip (highway in perspective into space toward a world, car from behind, odometer + time on the road + generations
  icons; hide = "??" for a guess beat), transfer (top-down orbits, linear up to Mars / square-root beyond; half-ellipse transfer with day
  counter; ghost = dashed straight line; straight = rules demo; avg = live average distance Venus vs Mercury; map = all orbits + AU box),
  slingshot (gravity assist boost | brake toward the Sun | tour = Voyager 2 Grand Tour with mission clock). Palette road amber / board teal /
  ticket coral. Structure NEW: "departure board" (one gate per destination). Learned: NASA Horizons / NSSDC hosts are blocked by the
  proxy -> verify numbers with web search; 1,400 words incl. 34 scenes = 8.2 min. ranking.py: vis "wind" (rank12). scale_short.py:
  vis "mapfit" (scale06, US outline normalised to 4,500 km).
EP14 added scenes: oceancut (side cross-section TO SCALE: sky / ocean v.depth km / seafloor, km ruler; a rock of v.d_m metres falls in:
  mode drop (rests on the floor; "still sticking out" tag if taller than the sea) | burst (explodes at v.alt km, the sea untouched) | crater
  (water cavity v.cav_km + rim wave + steam); v.everest silhouette; v.bare/v.hot for thumbnails), sizeladder (chapter card "ROCK n OF 5":
  rocks spaced evenly with leader lines to a log size axis 1 m -> 30 km + landmarks; n=0/6 = intro/recap), wavering (mode local: rings
  spread over a top-down sea toward a coastline at v.coast_km, minute clock + wave-height box; mode global: rings sweep over a globe,
  hour clock), plume (atmosphere 0-60 km: mode vapor = steam column into the stratosphere + counter; mode ozone = ozone band thins + UV
  index meter 0-60 with WHO "extreme" 11+). Palette abyss teal / impact orange / foam white. Structure NEW: "drop test" (same ocean, five
  rocks, each a chapter). Learned: 1,348 words + 28 scenes = 7.9 min -> ~1,400 words for 8.1 min; three renders in parallel on 4 cores
  are fine (~25 min). ranking.py: vis "crater" (rank13). scale_short.py: vis "bhfit" (scale07, M87* horizon vs the solar system).
EP15 added scenes: signalrun (Earth -> Voyager 1 track on a SQUARE-ROOT scale with landmarks + light times; a radio pulse travels v.h0 -> v.h1
  hours, v.log = log time for sub-second starts; light-time clock + distance readout; v.focus rings a landmark), signaldial (chapter card: a
  24-hour dial filling to v.h, v.stamp in the centre, kicker/title/sub/fact at right), heliobubble (the Sun's bubble TO SCALE: termination
  shock 94 AU + heliopause 121 AU with a tail, both Voyagers' tracks from piecewise year->AU tables, year counter; mode shock | pause | out;
  v.chart = particle-trend chart, labelled as an illustration), powerdown (watt meter 470 W -> v.w_end + 10 instrument lamps, 2 stay on),
  whisper (22 W leaves Voyager, ~4e-19 W reaches a 70 m dish, written out zero by zero), pixeldot (our own re-drawing of the Pale Blue
  Dot frame + pixel-grid zoom, Earth = a disc of 12% of one pixel). Helper voyager15() draws the spacecraft. Palette golden-record gold /
  DSN green / plasma violet. Structure NEW: "one message, hour by hour" (chapters = moments on a 24-hour light-time dial).
  Learned: science.nasa.gov is blocked for WebFetch here too -> web search only; 1,313 words + 32 scenes = 8.05 min; a polygon built
  with (-c) ** 1.4 for c > 0 returns complex numbers -> use max(0, -c); the full 8-min render takes ~45 min on this machine.
  ranking.py: vis "orbityear" (rank14). scale_short.py: vis "moonorbit" (scale08).
EP16 added scenes: zdial (chapter card: half-circle redshift dial on log(1+z) 0 -> 1,100, needle swings to v.z, live readouts of lookback /
  distance when the light left / distance now from cosmo16.py (flat ΛCDM, Planck 2018), 5 "wall" bricks with v.n lit), lightcone (the teardrop:
  distance-at-emission vs cosmic time, both sides; a photon dot rides to v.z with readout box; v.max rings the 5.8 Gly widest point;
  v.event = event-horizon callout), angsize (telescope eyepiece with one 100,000 ly galaxy reddening as it moves z0 -> z1 + apparent-size
  curve with the minimum near z≈1.6; v.dim fades it and shows (1+z)^4), slowmo (two Type Ia-like light curves: nearby vs v.z stretched by
  1+z, day cursor, flashing stars; labelled illustrative), fogwall (mode fog = protons/electrons/zig-zag photons under an orange haze; mode
  clear = electrons pair into atoms, photons fly straight). New helper module cosmo16.py (age, lookback, d_then, chi, EVENT).
  Palette infrared crimson / fog amber / deep teal. Structure NEW: "five walls" (each chapter a reason the edge stays hidden).
  Learned: render.py runs with -I, so a sibling module needs sys.path.insert(0, HERE) before import; EP03 already used horizons/stretch,
  so keep EP16's horizon beat short and visual-new (lightcone event mode). EP16 promised EP17: the biggest star in place of our Sun.
  ranking.py: vis "probes" (rank15). scale_short.py: vis "jupfill" (scale09, planets poured into Jupiter by volume).
EP17 added scenes: swapsky (beach at noon under a replacement star at its TRUE angular size from 1 AU — Sun = 70 px; sky brightness/tint
  from L and the star's blackbody colour bbcol17(T); from_sun animates Sun -> star; glare sky gets a white core + rays; mode inside = Earth
  inside the star, glowing fog), starcard (chapter card "SWAP n OF 5": star sprite star17(r, T) + log bars vs the Sun for width / brightness
  / surface), hzmap (top-down solar system, square-root scale to v.max AU, Kopparapu 2013 zone 0.99–1.70 AU × √L slides from the Sun's to
  the star's; star disc to scale swallows orbits; Earth tagged TOO HOT / TOO COLD / JUST RIGHT / INSIDE THE STAR; v.hl planet in the zone),
  earthtemp (Earth tinted ice/scorched + thermometer −250…500 °C with landmarks; T = 288 K × L^¼, labelled a simple estimate).
  Palette: each star's own blackbody colour. Structure NEW: "star swap" (same Earth, 5 replacement stars; sky / temperature / zone per chapter).
  Learned: ImageDraw on an RGBA image REPLACES pixels (alpha is not blended) -> draw translucent shapes on a separate layer and
  alpha_composite; 1,457 words + 30 scenes = 8.6 min; EP17 promised EP18: what if you fell into Jupiter.
  ranking.py: vis "weigh" (rank17, balance beam in Earth masses). scale_short.py: vis "dwarf" (scale12, Sirius B smaller than Earth).
EP06 added scenes: spinglobe (globe + speed by latitude; top=True rings; slow=True), pendulum, fling, bulge, yearday, dayclock (teal / amber palette)
2026-11-19 (Thursday, Shorts-only day after EP16): ranking.py vis "rocks" (rank16, lumpy asteroids to scale + drive-around counter);
  scale_short.py vis "ballearth" (scale10, Earth as a basketball + magnifier with to-scale coin/pencil + 7 m pan to the Moon) and "marble"
  (scale11, Earth squeezed to its 17.7 mm Schwarzschild size; ruler, balance, log squeeze, Sun = 5.9 km walk).
  Learned: python3 -I may load a broken Debian PIL (/usr/lib/python3/dist-packages) -> python3 -m pip install --force-reinstall pillow.
  Hook check: the spoken hook must say exactly what the big number measures (ISS 7.5 mm, not "space").
2026-11-21 (Saturday, Shorts-only): ranking.py vis "gravity" (rank18, stick person on a bathroom scale over each world's curved surface,
  LCD counter 70 kg -> 70 × g / 9.80, knees bend on a log curve + log ruler × Earth's gravity); scale_short.py vis "jupsun" (scale13, Sun
  packed with to-scale Jupiters, row of 9.95, Earth zoom, 1,048-dot mass grid, density jars) and "andromeda" (scale14, Andromeda + full Moon
  at the same angular scale over hills: 6 Moons along the axis, naked-eye smudge, 2.5 Myr light timeline, long-exposure frame).
  Learned: never paste sun_sprite(r) with r in the thousands (r × 6 px square float array -> OOM kill); fake a zoom with a tinted overlay.
  Moon counts per planet disagree between sources in 2026 (Saturn 274–293) -> avoid "most moons" rankings until NASA publishes one table.
  Ruler labels for near-equal values (1.00 / 1.07 / 1.14) need staggered offsets.
2026-11-22 (Sunday, Shorts-only): ranking.py vis "litre" (rank19, a litre of each planet poured into a glass jar on a kitchen scale, LCD
  counts to the planet's mean density in kg/L, 1-litre water bottle as reference + 0–6 kg/L bar with Saturn floating below water);
  scale_short.py vis "redgiant" (scale15, Betelgeuse 700 Suns wide TO SCALE: screen-filling disc + 1.6 px Sun, log zoom, 7×7×7 isometric
  cube of Suns, Earth equation, orbits Mercury–Mars swallowed, Orion sky) and "sand" (scale16, Sun = 1 mm grain: fingertip, 12 cm ruler +
  lens with a hair, 20 m track to Voyager 1, road to the horizon 28.9 km, Milky Way 680,000 km vs the Earth–Moon line).
  Learned: never cache one code-drawn sprite per radius during a zoom (hundreds of multi-MB arrays) -> cache one and resize; nested
  same-type quotes inside an f-string are a SyntaxError on 3.11; never start the same render twice into one output folder.
EP18 added scenes: plunge (mode hook = cloud horizon from a cached full-frame layer _horizon18 + capsule streak | approach = Jupiter grows
  from Europa's orbit, speed/hours HUD | view = 12.2° disc with 23 full Moons across | entry = capsule in plasma, speed + g HUD, v.label),
  depthgauge (chapter card: log depth gauge 0 -> 70,000 km with clouds / deep air / metal / core bands, capsule marker, floor name, depth,
  optional ptxt/ttxt rows, background darkens with depth), cloudstack (log PRESSURE axis 0.2–25 bar, three model cloud decks, Galileo's
  dotted parachute path to 23 bar, lightning, v.wind streaks + "600+ km/h"), nosurface (phase 0 "surface here? NOT HERE" scan + critical
  point box | 1 capsule sinking through a continuous gradient | 2 helium rain with neon specks in violet metallic hydrogen), jupcut (Jupiter
  cut open TO SCALE, wedge layers molecular / metallic from 10,000 km / dilute core or old compact core, Earth to scale, depth marker,
  hl=skin magnifier on Galileo's 150 km), scars (Shoemaker-Levy 9: fragment train + flashes + day HUD | dark scars on one latitude with
  Earth to scale). Helpers jup18(r) (one r=500 jup10 sprite resized), _capsule18, _hud18. Palette Jupiter ochre / ammonia cream / metallic
  violet. Structure NEW: "the elevator" (one fall, floor by floor; each floor opens on the depth gauge).
  Learned: depth-gauge rows must never show unsourced values -> pass only ptxt/ttxt you can cite; 1,365 words + 32 scenes = 8.3 min.
  EP18 promised EP19: what if Earth had a second Moon? ranking.py: vis "beads" (rank20, Earths strung across each planet at one common
  scale). scale_short.py: vis "magbubble" (scale17, Jupiter's magnetosphere 15 Suns wide, sunward edge 3.2–7.1 million km, sky vs the
  Moon, tail to Saturn's orbit, dissolves back into the hook for the loop).
2026-11-24 (Tuesday, Shorts-only): ranking.py vis "tilt" (rank21, banded planet rotated by its obliquity on the orbit-plane line,
  protractor arc from straight-up + degree counter, Earth 23.4° ghost axis, spin marker reverses for Venus); scale_short.py "sugarcube"
  (scale18, isometric grainy cube, crowd streaming in, stadium atom, Burj Khalifa vs 800 m flesh cube, table cracking, neutron star) and
  "saturnfloat" (scale19, Saturn cutaway packed with Earths, litre jars, floating tank). Learned: science.nasa.gov is not reachable from
  the cloud session (DNS) -> verify numbers with web search; moon counts change every few months -> avoid them in rankings.
2026-11-25 (Wednesday) EP19 added scenes: slotmap (chapter card: square-root distance strip Earth -> 1.5 million km with zones torn /
  falls in / can stay / Sun steals, Roche 18,400, geostationary 42,164, Moon, 0.49 R_H stability edge, Hill radius; pins 1-5, v.n active,
  v.drift in|out arrows, v.stamp verdict stamp), twinsky (desert mesas + lake at night; our Moon and a twin at v.km2 with TRUE relative angular
  size, v.fov zoom, v.phase = twin 75% lit, sky glow from the extra light), tidechart (72 h harbour curve: Moon alone dashed / twin alone /
  both, equilibrium tide, v.lead° and v.period2 h; mode bar = log tidal-pull bars), trojan (Earth-Moon-twin triangle with L4/L5; wobble =
  tadpole libration + Routh 1875 box; companion = Jutzi & Asphaug 1,200 km moon drifting toward the Moon), splat (shred = twin inside the
  Roche limit smearing into a ring; splat = slow 2-3 km/s pancake pile; farside = near side vs far side sprites moon19(far=True)), sunsteal
  (our Hill-problem RK4 simulation, Earth + Sun, frame turning with Earth: orbit started at 1,000,000 km leaves after ~149 days), tangle
  (minimoon loops 2006 RH120 | size lineup person / 1.2 m / 3 m / 10 m / bus | Kamo'oalewa quasi-satellite loop). Helpers moon19(r, k)
  (phase via k = cos phase angle), _sized19, _stamp19, _land19, _box19. Palette moonlight lilac / tide aqua / companion amber.
  Structure NEW: "five parking spots" (one twin Moon tried at 5 distances, each chapter opens and closes on the parking map with a verdict).
  Learned: a twin 60° ahead gives the SAME tide height (cos 2θ pattern, phasors 120° apart); 1,375 words + 32 scenes = 8.1 min.
  EP19 promised EP20: shrink the universe until the Sun is a grain of sand, then walk to the edge. ranking.py: vis "pair" (rank22,
  every planet the same size, moon to scale with it). scale_short.py: vis "olympus" (scale20, Olympus Mons over Arizona at one scale).
2026-11-27 (Friday) EP20 added scenes: signpost (chapter card: wooden trail post with one plank per stop and its distance at the
  grain-of-sand scale, v.n active / passed planks dim + tick, odometer counts (log) from the previous stop to v.km + walking time at 5 km/h,
  dusk hills with a walker), tabletop (macro desk TO SCALE with the 1 mm Sun: earth = cm ruler + Earth speck 10.75 cm away + magnifier with a
  hair + dashed orbit arc | moon = microscope strip, Earth-Moon 276 µm | jupiter = the room: desk, Jupiter 56 cm, Saturn 1.03 m, Neptune 3.23 m),
  fieldmap (top-down map with a log zoom v.z0 -> v.z1 metres: house = building + Neptune ring + Voyager 1 18.6 m | oort = town streets + icy
  shell 215 m - 10.75 km | proxima = 28.9 km; galaxy modes: galaxy (680,000 km Milky Way vs the real Earth-Moon line) | center (Sgr A* 17 mm
  bead in a magnifier, 184 km) | andromeda (25 galaxy widths + 44 Earth-Moon ticks) | collide (illustrative)), snailrace (light at this scale
  = 0.215 mm/s: sun = light front crossing 10.75 cm, 8:19 clock | race = record snail 2.75 mm/s vs light | proxima = year counter to 4.24),
  fitinside (real solar system on a LOG radial scale 0.3 -> 120,000 AU with the Oort band, Voyager 1, and the shrunken observable universe
  4,227 AU wide as a violet cosmic-web sphere; hook | zoom | real | reveal). Helpers _grain20, _lens20 (clipped magnifier), _woodtex20,
  _gal20 (cached galaxy resize), _scalebar20. Palette sand beige / trail green / dusk violet. Structure NEW: "the walk" (one fixed scale,
  five stops on a signpost, odometer + walking clock). Learned: 1,339 words + 33 scenes = 8.07 min; a fresh cloud session needs
  python3 -m pip install --break-system-packages --ignore-installed pillow numpy before python3 -I works. EP20 promised EP21: how many
  Earths fit inside the biggest things in the universe. ranking.py: vis "dwarfs" (rank24). scale_short.py: vis "sunspot" (scale23).
2026-11-26 (Shorts-only day): ranking.py vis "swarm" (rank23, each known moon a dot circling its planet; outro = one square per moon).
  scale_short.py: vis "hexagon" (scale21, Saturn's north-pole hexagon from above, 2 Earths to scale) and "moonmap" (scale22, the Moon on a
  hand-traced Australia at one scale + surface laid flat). Learned: on a day with 2 Scale Shorts the second file must be scale2.mp4
  (same folder); moon counts change often -> cite the Minor Planet Center date; NASA/earthsky hosts blocked -> verify via web search.
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

# ---------------- scenes (EP08: Moon crash — moon silver / ultramarine / magma) ----------------
SILVER8, SEA8, MAGMA8, ICE8 = (222, 226, 236), (46, 112, 255), (255, 96, 44), (150, 200, 255)
_moon8 = {}
def moon8(r, light=(-0.9, -0.35), cracked=0.0):
    """grey Moon with maria + craters (procedural); cracked: 0..1 glowing fracture lines"""
    r = max(3, int(r)); key = (r, light, round(cracked, 2))
    if key in _moon8: return _moon8[key]
    base = planet_sprite(r, (178, 178, 182), light=light).copy()
    if r >= 12:
        a = np.asarray(base, np.float32).copy(); s = a.shape[0]
        yy, xx = np.mgrid[0:s, 0:s].astype(np.float32); nx, ny = (xx - s / 2) / r, (yy - s / 2) / r
        rng = np.random.default_rng(8)
        for (mx, my, mr) in [(-0.25, -0.3, 0.32), (0.2, -0.15, 0.22), (-0.1, 0.25, 0.26), (0.35, 0.3, 0.15)]:
            m = np.exp(-(((nx - mx) ** 2 + (ny - my) ** 2) / (2 * mr * mr)))
            a[..., :3] *= (1 - 0.32 * m)[..., None]
        for _ in range(26):
            cx, cy, cr = rng.uniform(-0.85, 0.85), rng.uniform(-0.85, 0.85), rng.uniform(0.03, 0.11)
            dd = np.hypot(nx - cx, ny - cy)
            a[..., :3] *= (1 - 0.22 * ((dd < cr) & (dd > cr * 0.7)))[..., None]
        base = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
    if cracked > 0 and r >= 12:
        lay = Image.new("RGBA", base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rng = random.Random(5); c = base.width / 2
        for k in range(int(4 + 10 * cracked)):
            x, y = c + rng.uniform(-0.5, 0.5) * r, c + rng.uniform(-0.5, 0.5) * r; pts = [(x, y)]
            ang = rng.uniform(0, 2 * math.pi)
            for _ in range(9):
                ang += rng.uniform(-0.6, 0.6); x += math.cos(ang) * 0.09 * r; y += math.sin(ang) * 0.09 * r
                if math.hypot(x - c, y - c) > r * 0.97: break
                pts.append((x, y))
            if len(pts) > 1:
                d.line(pts, fill=MAGMA8 + (int(110 * min(1, cracked * 1.4)),), width=max(3, r // 22))
                d.line(pts, fill=(255, 210, 150, int(255 * min(1, cracked * 1.4))), width=max(1, r // 90))
        m = Image.new("L", base.size, 0); ImageDraw.Draw(m).ellipse([c - r, c - r, c + r, c + r], fill=255)
        lay.putalpha(Image.fromarray(np.minimum(np.asarray(lay.getchannel("A")), np.asarray(m))))
        base.alpha_composite(lay)
    _moon8[key] = base
    return base

def _fall_table():
    G, M, RE8, RM8, D = 6.674e-11, 5.972e24 + 7.346e22, 6.371e6, 1.7374e6, 3.844e8
    r, vv, tt, dt, out = D, 0.0, 0.0, 30.0, []
    while r > RE8 + RM8:
        out.append((tt / 86400, r / 1e3, -vv / 1e3)); vv -= G * M / r ** 2 * dt; r += vv * dt; tt += dt
    out.append((tt / 86400, (RE8 + RM8) / 1e3, -vv / 1e3)); return out
FALL8 = None
def fall_at(day):
    global FALL8
    if FALL8 is None: FALL8 = _fall_table(); FALL8.append(np.array([x[0] for x in FALL8[:-0 or None]]))
    i = min(len(FALL8) - 2, max(0, int(np.searchsorted(FALL8[-1], day))))
    return FALL8[i]

def landscape8(img, glow, t, tide=0.0):
    """night horizon: hills + city + sea; glow 0..1 moonlight; tide raises the sea line (px)"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    sky = mix((6, 9, 22), (40, 52, 90), glow)
    d.rectangle([0, 0, W, H], fill=sky + (int(170 * glow),))
    img.alpha_composite(lay)
    d = ImageDraw.Draw(img); rng = random.Random(81)
    pts = [(0, H)] + [(x, 800 - 70 * math.sin(x / 260) - 40 * math.sin(x / 97 + 1)) for x in range(0, W + 40, 40)] + [(W, H)]
    d.polygon(pts, fill=mix((10, 12, 20), (34, 38, 56), glow))
    x = 1100
    while x < 1700:
        bw, bh = rng.randint(30, 70), rng.randint(60, 190)
        d.rectangle([x, 820 - bh, x + bw, 900], fill=mix((14, 16, 28), (38, 42, 62), glow))
        for wy in range(int(830 - bh), 890, 22):
            for wx in range(x + 8, x + bw - 8, 16):
                if rng.random() < 0.35: d.rectangle([wx, wy, wx + 6, wy + 9], fill=(255, 214, 140))
        x += bw + rng.randint(4, 16)
    sea = 905 - tide
    d.rectangle([0, sea, W, H], fill=mix((8, 16, 40), (30, 60, 120), glow))
    for k in range(14):
        y = sea + 12 + k * 13; ww = 30 + k * 10 + 10 * math.sin(t * 2 + k)
        d.line([(W * 0.62 - ww, y), (W * 0.62 + ww, y)], fill=mix((40, 50, 80), SILVER8, glow * 0.8), width=3)

_halo8 = {}
def sc_skyline(img, v, t, dur):
    """the Moon as seen from a coastal town, angular size deg0 -> deg1 (60° field of view)"""
    p = easeio((t - 0.4) / max(1.0, dur * v.get("speed", 0.8)))
    deg = v["deg0"] * (v["deg1"] / v["deg0"]) ** p
    pxdeg = W / 60.0; r = min(deg * pxdeg / 2, 760)
    glow = min(1.0, (deg / 10.8) ** 0.8)
    if r > 20:
        hk = (min(int(r), 240) // 6, int(glow * 20))
        if hk not in _halo8: _halo8[hk] = radial(hk[0] * 30, [(0, (200, 210, 235, int(6 * hk[1]))), (0.4, (160, 175, 210, int(2.5 * hk[1]))), (1, (120, 130, 170, 0))])
        paste_c(img, _halo8[hk], W * 0.62, 420)
    landscape8(img, glow, t, v.get("tide", 0) * p)
    cr = round(v.get("cracked", 0) * p, 1)
    if r <= 220: spr = moon8(max(4, r), light=(-0.2, -0.1), cracked=cr)
    else:
        spr = moon8(220, light=(-0.2, -0.1), cracked=cr); k = r / 220; spr = spr.resize((int(spr.width * k), int(spr.height * k)), Image.BILINEAR)
    paste_c(img, spr, W * 0.62, 420 + max(0, r - 300) * 0.5)
    d = ImageDraw.Draw(img)
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([90, 140, 640, 420], 26, fill=(6, 10, 26, 210), outline=SILVER8 + (120,), width=2); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((130, 200), v.get("head", "Tonight"), font=F(52, "ExtraBold"), fill=SILVER8, anchor="lm")
    d.text((130, 290), f"{deg / 0.518:.0f}× wider" if deg > 5 else f"{deg / 0.518:.1f}× wider", font=F(70, "Black"), fill=MAGMA8 if deg > 3 else WHITE, anchor="lm")
    d.text((130, 370), "than the Moon you know", font=F(34, "SemiBold"), fill=DIM, anchor="lm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_fallpath(img, v, t, dur):
    """side view TO SCALE: Earth at left, Moon falling from 384,400 km; day counter, distance, speed"""
    x0, x1, cy = 230, 1730, 560
    k = (x1 - x0) / 384400.0
    u = easeio((t - 0.3) / max(1.0, dur - 1.5)); day = lerp(v["d0"], v["d1"], u)
    dd, dist, sp = fall_at(day)
    d = ImageDraw.Draw(img)
    for i in range(0, 8):
        dk = 50000 * i; x = x0 + dk * k
        d.line([(x, cy + 120), (x, cy + 140)], fill=(80, 90, 120), width=2)
        d.text((x, cy + 170), f"{dk // 1000:,}k km" if i else "0", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    d.line([(x0, cy + 130), (x1, cy + 130)], fill=(80, 90, 120), width=2)
    rr = 18400 * k
    for a in range(0, 360, 12): d.arc([x0 - rr, cy - rr, x0 + rr, cy + rr], a, a + 6, fill=MAGMA8, width=2)
    paste_c(img, earth_sprite(int(6371 * k) + 1, light=(1, -0.2)), x0, cy)
    # trail of daily positions
    for dd2 in range(0, 5):
        if dd2 <= day:
            xx = x0 + fall_at(dd2)[1] * k; d.line([(xx, cy - 40), (xx, cy + 40)], fill=(90, 110, 160), width=2)
            d.text((xx, cy - 60), f"day {dd2}", font=F(24, "SemiBold"), fill=DIM, anchor="mm")
    mx = x0 + dist * k
    paste_c(img, radial(60, [(0, (255, 255, 255, 200)), (1, (200, 210, 240, 0))]), mx, cy)
    paste_c(img, moon8(max(4, int(1737 * k)) + 2), mx, cy)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 140), v.get("head", "The fall, to scale"), font=F(60, "ExtraBold"), fill=WHITE, anchor="mm")
    cols = [("DAY", f"{day:.1f}", SILVER8), ("DISTANCE", f"{dist:,.0f} km", ICE8), ("SPEED", f"{sp:.2f} km/s", MAGMA8)]
    for i, (lab, val, c) in enumerate(cols):
        x = 420 + i * 540
        d.text((x, 830), lab, font=F(32, "Bold"), fill=DIM, anchor="mm"); d.text((x, 910), val, font=F(74, "Black"), fill=c, anchor="mm")
    d.text((x0 + rr + 14, cy - rr - 6), "Roche limit", font=F(24, "Bold"), fill=MAGMA8, anchor="lm")
    d.text((x1, 250), "Earth and Moon drawn to scale", font=F(28, "SemiBold"), fill=DIM, anchor="rm")

def sc_tides(img, v, t, dur):
    """ocean bulge pulled toward the Moon; tidal pull multiplier counts up (log)"""
    p = easeio((t - 0.4) / max(1.0, dur * 0.7))
    mult = v["m0"] * (v["m1"] / v["m0"]) ** p
    cx, cy, R0 = 600, 580, 230
    ex = R0 * (0.06 + 0.10 * math.log10(max(1, mult)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([cx - R0 - ex, cy - R0 + ex * 0.4, cx + R0 + ex, cy + R0 - ex * 0.4], fill=SEA8 + (200,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3)))
    paste_c(img, earth_sprite(R0 - 4, light=(1, -0.2)), cx, cy)
    mr = 30 + 40 * p
    paste_c(img, moon8(int(mr)), cx + 640 - 120 * p, cy)
    d = ImageDraw.Draw(img)
    for s in (-1, 1):
        x = cx + s * (R0 + ex + 30); d.line([(x, cy), (x + s * 50, cy)], fill=WHITE, width=5)
        d.polygon([(x + s * 60, cy), (x + s * 40, cy - 12), (x + s * 40, cy + 12)], fill=WHITE)
    d.text((W / 2, 130), v.get("head", "The oceans notice"), font=F(62, "ExtraBold"), fill=WHITE, anchor="mm")
    d.text((1480, 400), "tidal pull vs today", font=F(40, "Bold"), fill=DIM, anchor="mm")
    d.text((1480, 520), f"×{mult:,.0f}" if mult >= 10 else f"×{mult:.1f}", font=F(140, "Black"), fill=SEA8 if mult < 100 else MAGMA8, anchor="mm")
    d.text((1480, 640), "tides grow with 1 / distance³", font=F(38, "SemiBold"), fill=ICE8, anchor="mm")
    d.text((1480, 700), "half the distance = 8× the tide", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
    d.text((cx, cy + R0 + 80), "bulge exaggerated", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 3) / 0.5))

def sc_roche(img, v, t, dur):
    """top-down: Moon crosses the Roche limit and smears into a ring (mode 'ring') or crosses fast (mode 'fall')"""
    cx, cy, RE_ = 700, 560, 110
    rl = RE_ * 18400 / 6371; mr = RE_ * 1737 / 6371
    d = ImageDraw.Draw(img)
    for a in range(0, 360, 8): d.arc([cx - rl, cy - rl, cx + rl, cy + rl], a, a + 4, fill=MAGMA8, width=3)
    d.text((cx, cy - rl - 26), "Roche limit ≈ 18,000 km", font=F(30, "Bold"), fill=MAGMA8, anchor="mm")
    paste_c(img, earth_sprite(RE_, light=(-1, -0.2)), cx, cy)
    mode = v.get("mode", "ring"); rng = random.Random(9)
    if mode == "fall":
        u = min(1.0, max(0.0, (t - 0.5) / max(1.0, dur - 2.5)))
        x = cx + lerp(rl + 330, RE_ + mr, u ** 1.6)
        inside = x < cx + rl
        sx = 1.0 + (0.5 * (1 - (x - cx - RE_) / (rl - RE_)) if inside else 0)
        spr = moon8(int(mr), cracked=0.8 if inside else 0)
        spr = spr.resize((int(spr.width * sx), int(spr.height / sx ** 0.5)))
        if u < 1: paste_c(img, spr, x, cy)
        else:
            fl = max(0.0, 1 - (t - 0.5 - (dur - 2.5)) / 1.5)
            paste_c(img, radial(500, [(0, (255, 250, 220, 255)), (0.3, MAGMA8 + (220,)), (1, MAGMA8 + (0,))]), cx + RE_, cy, fl)
        d = ImageDraw.Draw(img)
        d.text((1500, 420), "inside the line", font=F(40, "Bold"), fill=DIM, anchor="mm")
        d.text((1500, 520), "22 min", font=F(130, "Black"), fill=MAGMA8, anchor="mm")
        d.text((1500, 620), "before impact", font=F(40, "Bold"), fill=WHITE, anchor="mm")
        d.text((1500, 700), "no time to fall apart", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
    else:
        u = easeio((t - 0.4) / max(1.0, dur * 0.6))
        orb = lerp(rl * 1.25, rl * 0.85, min(1, u * 1.4))
        ang0 = -0.6 + t * 0.35
        spread = max(0.0, (u - 0.35) / 0.65) * 2 * math.pi
        if u < 0.4:
            paste_c(img, moon8(int(mr), cracked=max(0, (u - 0.25) / 0.15)), cx + orb * math.cos(ang0), cy + orb * math.sin(ang0))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        if u >= 0.3:
            for i in range(900):
                f = rng.random(); a = ang0 - f * spread + rng.gauss(0, 0.04); rr = orb + rng.gauss(0, 10 + 30 * u)
                s = rng.choice([1.5, 2, 2.5, 3.5]); c = mix((150, 150, 160), (235, 230, 220), rng.random())
                x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
                dl.ellipse([x - s, y - s, x + s, y + s], fill=c + (int(230 * min(1, (u - 0.3) * 5)),))
        img.alpha_composite(lay)
        d = ImageDraw.Draw(img)
        d.text((1480, 420), v.get("big", "Earth gets rings"), font=F(70, "Black"), fill=SILVER8, anchor="mm")
        d.text((1480, 510), v.get("sub", "the slow ending"), font=F(40, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 3) / 0.5))

def sc_theia(img, v, t, dur):
    """giant impact: Mars-sized Theia hits the molten young Earth; debris disk clumps into the Moon"""
    cx, cy, R0 = 820, 580, 210
    tc = 2.2
    d = ImageDraw.Draw(img)
    d.text((W / 2, 120), v.get("head", "4.5 billion years ago"), font=F(62, "ExtraBold"), fill=WHITE, anchor="mm")
    hot = planet_sprite(R0, (200, 80, 40), light=(-0.8, -0.3), glow=(255, 120, 60))
    paste_c(img, hot, cx, cy)
    if t < tc:
        u = t / tc; tx, ty = lerp(1800, cx + R0 * 1.2, u ** 1.5), lerp(180, cy - R0 * 0.7, u ** 1.5)
        paste_c(img, planet_sprite(R0 // 2, (150, 140, 130), light=(-0.8, -0.3)), tx, ty)
        d.text((tx, ty - R0 // 2 - 40), "Theia (≈ Mars size)", font=F(34, "Bold"), fill=SILVER8, anchor="mm")
    else:
        s = t - tc
        fl = max(0.0, 1 - s / 1.2)
        if fl > 0: paste_c(img, radial(900, [(0, (255, 255, 240, 255)), (0.25, (255, 200, 120, 220)), (1, (255, 120, 50, 0))]), cx + R0 * 0.8, cy - R0 * 0.5, fl)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(12)
        clump = min(1.0, max(0.0, (s - 3.0) / 4.0))
        mang = s * 0.25; mx, my = cx + 470 * math.cos(mang), cy + 470 * 0.42 * math.sin(mang)
        for i in range(700):
            a = rng.uniform(0, 2 * math.pi) + s * 0.25 * (470 / rng.uniform(300, 600)); rr = rng.uniform(R0 * 1.3, R0 * 2.9) * min(1, s / 1.5)
            x, y = cx + rr * math.cos(a), cy + rr * 0.42 * math.sin(a)
            x, y = lerp(x, mx, clump * rng.uniform(0.7, 1)), lerp(y, my, clump * rng.uniform(0.7, 1))
            c = mix(MAGMA8, (200, 190, 180), min(1, s / 6)); r2 = rng.choice([1.5, 2, 3])
            dl.ellipse([x - r2, y - r2, x + r2, y + r2], fill=c + (220,))
        img.alpha_composite(lay)
        if clump > 0.6: paste_c(img, moon8(int(60 * (clump - 0.6) / 0.4) + 4), mx, my)
        d = ImageDraw.Draw(img)
        if clump > 0.8: d.text((mx, my + 90), "the Moon", font=F(40, "Black"), fill=SILVER8, anchor="mm")
    caption(img, v.get("caption"), ease((t - 3) / 0.5))

# ---------------- scenes (EP09: why is space black) ----------------
STAR9, IR9, MW9, INK9 = (246, 244, 255), (255, 70, 110), (60, 230, 190), (120, 128, 255)

def _forest9(seed=9, n=420, rmin=60, rmax=1300):
    rng = random.Random(seed); out = []
    while len(out) < n:
        a = rng.uniform(0, 2 * math.pi); r = math.sqrt(rng.uniform(rmin ** 2, rmax ** 2))
        out.append((r * math.cos(a), r * math.sin(a), rng.uniform(6, 13)))
    return np.array(out, np.float32)
FOREST9 = None

def sc_sightlines(img, v, t, dur):
    """top-down 'forest' of stars around you: lines of sight run outward and stop at the first star they hit.
    reach grows (fraction of the forest); limit (px) = edge of the light-travel bubble: rays stop there unlit."""
    global FOREST9
    if FOREST9 is None: FOREST9 = _forest9()
    cx, cy = W * 0.40, H * 0.52
    reach = lerp(v.get("r0", 120), v.get("r1", 1300), easeio((t - 0.3) / max(1.0, dur * 0.7)))
    limit = v.get("limit")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    sx, sy, sr = FOREST9[:, 0], FOREST9[:, 1], FOREST9[:, 2]
    dist = np.hypot(sx, sy)
    nray, hits = 180, 0
    for k in range(nray):
        a = 2 * math.pi * k / nray; ux, uy = math.cos(a), math.sin(a)
        proj = sx * ux + sy * uy; perp = np.abs(-sx * uy + sy * ux)
        ok = (proj > 0) & (perp < sr)
        tt = np.where(ok, proj - np.sqrt(np.maximum(0, sr ** 2 - perp ** 2)), 1e9)
        tmin = float(tt.min()); L = min(reach, limit or 1e9)
        hit = tmin <= L
        end = tmin if hit else L
        col = (255, 236, 170, 120) if hit else (120, 130, 170, 60)
        d.line([(cx, cy), (cx + ux * end, cy + uy * end)], fill=col, width=2)
        hits += hit
    img.alpha_composite(lay)
    d = ImageDraw.Draw(img)
    vis_r = min(reach, limit or 1e9)
    for (x, y, r), dd in zip(FOREST9, dist):
        X, Y = cx + x, cy + y
        if -40 < X < W + 40 and -40 < Y < H + 40:
            lit = dd <= vis_r + r
            c = (255, 230, 160) if lit else (70, 76, 100)
            d.ellipse([X - r, Y - r, X + r, Y + r], fill=c)
    if limit:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for k in range(0, 360, 6):
            dl.arc([cx - limit, cy - limit, cx + limit, cy + limit], k, k + 3, fill=MW9 + (220,), width=4)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.text((cx, cy - limit - 30), v.get("limit_label", "light has had time to reach us"), font=F(34, "Bold"), fill=MW9, anchor="mm")
    paste_c(img, earth_sprite(16, glow=None), cx, cy)
    d.text((cx, cy + 40), "you", font=F(32, "Bold"), fill=WHITE, anchor="mm")
    frac = hits / nray
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1330, 300, 1840, 640], 26, fill=(8, 8, 26, 220), outline=STAR9 + (110,), width=2); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((1585, 360), v.get("head", "Lines of sight"), font=F(40, "ExtraBold"), fill=STAR9, anchor="mm")
    d.text((1585, 470), f"{frac * 100:.0f}%", font=F(110, "Black"), fill=mix(WHITE, (255, 214, 120), frac), anchor="mm")
    d.text((1585, 580), "end on a star", font=F(36, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5))

def sc_blaze(img, v, t, dur):
    """a night horizon whose sky fills with star discs until it is a white wall; counter of Suns needed to tile the sky"""
    p = easeio((t - 0.3) / max(1.0, dur * v.get("speed", 0.75)))
    if v.get("reverse"): p = 1 - p
    rng = random.Random(19); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    n = int(40 + 2600 * p ** 2)
    for i in range(n):
        x, y = rng.uniform(0, W), rng.uniform(0, 820); r = rng.uniform(2, 5) + 70 * p ** 3 * rng.random()
        c = mix((255, 236, 200), (255, 250, 240), rng.random())
        d.ellipse([x - r, y - r, x + r, y + r], fill=c + (int(120 + 135 * p),))
    img.alpha_composite(lay)
    wash = Image.new("RGBA", img.size, (255, 246, 228, int(235 * max(0, p - 0.55) / 0.45)) if p > 0.55 else (0, 0, 0, 0)); img.alpha_composite(wash)
    d = ImageDraw.Draw(img)
    pts = [(0, H)] + [(x, 850 - 60 * math.sin(x / 300 + 0.6) - 25 * math.sin(x / 83)) for x in range(0, W + 40, 40)] + [(W, H)]
    d.polygon(pts, fill=mix((8, 9, 18), (60, 40, 30), p))
    for tx in (300, 360, 1500):
        d.polygon([(tx, 860), (tx - 26, 860), (tx - 13, 760)], fill=mix((6, 6, 12), (30, 20, 16), p))
    if v.get("count"):
        val = v["count"] * p
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([W / 2 - 430, 330, W / 2 + 430, 620], 30, fill=(6, 6, 20, 225)); img.alpha_composite(lay)
        d = ImageDraw.Draw(img)
        d.text((W / 2, 440), f"{val:,.0f}", font=F(150, "Black"), fill=(255, 200, 90), anchor="mm")
        d.text((W / 2, 560), v.get("unit", "Suns to tile the sky above you"), font=F(40, "Bold"), fill=WHITE, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 190), v["head"], F(70, "Black"), WHITE if p < 0.6 else (40, 30, 30), ease(t / 0.5), shadow=p < 0.6)
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_suspects(img, v, t, dur):
    """case board: suspect cards; 'focus' glows, 'cleared' get a stamp CLEARED, 'guilty' a red stamp GUILTY"""
    items = v["items"]; n = len(items); cw, ch, gap = 400, 520, 36
    x0 = W / 2 - (n * cw + (n - 1) * gap) / 2; y0 = 300
    alpha_text(img, (W / 2, 170), v.get("title", "THE SUSPECTS"), F(72, "Black"), STAR9, ease(t / 0.5))
    foc = v.get("focus", -1); cleared = v.get("cleared", []); guilty = v.get("guilty", []); new = v.get("new", [])
    for i, (num, name, note) in enumerate(items):
        a = ease((t - 0.2 - i * 0.25) / 0.5)
        if a <= 0: continue
        x = x0 + i * (cw + gap); lift = -24 * ease((t - 0.6) / 0.5) if i == foc else 0
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        oc = (255, 214, 120) if i == foc else (110, 118, 160)
        if i == foc:
            d.rounded_rectangle([x - 10, y0 - 10 + lift, x + cw + 10, y0 + ch + 10 + lift], 30, fill=(255, 214, 120, int(50 * a)))
        d.rounded_rectangle([x, y0 + lift, x + cw, y0 + ch + lift], 24, fill=(14, 14, 34, int(235 * a)), outline=oc + (int(255 * a),), width=4)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.text((x + cw / 2, y0 + 80 + lift), num, font=F(110, "Black"), fill=oc, anchor="mm")
        f = F(46, "ExtraBold"); words = name.split(); lines, cur = [], ""
        for w_ in words:
            tt = (cur + " " + w_).strip()
            if f.getlength(tt) < cw - 50: cur = tt
            else: lines.append(cur); cur = w_
        lines.append(cur)
        for k, l in enumerate(lines): d.text((x + cw / 2, y0 + 210 + k * 58 + lift), l, font=f, fill=WHITE, anchor="mm")
        stamp = "CLEARED" if i in cleared else ("GUILTY" if i in guilty else None)
        if not stamp: d.text((x + cw / 2, y0 + ch - 60 + lift), note, font=F(30, "SemiBold"), fill=DIM, anchor="mm")
        if stamp:
            sa = 1.0 if i not in new else ease((t - 1.2) / 0.3)
            if sa > 0:
                col = (120, 220, 150) if stamp == "CLEARED" else IR9
                s = Image.new("RGBA", (380, 120), (0, 0, 0, 0)); ds = ImageDraw.Draw(s)
                ds.rounded_rectangle([4, 4, 376, 116], 14, outline=col + (int(255 * sa),), width=8)
                ds.text((190, 62), stamp, font=F(70, "Black"), fill=col + (int(255 * sa),), anchor="mm")
                s = s.rotate(-14, expand=True, resample=Image.BICUBIC)
                k = 1 + 0.6 * (1 - sa); s = s.resize((int(s.width * k), int(s.height * k)))
                img.alpha_composite(s, (int(x + cw / 2 - s.width / 2), int(y0 + ch * 0.80 - s.height / 2 + lift)))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5))

def sc_shells(img, v, t, dur):
    """onion shells around you: shell k has k² stars, each 1/k² as bright -> equal light per shell; stacked light bars at right"""
    cx, cy = 620, H / 2 + 20; n = v.get("n", 5); d = ImageDraw.Draw(img)
    per = max(0.8, dur * 0.7) / n
    for k in range(1, n + 1):
        a = ease((t - 0.3 - (k - 1) * per) / 0.5)
        if a <= 0: continue
        R_ = 80 * k
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.ellipse([cx - R_, cy - R_, cx + R_, cy + R_], outline=INK9 + (int(150 * a),), width=3)
        m = 6 * k * k if k < 4 else 6 * k * k
        rng = random.Random(k)
        bright = 1.0 / (k * k)
        for j in range(min(m, 160)):
            ang = 2 * math.pi * (j + rng.random() * 0.5) / min(m, 160)
            x, y = cx + R_ * math.cos(ang), cy + R_ * math.sin(ang)
            r = max(1.6, 9 / k); c = mix((60, 60, 90), (255, 236, 180), 0.35 + 0.65 * bright ** 0.5)
            dl.ellipse([x - r, y - r, x + r, y + r], fill=c + (int(255 * a),))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        # bar
        bx, by = 1180, 860 - (k - 1) * 120
        d.rounded_rectangle([bx, by - 46, bx + 560 * a, by + 46], 16, fill=mix((40, 40, 70), (255, 214, 120), 0.4 + 0.12 * k))
        d.text((bx + 20, by), f"shell {k}:  {k*k}× stars  ·  1/{k*k} as bright", font=F(32, "Bold"), fill=(20, 16, 30), anchor="lm")
    paste_c(img, earth_sprite(14, glow=None), cx, cy)
    d = ImageDraw.Draw(img)
    d.text((1460, 200), v.get("head", "Every shell adds the same light"), font=F(48, "ExtraBold"), fill=STAR9, anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_lightbubble(img, v, t, dur):
    """the light-travel bubble grows with a cosmic clock; galaxies inside are lit, outside are grey outlines (light still on its way)"""
    cx, cy = W * 0.42, H * 0.53
    p = easeio((t - 0.3) / max(1.0, dur * 0.7))
    yrs = lerp(v.get("y0", 0.0), v.get("y1", 13.8), p)
    Rb = 470 * yrs / 13.8
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    if Rb > 2:
        for k in range(10, 0, -1):
            rr = Rb * k / 10; dl.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=INK9 + (int(10 + 3 * (10 - k)),))
        dl.ellipse([cx - Rb, cy - Rb, cx + Rb, cy + Rb], outline=MW9 + (230,), width=4)
    img.alpha_composite(lay)
    rng = random.Random(41); d = ImageDraw.Draw(img)
    for i in range(170):
        a = rng.uniform(0, 2 * math.pi); r = 30 + 900 * math.sqrt(rng.random()); x, y = cx + r * math.cos(a), cy + r * 0.62 * math.sin(a) * 1.4
        if not (0 < x < W - 560 and 120 < y < H - 160): continue
        ang = rng.uniform(0, math.pi); s = rng.uniform(8, 18)
        inside = math.hypot(x - cx, y - cy) < Rb
        col = mix((255, 220, 170), (170, 190, 255), rng.random()) if inside else (60, 64, 88)
        bb = [x - s, y - s * 0.4, x + s, y + s * 0.4]
        if inside: d.ellipse(bb, fill=col)
        else: d.ellipse(bb, outline=col, width=2)
    paste_c(img, earth_sprite(12, glow=None), cx, cy)
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1380, 280, 1860, 640], 26, fill=(8, 10, 26, 225), outline=MW9 + (120,), width=2); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((1620, 340), v.get("head", "Time since the beginning"), font=F(34, "Bold"), fill=DIM, anchor="mm")
    d.text((1620, 450), f"{yrs:.1f}", font=F(120, "Black"), fill=MW9, anchor="mm")
    d.text((1620, 560), "billion years", font=F(44, "ExtraBold"), fill=WHITE, anchor="mm")
    d.text((1620, 720), "lit = its light has reached us", font=F(30, "SemiBold"), fill=(255, 220, 170), anchor="mm")
    d.text((1620, 770), "grey = light still on its way", font=F(30, "SemiBold"), fill=(130, 136, 165), anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

BANDS9 = [("ULTRAVIOLET", (170, 110, 255)), ("VISIBLE", (255, 255, 255)), ("INFRARED", IR9), ("MICROWAVE", MW9)]
def sc_stretchwave(img, v, t, dur):
    """a light wave stretching as space expands: wavelength slides across UV->visible->IR->microwave; temperature or stretch counter"""
    p = easeio((t - 0.3) / max(1.0, dur * 0.75))
    s0, s1 = v.get("s0", 0.3), v.get("s1", 3.6)
    s = lerp(s0, s1, p)                      # position on the band ruler 0..4
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x0, x1, by = 160, W - 160, 830; bw = (x1 - x0) / 4
    for i, (name, col) in enumerate(BANDS9):
        d.rectangle([x0 + i * bw, by, x0 + (i + 1) * bw - 6, by + 70], fill=col + (70,))
        if name == "VISIBLE":
            for k in range(60):
                c = [(130, 80, 255), (60, 140, 255), (60, 220, 120), (255, 230, 60), (255, 140, 40), (255, 50, 50)]
                q = k / 59 * 5; c0 = c[int(q)]; c1 = c[min(5, int(q) + 1)]
                d.rectangle([x0 + i * bw + k * (bw - 6) / 60, by, x0 + i * bw + (k + 1) * (bw - 6) / 60, by + 70], fill=mix(c0, c1, q % 1) + (200,))
        d.text((x0 + (i + 0.5) * bw, by + 110), name, font=F(34, "ExtraBold"), fill=col + (255,), anchor="mm")
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    mx = x0 + s * bw
    d.polygon([(mx, by - 6), (mx - 22, by - 44), (mx + 22, by - 44)], fill=WHITE)
    band = min(3, int(s)); col = BANDS9[band][1] if band != 1 else (255, 240, 200)
    if band == 1:
        q = (s - 1) * 5; cs = [(130, 80, 255), (60, 140, 255), (60, 220, 120), (255, 230, 60), (255, 140, 40), (255, 50, 50)]
        col = mix(cs[min(5, int(q))], cs[min(5, int(q) + 1)], q % 1)
    lam = 40 * 4.0 ** s / 4.0 ** s0 * (1 if s < 3 else 1) ; lam = min(lam, 1400)
    pts = []; ph = t * 4
    for x in range(160, W - 160, 4):
        pts.append((x, 470 + 150 * math.sin(2 * math.pi * (x - 160) / lam - ph)))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.line(pts, fill=col + (90,), width=18); dl.line(pts, fill=col + (255,), width=6)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    if v.get("temp"):
        T = v["temp"][0] * (v["temp"][1] / v["temp"][0]) ** p
        d.text((W / 2, 200), (f"{T:,.0f} K" if T > 20 else f"{T:.1f} K"), font=F(120, "Black"), fill=col, anchor="mm")
        d.text((W / 2, 290), v.get("sub", "temperature of the glow"), font=F(40, "SemiBold"), fill=DIM, anchor="mm")
    else:
        alpha_text(img, (W / 2, 210), v.get("head", "Space stretches the light"), F(70, "Black"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 70)

# ---------------- scenes (EP10: Jupiter becomes a star) ----------------
OCH10, EMB10, LIME10 = (232, 176, 106), (255, 92, 56), (190, 240, 110)
JBANDS10 = [(-1.0, (196, 170, 140)), (-0.62, (222, 205, 178)), (-0.45, (176, 128, 96)), (-0.28, (232, 220, 196)), (-0.1, (190, 150, 115)),
            (0.08, (236, 226, 204)), (0.22, (170, 120, 90)), (0.4, (225, 210, 185)), (0.58, (186, 150, 120)), (0.78, (214, 196, 170))]
_jup10 = {}
def jup10(r, s=0.0):
    """banded Jupiter that turns into a red dwarf: s=0 planet, ~0.4 brown dwarf (dim magenta glow), 1 = red star"""
    r = max(3, int(r)); s = round(max(0.0, min(1.0, s)) * 20) / 20; key = (r, s)
    if key in _jup10: return _jup10[key]
    pad = int(r * 0.9) + 6; size = 2 * r + 2 * pad
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    nx, ny = (xx - size / 2) / r, (yy - size / 2) / r; rr = nx ** 2 + ny ** 2; dd = np.sqrt(rr); inside = rr <= 1
    lat = np.clip(ny, -1, 1); rgb = np.zeros((size, size, 3), np.float32)
    for i, (l0, col) in enumerate(JBANDS10):
        l1 = JBANDS10[i + 1][0] if i + 1 < len(JBANDS10) else 1.01
        rgb[(lat >= l0) & (lat < l1)] = col
    wav = np.sin(nx * 9 + ny * 31) * 10; rgb += wav[..., None]
    nz = np.sqrt(np.clip(1 - rr, 0, 1))
    shade = np.clip((nx * -0.8 + ny * -0.3 + nz * 0.5) / 1.0, 0, 1) * 0.85 + 0.15
    planet = rgb * shade[..., None]
    limb = (0.35 + 0.65 * nz)[..., None]
    star = np.array([255, 120, 70], np.float32) * limb + np.array([255, 220, 160], np.float32) * (nz[..., None] ** 3) * 0.6
    star += wav[..., None] * 0.6
    brown = np.array([150, 60, 80], np.float32) * (0.5 + 0.5 * nz[..., None]) + rgb * 0.15
    if s <= 0.4: body = planet * (1 - s / 0.4) + brown * (s / 0.4)
    else: body = brown * (1 - (s - 0.4) / 0.6) + star * ((s - 0.4) / 0.6)
    a = np.where(inside, 255, 0).astype(np.float32)
    if s > 0.2:
        gl = np.clip(1 - (dd - 1) / 0.85, 0, 1) ** 2 * (dd > 1) * (s - 0.2) / 0.8
        gcol = np.array([255, 90, 50], np.float32)
        body = np.where((dd > 1)[..., None], gcol, body); a = np.maximum(a, gl * 230)
    img = Image.fromarray(np.dstack([np.clip(body, 0, 255), a]).astype(np.uint8), "RGBA")
    _jup10[key] = img; return img

def stage10(M):
    """radius (× Jupiter) and look for a body of M Jupiter masses (rough: max size near 3 MJ, ~0.84 at the hydrogen limit)"""
    R = 1.0 + 0.05 * min(1, (M - 1) / 2) if M < 3 else 1.05 - 0.21 * (math.log(M / 3) / math.log(80 / 3))
    if M < 13: s, lab = 0.0, "GAS GIANT"
    elif M < 75: s, lab = 0.25 + 0.15 * (M - 13) / 62, "BROWN DWARF"
    else: s, lab = 0.4 + 0.6 * min(1, (M - 75) / 5), "RED DWARF STAR"
    return R, s, lab

def dash_circle10(d, cx, cy, r, col, w=3, step=7):
    for k in range(0, 360, step): d.arc([cx - r, cy - r, cx + r, cy + r], k, k + step * 0.55, fill=col, width=w)

def sc_massdial(img, v, t, dur):
    """gauge of mass (log 1..100 Jupiters, marks at 13 and 80) + the body: size barely changes, colour turns brown dwarf -> red star"""
    p = easeio((t - 0.3) / max(1.0, dur * v.get("speed", 0.7)))
    M = math.exp(lerp(math.log(v.get("m0", 1)), math.log(v.get("m1", 80)), p))
    gx, gy, gr = 560, 610, 330
    d = ImageDraw.Draw(img)
    def ang(m): return math.radians(160 + 220 * math.log10(m) / 2)
    d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 160, 380, fill=(60, 64, 90), width=26)
    for m0, m1, c in [(1, 13, OCH10), (13, 75, (180, 80, 120)), (75, 100, EMB10)]:
        a0, a1 = math.degrees(ang(m0)), math.degrees(ang(min(M, m1)))
        if M > m0: d.arc([gx - gr, gy - gr, gx + gr, gy + gr], a0, a1, fill=c, width=26)
    for m, lab in [(1, "1"), (13, "13"), (80, "80"), (100, "100")]:
        a = ang(m); x0, y0 = gx + (gr + 22) * math.cos(a), gy + (gr + 22) * math.sin(a)
        d.line([(gx + (gr - 20) * math.cos(a), gy + (gr - 20) * math.sin(a)), (x0, y0)], fill=WHITE, width=4)
        d.text((gx + (gr + 62) * math.cos(a), gy + (gr + 62) * math.sin(a)), lab, font=F(38, "Bold"), fill=WHITE, anchor="mm")
    a = ang(M); d.line([(gx, gy), (gx + (gr - 50) * math.cos(a), gy + (gr - 50) * math.sin(a))], fill=LIME10, width=10)
    d.ellipse([gx - 22, gy - 22, gx + 22, gy + 22], fill=LIME10)
    d.text((gx, gy + 110), f"{M:,.0f}" if M >= 10 else f"{M:,.1f}", font=F(140, "Black"), fill=WHITE, anchor="mm")
    d.text((gx, gy + 210), "Jupiter masses", font=F(40, "SemiBold"), fill=DIM, anchor="mm")
    Rx, s, lab = stage10(M)
    bx, by, R0 = 1400, 470, 220
    paste_c(img, jup10(R0 * Rx, s), bx, by)
    d = ImageDraw.Draw(img); dash_circle10(d, bx, by, R0, (200, 205, 230), 3)
    d.text((bx, by - R0 - 50), "dashed = Jupiter today", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    col = OCH10 if M < 13 else ((220, 120, 170) if M < 75 else EMB10)
    d.text((bx, by + R0 + 75), lab, font=F(62, "Black"), fill=col, anchor="mm")
    d.text((bx, by + R0 + 140), f"size: {Rx:.2f} × Jupiter", font=F(40, "SemiBold"), fill=WHITE, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 1.5) / 0.5))

def sc_sizeup(img, v, t, dur):
    """to scale: Jupiter, the smallest known star (EBLM J0555-57Ab) and Saturn, with the Sun's edge as a giant arc"""
    k = 215 / 71492; cy = 450
    sun_r = 696000 * k
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    sx = W + sun_r - 170 + (1 - ease(t / 1.2)) * 300
    dl.ellipse([sx - sun_r, cy - sun_r, sx + sun_r, cy + sun_r], fill=(255, 190, 80, 255))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3)))
    alpha_text(img, (W - 25, 150), "the Sun", F(40, "Bold"), (60, 30, 0), ease((t - 0.5) / 0.5), anchor="rm", shadow=False)
    items = [("Jupiter", 71492, 0.0, "1 Jupiter mass", OCH10), ("smallest known star", 60000, 1.0, "≈ 85 Jupiter masses", EMB10), ("Saturn", 58232, -1, "0.3 Jupiter masses", (225, 205, 150))]
    xs = [330, 860, 1330]
    for i, (nm, km, s, mass, col) in enumerate(items):
        a = ease((t - 0.4 - i * 0.9) / 0.6)
        if a <= 0: continue
        r = km * k; x = xs[i]
        if s >= 0: paste_c(img, jup10(r, s), x, cy, a)
        else: paste_c(img, planet_sprite(int(r), (225, 205, 150), light=(-0.8, -0.4)), x, cy, a)
        alpha_text(img, (x, cy + 215 + 55), nm, F(44, "ExtraBold"), col, a)
        alpha_text(img, (x, cy + 215 + 112), mass, F(36, "SemiBold"), WHITE, a)
        alpha_text(img, (x, cy + 215 + 160), f"{2 * km:,} km wide", F(32, "Medium"), DIM, a)
    if t > 3.2:
        d = ImageDraw.Draw(img); dash_circle10(d, 860, cy, 71492 * k, (200, 205, 230), 3)
    caption(img, v.get("caption"), ease((t - 3.5) / 0.5))

def sc_massbudget(img, v, t, dur):
    """mode 'planets': Jupiter vs all other planets (Earth masses). mode 'grid': 80 cells = mass needed; 1 = Jupiter, 0.4 = rest of the solar system"""
    d = ImageDraw.Draw(img)
    if v.get("mode") == "planets":
        alpha_text(img, (160, 200), v.get("head", "Mass, in Earths"), F(66, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
        rows = [("Jupiter", 317.8, OCH10), ("all other planets combined", 128.8, LIME10)]
        for i, (lab, val, col) in enumerate(rows):
            p = ease((t - 0.6 - i * 1.2) / 1.2); y = 430 + i * 250
            d.text((160, y - 70), lab, font=F(46, "Bold"), fill=mix(SPACE, WHITE, min(1, p * 3)), anchor="lm")
            bw = 1450 * val / 317.8 * p
            d.rounded_rectangle([160, y - 34, 160 + max(6, bw), y + 50], 18, fill=col)
            if p > 0.05: d.text((160 + max(6, bw) + 26, y + 8), f"{val * p:.0f} Earths", font=F(54, "Black"), fill=WHITE, anchor="lm")
        caption(img, v.get("caption"), ease((t - 3.0) / 0.5)); return
    cols, rows, cs, gap = 16, 5, 92, 10
    x0 = W / 2 - (cols * (cs + gap) - gap) / 2; y0 = 300
    alpha_text(img, (W / 2, 175), v.get("head", "80 Jupiters needed"), F(66, "ExtraBold"), WHITE, ease(t / 0.5))
    fill_p = ease((t - 0.8) / 1.0); rest_p = ease((t - 2.0) / 1.0); out_p = easeio((t - 3.4) / max(1.0, dur - 5.0)) if v.get("import") else 0
    for k in range(80):
        cx, cy = x0 + (k % cols) * (cs + gap), y0 + (k // cols) * (cs + gap)
        d.rounded_rectangle([cx, cy, cx + cs, cy + cs], 14, outline=(80, 86, 120), width=3)
        if k == 0 and fill_p > 0: d.rounded_rectangle([cx, cy, cx + cs, cy + cs], 14, fill=mix(SPACE, OCH10, fill_p))
        if k == 1 and rest_p > 0: d.rounded_rectangle([cx, cy, cx + max(8, cs * 0.405 * rest_p), cy + cs], 10, fill=LIME10)
        if k >= 2 and out_p * 78 > k - 2: d.rounded_rectangle([cx + 8, cy + 8, cx + cs - 8, cy + cs - 8], 10, fill=(150, 90, 200))
    yl = y0 + rows * (cs + gap) + 50
    for i, (lab, col) in enumerate([("Jupiter", OCH10), ("everything else in the solar system: 0.4", LIME10), ("needed from outside: about 79", (150, 90, 200))]):
        a = ease((t - 0.8 - i * 1.2) / 0.5)
        if a > 0:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            dl.rounded_rectangle([200, yl + i * 70 - 18, 236, yl + i * 70 + 18], 8, fill=col + (int(255 * a),))
            dl.text((262, yl + i * 70), lab, font=F(40, "SemiBold"), fill=WHITE + (int(255 * a),), anchor="lm"); img.alpha_composite(lay)
    caption(img, v.get("caption"), ease((t - 4.0) / 0.5))

def sc_twosuns(img, v, t, dur):
    """Earth's night landscape with Jupiter-star as a red point (spikes + glow) casting faint red shadows; magnitude meter (log)"""
    p = ease((t - 0.2) / max(1.0, dur * 0.5)); day = v.get("day", False)
    if day:
        sky = Image.new("RGBA", img.size, (90, 150, 220, 255)); img.alpha_composite(sky)
    else:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); g = np.zeros((H, W, 4), np.uint8); yy = np.linspace(0, 1, H)[:, None]
        g[..., 0] = 120; g[..., 1] = 20; g[..., 2] = 20; g[..., 3] = (np.clip(yy - 0.25, 0, 1) * 110 * p).astype(np.uint8)
        img.alpha_composite(Image.fromarray(g, "RGBA"))
    sx, sy = lerp(1180, 1240, p), lerp(820, 300, p)
    glow = radial(520, [(0, (255, 130, 90, 255)), (0.06, (255, 110, 70, 230)), (0.25, (255, 80, 50, 70)), (1, (255, 60, 40, 0))])
    paste_c(img, glow, sx, sy, 0.6 if day else 1.0)
    d = ImageDraw.Draw(img)
    for ang in (0, 90):
        a = math.radians(ang); L = 120
        d.line([(sx - L * math.cos(a), sy - L * math.sin(a)), (sx + L * math.cos(a), sy + L * math.sin(a))], fill=(255, 200, 170), width=3)
    d.ellipse([sx - 7, sy - 7, sx + 7, sy + 7], fill=(255, 240, 225))
    if day: paste_c(img, sun_sprite(60), 330, 220)
    gcol = (30, 34, 28) if day else mix((8, 8, 14), (40, 10, 12), p)
    pts = [(0, H)] + [(x, 880 - 40 * math.sin(x / 260 + 1.0) - 18 * math.sin(x / 71)) for x in range(0, W + 40, 40)] + [(W, H)]
    d.polygon(pts, fill=gcol)
    tx, ty = 620, 870
    d.rectangle([tx - 10, ty - 60, tx + 10, ty], fill=(4, 4, 8))
    for j in range(5): w_ = 95 - j * 17; y_ = ty - 50 - j * 55; d.polygon([(tx - w_, y_), (tx + w_, y_), (tx, y_ - 110)], fill=(4, 4, 8))
    if not day and p > 0.3:
        sl = Image.new("RGBA", img.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(sl)
        L = 260 * (1 - (820 - sy) / 520) + 90
        ds.polygon([(tx - 10, ty), (tx + 10, ty), (tx - 10 - L, ty + 60), (tx - 50 - L, ty + 60)], fill=(0, 0, 0, int(170 * p)))
        img.alpha_composite(sl); d = ImageDraw.Draw(img)
    d.text((sx - 40, sy + 70), "Jupiter, as a star", font=F(36, "Bold"), fill=(255, 190, 160), anchor="rm")
    if v.get("meter", True):
        mx, my0, my1 = 1700, 170, 820
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([mx - 210, my0 - 70, mx + 200, my1 + 60], 24, fill=(8, 8, 20, 210)); img.alpha_composite(box)
        d = ImageDraw.Draw(img)
        d.text((mx - 5, my0 - 30), "brightness", font=F(30, "Bold"), fill=DIM, anchor="mm")
        def my(mag): return lerp(my1, my0, (-mag - 0) / 27)
        d.line([(mx - 120, my0), (mx - 120, my1)], fill=(90, 96, 130), width=6)
        for mag, lab, col in [(-26.7, "Sun", (255, 210, 110)), (-13.6, "Jupiter-star", EMB10), (-12.7, "full Moon", (220, 220, 230)), (-4.6, "Venus", (240, 230, 200)), (-2.9, "Jupiter now", OCH10)]:
            if lab == "Jupiter-star" and p < 0.6: continue
            yy_ = my(mag) + (14 if lab == "full Moon" else (-14 if lab == "Jupiter-star" else 0))
            d.ellipse([mx - 132, my(mag) - 12, mx - 108, my(mag) + 12], fill=col)
            d.text((mx - 90, yy_), lab, font=F(28, "Bold"), fill=col, anchor="lm")
    if v.get("head"): alpha_text(img, (W / 2 - 200, 120), v["head"], F(58, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5))

def sc_barywobble(img, v, t, dur):
    """mode 'wobble': left = whole system (Sun + Jupiter-star around the barycentre); right = zoom with Mercury's orbit and the Sun's loop
    (mass grows 1 -> 80 Jupiters during the scene). mode 'zones': stable zone (≈2.1 AU, Holman & Wiegert rule) vs chaos."""
    if v.get("mode") == "zones":
        cx, cy, k = 640, 560, 46
        d = ImageDraw.Draw(img); p = ease((t - 0.5) / 1.5)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        rs = 2.12 * k; dl.ellipse([cx - rs, cy - rs, cx + rs, cy + rs], fill=LIME10 + (int(60 * p),), outline=LIME10 + (int(220 * p),), width=3)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        for au, nm, col in [(0.387, "", (170, 160, 150)), (0.723, "", (230, 200, 140)), (1.0, "Earth", (90, 150, 240)), (1.524, "Mars", (210, 100, 70))]:
            r = au * k; d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=2)
            ang = t * 0.9 / au ** 1.5 + au * 5; px, py = cx + r * math.cos(ang), cy + r * math.sin(ang)
            d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=col)
        rng = random.Random(4)
        for i in range(260):
            r = rng.uniform(2.2, 3.3) * k; a0 = rng.uniform(0, 6.28) + t * 0.15; jit = 14 * p * math.sin(t * 3 + i)
            x, y = cx + (r + jit) * math.cos(a0), cy + (r + jit) * math.sin(a0); d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(150, 140, 130))
        paste_c(img, sun_sprite(10), cx, cy)
        ja = t * 0.12; jx, jy = cx + 5.2 * k * math.cos(ja), cy + 5.2 * k * math.sin(ja)
        d.ellipse([cx - 5.2 * k, cy - 5.2 * k, cx + 5.2 * k, cy + 5.2 * k], outline=(255, 120, 90), width=2)
        paste_c(img, jup10(16, 1.0), jx, jy)
        sr = 9.54 * k; d = ImageDraw.Draw(img)
        for kk in range(0, 360, 5): d.arc([cx - sr, cy - sr, cx + sr, cy + sr], kk, kk + 2, fill=(255, 90, 90), width=3)
        sa = 2.2 + t * 0.05 + 0.25 * p * math.sin(t * 2); sxp, syp = cx + sr * math.cos(sa), cy + sr * math.sin(sa)
        paste_c(img, planet_sprite(12, (225, 205, 150)), sxp, syp)
        d = ImageDraw.Draw(img)
        d.text((sxp - 30, syp + 40), "Saturn", font=F(30, "Bold"), fill=(255, 140, 120), anchor="mm")
        bx = 1500
        for i, (head, body, col) in enumerate([("STABLE (≈ 2 AU)", "Mercury, Venus, Earth, Mars", LIME10), ("CHAOS", "the asteroid belt", (200, 180, 150)), ("DANGER", "Saturn, Uranus, Neptune", (255, 110, 100))]):
            a = ease((t - 0.8 - i * 1.0) / 0.5)
            alpha_text(img, (bx, 330 + i * 190), head, F(54, "Black"), col, a)
            alpha_text(img, (bx, 395 + i * 190), body, F(36, "SemiBold"), WHITE, a)
        caption(img, v.get("caption"), ease((t - 3.0) / 0.5)); return
    p = easeio((t - 0.4) / max(1.0, dur * 0.6))
    M = math.exp(lerp(0, math.log(80), p)); mu = M * 0.000954 / (1 + M * 0.000954)
    ang = t * 0.35
    cx, cy, k = 450, 540, 70
    d = ImageDraw.Draw(img)
    d.ellipse([cx - 5.2 * k, cy - 5.2 * k, cx + 5.2 * k, cy + 5.2 * k], outline=(90, 70, 70), width=2)
    jx, jy = cx + 5.2 * k * (1 - mu) * math.cos(ang), cy + 5.2 * k * (1 - mu) * math.sin(ang)
    sxp, syp = cx - 5.2 * k * mu * math.cos(ang), cy - 5.2 * k * mu * math.sin(ang)
    paste_c(img, sun_sprite(12), sxp, syp); paste_c(img, jup10(14 + 6 * p, stage10(M)[1]), jx, jy)
    d = ImageDraw.Draw(img); d.line([(cx - 8, cy), (cx + 8, cy)], fill=LIME10, width=3); d.line([(cx, cy - 8), (cx, cy + 8)], fill=LIME10, width=3)
    d.text((cx, 130), f"Jupiter: {M:,.0f}× its mass", font=F(44, "Bold"), fill=WHITE, anchor="mm")
    zx, zy, zk = 1460, 520, 780
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([zx - 400, zy - 380, zx + 400, zy + 380], 30, fill=(6, 8, 20, 200), outline=LIME10 + (140,), width=2); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    rm = 0.387 * zk; d.ellipse([zx - rm, zy - rm, zx + rm, zy + rm], outline=(170, 160, 150), width=2)
    d.text((zx, zy - rm + 34), "Mercury's orbit", font=F(28, "Bold"), fill=(190, 180, 170), anchor="mm")
    off = 5.2 * mu * zk
    for kk in range(0, 360, 6): d.arc([zx - off, zy - off, zx + off, zy + off], kk, kk + 3, fill=(255, 210, 120), width=2)
    paste_c(img, sun_sprite(int(max(4, 0.00465 * zk * 1.0)) + 6), zx - off * math.cos(ang), zy - off * math.sin(ang))
    d = ImageDraw.Draw(img); d.line([(zx - 10, zy), (zx + 10, zy)], fill=LIME10, width=3); d.line([(zx, zy - 10), (zx, zy + 10)], fill=LIME10, width=3)
    d.text((zx, zy + 330), f"balance point: {5.2 * mu:.2f} AU from the Sun", font=F(36, "ExtraBold"), fill=LIME10, anchor="mm")
    d.text((zx, zy - 360), "zoom: the inner solar system", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

MOONS10 = [("Io", 421700, (235, 210, 110)), ("Europa", 671034, (225, 215, 200)), ("Ganymede", 1070412, (170, 160, 150)), ("Callisto", 1882709, (120, 110, 100))]
def sc_moonfall(img, v, t, dur):
    """Galilean moons around a Jupiter whose mass grows: slow growth -> a ∝ 1/M (angular momentum conserved); square-root distance scale"""
    p = easeio((t - 0.5) / max(1.0, dur * 0.65))
    M = math.exp(lerp(math.log(v.get("m0", 1)), math.log(v.get("m1", 80)), p))
    cx, cy, kk = 760, 560, 470 / math.sqrt(1882709)
    def rp(km): return kk * math.sqrt(km)
    Rx, s, _ = stage10(M); star_km = 71492 * Rx
    d = ImageDraw.Draw(img)
    for nm, a0, col in MOONS10:
        a = a0 / M; r = rp(a)
        dash_circle10(d, cx, cy, rp(a0), (60, 64, 90), 2)
        if a > star_km:
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=2)
    paste_c(img, jup10(rp(star_km), s), cx, cy)
    d = ImageDraw.Draw(img)
    for i, (nm, a0, col) in enumerate(MOONS10):
        a = a0 / M; r = rp(a); per = (a0 / 421700) ** 1.5
        ang = t * 1.2 / per * (M ** 0.5) ** 0.3 + i * 1.6
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        if a > star_km:
            d.ellipse([x - 11, y - 11, x + 11, y + 11], fill=col); d.text((x + 18, y - 18), nm, font=F(28, "Bold"), fill=col, anchor="lm")
    bx = 1560
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([bx - 300, 190, bx + 300, 930], 26, fill=(8, 8, 22, 215)); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((bx, 250), f"mass × {M:,.0f}", font=F(60, "Black"), fill=LIME10, anchor="mm")
    d.text((bx, 320), f"star radius ≈ {star_km:,.0f} km", font=F(30, "SemiBold"), fill=(255, 170, 140), anchor="mm")
    for i, (nm, a0, col) in enumerate(MOONS10):
        a = a0 / M; y = 420 + i * 120; gone = a <= star_km
        d.text((bx - 260, y), nm, font=F(40, "ExtraBold"), fill=col, anchor="lm")
        d.text((bx + 260, y), "INSIDE" if gone else f"{a:,.0f} km", font=F(38, "Black" if gone else "Bold"), fill=EMB10 if gone else WHITE, anchor="rm")
    d.text((bx, 890), "distances: square-root scale", font=F(26, "Medium"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (cx, 110), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

# ---------------- scenes (EP11) ----------------
CREAM11, ROSE11, TEAL11 = (240, 226, 196), (240, 140, 160), (70, 200, 185)
# Saturn's main rings in Saturn radii (NASA ring fact sheet), scaled to Earth: (name, r_in, r_out, colour, opacity)
RINGS11 = [("C", 1.239, 1.527, (165, 152, 135), 0.38), ("B", 1.527, 1.951, (244, 230, 200), 0.95),
           ("Cassini Division", 1.951, 2.027, (110, 100, 90), 0.12), ("A", 2.027, 2.269, (222, 210, 186), 0.72)]
_rs11 = {}

def _v3dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def ring_layer11(lat, elev, fov, mode, shadow):
    """rings seen from the ground at latitude `lat`, facing the equator, camera tilted up `elev` degrees (gnomonic camera, cached)"""
    key = (lat, elev, fov, mode, shadow)
    if key in _rs11: return _rs11[key]
    phi, e = math.radians(abs(lat)), math.radians(elev)
    U = (math.cos(phi), 0.0, math.sin(phi)); S = (math.sin(phi), 0.0, -math.cos(phi))
    Fw = tuple(math.cos(e) * s + math.sin(e) * u for s, u in zip(S, U)); Cu = tuple(-math.sin(e) * s + math.cos(e) * u for s, u in zip(S, U))
    Rt = (0.0, -1.0, 0.0); f = (W / 2) / math.tan(math.radians(fov / 2))
    def proj(r, th):
        D = (r * math.cos(th) - U[0], r * math.sin(th) - U[1], -U[2])
        z = _v3dot(D, Fw)
        if z < 0.02: return None
        return (W / 2 + f * _v3dot(D, Rt) / z, H / 2 - f * _v3dot(D, Cu) / z)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    rng = random.Random(11); N = 900
    ths = [-math.pi + 2 * math.pi * k / N for k in range(N + 1)]
    for nm, r0, r1, col, op in RINGS11:
        nsub = 7
        for j in range(nsub):
            a_ = r0 + (r1 - r0) * j / nsub; b_ = r0 + (r1 - r0) * (j + 1) / nsub
            q = op * rng.uniform(0.7, 1.15)
            if mode == "day": c = mix((150, 185, 230), col, 0.55); al = int(255 * min(1, q * 0.75))
            else: c = col; al = int(255 * min(1, q))
            pa = [proj(a_, th) for th in ths]; pb = [proj(b_, th) for th in ths]
            for k in range(N):
                if None in (pa[k], pa[k + 1], pb[k], pb[k + 1]): continue
                th = ths[k]
                if max(abs(pa[k][0]), abs(pb[k][0])) > 4 * W or max(abs(pa[k][1]), abs(pb[k][1])) > 4 * H: continue
                cc, aa = c, al
                if shadow and math.cos(th) > 0 and abs(((a_ + b_) / 2) * math.sin(th)) < 1.0: cc, aa = mix(c, (40, 44, 70), 0.72), int(al * 0.7)
                d.polygon([pa[k], pa[k + 1], pb[k + 1], pb[k]], fill=cc + (aa,))
        for rr in (r0, r1):  # crisp edges (also makes the edge-on ring visible from the equator)
            pts = [p for p in (proj(rr, th) for th in ths) if p and abs(p[0]) < 4 * W and abs(p[1]) < 4 * H]
            if len(pts) > 1 and abs(lat) < 0.5: d.line(pts, fill=col + (240,), width=5)
    _rs11[key] = (lay, f)
    return _rs11[key]

def sky11(img, mode, hy):
    yy = np.linspace(0, 1, H)[:, None]
    g = np.zeros((H, W, 4), np.float32)
    if mode == "day":
        top, bot, al = np.array([40, 95, 190]), np.array([150, 195, 235]), 255
    elif mode == "dusk":
        top, bot, al = np.array([20, 24, 70]), np.array([235, 130, 90]), 235
    else:
        top, bot, al = np.array([4, 6, 20]), np.array([24, 30, 60]), 140
    k = np.clip(yy / max(1, hy / H), 0, 1) ** 1.6
    g[..., :3] = top[None, None, :] * (1 - k[..., None]) + bot[None, None, :] * k[..., None]
    g[..., 3] = al
    img.alpha_composite(Image.fromarray(np.clip(g, 0, 255).astype(np.uint8), "RGBA"))

_city11 = {}
def skyline11(img, hy, seed, mode, t):
    if seed not in _city11:
        rng = random.Random(seed); b = []; x = -20
        while x < W + 20:
            w_ = rng.uniform(30, 90); h_ = rng.choice([rng.uniform(20, 70), rng.uniform(60, 180)]); b.append((x, w_, h_)); x += w_ + rng.uniform(0, 14)
        _city11[seed] = b
    d = ImageDraw.Draw(img); gcol = (24, 40, 30) if mode == "day" else (8, 9, 16)
    pts = [(0, H)] + [(x, hy + 6 + 10 * math.sin(x / 210 + seed)) for x in range(0, W + 40, 40)] + [(W, H)]
    bcol = (40, 50, 64) if mode == "day" else (10, 11, 20)
    rng = random.Random(seed + 1)
    for x, w_, h_ in _city11[seed]:
        d.rectangle([x, hy - h_, x + w_, hy + 20], fill=bcol)
        if mode != "day":
            for wy in range(int(hy - h_ + 10), int(hy), 18):
                for wx in range(int(x + 6), int(x + w_ - 6), 14):
                    if rng.random() < 0.25: d.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 205, 120))
    d.polygon(pts, fill=gcol)

def sc_ringsky(img, v, t, dur):
    """ground view at latitude v.lat facing the equator: Saturn-scaled rings computed in 3D (gnomonic camera); mode day | night | dusk;
    shadow=True: Earth's shadow cuts a dark gap across the arch at midnight; v.city, v.head, v.caption"""
    lat = v.get("lat", 40.7); mode = v.get("mode", "night"); elev = v.get("elev", 30); fov = v.get("fov", 118)
    f = (W / 2) / math.tan(math.radians(fov / 2)); hy = H / 2 + f * math.tan(math.radians(elev))
    sky11(img, mode, hy)
    if mode == "day":
        alt = math.radians(90 - abs(lat)); e = math.radians(elev)
        z = math.cos(alt) * math.cos(e) + math.sin(alt) * math.sin(e); yv = math.sin(alt) * math.cos(e) - math.cos(alt) * math.sin(e)
        if z > 0.1:
            sx, sy = W / 2 + 260, H / 2 - f * yv / z
            if -100 < sy < H: paste_c(img, sun_sprite(46), sx, sy)
    lay, _ = ring_layer11(lat, elev, fov, mode, v.get("shadow", False))
    a = ease((t - 0.2) / 1.2); drift = 0
    if a > 0:
        l2 = lay if a >= 1 else Image.fromarray((np.asarray(lay) * np.array([1, 1, 1, a])).astype(np.uint8), "RGBA")
        img.alpha_composite(l2, (drift, 0)) if drift >= 0 else img.alpha_composite(l2.crop((-drift, 0, W, H)), (0, 0))
    if mode == "night" and v.get("glow", True):
        gl = Image.new("RGBA", img.size, (0, 0, 0, 0)); g = np.zeros((H, W, 4), np.uint8)
        yy = np.linspace(0, 1, H)[:, None]; g[..., 0] = 120; g[..., 1] = 115; g[..., 2] = 100
        g[..., 3] = (np.clip((yy - 0.45) * 1.8, 0, 1) * 40 * a).astype(np.uint8); img.alpha_composite(Image.fromarray(g, "RGBA"))
    skyline11(img, hy, int(abs(lat) * 7) + 3, mode, t)
    d = ImageDraw.Draw(img)
    toward = "SOUTH" if lat >= 0 else "NORTH"
    d.text((W / 2, min(H - 60, hy + 70)), f"looking {toward}", font=F(30, "Bold"), fill=(200, 205, 220), anchor="mm")
    d.text((60, min(H - 60, hy + 70)), "EAST" if lat >= 0 else "WEST", font=F(28, "Bold"), fill=DIM, anchor="lm")
    d.text((W - 60, min(H - 60, hy + 70)), "WEST" if lat >= 0 else "EAST", font=F(28, "Bold"), fill=DIM, anchor="rm")
    if v.get("city"):
        bx = 70; by = 150
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([bx - 20, by - 50, bx + 600, by + 170], 22, fill=(8, 10, 24, 200), outline=ROSE11 + (180,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img)
        d.text((bx, by - 2), v["city"], font=F(54, "Black"), fill=WHITE, anchor="lm")
        la = abs(lat); hem = "N" if lat >= 0 else "S"
        d.text((bx, by + 62), f"latitude {la:.0f}° {hem}", font=F(34, "Bold"), fill=ROSE11, anchor="lm")
        vis = [nm for nm, r0, r1, c, o in RINGS11 if nm != "Cassini Division" and la < math.degrees(math.acos(1 / r1))]
        full = [nm for nm, r0, r1, c, o in RINGS11 if nm != "Cassini Division" and la < math.degrees(math.acos(1 / r0))]
        txt = "rings: all visible" if len(full) == 3 else ("rings: hidden below the horizon" if not vis else "rings: only the outer part")
        if abs(lat) < 0.5: txt = "rings: edge-on, a thin line"
        alpha_text(img, (bx, by + 118), txt, F(32, "SemiBold"), CREAM11, ease((t - 1.0) / 0.5), anchor="lm")
    if v.get("head"): alpha_text(img, (W / 2, 70), v["head"], F(52, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 150)

def sc_orbitzones(img, v, t, dur):
    """top-down Earth TO SCALE with Saturn-scaled rings (7,900–14,500 km from the centre); scale animates fit0 -> fit1 (km at 440 px);
    show: list of 'rings', 'roche', 'iss', 'gps', 'geo', 'moon'"""
    p = easeio((t - 0.3) / max(1.0, dur * 0.5))
    fit = math.exp(lerp(math.log(v.get("fit0", 16000)), math.log(v.get("fit1", 16000)), p)); k = 440 / fit
    cx, cy = 640, 560; show = v.get("show", ["rings"]); d = ImageDraw.Draw(img)
    def circ(rkm, col, w=2, dash=False, label=None, ang=-0.5, a=1.0):
        r = rkm * k
        if a <= 0: return
        c = mix(SPACE, col, a)
        if dash: dash_circle10(d, cx, cy, r, c, w)
        else: d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=w)
        if label and r < 900:
            x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
            d.text((x + 10, y - 8), label, font=F(28, "Bold"), fill=c, anchor="lb")
    if "rings" in show:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for nm, r0, r1, col, op in RINGS11[::-1]:
            ro = r1 * 6371 * k
            dl.ellipse([cx - ro, cy - ro, cx + ro, cy + ro], fill=col + (int(220 * op),))
        ri = 1.239 * 6371 * k; dl.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=(0, 0, 0, 0))
        img.alpha_composite(lay)
        ri = 1.239 * 6371 * k
        hole = Image.new("L", img.size, 0); ImageDraw.Draw(hole).ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=255)
        img.paste(background(t).crop((0, 0, W, H)), (0, 0), hole)
    d = ImageDraw.Draw(img)
    paste_c(img, earth_sprite(max(4, int(6371 * k))), cx, cy)
    d = ImageDraw.Draw(img)
    items = []
    if "iss" in show: circ(6371 + 420, (120, 255, 170), 2, label=None); items.append(("ISS", "420 km up — below the rings", (120, 255, 170)))
    if "rings" in show: items.append(("RINGS", "1,500 to 8,100 km up", CREAM11))
    if "roche" in show:
        q = ease((t - 1.0) / 0.6)
        circ(19000, ROSE11, 3, dash=True, label="Roche limit, rock", ang=-2.5, a=q); circ(28400, (140, 200, 255), 3, dash=True, label="Roche limit, ice", ang=-0.6, a=q)
        items.append(("ROCHE LIMIT", "≈ 19,000–28,000 km from the centre", ROSE11))
    if "gps" in show: circ(26560, (255, 200, 90), 2, label="GPS", ang=0.6); items.append(("GPS", "20,200 km up — above the rings", (255, 200, 90)))
    if "geo" in show: circ(42164, (200, 150, 255), 2, label="geostationary", ang=0.9); items.append(("TV SATELLITES", "35,786 km up", (200, 150, 255)))
    if "moon" in show:
        mr = 384400 * k
        if mr < 1200: circ(384400, (200, 200, 210), 2)
        mx = min(cx + mr, W - 520); d.text((mx - 20, cy + 150), "Moon →" if cx + mr > W - 500 else "Moon", font=F(34, "Bold"), fill=(220, 220, 230), anchor="rm")
        items.append(("MOON", "384,400 km — far outside", (220, 220, 230)))
    bx = 1360
    for i, (h1, h2, col) in enumerate(items):
        a = ease((t - 0.5 - i * 0.7) / 0.5)
        alpha_text(img, (bx, 260 + i * 130), h1, F(46, "Black"), col, a, anchor="lm")
        alpha_text(img, (bx, 310 + i * 130), h2, F(30, "SemiBold"), WHITE, a, anchor="lm")
    d = ImageDraw.Draw(img)
    sb = 10000 * k
    if 40 < sb < 600:
        d.line([(90, 1010), (90 + sb, 1010)], fill=WHITE, width=3); d.text((90 + sb / 2, 985), "10,000 km", font=F(26, "Bold"), fill=WHITE, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 110), v["head"], F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5))

def sc_ringedge(img, v, t, dur):
    """side view of a ring zooming in (log): a hairline 273,000 km long becomes a band 10 m thick next to a 3-storey building;
    the field-of-view width counts down; optional paper analogy at the end"""
    p = easeio((t - 0.4) / max(1.0, dur * 0.7))
    z0, z1 = math.log(1700 / 2.8e8), math.log(1700 / 60.0)
    pxm = math.exp(lerp(z0, z1, p)); cy = 560; cx = W / 2
    d = ImageDraw.Draw(img)
    half = 1.365e8 * pxm
    th = max(1.5, 10 * pxm)
    x0, x1 = max(-10, cx - half), min(W + 10, cx + half)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rectangle([x0, cy - th / 2, x1, cy + th / 2], fill=CREAM11 + (110 if th > 6 else 255,))
    if pxm > 0.4:
        rng = random.Random(5)
        for i in range(900):
            s = 10 ** rng.uniform(-2, 0.7)
            r = max(0.8, s * pxm / 2)
            x = rng.uniform(0, W); y = cy + rng.uniform(-5, 5) * pxm
            sh = int(200 + 40 * rng.random())
            dl.ellipse([x - r, y - r * 0.8, x + r, y + r * 0.8], fill=(sh, sh - 8, sh - 25, 255))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    if half * 2 < W - 100:
        paste_c(img, planet_sprite(max(2, int(60268 * pxm * 1000)), (225, 205, 150)), cx, cy) if 60268e3 * pxm > 1 else None
        d.text((cx, cy + 60), "Saturn", font=F(30, "Bold"), fill=(225, 205, 150), anchor="mm")
    if pxm > 2:
        bh = 10 * pxm; bw = 9 * pxm; bx = 1500
        a = ease((pxm - 2) / 4)
        bl = Image.new("RGBA", img.size, (0, 0, 0, 0)); db = ImageDraw.Draw(bl)
        db.rectangle([bx, cy + th / 2 + 40 - bh, bx + bw, cy + th / 2 + 40], fill=(70, 80, 110, int(255 * a)), outline=(170, 180, 210, int(255 * a)), width=3)
        for fl in range(3):
            for wn in range(3):
                wx = bx + bw * (0.15 + 0.3 * wn); wy = cy + th / 2 + 40 - bh + bh * (0.1 + 0.32 * fl)
                db.rectangle([wx, wy, wx + bw * 0.15, wy + bh * 0.15], fill=(255, 210, 130, int(220 * a)))
        img.alpha_composite(bl)
        alpha_text(img, (bx + bw / 2, cy + th / 2 + 85), "a 3-storey building (≈ 10 m)", F(30, "Bold"), WHITE, a)
        d = ImageDraw.Draw(img)
        d.line([(bx - 40, cy - th / 2), (bx - 40, cy + th / 2)], fill=ROSE11, width=4)
        alpha_text(img, (bx - 60, cy), "≈ 10 m", F(40, "Black"), ROSE11, a, anchor="rm")
    view = W / pxm
    s = f"{view / 1000:,.0f} km" if view > 5000 else f"{view:,.0f} m"
    alpha_text(img, (W / 2, 900), "width of this view: " + s, F(44, "ExtraBold"), CREAM11, ease(t / 0.5))
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - dur * 0.75) / 0.5), y=H - 90)

def shadow_lat11(decl, band):
    """latitudes (deg) in the winter hemisphere where the noon Sun is behind ring band (r0, r1); decl in degrees"""
    if abs(decl) < 0.3: return []
    dd = math.radians(abs(decl)); out = []
    for i in range(0, 700):
        ph = math.radians(i / 10)
        x = math.cos(ph) + math.sin(ph) / math.tan(dd)
        if band[0] <= x < band[1]: out.append(i / 10)
    return out

CITIES11 = [("Quito", -0.2), ("Mexico City", 19.4), ("Hong Kong", 22.3), ("Miami", 25.8), ("Cairo", 30.0), ("New York", 40.7), ("London", 51.5),
            ("São Paulo", -23.5), ("Sydney", -33.9), ("Buenos Aires", -34.6)]
_sm11 = None
def sc_shadowmap(img, v, t, dur):
    """season chart: x = day of the year, y = latitude (−60..60), shaded where the rings block the noon Sun (our calculation, 23.44° tilt);
    a cursor sweeps the months and fills the chart; city lines with markers"""
    global _sm11
    X0, X1, Y0, Y1 = 400, 1780, 170, 930
    def ly(la): return lerp(Y0, Y1, (60 - la) / 120)
    if _sm11 is None:
        arr = np.zeros((int(Y1 - Y0), int(X1 - X0), 4), np.uint8)
        for xi in range(0, int(X1 - X0), 3):
            day = xi / (X1 - X0) * 365; dec = -23.44 * math.cos(2 * math.pi * (day + 10) / 365)
            for nm, r0, r1, col, op in RINGS11:
                if op < 0.2: continue
                for la in shadow_lat11(dec, (r0, r1))[::3]:
                    lat_ = la if dec < 0 else -la
                    yi = int(ly(lat_) - Y0)
                    if 0 <= yi < arr.shape[0]:
                        a_ = int(255 * op)
                        arr[max(0, yi - 1):yi + 2, xi:xi + 3] = np.maximum(arr[max(0, yi - 1):yi + 2, xi:xi + 3], np.array([20, 24, 60, a_], np.uint8))
        _sm11 = Image.fromarray(arr, "RGBA")
    d = ImageDraw.Draw(img)
    pane = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(pane).rectangle([X0, Y0, X1, Y1], fill=(255, 214, 120, 60)); img.alpha_composite(pane)
    p = ease((t - 0.4) / max(1.0, dur * 0.7)); xc = X0 + (X1 - X0) * p
    reveal = _sm11.crop((0, 0, max(1, int(xc - X0)), _sm11.height)); img.alpha_composite(reveal, (X0, Y0))
    d = ImageDraw.Draw(img)
    for la in (-60, -30, 0, 30, 60):
        d.line([(X0, ly(la)), (X1, ly(la))], fill=(120, 126, 150) if la else (200, 205, 225), width=1 if la else 2)
        d.text((X1 + 14, ly(la)), f"{abs(la)}°{'N' if la > 0 else ('S' if la < 0 else '')}", font=F(24, "SemiBold"), fill=DIM, anchor="lm")
    months = "JFMAMJJASOND"
    for i, m in enumerate(months):
        d.text((X0 + (i + 0.5) * (X1 - X0) / 12, Y1 + 30), m, font=F(30, "Bold"), fill=WHITE, anchor="mm")
    day = p * 365; dec = -23.44 * math.cos(2 * math.pi * (day + 10) / 365)
    d.line([(xc, Y0 - 10), (xc, Y1 + 10)], fill=ROSE11, width=4)
    cs = sorted([c for c in CITIES11 if c[0] in v.get("cities", [c[0] for c in CITIES11])], key=lambda c: -c[1])
    ys = []
    for nm, la in cs:
        y = ly(la)
        if ys and y < ys[-1] + 34: y = ys[-1] + 34
        ys.append(y)
    for (nm, la), yl in zip(cs, ys):
        y = ly(la)
        insh = False
        for _, r0, r1, col, op in RINGS11:
            if op < 0.2: continue
            if (la > 0) == (dec < 0) and any(abs(abs(la) - s) < 0.6 for s in shadow_lat11(dec, (r0, r1))): insh = True
        col = ROSE11 if insh else WHITE
        d.ellipse([X0 - 26, y - 9, X0 - 8, y + 9], fill=col)
        if abs(yl - y) > 2: d.line([(X0 - 30, y), (X0 - 60, yl)], fill=col, width=2)
        d.text((X0 - 66, yl), nm, font=F(30, "Bold" if insh else "SemiBold"), fill=col, anchor="rm")
    d.text((X0, Y0 - 40), v.get("head", "Where the rings hide the noon Sun"), font=F(46, "ExtraBold"), fill=WHITE, anchor="lm")
    d.text((X1, Y0 - 40), "shaded = ring shadow at noon", font=F(28, "SemiBold"), fill=CREAM11, anchor="rm")
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 70)

def sc_craterbelt(img, v, t, dur):
    """ancient Earth (Ordovician, ~466 million years ago) with a debris ring; 21 impact markers land inside the ±30° band (positions illustrative)"""
    cx, cy, R = 640, 560, 330; rot = t * 9
    tilt = 0.32
    def ring_pts(rr, front):
        pts = []
        for k in range(0, 181):
            a = math.pi * k / 180 + (0 if front else math.pi)
            x, y = rr * math.cos(a), rr * math.sin(a) * math.sin(tilt)
            pts.append((cx + x, cy + y))
        return pts
    def ring(front):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for i in range(16):
            rr = R * (1.35 + 0.9 * i / 16); a = int(150 * (0.6 + 0.4 * math.sin(i * 1.7)) * ease((t - 0.3) / 1.0))
            dl.line(ring_pts(rr, front), fill=(200, 170, 140, a), width=6)
        img.alpha_composite(lay)
    ring(False)
    paste_c(img, planet_sprite(R, (36, 70, 130), light=(-0.8, -0.4), glow=(110, 170, 255)), cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for la in (-30, 30):
        pts = [proj6(la, lo, 0, R, cx, cy, tilt=tilt) for lo in range(-180, 181, 4)]
        seg = [(p[0], p[1]) for p in pts if p[2] > 0]
        if len(seg) > 1: dl.line(seg, fill=ROSE11 + (230,), width=4)
    img.alpha_composite(lay)
    rng = random.Random(466); n = int(21 * ease((t - 1.0) / max(1.0, dur * 0.55)))
    d = ImageDraw.Draw(img)
    for i in range(21):
        la, lo = rng.uniform(-28, 28), rng.uniform(0, 360)
        if i >= n: continue
        x, y, z = proj6(la, lo, rot, R, cx, cy, tilt=tilt)
        if z > 0: d.ellipse([x - 9, y - 9, x + 9, y + 9], outline=(255, 190, 90), width=4)
    ring(True)
    bx = 1430
    alpha_text(img, (bx, 300), f"{n} / 21", F(120, "Black"), (255, 190, 90), ease((t - 0.8) / 0.5))
    alpha_text(img, (bx, 400), "impact craters from that era", F(34, "SemiBold"), WHITE, ease((t - 0.8) / 0.5))
    alpha_text(img, (bx, 450), "all within 30° of the equator", F(34, "ExtraBold"), ROSE11, ease((t - 1.5) / 0.5))
    alpha_text(img, (bx, 560), "≈ 466 million years ago", F(40, "Black"), CREAM11, ease((t - 2.0) / 0.5))
    alpha_text(img, (bx, 620), "crater positions illustrative", F(26, "Medium"), DIM, ease((t - 2.0) / 0.5))
    if v.get("head"): alpha_text(img, (W / 2, 100), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 3.0) / 0.5))

# ---------------- scenes (EP12: photon gold / signal green / fiber magenta) ----------------
PHOT12, SIG12, FIB12, NAVY12 = (255, 232, 150), (110, 255, 170), (255, 95, 200), (14, 20, 46)
LAG12 = [("Inside a chip", 3.3e-10), ("New York → London", 0.0273), ("The Moon", 1.28), ("Mars", (182, 1335)), ("Sunlight", 499),
         ("Voyager 1", 86000), ("Beyond the horizon", None)]
LAG_TICKS12 = [(1e-9, "1 ns"), (1e-3, "1 ms"), (1, "1 s"), (3600, "1 hour"), (3.156e7, "1 year"), (3.156e13, "1 million yr"), (3.156e16, "1 billion yr")]
def _lagx12(s, x0=170, x1=1600): return lerp(x0, x1, (math.log10(s) + 10.5) / 28.0)
def sc_lagmeter(img, v, t, dur):
    """chapter card: a log 'lag meter' from 0.1 ns to billions of years + NEVER; stamps for messages 1..n, the current one (n) pops in"""
    n = v.get("n", 0); d = ImageDraw.Draw(img); y = 660
    if n:
        alpha_text(img, (W / 2, 230), f"MESSAGE {n}", F(130, "Black"), PHOT12, ease(t / 0.4), dy=(1 - ease(t / 0.4)) * 30)
        alpha_text(img, (W / 2, 360), v.get("name", LAG12[n - 1][0]), F(64, "ExtraBold"), WHITE, ease((t - 0.3) / 0.4))
    else:
        alpha_text(img, (W / 2, 250), v.get("head", "7 messages, 1 stopwatch"), F(96, "Black"), PHOT12, ease(t / 0.4))
    d.rounded_rectangle([150, y - 10, 1630, y + 10], 10, fill=NAVY12, outline=(60, 80, 140), width=2)
    for s, lab in LAG_TICKS12:
        x = _lagx12(s); d.line([(x, y - 24), (x, y + 24)], fill=(90, 105, 150), width=3)
        d.text((x, y + 60), lab, font=F(28, "Bold"), fill=DIM, anchor="mm")
    d.rounded_rectangle([1660, y - 34, 1840, y + 34], 18, fill=(60, 16, 30), outline=RED, width=3)
    d.text((1750, y), "NEVER", font=F(36, "Black"), fill=RED, anchor="mm")
    show = range(len(LAG12)) if n == 0 else range(n)
    for i in show:
        nm, s = LAG12[i]; cur = (i == n - 1)
        a = ease((t - 0.6 - (i * 0.35 if n == 0 else (0.4 if cur else 0))) / 0.4)
        if a <= 0: continue
        col = SIG12 if cur or n == 0 else (120, 135, 175)
        if s is None:
            d.rounded_rectangle([1660, y - 34, 1840, y + 34], 18, fill=mix(SPACE, RED, a), outline=WHITE, width=4)
            d.text((1750, y), "NEVER", font=F(36, "Black"), fill=WHITE, anchor="mm"); d.text((1750, y - 70), str(i + 1), font=F(34, "Black"), fill=mix(SPACE, RED, a), anchor="mm")
            continue
        elif isinstance(s, tuple):
            xa, xb = _lagx12(s[0]), _lagx12(s[1]); x = (xa + xb) / 2
            d.rounded_rectangle([xa, y - 16, xb, y + 16], 12, fill=mix(SPACE, col, a))
        else: x = _lagx12(s)
        r = 22 if cur else 15
        d.ellipse([x - r, y - r, x + r, y + r], fill=mix(SPACE, col, a), outline=mix(SPACE, WHITE, a), width=3)
        d.text((x, y - 40 - (i % 2) * 44 if n == 0 else y - 46), str(i + 1), font=F(34 if cur else 28, "Black"), fill=mix(SPACE, col, a), anchor="mm")
    alpha_text(img, (W / 2, 830), "time for light to get there", F(36, "SemiBold"), DIM, ease((t - 0.5) / 0.5))
    caption(img, v.get("caption"), ease((t - 1.5) / 0.5))

def sc_chiptick(img, v, t, dur):
    """a processor die with a 10 cm ruler; a light pulse crosses it once per 3 GHz clock tick (slow motion), counter in cm"""
    cx, cy = W / 2, 560; L = 1000; x0 = cx - L / 2
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([cx - 560, cy - 250, cx + 560, cy + 250], 24, fill=(14, 40, 34, 245), outline=(80, 170, 130, 255), width=4)
    for i in range(14):
        for j in range(6):
            xx, yy = cx - 520 + i * 74, cy - 210 + j * 72
            dl.rectangle([xx, yy, xx + 60, yy + 56], fill=(24, 70, 56, 255), outline=(50, 120, 95, 255))
            dl.rectangle([xx + 8, yy + 8, xx + 26, yy + 20], fill=(200, 170, 70, 120))
    for k in range(40):
        dl.rectangle([cx - 560 + 14 + k * 28, cy + 250, cx - 560 + 26 + k * 28, cy + 268], fill=(200, 180, 110, 255))
        dl.rectangle([cx - 560 + 14 + k * 28, cy - 268, cx - 560 + 26 + k * 28, cy - 250], fill=(200, 180, 110, 255))
    img.alpha_composite(lay)
    per = v.get("period", 2.2); ph = (t % per) / per; ticks = int(t // per) + 1
    px = x0 + L * min(1, ph / 0.85); d = ImageDraw.Draw(img); yl = cy
    for k in range(40):
        tx = px - k * 9
        if tx < x0: break
        d.ellipse([tx - 10 + k * 0.2, yl - 10 + k * 0.2, tx + 10 - k * 0.2, yl + 10 - k * 0.2], fill=mix((14, 40, 34), PHOT12, 1 - k / 40))
    paste_c(img, radial(120, [(0, (255, 250, 220, 255)), (0.25, (255, 230, 140, 200)), (1, (255, 200, 80, 0))]), px, yl)
    d = ImageDraw.Draw(img); ry = cy + 330
    d.line([(x0, ry), (x0 + L, ry)], fill=WHITE, width=4)
    for k in range(11):
        x = x0 + L * k / 10; d.line([(x, ry - 22), (x, ry)], fill=WHITE, width=3)
        d.text((x, ry + 30), f"{k}", font=F(30, "Bold"), fill=WHITE, anchor="mm")
    d.text((x0 + L + 40, ry + 30), "cm", font=F(30, "Bold"), fill=DIM, anchor="lm")
    alpha_text(img, (W / 2, 150), v.get("head", "One clock tick at 3 GHz = 0.33 nanoseconds"), F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1430, 860, 1860, 1000], 20, fill=(8, 10, 24, 220), outline=PHOT12 + (160,), width=3); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((1645, 905), f"light: {10 * min(1, ph / 0.85):4.1f} cm", font=F(44, "Black"), fill=PHOT12, anchor="mm")
    d.text((1645, 960), f"tick #{ticks}  (slow motion)", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 80)

def sc_fiberrace(img, v, t, dur):
    """New York -> London (5,570 km) in slow motion: light in vacuum vs light in glass fiber (2/3 c); optional microwave lane"""
    xa, xb = 250, 1670; km = v.get("km", 5570); c = 299792.458
    lanes = [("light in a vacuum", c, PHOT12), ("light in glass fiber", c / 1.47, FIB12)]
    if v.get("microwave"): lanes.insert(1, ("radio through air", c / 1.0003, SIG12))
    slow = v.get("slow", 160.0)  # animation seconds per real second
    tr = max(0, t - 0.8) / slow
    d = ImageDraw.Draw(img)
    d.arc([xa - 300, 760, xb + 300, 1500], 200, 340, fill=(40, 90, 160), width=6)
    d.text((W / 2, 900), "Atlantic Ocean", font=F(32, "SemiBold"), fill=(80, 130, 200), anchor="mm")
    for x, nm in ((xa, "NEW YORK"), (xb, "LONDON")):
        d.line([(x, 280), (x, 800)], fill=(90, 100, 140), width=3)
        d.text((x, 245), nm, font=F(44, "Black"), fill=WHITE, anchor="mm")
    for i, (lab, sp, col) in enumerate(lanes):
        y = 380 + i * (360 / max(1, len(lanes) - 1)) if len(lanes) > 1 else 500
        dist = min(km, sp * tr); x = lerp(xa, xb, dist / km)
        d.line([(xa, y), (xb, y)], fill=mix(SPACE, col, 0.25), width=4)
        d.line([(xa, y), (x, y)], fill=col, width=8)
        paste_c(img, radial(90, [(0, (255, 255, 240, 255)), (0.3, col + (200,)), (1, col + (0,))]), x, y)
        d = ImageDraw.Draw(img)
        ms = 1000 * min(tr, km / sp)
        d.text((xa + 20, y - 44), lab, font=F(34, "Bold"), fill=col, anchor="lm")
        d.text((xb + 30, y), f"{ms:5.1f} ms", font=F(46, "Black"), fill=WHITE if dist < km else col, anchor="lm")
    alpha_text(img, (W / 2, 140), v.get("head", "New York → London: 5,570 km"), F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    d.text((W / 2, 1000), "slow motion  •  straight-line distance (real cables are longer)", font=F(28, "Medium"), fill=DIM, anchor="mm")
    caption(img, v.get("caption"), ease((t - 3.0) / 0.5), y=H - 160)

def _sig12(d, x0, y0, x1, y1, p, col):
    x, y = lerp(x0, x1, p), lerp(y0, y1, p)
    for k in range(3):
        r = 14 + k * 10; d.ellipse([x - r, y - r, x + r, y + r], outline=mix(SPACE, col, 1 - k * 0.3), width=3)
    return x, y

def sc_marsdelay(img, v, t, dur):
    """mode moon: Earth <-> Moon radio round trip in real time (1.28 s each way); mode range: top-down orbits, Mars from closest
    (perihelic opposition) to farthest (conjunction near aphelion), live one-way light time; mode landing: Perseverance timeline"""
    mode = v.get("mode", "range"); d = ImageDraw.Draw(img)
    if mode == "moon":
        ex, mx_, y = 330, 1590, 560
        paste_c(img, earth_sprite(110), ex, y); paste_c(img, moon8(46) if callable(globals().get("moon8")) else planet_sprite(46, (190, 190, 195)), mx_, y)
        d = ImageDraw.Draw(img); cyc = 2.56 + 0.8; ph = (t % cyc)
        if ph < 1.28: _sig12(d, ex + 120, y, mx_ - 60, y, ph / 1.28, SIG12); lab = "question on its way"
        elif ph < 2.56: _sig12(d, mx_ - 60, y, ex + 120, y, (ph - 1.28) / 1.28, PHOT12); lab = "answer on its way"
        else: lab = "answer arrives"
        d.text((W / 2, y + 170), f"{min(ph, 2.56):.2f} s", font=F(96, "Black"), fill=WHITE, anchor="mm")
        d.text((W / 2, y + 260), lab, font=F(38, "Bold"), fill=SIG12 if ph < 1.28 else PHOT12, anchor="mm")
        d.text((ex, y + 160), "EARTH", font=F(36, "Black"), fill=WHITE, anchor="mm"); d.text((mx_, y + 100), "MOON", font=F(36, "Black"), fill=WHITE, anchor="mm")
        d.text((W / 2, y - 120), "384,400 km  •  1.28 s each way (real time)", font=F(36, "Bold"), fill=DIM, anchor="mm")
    elif mode == "range":
        cx, cy, k = 700, 560, 200; a_, e_ = 1.524, 0.0934
        paste_c(img, sun_sprite(26), cx, cy); d = ImageDraw.Draw(img)
        d.ellipse([cx - k, cy - k, cx + k, cy + k], outline=(60, 100, 180), width=2)
        pts = []
        for i in range(181):
            nu = 2 * math.pi * i / 180; r = a_ * (1 - e_ ** 2) / (1 + e_ * math.cos(nu)); pts.append((cx + k * r * math.cos(nu), cy - k * r * math.sin(nu)))
        d.line(pts, fill=(150, 80, 60), width=2)
        p = easeio((t - 0.5) / max(1.0, dur * 0.75)); nu = math.pi * p; th = 2 * math.pi * p
        rm = a_ * (1 - e_ ** 2) / (1 + e_ * math.cos(nu)); mxp, myp = cx + k * rm * math.cos(nu), cy - k * rm * math.sin(nu)
        exp_, eyp = cx + k * math.cos(th), cy - k * math.sin(th)
        dist = math.hypot(rm * math.cos(nu) - math.cos(th), rm * math.sin(nu) - math.sin(th))
        blocked = dist > 2.3
        d.line([(exp_, eyp), (mxp, myp)], fill=SIG12 if not blocked else (120, 130, 150), width=3)
        paste_c(img, earth_sprite(16, glow=None), exp_, eyp); paste_c(img, planet_sprite(13, (210, 100, 70)), mxp, myp)
        d = ImageDraw.Draw(img)
        d.text((exp_ + 24, eyp - 24), "Earth", font=F(30, "Bold"), fill=WHITE, anchor="lb"); d.text((mxp + 22, myp - 20), "Mars", font=F(30, "Bold"), fill=(240, 140, 110), anchor="lb")
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1150, 330, 1820, 760], 28, fill=(8, 10, 24, 225), outline=SIG12 + (150,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img)
        d.text((1485, 390), "radio signal, one way", font=F(36, "Bold"), fill=DIM, anchor="mm")
        mins = dist * 499.0 / 60
        d.text((1485, 510), f"{mins:4.1f} min", font=F(120, "Black"), fill=SIG12, anchor="mm")
        d.text((1485, 620), f"{dist * 149.6:,.0f} million km", font=F(40, "ExtraBold"), fill=WHITE, anchor="mm")
        d.text((1485, 700), "range: about 3 to 22 minutes", font=F(32, "SemiBold"), fill=PHOT12, anchor="mm")
        d.text((700, 1010), "orbits to scale (Mars's orbit is slightly oval)", font=F(26, "Medium"), fill=DIM, anchor="mm")
    else:  # landing
        x0, x1 = 220, 1700; m2x = lambda m: lerp(x0, x1, m / 20.0)
        now = min(20.0, max(0.0, (t - 0.5) / max(1.0, dur * 0.8)) * 20.0)
        d.text((x0, 230), "ON MARS", font=F(40, "Black"), fill=(240, 140, 110), anchor="lm")
        d.text((x0, 560), "ON EARTH (signal ≈ 11 min 22 s later)", font=F(40, "Black"), fill=SIG12, anchor="lm")
        for y in (330, 660):
            d.rounded_rectangle([x0, y - 22, x1, y + 22], 14, fill=NAVY12)
        d.rounded_rectangle([m2x(0), 308, m2x(7), 352], 14, fill=(200, 90, 60))
        d.text(((m2x(0) + m2x(7)) / 2, 330), "entry → touchdown ≈ 7 min", font=F(28, "Black"), fill=WHITE, anchor="mm")
        lag = 11.37
        d.rounded_rectangle([m2x(lag), 638, m2x(lag + 7), 682], 14, fill=(40, 120, 80))
        d.text(((m2x(lag) + m2x(lag + 7)) / 2, 660), "what Earth hears", font=F(28, "Black"), fill=WHITE, anchor="mm")
        for m in range(0, 21, 2):
            d.text((m2x(m), 760), f"{m} min", font=F(26, "Bold"), fill=DIM, anchor="mm")
        d.line([(m2x(now), 260), (m2x(now), 720)], fill=WHITE, width=4)
        d.text((m2x(now), 810), f"{int(now):02d}:{int((now % 1) * 60):02d}", font=F(44, "Black"), fill=WHITE, anchor="mm")
        if now >= 7: d.text((m2x(7), 410), "rover already on the ground", font=F(32, "ExtraBold"), fill=PHOT12, anchor="mm")
        if now >= lag: d.text((m2x(lag), 600), "Earth hears: \"entry has begun\"", font=F(32, "ExtraBold"), fill=SIG12, anchor="lm")
        d.text((W / 2, 900), "Perseverance, 18 February 2021 (NASA)", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 130 if mode != "landing" else 120), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 90)

_rw12 = None
def _walk12():
    global _rw12
    if _rw12 is None:
        rng = np.random.default_rng(12); p = np.zeros(2); pts = [p.copy()]
        while np.hypot(*p) < 1.0 and len(pts) < 9000:
            a = rng.uniform(0, 2 * math.pi); st = rng.uniform(0.006, 0.03)
            p = p + st * np.array([math.cos(a), math.sin(a)]) + 0.00012 * p / max(0.05, np.hypot(*p))
            pts.append(p.copy())
        _rw12 = np.array(pts)
    return _rw12

def sc_randomwalk(img, v, t, dur):
    """Sun cross-section (core / radiative / convective), a random-walk path from the core to the surface; years counter (model-dependent);
    side box: 'straight line ≈ 2.3 s'. v.y1 = counter end, v.head, v.caption"""
    cx, cy, R_ = 680, 570, 430
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for fr, col in [(1.0, (230, 90, 30)), (0.71, (250, 140, 50)), (0.25, (255, 235, 170))]:
        r = R_ * fr; dl.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col + (255,))
    rng = random.Random(3)
    for i in range(70):
        a = rng.uniform(0, 2 * math.pi); rr = R_ * rng.uniform(0.74, 0.97); s = rng.uniform(12, 26)
        dl.ellipse([cx + rr * math.cos(a) - s, cy + rr * math.sin(a) - s, cx + rr * math.cos(a) + s, cy + rr * math.sin(a) + s], outline=(200, 70, 20, 160), width=3)
    img.alpha_composite(lay)
    paste_c(img, radial(int(R_ * 2.6), [(0, (255, 200, 90, 0)), (0.76, (255, 170, 60, 0)), (0.8, (255, 160, 50, 90)), (1, (255, 120, 30, 0))]), cx, cy)
    pts = _walk12(); p = easeio((t - 0.4) / max(1.0, dur * 0.8)); n = max(2, int(len(pts) * p))
    sel = pts[:n]; xy = [(cx + R_ * x, cy + R_ * y) for x, y in sel[:: max(1, n // 1500)]] + [(cx + R_ * sel[-1][0], cy + R_ * sel[-1][1])]
    d = ImageDraw.Draw(img); d.line(xy, fill=(40, 20, 60), width=3)
    paste_c(img, radial(60, [(0, (255, 255, 255, 255)), (0.3, (190, 230, 255, 220)), (1, (120, 180, 255, 0))]), *xy[-1])
    d = ImageDraw.Draw(img)
    for fr, lab in [(0.12, "CORE"), (0.48, "RADIATIVE ZONE"), (0.86, "CONVECTIVE ZONE")]:
        d.text((cx, cy + R_ * fr + (0 if fr > 0.2 else 0)), lab, font=F(24, "Black"), fill=(70, 30, 10), anchor="mm")
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1240, 300, 1840, 820], 28, fill=(8, 10, 24, 225), outline=PHOT12 + (150,), width=3); img.alpha_composite(box)
    d = ImageDraw.Draw(img); y1 = v.get("y1", 170000)
    d.text((1540, 360), "energy escaping the Sun", font=F(34, "Bold"), fill=DIM, anchor="mm")
    d.text((1540, 470), f"{y1 * p:,.0f}", font=F(110, "Black"), fill=PHOT12, anchor="mm")
    d.text((1540, 570), "years", font=F(48, "ExtraBold"), fill=WHITE, anchor="mm")
    d.text((1540, 660), "estimates: ≈ 10,000 to 170,000", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    d.text((1540, 740), "straight line: ≈ 2.3 seconds", font=F(36, "ExtraBold"), fill=SIG12, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 95), v["head"], F(52, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 80)

def sc_horizonrun(img, v, t, dur):
    """expanding space with a constant expansion rate (illustrative): galaxies drift away (x' = Hx), light heads toward us at c
    (x' = Hx - c). Inside the horizon (Hx = c) light arrives; beyond it, light is carried away forever. v.label = show the horizon label"""
    x0, y0 = 150, 560; xh = 900.0; c = 150.0; Hh = c / xh; tt = t * 0.9
    d = ImageDraw.Draw(img)
    for k in range(1, 40):  # stretching grid
        gx = x0 + 60 * k * math.exp(Hh * (tt % 6.0) * 0.4)
        if gx > W: break
        d.line([(gx, 300), (gx, 820)], fill=(26, 30, 60), width=2)
    d.line([(x0, y0), (W, y0)], fill=(50, 60, 100), width=2)
    xs = x0 + xh
    if v.get("label", True):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([xs, 280, W, 840], fill=(80, 10, 30, 70)); img.alpha_composite(lay); d = ImageDraw.Draw(img)
        for yy in range(290, 840, 30): d.line([(xs, yy), (xs, yy + 16)], fill=RED, width=5)
        d.text((xs, 245), "cosmic event horizon ≈ 16 billion light-years", font=F(34, "Black"), fill=RED, anchor="mm")
    rng = random.Random(16)
    gal = [rng.uniform(math.log(60), math.log(4000)) for _ in range(26)]
    for i, lg in enumerate(gal):
        xi = math.exp(lg) * math.exp(Hh * tt * 0.35) % 2600
        x = x0 + xi
        if x > W + 40: continue
        far = xi > xh
        col = (110, 115, 150) if far else (255, 225, 170)
        yy = y0 + (i % 5 - 2) * 46
        d.ellipse([x - 16, yy - 6, x + 16, yy + 6], fill=col)
        for k in range(6):  # photons emitted every 1.6 s toward us
            te = (math.floor(tt / 1.6) - k) * 1.6
            if te < -0.01: continue
            xe = math.exp(lg) * math.exp(Hh * te * 0.35) % 2600
            if (xe > xh) != far and abs(xe - xi) > 300: continue
            px = xh + (xe - xh) * math.exp(Hh * (tt - te))
            if 0 < px < W - x0 and abs(px - xi) > 4:
                d.ellipse([x0 + px - 5, yy - 5, x0 + px + 5, yy + 5], fill=PHOT12 if px < xh else (150, 150, 170))
    paste_c(img, earth_sprite(28, glow=(120, 180, 255)), x0 - 40, y0)
    d = ImageDraw.Draw(img); d.text((x0 - 40, y0 + 70), "US", font=F(34, "Black"), fill=WHITE, anchor="mm")
    d.text((560, 900), "light inside the horizon: arrives one day", font=F(32, "Bold"), fill=PHOT12, anchor="mm")
    d.text((1450, 900), "light beyond it: never arrives", font=F(32, "Bold"), fill=(170, 170, 190), anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 130), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    d.text((W / 2, 990), "illustration, not to scale", font=F(26, "Medium"), fill=DIM, anchor="mm")


# ---------------- scenes (EP13: road amber / board teal / ticket coral) ----------------
ROAD13, BOARD13, TICK13, PLUM13 = (255, 170, 60), (60, 225, 200), (255, 120, 110), (34, 14, 40)
DEP13 = [("MOON", "160 days", "18 days", "33 min", "1.3 s"), ("VENUS", "43.6 yr", "4.8 yr", "2.3 days", "2.1 min"),
         ("MARS", "62.3 yr", "6.9 yr", "3.3 days", "3.0 min"), ("MERCURY", "88.2 yr", "9.8 yr", "4.6 days", "4.3 min"),
         ("JUPITER", "671 yr", "74.6 yr", "35 days", "33 min"), ("SATURN", "1,364 yr", "152 yr", "72 days", "66 min"),
         ("URANUS", "2,945 yr", "327 yr", "155 days", "2.4 h"), ("NEPTUNE", "4,912 yr", "546 yr", "259 days", "4.0 h")]
PL13 = {"Mercury": (0.387, 88.0, (175, 165, 155)), "Venus": (0.723, 224.7, (235, 205, 150)), "Earth": (1.0, 365.25, (70, 130, 230)),
        "Mars": (1.524, 687.0, (210, 100, 70)), "Jupiter": (5.203, 4331, (215, 175, 130)), "Saturn": (9.537, 10747, (225, 200, 140)),
        "Uranus": (19.19, 30589, (150, 220, 230)), "Neptune": (30.07, 59800, (80, 120, 240))}
_FLAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def _flap13(txt, t, seed):
    """split-flap text: random letters that settle left to right"""
    rng = random.Random(seed + int(t * 20)); out = []
    for i, ch in enumerate(txt):
        out.append(ch if t > 0.25 + i * 0.04 or ch == " " else rng.choice(_FLAP))
    return "".join(out)

def sc_departures(img, v, t, dur):
    """airport split-flap departure board: GATE / DESTINATION / CAR / JET / FASTEST PROBE (+ LIGHT); v.rows shown, newest row flips in,
    v.hl highlighted (-1 none), v.detail line under the board, v.light adds a LIGHT column"""
    rows = v.get("rows", 0); hl = v.get("hl", -1); light = v.get("light", False)
    x0, x1, y0 = 120, 1800, 220
    cols = [("GATE", 150), ("DESTINATION", 360), ("CAR 100 km/h", 330), ("JET 900 km/h", 300), ("FASTEST PROBE", 330)]
    if light: cols.append(("LIGHT", 210))
    tw = sum(c[1] for c in cols); sx = (x1 - x0) / tw
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([x0 - 30, y0 - 120, x1 + 30, 1000], 28, fill=(14, 12, 20, 240), outline=(70, 60, 80, 255), width=4)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.text((x0, y0 - 70), v.get("head", "DEPARTURES"), font=F(56, "Black"), fill=ROAD13, anchor="lm")
    d.text((x1, y0 - 70), "SOLAR SYSTEM TERMINAL", font=F(30, "Bold"), fill=DIM, anchor="rm")
    x = x0
    for name, w in cols:
        d.text((x + 12, y0), name, font=F(26, "Bold"), fill=BOARD13 if name != "LIGHT" else PHOT12, anchor="lm"); x += w * sx
    rh = 88
    for i in range(min(rows, len(DEP13))):
        row = DEP13[i]; y = y0 + 70 + i * rh
        new = (i == rows - 1 and v.get("hl", -1) == i and not light)
        tt = t if new else 9.0
        if i == hl:
            g = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(g).rounded_rectangle([x0 - 14, y - 8, x1 + 14, y + rh - 14], 12, fill=BOARD13 + (50,), outline=BOARD13 + (220,), width=3); img.alpha_composite(g); d = ImageDraw.Draw(img)
        vals = [str(i), row[0], row[1], row[2], row[3]] + ([row[4]] if light else [])
        x = x0
        for k, ((name, w), val) in enumerate(zip(cols, vals)):
            cw = w * sx - 16
            d.rounded_rectangle([x + 4, y, x + cw, y + rh - 22], 8, fill=(30, 28, 36))
            d.line([(x + 4, y + (rh - 22) / 2), (x + cw, y + (rh - 22) / 2)], fill=(10, 10, 14), width=2)
            txt = _flap13(val.upper(), tt - k * 0.12, i * 10 + k)
            col = WHITE if k < 2 else (ROAD13 if k == 2 else (TICK13 if k == 3 else (BOARD13 if k == 4 else PHOT12)))
            d.text((x + 14, y + (rh - 22) / 2), txt, font=F(38, "Bold"), fill=col, anchor="lm"); x += w * sx
    if rows == 0:
        for i in range(8):
            y = y0 + 70 + i * rh; d.rounded_rectangle([x0 + 4, y, x1, y + rh - 22], 8, fill=(24, 22, 30))
        d.text((W / 2, y0 + 70 + 3.5 * rh), "BOARDING SOON", font=F(64, "Black"), fill=mix(SPACE, ROAD13, 0.5 + 0.5 * math.sin(t * 4)), anchor="mm")
    if v.get("detail"): alpha_text(img, (W / 2, 1040), v["detail"], F(40, "ExtraBold"), TICK13, ease((t - 1.0) / 0.5))
    elif rows: d.text((W / 2, 1040), "nonstop, straight line, planet at its closest (NASA fact sheet distances)", font=F(28, "SemiBold"), fill=DIM, anchor="mm")

def _car13(d, cx, cy, s, t):
    """car seen from behind (simple shapes)"""
    b = cy + math.sin(t * 9) * 1.5 * s
    d.rounded_rectangle([cx - 150 * s, b - 40 * s, cx + 150 * s, b + 50 * s], int(22 * s), fill=(200, 60, 50))
    d.polygon([(cx - 110 * s, b - 40 * s), (cx - 80 * s, b - 105 * s), (cx + 80 * s, b - 105 * s), (cx + 110 * s, b - 40 * s)], fill=(170, 45, 40))
    d.polygon([(cx - 92 * s, b - 46 * s), (cx - 70 * s, b - 96 * s), (cx + 70 * s, b - 96 * s), (cx + 92 * s, b - 46 * s)], fill=(60, 80, 110))
    for sx_ in (-1, 1):
        d.rounded_rectangle([cx + sx_ * 105 * s - 30 * s, b - 20 * s, cx + sx_ * 105 * s + 30 * s, b + 4 * s], int(6 * s), fill=(255, 70, 60))
        d.rounded_rectangle([cx + sx_ * 120 * s - 28 * s, b + 40 * s, cx + sx_ * 120 * s + 28 * s, b + 78 * s], int(8 * s), fill=(20, 20, 24))
    d.rectangle([cx - 45 * s, b + 10 * s, cx + 45 * s, b + 34 * s], fill=(235, 235, 220))

def sc_roadtrip(img, v, t, dur):
    """highway in perspective toward a destination world; car from behind; dashboard: odometer, time on the road, generations (v.gens);
    v.hide = counters show '?'"""
    dest = v.get("dest", "Mars"); vx, vy = W / 2, 470
    col = PL13.get(dest, (0, 0, (190, 190, 195)))[2] if dest in PL13 else (190, 190, 195)
    p = easeio((t - 0.3) / max(1.0, dur * 0.8))
    rr = 46 + 40 * p
    paste_c(img, radial(int(rr * 5), [(0, col + (80,)), (1, col + (0,))]), vx, vy - 90)
    if dest == "Moon": paste_c(img, moon8(int(rr)), vx, vy - 90)
    else: paste_c(img, planet_sprite(int(rr), col, light=(-0.6, -0.4)), vx, vy - 90)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.polygon([(vx - 14, vy), (vx + 14, vy), (W + 500, H), (-500, H)], fill=(36, 32, 40, 255))
    for side in (-1, 1): dl.line([(vx + side * 12, vy), (W / 2 + side * 1400, H)], fill=(230, 220, 200, 255), width=6)
    for k in range(14):
        z = ((k + t * 2.2) % 14) / 14; z2 = z + 0.03
        ya, yb = vy + (H - vy) * z ** 2.2, vy + (H - vy) * min(1, z2) ** 2.2
        wa, wb = 2 + 14 * z ** 2.2, 2 + 14 * min(1, z2) ** 2.2
        dl.polygon([(vx - wa, ya), (vx + wa, ya), (vx + wb, yb), (vx - wb, yb)], fill=ROAD13 + (255,))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    _car13(d, 620, 900, 0.9, t)
    d.text((vx, vy - 90 - rr - 40), dest.upper(), font=F(44, "Black"), fill=WHITE, anchor="mm")
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1150, 600, 1860, 1010], 26, fill=(10, 8, 16, 235), outline=ROAD13 + (180,), width=3); img.alpha_composite(box)
    d = ImageDraw.Draw(img); hide = v.get("hide")
    d.text((1505, 650), f"{v.get('kmh', 100)} km/h, no stops", font=F(32, "Bold"), fill=DIM, anchor="mm")
    km = v.get("km", 1) * p
    d.text((1505, 730), "?? km" if hide else f"{km:,.0f} km", font=F(60, "Black"), fill=WHITE, anchor="mm")
    if "days" in v: tv = "?? days" if hide else f"{v['days'] * p:,.0f} days"
    else: tv = "?? years" if hide else (f"{v['years'] * p:,.1f} years" if v["years"] < 100 else f"{v['years'] * p:,.0f} years")
    d.text((1505, 830), tv, font=F(84, "Black"), fill=ROAD13, anchor="mm")
    d.text((1505, 900), "on the road", font=F(32, "Bold"), fill=DIM, anchor="mm")
    if v.get("gens") and not hide:
        n = int(v["years"] * p / 30); show = min(n, 44)
        for k in range(show):
            gx, gy = 1180 + (k % 22) * 30, 950 + (k // 22) * 30
            d.ellipse([gx, gy - 12, gx + 10, gy - 2], fill=TICK13); d.rectangle([gx + 1, gy - 1, gx + 9, gy + 12], fill=TICK13)
        d.text((1505, 570), f"{n} generations of drivers", font=F(34, "ExtraBold"), fill=TICK13, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 70)

def _pos13(name, day, k, cx, cy, sq, ph0=0.0):
    a, P, _ = PL13[name]; r = k * (math.sqrt(a) if sq else a); th = ph0 + 2 * math.pi * day / P
    return cx + r * math.cos(th), cy - r * math.sin(th), r

def sc_transfer(img, v, t, dur):
    """top-down orbits (linear up to Mars, square-root scale beyond); a probe follows a half-ellipse transfer from Earth to v.target while the
    target moves to meet it; day counter (v.days). v.ghost = dashed straight line 'not how it works'; v.straight = only the straight line;
    v.avg = Mercury/Venus averaging demo; v.map = all orbits with AU labels"""
    tgt = v.get("target", "Mars"); cx, cy = 760 if not v.get("avg") else 640, 580
    amax = 30.07 if v.get("map") else max(1.7, PL13[tgt][0]); sq = amax > 2
    k = 440 / (math.sqrt(amax) if sq else amax)
    d = ImageDraw.Draw(img); paste_c(img, sun_sprite(16 if sq else 22), cx, cy); d = ImageDraw.Draw(img)
    for nm, (a, P, col) in PL13.items():
        if a > amax * 1.01: continue
        r = k * (math.sqrt(a) if sq else a)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=mix(SPACE, col, 0.45), width=2)
        if v.get("map") and a > 5: d.text((cx + r * 0.71 + 6, cy + r * 0.71 + 6), f"{nm} {a:g} AU", font=F(24, "Bold"), fill=col, anchor="lt")
    p = easeio((t - 0.4) / max(1.0, dur * 0.75))
    if v.get("map"):
        for i, nm in enumerate(PL13):
            x, y, _ = _pos13(nm, 0, k, cx, cy, sq, ph0=0.6 + i * 0.7); paste_c(img, planet_sprite(9, PL13[nm][2]), x, y)
        d = ImageDraw.Draw(img)
        r1, r2 = k * math.sqrt(1.524), k * math.sqrt(5.203)
        d.arc([cx - r2, cy - r2, cx + r2, cy + r2], 0, 360, fill=ROAD13, width=4)
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1300, 330, 1860, 820], 26, fill=(10, 8, 16, 230), outline=BOARD13 + (160,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img)
        for i, (lab, val, c_) in enumerate([("Sun → Mars", "1.5 AU", WHITE), ("Mars → Jupiter", "3.7 AU", ROAD13), ("Sun → Neptune", "30 AU", BOARD13), ("Sun as a 2 m door:", "Neptune 6.5 km", TICK13)]):
            d.text((1580, 390 + i * 110), lab, font=F(32, "Bold"), fill=DIM, anchor="mm"); d.text((1580, 435 + i * 110), val, font=F(46, "Black"), fill=c_, anchor="mm")
        d.text((cx, 1030), "square-root scale (true scale would not fit)", font=F(26, "Medium"), fill=DIM, anchor="mm")
    elif v.get("avg"):
        days = 30 + t * 420.0; ex, ey, _ = _pos13("Earth", days, k, cx, cy, sq); paste_c(img, earth_sprite(14, glow=None), ex, ey)
        acc = {"Venus": [], "Mercury": []}
        for nm in ("Venus", "Mercury"):
            for j in range(0, int(days) + 1, 7):
                a1 = _pos13("Earth", j, 1, 0, 0, False); b1 = _pos13(nm, j, 1, 0, 0, False, ph0=1.0)
                acc[nm].append(math.hypot(a1[0] - b1[0], a1[1] - b1[1]))
            x, y, _ = _pos13(nm, days, k, cx, cy, sq, ph0=1.0); paste_c(img, planet_sprite(11, PL13[nm][2]), x, y)
            d = ImageDraw.Draw(img); d.line([(ex, ey), (x, y)], fill=mix(SPACE, PL13[nm][2], 0.6), width=2)
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1200, 300, 1860, 860], 26, fill=(10, 8, 16, 230), outline=TICK13 + (160,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img); d.text((1530, 350), "average distance from Earth", font=F(34, "Bold"), fill=DIM, anchor="mm")
        for i, nm in enumerate(("Venus", "Mercury")):
            m_ = sum(acc[nm]) / len(acc[nm]); y = 470 + i * 200
            d.text((1250, y), nm, font=F(44, "Black"), fill=PL13[nm][2], anchor="lm"); d.text((1820, y), f"{m_:.2f} AU", font=F(56, "Black"), fill=WHITE, anchor="rm")
            d.rounded_rectangle([1250, y + 45, 1250 + 520 * min(1, m_ / 1.6), y + 75], 12, fill=PL13[nm][2])
        d.text((1530, 820), f"simulated: {days / 365.25:,.1f} years", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
        d.text((cx, 1030), "circular orbits, simplified", font=F(26, "Medium"), fill=DIM, anchor="mm")
    else:
        a2 = PL13[tgt][0]; r1, r2 = k * (1 if not sq else 1), k * (math.sqrt(a2) if sq else a2)
        th0 = math.radians(200); ex, ey = cx + r1 * math.cos(th0), cy - r1 * math.sin(th0)
        tx_end = (cx + r2 * math.cos(th0 + math.pi), cy - r2 * math.sin(th0 + math.pi))
        if v.get("ghost") or v.get("straight"):
            tq = th0 + math.pi * (0.62 if not v.get("straight") else 0.35)
            gx, gy = cx + r2 * math.cos(tq), cy - r2 * math.sin(tq)
            for j in range(0, 40, 2):
                d.line([(lerp(ex, gx, j / 40), lerp(ey, gy, j / 40)), (lerp(ex, gx, (j + 1) / 40), lerp(ey, gy, (j + 1) / 40))], fill=(200, 200, 215) if not v.get("straight") else ROAD13, width=4)
            if v.get("straight"):
                px, py = lerp(ex, gx, p), lerp(ey, gy, p); paste_c(img, radial(50, [(0, (255, 255, 255, 255)), (1, ROAD13 + (0,))]), px, py)
                paste_c(img, planet_sprite(16, PL13[tgt][2]), gx, gy)
            else:
                d.text(((ex + gx) / 2, (ey + gy) / 2 - 30), "straight line: not how it works", font=F(30, "Bold"), fill=(220, 220, 230), anchor="mm")
        if not v.get("straight"):
            a_ = (r1 + r2) / 2; c_ = (r2 - r1) / 2; b_ = math.sqrt(max(1, a_ * a_ - c_ * c_))
            pts = []
            for j in range(int(60 * p) + 1):
                E = math.pi * j / 60; xx = -c_ + a_ * math.cos(E) if False else a_ * math.cos(E) - c_; yy = b_ * math.sin(E)
                # ellipse with the Sun at a focus, perihelion at Earth (angle th0)
                ang = th0 + math.atan2(yy, -xx) if False else th0 + E
                rr = r1 + (r2 - r1) * (1 - math.cos(E)) / 2
                pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
            if len(pts) > 1: d.line(pts, fill=BOARD13, width=5)
            if pts: paste_c(img, radial(46, [(0, (255, 255, 255, 255)), (1, BOARD13 + (0,))]), *pts[-1])
            tth = th0 + math.pi - math.pi * 0.35 * (1 - p)
            paste_c(img, planet_sprite(18 if sq else 20, PL13[tgt][2]), cx + r2 * math.cos(tth), cy - r2 * math.sin(tth))
            d = ImageDraw.Draw(img)
            if v.get("days"):
                box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1360, 420, 1860, 700], 26, fill=(10, 8, 16, 230), outline=BOARD13 + (160,), width=3); img.alpha_composite(box)
                d = ImageDraw.Draw(img); dd = v["days"] * p
                d.text((1610, 480), f"to {tgt}", font=F(36, "Bold"), fill=DIM, anchor="mm")
                d.text((1610, 570), f"{dd:,.0f} days" if v["days"] < 1000 else f"{dd / 365.25:,.1f} years", font=F(72, "Black"), fill=BOARD13, anchor="mm")
        paste_c(img, earth_sprite(15, glow=None), ex, ey); d = ImageDraw.Draw(img)
        d.text((ex - 20, ey + 34), "Earth", font=F(28, "Bold"), fill=(140, 190, 255), anchor="mm")
        if sq: d.text((cx, 1030), "square-root scale; path illustrative", font=F(26, "Medium"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 95), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 70)

def sc_slingshot(img, v, t, dur):
    """gravity assist: mode boost (probe swings behind a moving planet and speeds up) | brake (probe falling sunward passes in front of a
    planet and slows) | tour (Voyager 2 Grand Tour: Jupiter 1979, Saturn 1981, Uranus 1986, Neptune 1989; square-root scale, illustrative)"""
    mode = v.get("mode", "boost"); d = ImageDraw.Draw(img)
    if mode == "tour":
        cx, cy = 520, 600; k = 430 / math.sqrt(30.07)
        paste_c(img, sun_sprite(12), cx, cy); d = ImageDraw.Draw(img)
        stops = [("Earth", 1977.6, 1.0, 200), ("Jupiter", 1979.5, 5.203, 160), ("Saturn", 1981.6, 9.537, 125), ("Uranus", 1986.1, 19.19, 95), ("Neptune", 1989.6, 30.07, 70)]
        for nm, yr, a, ang in stops:
            r = k * math.sqrt(a); d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=mix(SPACE, PL13[nm][2], 0.4), width=2)
        p = easeio((t - 0.3) / max(1.0, dur * 0.8)); yr_now = lerp(1977.6, 1989.6, p)
        pts = []
        for j in range(len(stops) - 1):
            n0, y0_, a0, g0 = stops[j]; n1, y1_, a1, g1 = stops[j + 1]
            for q in range(21):
                f = q / 20; yy = lerp(y0_, y1_, f)
                if yy > yr_now: break
                r = k * math.sqrt(lerp(a0, a1, f)); g = math.radians(lerp(g0, g1, f)); pts.append((cx + r * math.cos(g), cy - r * math.sin(g)))
        if len(pts) > 1: d.line(pts, fill=BOARD13, width=5)
        for nm, yr, a, ang in stops:
            r = k * math.sqrt(a); g = math.radians(ang); x, y = cx + r * math.cos(g), cy - r * math.sin(g)
            paste_c(img, planet_sprite(14 if nm != "Earth" else 10, PL13[nm][2]) if nm != "Earth" else earth_sprite(10, glow=None), x, y)
            d = ImageDraw.Draw(img)
            if yr_now >= yr - 0.05: d.text((x + 22, y - 22), f"{nm} {int(yr)}", font=F(30, "ExtraBold"), fill=PL13[nm][2], anchor="lb")
        if pts: paste_c(img, radial(40, [(0, (255, 255, 255, 255)), (1, BOARD13 + (0,))]), *pts[-1])
        d = ImageDraw.Draw(img)
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1180, 380, 1860, 760], 26, fill=(10, 8, 16, 230), outline=BOARD13 + (160,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img); d.text((1520, 450), "Voyager 2 mission clock", font=F(34, "Bold"), fill=DIM, anchor="mm")
        d.text((1520, 560), f"{yr_now - 1977.6:,.1f} years", font=F(90, "Black"), fill=BOARD13, anchor="mm")
        d.text((1520, 680), "alignment: about once every 175 years", font=F(30, "ExtraBold"), fill=ROAD13, anchor="mm")
        d.text((cx, 1030), "square-root scale; positions illustrative", font=F(26, "Medium"), fill=DIM, anchor="mm")
    else:
        pc = (900, 560); pr = 120; pn = v.get("planet", "Venus" if mode == "brake" else "Jupiter")
        cyc = 4.0; ph = (t % cyc) / cyc
        # planet moves left->right; probe comes in and bends around it
        ox = (ph - 0.5) * 120
        paste_c(img, planet_sprite(pr, PL13[pn][2], light=(-0.7, -0.4)), pc[0] + ox, pc[1])
        d = ImageDraw.Draw(img)
        d.line([(pc[0] - 260 + ox, pc[1] + pr + 40), (pc[0] + 260 + ox, pc[1] + pr + 40)], fill=PL13[pn][2], width=4)
        d.polygon([(pc[0] + 260 + ox, pc[1] + pr + 28), (pc[0] + 285 + ox, pc[1] + pr + 40), (pc[0] + 260 + ox, pc[1] + pr + 52)], fill=PL13[pn][2])
        d.text((pc[0] + ox, pc[1] + pr + 80), f"{pn}'s motion around the Sun", font=F(28, "Bold"), fill=PL13[pn][2], anchor="mm")
        pts = []; sgn = 1 if mode == "boost" else -1
        for j in range(int(80 * ph) + 1):
            u = j / 80 * 2 - 1
            x = pc[0] + ox + 520 * u; y = pc[1] - sgn * (pr + 60) * (1 / (1 + 6 * u * u)) * 1.0 + sgn * 0 - (260 * u if mode == "boost" else -260 * u) * 0.0
            yy = pc[1] - sgn * (pr + 50) - sgn * 300 * abs(u) ** 1.6 * (1 if u > 0 else 0.6)
            pts.append((pc[0] + ox + 520 * u * (1 if mode == "boost" else -1), yy))
        if len(pts) > 1: d.line(pts, fill=BOARD13, width=5)
        if pts: paste_c(img, radial(44, [(0, (255, 255, 255, 255)), (1, BOARD13 + (0,))]), *pts[-1])
        d = ImageDraw.Draw(img)
        sp = 0.5 + (0.35 if mode == "boost" else -0.3) * easeio((ph - 0.35) / 0.3)
        gx, gy, gr = 1580, 640, 190
        d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 180, 360, fill=(70, 70, 90), width=26)
        d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 180, 180 + 180 * sp, fill=BOARD13 if mode == "boost" else TICK13, width=26)
        ang = math.pi * (1 - sp); d.line([(gx, gy), (gx + (gr - 30) * math.cos(ang), gy - (gr - 30) * math.sin(ang))], fill=WHITE, width=7)
        d.text((gx, gy + 60), "probe speed vs the Sun", font=F(32, "Bold"), fill=DIM, anchor="mm")
        d.text((gx, gy + 120), "SPEED GAINED" if mode == "boost" else "SPEED SHED", font=F(52, "Black"), fill=BOARD13 if mode == "boost" else TICK13, anchor="mm")
        if mode == "brake":
            paste_c(img, sun_sprite(30), 150, 560); d = ImageDraw.Draw(img); d.text((150, 680), "toward the Sun", font=F(28, "Bold"), fill=ROAD13, anchor="mm")
        d.text((W / 2, 1030), "gravity assist, illustration", font=F(26, "Medium"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 110), v["head"], F(56, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.5) / 0.5), y=H - 80)


# ---------------- scenes (EP14) ----------------
TEAL14, IMPACT14, FOAM14, ABYSS14, SAND14 = (40, 205, 195), (255, 128, 46), (222, 242, 255), (6, 24, 52), (120, 92, 64)

def _rock14(r, seed=3, hot=0.0):
    """irregular shaded rock sprite (potato shape); hot 0..1 adds an entry glow"""
    r = max(2, int(r)); key = ("rock14", r, seed, round(hot, 2))
    if key in _pl: return _pl[key]
    pad = int(r * 0.8) + 4; s = 2 * r + 2 * pad
    yy, xx = np.mgrid[0:s, 0:s].astype(np.float32)
    nx, ny = (xx - s / 2) / r, (yy - s / 2) / r
    ang = np.arctan2(ny, nx); rng = np.random.default_rng(seed)
    ph = rng.uniform(0, 6.28, 4); amp = [0.10, 0.07, 0.05, 0.03]
    rad = 1 + sum(a * np.sin((k + 2) * ang + p) for k, (a, p) in enumerate(zip(amp, ph)))
    dd = np.sqrt(nx ** 2 + ny ** 2) / rad
    inside = dd <= 1
    nz = np.sqrt(np.clip(1 - dd ** 2, 0, 1))
    shade = np.clip((-0.7 * nx - 0.5 * ny + 0.5 * nz) / 1.0, 0, 1) * 0.9 + 0.1
    lo = Image.fromarray((rng.random((8, 8)) * 255).astype(np.uint8)).resize((s, s), Image.BICUBIC)
    tex = np.asarray(lo, np.float32) / 255
    base = np.array([118, 104, 92], np.float32)
    rgb = base[None, None, :] * (0.75 + 0.5 * tex[..., None]) * shade[..., None]
    a = np.where(inside, 255, 0).astype(np.float32)
    if hot > 0:
        rim = np.clip(1 - np.abs(dd - 1) / 0.25, 0, 1)
        rgb = rgb * (1 - rim[..., None] * hot) + np.array(IMPACT14, np.float32) * rim[..., None] * hot
        gl = np.clip((1.6 - dd) / 0.6, 0, 1) * (dd > 1) * hot
        rgb = np.where((dd > 1)[..., None], np.array((255, 170, 80), np.float32), rgb); a = np.maximum(a, gl * 150)
    img = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8), "RGBA")
    _pl[key] = img
    return img

def _nice_step(span):
    for s in (0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50):
        if span / s <= 7: return s
    return 100

def sc_oceancut(img, v, t, dur):
    """side cross-section TO SCALE: sky, ocean (v.depth km, default 3.7), seafloor; a rock of v.d_m metres falls in.
    v.view_km = vertical extent from the seafloor to the top of the frame; mode: drop (falls to the floor; if taller than the sea,
    'still sticking out' tag) | burst (explodes at v.alt km, shock ring, the sea is untouched) | crater (water cavity v.cav_km wide + rim
    wave + steam); v.everest = Everest silhouette on the floor; v.label = name under the rock size tag"""
    depth = v.get("depth", 3.7); view = v.get("view_km", 20.0); mode = v.get("mode", "drop")
    yF, yT = 990, 170; k = (yF - yT) / view; yS = yF - depth * k
    d = ImageDraw.Draw(img)
    # sky band (subtle) + sea + floor
    sky = Image.new("RGBA", (W, int(yS - yT)), (0, 0, 0, 0)); sd = ImageDraw.Draw(sky)
    for y in range(0, sky.height, 4):
        q = y / max(1, sky.height); sd.rectangle([0, y, W, y + 4], fill=(30, 60, 120, int(20 + 70 * q)))
    img.alpha_composite(sky, (0, int(yT)))
    sea = Image.new("RGBA", (W, max(1, int(yF - yS))), (0, 0, 0, 0)); wd = ImageDraw.Draw(sea)
    for y in range(0, sea.height, 2):
        q = y / max(1, sea.height); wd.rectangle([0, y, W, y + 2], fill=mix(TEAL14, ABYSS14, q ** 0.6) + (235,))
    img.alpha_composite(sea, (0, int(yS)))
    d = ImageDraw.Draw(img)
    floor = [(x, yF + 6 * math.sin(x / 90) + 4 * math.sin(x / 23)) for x in range(0, W + 20, 20)]
    d.polygon(floor + [(W, H), (0, H)], fill=SAND14)
    d.line([(0, yS), (W, yS)], fill=FOAM14, width=3)
    # ruler (left)
    st = _nice_step(view); kk = 0.0 if not v.get("bare") else view * 9
    if not v.get("bare"): d.line([(90, yF), (90, yT)], fill=(150, 165, 190), width=2)
    while kk <= view + 1e-6:
        y = yF - kk * k; d.line([(80, y), (100, y)], fill=(150, 165, 190), width=2)
        lab = f"{kk:g} km"; d.text((110, y), lab, font=F(22, "SemiBold"), fill=(170, 182, 205), anchor="lm"); kk += st
    if not v.get("bare"): d.text((W - 60, yS + 26), f"average ocean depth: {depth:g} km", font=F(28, "Bold"), fill=FOAM14, anchor="rm")
    if v.get("everest"):
        eh = 8.849 * k; ex = 1480
        d.polygon([(ex - eh * 0.9, yF), (ex - eh * 0.15, yF - eh * 0.82), (ex, yF - eh), (ex + eh * 0.35, yF - eh * 0.7), (ex + eh * 0.95, yF)], fill=(90, 96, 112))
        d.polygon([(ex - eh * 0.15, yF - eh * 0.82), (ex, yF - eh), (ex + eh * 0.35, yF - eh * 0.7), (ex + eh * 0.12, yF - eh * 0.78)], fill=(235, 240, 248))
        d.text((ex, yF - eh - 28), "Everest, 8.8 km", font=F(28, "Bold"), fill=WHITE, anchor="mm")
    # rock
    dkm = v.get("d_m", 1000) / 1000.0; rp = dkm / 2 * k; rr = max(4, rp)
    cx_end = v.get("x", 900)
    p = easeio((t - 0.4) / max(0.8, dur * 0.42))
    if mode == "burst":
        y_end = yF - v.get("alt", 30) * k
    else:
        y_end = yF - rp if rp * 2 > depth * k else yS + 0.6 * (yF - yS)
    x0, y0 = cx_end + 700, yT - rr - 60
    cx, cy = lerp(x0, cx_end, p), lerp(y0, y_end, p)
    hit_t = 0.4 + max(0.8, dur * 0.42)
    after = t - hit_t
    if mode == "burst" and after > 0:
        fl = max(0.0, 1 - after / 1.2)
        paste_c(img, radial(int(260 + 200 * min(1, after)), [(0, (255, 240, 200, int(255 * fl))), (0.3, (255, 170, 80, int(160 * fl))), (1, (255, 120, 40, 0))]), cx, cy)
        ring = 40 + after * 260; lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.ellipse([cx - ring, cy - ring, cx + ring, cy + ring], outline=(255, 220, 170, int(200 * max(0, 1 - after / 3))), width=5)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.text((cx, cy - 120), f"explodes ~{v.get('alt', 30):g} km up", font=F(34, "ExtraBold"), fill=WHITE, anchor="mm")
        if after > 1.5: d.text((W / 2, yS - 40), "the sea below: untouched", font=F(32, "Bold"), fill=TEAL14, anchor="mm")
    elif mode == "crater" and after > 0:
        q = ease(after / 1.6); cw = v.get("cav_km", 3) * k / 2 * q; ch = min(yF - yS - 2, cw * 0.9)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.chord([cx_end - cw, yS - ch, cx_end + cw, yS + ch], 0, 180, fill=(18, 26, 48, 255))
        rim = 20 + 60 * q * (1 - 0.5 * ease((after - 2) / 2))
        for side in (-1, 1):
            bx = cx_end + side * cw
            ld.polygon([(bx - side * 6, yS), (bx + side * rim * 0.4, yS - rim), (bx + side * rim * 1.6, yS)], fill=FOAM14 + (230,))
        img.alpha_composite(lay)
        for j in range(10):
            ph = (after * 0.6 + j / 10) % 1.0; sy = yS - ph * (yS - yT) * 0.8; sx = cx_end + math.sin(j * 2.1 + after) * 40 * (1 + ph * 3)
            paste_c(img, radial(int(80 + 140 * ph), [(0, (235, 240, 250, int(110 * (1 - ph)))), (1, (235, 240, 250, 0))]), sx, sy)
        d = ImageDraw.Draw(img)
        if after > 1.0: d.text((cx_end, yS - rim - 60), v.get("cav_label", "a hole in the water"), font=F(34, "ExtraBold"), fill=WHITE, anchor="mm")
    if not (mode in ("burst", "crater") and after > 0.15):
        hot = 0.9 if t > 0.5 else 0.0
        if p > 0.02 and rr < 60:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            for j in range(18):
                q = j / 18; ld.line([(lerp(cx, x0, q * 0.25), lerp(cy, y0, q * 0.25)), (lerp(cx, x0, (q + 0.05) * 0.25), lerp(cy, y0, (q + 0.05) * 0.25))], fill=IMPACT14 + (int(200 * (1 - q)),), width=max(2, int(rr * 0.6)))
            img.alpha_composite(lay)
        paste_c(img, _rock14(rr, seed=v.get("seed", 3), hot=v.get("hot", hot if rr < 200 else 0.4)), cx, cy)
        d = ImageDraw.Draw(img)
        if rp < 6:
            d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], outline=IMPACT14, width=3)
        if v.get("bare"): tag = ""
        else: tag = v.get("size", f"{v.get('d_m'):,} m" if v.get("d_m", 0) < 1000 else f"{dkm:g} km")
        d.text((cx + max(rr, 26) + 24, cy - 14), tag, font=F(40, "Black"), fill=IMPACT14, anchor="lm")
        if v.get("label"): d.text((cx + max(rr, 26) + 24, cy + 26), v["label"], font=F(26, "SemiBold"), fill=DIM, anchor="lm")
    if mode == "drop" and rp * 2 > depth * k and after > 0.2 and not v.get("bare"):
        d = ImageDraw.Draw(img)
        alpha_text(img, (cx_end, yS - (2 * rp - depth * k) - 60), "touches the seafloor, still sticking out of the sea", F(36, "ExtraBold"), WHITE, ease(after / 0.5))
        yy = yS - (2 * rp - depth * k)
        for x in range(int(cx_end - rp - 160), int(cx_end - rp - 20), 14): d.line([(x, yy), (x + 7, yy)], fill=FOAM14, width=2)
    if v.get("head"): alpha_text(img, (W / 2, 100), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.2) / 0.5), y=H - 50)

LADDER14 = [("18 m", 18, "Chelyabinsk-size"), ("140 m", 140, "NASA's danger line"), ("250 m", 250, "steam maker"), ("1 km", 1000, "ozone killer"), ("10 km", 10000, "Chicxulub")]
REFS14 = [("a person", 1.8), ("a bus", 12), ("Statue of Liberty", 93), ("Eiffel Tower", 330), ("Everest", 8849)]
def _lx14(m): return lerp(220, 1720, (math.log10(m) - math.log10(1)) / (math.log10(30000) - math.log10(1)))
def sc_sizeladder(img, v, t, dur):
    """chapter card: five rocks on a log size axis (1 m -> 30 km) with reference landmarks; v.n = current rock (1..5); later rocks are '?'"""
    n = v.get("n", 1); d = ImageDraw.Draw(img); y = 640
    head = f"ROCK {n} OF 5" if 1 <= n <= 5 else "FIVE ROCKS, ONE OCEAN"
    alpha_text(img, (W / 2, 140), head, F(74, "Black"), IMPACT14, ease(t / 0.4))
    alpha_text(img, (W / 2, 215), "same ocean, bigger rock" if n <= 5 else "the drop test, complete", F(34, "SemiBold"), DIM, ease((t - 0.2) / 0.4))
    d.line([(200, y), (1740, y)], fill=(90, 110, 150), width=4)
    for e in range(0, 5):
        x = _lx14(10 ** e); d.line([(x, y - 10), (x, y + 10)], fill=(90, 110, 150), width=3)
        d.text((x, y + 34), ["1 m", "10 m", "100 m", "1 km", "10 km"][e], font=F(24, "SemiBold"), fill=(130, 145, 175), anchor="mm")
    for lab, m in REFS14:
        x = _lx14(m); d.line([(x, y + 60), (x, y + 120)], fill=(70, 85, 120), width=2)
        d.text((x, y + 150), lab, font=F(24, "Medium"), fill=(150, 160, 185), anchor="mm")
        d.text((x, y + 180), f"{m:g} m" if m < 1000 else f"{m / 1000:.1f} km", font=F(22, "Medium"), fill=(110, 120, 150), anchor="mm")
    for i, (lab, m, nick) in enumerate(LADDER14):
        xa = _lx14(m); x = 380 + i * 300; r = 26 + i * 16; cy = y - 190
        d.line([(x, cy + r + (64 if i + 1 == n else 8)), (xa, y - 8)], fill=(70, 85, 120), width=2)
        d.ellipse([xa - 7, y - 7, xa + 7, y + 7], fill=IMPACT14 if i + 1 <= n else (70, 85, 120))
        if i + 1 < n or n > 5:
            paste_c(img, _rock14(r, seed=i + 2), x, cy, 0.45); d = ImageDraw.Draw(img)
            d.text((x, cy - r - 30), lab, font=F(30, "Bold"), fill=DIM, anchor="mm")
        elif i + 1 == n:
            a = ease((t - 0.4) / 0.5); pul = 1 + 0.04 * math.sin(t * 4)
            paste_c(img, radial(int(r * 5), [(0, IMPACT14 + (110,)), (1, IMPACT14 + (0,))]), x, cy, a)
            paste_c(img, _rock14(int(r * pul), seed=i + 2), x, cy, a); d = ImageDraw.Draw(img)
            d.text((x, cy - r - 44), lab, font=F(48, "Black"), fill=mix(SPACE, WHITE, a), anchor="mm")
            d.text((x, cy + r + 36), nick, font=F(28, "Bold"), fill=mix(SPACE, IMPACT14, a), anchor="mm")
        else:
            dash_circle10(d, x, cy, r, (80, 95, 130), w=3)
            d.text((x, cy), "?", font=F(int(r * 0.9) + 10, "Black"), fill=(80, 95, 130), anchor="mm")
    caption(img, v.get("caption"), ease((t - 1.5) / 0.5), y=H - 90)

def _ringpts14(theta, tilt, cx, cy, R, n=180):
    """points of a small circle at angular distance theta from an impact point tilted `tilt` rad toward the viewer (orthographic)"""
    pts = []
    for j in range(n + 1):
        ph = 2 * math.pi * j / n
        x, y, z = math.sin(theta) * math.cos(ph), math.sin(theta) * math.sin(ph), math.cos(theta)
        y2, z2 = y * math.cos(tilt) - z * math.sin(tilt), y * math.sin(tilt) + z * math.cos(tilt)
        pts.append((cx + R * x, cy + R * y2, z2))
    return pts

def sc_wavering(img, v, t, dur):
    """mode local: top-down sea, rings spread from the impact, a coastline at v.coast_km (scale v.view_km across), clock + wave-height readout
    from v.heights [[t_frac, text]]; mode global: a globe with rings sweeping over it from v.lat (tilt), clock to v.hours"""
    mode = v.get("mode", "local"); d = ImageDraw.Draw(img)
    p = min(1.0, max(0.0, (t - 0.3) / max(1.0, dur * 0.85)))
    if mode == "global":
        cx, cy, Rg = 760, 580, 400
        paste_c(img, earth_sprite(Rg, light=(-0.7, -0.4)), cx, cy)
        tilt = math.radians(v.get("tilt", 35))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for j in range(4):
            th = (p * math.pi * 0.72) - j * 0.12
            if th <= 0.02: continue
            pts = _ringpts14(th, tilt, cx, cy, Rg)
            seg = []
            for (x, y, z) in pts:
                if z > 0: seg.append((x, y))
                elif len(seg) > 1: ld.line(seg, fill=FOAM14 + (int(230 * (1 - j * 0.22)),), width=6 - j); seg = []
                else: seg = []
            if len(seg) > 1: ld.line(seg, fill=FOAM14 + (int(230 * (1 - j * 0.22)),), width=6 - j)
        ip = _ringpts14(0.0, tilt, cx, cy, Rg, n=1)[0]
        ld.ellipse([ip[0] - 12, ip[1] - 12, ip[0] + 12, ip[1] + 12], fill=IMPACT14 + (255,))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        hrs = v.get("hours", 48) * p
        d.text((1500, 420), f"{hrs:,.0f} h" if hrs >= 1 else f"{hrs * 60:,.0f} min", font=F(120, "Black"), fill=FOAM14, anchor="mm")
        d.text((1500, 510), "after impact", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
    else:
        cx, cy = 560, 600; R0 = 420; view = v.get("view_km", 300); k = R0 / (view / 2)
        disk = radial(2 * R0 + 40, [(0, (30, 140, 160, 200)), (0.9, (12, 60, 110, 200)), (1, (12, 60, 110, 0))]); paste_c(img, disk, cx, cy)
        ck = v.get("coast_km")
        if ck:
            cxk = cx + ck * k
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            pts = [(cxk + 18 * math.sin(yy / 40) + 8 * math.sin(yy / 13), yy) for yy in range(80, 1060, 20)]
            ld.polygon(pts + [(1120, 1060), (1120, 80)], fill=(92, 120, 70, 255)); img.alpha_composite(lay); d = ImageDraw.Draw(img)
            d.text((cxk + 60, 200), v.get("coast", "coast"), font=F(32, "Bold"), fill=WHITE, anchor="lm")
            d.text((cxk + 60, 245), f"{ck:g} km away", font=F(28, "SemiBold"), fill=(220, 230, 200), anchor="lm")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        reach = p * v.get("reach_km", view) * k
        for j in range(5):
            rr = reach - j * 26
            if rr <= 4: continue
            aa = int(220 * (1 - j / 5) * (1 - 0.6 * p))
            ld.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=FOAM14 + (aa,), width=max(2, 6 - j))
        ld.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=IMPACT14 + (255,))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.line([(cx - R0, 1030), (cx - R0 + 100 * k, 1030)], fill=WHITE, width=4); d.text((cx - R0, 1000), "100 km", font=F(24, "SemiBold"), fill=WHITE, anchor="lm")
        mins = v.get("minutes", 30) * p
        d.text((1500, 420), f"{mins:,.0f} min", font=F(110, "Black"), fill=FOAM14, anchor="mm")
        d.text((1500, 505), "after impact", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
    cur = None
    for fr, txt in v.get("heights", []):
        if p >= fr: cur = txt
    if cur:
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1210, 590, 1790, 760], 24, fill=(6, 16, 34, 230), outline=TEAL14 + (200,), width=3); img.alpha_composite(box)
        d = ImageDraw.Draw(img); d.text((1500, 645), v.get("hlabel", "wave height"), font=F(30, "Bold"), fill=DIM, anchor="mm")
        d.text((1500, 710), cur, font=F(58, "Black"), fill=TEAL14, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 100), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.2) / 0.5), y=H - 50)

def sc_plume(img, v, t, dur):
    """side view of the atmosphere (0-60 km: troposphere to 12 km, stratosphere 12-50 km); mode vapor: a steam column rises from the sea into
    the stratosphere + counter (v.count, v.unit); mode ozone: the ozone layer (~15-35 km) thins + UV index meter 0-60 (WHO 'extreme' 11+),
    needle to v.uv"""
    mode = v.get("mode", "vapor"); d = ImageDraw.Draw(img)
    yG, yT = 990, 180; k = (yG - yT) / 60.0; X1 = 1250 if mode == "ozone" else W - 80
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.rectangle([80, yG - 12 * k, X1, yG], fill=(40, 90, 160, 60)); ld.rectangle([80, yG - 50 * k, X1, yG - 12 * k], fill=(70, 60, 150, 45))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.rectangle([80, yG, X1, yG + 40], fill=mix(TEAL14, ABYSS14, 0.4))
    for km, lab in [(12, "12 km: airliners, top of the weather"), (50, "50 km: top of the stratosphere")]:
        y = yG - km * k
        for x in range(80, X1, 18): d.line([(x, y), (x + 9, y)], fill=(150, 160, 200), width=2)
        d.text((100, y - 22), lab, font=F(24, "SemiBold"), fill=(170, 180, 215), anchor="lm")
    d.text((100, yG - 6 * k), "troposphere", font=F(28, "Bold"), fill=(130, 175, 230), anchor="lm")
    d.text((100, yG - 31 * k), "stratosphere", font=F(28, "Bold"), fill=(160, 140, 235), anchor="lm")
    p = ease((t - 0.3) / max(1.0, dur * 0.7))
    if mode == "vapor":
        cx = 900; top = v.get("top_km", 40) * k * p
        for j in range(60):
            q = j / 60; y = yG - top * q; w = 30 + 90 * q + (220 * ease((q - 0.55) / 0.45) if q > 0.55 else 0)
            x = cx + math.sin(q * 9 + t * 1.5) * 18
            paste_c(img, radial(int(w * 2), [(0, (235, 240, 250, int(80 * (0.5 + 0.5 * q)))), (1, (235, 240, 250, 0))]), x, y)
        d = ImageDraw.Draw(img)
        cnt = v.get("count", 250) * p
        d.text((1560, 330), f"{cnt:,.0f}", font=F(120, "Black"), fill=FOAM14, anchor="mm")
        d.text((1560, 420), v.get("unit", "million tonnes of water"), font=F(32, "Bold"), fill=DIM, anchor="mm")
        d.text((1560, 465), "thrown up as steam", font=F(32, "Bold"), fill=DIM, anchor="mm")
    else:
        th = 1 - 0.75 * p
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for x in range(80, X1, 6):
            hole = 0.5 + 0.5 * math.sin(x / 70 + 1.3) * math.sin(x / 23)
            a = int(170 * max(0.05, th - 0.3 * hole * p))
            ld.line([(x, yG - 35 * k), (x, yG - 15 * k)], fill=(120, 230, 170, a), width=6)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.text((X1 - 20, yG - 25 * k), "ozone layer", font=F(30, "ExtraBold"), fill=(150, 240, 190), anchor="rm")
        # sun rays reaching the ground grow with p
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for j in range(9):
            x = 220 + j * 115; ld.line([(x + 200, yT), (x, yG)], fill=(190, 120, 255, int(40 + 120 * p)), width=4)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        # UV meter
        mx0, mx1, my = 1420, 1840, 900
        d.text((1630, 230), "UV INDEX", font=F(44, "Black"), fill=WHITE, anchor="mm")
        for u in range(0, 61, 2):
            y = lerp(my, 300, u / 60); c = (80, 200, 120) if u < 3 else (240, 220, 80) if u < 6 else (255, 150, 60) if u < 8 else (240, 80, 70) if u < 11 else (170, 90, 230)
            d.rectangle([1540, y - 8, 1600, y + 8], fill=c)
        for u, lab in [(0, "0"), (11, "11+ extreme (WHO)"), (30, "30"), (60, "60")]:
            y = lerp(my, 300, u / 60); d.text((1620, y), lab, font=F(24, "SemiBold"), fill=(200, 205, 225), anchor="lm")
        uv = lerp(v.get("uv0", 10), v.get("uv", 56), p); y = lerp(my, 300, uv / 60)
        d.polygon([(1525, y), (1495, y - 16), (1495, y + 16)], fill=WHITE)
        d.text((1480, y), f"{uv:.0f}", font=F(54, "Black"), fill=WHITE, anchor="rm")
    if v.get("head"): alpha_text(img, (W / 2, 100), v["head"], F(54, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.2) / 0.5), y=H - 50)

# ---------------- EP15 scenes: Voyager 1, one light-day away ----------------
GOLD15, DSN15, PLASMA15, NAVY15, PALE15 = (240, 190, 80), (90, 230, 150), (170, 120, 255), (8, 12, 30), (200, 220, 255)
AU_S15 = 499.005  # light-seconds per AU
V1_AU15 = 173.1
LM15 = [("Sun", 1.0), ("Jupiter", 5.2), ("Saturn", 9.5), ("Neptune", 30.1), ("Pale Blue Dot", 40.0), ("Termination shock", 94.0),
        ("Heliopause", 121.0), ("Voyager 1", V1_AU15)]

def _hms15(s):
    if s < 60: return f"{s:,.1f} s"
    h = int(s // 3600); m = int(s % 3600 // 60); sec = int(s % 60)
    return f"{h:d}:{m:02d}:{sec:02d}"

def voyager15(img, x, y, s=1.0, ang=-0.4, a=1.0):
    """code-drawn Voyager: dish (white), bus (dark gold), magnetometer boom (long thin), RTG boom with 3 cylinders"""
    lay = Image.new("RGBA", (int(260 * s) + 40, int(260 * s) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    c = lay.width / 2
    def P(px, py):
        ca, sa = math.cos(ang), math.sin(ang); return (c + (px * ca - py * sa) * s, c + (px * sa + py * ca) * s)
    d.line([P(0, 0), P(-120, 40)], fill=(170, 170, 180, int(255 * a)), width=max(1, int(2 * s)))  # magnetometer boom
    d.line([P(0, 0), P(70, 60)], fill=(150, 150, 160, int(255 * a)), width=max(2, int(4 * s)))   # RTG boom
    for k in range(3):
        q = P(46 + k * 12, 40 + k * 10); r = 6 * s; d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(110, 105, 100, int(255 * a)))
    b = [P(-14, 6), P(14, 6), P(14, 26), P(-14, 26)]; d.polygon(b, fill=(190, 150, 70, int(255 * a)))
    dish = [P(60 * math.cos(u) * 0.95, -6 + 14 * math.sin(u)) for u in [i * math.pi / 20 for i in range(41)]]
    d.polygon(dish, fill=(236, 238, 245, int(255 * a))); d.line([P(0, -6), P(0, -40)], fill=(220, 220, 230, int(255 * a)), width=max(1, int(2 * s)))
    img.alpha_composite(lay, (int(x - c), int(y - c)))

def _sx15(au, x0=170, x1=1730): return x0 + (x1 - x0) * math.sqrt(max(0.0, au) / V1_AU15)

def sc_signalrun(img, v, t, dur):
    """Earth -> Voyager 1 track on a SQUARE-ROOT scale with landmarks; a radio pulse travels from v.h0 to v.h1 hours (light time),
    passed landmarks light up, clock = time since sending; v.focus = landmark name to ring"""
    d = ImageDraw.Draw(img); y = 600; x0, x1 = 170, 1730
    p = easeio((t - 0.4) / max(1.0, dur * 0.75))
    h0, h1 = v.get("h0", 0.0), v.get("h1", 24.0); hrs = lerp(h0, h1, p) if v.get("log") is None else math.exp(lerp(math.log(max(1e-4, h0)), math.log(h1), p))
    au = hrs * 3600 / AU_S15; px = _sx15(min(au, V1_AU15))
    d.line([(x0, y), (x1, y)], fill=(50, 62, 100), width=4)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for j in range(26):
        u = j / 26; dl.line([(px - 300 * u, y), (px - 300 * (u + 0.04), y)], fill=DSN15 + (int(230 * (1 - u)),), width=8)
    img.alpha_composite(lay)
    R_e = 22; paste_c(img, earth_sprite(R_e, glow=None), x0 - 40, y)
    d = ImageDraw.Draw(img); d.text((x0 - 40, y + 50), "Earth", font=F(28, "Bold"), fill=WHITE, anchor="mm")
    for i, (n, a_) in enumerate(LM15):
        x = _sx15(a_); hit = au >= a_ - 1e-6; col = GOLD15 if hit else (110, 120, 150)
        if n == "Voyager 1":
            voyager15(img, x + 10, y - 6, 0.55, ang=-0.3); d = ImageDraw.Draw(img)
            d.text((x, y + 70), "Voyager 1", font=F(30, "Black"), fill=GOLD15 if hit else WHITE, anchor="mm")
            continue
        up = i % 2 == 0
        d.line([(x, y - 16), (x, y + 16)], fill=col, width=4)
        ly = y - 60 if up else y + 60
        d.text((x, ly), n, font=F(28, "Bold"), fill=col, anchor="mm")
        d.text((x, ly + (-34 if up else 34)), _hms15(a_ * AU_S15), font=F(24, "SemiBold"), fill=DIM if not hit else WHITE, anchor="mm")
        if v.get("focus") == n:
            q = 0.5 + 0.5 * math.sin(t * 4); d.ellipse([x - 34, y - 34, x + 34, y + 34], outline=mix(col, WHITE, q), width=4)
    R_p = radial(70, [(0, (255, 255, 255, 255)), (0.4, DSN15 + (200,)), (1, DSN15 + (0,))]); paste_c(img, R_p, px, y)
    d = ImageDraw.Draw(img)
    d.text((W / 2, 230), _hms15(hrs * 3600), font=F(120, "Black"), fill=DSN15, anchor="mm")
    d.text((W / 2, 320), "since the message left Earth", font=F(34, "SemiBold"), fill=DIM, anchor="mm")
    d.text((W / 2, 880), f"{au * 149.6:,.1f} million km" if au < 7 else f"{au * 0.1496:,.2f} billion km", font=F(56, "Black"), fill=WHITE, anchor="mm")
    d.text((x1, y - 150), "square-root scale", font=F(24, "SemiBold"), fill=DIM, anchor="rm")
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(44, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 70)

def sc_signaldial(img, v, t, dur):
    """chapter card: a 24-hour dial filling to v.h (hours of light time), v.stamp in the middle, v.title / v.sub / v.fact at right"""
    cx, cy, Rr = 500, 560, 330; d = ImageDraw.Draw(img)
    hv = v.get("h", 0.0); p = easeio((t - 0.2) / 1.6)
    d.ellipse([cx - Rr, cy - Rr, cx + Rr, cy + Rr], outline=(40, 50, 80), width=26)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    frac = min(1.0, max(0.0, hv / 24.0)) * p
    if frac > 0.0005: dl.arc([cx - Rr, cy - Rr, cx + Rr, cy + Rr], -90, -90 + 360 * max(frac, 0.004), fill=DSN15 + (255,), width=26)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    for k in range(24):
        a = -math.pi / 2 + 2 * math.pi * k / 24; r1, r2 = Rr + 26, Rr + (46 if k % 6 == 0 else 36)
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)), (cx + r2 * math.cos(a), cy + r2 * math.sin(a))], fill=(140, 150, 180), width=3)
        if k % 6 == 0: d.text((cx + (Rr + 80) * math.cos(a), cy + (Rr + 80) * math.sin(a)), f"{k}h", font=F(30, "Bold"), fill=DIM, anchor="mm")
    ang = -math.pi / 2 + 2 * math.pi * frac
    paste_c(img, radial(64, [(0, (255, 255, 255, 255)), (1, DSN15 + (0,))]), cx + Rr * math.cos(ang), cy + Rr * math.sin(ang))
    d = ImageDraw.Draw(img)
    d.text((cx, cy - 40), v.get("stamp", ""), font=F(110 if len(v.get("stamp", "")) < 8 else 84, "Black"), fill=WHITE, anchor="mm")
    d.text((cx, cy + 50), v.get("unit", "after sending"), font=F(32, "SemiBold"), fill=DIM, anchor="mm")
    a1, a2, a3 = ease((t - 0.3) / 0.5), ease((t - 0.7) / 0.5), ease((t - 1.1) / 0.5)
    alpha_text(img, (980, 380), v.get("kicker", ""), F(36, "Bold"), DSN15, a1, anchor="lm")
    lines = v.get("title", "").split("\n")
    for i, l in enumerate(lines): alpha_text(img, (980, 470 + i * 96), l, F(84, "Black"), WHITE, a1, anchor="lm", dy=(1 - a1) * 30)
    yy = 470 + len(lines) * 96
    alpha_text(img, (980, yy), v.get("sub", ""), F(40, "SemiBold"), GOLD15, a2, anchor="lm")
    if v.get("fact"): alpha_text(img, (980, yy + 70), v["fact"], F(34, "Medium"), PALE15, a3, anchor="lm")

def sc_heliobubble(img, v, t, dur):
    """the Sun's bubble seen from the side: termination shock (94 AU) + heliopause (121 AU) TO SCALE on the nose, a tail away from the
    interstellar wind; Voyager 1 (up-right) and Voyager 2 (down-right) tracks grow with a year counter; mode shock | pause | out;
    v.chart = particle chart at right (solar particles fall, cosmic rays rise at the crossing; illustration)"""
    mode = v.get("mode", "pause"); cx, cy, k = 820, 600, 3.3
    d = ImageDraw.Draw(img); p = easeio((t - 0.3) / max(1.0, dur * 0.7))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    def shell(r_au, col, a, w, fill=None):
        rr = r_au * k; pts = []
        for j in range(181):
            th = math.pi * j / 180 * 2; c = math.cos(th)
            r = rr * (1 + 0.9 * max(0.0, -c) ** 1.4)  # tail stretched to the left
            pts.append((cx + r * c, cy + r * math.sin(th) * (0.86 + 0.06 * c)))
        if fill: dl.polygon(pts, fill=fill)
        dl.line(pts + [pts[0]], fill=col + (a,), width=w)
    shell(121, PLASMA15, 230 if mode != "shock" else 120, 5, fill=(60, 40, 120, 40))
    shell(94, GOLD15, 220 if mode != "pause" else 110, 4)
    for j in range(14):  # interstellar wind streaks from the right
        yy = 160 + j * 62; xx = (W + 200 - (t * 160 + j * 97) % 700)
        dl.line([(xx, yy), (xx + 90, yy)], fill=(150, 160, 220, 70), width=2)
    img.alpha_composite(lay)
    paste_c(img, sun_sprite(8), cx, cy); d = ImageDraw.Draw(img)
    yr_end = {"shock": 2004.96, "pause": 2012.65, "out": 2026.9}[mode]
    yr = lerp(1977.7, yr_end, p)
    def au_at(year, craft):  # piecewise-linear from known points (approx.)
        pts = [(1977.7, 0), (1979.2, 5.2), (1980.9, 9.5), (1990.1, 40), (2004.96, 94), (2012.65, 121), (2026.9, 173.1)] if craft == 1 else \
              [(1977.6, 0), (1979.5, 5.2), (1981.6, 9.5), (1986.1, 19.2), (1989.6, 30), (2007.7, 84), (2018.85, 119), (2026.9, 145)]
        for (y0, a0), (y1, a1) in zip(pts, pts[1:]):
            if year <= y1: return lerp(a0, a1, (year - y0) / (y1 - y0))
        return pts[-1][1]
    for craft, ang, col in [(1, math.radians(-34), GOLD15), (2, math.radians(30), PALE15)]:
        r = au_at(yr, craft) * k; x1, y1 = cx + r * math.cos(ang), cy + r * math.sin(ang) * 0.92
        d.line([(cx, cy), (x1, y1)], fill=col, width=3)
        if craft == 1: voyager15(img, x1, y1, 0.36, ang=-0.6); d = ImageDraw.Draw(img)
        else: d.ellipse([x1 - 6, y1 - 6, x1 + 6, y1 + 6], fill=col)
        d.text((x1 + 30, y1 - 24 if craft == 1 else y1 + 24), f"Voyager {craft}", font=F(28, "Bold"), fill=col, anchor="lm")
    d.text((cx + 94 * k * 0.72, cy - 94 * k * 0.66 - 30), "termination shock · 94 AU", font=F(26, "Bold"), fill=GOLD15, anchor="rm")
    d.text((cx + 121 * k * 0.5, cy + 121 * k * 0.92 * 0.86 + 34), "heliopause · 121 AU", font=F(26, "Bold"), fill=PLASMA15, anchor="mm")
    d.text((cx - 470, cy), "the Sun's bubble", font=F(30, "SemiBold"), fill=(150, 140, 210), anchor="mm")
    d.text((1700, 140), f"{int(yr)}", font=F(96, "Black"), fill=WHITE, anchor="mm")
    if v.get("chart"):
        x0, y0, cw, ch = 1380, 640, 470, 300
        d.rounded_rectangle([x0 - 20, y0 - 60, x0 + cw + 20, y0 + ch + 60], 18, fill=(8, 10, 24))
        d.text((x0, y0 - 30), "particles hitting Voyager 1, 2012", font=F(24, "Bold"), fill=DIM, anchor="lm")
        q = p; n = 80
        for name, col, f in [("from the Sun", GOLD15, lambda u: 0.8 - 0.75 / (1 + math.exp(-(u - 0.62) * 40))),
                             ("from deep space", PLASMA15, lambda u: 0.35 + 0.35 / (1 + math.exp(-(u - 0.62) * 40)))]:
            pts = [(x0 + cw * j / n, y0 + ch * (1 - f(j / n))) for j in range(int(n * q) + 1)]
            if len(pts) > 1: d.line(pts, fill=col, width=4)
            d.text((x0 + cw, y0 + ch * (1 - f(1.0)) - 22), name, font=F(22, "Bold"), fill=col, anchor="rm")
        d.text((x0 + cw / 2, y0 + ch + 34), "illustration of the measured trend", font=F(20, "SemiBold"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2 - 120, 110), v["head"], F(50, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 60)

INSTR15 = [("Imaging cameras", 0), ("Infrared", 0), ("Photopolarimeter", 0), ("Plasma", 0), ("Planetary radio", 0), ("Ultraviolet", 0),
           ("Cosmic rays", 0), ("Low-energy particles", 0), ("Magnetometer", 1), ("Plasma waves", 1)]
def sc_powerdown(img, v, t, dur):
    """power meter (470 W at launch -> v.w_end, 'less than half') + a panel of 10 instrument lamps switching off one by one (2 stay on)"""
    p = easeio((t - 0.4) / max(1.0, dur * 0.7)); d = ImageDraw.Draw(img)
    mx, my0, my1 = 260, 900, 260
    d.rounded_rectangle([mx - 70, my1 - 20, mx + 70, my0 + 20], 30, fill=(16, 20, 40), outline=(60, 70, 110), width=3)
    w = lerp(470, v.get("w_end", 225), p); yy = lerp(my0, my1, w / 500)
    col = mix(DSN15, (255, 120, 80), p)
    d.rounded_rectangle([mx - 50, yy, mx + 50, my0], 20, fill=col)
    for ww in (0, 100, 200, 300, 400, 500):
        y = lerp(my0, my1, ww / 500); d.line([(mx + 74, y), (mx + 92, y)], fill=DIM, width=3); d.text((mx + 104, y), f"{ww} W", font=F(24, "SemiBold"), fill=DIM, anchor="lm")
    d.text((mx, 190), "POWER", font=F(40, "Black"), fill=WHITE, anchor="mm")
    d.text((mx, 975), f"{int(lerp(1977, 2026, p))}", font=F(54, "Black"), fill=WHITE, anchor="mm")
    d.text((mx, 1030), "less than half left" if p > 0.9 else "", font=F(28, "Bold"), fill=(255, 140, 100), anchor="mm")
    x0, y0 = 620, 230; cw, chh = 600, 140
    off_n = int(round(8 * min(1.0, p * 1.05)))
    for i, (name, stays) in enumerate(INSTR15):
        c, r = i % 2, i // 2; x = x0 + c * cw; y = y0 + r * chh
        on = stays or i >= off_n
        d.rounded_rectangle([x, y, x + cw - 40, y + chh - 30], 22, fill=(14, 18, 36) if not on else (16, 40, 34), outline=DSN15 if on else (60, 66, 90), width=3)
        lc = DSN15 if on else (60, 60, 70)
        if on: paste_c(img, radial(90, [(0, DSN15 + (200,)), (1, DSN15 + (0,))]), x + 54, y + (chh - 30) / 2); d = ImageDraw.Draw(img)
        d.ellipse([x + 38, y + (chh - 30) / 2 - 16, x + 70, y + (chh - 30) / 2 + 16], fill=lc)
        d.text((x + 96, y + (chh - 30) / 2), name, font=F(36, "Bold"), fill=WHITE if on else (110, 115, 135), anchor="lm")
        d.text((x + cw - 64, y + (chh - 30) / 2), "ON" if on else "OFF", font=F(30, "Black"), fill=DSN15 if on else (110, 115, 135), anchor="rm")
    if v.get("head"): alpha_text(img, (1210, 140), v["head"], F(48, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.0) / 0.5), y=H - 60)

def _dish15(d, x, y, s, col=(210, 215, 228)):
    d.chord([x - 150 * s, y - 120 * s, x + 150 * s, y + 60 * s], 200, 340, fill=col)
    d.polygon([(x - 20 * s, y + 20 * s), (x + 20 * s, y + 20 * s), (x + 40 * s, y + 170 * s), (x - 40 * s, y + 170 * s)], fill=(150, 155, 170))
    d.line([(x, y - 30 * s), (x, y - 120 * s)], fill=col, width=max(2, int(5 * s)))

def sc_whisper(img, v, t, dur):
    """22 W leaves Voyager, ~4×10^-19 W reaches a 70 m dish: the power written out with all its zeros, falling as 1/distance²"""
    d = ImageDraw.Draw(img); p = easeio((t - 0.3) / max(1.0, dur * 0.65))
    voyager15(img, 1640, 300, 1.0, ang=-0.2); d = ImageDraw.Draw(img)
    _dish15(d, 260, 680, 1.0); d.text((260, 880), "70 m dish, Deep Space Network", font=F(28, "Bold"), fill=WHITE, anchor="mm")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for j in range(7):
        q = ((t * 0.35 + j / 7) % 1.0); rr = 60 + q * 1500
        dl.arc([1640 - rr, 300 - rr, 1640 + rr, 300 + rr], 110, 190, fill=DSN15 + (int(200 * (1 - q) ** 1.5),), width=4)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.text((1640, 470), "leaves Voyager: 22 W", font=F(46, "Black"), fill=GOLD15, anchor="mm")
    d.text((1640, 525), "about a fridge light bulb", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    zeros = int(round(18 * p)); s = "0." + "0" * zeros + ("4" if zeros == 18 else "")
    d.text((1180, 760), s + " W", font=F(64 if zeros < 14 else 56, "Black"), fill=DSN15, anchor="mm")
    d.text((1180, 840), "arrives at the dish (our estimate)", font=F(32, "SemiBold"), fill=WHITE, anchor="mm")
    if p > 0.95: d.text((1180, 900), "less than a billionth of a billionth of a watt", font=F(34, "Bold"), fill=GOLD15, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 120), v["head"], F(50, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.4) / 0.5), y=H - 60)

def sc_pixeldot(img, v, t, dur):
    """our own re-drawing of the Pale Blue Dot idea: a camera frame with scattered-light bands; a pixel grid zooms in on one pixel and
    Earth fills only 0.12 of it (mode frame | zoom)"""
    mode = v.get("mode", "zoom"); d = ImageDraw.Draw(img)
    fx0, fy0, fs = 160, 170, 760
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rectangle([fx0, fy0, fx0 + fs, fy0 + fs], fill=(10, 8, 10, 255))
    for j, (off, wdt, a_) in enumerate([(0.18, 60, 70), (0.42, 110, 95), (0.68, 70, 60)]):
        x = fx0 + fs * off
        dl.polygon([(x, fy0), (x + wdt, fy0), (x + wdt + 160, fy0 + fs), (x + 160, fy0 + fs)], fill=(200, 140, 90, a_))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(14))); d = ImageDraw.Draw(img)
    d.rectangle([fx0, fy0, fx0 + fs, fy0 + fs], outline=(120, 120, 140), width=3)
    ex, ey = fx0 + fs * 0.5 + 92, fy0 + fs * 0.62
    d.ellipse([ex - 2, ey - 2, ex + 2, ey + 2], fill=(170, 200, 255))
    q = 0.5 + 0.5 * math.sin(t * 3); d.ellipse([ex - 30, ey - 30, ex + 30, ey + 30], outline=mix(GOLD15, WHITE, q), width=3)
    d.text((fx0 + fs / 2, fy0 + fs + 40), "our re-drawing: 14 February 1990, 6 billion km", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    if mode == "zoom":
        z = ease((t - 0.8) / 1.2); gx, gy, gs = 1100, 210, 680
        d.line([(ex + 30, ey - 30), (lerp(ex, gx, z), lerp(ey, gy, z))], fill=GOLD15, width=2)
        d.line([(ex + 30, ey + 30), (lerp(ex, gx, z), lerp(ey, gy + gs, z))], fill=GOLD15, width=2)
        if z > 0.05:
            n = 5; c = gs / n
            for i in range(n):
                for j in range(n):
                    shade = 18 + ((i * 7 + j * 3) % 5) * 4
                    d.rectangle([gx + i * c, gy + j * c, gx + (i + 1) * c - 3, gy + (j + 1) * c - 3], fill=(shade, shade - 4, shade - 6))
            ci = gx + 2 * c; cj = gy + 2 * c
            d.rectangle([ci, cj, ci + c - 3, cj + c - 3], outline=GOLD15, width=4)
            er = math.sqrt(0.12 / math.pi) * c  # a disc whose area is 12% of the pixel
            d.ellipse([ci + c / 2 - er, cj + c / 2 - er, ci + c / 2 + er, cj + c / 2 + er], fill=(120, 170, 255))
            d.text((gx + gs / 2, gy + gs + 50), "EARTH = 0.12 of ONE pixel", font=F(46, "Black"), fill=WHITE, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 100), v["head"], F(46, "ExtraBold"), WHITE, ease(t / 0.5))
    caption(img, v.get("caption"), ease((t - 2.4) / 0.5), y=H - 50)


# ---------------- scenes (EP16: why can't we see the edge of the universe?) ----------------
sys.path.insert(0, HERE); import cosmo16 as CM16
RED16, AMB16, TEAL16, PALE16 = (255, 84, 84), (255, 178, 70), (70, 210, 200), (255, 228, 214)
def _zx16(z, x0, x1): return lerp(x0, x1, math.log10(1 + z) / math.log10(1 + 1100))
def _fmt_ly16(gly):
    if gly >= 1: return f"{gly:,.1f} billion ly"
    if gly >= 0.001: return f"{gly * 1000:,.0f} million ly"
    return f"{gly * 1e6:,.1f} thousand ly" if gly >= 1e-6 else "here"

def sc_zdial(img, v, t, dur):
    """chapter card: a half-circle redshift dial on a log(1+z) scale (0 -> 1,100), needle swings to v.z; live readouts of lookback time,
    distance when the light left and distance now (flat ΛCDM, cosmo16); kicker / title / sub at right; wall number n = bricks lit"""
    cx, cy, Rr = 560, 760, 400; p = easeio((t - 0.2) / 1.8); z = v.get("z", 0.0)
    zz = (1 + z) ** p - 1  # swing on log(1+z)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for k in range(120):
        u0, u1 = k / 120, (k + 1) / 120
        col = mix(mix((150, 120, 255), RED16, min(1, u0 * 1.6)), AMB16, max(0, (u0 - 0.6) / 0.4))
        dl.arc([cx - Rr, cy - Rr, cx + Rr, cy + Rr], 180 + 180 * u0, 180 + 180 * u1 + 0.4, fill=col + (110 if u0 > math.log10(1 + zz) / math.log10(1101) else 255,), width=30)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    for zt, lab in [(0, "0"), (0.5, "0.5"), (1, "1"), (3, "3"), (10, "10"), (100, "100"), (1100, "1,100")]:
        u = math.log10(1 + zt) / math.log10(1101); a = math.pi + math.pi * u
        d.line([(cx + (Rr + 22) * math.cos(a), cy + (Rr + 22) * math.sin(a)), (cx + (Rr + 44) * math.cos(a), cy + (Rr + 44) * math.sin(a))], fill=(200, 190, 200), width=4)
        d.text((cx + (Rr + 82) * math.cos(a), cy + (Rr + 82) * math.sin(a)), lab, font=F(30, "Bold"), fill=DIM, anchor="mm")
    u = math.log10(1 + zz) / math.log10(1101); a = math.pi + math.pi * u
    d.line([(cx, cy), (cx + (Rr - 40) * math.cos(a), cy + (Rr - 40) * math.sin(a))], fill=WHITE, width=8)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=WHITE)
    d.text((cx, cy - 250), "REDSHIFT", font=F(30, "Bold"), fill=DIM, anchor="mm")
    d.text((cx, cy - 175), (f"{zz:,.0f}" if zz >= 100 else f"{zz:.2f}"), font=F(104, "Black"), fill=WHITE, anchor="mm")
    lb = CM16.lookback(zz) if zz > 1e-4 else 0.0
    rows = [("light left", (f"{lb:.2f} billion years ago" if lb >= 0.01 else "just now")),
            ("it was", _fmt_ly16(CM16.d_then(zz)) if zz > 1e-4 else "—"), ("it is now", _fmt_ly16(CM16.chi(zz)) if zz > 1e-4 else "—")]
    for i, (k, val) in enumerate(rows):
        d.text((cx - 360, cy + 70 + i * 52), k, font=F(30, "SemiBold"), fill=DIM, anchor="lm")
        d.text((cx + 360, cy + 70 + i * 52), val, font=F(32, "ExtraBold"), fill=PALE16, anchor="rm")
    n = v.get("n", 0)
    for k in range(5):
        x = 1060 + k * 150; on = k < n
        col = (RED16 if k == n - 1 else (120, 60, 60)) if on else (40, 36, 46)
        d.rounded_rectangle([x, 250, x + 128, 300], 8, fill=col)
        d.text((x + 64, 275), str(k + 1), font=F(28, "Black"), fill=WHITE if on else DIM, anchor="mm")
    a1, a2 = ease((t - 0.3) / 0.5), ease((t - 0.8) / 0.5)
    alpha_text(img, (1060, 400), v.get("kicker", ""), F(38, "Bold"), AMB16, a1, anchor="lm")
    lines = v.get("title", "").split("\n")
    for i, l in enumerate(lines): alpha_text(img, (1060, 500 + i * 100), l, F(92, "Black"), WHITE, a1, anchor="lm", dy=(1 - a1) * 30)
    alpha_text(img, (1060, 500 + len(lines) * 100), v.get("sub", ""), F(42, "SemiBold"), RED16, a2, anchor="lm")
    d = ImageDraw.Draw(img); d.text((W - 60, H - 60), "our calculation: flat ΛCDM, Planck 2018 values", font=F(24, "Medium"), fill=(110, 110, 130), anchor="rm")

_lc16 = None
def _lc_table16():
    global _lc16
    if _lc16 is None:
        zs = np.concatenate([np.linspace(0, 3, 300), np.logspace(math.log10(3.01), math.log10(1100), 300)])
        _lc16 = (zs, np.array([CM16.age(z) for z in zs]), np.array([CM16.d_then(z) for z in zs]))
    return _lc16

def sc_lightcone(img, v, t, dur):
    """the teardrop: x = distance of the source when its light left (Gly, both sides), y = cosmic time (Big Bang at the bottom, now at the
    top); a photon dot rides down the curve to v.z with a dashed path; v.max marks the widest point 5.8 Gly; v.event adds the event horizon"""
    zs, ages, dth = _lc_table16(); x0c, yb, yt = 820, 960, 200; sx = 122   # px per Gly
    def P(dist, age, side=1): return (x0c + side * dist * sx, lerp(yb, yt, age / CM16.AGE))
    d = ImageDraw.Draw(img)
    d.line([(x0c, yb), (x0c, yt - 20)], fill=(70, 70, 90), width=3)
    for gy in (0, 2, 4, 6):
        for sd in (-1, 1):
            if gy == 0 and sd == -1: continue
            xg = x0c + sd * gy * sx; d.line([(xg, yb), (xg, yb + 14)], fill=DIM, width=3); d.text((xg, yb + 38), f"{gy}", font=F(26, "Bold"), fill=DIM, anchor="mm")
    d.text((x0c, yb + 78), "distance when the light left (billion light-years)", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    for ag, lab in [(0, "Big Bang"), (5, "5 billion yrs"), (10, "10 billion yrs"), (CM16.AGE, "today")]:
        y = lerp(yb, yt, ag / CM16.AGE); d.text((x0c + 14, y - 18), lab, font=F(24, "Bold"), fill=DIM, anchor="lm"); d.line([(x0c - 10, y), (x0c + 10, y)], fill=DIM, width=2)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for side in (-1, 1):
        pts = [P(dd, aa, side) for dd, aa in zip(dth, ages)]
        dl.line(pts, fill=RED16 + (70,), width=16); dl.line(pts, fill=RED16 + (255,), width=5)
    if v.get("event"):
        q = ease((t - 0.5) / 1.0)
        dl.rounded_rectangle([40, 160, 525, 400], 22, fill=(6, 22, 24, int(235 * q)), outline=TEAL16 + (int(200 * q),), width=3)
        dl.text((282, 200), "EVENT HORIZON, TODAY", font=F(30, "Bold"), fill=TEAL16 + (int(255 * q),), anchor="mm")
        dl.text((282, 268), "16.6 billion ly", font=F(56, "Black"), fill=(255, 255, 255, int(255 * q)), anchor="mm")
        dl.text((282, 340), "light sent now from beyond it", font=F(26, "SemiBold"), fill=(200, 210, 215, int(255 * q)), anchor="mm")
        dl.text((282, 372), "will never reach us", font=F(26, "SemiBold"), fill=(200, 210, 215, int(255 * q)), anchor="mm")
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    paste_c(img, earth_sprite(14, glow=None), x0c, yt)
    z = v.get("z", 1.0); p = easeio((t - 0.4) / max(1.0, dur * 0.6))
    zt = (1 + z) ** p - 1; dd = CM16.d_then(zt); aa = CM16.age(zt)
    # photon path: from the source point back up to Earth along the curve
    sel = zs <= zt
    pts = [P(a_, b_) for a_, b_ in zip(dth[sel], ages[sel])] + [P(dd, aa)]
    if len(pts) > 1: d.line(pts, fill=AMB16, width=7)
    sx_, sy_ = P(dd, aa)
    paste_c(img, radial(80, [(0, (255, 255, 255, 255)), (0.35, AMB16 + (220,)), (1, AMB16 + (0,))]), sx_, sy_)
    d = ImageDraw.Draw(img)
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1535, 330, 1905, 700], 24, fill=(18, 8, 10, 230), outline=RED16 + (120,), width=2); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((1725, 380), f"redshift {zt:.2f}", font=F(36, "Bold"), fill=AMB16, anchor="mm")
    d.text((1725, 460), _fmt_ly16(dd).replace(" ly", ""), font=F(52, "Black"), fill=WHITE, anchor="mm")
    d.text((1725, 515), "light-years away, back then", font=F(25, "SemiBold"), fill=DIM, anchor="mm")
    d.text((1725, 590), f"{CM16.chi(zt):.1f} billion", font=F(44, "Black"), fill=PALE16, anchor="mm")
    d.text((1725, 640), "light-years away today", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    if v.get("max"):
        q = 0.5 + 0.5 * math.sin(t * 4); mx, my = P(5.846, CM16.age(1.59))
        d.ellipse([mx - 30, my - 30, mx + 30, my + 30], outline=mix(AMB16, WHITE, q), width=5)
        d.text((mx + 40, my + 60), "widest: 5.8 billion ly", font=F(34, "Black"), fill=AMB16, anchor="lm")
    if v.get("head"): alpha_text(img, (W / 2, 90), v["head"], F(48, "ExtraBold"), WHITE, ease(t / 0.5))

def _galaxy_small16(r, a=1.0, col=(255, 225, 190)):
    g = galaxy_sprite(); s = max(4, int(2 * r)); return g.resize((s, s), Image.LANCZOS)

def sc_angsize(img, v, t, dur):
    """one galaxy (same real size, 100,000 ly) moved from v.z0 to v.z1: left = telescope eyepiece showing its apparent size (arcsec, angular
    diameter distance), right = the size curve vs log(1+z) with a dot and the minimum near z≈1.6 marked; v.dim adds the (1+z)^4 fade"""
    p = easeio((t - 0.4) / max(1.0, dur * 0.7)); z0, z1 = v.get("z0", 0.1), v.get("z1", 14.44)
    z = (1 + z0) * ((1 + z1) / (1 + z0)) ** p - 1
    ang = 1e-4 / CM16.d_then(z) * 206265  # arcsec
    ex, ey, ER = 500, 580, 330
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([ex - ER - 18, ey - ER - 18, ex + ER + 18, ey + ER + 18], fill=(60, 56, 66, 255))
    dl.ellipse([ex - ER, ey - ER, ex + ER, ey + ER], fill=(3, 3, 8, 255))
    img.alpha_composite(lay)
    rng = random.Random(16); d = ImageDraw.Draw(img)
    for _ in range(70):
        a_, r_ = rng.uniform(0, 2 * math.pi), ER * math.sqrt(rng.random()) * 0.95
        x, y = ex + r_ * math.cos(a_), ey + r_ * math.sin(a_); d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(150, 150, 175))
    rpx = min(ER * 0.98, ang * 21.0)  # 21 px per arcsec
    fade = 1.0
    if v.get("dim"): fade = max(0.18, 1 / ((1 + z) / (1 + z0)) ** 1.1)
    gs = _galaxy_small16(rpx)
    redcol = mix((255, 255, 255), (255, 90, 60), min(1, math.log10(1 + z) / 1.2))
    arr = np.asarray(gs).astype(np.float32); arr[..., 0] *= redcol[0] / 255; arr[..., 1] *= redcol[1] / 255; arr[..., 2] *= redcol[2] / 255; arr[..., 3] = np.minimum(255, arr[..., 3] * 1.6) * fade
    paste_c(img, Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA"), ex, ey)
    d = ImageDraw.Draw(img)
    d.text((ex, ey + ER + 60), f"looks {ang:.1f} arcseconds wide", font=F(40, "Black"), fill=WHITE, anchor="mm")
    d.text((ex, ey + ER + 108), "same galaxy, 100,000 light-years across", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    # curve
    gx0, gx1, gy0, gy1 = 1000, 1820, 840, 330
    zz = np.logspace(-1.3, math.log10(20), 160); aa = np.array([1e-4 / CM16.d_then(q) * 206265 for q in zz])
    def G(zv, av): return (lerp(gx0, gx1, (math.log10(1 + zv) - math.log10(1 + zz[0])) / (math.log10(21) - math.log10(1 + zz[0]))), lerp(gy0, gy1, (min(av, 20) - 0) / 20))
    d.line([(gx0, gy0), (gx1, gy0)], fill=(90, 90, 110), width=3); d.line([(gx0, gy0), (gx0, gy1)], fill=(90, 90, 110), width=3)
    d.line([G(a_, b_) for a_, b_ in zip(zz, aa)], fill=RED16, width=6)
    for zt in (0.1, 0.5, 1, 1.6, 3, 10):
        x, _ = G(zt, 0); d.text((x, gy0 + 34), f"{zt:g}", font=F(26, "Bold"), fill=DIM, anchor="mm")
    d.text(((gx0 + gx1) / 2, gy0 + 80), "redshift (farther →)", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    d.text((gx0 - 16, gy1 - 30), "apparent size", font=F(28, "SemiBold"), fill=DIM, anchor="lm")
    mx, my = G(1.6, 1e-4 / CM16.d_then(1.6) * 206265)
    d.line([(mx, my + 20), (mx, gy0)], fill=AMB16, width=2); d.text((mx, my + 50), "smallest ≈ 1.6", font=F(26, "Bold"), fill=AMB16, anchor="mm")
    px_, py_ = G(z, ang); paste_c(img, radial(60, [(0, (255, 255, 255, 255)), (0.4, AMB16 + (220,)), (1, AMB16 + (0,))]), px_, py_)
    d = ImageDraw.Draw(img)
    d.text((1410, 250), f"redshift {z:.2f}", font=F(44, "Black"), fill=AMB16, anchor="mm")
    if v.get("dim"):
        k = (1 + z) ** 4
        d.text((1410, 960), f"surface brightness ÷ {k:,.0f}", font=F(46, "Black"), fill=RED16, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 90), v["head"], F(50, "ExtraBold"), WHITE, ease(t / 0.5))

def _sn16(tt):  # normalised Type Ia-like light curve vs rest-frame days (rise ~18 d, decline)
    if tt < 0: return 0.0
    if tt < 18: return (tt / 18) ** 2 * (3 - 2 * tt / 18)
    return math.exp(-(tt - 18) / 22) * 0.92 + 0.08 * math.exp(-(tt - 18) / 80)

def sc_slowmo(img, v, t, dur):
    """two supernova light curves on the same day axis: nearby (rest frame) and at redshift v.z (stretched ×(1+z)); a cursor sweeps the
    days, each star flashes with its current brightness and a day counter"""
    s = 1 + v.get("z", 1.0); p = easeio((t - 0.3) / max(1.0, dur * 0.8)); day = lerp(0, 120, p)
    rows = [("NEARBY", 1.0, TEAL16, 420), (f"REDSHIFT {v.get('z', 1.0):g}", s, RED16, 790)]
    x0, x1 = 560, 1820; d = ImageDraw.Draw(img)
    for name, k, col, yb in rows:
        h = 230
        d.line([(x0, yb), (x1, yb)], fill=(90, 90, 110), width=3)
        for dd in range(0, 121, 20):
            x = lerp(x0, x1, dd / 120); d.line([(x, yb), (x, yb + 10)], fill=DIM, width=2); d.text((x, yb + 32), f"{dd}", font=F(24, "Bold"), fill=DIM, anchor="mm")
        full = [(lerp(x0, x1, dd / 120), yb - h * _sn16(dd / k)) for dd in np.linspace(0, 120, 240)]
        d.line(full, fill=mix(col, (20, 20, 30), 0.7), width=4)
        now = [(lerp(x0, x1, dd / 120), yb - h * _sn16(dd / k)) for dd in np.linspace(0, day, max(2, int(240 * p)))]
        d.line(now, fill=col, width=7)
        b = _sn16(day / k)
        paste_c(img, radial(int(90 + 260 * b) // 2 * 2 + 2, [(0, (255, 255, 255, int(255 * min(1, 0.2 + b)))), (0.3, col + (int(200 * b),)), (1, col + (0,))]), 300, yb - 110)
        d = ImageDraw.Draw(img)
        d.text((300, yb - 240), name, font=F(34, "Black"), fill=col, anchor="mm")
        d.text((300, yb + 40), f"peak at day {18 * k:.0f}", font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    d.text((W / 2, 900), f"day {day:.0f} on our clock", font=F(48, "Black"), fill=WHITE, anchor="mm")
    d.text((W / 2, 955), "illustrative light curve; the stretch factor 1 + z is the measured one (Dark Energy Survey, 2024)", font=F(26, "Medium"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 110), v["head"], F(50, "ExtraBold"), WHITE, ease(t / 0.5))

_fog16 = None
def _fog_parts16():
    global _fog16
    if _fog16 is None:
        rng = np.random.default_rng(160)
        _fog16 = {"e": rng.uniform([120, 160], [1800, 940], (260, 2)), "p": rng.uniform([120, 160], [1800, 940], (130, 2)),
                  "ph": [(rng.uniform(200, 1700), rng.uniform(250, 850), rng.uniform(0, 2 * math.pi)) for _ in range(14)], "seed": 7}
    return _fog16

def sc_fogwall(img, v, t, dur):
    """plasma era: mode fog = free electrons (small blue) + protons (red) jitter, photons (amber) zig-zag with short random hops, orange
    haze + temperature 3,000+ K; mode clear = electrons pair with protons into atoms, haze fades, photons fly straight off-screen"""
    P_ = _fog_parts16(); mode = v.get("mode", "fog")
    q = 0.0 if mode == "fog" else easeio((t - 0.6) / max(1.0, dur * 0.45))
    haze = Image.new("RGBA", img.size, (255, 120, 40, int(95 * (1 - q)))); img.alpha_composite(haze)
    d = ImageDraw.Draw(img)
    for i, (x, y) in enumerate(P_["p"]):
        jx, jy = math.sin(t * 3 + i) * 3, math.cos(t * 2.6 + i * 1.7) * 3
        d.ellipse([x + jx - 7, y + jy - 7, x + jx + 7, y + jy + 7], fill=(255, 100, 90))
        e = P_["e"][i]
        ex_, ey_ = lerp(e[0], x + 16 * math.cos(t * 5 + i), q), lerp(e[1], y + 16 * math.sin(t * 5 + i), q)
        if q > 0.6: d.ellipse([x + jx - 16, y + jy - 16, x + jx + 16, y + jy + 16], outline=(140, 170, 255), width=2)
        d.ellipse([ex_ - 4, ey_ - 4, ex_ + 4, ey_ + 4], fill=(120, 170, 255))
    for i, (x, y) in enumerate(P_["e"][130:]):
        jx = math.sin(t * 4 + i) * 6; a_ = 1 - q
        if a_ > 0.05: d.ellipse([x + jx - 4, y - 4, x + jx + 4, y + 4], fill=mix(SPACE, (120, 170, 255), a_))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for k, (px, py, th) in enumerate(P_["ph"]):
        rng = random.Random(k * 31 + int(t * 3)); pts = [(px, py)]
        if mode == "fog":
            x, y = px, py
            for j in range(9):
                r2 = random.Random(k * 97 + j + int(t * 2.5)); a_ = r2.uniform(0, 2 * math.pi); L = r2.uniform(30, 80)
                x, y = x + L * math.cos(a_), y + L * math.sin(a_); pts.append((x, y))
        else:
            L = 120 + t * 420; pts.append((px + L * math.cos(th), py + L * math.sin(th)))
        dl.line(pts, fill=AMB16 + (220,), width=4); dl.ellipse([pts[-1][0] - 7, pts[-1][1] - 7, pts[-1][0] + 7, pts[-1][1] + 7], fill=(255, 240, 200, 255))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    T = 3000 * 1.3 if mode == "fog" else lerp(3000, 2900, q)
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1460, 820, 1880, 1010], 22, fill=(16, 8, 6, 230)); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    d.text((1670, 880), (f"{T:,.0f} K+" if mode == "fog" else "≈ 3,000 K"), font=F(64, "Black"), fill=AMB16, anchor="mm")
    d.text((1670, 950), ("light trapped: fog" if mode == "fog" else "atoms form: light flies free"), font=F(30, "Bold"), fill=WHITE, anchor="mm")
    lg = [((255, 100, 90), "proton"), ((120, 170, 255), "electron"), (AMB16, "light")]
    for i, (c, n) in enumerate(lg):
        d.ellipse([80, 870 + i * 44, 98, 888 + i * 44], fill=c); d.text((112, 879 + i * 44), n, font=F(28, "Bold"), fill=WHITE, anchor="lm")
    if v.get("head"): alpha_text(img, (W / 2, 80), v["head"], F(52, "ExtraBold"), WHITE, ease(t / 0.5))


# ---------------- scenes (EP17: star swap) ----------------
def bbcol17(T):
    """approximate visible colour of a blackbody at T kelvin (Tanner Helland fit), as an RGB tuple"""
    t = T / 100.0
    r = 255 if t <= 66 else 329.7 * (t - 60) ** -0.1332
    g = (99.47 * math.log(t) - 161.12) if t <= 66 else 288.12 * (t - 60) ** -0.0755
    b = 255 if t >= 66 else (0 if t <= 19 else 138.52 * math.log(t - 10) - 305.04)
    return tuple(int(max(0, min(255, c))) for c in (r, g, b))

_st17 = {}
def star17(r, T, halo=1.6):
    r = max(2, int(r)); key = (r, int(T // 50), halo)
    if key not in _st17:
        c = bbcol17(T); hot = mix(c, (255, 255, 255), 0.65); k = 1 / 3
        _st17[key] = radial(r * 6, [(0, hot + (255,)), (k * 0.75, mix(c, (255, 255, 255), 0.3) + (255,)), (k * 0.98, c + (255,)),
                                   (k * 1.04, c + (150,)), (k * halo, c + (40,)), (1.0, c + (0,))])
    return _st17[key]

def _logp(a, b, p): return math.exp(lerp(math.log(a), math.log(b), p))
SUNREF17 = {"L": 1.0, "R": 1.0, "T": 5772}
def _swapvals17(v, t):
    p = easeio((t - 0.4) / 2.0) if v.get("from_sun", False) else 1.0
    return p, _logp(1.0, v["L"], p), _logp(1.0, v["R"], p), lerp(5772, v["T"], p)

def _hills17(seed=17):
    rng = random.Random(seed); pts = []
    for k in range(0, 1121, 40):
        x = k * 1.0
        pts.append((x, 880 - 70 * math.sin(x / 260 + 1.3) - 40 * math.sin(x / 97) - rng.uniform(0, 14)))
    return pts

def sc_swapsky(img, v, t, dur):
    """ground view at noon: the star that replaced the Sun hangs in the sky at its TRUE angular size from 1 AU (Sun = 0.533° = 70 px);
    sky brightness/tint and the lit landscape follow its light (L) and colour (T); v.from_sun animates Sun -> star; v.ghost = dashed outline
    of the Sun's disc; HUD: sunlight vs today, disc width vs the Sun; mode inside = Earth is inside the star (glowing fog, no sky)"""
    p, L, R, T = _swapvals17(v, t)
    col = bbcol17(T)
    if v.get("mode") == "inside":
        a = ease((t - 0.2) / 1.5)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for y in range(0, H, 6):
            u = y / H; c = mix((255, 150, 70), (190, 40, 20), u)
            fl = 0.85 + 0.15 * math.sin(y / 37 + t * 2.1) * math.sin(y / 13 - t * 1.3)
            dl.rectangle([0, y, W, y + 6], fill=tuple(int(cc * fl) for cc in c) + (int(250 * a),))
        img.alpha_composite(lay)
        rng = random.Random(5); blobs = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(blobs)
        for _ in range(140):  # drifting glowing gas cells
            x = (rng.uniform(0, W) + t * rng.uniform(20, 60)) % W; y = rng.uniform(0, H); r = rng.uniform(20, 90)
            d.ellipse([x - r, y - r * 0.6, x + r, y + r * 0.6], fill=(255, 220, 160, int(18 * a)))
        img.alpha_composite(blobs.filter(ImageFilter.GaussianBlur(8)))
        alpha_text(img, (W / 2, H / 2 - 40), v.get("big", "YOU ARE INSIDE THE STAR"), F(96, "Black"), WHITE, ease((t - 0.8) / 0.6))
        alpha_text(img, (W / 2, H / 2 + 60), v.get("sub", ""), F(44, "SemiBold"), (255, 235, 200), ease((t - 1.3) / 0.6))
        return
    day = max(0.0, min(1.0, (math.log10(L) + 3.2) / 3.2))  # 0 = night (L <= 0.0006), 1 = full daylight at L = 1
    wash = max(0.0, min(1.0, math.log10(max(L, 1)) / 1.6))  # glare for brighter stars
    tint = mix((70, 130, 225), col, 0.35)
    top = mix((4, 6, 16), mix(tint, (235, 240, 255), wash * 0.8), day)
    bot = mix((10, 10, 24), mix(mix(tint, (255, 255, 255), 0.45), (255, 252, 245), wash), day)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for y in range(0, 900, 6):
        dl.rectangle([0, y, W, y + 6], fill=mix(top, bot, y / 900) + (int(255 * min(1, day * 1.4)),))
    img.alpha_composite(lay)
    sx, sy = v.get("x", 1180), v.get("y", 330)
    rpx = 35 * R  # Sun disc 0.533 deg -> 70 px across
    glow = 1.5 + 2.2 * min(1, L ** 0.25)
    if rpx >= 2.5:
        paste_c(img, star17(rpx, T, halo=glow), sx, sy)
        if wash > 0.2:  # glare sky: keep the disc readable with a hard white core + ring of rays
            d = ImageDraw.Draw(img)
            for k in range(12):
                a = k * math.pi / 6 + t * 0.15; r0, r1 = rpx * 1.25, rpx * (2.2 + 0.3 * math.sin(t * 2 + k))
                d.line([(sx + r0 * math.cos(a), sy + r0 * math.sin(a)), (sx + r1 * math.cos(a), sy + r1 * math.sin(a))], fill=(255, 255, 255), width=3)
            d.ellipse([sx - rpx, sy - rpx, sx + rpx, sy + rpx], fill=(255, 255, 255), outline=mix(col, (120, 160, 255), 0.5), width=4)
    else:
        gl = int(10 + 30 * L ** 0.25); paste_c(img, star17(gl, T, halo=3.0), sx, sy, 0.45)
        d = ImageDraw.Draw(img)
        for k in range(4):
            a = k * math.pi / 4; ln = 60 + 20 * math.sin(t * 3)
            d.line([(sx - ln * math.cos(a), sy - ln * math.sin(a)), (sx + ln * math.cos(a), sy + ln * math.sin(a))], fill=mix(col, (255, 255, 255), 0.6), width=2)
        d.ellipse([sx - 4, sy - 4, sx + 4, sy + 4], fill=(255, 255, 255))
    d = ImageDraw.Draw(img)
    if v.get("ghost", True) and p > 0.5:
        for k in range(0, 360, 12): d.arc([sx - 35, sy - 35, sx + 35, sy + 35], k, k + 6, fill=(255, 255, 255), width=3)
        d.text((sx + 48, sy - 50), "our Sun's size", font=F(26, "SemiBold"), fill=(255, 255, 255) if day < 0.6 else (40, 40, 60), anchor="lm")
    # landscape: sea + hills, lit by the star
    lit = mix((8, 10, 18), mix(col, (255, 255, 255), 0.25), day * 0.9)
    sea = mix((6, 10, 22), mix((40, 90, 150), col, 0.25), day)
    d.rectangle([0, 880, W, H], fill=sea)
    for k in range(10):
        yy = 900 + k * 18; d.line([(sx - 300 + k * 10, yy), (sx + 300 - k * 10, yy)], fill=mix(sea, col, 0.5 * day + 0.1), width=2)
    hill = _hills17(); poly = [(0, H)] + hill + [(1120, H)]
    d.polygon(poly, fill=mix((5, 6, 12), mix(lit, (40, 70, 40), 0.55), day))
    # HUD
    a = ease((t - 0.3) / 0.6)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([1250, 640, 1840, 990], 24, fill=(6, 8, 20, int(200 * a)), outline=col + (int(200 * a),), width=3)
    img.alpha_composite(lay)
    sl = f"{L * 100:.2f}% of today" if L < 0.01 else (f"{L * 100:.1f}% of today" if L < 0.1 else (f"{L * 100:.0f}% of today" if L < 1.995 else f"{L:,.0f}× today"))
    rows = [("STAR", v.get("name", "")), ("SUNLIGHT", sl), ("DISC WIDTH", (f"{R:.2f}× the Sun" if R >= 0.1 else f"1/{1 / R:,.0f} of the Sun")), ("COLOUR", f"{T:,.0f} K")]
    for i, (k, val) in enumerate(rows):
        alpha_text(img, (1285, 700 + i * 76), k, F(28, "Bold"), DIM, a, anchor="lm", shadow=False)
        alpha_text(img, (1810, 700 + i * 76), val, F(38, "ExtraBold"), WHITE if i else mix(col, (255, 255, 255), 0.4), a, anchor="rm", shadow=False)
    if v.get("head"): alpha_text(img, (W / 2, 150), v["head"], F(60, "Black"), WHITE, ease((t - 0.2) / 0.5))
    if v.get("caption"): caption(img, v["caption"], ease((t - 0.8) / 0.5), y=H - 70)

def sc_starcard(img, v, t, dur):
    """chapter card 'SWAP n OF 5': the star drawn at left (size ∝ R^0.25 so it fits), Sun ghost for scale, and stat rows with log bars
    centred on the Sun (1×): width, brightness, surface temperature, distance from us"""
    col = bbcol17(v["T"]); a1, a2 = ease((t - 0.2) / 0.6), ease((t - 0.7) / 0.6)
    r = max(6, min(300, 120 * v["R"] ** 0.25)) * (0.6 + 0.4 * ease(t / 1.2))
    paste_c(img, star17(r, v["T"], halo=1.9), 470, 560, a1)
    paste_c(img, sun_sprite(28), 470 + max(r, 40) + 120, 560 + max(r * 0.6, 60), a1)
    d = ImageDraw.Draw(img); d.text((470 + max(r, 40) + 120, 560 + max(r * 0.6, 60) + 58), "our Sun", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    if v["R"] > 50: d.text((470, 960), "(not to scale: way bigger)", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    alpha_text(img, (1000, 230), v.get("kicker", ""), F(38, "Bold"), mix(col, (255, 255, 255), 0.3), a1, anchor="lm")
    alpha_text(img, (1000, 320), v.get("name", ""), F(84, "Black"), WHITE, a1, anchor="lm", dy=(1 - a1) * 30)
    alpha_text(img, (1000, 400), v.get("sub", ""), F(38, "SemiBold"), DIM, a2, anchor="lm")
    rows = [("WIDTH", v["R"], f"{v['R']:.4f}×" if v["R"] < 0.1 else f"{v['R']:,.2f}×" if v["R"] < 100 else f"{v['R']:,.0f}×"),
            ("BRIGHTNESS", v["L"], (f"{v['L']:.4f}×" if v["L"] < 0.01 else (f"{v['L']:.2f}×" if v["L"] < 10 else f"{v['L']:,.0f}×"))),
            ("SURFACE", v["T"] / 5772, f"{v['T']:,.0f} K")]
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    x0, x1 = 1000, 1780; xm = (x0 + x1) / 2
    for i, (k, ratio, txt) in enumerate(rows):
        y = 520 + i * 125; ai = ease((t - 0.9 - i * 0.25) / 0.5)
        dl.rectangle([x0, y + 30, x1, y + 52], fill=(40, 44, 60, int(255 * a2)))
        dl.line([(xm, y + 20), (xm, y + 62)], fill=(255, 255, 255, int(200 * a2)), width=3)
        u = max(-1, min(1, math.log10(ratio) / 6)) * ai; xe = xm + u * (x1 - xm)
        dl.rectangle([min(xm, xe), y + 30, max(xm, xe), y + 52], fill=col + (int(255 * a2),))
    img.alpha_composite(lay)
    for i, (k, ratio, txt) in enumerate(rows):
        y = 520 + i * 125; ai = ease((t - 0.9 - i * 0.25) / 0.5)
        alpha_text(img, (x0, y), k, F(28, "Bold"), DIM, a2, anchor="lm", shadow=False)
        alpha_text(img, (x1, y), txt + ("" if k == "SURFACE" else " the Sun"), F(36, "ExtraBold"), WHITE, ai, anchor="rm", shadow=False)
    d = ImageDraw.Draw(img)
    d.text((xm, 905), "Sun = centre line · log scale", font=F(24, "Medium"), fill=(110, 115, 140), anchor="mm")
    alpha_text(img, (x0, 980), v.get("dist", ""), F(32, "SemiBold"), mix(col, (255, 255, 255), 0.5), a2, anchor="lm")

PLAN17 = [("Mercury", 0.387), ("Venus", 0.723), ("Earth", 1.0), ("Mars", 1.524), ("Jupiter", 5.20), ("Saturn", 9.54), ("Uranus", 19.2), ("Neptune", 30.1), ("Pluto", 39.5)]
def sc_hzmap(img, v, t, dur):
    """top-down solar system on a SQUARE-ROOT distance scale (to v.max AU); green 'Earth-like zone' (0.99–1.70 AU × √L, Kopparapu et al.
    2013 conservative limits) slides from the Sun's to the new star's; star disc to the same scale (R × 0.00465 AU) swallows inner orbits;
    Earth tagged TOO HOT / TOO COLD / JUST RIGHT; v.hl = planet name that now sits in the zone"""
    p = easeio((t - 0.6) / 2.2); L = _logp(1.0, v["L"], p); Rs = _logp(1.0, v["R"], p); T = lerp(5772, v["T"], p)
    cx, cy, Rmax = 640, 560, 470; mx = v.get("max", 40)
    def rp(au): return Rmax * math.sqrt(min(au, mx * 1.2) / mx)
    col = bbcol17(T)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    zi, zo = 0.99 * math.sqrt(L), 1.70 * math.sqrt(L)
    if zi < mx * 1.2:
        dl.ellipse([cx - rp(zo), cy - rp(zo), cx + rp(zo), cy + rp(zo)], fill=(60, 200, 110, 90))
        dl.ellipse([cx - rp(zi), cy - rp(zi), cx + rp(zi), cy + rp(zi)], fill=(0, 0, 0, 0))
    img.alpha_composite(lay)
    lay2 = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay2)
    sr = rp(Rs * 0.00465)
    for i, (nm, au) in enumerate(PLAN17):
        if au > mx: continue
        r = rp(au); gone = sr > r
        dl.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(120, 130, 160, 90 if gone else 200), width=2)
        ang = -0.9 + i * 0.75; px, py = cx + r * math.cos(ang), cy + r * math.sin(ang)
        pc = (90, 160, 255) if nm == "Earth" else ((120, 255, 150) if nm == v.get("hl") and p > 0.9 else (210, 210, 220))
        if mx > 200 and nm != "Pluto":
            continue
        if not gone:
            dl.ellipse([px - 9, py - 9, px + 9, py + 9], fill=pc + (255,))
            dl.text((px + 14, py), nm, font=F(26, "Bold"), fill=pc + (255,), anchor="lm")
        else:
            if mx > 200: continue
            dl.text((px + 14, py), nm + " ✕", font=F(24, "Bold"), fill=(255, 120, 90, 255), anchor="lm")
    img.alpha_composite(lay2)
    paste_c(img, star17(max(5, sr), T, halo=1.25 if sr > 60 else 2.0), cx, cy)
    d = ImageDraw.Draw(img)
    state = "INSIDE THE STAR" if sr > rp(1.0) else ("TOO HOT" if 1.0 < zi else ("TOO COLD" if 1.0 > zo else "JUST RIGHT"))
    scol = {"TOO HOT": (255, 120, 80), "TOO COLD": (120, 190, 255), "JUST RIGHT": (120, 255, 150), "INSIDE THE STAR": (255, 160, 60)}[state]
    alpha_text(img, (1180, 250), v.get("kicker", "THE EARTH-LIKE ZONE"), F(36, "Bold"), (120, 230, 150), 1, anchor="lm")
    alpha_text(img, (1180, 340), v.get("name", ""), F(70, "Black"), WHITE, 1, anchor="lm")
    zt = (f"{zi:,.0f}–{zo:,.0f} AU" if zi >= 10 else f"{zi:.2f}–{zo:.2f} AU")
    alpha_text(img, (1180, 450), "zone: " + zt, F(44, "ExtraBold"), (140, 240, 170), 1, anchor="lm", shadow=False)
    alpha_text(img, (1180, 540), "Earth (1 AU):", F(38, "SemiBold"), DIM, 1, anchor="lm", shadow=False)
    alpha_text(img, (1180, 610), state, F(64, "Black"), scol, ease((t - 2.4) / 0.5), anchor="lm")
    if v.get("note"): alpha_text(img, (1180, 720), v["note"], F(36, "SemiBold"), WHITE, ease((t - 2.8) / 0.5), anchor="lm")
    d = ImageDraw.Draw(img)
    d.text((1180, 960), "square-root distance scale · 1 AU = Earth–Sun", font=F(24, "Medium"), fill=(110, 115, 140), anchor="lm")
    d.text((1180, 995), "zone limits: Kopparapu et al. 2013, scaled by √brightness", font=F(24, "Medium"), fill=(110, 115, 140), anchor="lm")

def sc_earthtemp(img, v, t, dur):
    """Earth globe tinted by the new average temperature (ice white / scorched orange) + a thermometer −250…500 °C with landmarks
    (air freezes, water, lead melts, Venus); the reading slides from today's 15 °C to v.temp; simple estimate: T ∝ L^¼ (same air, clouds)"""
    p = easeio((t - 0.5) / 2.0); temp = lerp(15, v["temp"], p)
    paste_c(img, earth_sprite(230, glow=(120, 180, 255)), 540, 560)
    cold = max(0, min(1, (0 - temp) / 120)); hot = max(0, min(1, (temp - 40) / 300))
    m = Image.new("L", (520, 520), 0); ImageDraw.Draw(m).ellipse([30, 30, 490, 490], fill=255)
    ov = Image.new("RGBA", (520, 520), (235, 245, 255, 0))
    if cold > 0: ov = Image.new("RGBA", (520, 520), (235, 245, 255, int(215 * cold)))
    if hot > 0: ov = Image.new("RGBA", (520, 520), (230, 90, 30, int(200 * hot)))
    ov.putalpha(Image.fromarray((np.asarray(m, np.float32) * np.asarray(ov.getchannel("A"), np.float32) / 255).astype(np.uint8)))
    img.alpha_composite(ov, (540 - 260, 560 - 260))
    if hot > 0.3:
        d = ImageDraw.Draw(img); rng = random.Random(3)
        for _ in range(26):
            a0 = rng.uniform(0, 6.28); r0 = rng.uniform(20, 200); x, y = 540 + r0 * math.cos(a0), 560 + r0 * math.sin(a0)
            pts = [(x, y)]
            for _k in range(4): x += rng.uniform(-22, 22); y += rng.uniform(-22, 22); pts.append((x, y))
            d.line(pts, fill=(255, 210, 120), width=2)
    x, y0, y1 = 1150, 900, 180; tmin, tmax = -250, 500
    def ty(c): return lerp(y0, y1, (c - tmin) / (tmax - tmin))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x - 22, y1 - 20, x + 22, y0 + 20], 22, fill=(30, 34, 50), outline=(150, 160, 190), width=3)
    fc = (120, 190, 255) if temp < 0 else ((255, 200, 80) if temp < 100 else (255, 100, 60))
    d.rounded_rectangle([x - 12, ty(temp), x + 12, y0 + 10], 12, fill=fc)
    d.ellipse([x - 38, y0 - 4, x + 38, y0 + 72], fill=fc)
    marks = [(-210, "−210 °C  air (nitrogen) freezes"), (0, "0 °C  water freezes"), (15, "15 °C  Earth today"), (100, "100 °C  water boils"),
             (327, "327 °C  lead melts"), (464, "464 °C  Venus's surface")]
    for c, lab in marks:
        yy = ty(c); d.line([(x + 30, yy), (x + 60, yy)], fill=(200, 205, 220), width=3)
        d.text((x + 72, yy + {15: -16, 0: 14}.get(c, 0)), lab, font=F(28, "SemiBold"), fill=WHITE if c == 15 else DIM, anchor="lm")
    d.text((540, 880), f"{temp:+.0f} °C", font=F(92, "Black"), fill=fc, anchor="mm")
    d.text((540, 960), v.get("label", "average temperature, simple estimate"), font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    if v.get("head"): alpha_text(img, (W / 2, 110), v["head"], F(56, "Black"), WHITE, ease((t - 0.2) / 0.5))


# ---------------- scenes (EP18: the elevator into Jupiter) ----------------
_j18 = {}
def jup18(r):
    """banded Jupiter at radius r, drawn ONCE at r=500 with jup10 and resized (never one array per radius: see 2026-11-22 notes)"""
    r = max(4, int(r))
    if r not in _j18:
        if len(_j18) > 40: _j18.clear()
        base = jup10(500, 0.0); k = r / 500.0
        _j18[r] = base.resize((max(8, int(base.width * k)), max(8, int(base.height * k))), Image.BILINEAR)
    return _j18[r]

def _capsule18(img, x, y, s=1.0, glow=0.0, ang=0.0):
    """the imaginary unbreakable capsule: rounded cone + window, optional plasma glow"""
    if glow > 0: paste_c(img, radial(int(60 * s * (1 + glow)), [(0, (255, 240, 200, 255)), (0.3, (255, 150, 60, 200)), (1, (255, 80, 20, 0))]), x, y, min(1, glow))
    d = ImageDraw.Draw(img); c, sn = math.cos(ang), math.sin(ang)
    def P(px, py): return (x + (px * c - py * sn) * s, y + (px * sn + py * c) * s)
    d.polygon([P(-18, -26), P(18, -26), P(26, 18), P(-26, 18)], fill=(215, 220, 232), outline=(90, 95, 120))
    d.polygon([P(-30, 14), P(30, 14), P(24, 26), P(-24, 26)], fill=(120, 80, 60))
    wx, wy = P(0, -6); d.ellipse([wx - 7 * s, wy - 7 * s, wx + 7 * s, wy + 7 * s], fill=(90, 190, 255))

def _hud18(img, rows, x0=1360, y0=620, w=500, col=(230, 170, 100)):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([x0, y0, x0 + w, y0 + 70 + 82 * len(rows)], 24, fill=(8, 6, 14, 210), outline=col + (200,), width=3)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    for i, (k, val) in enumerate(rows):
        d.text((x0 + 30, y0 + 60 + i * 82), k, font=F(28, "Bold"), fill=DIM, anchor="lm")
        d.text((x0 + w - 30, y0 + 60 + i * 82), val, font=F(42, "ExtraBold"), fill=WHITE, anchor="rm")

_hz18 = {}
def _horizon18(R_, cy):
    """full-frame layer with the top of a radius-R_ Jupiter centred at (W/2, cy): built once from the r=500 sprite, cropped, cached"""
    key = (R_, int(cy))
    if key not in _hz18:
        base = jup10(500, 0.0); k = R_ / 500.0; side = base.width * k
        # crop the part of the base sprite that lands on screen, then scale only that
        x0s, y0s = (W / 2 - side / 2), (cy - side / 2)
        bx0, by0 = max(0, -x0s / k), max(0, -y0s / k); bx1, by1 = min(base.width, (W - x0s) / k), min(base.height, (H - y0s) / k)
        part = base.crop((int(bx0), int(by0), int(math.ceil(bx1)), int(math.ceil(by1)))).resize((int((math.ceil(bx1) - int(bx0)) * k), int((math.ceil(by1) - int(by0)) * k)), Image.BILINEAR)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); lay.alpha_composite(part, (int(x0s + int(bx0) * k), int(y0s + int(by0) * k)))
        _hz18[key] = lay
    return _hz18[key]

def sc_plunge(img, v, t, dur):
    """falling toward Jupiter. mode hook = giant cloud limb + the capsule streaking down | approach = Jupiter grows from Europa's distance,
    speed counter v0->v1 (∝ √ of the fall) + hours counter | view = Jupiter at 12.2° with 23 full Moons lined up across it, then it swells
    to fill the frame | entry = cloud horizon, capsule wrapped in plasma, speed + g meter rising to v.g (v.label = caption)"""
    mode = v.get("mode", "hook"); d = ImageDraw.Draw(img)
    if mode in ("hook", "entry"):
        # cloud horizon: a huge banded arc rising from the bottom
        R_ = 1900; cy = H + R_ - 430 + (0 if mode == "hook" else 60)
        img.alpha_composite(_horizon18(R_, cy))
        haze = Image.new("RGBA", img.size, (0, 0, 0, 0)); dh = ImageDraw.Draw(haze)
        for k in range(14): dh.ellipse([W / 2 - R_ - k * 6, cy - R_ - k * 6, W / 2 + R_ + k * 6, cy + R_ + k * 6], outline=(255, 210, 160, 14), width=6)
        img.alpha_composite(haze)
        if mode == "hook":
            p = (t * 0.22) % 1.0; x, y = lerp(560, 1150, p), lerp(150, 700, p)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            dl.line([(x - 260, y - 240), (x, y)], fill=(255, 220, 170, 120), width=6); img.alpha_composite(lay)
            _capsule18(img, x, y, 1.4, glow=0.3 + 0.7 * p, ang=-0.83)
            if v.get("head"): alpha_text(img, (W / 2, 140), v["head"], F(84, "Black"), WHITE, ease(t / 0.4))
            return
        p = (t * 0.35) % 1.0; x, y = lerp(300, 1400, p), lerp(200, 560, p)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for k in range(18):
            off = k * 9; dl.line([(x - 500 - off, y - 170 - off * 0.3 + k * 4), (x - 40, y - 10)], fill=(255, 160 - k * 4, 60, max(0, 150 - k * 8)), width=12 - k // 2)
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(4)))
        _capsule18(img, x, y, 1.6, glow=1.4 + 0.3 * math.sin(t * 20), ang=-1.25)
        rows = [("SPEED", f"{v.get('v0', 47):.1f} km/s")]
        if v.get("g"):
            g = v["g"] * math.exp(-((t - dur * 0.45) / (dur * 0.22)) ** 2) if t < dur * 0.45 else v["g"] * math.exp(-((t - dur * 0.45) / (dur * 0.35)) ** 2)
            rows.append(("BRAKING", f"{g:,.0f} g")); rows.append(("SHIELD", "≈ 16,000 °C"))
        _hud18(img, rows, y0=150)
        if v.get("label"): caption(img, v["label"], ease((t - 0.4) / 0.5), y=H - 90)
        return
    if mode == "approach":
        p = easeio(t / max(1.0, dur * 0.9)); r = lerp(40, 520, p ** 2.2)
        paste_c(img, jup18(r), 820, 560)
        # Europa shrinking away behind
        paste_c(img, planet_sprite(max(3, int(26 * (1 - p) + 3)), (210, 190, 160)), 200 + 100 * p, 900 + 80 * p, max(0.0, 1 - p))
        _capsule18(img, 1500 - 300 * p, 300 + 120 * p, 1.0, glow=p ** 4, ang=2.3)
        vel = lerp(v.get("v0", 0), v.get("v1", 56.3), p ** 1.7); hrs = v.get("hours", 14.8) * p
        _hud18(img, [("SPEED", f"{vel:.1f} km/s"), ("FALLING FOR", f"{hrs:.1f} h"), ("FROM", "Europa's orbit")], y0=640)
        alpha_text(img, (W / 2, 110), "Floor 1 · the fall", F(54, "Black"), WHITE, ease(t / 0.4))
        return
    if mode == "view":
        p = easeio((t - dur * 0.55) / (dur * 0.4)); mr = 17
        rj = mr * 23.4 * (1 + 3.5 * p ** 2)
        paste_c(img, jup18(rj), W / 2, H / 2 + 20)
        q = 1 - p
        if q > 0.02:
            for i in range(23):
                a_ = ease((t - 0.4 - i * 0.07) / 0.3) * q
                if a_ > 0: paste_c(img, planet_sprite(mr, (225, 225, 230)), W / 2 - rj + mr + i * 2 * mr * (rj / (mr * 23.4)), H / 2 + 20, a_)
            alpha_text(img, (W / 2, H / 2 + 20 + rj + 60), "23 full Moons, side by side", F(44, "ExtraBold"), CREAM18, q * ease((t - 1.8) / 0.5))
        alpha_text(img, (W / 2, 110), "From Europa: 12.2° of sky", F(56, "Black"), WHITE, ease(t / 0.4))

CREAM18 = (245, 225, 185)
GAUGE18 = [(0, 120, (235, 210, 160)), (120, 10000, (150, 95, 60)), (10000, 35000, (110, 70, 190)), (35000, 70000, (200, 80, 70))]
def _gy18(dep, y0=170, y1=980): return lerp(y0, y1, math.log10(1 + max(0, dep)) / math.log10(70001))

def sc_depthgauge(img, v, t, dur):
    """chapter card: a vertical depth gauge 0 -> 70,000 km on a log scale (bands: clouds / deep air / metallic hydrogen / dilute core),
    the capsule slides down to v.depth; background darkens with depth; right panel: floor name, depth, pressure, temperature, note"""
    dep = v["depth"]; p = easeio((t - 0.3) / 1.6); cur = lerp(dep * 0.25, dep, p)
    dark = min(1.0, math.log10(1 + dep) / 5.0)
    lay = Image.new("RGBA", img.size, mix((40, 22, 10), (18, 6, 30), dark) + (int(120 + 110 * dark),)); img.alpha_composite(lay)
    d = ImageDraw.Draw(img); x0, x1 = 230, 330
    for a_, b_, c in GAUGE18:
        d.rectangle([x0, _gy18(a_), x1, _gy18(b_)], fill=c)
    d.rectangle([x0, _gy18(0), x1, _gy18(70000)], outline=(230, 230, 240), width=3)
    for mk in (0, 10, 100, 1000, 10000, 70000):
        y = _gy18(mk); d.line([(x0 - 22, y), (x0, y)], fill=(220, 220, 235), width=3)
        d.text((x0 - 32, y), (f"{mk:,} km" if mk else "0"), font=F(26, "Bold"), fill=(200, 200, 220), anchor="rm")
    for (a_, b_, c), nm in zip(GAUGE18, ("clouds", "deep air", "metal", "core")):
        d.text((x1 + 18, (_gy18(a_) + _gy18(b_)) / 2), nm, font=F(24, "SemiBold"), fill=mix(c, (255, 255, 255), 0.4), anchor="lm")
    yc = _gy18(cur); d.line([(x0 - 6, yc), (x1 + 6, yc)], fill=(90, 220, 255), width=4)
    _capsule18(img, (x0 + x1) / 2, yc - 30, 0.9, glow=0.2)
    a1, a2 = ease((t - 0.2) / 0.5), ease((t - 0.8) / 0.5)
    alpha_text(img, (620, 230), v.get("floor", ""), F(46, "ExtraBold"), (230, 170, 100), a1, anchor="lm")
    num = f"−{cur:,.0f} km" if dep >= 1 else "0 km"
    alpha_text(img, (620, 370), num, F(150, "Black"), WHITE, a1, anchor="lm")
    rows = [r_ for r_ in (("PRESSURE", v.get("ptxt")), ("TEMPERATURE", v.get("ttxt"))) if r_[1]]
    for i, (k, val) in enumerate(rows):
        alpha_text(img, (625, 540 + i * 120), k, F(30, "Bold"), DIM, a2, anchor="lm", shadow=False)
        alpha_text(img, (625, 590 + i * 120), val, F(56, "ExtraBold"), (255, 215, 150) if i else (150, 210, 255), a2, anchor="lm")
    if v.get("note"): alpha_text(img, (625, 860), v["note"], F(36, "SemiBold"), WHITE, ease((t - 1.3) / 0.5), anchor="lm")
    d = ImageDraw.Draw(img)
    d.text((625, 960), "depth below the 1-bar level · log scale" + (" · model values" if v.get("approx") else ""), font=F(24, "Medium"), fill=(150, 150, 175), anchor="lm")

DECKS18 = [(0.7, "ammonia ice", (245, 245, 240)), (2.2, "ammonium hydrosulfide", (200, 140, 90)), (5.0, "water + lightning", (150, 190, 230))]
def _py18(pb, y0=200, y1=1000): return lerp(y0, y1, (math.log10(pb) + 0.7) / (math.log10(25) + 0.7))
def sc_cloudstack(img, v, t, dur):
    """side cross-section of the top of Jupiter's atmosphere on a log PRESSURE axis 0.2 -> 25 bar: three cloud decks (model levels 0.7 /
    2.2 / 5 bar) as textured bands, the capsule sinking to the highlighted deck, Galileo's parachute path to 23 bar (dotted), optional wind
    streaks (v.wind) that speed up with depth + "600+ km/h" (Galileo, Atkinson et al. 1998)"""
    hl = v.get("hl", 0); target = [0.7, 2.2, 5.0, 15.0][min(hl, 3)]
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for y in range(140, 1040, 8):
        u = (y - 140) / 900; dl.rectangle([0, y, W, y + 8], fill=mix((70, 110, 170), (30, 14, 8), u ** 0.8) + (235,))
    img.alpha_composite(lay)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(18)
    for i, (pb, nm, c) in enumerate(DECKS18):
        y = _py18(pb); on = (i == hl) or hl == 3
        for k in range(70):
            x = (rng.uniform(-100, W + 100) + t * (12 + 10 * i) * (1 if k % 2 else -0.6)) % (W + 200) - 100
            r_ = rng.uniform(30, 90); yy = y + rng.uniform(-28, 28)
            dl.ellipse([x - r_, yy - r_ * 0.35, x + r_, yy + r_ * 0.35], fill=c + (int((150 if on else 70) * rng.uniform(0.5, 1)),))
        if i == 2 and on and int(t * 3) % 4 == 0:
            lx = 300 + (int(t * 3) * 337) % 1200; dl.line([(lx, y - 30), (lx + 20, y), (lx - 10, y + 20), (lx + 15, y + 50)], fill=(255, 255, 200, 255), width=5)
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(3)))
    d = ImageDraw.Draw(img)
    for i, (pb, nm, c) in enumerate(DECKS18):
        y = _py18(pb); on = (i == hl)
        d.text((W - 60, y), f"{nm} · ≈ {pb:g} bar", font=F(36 if on else 28, "ExtraBold" if on else "SemiBold"), fill=c if on else mix(c, (90, 90, 110), 0.4), anchor="rm", stroke_width=3, stroke_fill=(0, 0, 0))
    for pb in (0.3, 1, 3, 10, 23):
        y = _py18(pb); d.line([(60, y), (90, y)], fill=(220, 220, 235), width=3); d.text((100, y), f"{pb:g} bar", font=F(26, "Bold"), fill=(220, 220, 235), anchor="lm")
    y1b = _py18(1.0)
    for x in range(60, W, 30): d.line([(x, y1b), (x + 14, y1b)], fill=(255, 255, 255), width=2)
    d.text((300, y1b - 22), "the zero line (1 bar)", font=F(24, "SemiBold"), fill=WHITE, anchor="lm")
    # Galileo's path, dotted, with a parachute at its last point
    gx = 520
    for k in range(40):
        pb = 0.4 * (23 / 0.4) ** (k / 39); y = _py18(pb); d.ellipse([gx + 30 * math.sin(k * 0.5) - 3, y - 3, gx + 30 * math.sin(k * 0.5) + 3, y + 3], fill=(255, 230, 120))
    ye = _py18(23); d.arc([gx - 40, ye - 70, gx + 40, ye - 10], 180, 360, fill=(255, 230, 120), width=5)
    d.text((gx + 50, ye - 20), "Galileo, 1995 · signal lost ≈ 23 bar", font=F(26, "Bold"), fill=(255, 230, 120), anchor="lm", stroke_width=3, stroke_fill=(0, 0, 0))
    cp = math.exp(lerp(math.log(max(0.3, target / 3)), math.log(target), easeio((t - 0.2) / 1.8)))
    _capsule18(img, 900, _py18(cp) - 30, 1.0, glow=0.15)
    if v.get("wind"):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(4)
        for k in range(60):
            pb = math.exp(rng.uniform(math.log(0.5), math.log(22))); y = _py18(pb); sp = 300 + 900 * (math.log10(pb) + 0.3) / 1.6
            x = (rng.uniform(0, W) + t * sp) % (W + 300) - 300; L = 80 + sp * 0.15
            dl.line([(x, y), (x + L, y)], fill=(255, 255, 255, 130), width=3)
        img.alpha_composite(lay)
        box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1320, 820, 1860, 1000], 22, fill=(10, 8, 6, 220)); img.alpha_composite(box)
        d = ImageDraw.Draw(img); d.text((1590, 880), "600+ km/h", font=F(64, "Black"), fill=(255, 215, 150), anchor="mm")
        d.text((1590, 950), "winds grow stronger with depth", font=F(28, "Bold"), fill=WHITE, anchor="mm")
    alpha_text(img, (W / 2, 80), "Floor 3 · the clouds", F(50, "Black"), WHITE, ease(t / 0.4))

def sc_nosurface(img, v, t, dur):
    """phase 0: a column of hydrogen getting denser with depth, a dashed 'surface?' line scans down and never finds a boundary (NOT HERE
    stamps) + the critical point note (−240 °C, 13 bar) | phase 1: the capsule sinks slower and slower through a continuous gradient,
    density meter | phase 2: helium rain: droplets fall through violet metallic hydrogen, carrying pink neon specks"""
    ph = v.get("phase", 0); d = ImageDraw.Draw(img)
    if ph in (0, 1):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for y in range(0, H, 6):
            u = y / H; dl.rectangle([0, y, W, y + 6], fill=mix((170, 120, 80), (25, 8, 6), u ** 0.7) + (int(lerp(120, 255, u)),))
        img.alpha_composite(lay)
        rng = random.Random(7); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for k in range(500):  # molecules: more of them, slower, deeper
            u = rng.random() ** 0.6; y = u * H; sp = lerp(60, 4, u); x = (rng.uniform(0, W) + t * sp) % W
            dl.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(255, 220, 180, int(lerp(90, 200, u))))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        if ph == 0:
            for j in range(3):
                yy = 260 + j * 260
                if t > 0.8 + j * 1.2:
                    for x in range(80, 1200, 34): d.line([(x, yy), (x + 18, yy)], fill=(255, 255, 255), width=3)
                    d.text((100, yy - 26), "surface here?", font=F(30, "Bold"), fill=WHITE, anchor="lm")
                    alpha_text(img, (1000, yy), "NOT HERE", F(56, "Black"), (255, 110, 90), ease((t - 1.3 - j * 1.2) / 0.3))
            box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1280, 300, 1860, 700], 24, fill=(10, 8, 14, 225)); img.alpha_composite(box)
            d = ImageDraw.Draw(img)
            for i, (s_, c_, f_) in enumerate((("HYDROGEN", (230, 170, 100), 32), ("above −240 °C and 13 bar:", WHITE, 30), ("no line between", WHITE, 34), ("gas and liquid", WHITE, 34))):
                d.text((1570, 370 + i * 80), s_, font=F(f_, "ExtraBold"), fill=c_, anchor="mm")
        else:
            p = 1 - math.exp(-t / (dur * 0.35)); y = lerp(200, 820, p)
            _capsule18(img, 760, y, 1.3, glow=0.1)
            dens = lerp(0.01, 0.4, p)
            _hud18(img, [("SINKING SPEED", "slower and slower"), ("SURFACE FOUND", "none")], y0=300, w=560)
            alpha_text(img, (W / 2, 90), "Floor 5 · where's the surface?", F(50, "Black"), WHITE, ease(t / 0.4))
        if ph == 0: alpha_text(img, (W / 2, 90), "Floor 5 · where's the surface?", F(50, "Black"), WHITE, ease(t / 0.4))
        return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for y in range(0, H, 6):
        u = y / H; dl.rectangle([0, y, W, y + 6], fill=mix((50, 30, 90), (110, 70, 200), u) + (235,))
    img.alpha_composite(lay)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(11)
    for k in range(260):  # metallic sheen: drifting electrons
        x = (rng.uniform(0, W) + t * rng.uniform(-80, 80)) % W; y = rng.uniform(0, H)
        dl.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(140, 200, 255, 150))
    for k in range(40):  # helium droplets with neon passengers
        x = rng.uniform(80, W - 380); sp = rng.uniform(120, 240); y = (rng.uniform(0, H) + t * sp) % (H + 80) - 40; r_ = rng.uniform(10, 22)
        dl.ellipse([x - r_ * 0.8, y - r_, x + r_ * 0.8, y + r_ * 1.1], fill=(230, 235, 255, 220), outline=(255, 255, 255, 255), width=2)
        dl.ellipse([x - 4, y - 2, x + 4, y + 6], fill=(255, 90, 170, 255))
        dl.line([(x, y - r_ - 4), (x, y - r_ - 4 - sp * 0.25)], fill=(230, 235, 255, 90), width=3)
    img.alpha_composite(lay)
    box = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(box).rounded_rectangle([1460, 360, 1880, 740], 24, fill=(10, 6, 20, 225)); img.alpha_composite(box)
    d = ImageDraw.Draw(img)
    for i, (c_, lab) in enumerate((((230, 235, 255), "helium droplet"), ((255, 90, 170), "neon, carried down"), ((140, 200, 255), "free electrons"))):
        d.ellipse([1490, 425 + i * 100, 1520, 455 + i * 100], fill=c_); d.text((1540, 440 + i * 100), lab, font=F(30, "Bold"), fill=WHITE, anchor="lm")
    d.text((1670, 700), "illustration", font=F(24, "Medium"), fill=DIM, anchor="mm")
    alpha_text(img, (W / 2, 90), "Floor 6 · helium rain", F(50, "Black"), WHITE, ease(t / 0.4))

def sc_jupcut(img, v, t, dur):
    """Jupiter cut open TO SCALE (r = 420 px for 69,911 km): a wedge shows molecular hydrogen, metallic hydrogen (from ≈ 10,000 km down),
    the dilute core (to ≈ half the radius) or the old compact core (hl=oldcore); Earth to scale beside it; the capsule marker at v.depth
    on the cut edge; hl=skin adds a magnifier on Galileo's 150 km sliver"""
    cx, cy, Rj = 600, 560, 420; hl = v.get("hl", "skin")
    paste_c(img, jup18(Rj), cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    a0, a1 = -70, 20
    def wedge(rf, col): rr = Rj * rf; dl.pieslice([cx - rr, cy - rr, cx + rr, cy + rr], a0, a1, fill=col)
    q = lambda name: 255 if hl == name else 200
    wedge(1.0, (190, 140, 95, 255)); wedge(0.995, (150, 100, 70, 255))
    wedge(1 - 10000 / 69911, (100, 70, 180, q("metal")))
    if hl in ("dilute", "centre"): wedge(0.5, (200, 90, 80, 230)); wedge(0.25, (230, 120, 90, 240))
    elif hl == "oldcore": wedge(0.15, (120, 110, 100, 255))
    else: wedge(0.5, (150, 70, 120, 200))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    if hl == "metal":
        rr = Rj * (1 - 10000 / 69911); pul = 0.5 + 0.5 * math.sin(t * 3)
        d.arc([cx - rr, cy - rr, cx + rr, cy + rr], a0, a1, fill=mix((140, 200, 255), (255, 255, 255), pul), width=6)
    if hl == "oldcore":
        rr = Rj * 0.15; d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(255, 255, 255), width=4)
    dep = v.get("depth", 0); rr = Rj * (1 - min(69900, dep) / 69911); ang = math.radians(a0 + 2)
    mx, my = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
    d.ellipse([mx - 11, my - 11, mx + 11, my + 11], fill=(90, 220, 255), outline=(255, 255, 255), width=3)
    # Earth to scale
    er = Rj * 6371 / 69911; paste_c(img, earth_sprite(int(er)), 150, cy + Rj - 20)
    d = ImageDraw.Draw(img); d.text((150, cy + Rj + 40), "Earth, to scale", font=F(26, "SemiBold"), fill=(150, 200, 255), anchor="mm")
    if hl == "skin":
        lx, ly, lr = 1180, 330, 170; ex, ey = cx + Rj * math.cos(ang), cy + Rj * math.sin(ang)
        d.line([(ex, ey), (lx - lr * 0.7, ly + lr * 0.7)], fill=(255, 255, 255), width=3)
        d.ellipse([lx - lr, ly - lr, lx + lr, ly + lr], fill=(40, 25, 18), outline=(255, 255, 255), width=5)
        d.rectangle([lx - lr + 30, ly - 120, lx + lr - 30, ly - 60], fill=(200, 150, 100))
        d.line([(lx, ly - 60), (lx, ly - 60 + 100 * ease((t - 0.5) / 1.5))], fill=(255, 230, 120), width=6)
        d.text((lx, ly + 90), "Galileo's 150 km", font=F(28, "Bold"), fill=(255, 230, 120), anchor="mm")
    labels = {"skin": ("0.2% OF THE WAY", (255, 230, 120)), "metal": ("METALLIC HYDROGEN", (150, 200, 255)), "oldcore": ("A SOLID CORE?", (220, 210, 200)),
              "dilute": ("A DILUTE CORE", (255, 150, 120)), "centre": ("NO FLOOR", (255, 150, 120))}
    lab, col = labels.get(hl, ("", WHITE))
    alpha_text(img, (1180, 640 if hl == "skin" else 400), lab, F(72 if len(lab) < 14 else 56, "Black"), col, ease((t - 0.4) / 0.5), anchor="lm")
    if v.get("note"): alpha_text(img, (1182, 720 if hl == "skin" else 490), v["note"], F(38, "SemiBold"), WHITE, ease((t - 0.9) / 0.5), anchor="lm")
    d = ImageDraw.Draw(img)
    for i, (c_, n_) in enumerate((((190, 140, 95), "hydrogen + helium gas → fluid"), ((100, 70, 180), "metallic hydrogen"), ((200, 90, 80), "heavy elements, mixed in"))):
        d.rectangle([1182, 820 + i * 50, 1210, 848 + i * 50], fill=c_); d.text((1226, 834 + i * 50), n_, font=F(28, "SemiBold"), fill=(215, 215, 230), anchor="lm")
    d.text((1182, 990), "layer depths from interior models · to scale", font=F(24, "Medium"), fill=(140, 140, 165), anchor="lm")

def sc_scars(img, v, t, dur):
    """Shoemaker-Levy 9 (July 1994): phase 0 = a train of 21 fragments sweeps in and flashes one by one near the southern limb, day counter
    1 -> 6 | phase 1 = the dark scars rotate into view along one southern latitude, with Earth to scale beside the biggest one"""
    cx, cy, Rj = 760, 560, 430; ph = v.get("phase", 0)
    paste_c(img, jup18(Rj), cx, cy); d = ImageDraw.Draw(img)
    lat = math.radians(-44); yb = cy - Rj * math.sin(lat) * 1.0
    if ph == 0:
        n_hit = int(min(21, max(0, (t - 0.8) / max(0.5, dur - 1.5) * 21)))
        for i in range(n_hit, 21):
            k = i - n_hit; x = cx - Rj * 0.5 - 90 - k * 46 - (t * 25) % 46 * 0; y = yb - 420 - k * 16
            d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=(230, 235, 255)); d.line([(x, y), (x - 50, y - 18)], fill=(160, 190, 255), width=2)
        if n_hit > 0 and (t * 4) % 1 < 0.6:
            fx = cx - Rj * math.cos(lat) * 0.92; paste_c(img, radial(90, [(0, (255, 255, 230, 255)), (0.3, (255, 200, 120, 200)), (1, (255, 120, 40, 0))]), fx, yb - 10)
        day = 1 + 5 * min(1, max(0, (t - 0.8) / max(0.5, dur - 1.5)))
        _hud18(img, [("FRAGMENTS LEFT", f"{21 - n_hit}"), ("DAY", f"{day:.0f} of 6")], x0=1380, y0=700, w=470)
        alpha_text(img, (W / 2, 90), "July 1994 · comet Shoemaker-Levy 9", F(52, "Black"), WHITE, ease(t / 0.4))
        return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(94)
    for i in range(9):
        lon = -1.3 + i * 0.32 + t * 0.06
        if abs(lon) > 1.45: continue
        x = cx + Rj * math.cos(lat) * math.sin(lon); s_ = math.cos(lon); r_ = rng.uniform(18, 48) * (1.25 if i == 4 else 1)
        dl.ellipse([x - r_ * s_, yb - r_ * 0.55, x + r_ * s_, yb + r_ * 0.55], fill=(35, 20, 18, 230))
        dl.ellipse([x - r_ * s_ * 0.5, yb - r_ * 0.3, x + r_ * s_ * 0.5, yb + r_ * 0.3], fill=(15, 8, 8, 240))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2)))
    er = Rj * 6371 / 71492; paste_c(img, earth_sprite(int(er)), cx + Rj + 160, yb)
    d = ImageDraw.Draw(img); d.text((cx + Rj + 160, yb + er + 34), "Earth, to scale", font=F(28, "SemiBold"), fill=(150, 200, 255), anchor="mm")
    alpha_text(img, (W / 2, 90), "Scars bigger than Earth", F(56, "Black"), WHITE, ease(t / 0.4))
    caption(img, "illustration of the 1994 impact sites; the darkest were larger than Earth (NASA)", ease((t - 0.8) / 0.5), y=H - 80)


# ---------------- scenes (EP19: what if Earth had a second Moon?) ----------------
LIL19, AQUA19, AMB19, RED19 = (200, 190, 255), (90, 220, 210), (255, 180, 90), (255, 105, 95)
GM19, OM19 = 3.986e5, 2 * math.pi / (365.25 * 86400)
_ph19 = {}
def moon19(r, k=-1.0, far=False):
    """Moon sprite with a phase: k = cos(phase angle) -> lit where x >= k·sqrt(1-y²) (k=-1 full, 0 half, 1 new); far = far-side look"""
    r = max(4, int(r)); key = (r, round(k, 2), far)
    if key in _ph19: return _ph19[key]
    if far:
        base = planet_sprite(r, (196, 193, 188), light=(-0.2, -0.1)).copy()
        a = np.asarray(base, np.float32).copy(); s = a.shape[0]
        yy, xx = np.mgrid[0:s, 0:s].astype(np.float32); nx, ny = (xx - s / 2) / r, (yy - s / 2) / r
        rng = np.random.default_rng(19)
        for _ in range(70):
            cx, cy, cr = rng.uniform(-0.9, 0.9), rng.uniform(-0.9, 0.9), rng.uniform(0.02, 0.09)
            dd = np.hypot(nx - cx, ny - cy); a[..., :3] *= (1 - 0.2 * ((dd < cr) & (dd > cr * 0.65)))[..., None]
        m = np.exp(-(((nx + 0.05) ** 2 + (ny - 0.55) ** 2) / (2 * 0.12 ** 2))); a[..., :3] *= (1 - 0.25 * m)[..., None]
        base = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
    else:
        base = moon8(r, light=(-0.2, -0.1)).copy()
    if k > -0.99:
        a = np.asarray(base, np.float32).copy(); s = a.shape[0]
        yy, xx = np.mgrid[0:s, 0:s].astype(np.float32); nx, ny = (xx - s / 2) / r, (yy - s / 2) / r
        lim = k * np.sqrt(np.clip(1 - ny ** 2, 0, 1)); lit = np.clip((nx - lim) * r / 2.0 + 0.5, 0, 1)
        a[..., :3] *= (0.06 + 0.94 * lit)[..., None]
        base = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
    _ph19[key] = base
    return base

def _sized19(r, k=-1.0, far=False):
    if r <= 240: return moon19(r, k, far)
    spr = moon19(240, k, far); q = r / 240.0
    return spr.resize((int(spr.width * q), int(spr.height * q)), Image.BILINEAR)

def _box19(img, x0, y0, x1, y1, col, a=210):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle([x0, y0, x1, y1], 24, fill=(8, 8, 26, a), outline=col + (150,), width=2); img.alpha_composite(lay)

def _stamp19(img, txt, col, cx, cy, p, ang=-8):
    if p <= 0: return
    f = F(84, "Black"); tw = int(f.getlength(txt)) + 80
    lay = Image.new("RGBA", (tw + 40, 190), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([20, 20, tw + 20, 170], 18, outline=col + (255,), width=10)
    d.text(((tw + 40) / 2, 95), txt, font=f, fill=col + (255,), anchor="mm")
    k = lerp(1.8, 1.0, ease(p / 0.6)); lay = lay.rotate(ang, expand=True, resample=Image.BICUBIC)
    lay = lay.resize((int(lay.width * k), int(lay.height * k)), Image.BILINEAR)
    al = lay.getchannel("A").point(lambda v: int(v * min(1, p / 0.3))); lay.putalpha(al)
    img.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))

def _land19(img, glow):
    """desert mesas + a still lake, lit by moonlight glow 0..1"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for y in range(0, 800, 8):
        c = mix((10, 10, 34), (70, 74, 128), glow * (y / 800) ** 1.2 + glow * 0.25)
        d.rectangle([0, y, W, y + 8], fill=c + (int(120 + 110 * glow),))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    rock = mix((14, 12, 24), (60, 52, 72), glow)
    pts = [(0, 800), (0, 700), (130, 700), (160, 640), (420, 640), (450, 700), (700, 705), (760, 760), (1180, 760), (1210, 690),
           (1260, 600), (1520, 600), (1560, 680), (1700, 690), (1760, 730), (W, 730), (W, 800)]
    d.polygon(pts, fill=rock)
    d.rectangle([0, 800, W, H], fill=mix((8, 10, 26), (36, 44, 86), glow))

def sc_twinsky(img, v, t, dur):
    """night sky over mesas: our Moon + the twin at v.km2, sizes to scale with each other (v.fov sets the zoom); v.phase = phases"""
    km2 = v["km2"]; ang2 = 2 * math.degrees(math.atan(1737.4 / km2)); ratio = ang2 / 0.518
    fov = v.get("fov", 5.5 if ratio < 1.5 else 9.0 if ratio < 5 else 30.0); pxd = W / fov
    r1 = 0.518 * pxd / 2; r2 = ang2 * pxd / 2
    light = 1 + (384400 / km2) ** 2 * (0.75 if v.get("phase") else 1)
    glow = max(0.15, min(1.0, 0.18 + 0.32 * math.log10(light)))
    _land19(img, glow * ease(t / 0.8))
    p = easeio((t - 0.3) / 1.6)
    x1, y1 = 520, 330; x2, y2 = 1220, 300 + r2 * 0.25
    for (x, y, r, k, a) in ((x1, y1, r1, -1, 1.0), (x2, y2 + (1 - p) * 120, r2, (-0.5 if v.get("phase") else -1), p)):
        hal = radial(int(r * 6) + 20, [(0, (225, 225, 255, int(70 * a))), (0.35, (180, 180, 240, int(25 * a))), (1, (120, 120, 200, 0))])
        paste_c(img, hal, x, y); paste_c(img, _sized19(r, k), x, y, a)
    d = ImageDraw.Draw(img)
    # reflections on the lake
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for i, (x, r) in enumerate(((x1, r1), (x2, r2))):
        for k2 in range(10):
            yy = 830 + k2 * 22; ww = max(8, r * 0.9) * (1 + 0.15 * math.sin(t * 2 + k2 + i))
            dl.line([(x - ww, yy), (x + ww, yy)], fill=(220, 220, 255, int((140 - k2 * 12) * (p if i else 1))), width=3)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.text((x1, y1 + max(r1, 10) + 40), "our Moon", font=F(30, "Bold"), fill=LIL19, anchor="mm")
    d.text((x2, y2 + r2 + 40), "the twin", font=F(30, "Bold"), fill=AMB19, anchor="mm") if p > 0.5 else None
    _box19(img, 80, 870, 900, 1030, LIL19)
    d = ImageDraw.Draw(img)
    d.text((120, 915), v.get("head", ""), font=F(46, "ExtraBold"), fill=WHITE, anchor="lm")
    d.text((120, 985), v.get("sub", ""), font=F(36, "SemiBold"), fill=AMB19, anchor="lm")
    d.text((W - 60, 1030), "sizes to scale with each other", font=F(24, "SemiBold"), fill=DIM, anchor="rm")

SL_X0, SL_X1, SL_Y = 230, 1760, 560
def _sx19(km): return SL_X0 + (SL_X1 - SL_X0) * math.sqrt(max(0, km) / 1.5e6)
SLOTS19 = [(15000, "1"), (30000, "2"), (100000, "3"), (384400, "4"), (1000000, "5")]
def sc_slotmap(img, v, t, dur):
    """chapter card: square-root distance strip Earth -> Hill radius with zones; pins 1-5; v.n active pin, v.stamp verdict, v.drift in|out"""
    d = ImageDraw.Draw(img); a = ease(t / 0.5); p = easeio((t - 0.2) / 1.0)
    zones = [(0, 18400, RED19, "torn apart"), (18400, 42164, AMB19, "falls in"), (42164, 732000, AQUA19, "can stay"), (732000, 1.5e6, (150, 150, 175), "Sun steals")]
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for (k0, k1, c, lab) in zones:
        x0, x1 = _sx19(k0), _sx19(k1) * 1.0
        dl.rectangle([x0, SL_Y - 26, lerp(x0, x1, p), SL_Y + 26], fill=c + (80,))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    for (k0, k1, c, lab) in zones[1:]:
        xm = (_sx19(k0) + _sx19(k1)) / 2
        d.text((xm, SL_Y + 64), lab, font=F(26, "Bold"), fill=mix(SPACE, c, p), anchor="mm")
    d.text((_sx19(9000), SL_Y + 64), "torn", font=F(22, "Bold"), fill=mix(SPACE, RED19, p), anchor="mm")
    er = _sx19(6371) - SL_X0
    paste_c(img, earth_sprite(int(er), light=(1, -0.2)), SL_X0, SL_Y)
    d = ImageDraw.Draw(img)
    marks = [(18400, "Roche limit", -1, RED19), (42164, "geostationary", 1, AMB19), (384400, "our Moon", 1, LIL19), (732000, "stability edge", -1, AQUA19), (1.5e6, "edge of Earth's pull", 1, (190, 190, 210))]
    for i, (km, lab, side, c) in enumerate(marks):
        x = _sx19(km); aa = ease((t - 0.3 - i * 0.12) / 0.4)
        if aa <= 0: continue
        cc = mix(SPACE, c, aa)
        d.line([(x, SL_Y - 40), (x, SL_Y + 40)], fill=cc, width=3)
        yy = SL_Y - 150 if side < 0 else SL_Y + 120
        if km == 18400: yy = SL_Y - 190
        d.line([(x, SL_Y + side * 40), (x, yy + (30 if side < 0 else -18))], fill=mix(SPACE, c, aa * 0.5), width=1)
        d.text((x, yy), lab, font=F(26, "Bold"), fill=cc, anchor="mm")
        d.text((x, yy + 32), f"{km:,.0f} km", font=F(22, "SemiBold"), fill=mix(SPACE, DIM, aa), anchor="mm")
    paste_c(img, moon19(9), _sx19(384400), SL_Y)
    n = v.get("n", 0)
    for i, (km, lab) in enumerate(SLOTS19):
        x = _sx19(km); act = (i + 1 == n); aa = ease((t - 0.6 - i * 0.1) / 0.4)
        if aa <= 0: continue
        c = AMB19 if act else (110, 110, 140)
        y = SL_Y - (95 if km != 384400 else 110)
        if km == 384400: x += 26
        d.ellipse([x - 24, y - 24, x + 24, y + 24], fill=mix(SPACE, c, aa), outline=WHITE if act else None, width=3)
        d.text((x, y), lab, font=F(28, "Black"), fill=SPACE, anchor="mm")
        d.line([(x, y + 24), (x, SL_Y - 30)], fill=mix(SPACE, c, aa), width=2)
        if act:
            pulse = 1 + 0.08 * math.sin(t * 4)
            paste_c(img, radial(80, [(0, AMB19 + (120,)), (1, AMB19 + (0,))]), x, SL_Y); d = ImageDraw.Draw(img)
            paste_c(img, moon19(int(12 * pulse)), x, SL_Y); d = ImageDraw.Draw(img)
            dr = v.get("drift")
            if dr:
                s_ = -1 if dr == "in" else 1; ox = 30 * math.sin(t * 3) * 0.3
                for k2 in range(3):
                    ax = x + s_ * (40 + 30 * k2) + ox
                    d.polygon([(ax + s_ * 16, SL_Y + 0), (ax - s_ * 4, SL_Y - 14), (ax - s_ * 4, SL_Y + 14)], fill=AMB19 if dr == "out" else RED19)
    alpha_text(img, (160, 210), v.get("title", ""), F(72, "ExtraBold"), WHITE, a, anchor="lm")
    if v.get("sub"): alpha_text(img, (160, 290), v["sub"], F(38, "SemiBold"), AMB19, ease((t - 0.3) / 0.5), anchor="lm")
    d = ImageDraw.Draw(img)
    d.text((W - 60, H - 60), "distances on a square-root scale", font=F(24, "SemiBold"), fill=DIM, anchor="rm")
    if v.get("stamp"): _stamp19(img, v["stamp"], tuple(v.get("scol", AQUA19)), W / 2 + 200, 860, (t - 0.8) / 0.8)

def sc_tidechart(img, v, t, dur):
    """harbor tide: mode curve = 72 h of water level, Moon alone (dashed) / twin alone / both (thick), cursor; mode bar = log pull bars"""
    d = ImageDraw.Draw(img); a = ease(t / 0.5)
    alpha_text(img, (160, 170), v.get("head", ""), F(60, "ExtraBold"), WHITE, a, anchor="lm")
    ratio = v.get("ratio", 1.0)
    if v.get("mode") == "bar":
        p = easeio((t - 0.4) / 2.2); x0, x1 = 420, 1700
        lx = lambda val: x0 + (x1 - x0) * math.log10(max(1, val)) / math.log10(3000)
        for i, (lab, val, c) in enumerate((("our Moon", 1, LIL19), ("twin at 30,000 km", ratio, RED19))):
            y = 430 + i * 230; vv = val ** p if i else 1
            d.text((160, y), lab, font=F(40, "Bold"), fill=WHITE, anchor="lm")
            d.rounded_rectangle([x0, y + 40, max(x0 + 10, lx(vv)), y + 120], 16, fill=c)
            d.text((max(x0 + 10, lx(vv)) + 24, y + 80), f"{vv:,.0f}×", font=F(64, "Black"), fill=c, anchor="lm")
        for k2, lab in ((1, "1"), (10, "10"), (100, "100"), (1000, "1,000")):
            x = lx(k2); d.line([(x, 900), (x, 920)], fill=DIM, width=2); d.text((x, 950), lab, font=F(26, "SemiBold"), fill=DIM, anchor="mm")
        d.line([(x0, 910), (x1, 910)], fill=DIM, width=2)
        d.text((x1, 1000), "tidal pull, log scale · grows with 1 / distance³", font=F(28, "SemiBold"), fill=DIM, anchor="rm")
        return
    x0, x1, y0, y1 = 200, 1500, 300, 860; ym = (y0 + y1) / 2; hrs = 72
    lead = math.radians(2 * v.get("lead", 0)); p2 = v.get("period2", 12.42)
    w1 = 2 * math.pi / 12.42; w2 = 2 * math.pi / p2
    amp = 1 + ratio; sc = (y1 - y0) / 2 / amp * 0.92
    reveal = easeio((t - 0.3) / max(1.0, dur * 0.7))
    d.line([(x0, ym), (x1, ym)], fill=(60, 60, 90), width=2)
    for hh in range(0, hrs + 1, 12):
        x = lerp(x0, x1, hh / hrs); d.line([(x, y1 + 10), (x, y1 + 26)], fill=DIM, width=2)
        d.text((x, y1 + 50), f"{hh} h", font=F(24, "SemiBold"), fill=DIM, anchor="mm")
    def curve(fn, col, wdt, dash=False):
        pts = []
        for i in range(0, 601):
            h = hrs * i / 600
            if h > hrs * reveal: break
            pts.append((lerp(x0, x1, h / hrs), ym - fn(h) * sc))
        if len(pts) < 2: return
        if dash:
            for j in range(0, len(pts) - 1, 6): d.line(pts[j:j + 4], fill=col, width=wdt)
        else: d.line(pts, fill=col, width=wdt, joint="curve")
    f1 = lambda h: math.cos(w1 * h); f2 = lambda h: ratio * math.cos(w2 * h - lead)
    curve(f2, AMB19, 3); curve(lambda h: f1(h) + f2(h), AQUA19, 7); curve(f1, LIL19, 4, dash=True)
    leg = [("our Moon alone", LIL19), ("the twin alone", AMB19), ("both together", AQUA19)]
    for i, (lab, c) in enumerate(leg):
        y = 360 + i * 70; d.line([(1560, y), (1620, y)], fill=c, width=6); d.text((1640, y), lab, font=F(30, "Bold"), fill=WHITE, anchor="lm")
    h = hrs * reveal; tot = f1(h) + f2(h)
    if reveal > 0.02:
        x = lerp(x0, x1, h / hrs); d.ellipse([x - 12, ym - tot * sc - 12, x + 12, ym - tot * sc + 12], fill=WHITE)
    d.text((1560, 640), "highest tide", font=F(30, "Bold"), fill=DIM, anchor="lm")
    d.text((1560, 700), f"up to {amp:,.0f}×" if ratio != 1 else "1.0× today", font=F(56, "Black"), fill=AQUA19, anchor="lm")
    d.text((x1, y0 - 40), "equilibrium tide, Sun ignored · our calculation", font=F(24, "SemiBold"), fill=DIM, anchor="rm")

def sc_trojan(img, v, t, dur):
    """Earth, the Moon and a twin at L4 (60° ahead): triangle | wobble (tadpole libration + Routh box) | companion (≈ 1,200 km, drifts in)"""
    mode = v.get("mode", "triangle"); cx, cy, R = 700, 570, 360
    d = ImageDraw.Draw(img)
    rr = R * (1 + (0.06 * easeio((t - 0.5) / max(1, dur - 1.5)) if mode == "companion" else 0))
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(70, 70, 110), width=2)
    am = math.radians(10) - t * 0.02
    lib = math.radians(12) * math.sin(t * 1.4) if mode == "wobble" else 0
    if mode == "companion": lib = -math.radians(40) * easeio((t - 1.0) / max(1, dur - 1.5)) ** 2 + math.radians(4) * math.sin(t * 2)
    a4 = am - math.radians(60) + lib
    mx, my = cx + rr * math.cos(am), cy + rr * math.sin(am); tx, ty = cx + rr * math.cos(a4), cy + rr * math.sin(a4)
    a5 = am + math.radians(60); l5 = (cx + rr * math.cos(a5), cy + rr * math.sin(a5)); l4 = (cx + rr * math.cos(am - math.radians(60)), cy + rr * math.sin(am - math.radians(60)))
    if mode != "companion" or t < dur * 0.5:
        ta = ease((t - 0.3) / 0.6)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.line([(cx, cy), (mx, my), l4, (cx, cy)], fill=LIL19 + (int(160 * ta),), width=3)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        for (px, py, lab) in ((l4[0], l4[1], "L4"), (l5[0], l5[1], "L5")):
            d.line([(px - 14, py - 14), (px + 14, py + 14)], fill=AQUA19, width=3); d.line([(px - 14, py + 14), (px + 14, py - 14)], fill=AQUA19, width=3)
            d.text((px + (40 if px > cx else -40), py - 30), lab, font=F(34, "Black"), fill=AQUA19, anchor="mm")
        if mode == "triangle":
            for (px, py) in ((cx, cy), (mx, my), l4):
                d.text(((px * 2 + cx + mx + l4[0] - px) / 3 * 0 + lerp(px, (cx + mx + l4[0]) / 3, 0.28), lerp(py, (cy + my + l4[1]) / 3, 0.28)), "60°", font=F(28, "Bold"), fill=WHITE, anchor="mm")
    if mode == "wobble":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        base = am - math.radians(60)
        dl.arc([cx - rr, cy - rr, cx + rr, cy + rr], math.degrees(base - math.radians(13)), math.degrees(base + math.radians(13)), fill=AMB19 + (200,), width=14)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
    paste_c(img, earth_sprite(70, light=(-1, -0.2)), cx, cy)
    paste_c(img, moon19(30), mx, my)
    tr = 30 if mode != "companion" else 11
    paste_c(img, radial(tr * 5, [(0, AMB19 + (110,)), (1, AMB19 + (0,))]), tx, ty)
    paste_c(img, moon19(tr), tx, ty)
    d = ImageDraw.Draw(img)
    d.text((cx, cy + 110), "Earth", font=F(30, "Bold"), fill=WHITE, anchor="mm")
    d.text((mx - 40, my + 60), "our Moon", font=F(30, "Bold"), fill=LIL19, anchor="rm")
    d.text((tx - (60 if mode != "companion" else 0), ty - tr - 34), "the twin" if mode != "companion" else "companion", font=F(30, "Bold"), fill=AMB19, anchor="mm")
    ax = 1240
    if mode == "triangle":
        _box19(img, ax, 300, 1840, 760, LIL19); d = ImageDraw.Draw(img)
        d.text((ax + 40, 360), "SPOT 4 · L4", font=F(50, "ExtraBold"), fill=WHITE, anchor="lm")
        for i, s in enumerate(["same orbit as the Moon", "60° ahead of it", "384,400 km from Earth", "a perfect triangle"]):
            d.text((ax + 40, 450 + i * 70), s, font=F(36, "SemiBold"), fill=mix(SPACE, WHITE, ease((t - 0.6 - i * 0.4) / 0.4)), anchor="lm")
    elif mode == "wobble":
        _box19(img, ax, 280, 1840, 820, AQUA19); d = ImageDraw.Draw(img)
        d.text((ax + 40, 340), "Routh's test (1875)", font=F(44, "ExtraBold"), fill=WHITE, anchor="lm")
        d.text((ax + 40, 410), "masses: Earth 1 · Moon 0.0123 · twin 0.0123", font=F(26, "SemiBold"), fill=DIM, anchor="lm")
        rows = [("27 × (m₁m₂ + m₂m₃ + m₃m₁)", "0.67"), ("(m₁ + m₂ + m₃)²", "1.05")]
        for i, (l, r_) in enumerate(rows):
            aa = ease((t - 0.8 - i * 0.8) / 0.5)
            d.text((ax + 40, 490 + i * 90), l, font=F(27, "Bold"), fill=mix(SPACE, WHITE, aa), anchor="lm")
            d.text((ax + 560, 490 + i * 90), r_, font=F(44, "Black"), fill=mix(SPACE, AMB19, aa), anchor="rm")
        aa = ease((t - 2.6) / 0.5)
        d.text((ax + 40, 700), "0.67 < 1.05 -> STABLE", font=F(46, "Black"), fill=mix(SPACE, AQUA19, aa), anchor="lm")
        d.text((ax + 40, 770), "the twin rocks around L4", font=F(28, "SemiBold"), fill=mix(SPACE, DIM, aa), anchor="lm")
    else:
        _box19(img, ax, 300, 1840, 760, AMB19); d = ImageDraw.Draw(img)
        d.text((ax + 40, 360), "The lost companion?", font=F(46, "ExtraBold"), fill=WHITE, anchor="lm")
        for i, s in enumerate(["≈ 1,200 km wide", "about 1/3 of the Moon's width", "parked at a Trojan point", "Jutzi & Asphaug, Nature 2011"]):
            d.text((ax + 40, 450 + i * 70), s, font=F(34, "SemiBold"), fill=mix(SPACE, AMB19 if i == 0 else WHITE, ease((t - 0.6 - i * 0.4) / 0.4)), anchor="lm")
        d.text((cx, cy + rr + 50 if cy + rr + 50 < H - 30 else H - 40), "the Moon drifts outward…", font=F(28, "SemiBold"), fill=DIM, anchor="mm") if t > dur * 0.4 else None

def sc_splat(img, v, t, dur):
    """mode shred = twin inside the Roche limit breaks into a ring | splat = slow companion pancakes onto the Moon | farside = near vs far side"""
    mode = v.get("mode", "shred"); d = ImageDraw.Draw(img)
    if mode == "shred":
        cx, cy, er = 560, 560, 140; k = er / 6371.0; rro = 18400 * k; ro = 15000 * k
        for a0 in range(0, 360, 8): d.arc([cx - rro, cy - rro, cx + rro, cy + rro], a0, a0 + 4, fill=RED19, width=3)
        d.text((cx, cy - rro - 30), "Roche limit · 18,400 km", font=F(30, "Bold"), fill=RED19, anchor="mm")
        p = easeio((t - 0.6) / max(1.0, dur - 1.5)); rng = random.Random(19)
        ang0 = -0.4 + t * 0.35; mr = 1737 * k
        if p < 0.08:
            paste_c(img, moon19(int(mr)), cx + ro * math.cos(ang0), cy + ro * math.sin(ang0))
        n = 260
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for i in range(n if p >= 0.08 else 0):
            u = rng.random(); spread = (u - 0.5) * 2 * math.pi * p ** 1.2
            rad = ro + rng.gauss(0, 1) * (mr * 0.5 + 18 * p)
            a_ = ang0 + spread + rng.gauss(0, 0.04)
            x, y = cx + rad * math.cos(a_), cy + rad * math.sin(a_) * lerp(1, 0.32, p)
            s_ = rng.uniform(1.5, 5.5) * (1 - 0.4 * p)
            dl.ellipse([x - s_, y - s_, x + s_, y + s_], fill=(205, 200, 195, 230))
        img.alpha_composite(lay)
        paste_c(img, earth_sprite(er, light=(-1, -0.2)), cx, cy)
        d = ImageDraw.Draw(img)
        _box19(img, 1180, 330, 1840, 760, RED19); d = ImageDraw.Draw(img)
        d.text((1220, 390), "SPOT 1 · 15,000 km", font=F(46, "ExtraBold"), fill=WHITE, anchor="lm")
        for i, s in enumerate(["near side pulled harder", "than the far side", "the twin is torn apart", "-> a ring around Earth"]):
            d.text((1220, 480 + i * 64), s, font=F(34, "SemiBold"), fill=mix(SPACE, RED19 if i == 2 else WHITE, ease((t - 0.5 - i * 0.6) / 0.4)), anchor="lm")
        d.text((cx, H - 70), "Earth, Moon and orbit drawn to scale", font=F(26, "SemiBold"), fill=DIM, anchor="mm")
    elif mode == "splat":
        mx, my, mr = 1150, 560, 300; cr = mr * 0.345
        p = easeio((t - 0.3) / max(1.0, dur * 0.55)); q = easeio((t - 0.3 - dur * 0.55) / max(0.8, dur * 0.35))
        paste_c(img, moon19(mr), mx, my)
        d = ImageDraw.Draw(img)
        if q <= 0:
            x = lerp(200, mx - mr - cr * 0.7, p)
            paste_c(img, radial(int(cr * 4), [(0, AMB19 + (90,)), (1, AMB19 + (0,))]), x, my)
            paste_c(img, moon19(int(cr)), x, my)
            d = ImageDraw.Draw(img)
            for k2 in range(5): d.line([(x - cr - 30 - k2 * 40, my - 40 + k2 * 20), (x - cr - 80 - k2 * 40, my - 40 + k2 * 20)], fill=AMB19, width=3)
        else:
            span = lerp(18, 62, q); thick = lerp(cr * 0.9, mr * 0.13, q)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            pts_o, pts_i = [], []
            for i in range(41):
                a_ = math.radians(180 - span + 2 * span * i / 40); bump = thick * (1 - ((i - 20) / 20) ** 2) ** 0.7
                pts_o.append((mx + (mr + bump) * math.cos(a_), my + (mr + bump) * math.sin(a_)))
                pts_i.append((mx + (mr - 4) * math.cos(a_), my + (mr - 4) * math.sin(a_)))
            dl.polygon(pts_o + pts_i[::-1], fill=(214, 196, 168, 255))
            dl.line(pts_o, fill=AMB19 + (255,), width=4)
            img.alpha_composite(lay); d = ImageDraw.Draw(img)
            d.text((mx - mr - 120, my + mr * 0.75), "a pile, not a crater", font=F(34, "Bold"), fill=AMB19, anchor="mm")
        _box19(img, 80, 820, 760, 1000, AMB19); d = ImageDraw.Draw(img)
        d.text((120, 870), "impact speed", font=F(32, "Bold"), fill=DIM, anchor="lm")
        d.text((120, 945), "2–3 km/s", font=F(66, "Black"), fill=AMB19, anchor="lm")
        d.text((470, 945), "(slow, for space)", font=F(30, "SemiBold"), fill=WHITE, anchor="lm")
        d.text((W - 60, H - 50), "illustration · after Jutzi & Asphaug 2011", font=F(24, "SemiBold"), fill=DIM, anchor="rm")
    else:
        for i, (x, far, lab, sub) in enumerate(((560, False, "NEAR SIDE", "dark lava plains"), (1360, True, "FAR SIDE", "thick, bright highlands"))):
            a = ease((t - 0.2 - i * 0.9) / 0.6)
            if a <= 0: continue
            paste_c(img, moon19(270, far=far), x, 540, a)
            d = ImageDraw.Draw(img)
            d.text((x, 160), lab, font=F(52, "ExtraBold"), fill=mix(SPACE, WHITE, a), anchor="mm")
            d.text((x, 900), sub, font=F(36, "SemiBold"), fill=mix(SPACE, AMB19 if far else LIL19, a), anchor="mm")
        a = ease((t - 2.5) / 0.6)
        if a > 0:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            dl.arc([1360 - 300, 240, 1360 + 300, 840], 200, 340, fill=AMB19 + (int(220 * a),), width=10)
            img.alpha_composite(lay); d = ImageDraw.Draw(img)
            d.text((1360, 990), "the scar of a second moon?", font=F(36, "Bold"), fill=mix(SPACE, AMB19, a), anchor="mm")
        d.text((W - 60, H - 40), "code-drawn illustration", font=F(22, "SemiBold"), fill=DIM, anchor="rm")

_traj19 = {}
def _hill19(r0, days=200, dt=1800.0):
    if r0 in _traj19: return _traj19[r0]
    def f(s):
        x, y, vx, vy = s; r3 = (x * x + y * y) ** 1.5
        return (vx, vy, 2 * OM19 * vy + 3 * OM19 * OM19 * x - GM19 * x / r3, -2 * OM19 * vx - GM19 * y / r3)
    s = (r0, 0.0, 0.0, math.sqrt(GM19 / r0) - OM19 * r0); out = [(0.0, r0, 0.0)]; tt = 0.0
    while tt < days * 86400:
        k1 = f(s); k2 = f(tuple(s[i] + dt / 2 * k1[i] for i in range(4))); k3 = f(tuple(s[i] + dt / 2 * k2[i] for i in range(4))); k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
        s = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)); tt += dt
        out.append((tt / 86400, s[0], s[1]))
        if math.hypot(s[0], s[1]) > 3.4e6: break
    _traj19[r0] = out
    return out

def sc_sunsteal(img, v, t, dur):
    """Hill-problem simulation (Earth + Sun, frame turning with Earth): a twin started on a circular orbit at 1,000,000 km escapes;
    phase 0 = days 0–75, phase 1 = 75 -> exit; Hill sphere, 0.49 R_H stability edge, Moon orbit"""
    cx, cy = 900, 560; k = 330 / 1.5e6; d = ImageDraw.Draw(img)
    for a0 in range(0, 360, 6): d.arc([cx - 330, cy - 330, cx + 330, cy + 330], a0, a0 + 3, fill=(170, 170, 195), width=2)
    rs = 732000 * k
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([cx - rs, cy - rs, cx + rs, cy + rs], fill=AQUA19 + (28,), outline=AQUA19 + (160,), width=3); img.alpha_composite(lay)
    d = ImageDraw.Draw(img); rm = 384400 * k
    d.ellipse([cx - rm, cy - rm, cx + rm, cy + rm], outline=(90, 90, 130), width=2)
    paste_c(img, earth_sprite(14, light=(-1, 0)), cx, cy)
    d = ImageDraw.Draw(img)
    d.text((cx, cy - 330 - 28), "edge of Earth's pull · 1.5 million km", font=F(26, "Bold"), fill=(190, 190, 210), anchor="mm")
    d.text((cx, cy - rs + 30), "safe zone ≈ 730,000 km", font=F(24, "Bold"), fill=AQUA19, anchor="mm")
    d.text((cx + rm * 0.72, cy + rm * 0.72 + 20), "Moon's orbit", font=F(22, "SemiBold"), fill=DIM, anchor="lm")
    for k2 in range(3):
        ax = 140 + k2 * 36 - (t * 30) % 36
        d.polygon([(ax - 18, 560), (ax + 6, 546), (ax + 6, 574)], fill=AMB19)
    d.text((150, 510), "to the Sun", font=F(30, "Bold"), fill=AMB19, anchor="lm")
    d.text((150, 610), "150 million km", font=F(24, "SemiBold"), fill=DIM, anchor="lm")
    tr = _hill19(1.0e6); dend = tr[-1][0]
    ph = v.get("phase", 0); d0, d1 = (0, 75) if ph == 0 else (75, dend)
    day = lerp(d0, d1, easeio((t - 0.3) / max(1.0, dur * 0.8)))
    pts = [(cx + x * k, cy - y * k) for (dd, x, y) in tr if dd <= day]
    if len(pts) > 1:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        n = len(pts)
        for i in range(0, n - 1, 2): dl.line([pts[i], pts[min(n - 1, i + 2)]], fill=AMB19 + (int(60 + 195 * i / n),), width=4)
        img.alpha_composite(lay)
    hx, hy = pts[-1]
    paste_c(img, radial(60, [(0, AMB19 + (160,)), (1, AMB19 + (0,))]), hx, hy); paste_c(img, moon19(8), hx, hy)
    d = ImageDraw.Draw(img)
    rnow = math.hypot(*[c for c in [tr[min(len(tr) - 1, len(pts) - 1)][1], tr[min(len(tr) - 1, len(pts) - 1)][2]]])
    _box19(img, 1380, 300, 1860, 640, AMB19); d = ImageDraw.Draw(img)
    d.text((1420, 350), "DAY", font=F(30, "Bold"), fill=DIM, anchor="lm"); d.text((1420, 410), f"{day:,.0f}", font=F(70, "Black"), fill=WHITE, anchor="lm")
    d.text((1420, 490), "DISTANCE", font=F(30, "Bold"), fill=DIM, anchor="lm"); d.text((1420, 550), f"{rnow / 1e6:.2f} million km", font=F(48, "Black"), fill=AMB19, anchor="lm")
    if ph == 1 and day > dend * 0.9: _stamp19(img, "STOLEN BY THE SUN", RED19, 1450, 830, (t - dur * 0.75) / 0.6)
    d.text((W - 60, H - 40), "our simulation: Earth + Sun, frame turning with Earth", font=F(22, "SemiBold"), fill=DIM, anchor="rm")

def _rock19(d, x, y, s, col, seed):
    rng = random.Random(seed); pts = []
    for i in range(12):
        a_ = 2 * math.pi * i / 12; rr = s * rng.uniform(0.75, 1.1); pts.append((x + rr * math.cos(a_), y + rr * 0.8 * math.sin(a_)))
    d.polygon(pts, fill=col)

def sc_tangle(img, v, t, dur):
    """real tiny second moons: phase 0 = 2006 RH120 tangled loops | 1 = size lineup (person, 1.2 m, 3 m, 10 m, bus) | 2 = Kamo'oalewa's
    quasi-satellite loop in a frame turning with Earth"""
    ph = v.get("phase", 0); d = ImageDraw.Draw(img)
    if ph in (0, 1):
        cx, cy = 620 if ph == 0 else 960, 520 if ph == 0 else 400; S = 300 if ph == 0 else 220
        paste_c(img, earth_sprite(36 if ph == 0 else 26, light=(-1, -0.2)), cx, cy)
        d = ImageDraw.Draw(img)
        u = easeio((t - 0.2) / max(1.0, dur * 0.85)); pts = []
        for i in range(int(900 * u) + 2):
            s_ = i / 900 * 26
            r_ = S * (0.45 + 0.4 * math.sin(0.61 * s_ + 0.5) ** 2 + 0.1 * math.sin(2.3 * s_))
            a_ = s_ + 0.9 * math.sin(0.33 * s_)
            pts.append((cx + r_ * math.cos(a_), cy + r_ * 0.8 * math.sin(a_)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for i in range(0, len(pts) - 1, 2): dl.line([pts[i], pts[min(len(pts) - 1, i + 2)]], fill=AQUA19 + (int(50 + 180 * i / len(pts)),), width=3)
        img.alpha_composite(lay)
        if len(pts) > 1: paste_c(img, radial(40, [(0, AQUA19 + (200,)), (1, AQUA19 + (0,))]), *pts[-1])
        d = ImageDraw.Draw(img)
        if ph == 0:
            _box19(img, 1180, 300, 1840, 760, AQUA19); d = ImageDraw.Draw(img)
            d.text((1220, 360), "2006 RH120", font=F(52, "ExtraBold"), fill=WHITE, anchor="lm")
            for i, s in enumerate(["≈ 3 m wide", "caught mid-2006", "looped Earth ≈ 1 year", "then escaped"]):
                d.text((1220, 450 + i * 70), s, font=F(36, "SemiBold"), fill=mix(SPACE, AQUA19 if i == 0 else WHITE, ease((t - 0.5 - i * 0.6) / 0.4)), anchor="lm")
            d.text((cx, H - 60), "loops: illustration", font=F(24, "SemiBold"), fill=DIM, anchor="mm")
        else:
            base = 960; xs = [260, 560, 860, 1200, 1600]; sc_ = 26
            d.line([(140, base), (1800, base)], fill=(80, 80, 110), width=3)
            hp = 1.7 * sc_
            d.ellipse([xs[0] - 9, base - hp - 4, xs[0] + 9, base - hp + 14], fill=WHITE); d.line([(xs[0], base - hp + 14), (xs[0], base - hp * 0.45)], fill=WHITE, width=5)
            d.line([(xs[0], base - hp * 0.45), (xs[0] - 9, base)], fill=WHITE, width=5); d.line([(xs[0], base - hp * 0.45), (xs[0] + 9, base)], fill=WHITE, width=5)
            items = [(xs[1], 1.2, "2020 CD3 · ≈ 1.2 m"), (xs[2], 3, "2006 RH120 · ≈ 3 m"), (xs[3], 10, "2024 PT5 · ≈ 10 m")]
            for i, (x, m, lab) in enumerate(items):
                a = ease((t - 0.4 - i * 0.9) / 0.5)
                if a <= 0: continue
                s_ = m * sc_ / 2; _rock19(d, x, base - s_ * 0.8, s_, mix(SPACE, (170, 160, 150), a), i + 3)
                d.text((x, base + 40), lab, font=F(28, "Bold"), fill=mix(SPACE, AQUA19, a), anchor="mm")
            bx = xs[4]; bl = 12 * sc_
            d.rounded_rectangle([bx - bl / 2, base - 3.2 * sc_, bx + bl / 2, base - 10], 10, fill=(220, 180, 60))
            for k2 in range(6): d.rectangle([bx - bl / 2 + 20 + k2 * 48, base - 2.8 * sc_, bx - bl / 2 + 56 + k2 * 48, base - 1.9 * sc_], fill=(60, 80, 110))
            d.ellipse([bx - bl / 2 + 40, base - 30, bx - bl / 2 + 80, base + 10], fill=(30, 30, 40)); d.ellipse([bx + bl / 2 - 80, base - 30, bx + bl / 2 - 40, base + 10], fill=(30, 30, 40))
            d.text((xs[0], base + 40), "you · 1.7 m", font=F(28, "Bold"), fill=WHITE, anchor="mm"); d.text((bx, base + 40), "a bus · 12 m", font=F(28, "Bold"), fill=WHITE, anchor="mm")
            a = ease((t - 3.2) / 0.5)
            d.text((W / 2, 1045), "2024 PT5's colours match Moon rock (Kareta et al. 2025)", font=F(30, "SemiBold"), fill=mix(SPACE, LIL19, a), anchor="mm")
    else:
        cx, cy = 820, 560; d = ImageDraw.Draw(img)
        paste_c(img, earth_sprite(30, light=(-1, 0)), cx, cy); d = ImageDraw.Draw(img)
        u = (t * 0.45) % (2 * math.pi); ax_, by_ = 190, 380
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.ellipse([cx - ax_, cy - by_, cx + ax_, cy + by_], outline=AMB19 + (170,), width=4); img.alpha_composite(lay)
        kx, ky = cx + ax_ * math.cos(u), cy - by_ * math.sin(u)
        paste_c(img, radial(50, [(0, AMB19 + (200,)), (1, AMB19 + (0,))]), kx, ky)
        d = ImageDraw.Draw(img); _rock19(d, kx, ky, 9, (190, 170, 150), 7)
        d.text((kx + 30, ky), "Kamo'oalewa", font=F(28, "Bold"), fill=AMB19, anchor="lm")
        for k2 in range(3):
            ax = 140 + k2 * 36 - (t * 30) % 36
            d.polygon([(ax - 18, 560), (ax + 6, 546), (ax + 6, 574)], fill=AMB19)
        d.text((150, 510), "to the Sun", font=F(30, "Bold"), fill=AMB19, anchor="lm")
        _box19(img, 1200, 300, 1850, 780, AMB19); d = ImageDraw.Draw(img)
        d.text((1240, 360), "A QUASI-MOON", font=F(50, "ExtraBold"), fill=WHITE, anchor="lm")
        for i, s in enumerate(["orbits the Sun, not Earth", "but stays beside us", "seems to loop around Earth", "Tianwen-2 reached it in 2026"]):
            d.text((1240, 450 + i * 70), s, font=F(34, "SemiBold"), fill=mix(SPACE, AMB19 if i == 3 else WHITE, ease((t - 0.5 - i * 0.6) / 0.4)), anchor="lm")
        d.text((W - 60, H - 40), "frame turning with Earth · loop shape illustrative", font=F(22, "SemiBold"), fill=DIM, anchor="rm")



# ---------------- EP20 scenes: signpost, tabletop, fieldmap, snailrace, fitinside ----------------
SAND20, TRAIL20, DUSK20, WOOD20, ICE20 = (240, 210, 150), (130, 215, 150), (175, 145, 255), (128, 84, 48), (150, 210, 235)
STOPS20 = [("THE DESK", "18.6 m", 0.0186), ("OORT CLOUD", "10.75 km", 10.75), ("PROXIMA", "28.9 km", 28.9),
           ("MILKY WAY", "680,000 km", 6.8e5), ("THE EDGE", "316 billion km", 3.16e11)]

def _fmt_km20(km):
    if km < 1: return f"{km * 1000:,.1f} m"
    if km < 100: return f"{km:,.2f} km"
    if km < 1e9: return f"{km:,.0f} km"
    return f"{km / 1e9:,.0f} billion km"

def _fmt_walk20(km):
    h = km / 5.0
    if h < 1 / 60: return f"{h * 3600:.0f} s"
    if h < 1: return f"{h * 60:.0f} min"
    if h < 48: return f"{int(h)} h {int((h % 1) * 60):02d} min"
    y = h / 8766
    if y < 1: return f"{h / 24:,.0f} days"
    if y < 1e6: return f"{y:,.1f} years"
    return f"{y / 1e6:,.1f} million years"

def _grain20(img, x, y, r=7, a=1.0):
    paste_c(img, radial(int(r * 9) + 4, [(0, (255, 240, 200, int(230 * a))), (0.25, (255, 210, 140, int(110 * a))), (1, (255, 190, 110, 0))]), x, y)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([x - r, y - r * 0.85, x + r, y + r * 0.85], fill=SAND20 + (int(255 * a),)); img.alpha_composite(lay)

def _walker20(d, x, y, s, t, col):
    sw = math.sin(t * 6) * 0.5
    d.ellipse([x - 6 * s, y - 62 * s, x + 6 * s, y - 50 * s], fill=col)
    d.line([(x, y - 50 * s), (x, y - 24 * s)], fill=col, width=max(2, int(4 * s)))
    for k in (-1, 1):
        d.line([(x, y - 24 * s), (x + k * sw * 14 * s, y)], fill=col, width=max(2, int(4 * s)))
        d.line([(x, y - 44 * s), (x - k * sw * 12 * s, y - 30 * s)], fill=col, width=max(2, int(3 * s)))
    d.rectangle([x - 12 * s, y - 48 * s, x - 3 * s, y - 32 * s], fill=col)  # backpack

def sc_signpost(img, v, t, dur):
    """chapter card: a wooden trail post (left) with one plank per stop and its distance AT THE GRAIN-OF-SAND SCALE; v.n = active stop
    (passed stops dim with a tick), odometer counts (log) from the previous stop to v.km, walking time at 5 km/h; dusk hills + walker"""
    a = ease(t / 0.5); n = v.get("n", 0); km = v.get("km", 0)
    # dusk band + hills
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for i in range(60):
        y = 760 + i * 5; dl.rectangle([0, y, W, y + 5], fill=mix((60, 40, 90), (16, 12, 30), i / 60) + (int(160 * a),))
    pts = [(x, 900 - 50 * math.sin(x / 260.0) - 30 * math.sin(x / 97.0 + 1)) for x in range(0, W + 20, 20)]
    dl.polygon(pts + [(W, H), (0, H)], fill=(14, 18, 24, 255))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    wx = (W * 0.62 + t * 40) % W; wy = 900 - 50 * math.sin(wx / 260.0) - 30 * math.sin(wx / 97.0 + 1)
    _walker20(d, wx, wy, 1.0, t, (40, 46, 58))
    # post
    px = 380; d.rectangle([px - 18, 150, px + 18, 960], fill=WOOD20); d.rectangle([px - 18, 150, px - 8, 960], fill=(100, 64, 36))
    _grain20(img, px + 70, 950, 6, a); d = ImageDraw.Draw(img)
    for i, (name, dist, k) in enumerate(STOPS20):
        aa = ease((t - 0.15 - i * 0.12) / 0.4)
        if aa <= 0: continue
        y = 210 + i * 140; right = (i % 2 == 0); x0 = px - 40 if right else px - 300; x1 = px + 300 if right else px + 40
        act = (i + 1 == n); done = (i + 1 < n)
        base = (176, 120, 70) if not done else (92, 70, 52)
        if act: base = mix(base, SAND20, 0.55 + 0.15 * math.sin(t * 4))
        tip = [(x1, y), (x1 + 40, y + 45), (x1, y + 90)] if right else [(x0, y), (x0 - 40, y + 45), (x0, y + 90)]
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([x0, y, x1, y + 90], fill=base + (int(255 * aa),)); dl.polygon(tip, fill=base + (int(255 * aa),))
        for g in range(3): dl.line([(x0 + 8, y + 22 + g * 24), (x1 - 8, y + 24 + g * 24)], fill=(0, 0, 0, int(28 * aa)), width=2)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        tc = (40, 24, 12) if not done else (170, 150, 130)
        cx_ = (x0 + x1) / 2 + (10 if right else -10)
        d.text((cx_, y + 30), name, font=F(34, "Black"), fill=tc, anchor="mm")
        d.text((cx_, y + 66), dist, font=F(26, "Bold"), fill=tc, anchor="mm")
        if done: d.line([(x0 + 14, y + 48), (x0 + 30, y + 66), (x0 + 58, y + 26)], fill=TRAIL20, width=6)
    # right column
    alpha_text(img, (820, 210), v.get("title", ""), F(70, "ExtraBold"), WHITE, a, anchor="lm")
    if v.get("sub"): alpha_text(img, (820, 290), v["sub"], F(36, "SemiBold"), SAND20, ease((t - 0.3) / 0.5), anchor="lm")
    prev = 0.0
    for (_, _, k) in STOPS20:
        if k < km * 0.999: prev = k
    if prev == 0: prev = km * 0.01 if km > 0 else 0
    if "km0" in v: prev = v["km0"]
    q = easeio((t - 0.5) / max(0.8, dur * 0.5))
    cur = 0 if km <= 0 else math.exp(lerp(math.log(max(prev, 1e-6)), math.log(km), q))
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([820, 400, 1780, 700], 26, fill=(10, 14, 24, int(225 * a)), outline=TRAIL20 + (int(160 * a),), width=3)
    dl.line([(1300, 430), (1300, 670)], fill=(60, 70, 90, int(255 * a)), width=2)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.text((1060, 450), "ODOMETER", font=F(28, "Bold"), fill=mix(SPACE, DIM, a), anchor="mm")
    d.text((1540, 450), "ON FOOT, NONSTOP", font=F(28, "Bold"), fill=mix(SPACE, DIM, a), anchor="mm")
    s1 = _fmt_km20(cur) if km > 0 else "0 m"; s2 = _fmt_walk20(cur) if km > 0 else "0 s"
    d.text((1060, 560), s1, font=F(64 if len(s1) < 12 else 46, "Black"), fill=mix(SPACE, TRAIL20, a), anchor="mm")
    d.text((1540, 560), s2, font=F(64 if len(s2) < 12 else 46, "Black"), fill=mix(SPACE, SAND20, a), anchor="mm")
    d.text((1060, 640), "at grain-of-sand scale", font=F(24, "SemiBold"), fill=mix(SPACE, DIM, a), anchor="mm")
    d.text((1540, 640), "at 5 km/h", font=F(24, "SemiBold"), fill=mix(SPACE, DIM, a), anchor="mm")
    d.text((W - 60, H - 40), "the Sun = a 1 mm grain · 1 mm = 1,391,400 km", font=F(24, "SemiBold"), fill=DIM, anchor="rm")

_wood20 = None
def _woodtex20():
    global _wood20
    if _wood20 is None:
        rng = np.random.default_rng(20); yy = np.arange(H)[:, None].astype(np.float32); xx = np.arange(W)[None, :].astype(np.float32)
        g = np.sin(yy / 9.0 + 2.5 * np.sin(xx / 300.0) + 1.2 * np.sin(xx / 77.0 + yy / 140.0)) * 0.5 + 0.5
        n = rng.normal(0, 1, (H // 4 + 1, W // 4 + 1)).astype(np.float32); n = np.kron(n, np.ones((4, 4), np.float32))[:H, :W]
        v = 0.55 + 0.25 * g + 0.04 * n
        base = np.array([96, 62, 36], np.float32); hi = np.array([150, 104, 64], np.float32)
        arr = base[None, None, :] + (hi - base)[None, None, :] * np.clip(v, 0, 1)[..., None] - 30
        _wood20 = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB").convert("RGBA")
    return _wood20

def _lens20(img, cx, cy, r, draw_fn, ring=SAND20):
    """circular magnifier: draw_fn(layer, cx, cy, r) paints inside; clipped to the circle"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([cx - r, cy - r, cx + r, cy + r], fill=(10, 10, 16, 255))
    draw_fn(lay, cx, cy, r)
    mask = Image.new("L", img.size, 0); ImageDraw.Draw(mask).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    al = Image.fromarray(np.minimum(np.array(lay.getchannel("A")), np.array(mask))); lay.putalpha(al)
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    d.ellipse([cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8], outline=(30, 30, 36), width=14); d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], outline=ring, width=4)

def sc_tabletop(img, v, t, dur):
    """macro desk from above, TO SCALE with the 1 mm Sun. mode earth = grain + Earth speck 10.75 cm away on a cm ruler, magnifier shows the
    9 µm Earth beside a 80 µm hair, dashed orbit arc (a dinner plate) | moon = microscope strip, Earth + Moon 276 µm apart (5 px/µm) |
    jupiter = the room: a desk with the grain, Jupiter 56 cm, Saturn 1.03 m, Neptune 3.23 m on the floor"""
    mode = v.get("mode", "earth"); a = ease(t / 0.5); d = ImageDraw.Draw(img)
    if mode in ("earth", "moon"):
        img.alpha_composite(_woodtex20()); d = ImageDraw.Draw(img)
    if mode == "earth":
        ppc = 120.0; gx, gy = 230, 620; ex = gx + 10.75 * ppc
        # orbit arc (radius 10.75 cm) — the whole orbit = a 21.5 cm plate
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); R_ = 10.75 * ppc
        for k in range(0, 360, 3):
            if k % 6: continue
            a0 = math.radians(k); a1 = math.radians(k + 3)
            dl.line([(gx + R_ * math.cos(a0), gy + R_ * math.sin(a0)), (gx + R_ * math.cos(a1), gy + R_ * math.sin(a1))], fill=(255, 240, 210, int(120 * ease((t - 1.2) / 0.6))), width=3)
        img.alpha_composite(lay)
        # ruler
        d = ImageDraw.Draw(img); d.rectangle([gx - 40, 860, gx + 12 * ppc + 40, 960], fill=(232, 222, 190), outline=(90, 80, 60), width=2)
        for mm_ in range(0, 121):
            x = gx + mm_ * ppc / 10; L = 34 if mm_ % 10 == 0 else (22 if mm_ % 5 == 0 else 12)
            d.line([(x, 860), (x, 860 + L)], fill=(40, 34, 26), width=2)
            if mm_ % 10 == 0: d.text((x, 920), f"{mm_ // 10}", font=F(26, "Bold"), fill=(40, 34, 26), anchor="mm")
        d.text((gx + 12 * ppc + 20, 940), "cm", font=F(22, "Bold"), fill=(40, 34, 26), anchor="rm")
        _grain20(img, gx, gy, 6); d = ImageDraw.Draw(img)
        d.text((gx, gy - 60), "THE SUN", font=F(34, "Black"), fill=SAND20, anchor="mm"); d.text((gx, gy - 26), "1 mm", font=F(26, "Bold"), fill=WHITE, anchor="mm")
        q = easeio((t - 0.4) / 1.2)
        d.line([(gx + 14, gy), (gx + 14 + (ex - gx - 28) * q, gy)], fill=(255, 255, 255), width=2)
        if q > 0.98:
            d.ellipse([ex - 2, gy - 2, ex + 2, gy + 2], fill=(140, 190, 255))
            d.text((ex, gy + 40), "EARTH · 10.75 cm", font=F(30, "Black"), fill=(160, 205, 255), anchor="mm")
        la = ease((t - 1.6) / 0.6)
        if la > 0:
            def inside(lay, cx, cy, r):
                dl = ImageDraw.Draw(lay)
                dl.rectangle([cx - r, cy - 40, cx + r, cy + 40], fill=(70, 50, 30, 255))  # the hair, ~80 µm at 1 px/µm × 1.0
                lay.alpha_composite(earth_sprite(5, light=(-1, -0.2), glow=None), (int(cx - 9), int(cy - 150)))
                dl.text((cx, cy - 190), "Earth · 9 µm", font=F(28, "Bold"), fill=(170, 210, 255, 255), anchor="mm")
                dl.text((cx, cy), "a human hair · ~80 µm", font=F(26, "Bold"), fill=(235, 220, 200, 255), anchor="mm")
                dl.line([(cx - 60, cy + 200), (cx + 40, cy + 200)], fill=(255, 255, 255, 255), width=4)
                dl.text((cx - 10, cy + 230), "100 µm", font=F(22, "Bold"), fill=(255, 255, 255, 255), anchor="mm")
            lx, ly_ = ex - 80, 330; r = int(250 * la)
            if r > 20:
                d.line([(ex, gy - 4), (lx, ly_ + r)], fill=(30, 30, 36), width=6)
                _lens20(img, lx, ly_, r, inside)
        alpha_text(img, (80, 120), "Earth's whole orbit = a dinner plate (21.5 cm)", F(36, "Bold"), (255, 240, 210), ease((t - 1.4) / 0.5), anchor="lm")
    elif mode == "moon":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rounded_rectangle([90, 250, W - 90, 800], 40, fill=(6, 8, 14, 245), outline=(200, 200, 210, 255), width=6); img.alpha_composite(lay)
        ppu = 5.0; ex, ey = 250, 525; mx = ex + 276.3 * ppu
        paste_c(img, earth_sprite(23, light=(-1, -0.2)), ex, ey); paste_c(img, moon8(6), mx, ey + 10 * math.sin(t))
        d = ImageDraw.Draw(img)
        q = easeio((t - 0.5) / 1.0)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([ex, ey - 120, ex + (mx - ex + 40) * q, ey + 120], fill=TRAIL20 + (int(40 * ease((t - 1.6) / 0.6)),))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.line([(ex + 30, ey + 60), (ex + 30 + (mx - ex - 40) * q, ey + 60)], fill=WHITE, width=3)
        d.text((ex, ey - 70), "EARTH", font=F(30, "Black"), fill=(160, 205, 255), anchor="mm"); d.text((mx, ey - 50), "MOON", font=F(30, "Black"), fill=(220, 220, 235), anchor="mm")
        d.text(((ex + mx) / 2, ey + 100), "0.28 mm", font=F(44, "Black"), fill=WHITE, anchor="mm")
        alpha_text(img, (W / 2, 330), "every astronaut, ever, stayed inside this strip", F(40, "ExtraBold"), TRAIL20, ease((t - 1.8) / 0.5))
        d.line([(160, 760), (160 + 100 * ppu, 760)], fill=WHITE, width=4); d.text((160 + 50 * ppu, 735), "100 µm", font=F(24, "Bold"), fill=WHITE, anchor="mm")
        d.text((W - 140, 770), "MICROSCOPE VIEW", font=F(24, "Bold"), fill=DIM, anchor="rm")
    else:  # jupiter: the room
        ppc = 4.6; gx, gy = 220, 560
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for i in range(0, W, 92):
            for j in range(150, H, 92): dl.rectangle([i, j, i + 90, j + 90], fill=(44, 46, 54, int(255 * a)))
        dl.rectangle([gx - 120, gy - 170, gx + 150 * ppc - 120, gy - 170 + 75 * ppc], fill=(120, 80, 46, int(255 * a)), outline=(70, 46, 26, 255), width=4)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.text((gx - 100, gy - 140), "DESK", font=F(24, "Bold"), fill=(230, 200, 160), anchor="lm")
        _grain20(img, gx, gy, 5); d = ImageDraw.Draw(img)
        objs = [("JUPITER", 56, 0.10, (215, 175, 130), "56 cm"), ("SATURN", 103, 0.087, (225, 205, 150), "1.03 m"), ("NEPTUNE", 323, 0.036, (90, 120, 240), "3.23 m")]
        for i, (nm, cm, mmw, col, lab) in enumerate(objs):
            aa = ease((t - 0.6 - i * 0.9) / 0.5)
            if aa <= 0: continue
            x = gx + cm * ppc
            d.line([(gx + 10, gy + 60 + i * 26), (x, gy + 60 + i * 26)], fill=mix(SPACE, col, aa * 0.7), width=3)
            paste_c(img, radial(60, [(0, col + (int(200 * aa),)), (1, col + (0,))]), x, gy); d = ImageDraw.Draw(img)
            d.ellipse([x - 3, gy - 3, x + 3, gy + 3], fill=col)
            d.text((x, gy - 70 - (i % 2) * 50), nm, font=F(34, "Black"), fill=mix(SPACE, col, aa), anchor="mm")
            d.text((x, gy - 36 - (i % 2) * 50), f"{lab} · {mmw:.2f} mm wide", font=F(24, "Bold"), fill=mix(SPACE, WHITE, aa), anchor="mm")
        d.text((gx, gy + 40), "SUN", font=F(26, "Black"), fill=SAND20, anchor="mm")
        d.line([(80, 980), (80 + 100 * ppc, 980)], fill=WHITE, width=4); d.text((80 + 50 * ppc, 1010), "1 meter", font=F(24, "Bold"), fill=WHITE, anchor="mm")
        alpha_text(img, (W / 2, 110), "ONE ROOM: THE WHOLE PLANET FAMILY", F(46, "ExtraBold"), WHITE, a)

_town20 = None
def _town_pts20():
    global _town20
    if _town20 is None:
        rng = random.Random(20); segs = []
        for k in range(-30, 31):
            p0 = k * 200.0
            segs.append(((p0 + rng.uniform(-40, 40), -6000), (p0 + rng.uniform(-40, 40), 6000)))
            segs.append(((-6000, p0 + rng.uniform(-40, 40)), (6000, p0 + rng.uniform(-40, 40))))
        ice = [(math.exp(rng.uniform(math.log(215), math.log(10750))), rng.uniform(0, 2 * math.pi)) for _ in range(1400)]
        _town20 = (segs, ice)
    return _town20

_galw20 = {}
def _gal20(w):
    w = max(6, int(w))
    if w not in _galw20:
        if len(_galw20) > 60: _galw20.clear()
        g = galaxy_sprite(); _galw20[w] = g.resize((w, int(w * 0.62)), Image.LANCZOS)
    return _galw20[w]

def _scalebar20(img, ppm, unit_m=1.0, unit="m", x=80, y=1010):
    target = 280 / ppm; e = 10 ** math.floor(math.log10(target)); nice = max(k * e for k in (1, 2, 5) if k * e <= target)
    L = nice * ppm; d = ImageDraw.Draw(img)
    d.line([(x, y), (x + L, y)], fill=WHITE, width=4); d.line([(x, y - 10), (x, y + 10)], fill=WHITE, width=3); d.line([(x + L, y - 10), (x + L, y + 10)], fill=WHITE, width=3)
    val = nice / unit_m; s = (f"{val:,.0f}" if val >= 1 else f"{val:g}") + f" {unit}"
    d.text((x + L / 2, y - 26), s, font=F(24, "Bold"), fill=WHITE, anchor="mm")

def sc_fieldmap(img, v, t, dur):
    """top-down map AT THE GRAIN-OF-SAND SCALE with a log zoom from half-width v.z0 to v.z1 (metres). mode house (building around the grain,
    Neptune ring 3.23 m, Voyager 1 at 18.6 m) | oort (town streets + icy shell 215 m -> 10.75 km) | proxima (grain left, Proxima 28.9 km
    and Alpha Cen A/B 29.7 km right). Galaxy modes (km): galaxy (Earth + Moon orbit vs a 680,000 km Milky Way) | center (Sagittarius A*
    bead 17 mm, 184 km from the grain) | andromeda (two galaxies 25 widths apart + 44 Earth-Moon ticks) | collide (illustrative merger)"""
    mode = v.get("mode", "house"); a = ease(t / 0.5); q = easeio((t - 0.3) / max(1.0, dur * 0.75))
    if mode in ("house", "oort", "proxima"):
        z = math.exp(lerp(math.log(v["z0"]), math.log(v["z1"]), q))
        if mode == "proxima": ox, oy = 260, 560; ppm = (W - 520) / max(z, 1.0)
        else: ox, oy = W / 2, 580; ppm = 430 / z
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([0, 0, W, H], fill=(14, 22, 20, int(200 * a)))
        segs, ice = _town_pts20()
        sa = max(0.0, min(1.0, (ppm * 200 - 6) / 30.0)) * (1 if mode != "proxima" else 0.6)
        if sa > 0 and ppm * 6000 > 40:
            for (p0, p1) in segs:
                dl.line([(ox + p0[0] * ppm, oy + p0[1] * ppm), (ox + p1[0] * ppm, oy + p1[1] * ppm)], fill=(60, 80, 70, int(160 * sa * a)), width=2)
        # Oort shell specks
        if ppm * 10750 > 30:
            ia = ease((t - 0.2) / 0.8) if mode == "oort" else 1.0
            for (r_, th_) in ice:
                x = ox + r_ * ppm * math.cos(th_ + t * 0.01); y = oy + r_ * ppm * math.sin(th_ + t * 0.01)
                if -10 < x < W + 10 and -10 < y < H + 10: dl.ellipse([x - 2, y - 2, x + 2, y + 2], fill=ICE20 + (int(150 * ia * a),))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        # house footprint 12 x 9 m
        hw, hh = 6 * ppm, 4.5 * ppm
        if 8 < hw < 4000:
            d.rectangle([ox - hw, oy - hh, ox + hw, oy + hh], outline=(200, 190, 170), width=3)
            if hw > 60: d.text((ox - hw + 12, oy - hh + 24), "THE BUILDING", font=F(24, "Bold"), fill=(200, 190, 170), anchor="lm")
        for (rm, lab, col) in ((0.1075, "Earth's orbit", (120, 170, 255)), (3.23, "Neptune · 3.23 m", (90, 120, 240)), (215, "Oort cloud starts · 215 m", ICE20), (10750, "Oort cloud ends · 10.75 km", ICE20)):
            rp = rm * ppm
            if 6 < rp < 2600:
                d.ellipse([ox - rp, oy - rp, ox + rp, oy + rp], outline=col, width=2)
                if rp > 40 and oy - rp > 40: d.text((ox, oy - rp - 16), lab, font=F(24, "Bold"), fill=col, anchor="mm")
        vx = ox + 18.6 * ppm * math.cos(-0.6); vy = oy + 18.6 * ppm * math.sin(-0.6)
        if 4 < 18.6 * ppm < 3000:
            d.line([(ox, oy), (vx, vy)], fill=(255, 220, 120), width=2); d.ellipse([vx - 7, vy - 7, vx + 7, vy + 7], fill=(255, 220, 120))
            d.text((vx + 16, vy - 18), "Voyager 1 · 18.6 m", font=F(28, "Bold"), fill=(255, 220, 120), anchor="lm")
        _grain20(img, ox, oy, 6); d = ImageDraw.Draw(img)
        d.text((ox, oy + 34), "SUN", font=F(24, "Black"), fill=SAND20, anchor="mm")
        if mode == "proxima":
            for (km_, dy, lab, col) in ((28.9, 0, "PROXIMA · 28.9 km", (255, 140, 110)), (29.7, 70, "ALPHA CEN A + B · 29.7 km", (255, 230, 170))):
                x = ox + km_ * 1000 * ppm
                if x < W + 50:
                    paste_c(img, radial(80, [(0, col + (230,)), (1, col + (0,))]), x, oy + dy); d = ImageDraw.Draw(img)
                    d.ellipse([x - 5, oy + dy - 5, x + 5, oy + dy + 5], fill=col)
                    d.text((x - 20, oy + dy + (-46 if dy == 0 else 46)), lab, font=F(30, "Black"), fill=col, anchor="rm")
            d.line([(ox + 20, oy + 140), (ox + 28.9 * 1000 * ppm - 20, oy + 140)], fill=(120, 130, 160), width=2)
            d.text(((ox + ox + 28.9 * 1000 * ppm) / 2, oy + 170), "nothing but empty space", font=F(30, "SemiBold"), fill=DIM, anchor="mm")
        _scalebar20(img, ppm) if ppm < 0.3 or True else None
        if ppm * 1000 > 280: pass
        title = {"house": "VOYAGER 1 HASN'T LEFT THE BUILDING", "oort": "THE OORT CLOUD = A TOWN", "proxima": "THE NEAREST STAR"}[mode]
        alpha_text(img, (W / 2, 80), title, F(48, "ExtraBold"), WHITE, a)
        return
    # ----- galaxy modes -----
    d = ImageDraw.Draw(img)
    if mode == "galaxy":
        kpx = 1300 / 680000.0; gx = W / 2 + 120; gy = 560
        gw = 1300 * easeio((t - 0.6) / 1.5)
        if gw > 8: paste_c(img, _gal20(gw), gx, gy, a)
        d = ImageDraw.Draw(img)
        ex = gx - 650; ey = 930; mx = ex + 384400 * kpx
        paste_c(img, earth_sprite(9), ex, ey); paste_c(img, moon8(5), mx, ey); d = ImageDraw.Draw(img)
        d.line([(ex, ey + 30), (mx, ey + 30)], fill=(200, 200, 220), width=3)
        d.text(((ex + mx) / 2, ey + 60), "real Earth -> Moon · 384,400 km", font=F(26, "Bold"), fill=(200, 200, 220), anchor="mm")
        if gw > 1000:
            d.line([(gx - 650, 200), (gx + 650, 200)], fill=DUSK20, width=3)
            d.text((gx, 170), "THE MILKY WAY at our scale · 680,000 km", font=F(32, "Black"), fill=DUSK20, anchor="mm")
        alpha_text(img, (60, 1030), "galaxy drawn to the same scale as the real Earth-Moon distance", F(24, "SemiBold"), DIM, a, anchor="lm")
    elif mode == "center":
        gx, gy = 640, 560; paste_c(img, _gal20(1000), gx, gy, a); d = ImageDraw.Draw(img)
        sx, sy = gx + 0.54 * 500, gy + 0.54 * 120
        d.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=SAND20); d.text((sx + 14, sy + 24), "our grain", font=F(24, "Bold"), fill=SAND20, anchor="lm")
        qq = easeio((t - 0.4) / 1.2); d.line([(sx, sy), (lerp(sx, gx, qq), lerp(sy, gy, qq))], fill=WHITE, width=3)
        d.text(((sx + gx) / 2, (sy + gy) / 2 - 30), "184 km", font=F(34, "Black"), fill=WHITE, anchor="mm")
        la = ease((t - 1.2) / 0.6)
        if la > 0:
            def inside(lay, cx, cy, r):
                dl = ImageDraw.Draw(lay)
                dl.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(40, 30, 50, 255))
                for k in range(26): dl.ellipse([cx - 60 - k * 2.4, cy - 60 - k * 2.4, cx + 60 + k * 2.4, cy + 60 + k * 2.4], outline=(255, 170, 90, max(0, 160 - k * 6)), width=2)
                dl.ellipse([cx - 60, cy - 60, cx + 60, cy + 60], fill=(0, 0, 0, 255))
                dl.line([(cx - 60, cy + 120), (cx + 60, cy + 120)], fill=(255, 255, 255, 255), width=4)
                dl.text((cx, cy + 150), "17 mm", font=F(28, "Black"), fill=(255, 255, 255, 255), anchor="mm")
                dl.text((cx, cy - 120), "SAGITTARIUS A*", font=F(28, "Black"), fill=(255, 200, 140, 255), anchor="mm")
            d.line([(gx, gy), (1460, 520)], fill=(30, 30, 36), width=6)
            _lens20(img, 1460, 520, int(270 * la), inside, ring=(255, 170, 90))
        alpha_text(img, (W / 2, 80), "A BLACK MARBLE, 184 KM AWAY", F(48, "ExtraBold"), WHITE, a)
    elif mode == "andromeda":
        mwx, y = 160, 470; w_ = 60; ax = mwx + 25 * w_
        paste_c(img, _gal20(w_), mwx, y, a); paste_c(img, _gal20(w_ * 1.5), ax, y, ease((t - 0.8) / 0.6)); d = ImageDraw.Draw(img)
        d.text((mwx, y + 60), "MILKY WAY", font=F(24, "Black"), fill=DUSK20, anchor="mm"); d.text((ax, y + 70), "ANDROMEDA", font=F(24, "Black"), fill=(255, 200, 160), anchor="mm")
        qq = easeio((t - 0.6) / max(1.0, dur * 0.6)); n = int(44 * qq)
        for i in range(n):
            x0 = mwx + i * (ax - mwx) / 44.0; d.line([(x0 + 2, 640), (x0 + (ax - mwx) / 44.0 - 2, 640)], fill=(210, 210, 230), width=8)
        d.text((W / 2, 700), f"{n} Earth-Moon distances", font=F(36, "Black"), fill=(210, 210, 230), anchor="mm")
        for i in range(25): d.ellipse([mwx + i * w_ - 3, 380 - 3, mwx + i * w_ + 3, 380 + 3], fill=DUSK20)
        d.text((W / 2, 340), "25 Milky Way widths", font=F(32, "Black"), fill=DUSK20, anchor="mm")
        d.text((W / 2, 820), f"{17.0 * qq:,.1f} million km at our scale", font=F(56, "Black"), fill=WHITE, anchor="mm")
        d.text((W / 2, 890), "about 388 years on foot", font=F(34, "Bold"), fill=SAND20, anchor="mm")
    elif mode == "collide":
        qq = easeio(t / max(1.0, dur * 0.8)); sep = lerp(700, 0, qq)
        g1 = _gal20(520).rotate(lerp(0, 60, qq), expand=True, resample=Image.BICUBIC); g2 = _gal20(620).rotate(lerp(30, -40, qq), expand=True, resample=Image.BICUBIC)
        paste_c(img, g1, W / 2 - sep / 2, 540, a * lerp(1, 0.75, qq)); paste_c(img, g2, W / 2 + sep / 2, 540, a * lerp(1, 0.75, qq))
        alpha_text(img, (W / 2, 90), "GALAXIES COLLIDE. STARS SLIDE PAST.", F(46, "ExtraBold"), WHITE, a)
        alpha_text(img, (W / 2, 960), "Hubble 2012: ~4 billion years  ·  2025 study: ~50% chance in 10 billion", F(30, "Bold"), SAND20, ease((t - 1.0) / 0.5))
        alpha_text(img, (W / 2, 1020), "illustration", F(22, "SemiBold"), DIM, a)

def _snail20(d, x, y, s, t, col=(200, 170, 120)):
    d.ellipse([x - 60 * s, y - 10 * s, x + 40 * s, y + 14 * s], fill=(170, 160, 130))
    d.line([(x + 30 * s, y - 4 * s), (x + 46 * s, y - 34 * s)], fill=(170, 160, 130), width=max(2, int(4 * s)))
    d.line([(x + 22 * s, y - 4 * s), (x + 32 * s, y - 36 * s)], fill=(170, 160, 130), width=max(2, int(4 * s)))
    d.ellipse([x - 44 * s, y - 60 * s, x + 16 * s, y], fill=col, outline=(120, 90, 50), width=max(2, int(3 * s)))
    for k in range(1, 4):
        rr = 30 * s * k / 4; d.arc([x - 14 * s - rr, y - 30 * s - rr, x - 14 * s + rr, y - 30 * s + rr], 0, 300, fill=(120, 90, 50), width=max(2, int(3 * s)))

def sc_snailrace(img, v, t, dur):
    """light at the grain-of-sand scale: 0.215 mm/s. mode sun = light front crossing 10.75 cm from the grain to Earth, clock 0 -> 8:19 |
    race = two lanes on a cm track: record racing snail 2.75 mm/s vs light 0.215 mm/s (both sped up the same) | proxima = a light pulse
    crawling 28.9 km to Proxima while a year counter runs to 4.24"""
    mode = v.get("mode", "sun"); a = ease(t / 0.5); d = ImageDraw.Draw(img)
    if mode == "sun":
        ppc = 130.0; gx, gy = 260, 520; ex = gx + 10.75 * ppc
        qq = max(0.0, min(1.0, (t - 0.4) / max(1.0, dur * 0.7)))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        fx = gx + (ex - gx) * qq
        for k in range(40): dl.rectangle([gx + (fx - gx) * k / 40, gy - 40, gx + (fx - gx) * (k + 1) / 40, gy + 40], fill=(255, 230, 150, int(20 + 60 * k / 40)))
        dl.rectangle([fx - 4, gy - 50, fx + 4, gy + 50], fill=(255, 245, 200, 255))
        img.alpha_composite(lay); _grain20(img, gx, gy, 7); d = ImageDraw.Draw(img)
        d.ellipse([ex - 4, gy - 4, ex + 4, gy + 4], fill=(140, 190, 255)); d.text((ex, gy + 80), "EARTH", font=F(30, "Black"), fill=(160, 205, 255), anchor="mm")
        d.text((gx, gy + 80), "SUN", font=F(30, "Black"), fill=SAND20, anchor="mm")
        d.line([(gx, 700), (ex, 700)], fill=WHITE, width=3); d.text(((gx + ex) / 2, 735), "10.75 cm", font=F(32, "Black"), fill=WHITE, anchor="mm")
        s = 499 * qq; d.text((W / 2, 860), f"{int(s // 60)}:{int(s % 60):02d}", font=F(110, "Black"), fill=(255, 235, 160), anchor="mm")
        d.text((W / 2, 950), "minutes for light to cross the gap (shown sped up)", font=F(30, "Bold"), fill=DIM, anchor="mm")
        alpha_text(img, (W / 2, 160), "SUNLIGHT STILL TAKES 8 MINUTES", F(52, "ExtraBold"), WHITE, a)
    elif mode == "race":
        x0, x1 = 160, W - 160; ppm_ = (x1 - x0) / 60.0  # 60 mm track
        sp = 60 / 2.75 / max(1.0, dur * 0.8 - 0.6)  # visual speed-up: the snail finishes at 80% of the scene
        tt = max(0.0, t - 0.6) * sp
        sx = x0 + min(60, 2.75 * tt) * ppm_; lx = x0 + min(60, 0.2155 * tt) * ppm_
        for i, (y, lab, col) in enumerate(((420, "RECORD RACING SNAIL · 2.75 mm/s", (210, 190, 140)), (700, "LIGHT, AT OUR SCALE · 0.215 mm/s", (255, 235, 150)))):
            d.rectangle([x0, y - 50, x1, y + 50], fill=(18, 22, 34)); d.line([(x1, y - 60), (x1, y + 60)], fill=(255, 255, 255), width=4)
            for mm_ in range(0, 61, 5):
                X = x0 + mm_ * ppm_; d.line([(X, y + 50), (X, y + (34 if mm_ % 10 else 24))], fill=(120, 130, 150), width=2)
            d.text((x0, y - 82), lab, font=F(32, "Black"), fill=col, anchor="lm")
        _snail20(d, sx, 440, 1.0, t)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([x0, 690, lx, 710], fill=(255, 235, 150, 140)); dl.ellipse([lx - 14, 686, lx + 14, 714], fill=(255, 250, 210, 255)); img.alpha_composite(lay)
        d = ImageDraw.Draw(img)
        d.text((W / 2, 880), "the snail is 13× faster", font=F(64, "Black"), fill=(210, 190, 140), anchor="mm")
        d.text((W / 2, 960), "light: 78 cm per hour · both sped up the same", font=F(30, "Bold"), fill=DIM, anchor="mm")
        alpha_text(img, (W / 2, 160), "LIGHT LOSES TO A SNAIL", F(56, "ExtraBold"), WHITE, a)
    else:  # proxima
        x0, x1, y = 200, W - 260, 540; qq = easeio((t - 0.4) / max(1.0, dur * 0.75))
        d.line([(x0, y), (x1, y)], fill=(80, 90, 120), width=3)
        _grain20(img, x0, y, 7); paste_c(img, radial(90, [(0, (255, 140, 110, 230)), (1, (255, 140, 110, 0))]), x1, y); d = ImageDraw.Draw(img)
        d.ellipse([x1 - 6, y - 6, x1 + 6, y + 6], fill=(255, 150, 120))
        px = lerp(x0, x1, qq); paste_c(img, radial(60, [(0, (255, 250, 210, 255)), (1, (255, 230, 150, 0))]), px, y); d = ImageDraw.Draw(img)
        d.text((x0, y + 60), "SUN", font=F(28, "Black"), fill=SAND20, anchor="mm"); d.text((x1, y + 60), "PROXIMA", font=F(28, "Black"), fill=(255, 150, 120), anchor="mm")
        d.text((W / 2, y - 80), "28.9 km at our scale", font=F(32, "Bold"), fill=WHITE, anchor="mm")
        d.text((W / 2, 780), f"{4.24 * qq:.2f} years", font=F(110, "Black"), fill=(255, 235, 160), anchor="mm")
        d.text((W / 2, 870), "for light to get there: the same as in real life", font=F(32, "Bold"), fill=DIM, anchor="mm")
        alpha_text(img, (W / 2, 160), "THE SNAIL'S LONG CRAWL", F(56, "ExtraBold"), WHITE, a)

def _rau20(au, cx_r=470):
    lo, hi = math.log10(0.3), math.log10(1.2e5)
    return 40 + cx_r * (math.log10(max(au, 0.3)) - lo) / (hi - lo)

_web20 = None
def _webdots20():
    global _web20
    if _web20 is None:
        rng = random.Random(2020); pts = []
        nodes = [(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(40)]
        for _ in range(1800):
            nx, ny = rng.choice(nodes); mx, my = rng.choice(nodes); f = rng.random()
            x = lerp(nx, mx, f) + rng.gauss(0, 0.03); y = lerp(ny, my, f) + rng.gauss(0, 0.03)
            if x * x + y * y < 1: pts.append((x, y, rng.random()))
        _web20 = pts
    return _web20

def _universe20(img, cx, cy, r, t, a=1.0):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(60, 40, 110, int(120 * a)), outline=DUSK20 + (int(255 * a),), width=4)
    for (x, y, b) in _webdots20():
        s = 1.2 + b * 1.6; X = cx + x * r * 0.97; Y = cy + y * r * 0.97
        dl.ellipse([X - s, Y - s, X + s, Y + s], fill=mix((180, 160, 255), (255, 220, 190), b) + (int((140 + 100 * b) * a),))
    img.alpha_composite(lay)
    paste_c(img, radial(int(r * 2.6), [(0, DUSK20 + (0,)), (0.74, DUSK20 + (0,)), (0.78, DUSK20 + (int(90 * a),)), (1, DUSK20 + (0,))]), cx, cy)

def sc_fitinside(img, v, t, dur):
    """the real solar system on a LOG radial scale (0.3 AU -> 120,000 AU): Earth / Jupiter / Neptune orbits, Voyager 1 at 173 AU, the Oort
    cloud 2,000 -> 100,000 AU as an icy band, and the observable universe at grain-of-sand scale (4,227 AU wide, radius 2,113 AU) as a violet
    cosmic-web sphere. mode hook (all + headline + grain inset) | zoom (radius counter sweeps out to 2,113 AU) | real (labels in order) | reveal"""
    mode = v.get("mode", "real"); a = ease(t / 0.5) if mode != "hook" else 1.0
    cx, cy = (1240, 560) if mode != "zoom" else (W / 2, 560)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    r0, r1 = _rau20(2000), _rau20(1.0e5); rng = random.Random(7)
    for _ in range(900):
        rr = lerp(r0, r1, rng.random() ** 0.8); th_ = rng.uniform(0, 2 * math.pi) + t * 0.01
        x = cx + rr * math.cos(th_); y = cy + rr * math.sin(th_)
        dl.ellipse([x - 1.6, y - 1.6, x + 1.6, y + 1.6], fill=ICE20 + (int(110 * a),))
    img.alpha_composite(lay); d = ImageDraw.Draw(img)
    orbs = [(1, "Earth", (120, 170, 255)), (5.2, "Jupiter", (215, 175, 130)), (30.07, "Neptune", (90, 120, 240))]
    for i, (au, nm, col) in enumerate(orbs):
        rp = _rau20(au); d.ellipse([cx - rp, cy - rp, cx + rp, cy + rp], outline=col, width=2)
    uq = 1.0
    if mode == "zoom": uq = easeio((t - 0.4) / max(1.0, dur * 0.7))
    if mode in ("real",): uq = ease((t - dur * 0.5) / 0.8)
    ur = _rau20(lerp(0.3, 2113, uq)) if mode == "zoom" else _rau20(2113)
    if uq > 0: _universe20(img, cx, cy, ur, t, a * (uq if mode == "real" else 1.0))
    d = ImageDraw.Draw(img)
    for i, (au, nm, col) in enumerate(orbs):
        rp = _rau20(au); d.text((cx + rp * 0.71 + 6, cy - rp * 0.71 - 10), nm, font=F(22, "Bold"), fill=col, anchor="lm")
    paste_c(img, sun_sprite(6), cx, cy); d = ImageDraw.Draw(img)
    vr = _rau20(173); vx, vy = cx - vr * 0.8, cy + vr * 0.6
    d.ellipse([vx - 6, vy - 6, vx + 6, vy + 6], fill=(255, 220, 120)); d.text((vx - 12, vy + 22), "Voyager 1 · 173 AU", font=F(24, "Bold"), fill=(255, 220, 120), anchor="rm")
    d.text((cx, cy - r1 - 18), "OORT CLOUD · out to ~100,000 AU", font=F(26, "Bold"), fill=ICE20, anchor="mm")
    if mode == "zoom":
        au_now = lerp(0.3, 2113, uq)
        d.text((W / 2, 1010), f"{au_now:,.0f} × the Earth-Sun distance", font=F(46, "Black"), fill=DUSK20, anchor="mm")
        d.text((W - 40, 1050), "log scale", font=F(22, "SemiBold"), fill=DIM, anchor="rm")
        return
    d.text((cx + ur * 0.0, cy + ur + 30), "THE OBSERVABLE UNIVERSE at grain-of-sand scale · 4,227 AU wide", font=F(26, "Black"), fill=DUSK20, anchor="mm") if uq > 0.5 else None
    d.text((W - 40, 1050), "distances from the Sun on a log scale", font=F(22, "SemiBold"), fill=DIM, anchor="rm")
    # left column
    if mode == "hook":
        alpha_text(img, (60, 230), "THE SUN = 1 mm", F(76, "Black"), SAND20, 1.0, anchor="lm")
        alpha_text(img, (60, 360), "THE UNIVERSE", F(96, "Black"), WHITE, 1.0, anchor="lm")
        alpha_text(img, (60, 470), "FITS IN HERE", F(96, "Black"), DUSK20, 1.0, anchor="lm")
        _grain20(img, 200, 760, 12); d = ImageDraw.Draw(img)
        d.ellipse([200 - 70, 760 - 70, 200 + 70, 760 + 70], outline=SAND20, width=3)
        d.text((300, 760), "a 1 mm grain of sand", font=F(32, "Bold"), fill=SAND20, anchor="lm")
    elif mode == "real":
        rows = [("Earth's orbit", "1 AU"), ("Neptune", "30 AU"), ("Voyager 1", "173 AU"), ("the shrunken universe", "4,227 AU wide"), ("Oort cloud", "to ~100,000 AU")]
        for i, (k, val) in enumerate(rows):
            aa = ease((t - 0.3 - i * dur * 0.14) / 0.4); y = 260 + i * 120
            alpha_text(img, (70, y), k, F(36, "Bold"), WHITE, aa, anchor="lm")
            alpha_text(img, (70, y + 46), val, F(40, "Black"), DUSK20 if i == 3 else SAND20, aa, anchor="lm")
    else:  # reveal
        alpha_text(img, (70, 300), "EVERY GALAXY", F(80, "Black"), WHITE, a, anchor="lm")
        alpha_text(img, (70, 400), "WE CAN SEE", F(80, "Black"), WHITE, a, anchor="lm")
        alpha_text(img, (70, 520), "inside the Sun's", F(48, "Bold"), SAND20, ease((t - 0.6) / 0.5), anchor="lm")
        alpha_text(img, (70, 580), "cloud of comets", F(48, "Bold"), ICE20, ease((t - 0.8) / 0.5), anchor="lm")


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
