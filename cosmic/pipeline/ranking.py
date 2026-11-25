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
vis.type == "spin" / THEME.hook/outro == "spin": objeto girando (vis.kind = gas | dwarf | rock | pulsar) numa velocidade visível vis.vis_rps,
  com selo "REAL SPEED" / "sped up N×" / "slowed down N×" calculado contra a real (vis.rps = voltas por segundo) + régua log de voltas por
  segundo (1 por dia -> 1.000/s, Terra de referência) (rank11).
vis.type == "wind" / THEME.hook/outro == "wind": planeta com faixas e nuvens correndo numa velocidade visível (log da real) + régua log
  de vento 100–50.000 km/h com marcas de referência (furacão cat. 5, avião, som); vis.kmh, vis.col, vis.r, vis.earth, vis.note (rank12).
vis.type == "crater" / THEME.hook/outro == "crater": cratera vista de cima EM ESCALA (4 px/km) sobre chão rochoso; um rastro cai, a cratera
  abre com flash, borda e anel central (vis.erosion 0–1 apaga a borda das antigas) + barra de uma maratona (42 km) como régua; outro = as 5
  bordas concêntricas em escala com cores vis.ring (rank13).
vis.type == "orbityear" / THEME.hook/outro == "orbityear": órbita do mundo EM ESCALA em volta de um Sol minúsculo (órbita da Terra na mesma escala),
  uma volta com tempo de Kepler (lento longe do Sol) + contador de anos terrestres + "sped up N×" + régua log 1–20.000 anos; vis.a (UA), vis.e,
  vis.yr, vis.col, vis.ang; outro = as 5 órbitas na mesma escala (rank14).
vis.type == "probes" / THEME.hook/outro == "probes": sonda desenhada por código (vis.kind = voyager | pioneer | horizons) + "a luz leva N horas"
  + selo STILL TALKING / SILENT SINCE + trilha Sol -> 180 UA em escala de raiz quadrada (Netuno, fim da bolha do Sol) com a sonda saindo
  do Sol até vis.au; gancho = pulso de luz correndo na trilha até um "?"; outro = as 5 na mesma trilha (rank15).
vis.type == "rocks" / THEME.hook/outro == "rocks": asteroide desenhado por código (contorno irregular por harmônicos vis.lump, crateras,
  vis.spot = manchas claras de Ceres) EM ESCALA (0,72 px/km) girando devagar + barra de 100 km + "dar a volta de carro a 100 km/h: N h";
  gancho = silhueta escura de Ceres com "?"; outro = os 5 lado a lado na mesma escala (rank16).
vis.type == "weigh" / THEME.hook/outro == "weigh": balança: o objeto no prato esquerdo (vis.kind = sun | gas | ringed | ice, vis.col, vis.r)
  contra uma pilha de Terras no direito, o braço nivela enquanto o contador sobe até vis.earths + régua log 1–1.000.000 massas terrestres;
  gancho = Terra sozinha num prato contra "?"; outro = as 5 na régua (rank17).
vis.type == "gravity" / THEME.hook/outro == "gravity": bonequinho numa balança de banheiro sobre a superfície curva do mundo (vis.kind =
  sun | gas | ringed | ice | earth, vis.col), o visor sobe de 70 kg até 70 × g/9,80 e os joelhos dobram (log) + régua log "× gravidade da
  Terra" (½× – 30×) com Vênus/Urano de fora; vis.g em m/s²; gancho = visor piscando "? ? ?" sobre chão escuro; outro = as 5 na régua (rank18).
vis.type == "litre" / THEME.hook/outro == "litre": 1 litro do material médio do planeta despejado num pote de vidro sobre uma balança de
  cozinha (visor sobe até vis.kgl kg) ao lado de uma garrafa de água de 1,00 kg + barra 0–6 kg/L com a linha da água e Saturno (0,69,
  boiaria); gancho = pote vazio com "?" e visor correndo; outro = os 5 potes em fila, cada um na sua balança (rank19).
vis.type == "beads" / THEME.hook/outro == "beads": o planeta numa ESCALA COMUM (raio de Júpiter = 430 px; vis.km = diâmetro equatorial,
  vis.kind = jupiter | ringed | earth | outro, vis.col) e Terras na mesma escala caindo uma a uma num fio sobre o equador, contador até
  vis.earths + contorno tracejado do tamanho do #1; Vênus ao lado da Terra no #5; gancho = disco "?" do tamanho de Júpiter com 11 Terras
  enfileiradas; outro = os 5 lado a lado numa escala menor (rank20).
vis.type == "tilt" / THEME.hook/outro == "tilt": inclinação do eixo. Planeta com faixas girado pela obliquidade (vis.deg) sobre a linha do
  plano da órbita, linha tracejada "reto para cima" + arco transferidor que varre até o eixo com contador de graus + eixo fantasma da
  Terra (23,4°); marcador na superfície mostra o sentido da rotação (vis.retro = gira ao contrário); vis.kind = gas | ice | rock | ringed;
  gancho = planeta "?" com o eixo virando até ficar de cabeça para baixo; outro = os 5 em fila, cada um na sua inclinação (rank21).
vis.type == "pair" / THEME.hook/outro == "pair": a lua do lado do SEU planeta, com o planeta sempre do mesmo tamanho (raio 300 px) e a lua
  em escala com ele (vis.ratio = diâmetro da lua / diâmetro do planeta); a lua sai de trás do planeta e para ao lado, contador "% da
  largura" + barra 0–60%; vis.kind = gas | ringed | earth | ice | dwarf, vis.col (planeta), vis.mcol (lua), vis.pname / vis.mname;
  gancho = planeta escuro com uma lua "?" da metade do tamanho; outro = os 5 pares em fila, planetas iguais (rank22).
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

# ---- rank11: spin ----
SP_LO, SP_HI = -5.5, 3.3   # log10 spins per second on the meter
SP_X0, SP_X1 = 90, W - 90
def sp_x(rps): return lerp(SP_X0, SP_X1, (math.log10(rps) - SP_LO) / (SP_HI - SP_LO))
def spin_meter(img, th, shown, cur=None, y=1160, a=1.0):
    d = ImageDraw.Draw(img); acc = tuple(th["accent"]); acc2 = tuple(th["accent2"])
    d.rounded_rectangle([SP_X0, y - 12, SP_X1, y + 12], 12, fill=(20, 26, 50), outline=(70, 90, 140), width=2)
    for e, lab in [(-5, "1 per day"), (-2, ""), (0, "1 per second"), (2, ""), (3, "1,000 / s")]:
        x = sp_x(10 ** e) if e != -5 else sp_x(1 / 86400)
        d.line([(x, y - 26), (x, y + 26)], fill=(110, 125, 170), width=3)
        if lab: d.text((x, y + 52), lab, font=F(26, "Bold"), fill=(150, 160, 195), anchor="mm")
    d.text((sp_x(1 / 86400) - 6, y + 52), "", font=F(26, "ExtraBold"), fill=(140, 190, 255), anchor="mm")
    xe = sp_x(1 / 86400); d.ellipse([xe - 9, y - 9, xe + 9, y + 9], fill=(140, 190, 255)); d.text((xe, y + 88), "(Earth)", font=F(24, "ExtraBold"), fill=(140, 190, 255), anchor="mm")
    for o in shown:
        x = sp_x(o["vis"]["rps"]); c = acc if (cur is not None and o is cur) else acc2
        rr = 18 if o is cur else 12
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=c, outline=(255, 255, 255), width=3)
        d.text((x, y - 48 - (12 if o is cur else 0) - (30 if o["rank"] == 1 and cur is None else 0)), f'#{o["rank"]}', font=F(30 if o is cur else 24, "Black"), fill=c, anchor="mm")
    d.text((W / 2, y - 100), "SPINS PER SECOND (log scale)", font=F(28, "ExtraBold"), fill=(200, 205, 225), anchor="mm")

def spin_obj(img, kind, cx, cy, r, ang, col):
    d = ImageDraw.Draw(img)
    if kind == "gas":
        R.paste_c(img, R.planet_sprite(r, col, light=(-0.7, -0.3)), cx, cy); d = ImageDraw.Draw(img)
        for k, dy in enumerate((-0.55, -0.25, 0.1, 0.4, 0.62)):
            w_ = r * math.sqrt(1 - dy * dy); d.line([(cx - w_, cy + dy * r), (cx + w_, cy + dy * r)], fill=mix(col, (120, 70, 40), 0.5), width=max(3, r // 18))
        for off, sc_, c2 in ((0, 1.0, (200, 90, 60)), (2.1, 0.6, (240, 230, 210)), (4.0, 0.5, (150, 90, 60))):
            a_ = ang * 2 * math.pi + off; z = math.cos(a_)
            if z > 0:
                x = cx + r * 0.95 * math.sin(a_); w_ = r * 0.22 * sc_ * (0.3 + 0.7 * z); yy = cy + r * 0.22
                d.ellipse([x - w_, yy - r * 0.09 * sc_, x + w_, yy + r * 0.09 * sc_], fill=c2)
    elif kind == "dwarf":
        R.paste_c(img, R.radial(int(r * 3), [(0, (255, 255, 255, 255)), (0.3, (220, 235, 255, 255)), (0.34, (170, 200, 255, 160)), (1, (90, 140, 255, 0))]), cx, cy)
        d = ImageDraw.Draw(img)
        for off in (0, math.pi):
            a_ = ang * 2 * math.pi + off; z = math.cos(a_)
            if z > -0.1:
                x = cx + r * 0.42 * math.sin(a_); w_ = r * 0.12 * (0.3 + 0.7 * max(0, z))
                d.ellipse([x - w_, cy - r * 0.2 - w_, x + w_, cy - r * 0.2 + w_], fill=(255, 190, 120))
    elif kind == "rock":
        a_ = ang * 2 * math.pi; pts = []
        rng = random.Random(24)
        rad = [0.75 + 0.35 * rng.random() for _ in range(14)]
        for k in range(14):
            th_ = a_ + 2 * math.pi * k / 14; rr = r * rad[k] * (1.35 if k in (0, 7) else 1.0)
            pts.append((cx + rr * math.cos(th_), cy + rr * 0.8 * math.sin(th_)))
        d.polygon(pts, fill=(120, 108, 96), outline=(200, 185, 165)); 
        for k in (2, 5, 10):
            x, y = pts[k]; d.ellipse([lerp(cx, x, 0.5) - 10, lerp(cy, y, 0.5) - 8, lerp(cx, x, 0.5) + 10, lerp(cy, y, 0.5) + 8], fill=(85, 76, 68))
    elif kind == "pulsar":
        a_ = ang * 2 * math.pi
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for off in (0, math.pi):
            b = a_ + off; L = 520
            p1 = (cx + L * math.cos(b - 0.12), cy + L * math.sin(b - 0.12)); p2 = (cx + L * math.cos(b + 0.12), cy + L * math.sin(b + 0.12))
            dl.polygon([(cx, cy), p1, p2], fill=col + (120,))
        img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(6)))
        R.paste_c(img, R.radial(int(r * 4), [(0, (255, 255, 255, 255)), (0.22, (200, 225, 255, 255)), (0.25, (150, 190, 255, 150)), (1, (90, 120, 255, 0))]), cx, cy)

def spin_vis(img, it, th, t, dur):
    v = it["vis"]; ang = t * v.get("vis_rps", 0.5)
    spin_obj(img, v["kind"], W / 2, 760, v.get("r", 230), ang, tuple(v.get("col", (200, 200, 220))))
    f = v["vis_rps"] / v["rps"]
    lab = "REAL SPEED" if 0.7 < f < 1.4 else (f"sped up {f:,.0f}×" if f > 1 else f"slowed down {1 / f:,.0f}×")
    text(img, (W / 2, 450), lab, 40, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.5) / 0.4))
    if v.get("note"): text(img, (W / 2, 990), v["note"], 38, (235, 235, 245), w="ExtraBold", a=ease((t - 1.6) / 0.5))
    shown = [o for o in ALL_ITEMS if o["rank"] >= it["rank"]]
    spin_meter(img, th, shown, cur=it, a=1.0)


# ---- rank12: wind (planet with streaming cloud bands + log wind gauge 100–50,000 km/h with reference marks) ----
WD_LO, WD_HI, WD_X0, WD_X1 = 2.0, math.log10(50000), 110, W - 110
WD_REFS = [(252, "Cat 5 hurricane"), (900, "airliner"), (1235, "speed of sound")]
def wd_x(kmh): return lerp(WD_X0, WD_X1, (math.log10(kmh) - WD_LO) / (WD_HI - WD_LO))
def wind_meter(img, th, shown, cur=None, y=1180, a=1.0, prog=1.0):
    d = ImageDraw.Draw(img); acc = tuple(th["accent"]); acc2 = tuple(th["accent2"])
    d.rounded_rectangle([WD_X0, y - 12, WD_X1, y + 12], 12, fill=(30, 34, 50))
    for k in (100, 1000, 10000):
        x = wd_x(k); d.line([(x, y - 26), (x, y + 26)], fill=(120, 130, 160), width=3)
        d.text((x, y + 50), f"{k:,} km/h", font=F(26, "Bold"), fill=(150, 160, 190), anchor="mm")
    for kmh, lab in WD_REFS:
        x = wd_x(kmh); d.line([(x, y - 60), (x, y - 14)], fill=(200, 200, 215), width=2)
        d.text((x, y - 74 - (30 if lab == "airliner" else 0)), lab, font=F(24, "SemiBold"), fill=(200, 205, 220), anchor="mm")
    for o in shown:
        v = o["vis"]; col = tuple(v["col"]); x = wd_x(v["kmh"] * (prog if o is cur else 1.0) if (o is not cur or prog >= 0.01) else 100)
        r = 20 if o is cur else 13
        d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=(255, 255, 255), width=3)
        if o is not cur: d.text((x, y + 86 + (34 if o["rank"] % 2 == 0 else 0)), o["short"], font=F(24, "ExtraBold"), fill=col, anchor="mm")

def wind_planet(img, cx, cy, r, col, speed, t, a=1.0, earth=False):
    """banded planet; cloud streaks race along the bands at a visible speed (log of real speed)"""
    if earth: R.paste_c(img, R.earth_sprite(int(r), glow=None), cx, cy)
    else: R.paste_c(img, R.planet_sprite(int(r), col, light=(-0.7, -0.35)), cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(int(r) + 7)
    vis = 0.15 + 0.22 * (math.log10(max(100, speed)) - 2)
    for i in range(26):
        lat = rng.uniform(-0.85, 0.85); hw = math.sqrt(1 - lat * lat) * r; y = cy + lat * r
        L = rng.uniform(0.15, 0.45) * hw * (0.6 + vis); ph = (rng.random() + t * vis * rng.uniform(0.7, 1.3)) % 1.0
        x = cx - hw + ph * 2 * hw
        x0_, x1_ = max(cx - hw, x - L), min(cx + hw, x)
        if x1_ > x0_: dl.line([(x0_, y), (x1_, y)], fill=(255, 255, 255, int(150 * a)), width=rng.choice([3, 4, 6]))
    img.alpha_composite(lay)

def wind_vis(img, it, th, t, dur):
    v = it["vis"]; prog = easeio((t - 0.4) / 1.6)
    wind_planet(img, W / 2, 800, v.get("r", 250), tuple(v["col"]), v["kmh"], t, earth=v.get("earth", False))
    wind_meter(img, th, [o for o in ALL_ITEMS if o["rank"] > it["rank"]] + [it], cur=it, prog=max(0.01, prog))
    if v.get("note"): text(img, (W / 2, 470), v["note"], 40, (230, 232, 240), w="ExtraBold", a=ease((t - 1.2) / 0.5))

# ---- rank13: crater (top-down crater TO SCALE on rocky ground: a streak hits, the crater opens with rim + peak ring; marathon bar for scale;
#      old craters are eroded = fainter rim) ----
CR_K = 4.0  # px per km (160 km = 640 px)
_cr_ground = None
def cr_ground():
    global _cr_ground
    if _cr_ground is None:
        rng = np.random.default_rng(13); acc = np.zeros((900, W), np.float32)
        for k in range(5):
            n = 4 * 2 ** k
            lo = Image.fromarray((rng.random((n, n)) * 255).astype(np.uint8)).resize((W, 900), Image.BICUBIC)
            acc += (np.asarray(lo, np.float32) / 255 - 0.5) / (1.6 ** k)
        base = np.array([96, 82, 66], np.float32); rgb = base[None, None, :] * (1 + acc[..., None] * 0.9)
        yy = np.linspace(-1, 1, 900)[:, None]; xx = np.linspace(-1, 1, W)[None, :]
        a = np.clip(1.25 - np.sqrt(xx ** 2 * 0.9 + yy ** 2) * 1.0, 0, 1) * 255
        _cr_ground = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8), "RGBA")
    return _cr_ground

def cr_crater(img, cx, cy, km, q, erosion=0.0, col=(255, 150, 70)):
    """crater of km diameter at progress q (0..1), erosion 0..1 fades the rim"""
    r = km / 2 * CR_K * ease(q)
    if r < 2: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    n = 24
    for i in range(n):
        f = 1 - i / n; rr = r * f
        sh = int(40 + 60 * (1 - f))
        dl.ellipse([cx - rr, cy - rr * 0.92, cx + rr, cy + rr * 0.92], fill=(sh, int(sh * 0.86), int(sh * 0.72), 255))
    rimw = max(3, int(r * 0.07)); ra = int(230 * (1 - 0.6 * erosion))
    dl.ellipse([cx - r, cy - r * 0.92, cx + r, cy + r * 0.92], outline=(200, 175, 140, ra), width=rimw)
    dl.arc([cx - r, cy - r * 0.92, cx + r, cy + r * 0.92], 200, 340, fill=(240, 220, 190, ra), width=max(2, rimw // 2))
    pr = r * 0.42
    dl.ellipse([cx - pr, cy - pr * 0.92, cx + pr, cy + pr * 0.92], outline=(170, 150, 120, int(200 * (1 - 0.5 * erosion))), width=max(2, rimw // 2))
    img.alpha_composite(lay)

def cr_scene(img, cx, cy, km, t, col, erosion=0.0, hit_t=0.5, label=True):
    img.alpha_composite(cr_ground(), (0, int(cy - 450)))
    q = (t - hit_t) / 1.0
    if q < 0:
        p = ease((t + 0.3) / (hit_t + 0.3)); x0, y0 = cx + 700, cy - 900
        d = ImageDraw.Draw(img); x, y = lerp(x0, cx, p), lerp(y0, cy, p)
        for j in range(16):
            u = j / 16; d.line([(lerp(x, x0, u * 0.3), lerp(y, y0, u * 0.3)), (lerp(x, x0, (u + 0.06) * 0.3), lerp(y, y0, (u + 0.06) * 0.3))], fill=(255, int(200 - 80 * u), 120), width=max(2, int(14 * (1 - u))))
        R.paste_c(img, R.radial(80, [(0, (255, 250, 220, 255)), (1, (255, 160, 60, 0))]), x, y)
        return
    cr_crater(img, cx, cy, km, min(1, q), erosion, col)
    if q < 1.2:
        fl = max(0.0, 1 - q / 1.2)
        R.paste_c(img, R.radial(int(km * CR_K * 1.6), [(0, (255, 245, 210, int(255 * fl))), (0.4, (255, 150, 60, int(160 * fl))), (1, (255, 100, 30, 0))]), cx, cy)
    d = ImageDraw.Draw(img)
    if label and q > 0.8:
        r = km / 2 * CR_K
        d.line([(cx - r, cy + r * 0.92 + 40), (cx + r, cy + r * 0.92 + 40)], fill=(255, 255, 255), width=4)
        for s in (-1, 1): d.line([(cx + s * r, cy + r * 0.92 + 28), (cx + s * r, cy + r * 0.92 + 52)], fill=(255, 255, 255), width=4)

def cr_marathon(img, x, y, th):
    d = ImageDraw.Draw(img); L = 42.195 * CR_K
    d.rounded_rectangle([x, y - 8, x + L, y + 8], 6, fill=tuple(th["accent2"]))
    d.text((x, y - 34), "a marathon, 42 km", font=F(28, "ExtraBold"), fill=tuple(th["accent2"]), anchor="lm")

def crater_vis(img, it, th, t, dur):
    v = it["vis"]; cy = 860
    cr_scene(img, W / 2, cy, v["km"], t, tuple(th["accent"]), erosion=v.get("erosion", 0.0))
    cr_marathon(img, 90, 470, th)
    if v.get("note"): text(img, (W / 2, 1260), v["note"], 40, (240, 232, 220), w="ExtraBold", a=ease((t - 1.6) / 0.5))


# ---- rank14: orbityear (one full "year" of a far world: its orbit TO SCALE around a tiny Sun, Earth's orbit drawn at the same scale,
#      the world laps once with Kepler timing (slow far out), an Earth-years counter + "sped up N×"; log ruler 1 -> 20,000 years) ----
OY_X0, OY_X1, OY_LO, OY_HI = 110, 970, 0.0, math.log10(20000)
OY_REFS = [(1, "Earth"), (11.9, "Jupiter"), (164.8, "Neptune")]
def oy_x(yr): return lerp(OY_X0, OY_X1, (math.log10(yr) - OY_LO) / (OY_HI - OY_LO))
def oy_ruler(img, th, shown, cur=None, y=1120, prog=1.0):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([OY_X0, y - 10, OY_X1, y + 10], 10, fill=(34, 30, 52))
    for k in (1, 10, 100, 1000, 10000):
        x = oy_x(k); d.line([(x, y - 22), (x, y + 22)], fill=(120, 125, 160), width=3)
        d.text((x, y + 46), f"{k:,} yr", font=F(24, "Bold"), fill=(150, 155, 190), anchor="mm")
    for yr, lab in OY_REFS:
        x = oy_x(yr); d.line([(x, y - 56), (x, y - 12)], fill=(200, 200, 215), width=2)
        d.text((x, y - 72), lab, font=F(24, "SemiBold"), fill=(200, 205, 220), anchor="mm")
    for o in shown:
        v = o["vis"]; col = tuple(v["col"]); yr = v["yr"] if o is not cur else max(1.0, v["yr"] ** max(0.0, min(1.0, prog)))
        x = oy_x(yr); r = 19 if o is cur else 12
        d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=(255, 255, 255), width=3)
        if o is not cur: d.text((x, y + 82 + {5: 0, 4: 30, 3: 60, 2: 90}.get(o["rank"], 0)), o["short"], font=F(24, "ExtraBold"), fill=col, anchor="mm")

def oy_kepler(M, e):
    E = M
    for _ in range(12): E = E - (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    return E

def oy_orbit(img, cx, cy, a_au, e, frac, col, span=820, tilt=0.42, earth=True, label=True, trail=True, ang=0.5, a=1.0, at_sun=False, k=None):
    """ellipse with the Sun at a focus; frac = fraction of the orbit done (0..1, mean anomaly). Returns the world's (x, y)"""
    k = k or span / (2 * a_au); b_au = a_au * math.sqrt(1 - e * e)
    cosA, sinA = math.cos(ang), math.sin(ang)
    def P(E):
        x, y = a_au * (math.cos(E) - e), b_au * math.sin(E)
        xr, yr = x * cosA - y * sinA, x * sinA + y * cosA
        return cx + xr * k, cy + yr * k * tilt
    # centre the drawing on the ellipse centre, not the Sun
    ox = a_au * e * cosA * k; oy = a_au * e * sinA * k * tilt
    if at_sun: ox, oy = 0.0, 0.0
    def Pc(E): x, y = P(E); return x + ox, y + oy
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    pts = [Pc(2 * math.pi * j / 240) for j in range(241)]
    for j in range(0, 240, 2): dl.line([pts[j], pts[j + 1]], fill=col + (int(110 * a),), width=3)
    if trail and frac > 0:
        Ecur = oy_kepler(2 * math.pi * frac, e); n = max(2, int(120 * Ecur / (2 * math.pi)) + 2)
        tp = [Pc(Ecur * j / (n - 1)) for j in range(n)]
        dl.line(tp, fill=col + (int(235 * a),), width=6)
    img.alpha_composite(lay)
    R.paste_c(img, R.sun_sprite(5), cx + ox, cy + oy, a)
    d = ImageDraw.Draw(img); sx, sy = cx + ox, cy + oy
    if earth:
        er = max(1.5, 1.0 * k)
        d.ellipse([sx - er, sy - er * tilt, sx + er, sy + er * tilt], outline=(110, 170, 255), width=2)
        if label:
            sg = -1 if sx > W / 2 else 1
            d.line([(sx + 8 * sg, sy + 10), (sx + 70 * sg, sy + 80)], fill=(140, 190, 255), width=2)
            d.text((sx + 76 * sg, sy + 92), "Sun + Earth's orbit", font=F(26, "Bold"), fill=(150, 195, 255), anchor="lm" if sg > 0 else "rm")
    E = oy_kepler(2 * math.pi * (frac % 1.0), e); wx, wy = Pc(E)
    R.paste_c(img, R.planet_sprite(16, col, light=(-0.8, -0.3)), wx, wy, a)
    return wx, wy

def orbityear_vis(img, it, th, t, dur):
    v = it["vis"]; col = tuple(v["col"]); lap = max(2.5, dur - 1.6)
    frac = min(1.0, max(0.0, (t - 0.5) / lap))
    oy_orbit(img, W / 2, 760, v["a"], v["e"], frac, col, span=v.get("span", 860), ang=v.get("ang", 0.5))
    yrs = v["yr"] * frac
    text(img, (W / 2, 470), f"{yrs:,.0f} Earth years", 54, (255, 255, 255), a=ease((t - 0.3) / 0.4))
    sped = v["yr"] * 365.25 * 86400 / lap
    big = f"{sped / 1e9:,.0f} billion" if sped >= 1e9 else f"{sped / 1e6:,.0f} million"
    text(img, (W / 2, 528), f"one full year, sped up about {big} times", 30, (180, 185, 210), w="Bold", a=ease((t - 0.5) / 0.4))
    oy_ruler(img, th, [o for o in ALL_ITEMS if o["rank"] > it["rank"]] + [it], cur=it, prog=max(0.0, min(1.0, frac * 1.3)))
    if v.get("note"): text(img, (W / 2, 1010), v["note"], 38, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.4) / 0.5))

# ---- rank15: farthest human-made objects ----
PR_X0, PR_X1, PR_MAX = 110, 970, 180.0
def pr_x(au): return lerp(PR_X0, PR_X1, math.sqrt(max(0.0, au) / PR_MAX))
def pr_icon(img, kind, x, y, s=1.0, ang=0.0, a=1.0):
    if kind == "voyager":
        R.voyager15(img, x, y, s, ang=ang - 0.3, a=a); return
    lay = Image.new("RGBA", (int(300 * s) + 40, int(300 * s) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); c = lay.width / 2
    def P(px, py):
        ca, sa = math.cos(ang), math.sin(ang); return (c + (px * ca - py * sa) * s, c + (px * sa + py * ca) * s)
    A = int(255 * a)
    if kind == "pioneer":
        d.line([P(0, 10), P(-110, 70)], fill=(160, 160, 170, A), width=max(2, int(4 * s))); d.line([P(0, 10), P(110, 70)], fill=(160, 160, 170, A), width=max(2, int(4 * s)))
        for sx_ in (-1, 1):
            q = P(sx_ * 96, 62); r = 9 * s; d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=(120, 110, 100, A))
        hexa = [P(22 * math.cos(k * math.pi / 3), 22 + 14 * math.sin(k * math.pi / 3)) for k in range(6)]; d.polygon(hexa, fill=(200, 170, 90, A))
        dish = [P(78 * math.cos(u), -2 + 16 * math.sin(u)) for u in [i * math.pi / 20 for i in range(41)]]; d.polygon(dish, fill=(238, 238, 245, A))
        d.line([P(0, -2), P(0, -46)], fill=(225, 225, 235, A), width=max(1, int(2 * s)))
    else:  # new horizons
        tri = [P(-46, 40), P(46, 40), P(0, -30)]; d.polygon(tri, fill=(214, 176, 80, A))
        dish = [P(44 * math.cos(u), -34 + 10 * math.sin(u)) for u in [i * math.pi / 20 for i in range(41)]]; d.polygon(dish, fill=(240, 240, 248, A))
        d.line([P(30, 30), P(80, 50)], fill=(80, 80, 90, A), width=max(3, int(10 * s)))
    img.alpha_composite(lay, (int(x - c), int(y - c)))
def pr_track(img, th, shown, cur=None, prog=1.0, y=1000, a=1.0):
    d = ImageDraw.Draw(img); acc2 = tuple(th["accent2"])
    d.line([(PR_X0, y), (PR_X1, y)], fill=(60, 70, 110), width=6)
    R.paste_c(img, R.sun_sprite(9), PR_X0, y); d = ImageDraw.Draw(img)
    for au, lab in [(30.1, "Neptune"), (121, "Sun's bubble ends")]:
        x = pr_x(au); d.line([(x, y - 70), (x, y + 70)], fill=(120, 125, 160), width=3)
        d.text((x, y + 92), lab, font=F(24, "Bold"), fill=(160, 165, 195), anchor="mm")
    for au in (1, 10, 50, 100, 150):
        x = pr_x(au); d.line([(x, y - 12), (x, y + 12)], fill=(110, 115, 150), width=2)
        d.text((x, y - 32), f"{au} AU", font=F(20, "SemiBold"), fill=(120, 125, 160), anchor="mm")
    for o in shown:
        v = o["vis"]; au = v["au"] * (prog if o is cur else 1.0); x = pr_x(au); col = tuple(v["col"])
        r = 16 if o is cur else 10; d.ellipse([x - r, y - r, x + r, y + r], fill=col, outline=(255, 255, 255), width=3)
        if o is not cur: d.text((x, y + 124 + {5: 0, 4: 26, 3: 52, 2: 78}.get(o["rank"], 0)), o["short"], font=F(24, "ExtraBold"), fill=col, anchor="mm")
    d.text((PR_X1, y - 70), "square-root scale", font=F(22, "SemiBold"), fill=(120, 125, 160), anchor="rm")
def probes_vis(img, it, th, t, dur):
    v = it["vis"]; col = tuple(v["col"]); acc2 = tuple(th["accent2"])
    prog = easeio((t - 0.4) / max(1.2, dur * 0.6))
    pr_icon(img, v["kind"], W / 2, 590, 1.9, ang=0.15 * math.sin(t * 0.8))
    lt = v["au"] * prog * 499.0 / 3600
    text(img, (W / 2, 790), f"light needs {lt:.1f} hours to get there", 38, (255, 255, 255), w="ExtraBold", a=ease((t - 0.4) / 0.4))
    alive = v.get("alive", True)
    pill = "STILL TALKING TO EARTH" if alive else v.get("silent", "SILENT")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    w_ = F(30, "Black").getlength(pill) + 60; pc = (90, 230, 150) if alive else (150, 150, 165)
    dl.rounded_rectangle([W / 2 - w_ / 2, 850, W / 2 + w_ / 2, 905], 28, fill=pc + (60,), outline=pc + (255,), width=3); img.alpha_composite(lay)
    text(img, (W / 2, 878), pill, 30, pc)
    pr_track(img, th, [o for o in ALL_ITEMS if o["rank"] > it["rank"]] + [it], cur=it, prog=prog, y=1000)
    if v.get("note"): text(img, (W / 2, 1300), v["note"], 36, acc2, w="ExtraBold", a=ease((t - 1.4) / 0.5))

# ---- rank16: biggest asteroids ----
RK_K = 0.72  # px per km
_rk = {}
def rk_rock(km, lump, col, seed, spot=False):
    """lumpy asteroid sprite EM ESCALA (RK_K px/km): noisy outline + lit shading + craters; spot = Ceres' bright Occator spots"""
    key = (km, lump, col, seed, spot)
    if key in _rk: return _rk[key]
    r = km / 2 * RK_K; S = int(r * 2.6) + 8; c = S / 2
    rng = random.Random(seed); harm = [(rng.uniform(0, 6.283), rng.uniform(0.4, 1.0) / (k ** 1.2)) for k in range(2, 7)]
    yy, xx = np.mgrid[0:S, 0:S].astype(np.float32); dx, dy = xx - c, yy - c; ang = np.arctan2(dy, dx); d = np.sqrt(dx * dx + dy * dy)
    rad = np.ones_like(ang)
    for k, (ph, am) in enumerate(harm, start=2): rad += lump * am * np.cos(k * ang + ph)
    rr = r * rad; inside = d <= rr
    nz = np.clip(-(dx / r) * 0.6 - (dy / r) * 0.5 + 0.55, 0.15, 1.2)
    base = np.array(col, np.float32)
    out = np.zeros((S, S, 4), np.float32); out[..., :3] = base * nz[..., None]; out[..., 3] = inside * 255
    im = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA"); dd = ImageDraw.Draw(im)
    for i in range(int(14 + r / 12)):
        a_ = rng.uniform(0, 6.283); q = rng.uniform(0, 0.8) * r; cr = rng.uniform(0.03, 0.14) * r
        x, y = c + q * math.cos(a_), c + q * math.sin(a_)
        dd.ellipse([x - cr, y - cr, x + cr, y + cr], fill=tuple(int(v * 0.6) for v in col) + (150,), outline=tuple(min(255, int(v * 1.25)) for v in col) + (120,), width=max(1, int(cr * 0.15)))
    if spot:
        dd.ellipse([c - r * 0.05, c - r * 0.25, c + r * 0.05, c - r * 0.15], fill=(255, 255, 250, 255)); dd.ellipse([c + r * 0.07, c - r * 0.2, c + r * 0.11, c - r * 0.16], fill=(240, 240, 235, 255))
    al = np.array(im.getchannel("A")); al[~inside] = 0; im.putalpha(Image.fromarray(al))
    _rk[key] = im; return im

def rocks_vis(img, it, th, t, dur):
    v = it["vis"]; acc2 = tuple(th["accent2"])
    g = ease((t - 0.2) / 0.8)
    spr = rk_rock(v["km"], v["lump"], tuple(v["col"]), v.get("seed", 1), v.get("spot", False))
    rot = spr.rotate(t * 6, resample=Image.BICUBIC)
    R.paste_c(img, rot, W / 2, 740, g)
    d = ImageDraw.Draw(img); r = v["km"] / 2 * RK_K
    # 100 km scale bar
    d.line([(W - 120 - 100 * RK_K, 470), (W - 120, 470)], fill=(230, 230, 240), width=6); d.text((W - 120 - 50 * RK_K, 440), "100 km", font=F(28, "Bold"), fill=(230, 230, 240), anchor="mm")
    hrs = math.pi * v["km"] / 100 * ease((t - 0.6) / max(1.0, dur * 0.5))
    text(img, (W / 2, 1140), f"driving around it at 100 km/h: {hrs:.0f} h", 40, (255, 255, 255), w="ExtraBold", a=ease((t - 0.5) / 0.4), stroke=3)
    if v.get("note"): text(img, (W / 2, 1290), v["note"], 38, acc2, w="ExtraBold", a=ease((t - 1.2) / 0.5), stroke=3)


# ---------- rank17: "weigh" (balance beam in Earth masses) ----------
WG_LOG = (0, 6)  # log10 Earth masses on the ruler: 1 -> 1,000,000
def wg_body(img, kind, col, cx, cy, r, t):
    if kind == "sun": R.paste_c(img, R.sun_sprite(int(r / 1.0)).resize((int(r * 4), int(r * 4))), cx, cy); return
    R.paste_c(img, R.planet_sprite(int(r), tuple(col), light=(-0.9, -0.4)), cx, cy)
    d = ImageDraw.Draw(img)
    if kind == "gas":  # a few bands
        for k in (-0.45, -0.15, 0.2, 0.5):
            w = r * math.sqrt(max(0, 1 - k * k)) * 0.95; d.line([(cx - w, cy + k * r), (cx + w, cy + k * r)], fill=tuple(max(0, int(c * 0.78)) for c in col), width=max(2, int(r * 0.08)))
    if kind == "ringed":
        d.ellipse([cx - r * 2.0, cy - r * 0.42, cx + r * 2.0, cy + r * 0.42], outline=(230, 210, 160), width=max(3, int(r * 0.09)))
def wg_ruler(img, th, items, cur=None, y=1200):
    x0, x1 = 110, W - 110; d = ImageDraw.Draw(img)
    def X(m): return lerp(x0, x1, (math.log10(max(1, m)) - WG_LOG[0]) / (WG_LOG[1] - WG_LOG[0]))
    d.line([(x0, y), (x1, y)], fill=(90, 95, 130), width=6)
    for e in range(WG_LOG[0], WG_LOG[1] + 1):
        x = X(10 ** e); d.line([(x, y - 12), (x, y + 12)], fill=(150, 155, 185), width=3)
        d.text((x, y + 40), f"{10 ** e:,}", font=F(24, "Bold"), fill=(150, 155, 185), anchor="mm")
    R.paste_c(img, R.earth_sprite(14, glow=None), X(1), y - 40); d = ImageDraw.Draw(img)
    d.text((x1, y + 78), "Earth masses (log scale)", font=F(26, "SemiBold"), fill=(150, 155, 185), anchor="rm")
    for o in items:
        v = o["vis"]; x = X(v["earths"]); on = cur is None or o is cur
        if cur is not None and o["rank"] < cur["rank"]: continue
        d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=tuple(v["col"]) if on else (110, 110, 130))
        d.text((x, y - 44 - (34 if o["rank"] % 2 == 0 else 0)), f"#{o['rank']}", font=F(30, "Black"), fill=tuple(v["col"]) if on else (130, 130, 150), anchor="mm")
def wg_balance(img, th, left, right_n, t, bp, cy=760, label=None):
    """left = (kind, col, r) body on the left pan; right pan = stack of Earth tokens up to right_n (shown as count); beam levels as bp -> 1"""
    cx = W / 2; L = 380; tilt = 0.32 * (1 - easeio(bp)) + 0.015 * math.sin(t * 3) * (1 - bp)
    lx, ly = cx - L * math.cos(tilt), cy + L * math.sin(tilt); rx, ry = cx + L * math.cos(tilt), cy - L * math.sin(tilt)
    d = ImageDraw.Draw(img)
    d.polygon([(cx, cy), (cx - 60, cy + 470), (cx + 60, cy + 470)], fill=(60, 66, 100)); d.line([(lx, ly), (rx, ry)], fill=(215, 220, 245), width=12)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(255, 255, 255))
    for x, y in ((lx, ly), (rx, ry)):
        d.line([(x, y), (x - 120, y + 160)], fill=(170, 175, 200), width=3); d.line([(x, y), (x + 120, y + 160)], fill=(170, 175, 200), width=3)
        d.arc([x - 140, y + 120, x + 140, y + 200], 0, 180, fill=(215, 220, 245), width=8)
    kind, col, r = left; wg_body(img, kind, col, lx, ly + 160 - r * (0.6 if kind != "sun" else 0.5), r, t)
    n = (right_n ** easeio(bp) if right_n > 1000 else right_n * easeio(bp)); shown = min(28, max(1, int(round(n)) if n < 28 else 28))
    for k in range(shown):
        row, colk = divmod(k, 7); ex = rx - 105 + colk * 35; ey = ry + 150 - row * 32
        R.paste_c(img, R.earth_sprite(15, glow=None), ex, ey)
    text(img, (min(rx, W - 250), ry - 70), f"{n:,.0f} Earths" if n >= 10 else f"{n:,.1f} Earths", 54, tuple(th["accent2"]), stroke=4)
    if label: text(img, (lx, ly + 260), label, 34, (235, 235, 245), w="Bold", stroke=3)
def weigh_vis(img, it, th, t, dur):
    v = it["vis"]; bp = (t - 0.4) / max(1.2, dur * 0.6)
    wg_balance(img, th, (v["kind"], v["col"], v.get("r", 80)), v["earths"], t, max(0, min(1, bp)), cy=600, label=v.get("label"))
    wg_ruler(img, th, ALL_ITEMS, cur=it, y=1170)
    if v.get("note"): text(img, (W / 2, 1290), v["note"], 38, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.2) / 0.5), stroke=3)

# ---------- rank18: "gravity" (a person on a bathroom scale standing on each world) ----------
GV_LOG = (-0.5, 1.6)  # log10 of × Earth's gravity on the ruler: 0.32 -> 40
GV_EARTH = 9.80
def gv_surface(img, kind, col, t, top=1060, a=1.0):
    """the world's surface as a huge curved horizon (radius 1500 px) fading out before the number block"""
    lay = Image.new("RGBA", (W, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); Rr = 1500; cy = Rr
    c = tuple(int(v * 0.55) for v in col)
    d.ellipse([W / 2 - Rr, 0, W / 2 + Rr, 2 * Rr], fill=c + (255,))
    if kind == "gas" or kind == "ringed" or kind == "ice":
        for k in range(6):
            yy = 30 + k * 48 + 6 * math.sin(t * 0.8 + k); d.arc([W / 2 - Rr - 40, yy, W / 2 + Rr + 40, yy + 2 * Rr], 200, 340, fill=tuple(int(v * (0.42 + 0.1 * (k % 2))) for v in col) + (255,), width=18)
    if kind == "sun":
        rng = np.random.default_rng(int(t * 3)); 
        for _ in range(90):
            x, y = rng.uniform(0, W), rng.uniform(20, 380); r = rng.uniform(6, 16)
            if (x - W / 2) ** 2 + (y - cy) ** 2 < Rr ** 2: d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 220, 120, 120))
    if kind == "earth":
        for x0, w in ((60, 260), (560, 380)): d.ellipse([x0, 40, x0 + w, 120], fill=(50, 110, 60, 255))
    al = np.asarray(lay.getchannel("A"), np.float32) * (np.clip((300 - np.arange(420)) / 120, 0, 1)[:, None]) * a
    lay.putalpha(Image.fromarray(al.astype(np.uint8))); img.alpha_composite(lay, (0, top))
    if kind == "sun": R.paste_c(img, R.radial(1400, [(0, (255, 200, 90, 90)), (1, (255, 140, 40, 0))]), W / 2, top + 80, a)
def gv_person(img, x, foot_y, squash, col=(240, 240, 250), lcd="70 kg", lcd_col=(120, 255, 160)):
    """stick person on a bathroom scale; squash 0..1 bends the knees and lowers the body"""
    d = ImageDraw.Draw(img); sw = 230
    d.rounded_rectangle([x - sw / 2, foot_y - 34, x + sw / 2, foot_y + 6], 14, fill=(230, 232, 240), outline=(90, 95, 120), width=3)
    d.rounded_rectangle([x - 52, foot_y - 28, x + 52, foot_y - 6], 5, fill=(20, 30, 26))
    d.text((x, foot_y - 17), lcd, font=F(18, "Black"), fill=lcd_col, anchor="mm")
    fy = foot_y - 36; leg = 120 * (1 - 0.35 * squash); knee_dx = 30 * squash
    hip = fy - leg; d.line([(x - 30, fy), (x - 30 - knee_dx, fy - leg / 2), (x - 12, hip)], fill=col, width=14, joint="curve")
    d.line([(x + 30, fy), (x + 30 + knee_dx, fy - leg / 2), (x + 12, hip)], fill=col, width=14, joint="curve")
    torso = 115 * (1 - 0.12 * squash); sh = hip - torso
    d.line([(x, hip), (x, sh)], fill=col, width=18)
    arm_y = sh + 15 + 40 * squash
    d.line([(x, sh + 12), (x - 55, arm_y + 70)], fill=col, width=12); d.line([(x, sh + 12), (x + 55, arm_y + 70)], fill=col, width=12)
    d.ellipse([x - 32, sh - 70 + 12 * squash, x + 32, sh - 6 + 12 * squash], fill=col)
def gv_ruler(img, th, items, cur=None, y=1290, labels=True, a=1.0):
    x0, x1 = 110, W - 110
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([60, y - 150, W - 60, y + 100], 24, fill=(6, 8, 18, 190)); img.alpha_composite(lay)
    d = ImageDraw.Draw(img)
    def X(g): return lerp(x0, x1, (math.log10(g / GV_EARTH) - GV_LOG[0]) / (GV_LOG[1] - GV_LOG[0]))
    d.line([(x0, y), (x1, y)], fill=(110, 115, 150), width=6)
    for v, lab in ((0.5, "½×"), (1, "1×"), (2, "2×"), (5, "5×"), (10, "10×"), (30, "30×")):
        x = X(v * GV_EARTH); d.line([(x, y - 12), (x, y + 12)], fill=(160, 165, 195), width=3)
        d.text((x, y + 36), lab, font=F(26, "Bold"), fill=(160, 165, 195), anchor="mm")
    x = X(8.87); d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(110, 110, 130))
    if labels: d.text((x - 16, y + 68), "Venus, Uranus", font=F(22, "Bold"), fill=(130, 130, 150), anchor="rm")
    for o in items:
        if cur is not None and o["rank"] < cur["rank"]: continue
        v = o["vis"]; x = X(v["g"]); on = cur is None or o is cur
        d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=tuple(v["col"]) if on else (120, 120, 140))
        dy, dx = {5: (-44, -34), 4: (-82, 0), 3: (-120, 34)}.get(o["rank"], (-44, 0))
        d.text((x + dx, y + dy), f"#{o['rank']}", font=F(30, "Black"), fill=tuple(v["col"]) if on else (140, 140, 160), anchor="mm")
    d.text((x1, y + 74), "gravity, × Earth's (log scale)", font=F(24, "SemiBold"), fill=(150, 155, 185), anchor="rm")
def gravity_vis(img, it, th, t, dur):
    v = it["vis"]; bp = max(0.0, min(1.0, (t - 0.4) / max(1.2, dur * 0.55))); r = v["g"] / GV_EARTH
    gv_surface(img, v["kind"], tuple(v["col"]), t)
    kg = 70 * (1 + (r - 1) * easeio(bp))
    sq = min(1.0, math.log10(1 + (r - 1) * easeio(bp)) / math.log10(28)) if r > 1 else 0.0
    gv_person(img, W / 2, 1078, sq, lcd=f"{kg:,.0f} kg")
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([W / 2 - 250, 430, W / 2 + 250, 560], 24, fill=(14, 22, 18, 230), outline=(120, 255, 160, 200), width=4); img.alpha_composite(lay)
    text(img, (W / 2, 495), f"{kg:,.0f} kg", 96, (120, 255, 160))
    text(img, (W / 2, 600), "a 70 kg person on the scale", 34, (220, 225, 240), w="Bold", stroke=3)
    if v.get("note"): text(img, (W / 2, 660), v["note"], 36, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.2) / 0.5), stroke=3)
    gv_ruler(img, th, ALL_ITEMS, cur=it, y=1250)

# ---------- rank19: "litre" (one litre of each planet, poured into a jar on a kitchen scale) ----------
LT_MAX = 6.0  # kg per litre on the bar
def lt_jar(img, cx, base_y, fill_col, fill=1.0, t=0.0, w=230, h=300, label=None, a=1.0, swirl=True):
    """code-drawn glass jar (1 litre) on a scale plate; filled with the planet's average stuff (banded layers)"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x0, x1, y1 = cx - w / 2, cx + w / 2, base_y; y0 = y1 - h
    top = y1 - h * 0.92 * max(0.0, min(1.0, fill))
    if fill > 0 and top < y1 - 30:
        c = tuple(fill_col)
        d.rounded_rectangle([x0 + 10, top, x1 - 10, y1 - 8], 18, fill=c + (int(240 * a),))
        for k in range(6):  # strata / swirls inside the jar
            yy = top + (y1 - top) * (k + 0.5) / 6 + (5 * math.sin(t * 1.3 + k) if swirl else 0)
            if yy < top + 6: continue
            cc = tuple(int(v * (0.72 if k % 2 else 1.15)) for v in c); cc = tuple(min(255, v) for v in cc)
            d.line([(x0 + 14, yy), (x1 - 14, yy + 6 * math.sin(k))], fill=cc + (int(170 * a),), width=10)
    d.rounded_rectangle([x0, y0, x1, y1], 26, outline=(220, 235, 255, int(230 * a)), width=6)
    d.rectangle([x0 + 20, y0 - 30, x1 - 20, y0 + 4], fill=(150, 160, 190, int(255 * a)))  # lid
    d.line([(x0 + 22, y0 + 30), (x0 + 22, y1 - 40)], fill=(255, 255, 255, int(110 * a)), width=8)  # glass glint
    img.alpha_composite(lay)
    if label: text(img, (cx, y0 - 70), label, 40, (240, 240, 250), w="ExtraBold", a=a, stroke=3)
def lt_scale(img, cx, y, lcd, lcd_col=(120, 255, 160), w=360, a=1.0):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([cx - w / 2, y, cx + w / 2, y + 110], 22, fill=(225, 228, 238, int(255 * a)), outline=(90, 95, 120, int(255 * a)), width=4)
    d.rounded_rectangle([cx - w * 0.3, y + 28, cx + w * 0.3, y + 92], 10, fill=(20, 28, 24, int(255 * a)))
    img.alpha_composite(lay)
    text(img, (cx, y + 61), lcd, 50 if w > 300 else 34, lcd_col, a=a)
def lt_bar(img, th, items, cur=None, y=1215, a=1.0, labels=True):
    x0, x1 = 120, W - 120
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([60, y - 120, W - 60, y + 95], 24, fill=(6, 8, 18, int(190 * a))); img.alpha_composite(lay)
    d = ImageDraw.Draw(img)
    def X(v): return lerp(x0, x1, v / LT_MAX)
    d.line([(x0, y), (x1, y)], fill=(110, 115, 150), width=6)
    for v in range(0, 7):
        d.line([(X(v), y - 10), (X(v), y + 10)], fill=(160, 165, 195), width=3); d.text((X(v), y + 34), f"{v}", font=F(26, "Bold"), fill=(160, 165, 195), anchor="mm")
    xw = X(1.0); d.line([(xw, y - 60), (xw, y + 10)], fill=(90, 160, 255), width=4)
    if labels: d.text((xw + 10, y - 68), "water", font=F(24, "Bold"), fill=(110, 170, 255), anchor="lm")
    xs = X(0.687); d.ellipse([xs - 8, y - 8, xs + 8, y + 8], fill=(225, 200, 150))
    if labels: d.text((xs, y + 66), "Saturn", font=F(22, "Bold"), fill=(225, 200, 150), anchor="mm")
    for o in items:
        if cur is not None and o["rank"] < cur["rank"]: continue
        v = o["vis"]; x = X(v["kgl"]); on = cur is None or o is cur
        d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=tuple(v["col"]) if on else (120, 120, 140))
        dy = {5: -44, 4: -92, 3: -44, 2: -92, 1: -44}.get(o["rank"], -44)
        d.text((x, y + dy), f"#{o['rank']}", font=F(28, "Black"), fill=tuple(v["col"]) if on else (140, 140, 160), anchor="mm")
    d.text((x1, y + 72), "kilograms per litre, planet average", font=F(24, "SemiBold"), fill=(150, 155, 185), anchor="rm")
def litre_vis(img, it, th, t, dur):
    v = it["vis"]; bp = max(0.0, min(1.0, (t - 0.3) / max(1.2, dur * 0.5)))
    jx, base = W / 2 + 130, 880
    # pour stream from above while filling
    if bp < 1:
        d = ImageDraw.Draw(img); d.line([(jx, 430), (jx, base - 300 * 0.92 * easeio(bp))], fill=tuple(v["col"]), width=22)
    lt_jar(img, jx, base, v["col"], easeio(bp), t, label="1 litre of " + it["name"])
    lt_scale(img, jx, base + 6, f"{v['kgl'] * easeio(bp):.2f} kg")
    # reference: a 1-litre bottle of water, always 1.00 kg
    bx = 210
    lt_jar(img, bx, base, (70, 130, 230), 1.0, t, w=140, h=210, label="1 litre of water", swirl=False)
    lt_scale(img, bx, base + 6, "1.00 kg", lcd_col=(140, 190, 255), w=220)
    if v.get("note"): text(img, (W / 2, 1035), v["note"], 38, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 1.0) / 0.5), stroke=3)
    lt_bar(img, th, ALL_ITEMS, cur=it, y=1180, labels=False)


# ---------- rank20: "beads" (Earths strung like beads across each planet's diameter, one common scale) ----------
BD_K = 430 / 71492  # px per km: Jupiter's equatorial radius = 430 px; every item uses this same scale
_bd = {}
def bd_body(kind, r, col):
    key = (kind, int(r), tuple(col))
    if key not in _bd:
        if kind == "jupiter":
            base = R.jup10(500, 0.0); k = r / 500.0; _bd[key] = base.resize((int(base.width * k), int(base.height * k)), Image.BILINEAR)
        elif kind == "earth": _bd[key] = R.earth_sprite(max(3, int(r)))
        else: _bd[key] = R.planet_sprite(max(3, int(r)), tuple(col))
    return _bd[key]
def bd_planet(img, kind, col, cx, cy, r, a=1.0):
    if kind == "ringed":  # back half of the rings, planet, front half
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for k in range(5):
            rr = r * (1.35 + k * 0.12); d.arc([cx - rr, cy - rr * 0.28, cx + rr, cy + rr * 0.28], 180, 360, fill=(220, 200, 160, int(170 * a)), width=7)
        img.alpha_composite(lay)
    R.paste_c(img, bd_body(kind, r, col), cx, cy, a)
    if kind == "ringed":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        for k in range(5):
            rr = r * (1.35 + k * 0.12); d.arc([cx - rr, cy - rr * 0.28, cx + rr, cy + rr * 0.28], 0, 180, fill=(235, 215, 170, int(200 * a)), width=7)
        img.alpha_composite(lay)
def beads_vis(img, it, th, t, dur):
    """the planet TO A COMMON SCALE (Jupiter r = 430 px), then Earths (same scale, 37.8 px wide... r = 38 px) drop in one by one along a
    string across its equator; the counter climbs to vis.earths; a ghost outline of Jupiter shows how far the smaller ones are from #1"""
    v = it["vis"]; acc = tuple(th["accent"]); cx, cy = W / 2, 820
    r = v["km"] / 2 * BD_K; er = 12756 / 2 * BD_K
    d = ImageDraw.Draw(img)
    rj = 71492 * BD_K
    if v["km"] < 140000:
        for k in range(0, 360, 8): d.arc([cx - rj, cy - rj, cx + rj, cy + rj], k, k + 4, fill=(120, 120, 150), width=3)
        d.text((cx, cy - rj - 22), "#1's size", font=F(26, "Bold"), fill=(140, 140, 170), anchor="mm")
    bd_planet(img, v["kind"], v["col"], cx, cy, r, ease(t / 0.4))
    p = max(0.0, min(1.0, (t - 0.7) / max(1.0, dur * 0.55))); n = v["earths"] * p
    d = ImageDraw.Draw(img); d.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=3)
    full = int(n); whole = int(v["earths"] + 1e-6)
    for i in range(min(whole, full + 1) if v.get("kind") != "earth" else 0):
        x = cx - r + er + i * 2 * er; drop = 0 if i < full else (1 - (n - full)) * 160
        R.paste_c(img, bd_body("earth", er, (0, 0, 0)), x, cy - drop)
    if v.get("kind") == "earth":
        vr = 12104 / 2 * BD_K; d = ImageDraw.Draw(img)
        d.ellipse([cx + 160 - vr, cy - vr, cx + 160 + vr, cy + vr], fill=(220, 190, 130)); d.text((cx + 160, cy + vr + 30), "Venus", font=F(30, "Bold"), fill=(230, 200, 150), anchor="mm")
        R.paste_c(img, bd_body("earth", er, (0, 0, 0)), cx, cy); d = ImageDraw.Draw(img)
        d.text((cx, cy + er + 30), "Earth", font=F(30, "Bold"), fill=(140, 190, 255), anchor="mm")
    text(img, (W / 2, 1220), f"{n:.2f} Earths wide" if v["earths"] > 1.01 else "1 Earth wide", 54, tuple(th["accent2"]), w="ExtraBold", a=ease((t - 0.6) / 0.3), stroke=4)
    if v.get("note"): text(img, (W / 2, 1290), v["note"], 36, (235, 235, 245), w="Bold", a=ease((t - 1.2) / 0.4), stroke=3)

# ---- rank21: "tilt" — axial tilt. The planet (banded, rotated by its obliquity) sits on a horizontal orbit-plane line; a dashed vertical
# line = "straight up" (0°), a protractor arc sweeps from vertical to the spin axis while the degree counter climbs; Earth's 23.4° is a
# ghost axis for reference; vis.retro = spins backward (curved arrow flips); vis.kind = gas | ice | rock | ringed.
_tl = {}
def tl_body(kind, r, col):
    key = (kind, int(r), tuple(col))
    if key not in _tl:
        spr = R.planet_sprite(max(4, int(r)), tuple(col), light=(-0.7, -0.5)).copy()
        w, h = spr.size; cx, cy = w / 2, h / 2
        band = Image.new("RGBA", spr.size, (0, 0, 0, 0)); d = ImageDraw.Draw(band)
        nb = {"gas": 9, "ringed": 7, "ice": 3, "rock": 0}.get(kind, 4)
        for i in range(nb):
            y = cy - r + (i + 0.6) * 2 * r / (nb + 0.4)
            dark = tuple(int(c * (0.72 if i % 2 else 1.12)) for c in col)
            d.rectangle([0, y - r * 0.06, w, y + r * 0.06], fill=tuple(min(255, c) for c in dark) + (110,))
        m = Image.new("L", spr.size, 0); ImageDraw.Draw(m).ellipse([cx - r + 2, cy - r + 2, cx + r - 2, cy + r - 2], fill=255)
        bb = Image.new("RGBA", spr.size, (0, 0, 0, 0)); bb.paste(band, (0, 0), m); spr.alpha_composite(bb)
        if kind == "rock":  # polar cap
            dd = ImageDraw.Draw(spr); dd.ellipse([cx - r * 0.35, cy - r * 0.98, cx + r * 0.35, cy - r * 0.78], fill=(245, 245, 250, 220))
        _tl[key] = spr
    return _tl[key]
def tl_planet(img, kind, col, cx, cy, r, deg, spin, a=1.0, axis=True, retro=False):
    """planet tilted by deg (clockwise from straight up), spin = phase for the moving surface marker"""
    big = Image.new("RGBA", (int(r * 4.2), int(r * 4.2)), (0, 0, 0, 0)); bc = big.width / 2
    d = ImageDraw.Draw(big)
    if kind == "ringed":
        for k in range(4):
            rr = r * (1.4 + k * 0.13); d.arc([bc - rr, bc - rr * 0.22, bc + rr, bc + rr * 0.22], 180, 360, fill=(225, 205, 160, 190), width=max(2, int(r * 0.05)))
    if axis: d.line([(bc, bc - r * 1.75), (bc, bc + r * 1.75)], fill=(255, 255, 255, 230), width=max(3, int(r * 0.04)))
    spr = tl_body(kind, r, col); big.alpha_composite(spr, (int(bc - spr.width / 2), int(bc - spr.height / 2)))
    d = ImageDraw.Draw(big)
    # moving surface marker shows the spin direction (sped up)
    ph = (spin * (-1 if retro else 1)) % 1.0; x = bc + r * 0.85 * math.sin(2 * math.pi * ph)
    if math.cos(2 * math.pi * ph) > 0: d.ellipse([x - r * 0.08, bc - r * 0.08, x + r * 0.08, bc + r * 0.08], fill=(255, 255, 255, 200))
    if kind == "ringed":
        for k in range(4):
            rr = r * (1.4 + k * 0.13); d.arc([bc - rr, bc - rr * 0.22, bc + rr, bc + rr * 0.22], 0, 180, fill=(240, 220, 175, 220), width=max(2, int(r * 0.05)))
    if axis:
        d.line([(bc, bc - r * 1.75), (bc, bc - r * 1.02)], fill=(255, 255, 255, 240), width=max(3, int(r * 0.04)))
        d.polygon([(bc, bc - r * 1.92), (bc - r * 0.1, bc - r * 1.72), (bc + r * 0.1, bc - r * 1.72)], fill=(255, 255, 255, 240))
        d.text((bc + r * 0.14, bc - r * 1.8), "N", font=F(max(18, int(r * 0.18)), "Black"), fill=(255, 255, 255, 230), anchor="lm")
    big = big.rotate(-deg, resample=Image.BICUBIC)
    R.paste_c(img, big, cx, cy, a)
def tl_arc(img, cx, cy, rad, deg, col, a=1.0, label=True):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for k in range(0, 40):  # dashed vertical "straight up" reference
        y0 = cy - rad * 1.15 + k * rad * 2.3 / 40
        if k % 2 == 0: d.line([(cx, y0), (cx, y0 + rad * 2.3 / 80)], fill=(200, 205, 230, int(160 * a)), width=3)
    if deg > 0.3: d.arc([cx - rad, cy - rad, cx + rad, cy + rad], -90, -90 + deg, fill=col + (int(255 * a),), width=10)
    img.alpha_composite(lay)
def tl_ghost(img, cx, cy, L, deg, col=(120, 190, 255), a=1.0):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    s, c = math.sin(math.radians(deg)), math.cos(math.radians(deg))
    for k in range(16):
        f0, f1 = -1 + k * 2 / 16, -1 + (k + 0.5) * 2 / 16
        d.line([(cx + s * L * f0, cy - c * L * f0), (cx + s * L * f1, cy - c * L * f1)], fill=col + (int(200 * a),), width=4)
    img.alpha_composite(lay)
    text(img, (cx - s * L - 20, cy + c * L + 10), "Earth 23.4°", 30, col, w="Bold", a=a, anchor="rm", stroke=3)
def tilt_vis(img, it, th, t, dur):
    v = it["vis"]; acc = tuple(th["accent"]); cx, cy = W / 2, 830; r = v.get("r", 230)
    d = ImageDraw.Draw(img)
    d.line([(60, cy), (W - 60, cy)], fill=(150, 160, 200), width=3)
    d.text((W - 70, cy + 26), "orbit plane", font=F(26, "SemiBold"), fill=(150, 160, 200), anchor="rm")
    p = easeio((t - 0.5) / max(1.2, dur * 0.5)); deg = v["deg"] * p
    tl_arc(img, cx, cy, r * 1.55, deg, acc)
    if v["deg"] > 30 or v.get("ghost"): tl_ghost(img, cx, cy, r * 1.6, 23.44, a=ease((t - 0.3) / 0.4))
    tl_planet(img, v["kind"], tuple(v["col"]), cx, cy, r, deg, t * 0.35, ease(t / 0.35), retro=v.get("retro", False))
    text(img, (W - 190, 470), f"{deg:.1f}°", 72, acc, a=ease((t - 0.4) / 0.3), stroke=4)
    text(img, (W - 190, 525), "from straight up", 26, (200, 205, 230), w="SemiBold", a=ease((t - 0.4) / 0.3), stroke=2)
    if v.get("note"): text(img, (W / 2, 1265), v["note"], 38, (235, 235, 245), w="Bold", a=ease((t - 1.4) / 0.4), stroke=3)

# ---- rank22: "pair" — each moon next to its own planet; the planet is always the same size, so the moon's size IS the ratio.
PA_R = 300
_pa = {}
def pa_body(kind, r, col):
    key = (kind, int(r), tuple(col))
    if key not in _pa:
        if kind == "gas": _pa[key] = tl_body("gas", r, col)
        elif kind == "ringed": _pa[key] = tl_body("ringed", r, col)
        elif kind == "earth": _pa[key] = R.earth_sprite(max(3, int(r)), glow=None)
        elif kind == "ice": _pa[key] = tl_body("ice", r, col)
        elif kind == "moon": _pa[key] = R.moon8(max(4, int(r)))
        else: _pa[key] = R.planet_sprite(max(3, int(r)), tuple(col), light=(-0.7, -0.5))
    return _pa[key]
def pa_pair(img, v, cx, cy, rp, q, t, a=1.0, label=True):
    """planet of radius rp at (cx, cy); moon slides out to its right by q (0..1)"""
    rm = rp * v["ratio"]
    mx = lerp(cx + rp * 0.2, cx + rp + rm + rp * 0.18, q); my = cy + (1 - q) * rp * 0.1
    if q < 0.5: R.paste_c(img, pa_body(v.get("mkind", "rock"), rm, tuple(v.get("mcol", (190, 185, 180)))), mx, my, a * ease(q * 4))
    if v["kind"] == "ringed": bd_planet(img, "ringed", tuple(v["col"]), cx, cy, rp, a) if rp > 200 else R.paste_c(img, pa_body("ringed", rp, tuple(v["col"])), cx, cy, a)
    else: R.paste_c(img, pa_body(v["kind"], rp, tuple(v["col"])), cx, cy, a)
    if q >= 0.5: R.paste_c(img, pa_body(v.get("mkind", "rock"), rm, tuple(v.get("mcol", (190, 185, 180)))), mx, my, a)
    return mx, my, rm
def pa_bar(img, th, items, cur=None, y=1200, a=1.0):
    d = ImageDraw.Draw(img); x0, x1 = 110, W - 110; mx_ = 0.6
    d.line([(x0, y), (x1, y)], fill=(150, 160, 200), width=4)
    for pc in (0, 10, 20, 30, 40, 50, 60):
        x = lerp(x0, x1, pc / 100 / mx_); d.line([(x, y - 10), (x, y + 10)], fill=(150, 160, 200), width=2)
        d.text((x, y + 34), f"{pc}%", font=F(26, "SemiBold"), fill=(150, 160, 200), anchor="mm")
    for o in items:
        v = o["vis"]; x = lerp(x0, x1, v["ratio"] / mx_); c = tuple(v.get("mcol", th["accent"])) if o is not cur else tuple(th["accent"])
        d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=c)
        d.text((x + {5: -22, 4: 0, 3: 22}.get(o["rank"], 0), y - 40 - {5: 0, 4: 30, 3: 0}.get(o["rank"], 0)), f"#{o['rank']}", font=F(30, "Black"), fill=c, anchor="mm")
def pair_vis(img, it, th, t, dur):
    v = it["vis"]; acc = tuple(th["accent"]); cx, cy = 400, 790
    q = easeio((t - 0.4) / max(1.0, dur * 0.45))
    mx, my, rm = pa_pair(img, v, cx, cy, PA_R, q, t, ease(t / 0.35))
    d = ImageDraw.Draw(img)
    d.line([(cx - PA_R, cy + PA_R + 40), (cx + PA_R, cy + PA_R + 40)], fill=tuple(v["col"]), width=5)
    d.text((cx, cy + PA_R + 78), v.get("pname", ""), font=F(34, "ExtraBold"), fill=tuple(v["col"]), anchor="mm")
    if q > 0.5:
        d.line([(mx - rm, my + PA_R + 40), (mx + rm, my + PA_R + 40)], fill=acc, width=5)
        text(img, (mx, my - rm - 46), v.get("mname", ""), 38, acc, w="ExtraBold", stroke=3)
    pa_bar(img, th, [o for o in ALL_ITEMS if o["rank"] >= it["rank"]], cur=it, y=1240, a=ease((t - 0.8) / 0.4))
    if v.get("note"): text(img, (W / 2, 560), v["note"], 36, (235, 235, 245), w="Bold", a=ease((t - 1.6) / 0.4), stroke=3)

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
    if th.get("hook") == "pair":
        # frame 0: big number + a dark planet with a "?" moon half its width bobbing next to it
        cx, cy = 400, 900; R.paste_c(img, R.planet_sprite(PA_R, (60, 55, 85), light=(-0.7, -0.5)), cx, cy)
        rm = PA_R * 0.51; mx = cx + PA_R + rm + 50; my = cy + 14 * math.sin(t * 2.4)
        d = ImageDraw.Draw(img); d.ellipse([mx - rm, my - rm, mx + rm, my + rm], fill=(40, 36, 60), outline=tuple(th["accent"]), width=6)
        text(img, (mx, my), "?", 160, tuple(th["accent"]), stroke=4)
        d.line([(cx - PA_R, cy + PA_R + 40), (cx + PA_R, cy + PA_R + 40)], fill=(160, 150, 200), width=5)
        d.line([(mx - rm, cy + PA_R + 40), (mx + rm, cy + PA_R + 40)], fill=tuple(th["accent"]), width=5)
        text(img, (W / 2, 220), sc.get("big", ""), 150, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 340), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1420), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "tilt":
        # frame 0: the big number + a dark "?" planet whose axis swings back and forth, ending upside down; Earth's 23.4° ghost
        cx, cy = W / 2, 930; d = ImageDraw.Draw(img); d.line([(60, cy), (W - 60, cy)], fill=(150, 160, 200), width=3)
        deg = 177.4 + 4 * math.sin(t * 2.2)
        tl_ghost(img, cx, cy, 400, 23.44)
        tl_arc(img, cx, cy, 340, deg, tuple(th["accent"]))
        tl_planet(img, "rock", (70, 60, 95), cx, cy, 210, deg, t * 0.4)
        text(img, (cx, cy), "?", 200, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 220), sc.get("big", ""), 150, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 340), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1420), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "beads":
        # frame 0: the big number + Jupiter-sized "?" disc with a row of Earths already strung across it
        cx, cy = W / 2, 930; rj = 71492 * BD_K * 0.92; er = 12756 / 2 * BD_K * 0.92
        d = ImageDraw.Draw(img); d.ellipse([cx - rj, cy - rj, cx + rj, cy + rj], fill=(40, 30, 50), outline=tuple(th["accent"]), width=6)
        n = 11.2
        for i in range(11):
            R.paste_c(img, bd_body("earth", er, (0, 0, 0)), cx - rj + er + i * 2 * er, cy + 10 * math.sin(t * 6 + i))
        text(img, (cx, cy - rj * 0.5), "?", 190, tuple(th["accent"]))
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1460), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "litre":
        # frame 0: the big number + an empty jar on a scale whose display races, a "?" inside, water bottle for reference
        lt_jar(img, W / 2 + 130, 960, (60, 55, 80), 0.0, t, label="1 litre of ?")
        text(img, (W / 2 + 130, 800), "?", 200, tuple(th["accent"]))
        lt_scale(img, W / 2 + 130, 966, f"{(t * 9.7) % 6:.2f} kg" if int(t * 3) % 2 else "? ? ?", lcd_col=(255, 120, 120))
        lt_jar(img, 210, 960, (70, 130, 230), 1.0, t, w=140, h=210, label="water", swirl=False)
        lt_scale(img, 210, 966, "1.00 kg", lcd_col=(140, 190, 255), w=220)
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1300), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "gravity":
        # frame 0: the big number + a person on a scale over a dark unknown surface, the display flickering "????"
        gv_surface(img, "gas", (60, 55, 80), t)
        gv_person(img, W / 2, 1078, 0.6, lcd="? ? ?", lcd_col=(255, 120, 120))
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([W / 2 - 250, 430, W / 2 + 250, 560], 24, fill=(14, 22, 18, 230), outline=(255, 120, 120, 200), width=4); img.alpha_composite(lay)
        text(img, (W / 2, 495), f"{int(1000 + 957 * ((t * 7) % 1)):,} kg" if int(t * 3) % 2 else "? ? ?", 96, (255, 120, 120))
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1300), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "weigh":
        # frame 0: the big number + Earth alone on one pan, a "?" on the heavy pan (beam tipped hard)
        cx, cy, L, tilt = W / 2, 760, 380, -0.32
        d = ImageDraw.Draw(img); lx, ly = cx - L * math.cos(tilt), cy + L * math.sin(tilt); rx, ry = cx + L * math.cos(tilt), cy - L * math.sin(tilt)
        d.polygon([(cx, cy), (cx - 60, cy + 470), (cx + 60, cy + 470)], fill=(60, 66, 100)); d.line([(lx, ly), (rx, ry)], fill=(215, 220, 245), width=12)
        for x, y in ((lx, ly), (rx, ry)):
            d.line([(x, y), (x - 120, y + 160)], fill=(170, 175, 200), width=3); d.line([(x, y), (x + 120, y + 160)], fill=(170, 175, 200), width=3)
            d.arc([x - 140, y + 120, x + 140, y + 200], 0, 180, fill=(215, 220, 245), width=8)
        d.text((lx, ly + 90), "?", font=F(200, "Black"), fill=tuple(th["accent"]), anchor="mm")
        R.paste_c(img, R.earth_sprite(40, glow=None), rx, ry + 150)
        text(img, (rx, ry + 250), "Earth", 40, (140, 200, 255), stroke=3)
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1360), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "rocks":
        # frame 0: the big number + Ceres already on screen to scale (as a dark silhouette with a "?"), a 100 km bar for scale
        o = [x for x in ALL_ITEMS if x["rank"] == 1][0]; v = o["vis"]
        spr = rk_rock(v["km"], v["lump"], (60, 55, 70), v.get("seed", 1)); R.paste_c(img, spr.rotate(t * 6, resample=Image.BICUBIC), W / 2, 820)
        d = ImageDraw.Draw(img); d.text((W / 2, 820), "?", font=F(240, "Black"), fill=tuple(th["accent"]), anchor="mm")
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1300), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "probes":
        # frame 0: the big number + the Sun-to-#1 track drawn, a light pulse running along it toward a "?"
        y = 1000; d = ImageDraw.Draw(img)
        d.line([(PR_X0, y), (PR_X1, y)], fill=(60, 70, 110), width=6); R.paste_c(img, R.sun_sprite(9), PR_X0, y)
        px = lerp(PR_X0, PR_X1, (0.25 + t * 0.4) % 1.0)
        R.paste_c(img, R.radial(80, [(0, (255, 255, 255, 255)), (0.4, tuple(th["accent2"]) + (200,)), (1, tuple(th["accent2"]) + (0,))]), px, y)
        d = ImageDraw.Draw(img); d.text((PR_X1 - 10, y - 110), "?", font=F(150, "Black"), fill=tuple(th["accent"]), anchor="mm")
        pr_icon(img, "voyager", PR_X1 - 40, y + 20, 0.5, a=0.5)
        d = ImageDraw.Draw(img); d.text((px, y - 50), "light", font=F(30, "Black"), fill=tuple(th["accent2"]), anchor="mm")
        text(img, (W / 2, 640), "Sun  →  #1", 64, (255, 255, 255))
        text(img, (W / 2, 720), "even at 300,000 km every second", 38, (200, 205, 225), w="Bold")
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1320), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "orbityear":
        # frame 0: the big number + Sedna's long orbit already drawn, the world crawling far out, a "?" on it
        o = [x for x in ALL_ITEMS if x["rank"] == 1][0]; v = o["vis"]
        wx, wy = oy_orbit(img, W / 2, 860, v["a"], v["e"], 0.5 + 0.02 * t, tuple(v["col"]), span=900, ang=v.get("ang", 0.5), trail=False)
        d = ImageDraw.Draw(img); d.text((wx, wy - 90), "?", font=F(130, "Black"), fill=tuple(th["accent"]), anchor="mm")
        text(img, (W / 2, 220), sc.get("big", ""), 136, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1320), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "crater":
        # frame 0: the big number + the #1 crater already open on the ground (eroded rim), a "?" in the middle, a second streak coming in
        img.alpha_composite(cr_ground(), (0, 860 - 450)); cr_crater(img, W / 2, 860, 160, 1.0, 0.5)
        d = ImageDraw.Draw(img); d.text((W / 2, 860), "?", font=F(220, "Black"), fill=tuple(th["accent"]), anchor="mm")
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1360), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "wind":
        # frame 0: the big speed + a hot-Jupiter already streaming at full tilt, the "?" over it
        wind_planet(img, W / 2, 860, 300, (90, 120, 200), 33000, t)
        d = ImageDraw.Draw(img); d.text((W / 2, 860), "?", font=F(220, "Black"), fill=tuple(th["accent"]), anchor="mm")
        text(img, (W / 2, 220), sc.get("big", ""), 126, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 52, (255, 255, 255))
        text(img, (W / 2, 1300), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
    if th.get("hook") == "spin":
        # frame 0: the big number + a pulsar already sweeping its beams (slowed down) + the "?" over the meter
        spin_obj(img, "pulsar", W / 2, 820, 60, t * 1.8, tuple(th["accent"]))
        text(img, (W / 2, 220), sc.get("big", ""), 140, tuple(th["accent"]), stroke=3)
        text(img, (W / 2, 335), sc["top"].upper(), 56, (255, 255, 255))
        text(img, (W / 2, 1300), sc["sub"], 46, tuple(th["accent2"]), w="ExtraBold")
        return
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
    if v["type"] == "spin":
        spin_vis(img, it, th, t, dur)
    if v["type"] == "wind":
        wind_vis(img, it, th, t, dur)
    if v["type"] == "crater":
        crater_vis(img, it, th, t, dur)
    if v["type"] == "orbityear":
        orbityear_vis(img, it, th, t, dur)
    if v["type"] == "probes":
        probes_vis(img, it, th, t, dur)
    if v["type"] == "rocks":
        rocks_vis(img, it, th, t, dur)
    if v["type"] == "weigh":
        weigh_vis(img, it, th, t, dur)
    if v["type"] == "gravity":
        gravity_vis(img, it, th, t, dur)
    if v["type"] == "litre":
        litre_vis(img, it, th, t, dur)
    if v["type"] == "beads":
        beads_vis(img, it, th, t, dur)
    if v["type"] == "tilt":
        tilt_vis(img, it, th, t, dur)
    if v["type"] == "pair":
        pair_vis(img, it, th, t, dur)
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
    if th.get("outro") == "pair":
        # all five pairs in a row: every planet drawn the same size, moons to scale with their own planet
        for i, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["rank"])):
            x = 120 + i * 210; vv = o["vis"]; rp = 52
            R.paste_c(img, pa_body(vv["kind"] if vv["kind"] != "ringed" else "gas", rp, tuple(vv["col"])), x - 22, 620, a)
            rm = rp * vv["ratio"]; R.paste_c(img, pa_body(vv.get("mkind", "rock"), max(3, rm), tuple(vv.get("mcol", (190, 185, 180)))), x + rp - 18 + rm, 620 - rp * 0.7, a)
            text(img, (x, 470), f"#{o['rank']}", 40, tuple(th["accent"]), a=a, stroke=3)
            text(img, (x, 740), f"{vv['ratio'] * 100:.0f}%" if vv["ratio"] > 0.1 else f"{vv['ratio'] * 100:.1f}%", 40, (255, 255, 255), a=a, stroke=3)
            text(img, (x, 785), vv.get("mname", ""), 28, tuple(vv.get("mcol", th["accent"])), w="ExtraBold", a=a, stroke=3)
        if th.get("outro_note"): text(img, (W / 2, 940), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a, stroke=3)
        text(img, (W / 2, 1080), "WHICH MOON", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1170), "SHOULD WE MEASURE NEXT?", 56, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1340), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1430), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "tilt":
        # all five in a row, each tilted by its own obliquity, + Earth for reference
        row = sorted(ALL_ITEMS, key=lambda o: o["rank"])
        d = ImageDraw.Draw(img); d.line([(40, 640), (W - 40, 640)], fill=(150, 160, 200), width=2)
        for i, o in enumerate(row):
            x = 130 + i * 205; vv = o["vis"]
            tl_planet(img, vv["kind"], tuple(vv["col"]), x, 640, 62, vv["deg"], t * 0.4, a, retro=vv.get("retro", False))
            text(img, (x, 470), f"#{o['rank']}", 40, tuple(th["accent"]), a=a, stroke=3)
            text(img, (x, 810), f"{vv['deg']:.0f}°", 40, (255, 255, 255), a=a, stroke=3)
            text(img, (x, 855), o["name"], 28, tuple(vv["col"]), w="ExtraBold", a=a, stroke=3)
        if th.get("outro_note"): text(img, (W / 2, 975), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a, stroke=3)
        text(img, (W / 2, 1100), "WHICH PLANET", 92, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1190), "SHOULD WE MEASURE NEXT?", 56, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1360), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1450), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "beads":
        # all five side by side at one smaller common scale, biggest first
        k = 0.2 * BD_K; x = 150; cy = 680
        for o in sorted(ALL_ITEMS, key=lambda o: o["rank"]):
            vv = o["vis"]; r = vv["km"] / 2 * k
            if vv["kind"] == "ringed": x += 0.85 * r
            bd_planet(img, vv["kind"], vv["col"], x + r, cy, r, a)
            text(img, (x + r, cy + max(r, 30) + 40), f"#{o['rank']}", 38, tuple(th["accent"]), a=a, stroke=3)
            x += 2 * r + (60 if vv["kind"] == "ringed" else 44)
        if th.get("outro_note"): text(img, (W / 2, 1000), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a, stroke=3)
        text(img, (W / 2, 1130), "WHICH WORLD", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1225), "SHOULD WE MEASURE NEXT?", 56, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1400), "SUBSCRIBE to Cosmic Scale", 56, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        return
    if th.get("outro") == "litre":
        # five small jars side by side, each on its own scale, + Saturn's jar floating in a water tank
        for i, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["rank"])):
            x = 140 + i * 200; vv = o["vis"]
            lt_jar(img, x, 760, vv["col"], 1.0, t, w=130, h=180, a=a, label=None)
            lt_scale(img, x, 766, f"{vv['kgl']:.1f} kg", w=190, a=a)
            text(img, (x, 470), f"#{o['rank']}", 40, tuple(vv["col"]), a=a, stroke=3)
            text(img, (x, 515), o["name"], 30, tuple(vv["col"]), w="ExtraBold", a=a, stroke=3)
        if th.get("outro_note"): text(img, (W / 2, 960), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a, stroke=3)
        text(img, (W / 2, 1080), "WHAT SHOULD WE", 86, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1165), "WEIGH NEXT?", 70, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1340), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1430), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "gravity":
        gv_ruler(img, th, ALL_ITEMS, cur=None, y=640)
        if th.get("outro_note"): text(img, (W / 2, 820), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 980), "WHERE SHOULD WE", 86, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1070), "WEIGH YOU NEXT?", 70, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1300), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1390), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "weigh":
        wg_ruler(img, th, ALL_ITEMS, cur=None, y=640)
        if th.get("outro_note"): text(img, (W / 2, 850), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 990), "WHAT SHOULD WE", 90, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1080), "WEIGH NEXT?", 70, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1310), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1400), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "rocks":
        # all five side by side at one scale (0.45 px/km), biggest first, plus the Moon's edge for scale
        x = 70; k3 = 0.45; d = ImageDraw.Draw(img)
        for o in sorted(ALL_ITEMS, key=lambda o: o["rank"]):
            v = o["vis"]; w = v["km"] * k3; spr = rk_rock(v["km"], v["lump"], tuple(v["col"]), v.get("seed", 1), v.get("spot", False))
            sm = spr.resize((max(4, int(spr.width * k3 / RK_K)), max(4, int(spr.height * k3 / RK_K))))
            cx_ = x + w / 2 if o["rank"] == 1 else None
            if o["rank"] == 1: R.paste_c(img, sm, 70 + w / 2, 600)
            else:
                col_i = o["rank"] - 2; xx = 70 + 939 * k3 + 30 + (col_i % 2) * 250; yy = 470 + (col_i // 2) * 270
                R.paste_c(img, sm, xx + v["km"] * k3 / 2, yy + 20)
                d = ImageDraw.Draw(img); d.text((xx + v["km"] * k3 / 2, yy + 20 + v["km"] * k3 / 2 + 26), f"#{o['rank']}", font=F(30, "Black"), fill=tuple(v["col"]), anchor="mm")
        d = ImageDraw.Draw(img); d.text((70 + 939 * k3 / 2, 600 + 939 * k3 / 2 + 30), "#1", font=F(34, "Black"), fill=tuple(th["accent"]), anchor="mm")
        if th.get("outro_note"): text(img, (W / 2, 1010), th["outro_note"], 42, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 1180), "WHICH ROCK", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1275), "SHOULD WE VISIT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1440), "SUBSCRIBE to Cosmic Scale", 56, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        return
    if th.get("outro") == "probes":
        pr_track(img, th, ALL_ITEMS, cur=None, y=760)
        for o in ALL_ITEMS:
            v = o["vis"]; x = pr_x(v["au"]); d = ImageDraw.Draw(img)
            d.text((x, 640 - {5: 0, 4: 0, 3: 0, 2: 60, 1: 0}.get(o["rank"], 0)), f"#{o['rank']}", font=F(34, "Black"), fill=tuple(v["col"]), anchor="mm")
        if th.get("outro_note"): text(img, (W / 2, 1060), th["outro_note"], 42, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 1200), "WHERE SHOULD WE", 84, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1290), "SEND ONE NEXT?", 70, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1440), "SUBSCRIBE to Cosmic Scale", 56, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        return
    if th.get("outro") == "orbityear":
        # all five orbits at ONE common scale around the same Sun: four small rings and Sedna's long needle
        k1 = 980 / (506.0 * 1.85)
        for o in sorted(ALL_ITEMS, key=lambda o: o["rank"]):
            v = o["vis"]
            oy_orbit(img, 95, 600, v["a"], v["e"], (0.3 + t * 0.03) % 1.0, tuple(v["col"]), k=k1, ang=math.pi + 0.12 if o["rank"] == 1 else v.get("ang", 0.5),
                     earth=False, trail=False, at_sun=True)
        text(img, (W / 2, 400), "all five, same scale", 34, (200, 205, 225), w="Bold")
        oy_ruler(img, th, ALL_ITEMS, cur=None, y=860)
        if th.get("outro_note"): text(img, (W / 2, 1100), th["outro_note"], 42, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 1230), "WHICH WORLD", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1320), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1460), "SUBSCRIBE to Cosmic Scale", 56, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        return
    if th.get("outro") == "crater":
        img.alpha_composite(cr_ground(), (0, 700 - 450))
        for i, o in enumerate(sorted(ALL_ITEMS, key=lambda o: o["rank"])):
            km = o["vis"]["km"]; r = km / 2 * CR_K; d = ImageDraw.Draw(img)
            d.ellipse([W / 2 - r, 700 - r * 0.92, W / 2 + r, 700 + r * 0.92], outline=tuple(o["vis"].get("ring", th["accent"])), width=5)
            ang = math.radians([-90, -35, 10, 180, 125][i]); lx, ly = W / 2 + (r + 16) * math.cos(ang), 700 + (r * 0.92 + 16) * math.sin(ang)
            anc = "mm" if abs(math.cos(ang)) < 0.3 else ("lm" if math.cos(ang) > 0 else "rm")
            d.text((lx, ly - (14 if i == 0 else 0)), o["short"], font=F(32, "ExtraBold"), fill=tuple(o["vis"].get("ring", th["accent"])), anchor=anc, stroke_width=4, stroke_fill=(0, 0, 0))
        if th.get("outro_note"): text(img, (W / 2, 1130), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 1240), "WHICH CRATER", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1330), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1460), "SUBSCRIBE to Cosmic Scale", 56, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        return
    if th.get("outro") == "wind":
        wind_meter(img, th, ALL_ITEMS, cur=None, y=640)
        if th.get("outro_note"): text(img, (W / 2, 850), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 980), "WHICH WORLD", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1070), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1310), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1400), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
    if th.get("outro") == "spin":
        spin_meter(img, th, ALL_ITEMS, cur=None, y=640)
        if th.get("outro_note"): text(img, (W / 2, 820), th["outro_note"], 44, tuple(th["accent2"]), w="ExtraBold", a=a)
        text(img, (W / 2, 960), "WHICH OBJECT", 96, (255, 255, 255), a=ease((t - 0.3) / 0.5))
        text(img, (W / 2, 1050), "SHOULD WE PUT NEXT?", 58, tuple(th["accent"]), a=ease((t - 0.5) / 0.5))
        text(img, (W / 2, 1310), "SUBSCRIBE", 100, tuple(th["accent"]), a=ease((t - 0.8) / 0.5))
        text(img, (W / 2, 1400), "to Cosmic Scale", 50, (255, 255, 255), w="ExtraBold", a=ease((t - 1.0) / 0.5))
        return
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
