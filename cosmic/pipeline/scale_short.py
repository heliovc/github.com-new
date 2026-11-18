"""Cosmic Scale — "Scale Shorts" (vertical nativo 1080x1920 30fps): UMA comparação de escala ("X inside Y", "small vs giant"), 30–50 s.
Uso: python3 -I scale_short.py scaleNN_algo.py out/scaleNN [--preview]
Roteiro: TITLE, THEME {accent, accent2, tint}, BIG {num, top, sub} (número grande já no frame 0), BEATS [{say, vis{...}}], SOURCES.
- O 1º beat é o gancho (≤ 2 s falado); o último termina com uma pergunta e emenda no 1º (loop): o frame final repete a composição do frame 0.
- Sem fade no início; legenda grande queimada (3 palavras por bloco); narração Kokoro af_heart.
Visuais (vis.type):
  "gap"    : Terra no topo e Lua embaixo EM ESCALA; os planetas caem e empilham no vão (vis.add = nomes que entram neste beat,
             vis.moon = "apogee" | "mean"; vis.show_total = mostra a soma) (scale01).
  "inside" : corpo grande Y (vis.big_r_km, vis.big_col) e o pequeno X (vis.small_r_km) com contador de quantos X cabem em Y (vis.count).
  "storm"  : Júpiter com faixas; zoom do planeta inteiro (z0/z1 = 0) até a Grande Mancha Vermelha (1); largura da mancha segue o ano
             (y0/y1: 1880 = 41.000 km -> 2017 = 16.000 km); vis.earths = Terras em escala dentro da mancha (drop = caem) (scale02).
  "starinside": uma estrela real (EBLM J0555-57Ab) EM ESCALA dentro de Júpiter; vis.mode = inside (drop = cai no disco) | balance
             (1 estrela x pilha de 85 Júpiteres) | saturn (lado a lado com Saturno) | limit (barra 0–100 massas de Júpiter, linha de fusão) (scale03).
  "thinring": anéis de Saturno, 273.000 km de largura x ~10 m de espessura; vis.mode = edge (linha + lupa com prédio de 3 andares) | wide
             (Saturno inclinado + barra Terra–Lua em escala) | zoom (zoom log na borda) | paper (anel fino como papel = 2,7 km sobre uma
             cidade em escala) | tilt (anéis ficando de perfil, 2017 -> 2025) (scale04).
  "fillsun": o Sol EM ESCALA contra a Terra; vis.mode = hook (Sol + Terra minúscula ao lado) | row (109 Terras no diâmetro) | fill
             (Terras enchendo o disco + contador até 1,3 milhão por volume; fatia 2D ilustrativa) | door (Sol = porta de 2 m, Terra = 18 mm) (scale05); vis.count = alvo do contador.
  "mapfit": Plutão EM ESCALA contra o contorno simplificado dos EUA (48 estados, desenhado à mão em lon/lat); vis.mode = hook (mapa +
             Plutão em cima; drop = cai) | ruler (barras 4.500 x 2.377 km) | moon (Lua x Plutão sobre o mapa) | trip (Terra -> Plutão,
             contador de anos da New Horizons 2006 -> 2015) (scale06).
  "bhfit" : o Sistema Solar EM ESCALA dentro do horizonte de eventos de M87* (raio 128,3 UA = Schwarzschild de 6,5 bilhões de Sóis);
             vis.mode = hook (buraco negro + órbitas até Netuno; rows = 4 órbitas de Netuno lado a lado) | zoom (começa nos planetas e
             afasta em log até o horizonte aparecer) | mass (Sol minúsculo + contador de Sóis) | voyager (linha da Voyager 1, 1977 -> 2026,
             173 UA, sai da borda por pouco) | light (pulso de luz atravessando o diâmetro, contador até 35,6 h) (scale07).
  "moonorbit": a órbita inteira da Lua DENTRO do Sol, em escala (Terra no centro do Sol; raio do Sol 696.000 km, Lua a 384.400 km);
             vis.mode = hook (Sol translúcido + órbita + Lua girando) | orbit (zoom log da Terra até a órbita, contador de km) | room
             (barras raio x distância + 311.600 km de folga) | trip (ponto no ritmo da Apollo 11 atravessa o Sol, contador até 11,5 dias) (scale08).
  "jupfill": Júpiter como globo de vidro (raio 430 px) enchido POR VOLUME com os outros 7 planetas em camadas coloridas (altura do
             líquido resolve f = x²(3 − 2x)); vis.mode = hook (os 7 dentro, linha em 67%) | pour (vis.before = já despejados, vis.add =
             caem em escala neste beat e o nível sobe) | room (o terço vazio brilha + contador de Terras até 435) (scale09).
Reaproveita render.py (sprites, fontes) e ranking.py (fundo, texto, legendas).
"""
import sys, os, math, json, subprocess, importlib.util, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw
import render as R
import ranking as K

W, H, FPS = 1080, 1920, 30
F, ease, easeio, mix, lerp, text = R.F, R.ease, R.easeio, R.mix, R.lerp, K.text
HANDLE = "@universeinscale"

PL_KM = {"Mercury": 4879, "Venus": 12104, "Mars": 6792, "Jupiter": 142984, "Saturn": 120536, "Uranus": 51118, "Neptune": 49528}
PL_ORDER = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
EARTH_KM, MOON_KM = 12742, 3474.8
GAP = {"apogee": 405500 - 6371 - 1737, "mean": 384400 - 6371 - 1737}
GX, GY0, GY1 = 690, 330, 1480  # gap column: Earth surface at GY0, Moon surface (apogee) at GY1

def load(path):
    spec = importlib.util.spec_from_file_location("sc", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def schedule(beats, durs):
    """global arrival time of each planet: spread evenly over the beat that adds it"""
    arr, acc = {}, 0.0
    for b, d in zip(beats, durs):
        add = b["vis"].get("add", [])
        for i, n in enumerate(add): arr[n] = acc + 0.3 + (d - 0.8) * i / max(1, len(add))
        acc += d
    return arr

def gap_vis(img, v, th, gt, t, dur, arr):
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"])
    s = (GY1 - GY0) / GAP["apogee"]
    moon_mode = v.get("moon", "apogee")
    mp = easeio((t - 1.0) / 1.5) if moon_mode == "mean" else 0.0
    gap_px = lerp(GAP["apogee"], GAP["mean"], mp) * s
    d = ImageDraw.Draw(img)
    # Earth (to scale) at top, Moon at bottom
    er = EARTH_KM / 2 * s; mr = MOON_KM / 2 * s
    R.paste_c(img, R.radial(140, [(0, (120, 180, 255, 160)), (1, (60, 120, 255, 0))]), GX, GY0 - er)
    R.paste_c(img, R.earth_sprite(max(6, int(er)), glow=None), GX, GY0 - er)
    my = GY0 + gap_px + mr
    R.paste_c(img, R.radial(110, [(0, (230, 230, 240, 150)), (1, (200, 200, 220, 0))]), GX, my)
    R.paste_c(img, R.planet_sprite(max(4, int(mr)), (185, 185, 190)), GX, my)
    d = ImageDraw.Draw(img)
    d.line([(GX - 260, GY0), (GX + 260, GY0)], fill=(90, 140, 255), width=2)
    d.line([(GX - 260, GY0 + gap_px), (GX + 260, GY0 + gap_px)], fill=(200, 200, 215), width=2)
    d.text((GX + 270, GY0 - er), "EARTH", font=F(34, "Black"), fill=(130, 180, 255), anchor="lm")
    d.text((GX + 270, my), "MOON", font=F(34, "Black"), fill=(220, 220, 230), anchor="lm")
    # ghost outlines: where the planets will go (hook teases the answer)
    if v.get("ghost"):
        yg = GY0; dg = ImageDraw.Draw(img)
        for n in PL_ORDER:
            h = PL_KM[n] * s
            if not (n in arr and gt >= arr[n]): K.dashed_circle(dg, GX, yg + h / 2, max(3, h / 2), (150, 170, 200), 3)
            yg += h
        dg.text((GX, GY0 + 0.4 * (GY1 - GY0)), "?", font=F(160, "Black"), fill=acc, anchor="mm") if not arr or gt < min(arr.values()) else None
    # stacked planets
    y = GY0; total = 0
    for n in PL_ORDER:
        if n not in arr or gt < arr[n]: continue
        u = ease((gt - arr[n]) / 0.45)
        h = PL_KM[n] * s; cy = lerp(-200, y + h / 2, u)
        col = R.PCOL[n]
        if n == "Saturn":
            d = ImageDraw.Draw(img); d.ellipse([GX - h * 1.1, cy - h * 0.18, GX + h * 1.1, cy + h * 0.18], outline=(225, 205, 150), width=max(2, int(h * 0.05)))
        R.paste_c(img, R.planet_sprite(max(2, int(h / 2)), col, light=(-0.8, -0.4)), GX, cy)
        d = ImageDraw.Draw(img)
        lx = GX - max(h / 2, 20) - 30
        if n == "Saturn": lx = GX - h * 1.1 - 20
        d.text((lx, cy), n, font=F(36 if h > 40 else 28, "ExtraBold"), fill=col, anchor="rm")
        y += h; total += PL_KM[n]
    # overflow marker
    over = y - (GY0 + gap_px)
    if over > 1:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([GX - 200, GY0 + gap_px, GX + 200, y], fill=(255, 70, 70, 110)); img.alpha_composite(lay)
    return total, gap_px / s

def inside_vis(img, v, th, gt, t, dur):
    acc = tuple(th["accent"]); cx, cy = W / 2, 900; Rb = 380
    R.paste_c(img, R.planet_sprite(Rb, tuple(v.get("big_col", (255, 190, 90))), light=(-0.7, -0.4)), cx, cy)
    rs = max(2, Rb * v["small_r_km"] / v["big_r_km"])
    n = int(v.get("count", 1) * easeio((t - 0.4) / max(1.0, dur * 0.7)))
    rng = random.Random(3); d = ImageDraw.Draw(img)
    for i in range(min(n, 900)):
        a = rng.uniform(0, 2 * math.pi); r = Rb * math.sqrt(rng.random()) * 0.95
        x, y = cx + r * math.cos(a), cy + r * math.sin(a); d.ellipse([x - rs, y - rs, x + rs, y + rs], fill=tuple(v.get("small_col", (90, 140, 255))))
    text(img, (W / 2, 330), f"{n:,}", 140, acc)

# ---- scale02: "storm" — Jupiter with banded clouds; zoom from the whole planet (zoom 0) to the Great Red Spot (zoom 1);
# the spot's width follows the year (1880: 41,000 km -> 2017: 16,000 km, linear between); 'earths' = Earth discs dropped inside, to scale.
JUP_KM, GRS_LAT = 142984, -0.37
BANDS2 = [(-1.0, (196, 170, 140)), (-0.62, (222, 205, 178)), (-0.47, (176, 128, 96)), (-0.28, (232, 220, 196)), (-0.12, (190, 150, 115)),
          (0.06, (236, 226, 204)), (0.2, (170, 120, 90)), (0.38, (225, 210, 185)), (0.55, (186, 150, 120)), (0.75, (214, 196, 170))]
def grs_width(year): return lerp(41000, 16000, max(0, min(1, (year - 1880) / (2017 - 1880))))
def storm_vis(img, v, th, t, dur, beat_p):
    z = lerp(v.get("z0", 1.0), v.get("z1", v.get("z0", 1.0)), beat_p)
    year = lerp(v.get("y0", 2017), v.get("y1", v.get("y0", 2017)), beat_p)
    k0, k1 = 840 / JUP_KM, 470 / 16000
    k = k0 * (k1 / k0) ** z                      # px per km
    cx, cy = W / 2, 900
    Rj = JUP_KM / 2 * k; jx, jy = cx, cy - GRS_LAT * Rj   # spot at screen centre
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, (lat, col) in enumerate(BANDS2):
        top = jy + lat * Rj; nxt = BANDS2[i + 1][0] if i + 1 < len(BANDS2) else 1.0
        wob = 6 * math.sin(t * 0.8 + i)
        d.rectangle([0, top + wob, W, jy + nxt * Rj + wob], fill=col + (255,))
    for j in range(40):  # thin turbulent streaks
        rr = random.Random(j); lat = rr.uniform(-0.9, 0.9); y = jy + lat * Rj
        x0 = (rr.uniform(0, W) + t * 30 * (1 if lat > 0 else -1)) % (W + 400) - 200
        d.line([(x0, y), (x0 + rr.uniform(80, 300), y + rr.uniform(-4, 4))], fill=(255, 245, 225, 70), width=max(2, int(Rj * 0.006)))
    gw = grs_width(year) * k; gh = gw * 0.82
    for q in range(6, 0, -1):
        f = q / 6; c = mix((150, 50, 30), (225, 120, 80), 1 - f)
        d.ellipse([cx - gw / 2 * f, cy - gh / 2 * f, cx + gw / 2 * f, cy + gh / 2 * f], fill=c + (255,))
    for q in range(3):  # swirl
        a0 = t * 40 + q * 120
        d.arc([cx - gw * 0.38, cy - gh * 0.38, cx + gw * 0.38, cy + gh * 0.38], a0, a0 + 70, fill=(250, 170, 130, 200), width=max(2, int(gw * 0.015)))
    m = Image.new("L", img.size, 0); ImageDraw.Draw(m).ellipse([jx - Rj, jy - Rj, jx + Rj, jy + Rj], fill=255)
    lay.putalpha(Image.fromarray(np.minimum(np.asarray(lay.getchannel("A")), np.asarray(m))))
    img.alpha_composite(lay)
    d = ImageDraw.Draw(img)
    # Earths dropped in, side by side across the spot, to scale
    n = v.get("earths", 0); n = max(1, int(grs_width(year) / 12742)) if n == "auto" else n; er = 12742 / 2 * k
    if n and er > 3:
        u = ease((t - 0.3) / 0.6) if v.get("drop") else 1.0
        for i in range(int(n)):
            ex = cx + (i - (n - 1) / 2) * 2 * er
            ey = lerp(cy - 900, cy, u)
            R.paste_c(img, R.earth_sprite(max(4, int(er)), glow=None), ex, ey)
    d = ImageDraw.Draw(img)
    if z > 0.6:
        d.line([(cx - gw / 2, cy + gh / 2 + 40), (cx + gw / 2, cy + gh / 2 + 40)], fill=(255, 255, 255), width=4)
        for xx in (cx - gw / 2, cx + gw / 2): d.line([(xx, cy + gh / 2 + 25), (xx, cy + gh / 2 + 55)], fill=(255, 255, 255), width=4)
        text(img, (cx, cy + gh / 2 + 95), f"{grs_width(year):,.0f} km  ·  {grs_width(year) / 12742:.1f} Earths", 44, (255, 255, 255), w="ExtraBold")
    if v.get("show_year"):
        text(img, (W / 2, 420), f"{int(year)}", 110, tuple(th["accent2"]), stroke=4)
    if z < 0.4 and v.get("label_planet"):
        text(img, (cx, jy - Rj - 40 if jy - Rj > 380 else 420), "JUPITER · 11 Earths wide", 46, (255, 230, 200), w="ExtraBold")

# ---- scale03: "starinside" — a real star (EBLM J0555-57Ab) drawn TO SCALE inside Jupiter; modes: inside (star drops into Jupiter's disc),
# balance (1 star vs a pile of 85 Jupiters on a beam), saturn (star beside Saturn, same size), limit (mass bar 0–100 Jupiters, fusion line ~80).
JUP_R3, STAR_R3, SAT_R3 = 71492, 59000, 58232
def starinside_vis(img, v, th, t, dur, bp):
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "inside"); cx, cy = W / 2, 930
    if mode == "inside":
        Rj = 400; R.paste_c(img, R.jup10(Rj, 0.0), cx, cy)
        u = ease((t - 0.2) / 0.7) if v.get("drop") else 1.0
        rs = Rj * STAR_R3 / JUP_R3; sy = lerp(cy - 1100, cy, u)
        spr = R.jup10(rs, 1.0).copy(); m_ = Image.new("L", spr.size, 0); c_ = spr.width / 2
        ImageDraw.Draw(m_).ellipse([c_ - rs - 5, c_ - rs - 5, c_ + rs + 5, c_ + rs + 5], fill=255)
        spr.putalpha(Image.fromarray(np.minimum(np.asarray(spr.getchannel("A")), np.asarray(m_)))); R.paste_c(img, spr, cx, sy)
        text(img, (cx, sy), "STAR", 70, (90, 20, 10), w="Black", a=u)
        d = ImageDraw.Draw(img); R.dash_circle10(d, cx, cy, Rj, (255, 235, 200), 4)
        text(img, (cx, cy + Rj + 60), "dashed: Jupiter", 40, (255, 225, 190), w="ExtraBold")
    elif mode == "balance":
        ang = 0.0
        px, py, L = cx, 1080, 400
        d = ImageDraw.Draw(img)
        d.polygon([(px, py), (px - 60, py + 160), (px + 60, py + 160)], fill=(120, 125, 150))
        lx, ly = px - L * math.cos(ang), py - L * math.sin(ang); rx, ry = px + L * math.cos(ang), py + L * math.sin(ang)
        d.line([(lx, ly), (rx, ry)], fill=(200, 205, 225), width=12)
        R.paste_c(img, R.jup10(120, 1.0), rx, ry - 130)   # the star, heavy side goes down (right)
        rng = random.Random(5); n = int(85 * ease((t - 0.1) / 0.9))
        for i in range(n):
            row = int((math.sqrt(8 * i + 1) - 1) / 2); col = i - row * (row + 1) // 2
            R.paste_c(img, R.jup10(12, 0.0), lx - row * 13 + col * 26, ly - 40 - (12 - row) * 23)
        text(img, (lx, ly + 90), f"{n} Jupiters", 46, (240, 200, 150), w="ExtraBold")
        text(img, (rx, ry + 90), "1 star", 46, acc, w="ExtraBold")
        text(img, (cx, py + 230), "balanced", 52, (255, 255, 255), a=ease((t - 1.0) / 0.4))
    elif mode == "saturn":
        k = 330 / STAR_R3
        R.paste_c(img, R.jup10(STAR_R3 * k * 0.42, 1.0), cx - 250, cy - 160)
        sr = SAT_R3 * k * 0.42; sx, sy = cx + 250, cy - 160
        d = ImageDraw.Draw(img); d.ellipse([sx - sr * 1.9, sy - sr * 0.4, sx + sr * 1.9, sy + sr * 0.4], outline=(225, 205, 150), width=8)
        R.paste_c(img, R.planet_sprite(int(sr), (225, 205, 150), light=(-0.8, -0.4)), sx, sy)
        d = ImageDraw.Draw(img); d.arc([sx - sr * 1.9, sy - sr * 0.4, sx + sr * 1.9, sy + sr * 0.4], 0, 180, fill=(225, 205, 150), width=8)
        text(img, (cx - 250, cy + 60), "the star", 44, acc, w="ExtraBold"); text(img, (cx + 250, cy + 60), "Saturn", 44, (225, 205, 150), w="ExtraBold")
        text(img, (cx - 250, cy + 120), "≈ 118,000 km", 36, (230, 230, 240), w="Bold"); text(img, (cx + 250, cy + 120), "116,464 km", 36, (230, 230, 240), w="Bold")
    elif mode == "limit":
        x0, x1, y = 110, W - 110, 980; d = ImageDraw.Draw(img)
        def mx(m): return lerp(x0, x1, m / 100)
        d.rounded_rectangle([x0, y - 22, x1, y + 22], 22, fill=(45, 40, 60))
        p = easeio((t - 0.2) / max(0.8, dur * 0.6)); m = 85 * p
        d.rounded_rectangle([x0, y - 22, max(x0 + 44, mx(m)), y + 22], 22, fill=acc)
        for mm, lab in [(1, "Jupiter"), (13, "brown dwarf"), (80, "STAR")]:
            x = mx(mm); d.line([(x, y - 60), (x, y + 60)], fill=(255, 255, 255), width=4)
            d.text((x, y - 90 if mm != 13 else y + 100), lab, font=F(36, "ExtraBold"), fill=(255, 255, 255) if mm != 80 else acc2, anchor="mm")
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([mx(75), y - 40, mx(83), y + 40], fill=acc2 + (90,)); img.alpha_composite(lay)
        R.paste_c(img, R.jup10(90, 1.0 if m > 78 else 0.3), mx(m), y - 230)
        text(img, (W / 2, y + 220), f"{m:.0f} Jupiter masses", 64, (255, 255, 255))
        text(img, (W / 2, y + 300), "hydrogen fusion line ≈ 80", 40, acc2, w="ExtraBold")

# ---- scale04: "thinring" — Saturn's rings: 273,000 km across vs about 10 m thick. modes: edge (hairline across the screen + magnifier with a
# 3-storey building beside the ring band) | wide (tilted Saturn + rings vs the Earth–Moon distance, to scale) | zoom (log zoom on the edge,
# field-of-view counter) | paper (paper-thin rings would still be 2.7 km wide: strip over a skyline to scale) | tilt (rings close to edge-on,
# year counter 2017 -> 2025).
SAT_R4 = 60268
def saturn4(img, cx, cy, r, tilt):
    s = math.sin(math.radians(max(0.15, tilt)))
    def rings(front):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        for nm, r0, r1, col, op in R.RINGS11:
            for j in range(6):
                rr = r * lerp(r0, r1, (j + 0.5) / 6); w_ = max(2, int(r * (r1 - r0) / 6 * s * 1.1 + 2)) if s > 0.05 else 2
                box = [cx - rr, cy - rr * s, cx + rr, cy + rr * s]
                dl.arc(box, 0 if front else 180, 180 if front else 360, fill=col + (int(255 * op),), width=max(2, int(r * (r1 - r0) / 6) if s > 0.2 else 3))
        img.alpha_composite(lay)
    rings(False)
    R.paste_c(img, R.planet_sprite(int(r), (226, 204, 150), light=(-0.8, -0.5)), cx, cy)
    rings(True)
def thinring_vis(img, v, th, t, dur, bp):
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "edge"); cx, cy = W / 2, 930
    d = ImageDraw.Draw(img)
    if mode == "edge":
        d.line([(0, cy), (W, cy)], fill=R.CREAM11, width=2)
        mr = 330; mx, my = cx, cy
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(6, 8, 22, 245))
        bh = 260  # 10 m = 260 px inside the magnifier
        dl.rectangle([mx - mr, my - bh / 2, mx + mr, my + bh / 2], fill=R.CREAM11 + (70,))
        rng = random.Random(4)
        for i in range(160):
            x = mx + rng.uniform(-mr, mr); y = my + rng.uniform(-bh / 2 + 10, bh / 2 - 10); s_ = 10 ** rng.uniform(-0.3, 1.5)
            sh = int(205 + 40 * rng.random()); dl.ellipse([x - s_, y - s_ * 0.8, x + s_, y + s_ * 0.8], fill=(sh, sh - 6, sh - 24, 255))
        bx = mx + 70; bw = 150
        dl.rectangle([bx, my + bh / 2 - bh, bx + bw, my + bh / 2], fill=(60, 72, 110, 255), outline=(170, 180, 215, 255), width=4)
        for fl in range(3):
            for wn in range(3): dl.rectangle([bx + 18 + wn * 45, my - bh / 2 + 22 + fl * 84, bx + 46 + wn * 45, my - bh / 2 + 60 + fl * 84], fill=(255, 210, 130, 255))
        m = Image.new("L", img.size, 0); ImageDraw.Draw(m).ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=255)
        lay.putalpha(Image.fromarray(np.minimum(np.asarray(lay.getchannel("A")), np.asarray(m))))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        d.ellipse([mx - mr, my - mr, mx + mr, my + mr], outline=acc, width=8)
        d.line([(mx + mr + 30, my - bh / 2), (mx + mr + 30, my + bh / 2)], fill=acc2, width=6)
        for yy in (my - bh / 2, my + bh / 2): d.line([(mx + mr + 14, yy), (mx + mr + 46, yy)], fill=acc2, width=6)
        text(img, (mx + mr + 30, my - bh / 2 - 50), "10 m", 52, acc2)
        text(img, (W / 2, cy + mr + 70), "the ring, edge-on (magnified)", 38, (230, 232, 240), w="ExtraBold")
    elif mode == "wide":
        k = 520 / 136775; saturn4(img, cx, 800, SAT_R4 * k, 22)
        y = 1240; x0 = 50
        for i, (lab, km, col) in enumerate([("main rings, edge to edge: 273,000 km", 273550, R.CREAM11), ("Earth to the Moon: 384,400 km", 384400, (140, 190, 255))]):
            p = ease((t - 0.3 - i * 0.8) / 0.8); L = (W - 100) * km / 384400 * p; yy = y + i * 130
            d.rounded_rectangle([x0, yy - 16, x0 + max(20, L), yy + 16], 16, fill=col)
            d.text((x0, yy - 50), lab, font=F(34, "ExtraBold"), fill=col, anchor="lm")
        d.text((W / 2, y + 230), "same scale", font=F(30, "Bold"), fill=(170, 175, 200), anchor="mm")
    elif mode == "zoom":
        p = easeio((t - 0.2) / max(0.8, dur * 0.8))
        pxm = math.exp(lerp(math.log(1000 / 2.8e8), math.log(1000 / 40.0), p)); th_ = max(2, 10 * pxm); half = 1.365e8 * pxm
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rectangle([max(-10, cx - half), cy - th_ / 2, min(W + 10, cx + half), cy + th_ / 2], fill=R.CREAM11 + (110 if th_ > 6 else 255,))
        if pxm > 0.4:
            rng = random.Random(5)
            for i in range(500):
                s_ = 10 ** rng.uniform(-2, 0.7); r_ = max(0.8, s_ * pxm / 2); x = rng.uniform(0, W); y = cy + rng.uniform(-5, 5) * pxm
                sh = int(200 + 40 * rng.random()); dl.ellipse([x - r_, y - r_ * 0.8, x + r_, y + r_ * 0.8], fill=(sh, sh - 8, sh - 25, 255))
        img.alpha_composite(lay)
        if half * 2 < W - 60:
            R.paste_c(img, R.planet_sprite(max(2, int(SAT_R4 * 1000 * pxm)), (226, 204, 150)), cx, cy)
        view = W / pxm; s = f"{view / 1000:,.0f} km" if view > 5000 else f"{view:,.0f} m"
        text(img, (W / 2, 1290), "view: " + s + " wide", 56, acc2)
    elif mode == "paper":
        y = 1080; L = W - 120; pxm = L / 2730.0
        rng = random.Random(9); x = 60
        while x < W - 60:
            bw = rng.uniform(30, 70); bh = rng.choice([rng.uniform(60, 120), rng.uniform(150, 330)]) * pxm
            d.rectangle([x, y + 60 - bh, x + bw, y + 60], fill=(50, 58, 90)); x += bw + rng.uniform(2, 10)
        d.rectangle([0, y + 60, W, y + 75], fill=(30, 34, 55))
        p = ease((t - 0.3) / 1.0)
        d.rectangle([W / 2 - L / 2 * p, y - 400, W / 2 + L / 2 * p, y - 396], fill=(255, 255, 255))
        d.line([(60, y - 340), (W - 60, y - 340)], fill=acc2, width=4)
        for xx in (60, W - 60): d.line([(xx, y - 360), (xx, y - 320)], fill=acc2, width=4)
        text(img, (W / 2, y - 290), "2.7 km", 90, acc2)
        text(img, (W / 2, y - 470), "a ring as thin as paper (0.1 mm)", 40, (255, 255, 255), w="ExtraBold")
        text(img, (W / 2, y + 130), "city skyline, same scale", 32, (170, 175, 200), w="Bold")
    elif mode == "tilt":
        p = easeio((t - 0.2) / max(0.8, dur * 0.7)); tilt = lerp(27, 0.3, p); yr = lerp(2017, 2025, p)
        saturn4(img, cx, 880, 230, tilt)
        text(img, (W / 2, 1270), f"{yr:.0f}", 110, acc2)
        text(img, (W / 2, 1365), "as seen from Earth", 38, (230, 232, 240), w="ExtraBold")

SUN_KM5, EARTH_KM5 = 1392000, 12742
_fill5 = {}
def _fill_pts5(R_, er):
    key = (int(R_), round(er, 2))
    if key not in _fill5:
        pts = []; dx = 2 * er; dy = math.sqrt(3) * er; j = 0; y = -R_ + er
        while y < R_:
            x = -R_ + er + (er if j % 2 else 0)
            while x < R_:
                if x * x + y * y < (R_ - er) ** 2: pts.append((x, y))
                x += dx
            y += dy; j += 1
        pts.sort(key=lambda p: -p[1]); _fill5[key] = pts
    return _fill5[key]

def fillsun_vis(img, v, th, t, dur, bp):
    """the Sun TO SCALE against Earth: mode hook (Sun + tiny Earth beside it) | row (109 Earths across the diameter) | fill (Earths pour in,
    counter to 1.3 million by volume; 2D slice is illustrative) | door (Sun = a 2 m front door, Earth = an 18 mm coin)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy = (W / 2 if mode != "hook" else 470), 900
    R_ = 420; er = R_ * EARTH_KM5 / SUN_KM5
    d = ImageDraw.Draw(img)
    if mode in ("hook", "row", "fill"):
        R.paste_c(img, R.sun_sprite(R_), cx, cy)
        d = ImageDraw.Draw(img)
    if mode == "hook":
        ex = cx + R_ + 60; R.paste_c(img, R.earth_sprite(max(4, int(er * 1.0)), glow=None), ex, cy)
        d = ImageDraw.Draw(img); d.ellipse([ex - 28, cy - 28, ex + 28, cy + 28], outline=acc2, width=4)
        d.line([(ex, cy - 28), (ex - 10, cy - 120)], fill=acc2, width=4); text(img, (ex - 20, cy - 150), "EARTH", 40, acc2)
        text(img, (W / 2, cy + R_ + 80), "to scale", 36, (230, 232, 240), w="ExtraBold")
    elif mode == "row":
        n = int(109 * min(1, bp * 1.1)); x0 = cx - R_ + (2 * R_ - 109 * 2 * er) / 2
        d = ImageDraw.Draw(img)
        for k in range(n):
            x = x0 + er + k * 2 * er; d.ellipse([x - er, cy - er, x + er, cy + er], fill=(40, 110, 230) if k % 2 else (120, 200, 255))
        text(img, (W / 2, cy + R_ + 70), "each dot = 1 Earth, to scale", 36, (230, 232, 240), w="ExtraBold")
        d = ImageDraw.Draw(img); d.rounded_rectangle([cx - 150, cy + 30, cx + 150, cy + 130], 20, fill=(10, 10, 20))
        d.text((cx, cy + 80), f"{n} / 109", font=F(64, "Black"), fill=acc2, anchor="mm")
    elif mode == "fill":
        pts = _fill_pts5(R_, er * 2.2); n = int(len(pts) * bp)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rr = er * 2.2 * 0.9
        for (x, y) in pts[:n]:
            dl.ellipse([cx + x - rr, cy + y - rr, cx + x + rr, cy + y + rr], fill=(70, 130, 230, 255), outline=(170, 210, 255, 255))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        cnt = v.get("count", 1300000) * bp
        d.rounded_rectangle([cx - 330, cy - 70, cx + 330, cy + 70], 26, fill=(10, 10, 20, 230))
        d.text((cx, cy), f"{cnt:,.0f}", font=F(110, "Black"), fill=acc2, anchor="mm")
        text(img, (W / 2, cy + R_ + 70), "Earths, by volume (dots enlarged)", 36, (230, 232, 240), w="ExtraBold")
    elif mode == "door":
        dh = 900; dw = 420; x0, y0 = 270, cy - dh / 2 + 60
        d.rectangle([x0 - 24, y0 - 24, x0 + dw + 24, y0 + dh], fill=(60, 40, 30))
        d.rectangle([x0, y0, x0 + dw, y0 + dh], fill=(120, 80, 50))
        for k in range(2):
            for j in range(3): d.rectangle([x0 + 40 + k * 190, y0 + 40 + j * 280, x0 + 190 + k * 190, y0 + 260 + j * 280], outline=(90, 60, 38), width=6)
        d.ellipse([x0 + dw - 60, y0 + dh / 2 - 15, x0 + dw - 30, y0 + dh / 2 + 15], fill=(220, 190, 90))
        sa = ease((t - 0.3) / 0.6); sr_ = dh / 2; scx, scy = x0 + dw / 2, y0 + dh / 2
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([scx - sr_, scy - sr_, scx + sr_, scy + sr_], fill=(255, 190, 60, int(70 * sa)), outline=(255, 200, 60, int(255 * sa)), width=8)
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        er_px = dh / 2 / 109.2; xc = x0 + dw + 190; yc = y0 + dh - 120
        R.paste_c(img, R.earth_sprite(max(4, int(er_px)), glow=None), xc, yc)
        d = ImageDraw.Draw(img); d.ellipse([xc - 36, yc - 36, xc + 36, yc + 36], outline=acc2, width=4)
        text(img, (xc, yc - 80), "EARTH", 40, acc2); text(img, (xc, yc + 80), "≈ 18 mm", 40, (255, 255, 255))
        d.line([(x0 + dw + 60, y0), (x0 + dw + 60, y0 + dh)], fill=acc, width=5)
        text(img, (x0 + dw + 120, y0 + 60), "SUN = 2 m", 40, acc, anchor="lm")


# ---- scale06: Pluto vs the contiguous United States (hand-traced, simplified outline; equirectangular at 39°N) ----
US6 = [(-124.7, 48.4), (-124.0, 46.3), (-124.2, 43.0), (-124.4, 40.4), (-122.4, 37.8), (-120.6, 34.6), (-117.1, 32.5), (-114.7, 32.7),
       (-111.0, 31.3), (-108.2, 31.3), (-106.5, 31.8), (-104.5, 29.6), (-103.0, 29.0), (-101.4, 29.8), (-99.5, 27.5), (-97.4, 25.9),
       (-97.4, 27.8), (-94.7, 29.4), (-91.0, 29.2), (-89.4, 29.0), (-89.6, 30.2), (-87.5, 30.3), (-85.0, 29.7), (-83.0, 29.0), (-82.6, 27.5),
       (-81.8, 26.0), (-80.4, 25.2), (-80.0, 26.8), (-81.2, 29.9), (-81.4, 30.7), (-80.9, 32.0), (-79.1, 33.4), (-77.9, 34.0), (-75.5, 35.2),
       (-76.0, 37.0), (-75.0, 38.5), (-74.0, 40.5), (-72.0, 41.0), (-70.0, 41.6), (-70.6, 42.6), (-70.2, 43.7), (-67.0, 44.8), (-67.8, 47.1),
       (-69.2, 47.4), (-71.5, 45.0), (-74.9, 45.0), (-76.9, 43.6), (-79.0, 43.3), (-79.2, 42.5), (-82.5, 41.7), (-83.1, 42.3), (-82.4, 43.0),
       (-82.5, 45.3), (-84.6, 46.4), (-88.4, 48.3), (-89.6, 48.0), (-95.2, 49.0), (-123.0, 49.0), (-122.8, 48.2)]
PLUTO_KM6, MOON_KM6, US_KM6 = 2377, 3475, 4500
def us_poly6(cx, cy, kpx):
    """kpx = pixels per km; returns screen polygon centred on (cx, cy)"""
    c = math.cos(math.radians(39)); pts = [(lo * c * 111.32, la * 110.57) for lo, la in US6]
    mx = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2; my = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2
    f = US_KM6 / (max(p[0] for p in pts) - min(p[0] for p in pts))  # outline width normalised to ~4,500 km coast to coast
    return [(cx + (x - mx) * f * kpx, cy - (y - my) * f * kpx) for x, y in pts]

def pluto6(r):
    """Pluto: tan/cream with the pale heart-shaped plain (Tombaugh Regio, simplified) and a darker equatorial band"""
    r = max(4, int(r)); img = R.planet_sprite(r, (196, 160, 128), light=(-0.75, -0.35)).copy()
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); c = img.width / 2
    dl.ellipse([c - r * 0.95, c + r * 0.05, c + r * 0.95, c + r * 0.55], fill=(110, 70, 55, 120))
    hx, hy, hs = c + 0.15 * r, c + 0.05 * r, 0.62
    for ox in (-0.16, 0.16):
        dl.ellipse([hx + (ox - 0.2) * r * hs / 0.62, hy - 0.18 * r, hx + (ox + 0.2) * r * hs / 0.62, hy + 0.18 * r], fill=(240, 228, 210, 130))
    dl.polygon([(hx - 0.34 * r, hy + 0.05 * r), (hx + 0.34 * r, hy + 0.05 * r), (hx, hy + 0.45 * r)], fill=(240, 228, 210, 130))
    m = Image.new("L", img.size, 0); ImageDraw.Draw(m).ellipse([c - r, c - r, c + r, c + r], fill=255)
    lay.putalpha(Image.fromarray(np.minimum(np.asarray(lay.getchannel("A")), np.asarray(m))))
    img.alpha_composite(lay); return img

def mapfit_vis(img, v, th, t, dur, bp):
    """Pluto TO SCALE against the contiguous US: mode hook (map + Pluto dropped on it) | ruler (two bars: 2,377 vs ~4,500 km) |
    moon (Moon vs Pluto over the map) | trip (Earth -> Pluto, New Horizons year counter 2006 -> 2015)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy = W / 2, 920
    kpx = 920 / US_KM6
    if mode in ("hook", "ruler", "moon"):
        poly = us_poly6(cx, cy, kpx)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.polygon(poly, fill=(40, 90, 70, 235), outline=(140, 220, 170, 255)); dl.line(poly + [poly[0]], fill=(140, 220, 170, 255), width=4)
        img.alpha_composite(lay)
        if mode != "moon": text(img, (cx, cy + 330), "USA (lower 48), outline simplified", 32, (200, 230, 210), w="Bold")
    if mode == "hook":
        drop = ease((t - 0.0) / 0.5) if v.get("drop") else 1.0
        R.paste_c(img, pluto6(PLUTO_KM6 / 2 * kpx), cx + 30, cy + 20 - (1 - drop) * 500)
        d = ImageDraw.Draw(img); d.text((cx + 30, cy + 20 - (1 - drop) * 500), "PLUTO", font=F(52, "Black"), fill=(40, 25, 20), anchor="mm")
    elif mode == "ruler":
        d = ImageDraw.Draw(img); y1, y2 = 1340, 1440; x0 = cx - US_KM6 / 2 * kpx
        d.rounded_rectangle([x0, y1 - 22, x0 + US_KM6 * kpx * min(1, bp * 1.3), y1 + 22], 16, fill=(140, 220, 170))
        d.rounded_rectangle([x0, y2 - 22, x0 + PLUTO_KM6 * kpx * min(1, bp * 1.3), y2 + 22], 16, fill=acc)
        d.text((x0 + 10, y1), "USA ≈ 4,500 km", font=F(32, "Black"), fill=(10, 30, 20), anchor="lm")
        d.text((x0 + 10, y2), "PLUTO 2,377 km", font=F(32, "Black"), fill=(40, 20, 10), anchor="lm")
        R.paste_c(img, pluto6(PLUTO_KM6 / 2 * kpx), x0 + PLUTO_KM6 / 2 * kpx, cy, ease((t - 0.3) / 0.5))
    elif mode == "moon":
        R.paste_c(img, R.planet_sprite(int(MOON_KM6 / 2 * kpx), (185, 185, 190), light=(-0.7, -0.4)), cx - 175, cy - 40)
        R.paste_c(img, pluto6(PLUTO_KM6 / 2 * kpx), cx + 285, cy + 90)
        text(img, (cx - 175, cy - 40), "MOON", 50, (40, 40, 45)); text(img, (cx + 285, cy + 90), "PLUTO", 46, (40, 25, 20))
        text(img, (cx - 230, cy - 440), "3,475 km", 44, (230, 230, 240)); text(img, (cx + 285, cy + 370), "2,377 km", 44, acc)
    elif mode == "trip":
        d = ImageDraw.Draw(img); y = 980; xa, xb = 150, 930
        R.paste_c(img, R.earth_sprite(30, glow=None), xa, y); R.paste_c(img, pluto6(16), xb, y)
        for k in range(0, 60, 2):
            d = ImageDraw.Draw(img); d.line([(lerp(xa + 40, xb - 30, k / 60), y), (lerp(xa + 40, xb - 30, (k + 1) / 60), y)], fill=(150, 160, 190), width=4)
        px = lerp(xa + 40, xb - 30, bp); R.paste_c(img, R.radial(60, [(0, (255, 255, 255, 255)), (1, acc2 + (0,))]), px, y)
        d = ImageDraw.Draw(img); d.line([(xa + 40, y), (px, y)], fill=acc2, width=6)
        text(img, (xa, y + 70), "EARTH", 36, (140, 190, 255)); text(img, (xb, y + 70), "PLUTO", 36, acc)
        yr = 2006.05 + 9.48 * bp
        d.rounded_rectangle([cx - 300, 1130, cx + 300, 1330], 26, fill=(10, 10, 20))
        d.text((cx, 1190), f"{yr:.1f}", font=F(96, "Black"), fill=acc2, anchor="mm")
        d.text((cx, 1280), "New Horizons, 2006 → 2015", font=F(34, "Bold"), fill=(220, 225, 240), anchor="mm")

# ---- scale07: the solar system inside M87*'s event horizon (TO SCALE: horizon radius 128.3 AU; Schwarzschild, 6.5 billion Suns) ----
RS_AU7 = 128.34
ORB7 = [("Mercury", 0.387), ("Venus", 0.723), ("Earth", 1.0), ("Mars", 1.524), ("Jupiter", 5.203), ("Saturn", 9.537), ("Uranus", 19.19), ("Neptune", 30.07)]
def bh7(img, cx, cy, rpx, t, a=1.0):
    """event horizon disc of radius rpx: warm photon ring + lensed glow, black inside"""
    if rpx < 2: return
    g = int(rpx * 3.2)
    R.paste_c(img, R.radial(g, [(0, (0, 0, 0, 0)), (0.30, (0, 0, 0, 0)), (0.33, (255, 200, 120, int(220 * a))), (0.40, (255, 120, 50, int(130 * a))),
                                  (0.62, (180, 60, 30, int(40 * a))), (1, (120, 40, 20, 0))]), cx, cy)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse([cx - rpx, cy - rpx, cx + rpx, cy + rpx], fill=(0, 0, 0, int(255 * a)))
    sh = 0.5 + 0.5 * math.sin(t * 1.3)
    dl.arc([cx - rpx * 1.04, cy - rpx * 1.04, cx + rpx * 1.04, cy + rpx * 1.04], 150, 390, fill=(255, 235, 190, int((150 + 80 * sh) * a)), width=max(2, int(rpx * 0.03)))
    img.alpha_composite(lay)

def solar7(img, cx, cy, k, t, upto=30.07, a=1.0, labels=True):
    """orbits to scale (k px per AU) + planets on them; the Sun as a glow point"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for i, (n, au) in enumerate(ORB7):
        if au > upto: continue
        r = au * k
        if r < 3: continue
        dl.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(120, 170, 255, int(170 * a)), width=2)
        ang = t * 0.4 / math.sqrt(au) + i * 1.7
        px, py = cx + r * math.cos(ang), cy + r * math.sin(ang)
        pr = 4 if au < 3 else 6
        dl.ellipse([px - pr, py - pr, px + pr, py + pr], fill=R.PCOL.get(n, (200, 200, 200)) + (int(255 * a),))
        if labels and n in ("Earth", "Jupiter", "Neptune") and r > 26:
            dl.text((px + 12, py - 12), n, font=F(26, "Bold"), fill=(220, 230, 255, int(255 * a)), anchor="lm")
    img.alpha_composite(lay)
    R.paste_c(img, R.radial(36, [(0, (255, 250, 220, int(255 * a))), (0.3, (255, 210, 120, int(200 * a))), (1, (255, 160, 60, 0))]), cx, cy)

def bhfit_vis(img, v, th, t, dur, bp):
    """mode hook (black hole + the solar system to scale inside) | zoom (start on the planets, zoom out log until the horizon appears around them)
    | mass (a tiny Sun vs the hole + counter of Suns) | voyager (Voyager 1 line from the Sun, 1977 -> 2026, just crosses the edge) |
    light (a light pulse crosses the diameter, hours counter to 35.6)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy = W / 2, 960
    kfit = 470 / RS_AU7
    if mode == "zoom":
        k = math.exp(lerp(math.log(470 / 31.0), math.log(kfit), bp))
        bh7(img, cx, cy, RS_AU7 * k, t, a=ease((bp - 0.35) / 0.4))
        solar7(img, cx, cy, k, t)
        if bp > 0.8: text(img, (cx, cy + RS_AU7 * k + 70), "event horizon, to scale", 36, acc, w="ExtraBold", a=ease((bp - 0.8) / 0.2))
        return
    if mode == "voyager":
        bh7(img, cx, cy, RS_AU7 * kfit * 0.8, t); k = kfit * 0.8
        solar7(img, cx, cy, k, t, labels=False)
        dist = 173.1 * bp; ang = math.radians(-35)
        x1, y1 = cx + dist * k * math.cos(ang), cy + dist * k * math.sin(ang)
        d = ImageDraw.Draw(img); d.line([(cx, cy), (x1, y1)], fill=acc2, width=4)
        R.paste_c(img, R.radial(40, [(0, (255, 255, 255, 255)), (1, acc2 + (0,))]), x1, y1)
        out = dist > RS_AU7
        text(img, (x1 - 40, y1 - 50), "VOYAGER 1", 34, acc2, anchor="mm")
        yr = 1977.7 + (2026.9 - 1977.7) * bp
        d.rounded_rectangle([cx - 300, 1330, cx + 300, 1500], 26, fill=(10, 8, 16))
        d.text((cx, 1385), f"{int(yr)}", font=F(84, "Black"), fill=acc2, anchor="mm")
        d.text((cx, 1460), "OUTSIDE, BARELY" if out else "still inside", font=F(36, "ExtraBold"), fill=(140, 255, 160) if out else (255, 255, 255), anchor="mm")
        return
    bh7(img, cx, cy, RS_AU7 * kfit, t)
    if mode == "hook":
        solar7(img, cx, cy, kfit, t)
        if v.get("rows"):
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rr = 30.07 * kfit
            for j in range(4):
                x = cx - RS_AU7 * kfit + rr + j * 2 * rr * 1.0 + 6 * j
                q = ease((t - 0.3 - j * 0.35) / 0.4)
                if q > 0: dl.ellipse([x - rr, cy - rr, x + rr, cy + rr], outline=acc + (int(230 * q),), width=4)
            img.alpha_composite(lay)
            text(img, (cx, cy + 300), "Neptune's orbit, 4 times across", 38, acc, w="ExtraBold", a=ease((t - 1.2) / 0.4))
    elif mode == "mass":
        R.paste_c(img, R.sun_sprite(6), cx + 380, cy - 420)
        text(img, (cx + 380, cy - 470), "our Sun", 32, (255, 225, 180), w="Bold")
        d = ImageDraw.Draw(img); n = 6.5e9 * bp
        d.text((cx, cy), f"{n:,.0f}", font=F(84, "Black"), fill=(255, 255, 255), anchor="mm")
        d.text((cx, cy + 80), "Suns of mass", font=F(40, "ExtraBold"), fill=acc, anchor="mm")
        text(img, (cx, cy + 560), "M87*: the first black hole ever photographed (EHT, 2019)", 30, (200, 205, 225), w="SemiBold")
    elif mode == "light":
        p = (t * 0.25) % 1.0; x0 = cx - RS_AU7 * kfit; x = lerp(x0, cx + RS_AU7 * kfit, bp)
        d = ImageDraw.Draw(img); d.line([(x0, cy), (x, cy)], fill=(255, 245, 170), width=5)
        R.paste_c(img, R.radial(70, [(0, (255, 255, 255, 255)), (1, (255, 240, 160, 0))]), x, cy)
        d.text((cx, cy - 120), f"{35.6 * bp:.1f} h", font=F(110, "Black"), fill=(255, 245, 170), anchor="mm")
        d.text((cx, cy + 110), "for light to cross it", font=F(40, "ExtraBold"), fill=(255, 255, 255), anchor="mm")

# ---- scale08: the Moon's whole orbit inside the Sun (Earth at the Sun's centre, everything TO SCALE: Sun r 696,000 km, Moon orbit r 384,400 km) ----
SUN_R8, MOON_A8, MOON_APO8, EARTH_R8, MOON_R8 = 696000, 384400, 405500, 6371, 1737
_sun8 = None
def sun_slice8(img, cx, cy, rpx, t, a=1.0):
    """the Sun as a translucent disc so what's inside shows through: limb glow + soft granulation rings"""
    global _sun8
    if a <= 0: return
    if _sun8 is None:
        _sun8 = R.radial(int(470 * 2.9), [(0, (255, 170, 60, 120)), (0.66, (255, 140, 40, 110)), (0.69, (255, 230, 150, 230)), (0.72, (255, 150, 50, 120)), (1, (255, 100, 20, 0))])
    spr = _sun8 if abs(rpx - 470) < 1 else _sun8.resize((int(rpx * 2.9), int(rpx * 2.9)), Image.BILINEAR)
    R.paste_c(img, spr, cx, cy, a)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); rng = random.Random(8)
    for i in range(70):
        ang = rng.uniform(0, 2 * math.pi); rr = rpx * math.sqrt(rng.uniform(0.0, 0.92)); sz = rng.uniform(10, 30) * (1 + 0.15 * math.sin(t * 2 + i))
        x, y = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
        dl.ellipse([x - sz * 0.6, y - sz * 0.6, x + sz * 0.6, y + sz * 0.6], fill=(255, 200, 110, 14))
    img.alpha_composite(lay)

def moonorbit_vis(img, v, th, t, dur, bp):
    """mode hook (translucent Sun, Earth at its centre, the Moon's orbit drawn inside, Moon circling) | orbit (zoom in from Earth to the
    Moon's orbit, distance counter) | room (radius bars: 384,400 vs 696,000 km, the 311,600 km to spare highlighted) | trip (an Apollo-pace
    dot crosses the Sun's diameter, days counter to 11.5)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy = W / 2, 930
    rpx = 470; k = rpx / SUN_R8
    if mode == "orbit":
        z = math.exp(lerp(math.log(rpx / 20000.0), math.log(k), min(1.0, bp / 0.7)))  # px per km: start near Earth, end at the hook scale
        sun_slice8(img, cx, cy, rpx, t, a=ease((bp - 0.7) / 0.3))
    else:
        z = k; sun_slice8(img, cx, cy, rpx, t)
    d = ImageDraw.Draw(img)
    mo = MOON_A8 * z
    if mode != "trip":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.ellipse([cx - mo, cy - mo, cx + mo, cy + mo], outline=acc2 + (230,), width=4)
        img.alpha_composite(lay)
        er = max(5, EARTH_R8 * z); R.paste_c(img, R.earth_sprite(int(er), glow=None), cx, cy)
        ang = -math.pi / 2 + t * 0.6; mx, my = cx + mo * math.cos(ang), cy + mo * math.sin(ang)
        R.paste_c(img, R.planet_sprite(max(7, int(MOON_R8 * z)), (225, 225, 230)), mx, my)
        d = ImageDraw.Draw(img)
        if MOON_R8 * z < 7: d.ellipse([mx - 22, my - 22, mx + 22, my + 22], outline=(255, 255, 255), width=3)
        if mode in ("hook", "orbit"):
            text(img, (cx, cy + mo + 46), "the Moon's orbit", 36, acc2, w="ExtraBold")
            text(img, (cx + 70, cy - 30), "Earth", 30, (170, 210, 255), w="Bold", anchor="lm")
        if mode == "orbit":
            text(img, (W / 2, 1450), f"{MOON_A8 * min(1, bp * 1.6):,.0f} km", 64, acc2)
        if mode == "hook":
            text(img, (W / 2, 1440), "to scale", 36, (230, 232, 240), w="ExtraBold")
    if mode == "room":
        y1, y2 = 1360, 1440; x0 = cx
        ln = MOON_A8 * z * min(1, bp * 1.5); ls = SUN_R8 * z * min(1, bp * 1.5)
        d.line([(x0, cy), (x0 + ls, cy)], fill=acc, width=5); d.line([(x0, cy - 14), (x0 + ln, cy - 14)], fill=acc2, width=5)
        d.rounded_rectangle([100, y1 - 40, 980, y2 + 70], 24, fill=(14, 8, 4))
        d.text((140, y1), "Moon's distance", font=F(34, "Bold"), fill=acc2, anchor="lm"); d.text((940, y1), "384,400 km", font=F(40, "Black"), fill=acc2, anchor="rm")
        d.text((140, y2), "Sun's radius", font=F(34, "Bold"), fill=acc, anchor="lm"); d.text((940, y2), "696,000 km", font=F(40, "Black"), fill=acc, anchor="rm")
        if bp > 0.6:
            q = ease((bp - 0.6) / 0.3)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            dl.rectangle([x0 + MOON_A8 * z, cy - 40, x0 + SUN_R8 * z, cy + 40], fill=(140, 255, 160, int(90 * q)))
            img.alpha_composite(lay)
            text(img, (W - 40, cy - 80), "311,600 km", 40, (160, 255, 170), w="Black", a=q, anchor="rm")
            text(img, (W - 40, cy + 80), "to spare", 34, (160, 255, 170), w="ExtraBold", a=q, anchor="rm")
    if mode == "trip":
        x0, x1 = cx - rpx, cx + rpx; x = lerp(x0, x1, bp)
        d.line([(x0, cy), (x, cy)], fill=(255, 255, 255), width=4)
        R.paste_c(img, R.radial(60, [(0, (255, 255, 255, 255)), (1, acc2 + (0,))]), x, cy)
        d = ImageDraw.Draw(img)
        # the Moon trip at the same pace, for scale: Earth -> Moon in 3.2 days
        mo_px = MOON_A8 * z; yy = cy + rpx + 110
        d.line([(x0, yy), (x0 + mo_px, yy)], fill=acc2, width=6); d.text((x0, yy - 30), "Earth to Moon: 3.2 days (Apollo 11)", font=F(30, "Bold"), fill=acc2, anchor="lm")
        d.rounded_rectangle([cx - 230, cy - 230, cx + 230, cy - 80], 24, fill=(14, 8, 4))
        d.text((cx, cy - 170), f"{11.5 * bp:.1f} days", font=F(72, "Black"), fill=(255, 255, 255), anchor="mm")
        d.text((cx, cy - 110), "at Apollo's pace", font=F(30, "ExtraBold"), fill=acc, anchor="mm")

# ---- scale09: every other planet poured into Jupiter, by volume ----
VOL9 = {"Jupiter": 143128.0, "Saturn": 82713.0, "Uranus": 6833.0, "Neptune": 6254.0, "Earth": 108.321, "Venus": 92.843, "Mars": 16.318, "Mercury": 6.083}  # 10^10 km^3, NASA fact sheet
COL9 = {"Saturn": (226, 196, 130), "Uranus": (150, 225, 230), "Neptune": (80, 120, 240), "Earth": (90, 170, 255), "Venus": (240, 200, 140), "Mars": (220, 110, 70), "Mercury": (170, 165, 160)}
POUR9 = ["Saturn", "Uranus", "Neptune", "Venus", "Earth", "Mars", "Mercury"]
RKM9 = {"Saturn": 58232, "Uranus": 25362, "Neptune": 24622, "Earth": 6371, "Venus": 6052, "Mars": 3390, "Mercury": 2440}
_jf9 = {}
def _h9(f):
    """height (fraction of the diameter) of a liquid filling fraction f of a sphere's volume: f = x^2 (3 - 2x) with x = h / 2R"""
    lo, hi = 0.0, 1.0
    for _ in range(40):
        m = (lo + hi) / 2
        if m * m * (3 - 2 * m) < f: lo = m
        else: hi = m
    return (lo + hi) / 2
def jupfill_vis(img, v, th, t, dur, bp):
    """Jupiter as a glass globe (r 430 px) filled by volume with the other planets as coloured layers; vis.mode = hook (full: all seven
    poured, 67% line) | pour (vis.add = planets poured in this beat: each falls in to scale, then the level rises) | room (empty third
    glows + Earth-sized dots counter up to 435)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy, Rj = W / 2, 960, 430
    add = v.get("add", []); before = v.get("before", [])
    if mode in ("hook", "room"): before, add = POUR9, []
    prog = {n: 1.0 for n in before}
    for i, n in enumerate(add):
        prog[n] = ease((bp - i / max(1, len(add))) * max(1, len(add)))
    key = int(cx)
    if "base" not in _jf9: _jf9["base"] = R.jup10(Rj, 0.0)
    base = _jf9["base"].copy(); al = base.getchannel("A").point(lambda q: int(q * 0.38)); base.putalpha(al)
    R.paste_c(img, base, cx, cy)
    # liquid layers
    size = 2 * Rj; yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    inside = ((xx - Rj) ** 2 + (yy - Rj) ** 2) <= (Rj - 3) ** 2
    hfrac = 1 - yy / size  # 0 at the bottom
    rgba = np.zeros((size, size, 4), np.float32); cum = 0.0
    for n in POUR9:
        p = prog.get(n, 0.0)
        if p <= 0: continue
        f0 = cum; cum += VOL9[n] / VOL9["Jupiter"] * p
        h0, h1 = _h9(f0), _h9(cum); band = inside & (hfrac >= h0) & (hfrac < max(h1, h0 + 0.004 if n in ("Earth", "Venus", "Mars", "Mercury") else h1))
        c = COL9[n]; rgba[band, 0], rgba[band, 1], rgba[band, 2], rgba[band, 3] = c[0], c[1], c[2], 225
    wave = (np.sin(xx / 30 + t * 3) * 0.004)
    lay = Image.fromarray(rgba.astype(np.uint8), "RGBA"); img.alpha_composite(lay, (int(cx - Rj), int(cy - Rj)))
    d = ImageDraw.Draw(img)
    d.ellipse([cx - Rj, cy - Rj, cx + Rj, cy + Rj], outline=(255, 225, 180), width=5)
    lvl = cy + Rj - 2 * Rj * _h9(cum)
    if cum > 0:
        hw = math.sqrt(max(0, Rj ** 2 - (lvl - cy) ** 2))
        d.line([(cx - hw, lvl), (cx + hw, lvl)], fill=(255, 255, 255), width=4)
        text(img, (cx, lvl + 50), f"{cum * 100:.1f}% full", 46, (255, 255, 255), stroke=4)
    # falling planets to scale
    for i, n in enumerate(add):
        p0 = (bp - i / max(1, len(add))) * max(1, len(add))
        if 0 < p0 < 1:
            r = RKM9[n] / 71492 * Rj; y = lerp(300 - r, lvl, ease(min(1, p0 * 1.4)))
            R.paste_c(img, R.planet_sprite(max(4, int(r)), COL9[n]), cx + (i - 1) * 60, y, a=1 - max(0, (p0 - 0.7) / 0.3))
            d = ImageDraw.Draw(img); text(img, (cx + (i - 1) * 60, y - r - 40), n, 40, COL9[n], w="Black", stroke=3)
    if mode == "room":
        q = 0.5 + 0.5 * math.sin(t * 4)
        mask = inside & (hfrac >= _h9(cum)); g = np.zeros((size, size, 4), np.uint8); g[mask] = (140, 255, 170, int(40 + 50 * q))
        img.alpha_composite(Image.fromarray(g, "RGBA"), (int(cx - Rj), int(cy - Rj)))
        n_e = int(435 * min(1, bp * 1.2)); er = 6371 / 71492 * Rj
        R.paste_c(img, R.earth_sprite(int(er), glow=None), cx, cy - Rj * 0.55)
        text(img, (cx, cy - Rj * 0.55 + er + 34), "1 Earth, to scale", 32, (200, 230, 255), w="ExtraBold", stroke=3)
        text(img, (W / 2, 1460), f"{n_e} Earths fit in the gap", 50, (160, 255, 180))
    if mode == "hook":
        text(img, (W / 2, 1460), "all 7 other planets, by volume", 40, (235, 235, 245), w="ExtraBold")

def chrome(img, th, gt, total):
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, int(W * gt / total), 10], fill=tuple(th["accent"]))
    d.text((W / 2, 1720), HANDLE, font=F(34, "Bold"), fill=R.CYAN, anchor="mm")

def frame(m, durs, gt, chunks, arr):
    th = m.THEME; beats = m.BEATS; total = sum(durs); acc = 0
    for i, (b, d) in enumerate(zip(beats, durs)):
        if gt < acc + d: break
        acc += d
    t = gt - acc; v = b["vis"]
    img = K.bg(gt, th)
    if v["type"] == "gap":
        tot_km, gap_km = gap_vis(img, v, th, gt, t, d, arr)
        # headline (always on: the number is on screen from frame 0)
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 120), hl["num"], 118 if len(hl["num"]) < 12 else 96, tuple(th["accent"]))
        text(img, (W / 2, 215), hl["top"], 50, (255, 255, 255))
        if v.get("show_total"):
            p = 1.0 if v.get("moon") == "mean" else easeio((t - 0.3) / 1.2)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([20, 1090, 420, 1450], 26, fill=(8, 10, 24, 225), outline=tuple(th["accent"]) + (160,), width=3); img.alpha_composite(lay)
            dd = ImageDraw.Draw(img)
            dd.text((220, 1135), "7 planets, side by side", font=F(28, "Bold"), fill=(200, 205, 220), anchor="mm")
            dd.text((220, 1195), f"{tot_km * p:,.0f} km", font=F(58, "Black"), fill=tuple(th["accent"]), anchor="mm")
            dd.text((220, 1265), "gap tonight" if v.get("moon") == "mean" else "gap, Moon at its farthest", font=F(28, "Bold"), fill=(200, 205, 220), anchor="mm")
            dd.text((220, 1325), f"{gap_km:,.0f} km", font=F(58, "Black"), fill=tuple(th["accent2"]), anchor="mm")
            diff = gap_km - tot_km
            dd.text((220, 1400), (f"{diff:,.0f} km to spare" if diff >= 0 else f"{-diff:,.0f} km too long"), font=F(34, "ExtraBold"), fill=(140, 255, 160) if diff >= 0 else (255, 110, 110), anchor="mm")
        if v.get("sub"): text(img, (W / 2, 290), v["sub"], 40, tuple(th["accent2"]), w="ExtraBold")
    elif v["type"] == "inside":
        inside_vis(img, v, th, gt, t, d)
    elif v["type"] == "storm":
        storm_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.75)))
        sh = Image.new("RGBA", (W, 330), (0, 0, 0, 0)); a_ = np.zeros((330, W), np.uint8) + np.linspace(200, 0, 330).astype(np.uint8)[:, None]
        sh.putalpha(Image.fromarray(a_)); img.alpha_composite(sh)
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 140), hl["num"], 124 if len(hl["num"]) < 12 else 96, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 245), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "thinring":
        thinring_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.75)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 160), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 265), hl["top"], 50, (255, 255, 255), stroke=3)
    elif v["type"] == "fillsun":
        fillsun_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "mapfit":
        mapfit_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "bhfit":
        bhfit_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "moonorbit":
        moonorbit_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "jupfill":
        jupfill_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "starinside":
        starinside_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.75)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 160), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 265), hl["top"], 52, (255, 255, 255), stroke=3)
    chrome(img, th, gt, total)
    K.draw_caption(img, chunks, gt, y=1590)
    return img

def tts(beats, outdir, voice):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(R.HERE, "models/kokoro.onnx"), os.path.join(R.HERE, "models/voices.bin"))
    speed = float(os.environ.get("SPEED", "1.05")); durs, chunks = [], []
    for i, b in enumerate(beats):
        cache = os.path.join(outdir, f"beat_{i:02d}.wav"); key = f"{voice}|{speed}|{b['say']}"
        if os.path.exists(cache) and open(cache + ".txt").read() == key: a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(b["say"], voice=voice, speed=speed, lang="en-us"); sf.write(cache, a, sr); open(cache + ".txt", "w").write(key)
        lead = 0.0 if i == 0 else 0.08  # hook starts on frame 0
        a = np.concatenate([np.zeros(int(sr * lead)), a, np.zeros(int(sr * (0.15 if i == len(beats) - 1 else 0.3)))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    tt = np.arange(len(audio)) / sr
    drone = (np.sin(2 * np.pi * 41 * tt) * 0.5 + np.sin(2 * np.pi * 61.5 * tt) * 0.3 + np.sin(2 * np.pi * 82.3 * tt) * 0.2) * 0.035
    audio = (audio + drone).astype(np.float32); audio /= max(1.0, np.abs(audio).max() / 0.95)
    sf.write(os.path.join(outdir, "voice.wav"), audio, sr)
    return durs

def main():
    m = load(sys.argv[1]); outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    if "--preview" in sys.argv:
        durs = [6.0] * len(m.BEATS); arr = schedule(m.BEATS, durs)
        for i in range(len(m.BEATS)):
            for k2, tt in enumerate((0.0, 5.5)):
                frame(m, durs, i * 6 + tt, [], arr).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}_{k2}.jpg"), quality=80)
        print("preview ok"); return
    durs = tts(m.BEATS, outdir, os.environ.get("VOICE", "af_heart"))
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w")); total = sum(durs); print("total", round(total, 1), "s")
    arr = schedule(m.BEATS, durs); chunks = []; acc = 0
    for b, d in zip(m.BEATS, durs): chunks += K.caption_chunks(b["say"], acc - (0.2 if acc == 0 else 0), d); acc += d
    out = os.path.join(outdir, "scale.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voice.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        p.stdin.write(frame(m, durs, f / FPS, chunks, arr).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    main()
