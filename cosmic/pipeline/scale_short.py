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
  "ballearth": a Terra encolhida para uma bola de basquete (23,9 cm; 12.742 km -> 1 mm = 53,3 km); vis.mode = hook (bola + anel da estação
             espacial a 7,5 mm) | shrink (Terra -> bola, contador km -> cm, costuras aparecem) | edge (lupa na borda: limite do espaço
             100 km = 1,9 mm x moeda 1,75 mm) | iss (lupa: 400 km = 7,5 mm x lápis 7 mm) | moon (câmera corre 7,2 m até a Lua do tamanho de
             uma bola de tênis, contador em metros) (scale10).
  "marble": a Terra espremida numa bolinha de gude = buraco negro (diâmetro de Schwarzschild 17,7 mm); vis.mode = hook (buraco negro sobre
             régua em cm em tamanho real) | mass (balança Terra x bolinha) | squeeze (Terra encolhe em escala log passando por Lua, cidade,
             campo, pessoa, bolinha; flash) | sun (Sol espremido = 5,9 km; bonequinho andando numa barra 0–6 km) | star (estrela gigante
             colapsa) (scale11).
  "dwarf": Sirius B, anã branca menor que a Terra com a massa do Sol; vis.mode = hook (Terra em cima x Sirius B embaixo EM ESCALA,
             12.742 x 11.270 km) | mass (balança Sol x Sirius B, contador até 339 mil Terras) | spoon (colher de chá = 13,5 t x 2 elefantes) |
             gravity (régua log 1 -> 433.000 g, peso de uma pessoa de 70 kg) | sirius (Sirius A + B na órbita de 50 anos) (scale12).
  "jupsun": o Sol EM ESCALA contra Júpiter (raio 9,95×); vis.mode = hook (Sol cheio de Júpiteres em escala, fatia 2D) | row (Júpiteres
             rolam no diâmetro, contador até 9,7) | fill (chovem Júpiteres, contador até 986 por volume) | earth (zoom num Júpiter + Terra em
             escala, contador até 1.321) | density (dois potes: Sol 1,41 x Júpiter 1,33 g/cm³, linha da água) | mass (grade de 1.048 pontos
             = massas de Júpiter, os 986 do volume em outra cor) (scale13).
  "andromeda": céu noturno com morros; Lua cheia e Andrômeda NA MESMA ESCALA ANGULAR (eixo longo = 6 Luas, ~3° x 0,5°); vis.mode = hook
             | row (6 Luas deslizam ao longo do eixo) | eye (a galáxia some e sobra a mancha do núcleo, o que o olho vê) | light (pulso de luz
             Andrômeda -> Terra, linha do tempo 2,5 milhões de anos com o surgimento da nossa espécie) | photo (moldura de câmera, contador
             de exposição, o disco aparece) (scale14).
  "redgiant": Betelgeuse (raio ~700 Sóis) EM ESCALA contra o Sol; vis.mode = hook (disco gigante cortando a tela + o Sol = ponto de 1,6 px
             circulado) | zoom (zoom log do Sol até Betelgeuse, contador "× wider" até 700) | cube (cubo isométrico 7×7×7, cada bloco =
             1 milhão de Sóis, contador até 343 milhões) | earths (equação 1 Sol = 1,3 mi Terras × 343 mi = 447 trilhões) | orbits (no lugar
             do Sol: órbitas Mercúrio–Marte + cinturão de asteroides em escala, superfície em 3,26 UA) | orion (céu com Órion em pontos e linhas,
             Betelgeuse pulsando) (scale15).
  "sand"  : o Sol encolhido a um grão de areia de 1 mm (1 mm = 1.391.400 km); vis.mode = hook (ponta do dedo com o grão + ponto no horizonte
             = próxima estrela, linha tracejada) | earth (régua 0–12 cm, Terra a 10,8 cm + lupa: Terra de 9 µm ao lado de um fio de cabelo) |
             ruler (pista 0–20 m: Terra, Netuno 3,2 m, Voyager 1 18,6 m, pessoa de 1,7 m) | gap (estrada até o horizonte, contador 0 -> 28,9 km
             e horas a pé) | galaxy (Terra, Lua a 384.400 km e a Via Láctea nessa escala, 680.000 km, tudo em escala) (scale16).
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

# ---- scale10: Earth shrunk to a basketball (24 cm): edge of space 1.9 mm, ISS 7.5 mm, Moon 7.2 m ----
BALL_KM10 = 12742.0; BALL_CM10 = 23.9
def _ball10(img, cx, cy, r, seams=1.0, t=0.0):
    R.paste_c(img, R.earth_sprite(int(r), glow=None), cx, cy)
    if seams > 0:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); A = int(150 * seams)
        d.line([(cx - r, cy), (cx + r, cy)], fill=(20, 20, 30, A), width=max(2, int(r * 0.02)))
        d.line([(cx, cy - r), (cx, cy + r)], fill=(20, 20, 30, A), width=max(2, int(r * 0.02)))
        for sx_ in (-1, 1):
            d.arc([cx + sx_ * r * 0.55 - r * 0.9, cy - r * 0.95, cx + sx_ * r * 0.55 + r * 0.9, cy + r * 0.95],
                  90 if sx_ < 0 else 270, 270 if sx_ < 0 else 90, fill=(20, 20, 30, A), width=max(2, int(r * 0.02)))
        m = Image.new("L", img.size, 0); ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
        lay.putalpha(Image.fromarray(np.minimum(np.array(lay.getchannel("A")), np.array(m)))); img.alpha_composite(lay)
        d = ImageDraw.Draw(img); d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(230, 140, 60), width=max(2, int(r * 0.025)))

def _lens10(img, cx, cy, lr, ball_cx, ball_cy, br, th, alt_mm, ref, t, bp):
    """magnifier on the ball's edge: px_per_mm chosen so the layer fills ~85% of the lens; ref = (label, mm, colour)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"])
    d = ImageDraw.Draw(img)
    d.line([(ball_cx + br * 0.71, ball_cy - br * 0.71), (cx - lr * 0.71, cy + lr * 0.71)], fill=(200, 205, 230), width=4)
    lay = Image.new("RGBA", (2 * lr, 2 * lr), (6, 8, 20, 255)); dl = ImageDraw.Draw(lay)
    ppm = lr * 1.25 / max(alt_mm, ref[1])
    gy = lr * 1.55  # ground line inside the lens
    dl.rectangle([0, gy, 2 * lr, 2 * lr], fill=(60, 110, 200, 255))
    dl.rectangle([0, gy, 2 * lr, gy + 10], fill=(140, 200, 255, 255))
    for k in range(18):  # atmosphere glow, fading with height
        y = gy - k * 0.25 * ppm
        dl.rectangle([0, y - 0.25 * ppm, 2 * lr, y], fill=(90, 160, 255, int(70 * (1 - k / 18) ** 2)))
    a = ease(bp * 2)
    ya = gy - alt_mm * ppm * a
    dl.line([(0, ya), (2 * lr, ya)], fill=acc + (255,), width=4)
    # reference object, to scale, standing on the ground
    rx = lr * (1.2 if ref[0].startswith("pencil") else 1.45); rh = ref[1] * ppm
    if ref[0].startswith("pencil"):
        rr = rh / 2; dl.regular_polygon((rx, gy - rr, rr), 6, fill=(250, 200, 60, 255)); dl.ellipse([rx - rr * 0.3, gy - rr * 1.3, rx + rr * 0.3, gy - rr * 0.7], fill=(60, 50, 40, 255))
    else:
        dl.rounded_rectangle([rx - 70, gy - rh, rx + 70, gy], 6, fill=(200, 200, 210, 255), outline=(255, 255, 255, 255), width=2)
    m = Image.new("L", (2 * lr, 2 * lr), 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * lr - 1, 2 * lr - 1], fill=255); lay.putalpha(m)
    img.alpha_composite(lay, (int(cx - lr), int(cy - lr)))
    d = ImageDraw.Draw(img); d.ellipse([cx - lr, cy - lr, cx + lr, cy + lr], outline=(230, 235, 255), width=8)
    text(img, (cx - lr * 0.35, cy - lr + (gy - alt_mm * ppm * a) - 34), f"{alt_mm * a:.1f} mm", 44, acc, stroke=4)
    text(img, (cx + lr * 0.45, cy + lr + 44), ref[0], 34, (240, 230, 200), w="ExtraBold", stroke=3)

def ballearth_vis(img, v, th, t, dur, bp):
    """Earth shrunk to a basketball; vis.mode = hook (ball + ISS ring 7.5 mm up, ISS orbiting) | shrink (Earth -> ball, size counter
    12,742 km -> 24 cm, seams fade in) | edge (lens on the rim: edge of space 1.9 mm vs a coin 1.75 mm) | iss (lens: ISS 7.5 mm vs a
    pencil 7 mm) | moon (camera pans 7.2 m from the ball to a tennis-ball Moon, metre counter)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); k = BALL_CM10 * 10 / BALL_KM10  # mm per km
    if mode == "hook":
        cx, cy, r = W / 2, 930, 330
        _ball10(img, cx, cy, r, 1.0, t)
        rr = r * (1 + 400 / 6371.0); d = ImageDraw.Draw(img)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=acc2, width=3)
        ang = -1.0 + t * 0.9; ix, iy = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
        d.rectangle([ix - 14, iy - 3, ix + 14, iy + 3], fill=(230, 230, 240)); d.rectangle([ix - 3, iy - 8, ix + 3, iy + 8], fill=(200, 170, 90))
        text(img, (cx + r * 0.62, cy - r - 70), "space station", 40, acc2, w="ExtraBold", stroke=3)
        text(img, (W / 2, 1420), "Earth = one basketball", 46, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "shrink":
        cx, cy = W / 2, 930; p = bp
        r = lerp(470, 330, p); _ball10(img, cx, cy, r, max(0.0, (p - 0.5) * 2), t)
        km = 10 ** lerp(math.log10(BALL_KM10 * 1e5), math.log10(BALL_CM10), p)  # in cm
        s = f"{km / 1e5:,.0f} km" if km >= 1e5 else (f"{km / 100:,.0f} m" if km >= 100 else f"{km:,.0f} cm")
        d = ImageDraw.Draw(img); d.line([(cx - r, cy + r + 40), (cx + r, cy + r + 40)], fill=acc2, width=5)
        for x in (cx - r, cx + r): d.line([(x, cy + r + 25), (x, cy + r + 55)], fill=acc2, width=5)
        text(img, (cx, cy + r + 100), s, 70, acc2, stroke=4)
    elif mode in ("edge", "iss"):
        bcx, bcy, br = 330, 1050, 230
        _ball10(img, bcx, bcy, br, 1.0, t)
        if mode == "edge": _lens10(img, 700, 720, 300, bcx, bcy, br, th, 100 * k, ("coin: 1.75 mm thick", 1.75), t, bp)
        else: _lens10(img, 700, 720, 300, bcx, bcy, br, th, 400 * k, ("pencil: 7 mm wide", 7.0), t, bp)
        text(img, (W / 2, 1420), "edge of space (100 km)" if mode == "edge" else "space station (400 km)", 44, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "moon":
        ppcm = 6.0  # px per cm
        dist_cm = 384400 * k / 10; off = easeio(bp) * (180 + dist_cm * ppcm - (W - 260))
        y = 900; bx = 180 - off; mx = bx + dist_cm * ppcm
        d = ImageDraw.Draw(img)
        d.line([(max(0, bx), y + 120), (min(W, mx), y + 120)], fill=acc2, width=4)
        for m_ in range(0, 8):
            x = bx + m_ * 100 * ppcm
            if -50 < x < W + 50:
                d.line([(x, y + 100), (x, y + 140)], fill=acc2, width=4); d.text((x, y + 170), f"{m_} m", font=F(34, "Bold"), fill=acc2, anchor="mm")
        _ball10(img, bx, y, BALL_CM10 / 2 * ppcm, 1.0, t)
        R.paste_c(img, R.planet_sprite(max(4, int(3474.8 * k / 20 * ppcm)), (190, 190, 195)), mx, y)
        if mx < W + 40: text(img, (mx, y - 80), "the Moon: a tennis ball", 36, (230, 230, 240), w="ExtraBold", stroke=3, anchor="mm")
        text(img, (W / 2, 640), f"{easeio(bp) * dist_cm / 100:.1f} m", 110, acc, stroke=4)
        text(img, (W / 2, 1420), "Earth to Moon, same scale", 44, (255, 255, 255), w="ExtraBold", stroke=3)

# ---- scale11: Earth squeezed into a marble = a black hole (Schwarzschild diameter 17.7 mm) ----
def _marble11(img, cx, cy, r, t, a=1.0):
    """black hole the size of a marble: shadow + photon ring + glow (bh_static scaled so the shadow diameter = 2r)"""
    spr = R.bh_static(int(r / 1.42)); R.paste_c(img, spr, cx, cy, a)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.ellipse([cx - r * 0.55, cy - r * 0.75, cx - r * 0.15, cy - r * 0.45], fill=(255, 255, 255, int(40 * a)))
    img.alpha_composite(lay)

def _ruler11(img, x0, y, ppcm, ncm, th, a=1.0):
    d = ImageDraw.Draw(img); lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.rounded_rectangle([x0 - 20, y, x0 + ncm * ppcm + 20, y + 110], 10, fill=(235, 215, 160, int(240 * a))); img.alpha_composite(lay)
    d = ImageDraw.Draw(img)
    for mm in range(0, ncm * 10 + 1):
        x = x0 + mm * ppcm / 10; h = 50 if mm % 10 == 0 else (32 if mm % 5 == 0 else 18)
        d.line([(x, y), (x, y + h)], fill=(40, 30, 20), width=3 if mm % 10 == 0 else 2)
        if mm % 10 == 0: d.text((x, y + 80), f"{mm // 10}", font=F(30, "Black"), fill=(40, 30, 20), anchor="mm")
    d.text((x0 + ncm * ppcm - 10, y + 80), "cm", font=F(26, "Bold"), fill=(40, 30, 20), anchor="rm")

SQ11 = [(12742e3, "Earth"), (3474.8e3, "the Moon's size"), (20e3, "a city"), (100.0, "a football field"), (1.7, "a person"), (0.0177, "a marble")]
def marble_vis(img, v, th, t, dur, bp):
    """Earth squeezed into a marble-sized black hole; vis.mode = hook (marble black hole over a real-size cm ruler: 1.77 cm) | mass (balance:
    Earth vs the marble, level) | squeeze (Earth shrinks on a log scale past Moon / city / field / person / marble, counter in km -> cm;
    ends in a flash) | sun (the Sun squeezed: 5.9 km across, walking figure on a 0–6 km bar, ~1 h 10 min) | star (giant star collapses)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook")
    if mode == "hook":
        ppcm = 150; cx, cy = W / 2, 860; r = 1.774 / 2 * ppcm
        _marble11(img, cx, cy, r, t)
        x0 = cx - r; _ruler11(img, cx - 1.5 * ppcm - r * 0 , 1100, ppcm, 3, th)
        d = ImageDraw.Draw(img)
        for x in (cx - r, cx + r): d.line([(x, cy + r + 10), (x, 1095)], fill=acc2, width=3)
        text(img, (W / 2, 1300), "all of Earth's mass", 48, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "mass":
        cx, py = W / 2, 760; tilt = 0.06 * math.sin(t * 2.2) * (1 - min(1, bp * 1.3))
        d = ImageDraw.Draw(img); L = 380
        lx, ly = cx - L * math.cos(tilt), py - L * math.sin(tilt); rx, ry = cx + L * math.cos(tilt), py + L * math.sin(tilt)
        d.polygon([(cx, py), (cx - 70, py + 520), (cx + 70, py + 520)], fill=(70, 75, 110)); d.line([(lx, ly), (rx, ry)], fill=(210, 215, 240), width=12)
        for x, y in ((lx, ly), (rx, ry)):
            d.line([(x, y), (x - 110, y + 180)], fill=(170, 175, 200), width=3); d.line([(x, y), (x + 110, y + 180)], fill=(170, 175, 200), width=3)
            d.arc([x - 130, y + 140, x + 130, y + 220], 0, 180, fill=(210, 215, 240), width=8)
        R.paste_c(img, R.earth_sprite(110, glow=None), lx, ly + 75)
        _marble11(img, rx, ry + 170, 14, t)
        text(img, (lx, ly + 260), "Earth", 44, (140, 200, 255), stroke=3); text(img, (rx, ry + 260), "the marble", 44, acc, stroke=3)
        text(img, (W / 2, 1360), "5.97 × 10²⁴ kg each", 56, acc2, stroke=4)
    elif mode == "squeeze":
        cx, cy = W / 2, 900; p = min(1.0, bp * 1.08)
        lg = lerp(math.log10(SQ11[0][0]), math.log10(SQ11[-1][0]), p); size = 10 ** lg
        r = lerp(400, 30, p)
        if p < 0.995: R.paste_c(img, R.earth_sprite(max(4, int(r)), glow=None), cx, cy)
        else: _marble11(img, cx, cy, 30, t)
        if p > 0.95:
            fl = 1 - abs(p - 0.975) / 0.025; R.paste_c(img, R.radial(500, [(0, (255, 255, 255, int(255 * max(0, fl)))), (1, (255, 255, 255, 0))]), cx, cy)
        lab = [s for s in SQ11 if s[0] >= size * 0.999][-1][1]
        s = f"{size / 1e3:,.0f} km" if size >= 1e3 else (f"{size:,.0f} m" if size >= 1 else f"{size * 100:.1f} cm")
        text(img, (W / 2, 1360), s, 96, acc, stroke=4)
        text(img, (W / 2, 1450), "now: " + lab, 42, (255, 255, 255), w="ExtraBold", stroke=3)
        text(img, (W / 2, 420), "squeezed 720 million times", 44, acc2, w="ExtraBold", stroke=3, a=ease((p - 0.6) * 4))
    elif mode == "sun":
        y = 840; x0, x1 = 120, 960; kpx = (x1 - x0) / 6.0
        d = ImageDraw.Draw(img)
        rr = 5.907 / 2 * kpx; cx = x0 + rr
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([cx - rr, y - rr, cx + rr, y + rr], fill=(2, 2, 6, 255), outline=(255, 190, 110, 255), width=6)
        img.alpha_composite(R.radial(int(rr * 3), [(0, (255, 160, 60, 0)), (0.6, (255, 160, 60, 0)), (0.68, (255, 170, 80, 160)), (1, (255, 120, 40, 0))]), (int(cx - rr * 1.5), int(y - rr * 1.5)))
        img.alpha_composite(lay); d = ImageDraw.Draw(img)
        by = y + rr + 70; d.line([(x0, by), (x1, by)], fill=acc2, width=5)
        for km in range(7):
            x = x0 + km * kpx; d.line([(x, by - 15), (x, by + 15)], fill=acc2, width=4); d.text((x, by + 45), f"{km} km", font=F(28, "Bold"), fill=acc2, anchor="mm")
        p = easeio(bp); wx = x0 + p * 5.907 * kpx; ph = t * 8
        d.ellipse([wx - 12, by - 120, wx + 12, by - 96], fill=(255, 255, 255)); d.line([(wx, by - 96), (wx, by - 50)], fill=(255, 255, 255), width=6)
        for sgn in (-1, 1): d.line([(wx, by - 50), (wx + sgn * 16 * math.sin(ph), by - 8)], fill=(255, 255, 255), width=6)
        mins = p * 5.907 / 5 * 60
        text(img, (W / 2, 1450), f"walking across: {int(mins) // 60} h {int(mins) % 60:02d} min", 50, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "star":
        cx, cy = W / 2, 900; p = bp
        rs = 380 * (1 - ease((p - 0.35) / 0.4)) + 10
        if p < 0.78: R.paste_c(img, R.radial(int(rs * 2.6), [(0, (230, 240, 255, 255)), (0.33, (170, 200, 255, 255)), (0.4, (120, 160, 255, 120)), (1, (80, 120, 255, 0))]), cx, cy)
        else: _marble11(img, cx, cy, 40, t)
        if 0.72 < p < 0.86: R.paste_c(img, R.radial(700, [(0, (255, 255, 255, int(255 * (1 - abs(p - 0.79) / 0.07)))), (1, (255, 255, 255, 0))]), cx, cy)
        text(img, (W / 2, 1420), "only giant stars get crushed this far", 42, (255, 255, 255), w="ExtraBold", stroke=3)

def _dwarf12(img, cx, cy, r, t, a=1.0):
    """Sirius B: blue-white white dwarf with a tight hot glow"""
    R.paste_c(img, R.radial(max(8, int(r * 3.2)), [(0, (255, 255, 255, 255)), (0.5, (225, 235, 255, 255)), (0.625, (170, 195, 255, 255)),
                                                   (0.66, (140, 170, 255, 130)), (1, (110, 140, 255, 0))]), cx, cy, a)

def _elephant12(d, x, y, s, col=(190, 195, 215)):
    d.ellipse([x - 60 * s, y - 40 * s, x + 60 * s, y + 35 * s], fill=col)
    for k in (-42, -18, 18, 42): d.rectangle([x + k * s - 9 * s, y + 20 * s, x + k * s + 9 * s, y + 75 * s], fill=col)
    d.ellipse([x + 45 * s, y - 60 * s, x + 95 * s, y - 5 * s], fill=col)
    d.ellipse([x + 35 * s, y - 55 * s, x + 65 * s, y - 5 * s], fill=tuple(int(c * 0.85) for c in col))
    d.line([(x + 90 * s, y - 25 * s), (x + 100 * s, y + 20 * s), (x + 92 * s, y + 50 * s)], fill=col, width=int(12 * s))

def dwarf_vis(img, v, th, t, dur, bp):
    """Sirius B, a white dwarf smaller than Earth with the Sun's mass; vis.mode = hook (Earth on top vs Sirius B below, TO SCALE:
    12,742 vs 11,270 km) | mass (balance: the Sun vs the tiny dwarf, level; counter to 339,000 Earths) | spoon (teaspoon of its
    matter = 13.5 t; two elephants on the other side) | gravity (log meter 1 g -> 430,000 g, a person's weight counter) |
    sirius (Sirius A + B on their 50-year orbit, B's size exaggerated with a label)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); d = ImageDraw.Draw(img)
    if mode == "hook":
        k = 0.042  # px per km
        re_, rd = 12742 / 2 * k, 11270 / 2 * k
        R.paste_c(img, R.earth_sprite(int(re_), glow=(120, 180, 255)), W / 2, 680)
        _dwarf12(img, W / 2, 1185, rd, t)
        d = ImageDraw.Draw(img)
        for x in (W / 2 - re_, W / 2 + re_): d.line([(x, 680), (x, 1185)], fill=(140, 200, 255), width=2)
        text(img, (W / 2 + re_ + 10, 560), "Earth", 40, (140, 200, 255), stroke=3, anchor="lm")
        text(img, (W / 2 + rd + 10, 1330), "Sirius B", 40, acc2, stroke=3, anchor="lm")
        text(img, (W / 2, 1460), "12,742 km  vs  11,270 km", 44, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "mass":
        cx, py = W / 2, 760; L = 380; tilt = 0.25 * (1 - bp)
        lx, ly = cx - L * math.cos(tilt), py + L * math.sin(tilt); rx, ry = cx + L * math.cos(tilt), py - L * math.sin(tilt)
        d.polygon([(cx, py), (cx - 70, py + 520), (cx + 70, py + 520)], fill=(70, 75, 110)); d.line([(lx, ly), (rx, ry)], fill=(210, 215, 240), width=12)
        for x, y in ((lx, ly), (rx, ry)):
            d.line([(x, y), (x - 110, y + 180)], fill=(170, 175, 200), width=3); d.line([(x, y), (x + 110, y + 180)], fill=(170, 175, 200), width=3)
            d.arc([x - 130, y + 140, x + 130, y + 220], 0, 180, fill=(210, 215, 240), width=8)
        R.paste_c(img, R.sun_sprite(70), lx, ly + 100)
        _dwarf12(img, rx, ry + 168, 9, t)
        text(img, (lx, ly + 270), "the Sun", 44, (255, 200, 110), stroke=3); text(img, (rx, ry + 270), "Sirius B", 44, acc2, stroke=3)
        text(img, (W / 2, 1400), f"{339000 ** bp:,.0f} Earths of mass", 56, acc, stroke=4)
    elif mode == "spoon":
        sx, sy = 330, 900
        d.ellipse([sx - 120, sy - 70, sx + 120, sy + 70], fill=(200, 205, 220)); d.line([(sx + 110, sy - 10), (sx + 330, sy - 120)], fill=(200, 205, 220), width=26)
        _dwarf12(img, sx, sy - 10, 55, t)
        d = ImageDraw.Draw(img)
        text(img, (sx, sy + 140), "1 teaspoon", 44, acc2, stroke=3)
        n = 2 if bp > 0.5 else 1
        for k in range(n): _elephant12(d, 760, 760 + k * 230, 1.15)
        text(img, (760, 1240), f"{13.5 * bp:.1f} tonnes", 70, acc, stroke=4)
        text(img, (760, 1320), "≈ two elephants", 40, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "gravity":
        x0, x1, y = 120, W - 120, 1050; lo, hi = 0, 6
        def X(g): return lerp(x0, x1, (math.log10(g) - lo) / (hi - lo))
        d.line([(x0, y), (x1, y)], fill=(90, 95, 130), width=8)
        for e in range(7):
            x = X(10 ** e); d.line([(x, y - 14), (x, y + 14)], fill=(150, 155, 185), width=3)
            d.text((x, y + 44), f"{10 ** e:,}", font=F(24, "Bold"), fill=(150, 155, 185), anchor="mm")
        for g, lab, up in ((1, "Earth", 1), (2.5, "Jupiter", 0), (28, "the Sun", 1), (433000, "Sirius B", 0)):
            x = X(g); yy = y - 70 if up else y + 100
            d.ellipse([x - 10, y - 10, x + 10, y + 10], fill=acc2 if g > 1000 else (230, 230, 240)); d.text((x, yy), lab, font=F(30, "ExtraBold"), fill=acc2 if g > 1000 else (230, 230, 240), anchor="mm")
        g = 433000 ** bp; x = X(g); d.polygon([(x, y - 30), (x - 18, y - 60), (x + 18, y - 60)], fill=acc)
        text(img, (W / 2, 700), f"{70 * g:,.0f} kg", 96, acc, stroke=4)
        text(img, (W / 2, 790), "what a 70 kg person would weigh", 40, (255, 255, 255), w="ExtraBold", stroke=3)
        text(img, (W / 2, 1300), "surface gravity, × Earth's (log scale)", 34, (170, 175, 200), w="Bold")
    elif mode == "sirius":
        cx, cy = W / 2, 900; a_ = 380; b_ = 230; ang = 2 * math.pi * (0.15 + 0.12 * bp)
        d.ellipse([cx - a_ - 120, cy - b_, cx + a_ - 120, cy + b_], outline=(110, 120, 170), width=3)
        R.paste_c(img, R.radial(320, [(0, (255, 255, 255, 255)), (0.3, (220, 232, 255, 255)), (0.36, (170, 200, 255, 160)), (1, (120, 160, 255, 0))]), cx - 120 - a_ * 0.6, cy)
        bx, by = cx - 120 + a_ * math.cos(ang), cy + b_ * math.sin(ang); _dwarf12(img, bx, by, 10, t)
        d = ImageDraw.Draw(img)
        text(img, (cx - 120 - a_ * 0.6, cy + 140), "Sirius A", 44, (230, 235, 255), stroke=3)
        text(img, (bx + 30, by + 50), "Sirius B", 40, acc2, stroke=3)
        text(img, (W / 2, 1300), "one orbit every 50 years · 8.6 light-years away", 38, (255, 255, 255), w="ExtraBold", stroke=3)

# ---- scale13: 986 Jupiters fit inside the Sun (volume, NASA fact sheets); 1,048 by mass; densities 1.41 vs 1.33 g/cm³ ----
SUN_KM13, JUP_KM13, EARTH_KM13 = 695700.0, 69911.0, 6371.0
def _hexpack13(Rs, rj):
    """centres of Jupiter discs (radius rj) hex-packed inside a disc of radius Rs (2D slice, illustrative)"""
    pts = []; dy = rj * math.sqrt(3); row = 0; y = -Rs + rj
    while y <= Rs - rj:
        off = rj if row % 2 else 0; x = -Rs + rj + off
        while x <= Rs - rj:
            if math.hypot(x, y) <= Rs - rj: pts.append((x, y))
            x += 2 * rj
        y += dy; row += 1
    pts.sort(key=lambda p: (p[1], p[0])); return pts
def _sundisc13(img, cx, cy, Rs, a=1.0):
    R.paste_c(img, R.sun_sprite(int(Rs)), cx, cy, a)
def jupsun_vis(img, v, th, t, dur, bp):
    """the Sun TO SCALE against Jupiter (radius ratio 9.95); vis.mode = hook (Sun packed with to-scale Jupiters, slice view) | row
    (Jupiters roll in one by one across the diameter, counter to 9.7) | fill (Jupiters rain in, counter to 986 by volume) | earth (zoom on
    one Jupiter: an Earth to scale + counter to 1,321) | density (two jars: a cup of Sun 1.41 g/cm³ vs a cup of Jupiter 1.33, bars) |
    mass (grid of 1,048 tiny dots = Jupiter masses vs 986 by volume)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); cx, cy, Rs = W / 2, 930, 440
    rj = Rs * JUP_KM13 / SUN_KM13
    if mode in ("hook", "fill"):
        _sundisc13(img, cx, cy, Rs, 0.85)
        pts = _hexpack13(Rs, rj); n = len(pts) if mode == "hook" else int(len(pts) * min(1, bp * 1.15))
        spr = R.jup10(rj, 0.0)
        for k, (x, y) in enumerate(pts[:n]): R.paste_c(img, spr, cx + x, cy + y)
        if mode == "fill":
            cnt = int(986 * min(1, bp * 1.15)); text(img, (W / 2, 1450), f"{cnt:,} Jupiters", 70, acc, stroke=4)
            text(img, (W / 2, 1520), "by volume  (one slice shown)", 34, (230, 230, 240), w="Bold", stroke=3)
        else:
            text(img, (W / 2, 1450), "Jupiter, to scale, inside the Sun", 42, (255, 240, 220), w="ExtraBold", stroke=3)
    elif mode == "row":
        _sundisc13(img, cx, cy, Rs, 0.9); spr = R.jup10(rj, 0.0); d = ImageDraw.Draw(img)
        d.line([(cx - Rs, cy), (cx + Rs, cy)], fill=(255, 255, 255), width=3)
        n = 9.95 * min(1, bp * 1.1); k = 0
        while k < int(n):
            x = cx - Rs + rj + 2 * rj * k; R.paste_c(img, spr, x, cy); k += 1
        if n - int(n) > 0 and int(n) < 10:
            x = lerp(-rj, cx - Rs + rj + 2 * rj * int(n), ease(n - int(n))); R.paste_c(img, spr, x, cy)
        text(img, (W / 2, 1450), f"{n:.1f} Jupiters across", 64, acc, stroke=4)
        text(img, (W / 2, 1520), "1,391,400 km  vs  139,822 km (average)", 36, (230, 230, 240), w="Bold", stroke=3)
    elif mode == "earth":
        z = 1 + 7 * easeio(bp); jr = rj * z; jx = lerp(cx + Rs * 0.55, cx, easeio(bp)); jy = lerp(cy - Rs * 0.3, cy, easeio(bp))
        if bp < 0.7:  # the Sun's surface fills the frame as we zoom in, then fades (no giant sprite: memory)
            lay = Image.new("RGBA", img.size, (255, 150, 40, int(150 * (1 - bp / 0.7)))); img.alpha_composite(lay)
            _sundisc13(img, cx, cy, Rs, max(0, 1 - bp * 3))
        R.paste_c(img, R.jup10(min(400, jr), 0.0), jx, jy)
        er = jr * EARTH_KM13 / JUP_KM13
        if bp > 0.55:
            R.paste_c(img, R.earth_sprite(max(3, int(er)), glow=None), jx + jr * 0.35, jy - jr * 0.25)
            text(img, (jx + jr * 0.35, jy - jr * 0.25 - er - 34), "Earth", 36, (150, 210, 255), stroke=3)
        cnt = int(1321 * ease((bp - 0.55) / 0.45))
        text(img, (W / 2, 1450), f"{cnt:,} Earths per Jupiter", 62, acc2, stroke=4, a=ease((bp - 0.5) / 0.2))
    elif mode == "density":
        d = ImageDraw.Draw(img)
        for i, (lab, rho, col) in enumerate((("the Sun", 1.41, (255, 190, 80)), ("Jupiter", 1.33, (215, 170, 125)))):
            x = 300 + i * 480; y0, y1 = 1260, 560; h = (y0 - y1) * rho / 1.6 * ease(bp * 1.3 - i * 0.15)
            d.rounded_rectangle([x - 120, y1 - 20, x + 120, y0 + 10], 30, outline=(200, 210, 240), width=6)
            d.rectangle([x - 110, y0 - h, x + 110, y0], fill=col)
            for kk in range(6):
                if y0 - h + 30 + kk * 60 < y0 - 5: d.line([(x - 100, y0 - h + 30 + kk * 60), (x + 100, y0 - h + 30 + kk * 60)], fill=tuple(int(c * 0.85) for c in col), width=4)
            text(img, (x, y1 - 70), lab, 50, col, stroke=3)
            text(img, (x, y0 + 70), f"{rho:.2f} g/cm³", 52, (255, 255, 255), stroke=3, a=ease(bp * 2 - 0.4))
        y_w = 1260 - (1260 - 560) * 1.0 / 1.6; d = ImageDraw.Draw(img)
        for xx in range(140, 960, 40): d.line([(xx, y_w), (xx + 20, y_w)], fill=(120, 200, 255), width=3)
        text(img, (W / 2, y_w - 30), "water = 1.00", 32, (120, 200, 255), w="Bold", stroke=3)
        text(img, (W / 2, 1450), "almost the same stuff", 58, acc, stroke=4)
    elif mode == "mass":
        d = ImageDraw.Draw(img); cols = 33; s = 26; x0 = W / 2 - cols * s / 2 + s / 2; y0 = 520
        nv = 986; nm = int(1048 * min(1, bp * 1.1))
        for k in range(nm):
            r_, c_ = divmod(k, cols); x = x0 + c_ * s; y = y0 + r_ * s
            col = (215, 170, 125) if k < nv else acc2
            d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=col)
        text(img, (W / 2, 1450), f"{nm:,} by mass", 70, acc, stroke=4)
        text(img, (W / 2, 1520), "986 by volume", 40, (215, 170, 125), w="ExtraBold", stroke=3)

# ---- scale14: Andromeda spans ~3° of sky, six times the full Moon (0.5°) (NASA Hubble M31 page) ----
_and14 = {}
def _andro14(L, ang=-32):
    """Andromeda drawn by code: elliptical disc 3:1, bright yellowish core, bluish spiral arms + dark dust lanes, rotated"""
    key = (int(L), ang)
    if key in _and14: return _and14[key]
    S = int(L * 1.15); yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
    nx, ny = (xx - S / 2) / (L / 2), (yy - S / 2) / (L / 6)
    rr = np.sqrt(nx ** 2 + ny ** 2)
    disc = np.clip(1 - rr ** 2, 0, 1) ** 0.7 * 0.62 + np.exp(-(rr / 0.3) ** 2) * 0.35 + np.exp(-(rr / 0.08) ** 2) * 1.0
    lanes = 1 - 0.45 * np.clip(np.sin(rr * 26 + np.arctan2(ny, nx) * 1.5) * 0.5 + 0.5, 0, 1) ** 6 * (rr > 0.18) * (rr < 0.95)
    rng = np.random.default_rng(31); noise = np.asarray(Image.fromarray((rng.random((60, 60)) * 255).astype(np.uint8)).resize((S, S), Image.BICUBIC), np.float32) / 255
    b = np.clip(disc * lanes * (0.85 + 0.3 * noise), 0, 1.3)
    core = np.exp(-(rr / 0.2) ** 2)
    rgb = np.dstack([200 + 55 * core, 205 + 30 * core, 255 - 90 * core]) * np.clip(b, 0, 1)[..., None]
    a = np.clip(b * 255, 0, 255)
    im = Image.fromarray(np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8), "RGBA").rotate(ang, resample=Image.BICUBIC)
    rs = np.random.default_rng(5)
    dd = ImageDraw.Draw(im)
    for _ in range(int(L * 0.6)):  # sprinkled stars along the disc
        u, w_ = rs.normal(0, 0.35), rs.normal(0, 0.1); x = S / 2 + (u * math.cos(math.radians(-ang)) - w_ * math.sin(math.radians(-ang))) * L / 2
        y = S / 2 + (u * math.sin(math.radians(-ang)) + w_ * math.cos(math.radians(-ang))) * L / 2
        dd.point((x, y), fill=(255, 255, 255, int(rs.uniform(60, 200))))
    _and14[key] = im; return im
def _moon14(img, cx, cy, r, a=1.0):
    R.paste_c(img, R.radial(int(r * 3), [(0, (255, 255, 245, 255)), (0.6, (235, 235, 225, 255)), (0.66, (220, 220, 210, 255)), (0.7, (220, 220, 210, 90)), (1, (200, 200, 190, 0))]), cx, cy, a)
    d = ImageDraw.Draw(img)
    for dx, dy, rr in ((-0.3, -0.2, 0.22), (0.25, 0.1, 0.18), (-0.05, 0.35, 0.14)):
        d.ellipse([cx + dx * r - rr * r, cy + dy * r - rr * r, cx + dx * r + rr * r, cy + dy * r + rr * r], fill=(200, 200, 192, int(180 * a)))
def _hills14(img):
    d = ImageDraw.Draw(img); pts = [(0, 1560)]
    for x in range(0, W + 40, 40): pts.append((x, 1330 + 40 * math.sin(x / 140) + 22 * math.sin(x / 47)))
    pts.append((W, 1560)); d.polygon(pts, fill=(6, 8, 16))
    for x in (150, 210, 820, 870, 905):  # pine trees
        y = 1330 + 40 * math.sin(x / 140) + 22 * math.sin(x / 47)
        d.polygon([(x, y - 120), (x - 34, y + 5), (x + 34, y + 5)], fill=(6, 8, 16))
def andromeda_vis(img, v, th, t, dur, bp):
    """night sky over hills; full Moon (diameter 120 px) and Andromeda TO THE SAME ANGULAR SCALE (long axis 720 px = 6 Moons);
    vis.mode = hook (both in the sky, Andromeda bright as a long exposure) | row (6 Moons slide in along the long axis) | eye (galaxy fades
    to what eyes see: a faint core smudge) | light (light leaves Andromeda, counter of years to 2.5 million; timeline with first humans) |
    photo (camera frame + exposure counter: the full disc slowly appears)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); L = 720; mr = 60
    gx, gy, mx, my = W / 2 + 20, 860, 860, 470
    if mode == "hook":
        R.paste_c(img, _andro14(L), gx, gy); _moon14(img, mx, my, mr); _hills14(img)
        text(img, (mx, my + 100), "full Moon", 36, (240, 240, 230), stroke=3)
        text(img, (gx - 250, gy + 230), "Andromeda", 44, acc, stroke=3)
    elif mode == "row":
        R.paste_c(img, _andro14(L), gx, gy, 0.8); _hills14(img)
        ang = math.radians(32); n = 6 * min(1, bp * 1.15)
        for k in range(int(math.ceil(n))):
            f = min(1, n - k); u = -L / 2 + mr + 2 * mr * k
            x, y = gx + u * math.cos(ang), gy + u * math.sin(ang)
            _moon14(img, lerp(mx, x, ease(f)), lerp(my, y, ease(f)), mr, 0.9)
        text(img, (W / 2, 1450), f"{min(6, int(n + 0.001))} full Moons", 70, acc2, stroke=4)
        text(img, (W / 2, 1520), "≈ 3° of sky vs 0.5°", 38, (235, 235, 245), w="Bold", stroke=3)
    elif mode == "eye":
        q = easeio(bp); full = _andro14(L)
        R.paste_c(img, full, gx, gy, 1 - 0.92 * q)
        R.paste_c(img, R.radial(110, [(0, (235, 230, 210, int(140 * q))), (1, (200, 200, 220, 0))]), gx, gy)
        _moon14(img, mx, my, mr); _hills14(img)
        text(img, (W / 2, 1450), "what your eyes see", 58, acc, stroke=4, a=ease(bp * 2 - 0.6))
        text(img, (W / 2, 1520), "only the bright core, from a dark sky", 36, (235, 235, 245), w="Bold", stroke=3, a=ease(bp * 2 - 0.8))
    elif mode == "light":
        d = ImageDraw.Draw(img); x0, x1, y = 120, W - 120, 1000
        R.paste_c(img, _andro14(260), x0 + 40, 760)
        R.paste_c(img, R.earth_sprite(36, glow=(120, 180, 255)), x1 - 20, 760)
        d = ImageDraw.Draw(img); p = easeio(bp); xp = lerp(x0 + 120, x1 - 70, p)
        for k in range(16): d.ellipse([xp - 10 - k * 18, 750, xp + 10 - k * 18, 770], fill=(255, 245, 190, int(230 * (1 - k / 16))))
        d.line([(x0, y), (x1, y)], fill=(90, 95, 130), width=6)
        for frac, lab in ((0.0, "light leaves"), (1 - 0.3 / 2.5, "our species appears ↑"), (1.0, "today")):
            xx = lerp(x0, x1, frac); d.line([(xx, y - 16), (xx, y + 16)], fill=(180, 185, 210), width=4)
            d.text((xx, y + (50 if frac != 1 - 0.3 / 2.5 else 90)), lab, font=F(28, "Bold"), fill=(190, 195, 215), anchor="mm" if 0 < frac < 1 else ("lm" if frac == 0 else "rm"))
        d.polygon([(lerp(x0, x1, p), y - 24), (lerp(x0, x1, p) - 14, y - 50), (lerp(x0, x1, p) + 14, y - 50)], fill=acc)
        text(img, (W / 2, 1450), f"{2.5 * p:.2f} million years", 66, acc, stroke=4)
        text(img, (W / 2, 1520), "the trip its light took to reach you", 36, (235, 235, 245), w="Bold", stroke=3)
    elif mode == "photo":
        q = easeio(bp); R.paste_c(img, _andro14(L), gx, gy, 0.08 + 0.92 * q); _moon14(img, mx, my, mr); _hills14(img)
        d = ImageDraw.Draw(img); fx0, fy0, fx1, fy1 = 90, 420, W - 90, 1280
        for (x, y, sx, sy) in ((fx0, fy0, 1, 1), (fx1, fy0, -1, 1), (fx0, fy1, 1, -1), (fx1, fy1, -1, -1)):
            d.line([(x, y), (x + 70 * sx, y)], fill=(255, 255, 255), width=6); d.line([(x, y), (x, y + 70 * sy)], fill=(255, 255, 255), width=6)
        d.ellipse([fx0 + 20, fy0 + 20, fx0 + 44, fy0 + 44], fill=(255, 70, 70) if int(t * 2) % 2 == 0 else (120, 30, 30))
        text(img, (W / 2, 1450), f"exposure {int(1 + 179 * q)} s", 62, acc, stroke=4)
        text(img, (W / 2, 1520), "a long exposure reveals the whole disc", 36, (235, 235, 245), w="Bold", stroke=3)

# ---- scale15: 343 million Suns fit inside Betelgeuse (radius ~700 Suns, NOIRLab/Gemini 2025; volume 700³) ----
_bg15 = {}
def _betel15(r):
    """Betelgeuse drawn by code: red-orange disc, strong limb darkening, a few giant convection cells, soft corona"""
    r = max(2, int(r))
    if r in _bg15: return _bg15[r]
    if r not in (600, 1150) and (r > 150 or len(_bg15) > 40):  # zoom frames: scale one cached sprite instead of caching hundreds
        base = _betel15(600 if r < 1300 else 1150); sz = int(base.width * r / (600 if r < 1300 else 1150))
        return base.resize((max(4, sz), max(4, sz)), Image.BILINEAR)
    S = int(r * 2.5) + 4; yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
    d = np.sqrt((xx - S / 2) ** 2 + (yy - S / 2) ** 2) / r
    mu = np.sqrt(np.clip(1 - d ** 2, 0, 1))
    rng = np.random.default_rng(15); small = (rng.random((9, 9)) * 255).astype(np.uint8)
    cells = np.asarray(Image.fromarray(small).resize((S, S), Image.BICUBIC), np.float32) / 255
    b = (0.35 + 0.65 * mu) * (0.78 + 0.35 * cells)
    rgb = np.dstack([255 * np.clip(b * 1.05, 0, 1), 120 * b + 30 * mu, 50 * b])
    a = (d <= 1).astype(np.float32) * 255
    glow = np.clip(1 - (d - 1) / 0.25, 0, 1) * (d > 1) * 120
    rgbg = np.where((d > 1)[..., None], np.dstack([np.full_like(d, 255), np.full_like(d, 90), np.full_like(d, 40)]), rgb)
    im = Image.fromarray(np.dstack([np.clip(rgbg, 0, 255), np.maximum(a, glow)]).astype(np.uint8), "RGBA")
    _bg15[r] = im; return im
def _sundot15(img, x, y, rpx, lab=True, ring=True, a=1.0):
    R.paste_c(img, R.radial(max(24, int(rpx * 6)), [(0, (255, 250, 220, 255)), (0.35, (255, 220, 120, 230)), (1, (255, 200, 90, 0))]), x, y, a)
    d = ImageDraw.Draw(img)
    if ring: d.ellipse([x - 34, y - 34, x + 34, y + 34], outline=(255, 255, 255), width=4)
    if lab: d.text((x + 46, y), "our Sun", font=F(40, "ExtraBold"), fill=(255, 255, 255), anchor="lm", stroke_width=4, stroke_fill=(0, 0, 0))
def _cube15(img, cx, cy, n_filled, th, s=58):
    """isometric 7x7x7 cube; each small cube = 100 x 100 x 100 Suns (1 million); fills layer by layer"""
    acc = tuple(th["accent"]); d = ImageDraw.Draw(img)
    ux, uy = s * 0.87, s * 0.5
    def P(i, j, k): return (cx + (i - j) * ux, cy + (i + j) * uy - k * s)
    idx = 0
    for k in range(7):
        for j in range(7):
            for i in range(7):
                idx += 1
                if idx > n_filled: continue
                top = [P(i, j, k + 1), P(i + 1, j, k + 1), P(i + 1, j + 1, k + 1), P(i, j + 1, k + 1)]
                left = [P(i, j + 1, k), P(i + 1, j + 1, k), P(i + 1, j + 1, k + 1), P(i, j + 1, k + 1)]
                right = [P(i + 1, j, k), P(i + 1, j + 1, k), P(i + 1, j + 1, k + 1), P(i + 1, j, k + 1)]
                shade = 0.75 + 0.25 * (k / 6)
                d.polygon(left, fill=tuple(int(c * 0.55 * shade) for c in acc), outline=(30, 10, 5))
                d.polygon(right, fill=tuple(int(c * 0.75 * shade) for c in acc), outline=(30, 10, 5))
                d.polygon(top, fill=tuple(int(min(255, c * 1.0 * shade + 30)) for c in acc), outline=(30, 10, 5))
    # wireframe of the full cube
    for a_, b_ in (((0, 0, 7), (7, 0, 7)), ((7, 0, 7), (7, 7, 7)), ((7, 7, 7), (0, 7, 7)), ((0, 7, 7), (0, 0, 7)),
                   ((7, 0, 0), (7, 0, 7)), ((7, 7, 0), (7, 7, 7)), ((0, 7, 0), (0, 7, 7)), ((7, 0, 0), (7, 7, 0)), ((7, 7, 0), (0, 7, 0))):
        d.line([P(*a_), P(*b_)], fill=(255, 230, 200), width=3)
    return P
ORI15 = [("Betelgeuse", 0.30, 0.18, 10, (255, 120, 70)), ("Bellatrix", 0.70, 0.22, 6, (200, 215, 255)), ("Alnitak", 0.40, 0.52, 6, (200, 215, 255)),
         ("Alnilam", 0.50, 0.50, 6, (200, 215, 255)), ("Mintaka", 0.60, 0.48, 6, (200, 215, 255)), ("Saiph", 0.36, 0.84, 6, (200, 215, 255)),
         ("Rigel", 0.74, 0.80, 8, (190, 210, 255)), ("Meissa", 0.52, 0.08, 4, (200, 215, 255))]
def redgiant_vis(img, v, th, t, dur, bp):
    """vis.mode = hook (Betelgeuse fills the screen, the Sun a dot circled at its edge, both TO SCALE) | zoom (log zoom out from the
    Sun to Betelgeuse, counter "× wider" 1 -> 700) | cube (7×7×7 isometric cube; each block = 100×100×100 Suns; counter to 343 million) |
    earths (Sun = 1.3 million Earths -> × 343 million = 447 trillion Earths, as a stacked equation) | orbits (Betelgeuse in the Sun's place:
    orbits of Mercury..Mars + asteroid belt TO SCALE, surface at 3.26 AU) | orion (night sky, Orion drawn as dots + lines, Betelgeuse pulsing)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook")
    if mode == "hook":
        Rb = 1150; cx, cy = W / 2 + 380, 1700  # huge disc, edge sweeping across the screen
        R.paste_c(img, _betel15(Rb), cx, cy)
        sx, sy = 300, 560  # the Sun, to scale (radius 1150/700 = 1.6 px)
        _sundot15(img, sx, sy, 1.6)
        text(img, (W / 2 + 120, 1250), "Betelgeuse", 76, (255, 235, 220), stroke=5)
        text(img, (W / 2 + 120, 1330), "drawn to the same scale", 38, (255, 255, 255), w="Bold", stroke=4)
    elif mode == "zoom":
        z = 3 * (700 / 3) ** easeio(bp)  # Sun radius shrinks from 140 px to 0.6 px
        Rs = 420 / z; cx, cy = W / 2, 900
        Rb = 700 * Rs
        if 4 < Rb < 1600: R.paste_c(img, _betel15(Rb), cx, cy, ease((1600 - Rb) / 400))
        _sundot15(img, cx, cy, max(1.5, Rs), lab=False, ring=Rs < 20)
        if Rs >= 20: R.paste_c(img, R.sun_sprite(Rs), cx, cy)
        text(img, (W / 2, 1450), f"{700 ** easeio(bp):,.0f}× wider", 76, acc2, stroke=4)
        text(img, (W / 2, 1525), "about 700 Suns across", 38, (255, 255, 255), w="Bold", stroke=3)
    elif mode == "cube":
        n = int(343 * easeio(bp)); _cube15(img, W / 2, 640, n, th)
        text(img, (W / 2, 1390), f"{n:,} million Suns", 72, acc2, stroke=4)
        text(img, (W / 2, 1465), "700 × 700 × 700  ·  each block = 1 million", 34, (255, 255, 255), w="Bold", stroke=3)
    elif mode == "earths":
        R.paste_c(img, R.sun_sprite(120), 260, 640)
        R.paste_c(img, R.earth_sprite(14, glow=None), 470, 640)
        d = ImageDraw.Draw(img)
        text(img, (720, 610), "1 Sun =", 52, (255, 255, 255), w="ExtraBold", stroke=3)
        text(img, (720, 680), "1.3 million Earths", 46, (140, 200, 255), w="ExtraBold", stroke=3)
        q = easeio(bp)
        R.paste_c(img, _betel15(150), W / 2 - 300, 1000, ease(q * 3))
        text(img, (W / 2 + 120, 960), "× 343 million", 60, acc2, a=ease(q * 3), stroke=3)
        text(img, (W / 2 + 120, 1040), "Suns", 46, (255, 255, 255), w="ExtraBold", a=ease(q * 3), stroke=3)
        val = 447 * ease((q - 0.3) / 0.7)
        text(img, (W / 2, 1300), f"{val:,.0f} trillion", 96, acc, a=ease((q - 0.25) * 4), stroke=4)
        text(img, (W / 2, 1385), "Earths inside one star", 44, (255, 255, 255), w="ExtraBold", a=ease((q - 0.25) * 4), stroke=3)
    elif mode == "orbits":
        k = 440 / 3.6; cx, cy = W / 2, 880; d = ImageDraw.Draw(img)
        rr = 3.255 * k * easeio(bp)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        rng = random.Random(4)
        for _ in range(700):  # asteroid belt 2.2-3.2 AU
            a_ = rng.uniform(0, 2 * math.pi); r_ = rng.uniform(2.2, 3.2) * k
            xx_, yy_ = cx + r_ * math.cos(a_), cy + r_ * math.sin(a_); dl.ellipse([xx_ - 2, yy_ - 2, xx_ + 2, yy_ + 2], fill=(190, 180, 170, 220))
        img.alpha_composite(lay)
        if rr > 2: R.paste_c(img, _betel15(rr), cx, cy, 0.92)
        d = ImageDraw.Draw(img)
        for n, au, col in (("Mercury", 0.387, (170, 160, 150)), ("Venus", 0.723, (230, 200, 140)), ("Earth", 1.0, (90, 150, 255)), ("Mars", 1.524, (220, 110, 80))):
            r_ = au * k; swallowed = rr > r_
            d.ellipse([cx - r_, cy - r_, cx + r_, cy + r_], outline=(255, 255, 255, 90) if not swallowed else (120, 40, 20), width=2)
            ang = {"Mercury": -1.57, "Venus": 0.0, "Earth": 1.57, "Mars": 3.14}[n]; px, py = cx + r_ * math.cos(ang), cy + r_ * math.sin(ang)
            if not swallowed:
                d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=col)
                text(img, (px, py - 30) if n in ("Mercury", "Earth") else (px + (40 if n == "Venus" else -40), py - 30), n, 30, col, w="ExtraBold", stroke=3)
                d = ImageDraw.Draw(img)
        if bp > 0.95: text(img, (W / 2, 1390), "surface ≈ 3.3 × the Earth–Sun distance", 40, (255, 255, 255), w="ExtraBold", stroke=3)
        text(img, (cx + 3.2 * k * 0.7, cy - 3.2 * k * 0.72 - 20), "asteroid belt", 30, (210, 200, 190), w="Bold", stroke=3)
    elif mode == "orion":
        x0, y0, sw, sh = 190, 420, 700, 880; d = ImageDraw.Draw(img)
        P = {n: (x0 + fx * sw, y0 + fy * sh) for n, fx, fy, _, _ in ORI15}
        for a_, b_ in (("Betelgeuse", "Alnitak"), ("Bellatrix", "Mintaka"), ("Alnitak", "Alnilam"), ("Alnilam", "Mintaka"), ("Alnitak", "Saiph"),
                       ("Mintaka", "Rigel"), ("Betelgeuse", "Meissa"), ("Bellatrix", "Meissa")):
            d.line([P[a_], P[b_]], fill=(120, 130, 180), width=2)
        for n, fx, fy, s, col in ORI15:
            x, y = P[n]; pul = 1 + (0.25 * math.sin(t * 4) if n == "Betelgeuse" else 0)
            R.paste_c(img, R.radial(int(s * 9 * pul), [(0, col + (255,)), (0.25, col + (200,)), (1, col + (0,))]), x, y)
        bx, by = P["Betelgeuse"]
        d.ellipse([bx - 60, by - 60, bx + 60, by + 60], outline=acc, width=4)
        text(img, (bx + 80, by - 20), "Betelgeuse", 46, acc, stroke=3, anchor="lm")
        text(img, (bx + 80, by + 30), "visible tonight", 34, (255, 255, 255), w="Bold", stroke=3, anchor="lm")

# ---- scale16: the Sun shrunk to a 1 mm grain of sand (1 mm = 1,391,400 km): Earth 9 µm at 10.8 cm, Neptune 3.2 m, Voyager 1 18.6 m,
# Proxima Centauri 28.9 km, the Milky Way (100,000 ly) 680,000 km = 1.8 × the Earth–Moon distance ----
def _grain16(img, x, y, r, a=1.0):
    R.paste_c(img, R.radial(max(12, int(r * 7)), [(0, (255, 250, 220, 255)), (0.18, (255, 215, 110, 255)), (0.3, (255, 190, 80, 120)), (1, (255, 170, 60, 0))]), x, y, a)
def _finger16(img, x, y):
    """a fingertip (rounded, skin tone, nail) coming from the bottom; the grain sits on top at (x, y)"""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([x - 130, y + 18, x + 130, y + 660], 130, fill=(214, 160, 128, 255))
    d.rounded_rectangle([x - 70, y + 40, x + 70, y + 180], 60, fill=(236, 196, 176, 255))
    for k in range(5): d.arc([x - 100 + k * 8, y + 260 + k * 22, x + 100 - k * 8, y + 330 + k * 22], 200, 340, fill=(190, 135, 105, 255), width=3)
    img.alpha_composite(lay)
_gal16 = {}
def _galaxy16(w):
    w = int(w)
    if w in _gal16: return _gal16[w]
    im = Image.new("RGBA", (w, int(w * 0.45)), (0, 0, 0, 0)); d = ImageDraw.Draw(im); rng = random.Random(16)
    for _ in range(int(w * 14)):
        arm = rng.randint(0, 1); th_ = rng.uniform(0, 3.4 * math.pi); rr = math.exp(0.22 * (th_ - 3.4 * math.pi)) * w / 2 * 0.97
        ang = th_ + arm * math.pi + rng.gauss(0, 0.25); x = w / 2 + rr * math.cos(ang); y = im.height / 2 + rr * math.sin(ang) * 0.38
        c = (200, 215, 255) if rng.random() < 0.7 else (255, 225, 180)
        d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=c + (rng.randint(90, 230),))
    R.paste_c(im, R.radial(int(w * 0.22), [(0, (255, 235, 190, 255)), (0.5, (255, 220, 160, 110)), (1, (255, 200, 140, 0))]), w / 2, im.height / 2)
    _gal16[w] = im; return im
def sand_vis(img, v, th, t, dur, bp):
    """vis.mode = hook (fingertip holding the grain-Sun; a far dot on the horizon = next star, dashed "29 km") | earth (lens: Earth = 9 µm
    beside a human hair ~70 µm; ruler: the grain and Earth 10.8 cm away) | ruler (0–20 m track: grain, Earth 0.11 m, Neptune 3.2 m,
    Voyager 1 18.6 m, a 1.7 m person for scale) | gap (road to the horizon, km counter 0 -> 28.9, walking hours) | galaxy (Earth, the
    Moon 384,400 km away and the Milky Way at this scale, 680,000 km wide, all TO SCALE)"""
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"]); mode = v.get("mode", "hook"); d = ImageDraw.Draw(img)
    if mode == "hook":
        d.line([(0, 1060), (W, 1060)], fill=(70, 80, 120), width=2)
        hx, hy = 860, 1050
        for k in range(14):  # dashed sightline from the grain to the far star
            x = lerp(330, hx, k / 14); y = lerp(820, hy, k / 14); x2 = lerp(330, hx, (k + 0.5) / 14); y2 = lerp(820, hy, (k + 0.5) / 14)
            d.line([(x, y), (x2, y2)], fill=acc2, width=4)
        _grain16(img, hx, hy, 3 + 1.5 * math.sin(t * 5))
        _finger16(img, 330, 820); _grain16(img, 330, 812, 16)
        text(img, (hx - 20, hy - 70), "next star", 40, acc2, stroke=3)
        text(img, ((330 + hx) / 2 + 40, (820 + hy) / 2 - 50), "29 km", 46, acc, stroke=3)
        text(img, (330, 740), "the Sun, 1 mm", 44, (255, 235, 180), stroke=3)
    elif mode == "earth":
        x0, x1, y = 110, W - 110, 1180; ppm = (x1 - x0) / 120.0
        d.line([(x0, y), (x1, y)], fill=(200, 205, 225), width=4)
        for mm in range(0, 121, 10):
            xx = x0 + mm * ppm; d.line([(xx, y - (24 if mm % 50 == 0 else 14)), (xx, y)], fill=(200, 205, 225), width=3)
            d.text((xx, y + 30), f"{mm // 10}", font=F(26, "Bold"), fill=(170, 175, 200), anchor="mm")
        d.text((x1, y + 70), "centimetres", font=F(26, "SemiBold"), fill=(150, 155, 185), anchor="rm")
        _grain16(img, x0, y - 40, 5)
        ex = x0 + 107.5 * ppm * easeio(min(1, bp * 1.6)); d = ImageDraw.Draw(img); d.ellipse([ex - 3, y - 43, ex + 3, y - 37], fill=(120, 180, 255))
        # magnifier on Earth
        lx, ly, lr = W / 2, 720, 300; q = ease((bp - 0.4) / 0.3)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.ellipse([lx - lr, ly - lr, lx + lr, ly + lr], fill=(10, 12, 26, int(240 * q)), outline=(220, 230, 255, int(255 * q)), width=8)
        dl.line([(lx + 60, ly - lr), (lx + 200, ly + lr - 40)], fill=(150, 110, 70, int(200 * q)), width=140)  # a human hair, ~70 µm
        dl.line([(ex, y - 40), (lx + lr * 0.6, ly + lr * 0.8)], fill=(220, 230, 255, int(150 * q)), width=3)
        m = Image.new("L", img.size, 0); ImageDraw.Draw(m).ellipse([lx - lr + 6, ly - lr + 6, lx + lr - 6, ly + lr - 6], fill=255)
        hair = Image.new("RGBA", img.size, (0, 0, 0, 0)); hair.paste(lay, (0, 0), m); img.alpha_composite(lay if q < 0.01 else hair)
        if q > 0.01:
            dd = ImageDraw.Draw(img); dd.ellipse([lx - lr, ly - lr, lx + lr, ly + lr], outline=(220, 230, 255), width=8)
            R.paste_c(img, R.earth_sprite(9, glow=(120, 180, 255)), lx - 120, ly, q)
            text(img, (lx - 120, ly + 60), "Earth", 34, (140, 200, 255), a=q, stroke=3)
            text(img, (lx + 150, ly + 40), "a hair", 34, (230, 200, 170), a=q, stroke=3)
        text(img, (W / 2, 1380), f"{10.75 * easeio(min(1, bp * 1.6)):.1f} cm away", 70, acc2, stroke=4)
    elif mode == "ruler":
        x0, x1, y = 90, W - 90, 1050; ppm = (x1 - x0) / 20.0
        d.line([(x0, y), (x1, y)], fill=(200, 205, 225), width=4)
        for m_ in range(0, 21, 5):
            xx = x0 + m_ * ppm; d.line([(xx, y - 18), (xx, y + 18)], fill=(200, 205, 225), width=3); d.text((xx, y + 44), f"{m_} m", font=F(28, "Bold"), fill=(170, 175, 200), anchor="mm")
        _grain16(img, x0, y, 4)
        d = ImageDraw.Draw(img)
        px = x0 + 1.0 * ppm; hgt = 1.7 * ppm  # person for scale
        d.ellipse([px - 9, y - hgt, px + 9, y - hgt + 18], fill=(230, 230, 240)); d.line([(px, y - hgt + 18), (px, y - hgt * 0.45)], fill=(230, 230, 240), width=6)
        d.line([(px, y - hgt * 0.45), (px - 12, y)], fill=(230, 230, 240), width=6); d.line([(px, y - hgt * 0.45), (px + 12, y)], fill=(230, 230, 240), width=6)
        for i, (n, m_, col, dy) in enumerate((("Earth 0.11 m", 0.11, (120, 180, 255), -230), ("Neptune 3.2 m", 3.23, (90, 130, 240), -150), ("Voyager 1 · 18.6 m", 18.6, acc, -230))):
            q = ease((bp - i * 0.3) / 0.25)
            if q <= 0: continue
            xx = x0 + m_ * ppm; d.line([(xx, y + dy + 30), (xx, y - 8)], fill=col, width=3); d.ellipse([xx - 7, y - 7, xx + 7, y + 7], fill=col)
            text(img, (min(max(xx, 200), W - 200), y + dy), n, 38, col, a=q, stroke=3); d = ImageDraw.Draw(img)
        text(img, (W / 2, 1330), "after 49 years of flying", 46, (255, 255, 255), w="ExtraBold", a=ease((bp - 0.75) / 0.2), stroke=3)
    elif mode == "gap":
        hy = 860
        d.polygon([(0, hy), (W, hy), (W, 1560), (0, 1560)], fill=(10, 12, 22))
        d.polygon([(W / 2 - 6, hy), (W / 2 + 6, hy), (W / 2 + 330, 1560), (W / 2 - 330, 1560)], fill=(38, 40, 56))
        off = (t * 2.2) % 1
        for k in range(10):  # dashes rushing toward the viewer
            f0 = ((k + off) / 10) ** 2; f1 = ((k + off + 0.4) / 10) ** 2
            d.polygon([(W / 2 - 3 - 12 * f0, lerp(hy, 1560, f0)), (W / 2 + 3 + 12 * f0, lerp(hy, 1560, f0)), (W / 2 + 3 + 12 * f1, lerp(hy, 1560, f1)), (W / 2 - 3 - 12 * f1, lerp(hy, 1560, f1))], fill=(230, 220, 150))
        _grain16(img, W / 2, hy - 6, 5 + 2 * math.sin(t * 6))
        text(img, (W / 2, hy - 70), "Proxima Centauri", 40, acc2, stroke=3)
        km = 28.9 * easeio(bp)
        text(img, (W / 2, 560), f"{km:.1f} km", 120, acc, stroke=4)
        text(img, (W / 2, 660), f"of nothing  ·  {km / 5:.1f} hours on foot", 40, (255, 255, 255), w="ExtraBold", stroke=3)
    elif mode == "galaxy":
        ex, y = 100, 1000; scale = 470 / 384400  # px per km
        mx = ex + 384400 * scale; gw = 680000 * scale
        R.paste_c(img, _galaxy16(gw), ex + gw / 2, 720, ease(bp * 2))
        d = ImageDraw.Draw(img)
        R.paste_c(img, R.earth_sprite(12, glow=(120, 180, 255)), ex, y)
        R.paste_c(img, R.planet_sprite(5, (200, 200, 205)), mx, y)
        d = ImageDraw.Draw(img); d.line([(ex + 20, y), (mx - 12, y)], fill=(200, 205, 225), width=3)
        text(img, (ex, y + 50), "Earth", 32, (140, 200, 255), stroke=3); text(img, (mx, y + 50), "Moon", 32, (220, 220, 230), stroke=3)
        text(img, ((ex + mx) / 2, y - 40), "384,400 km", 34, (220, 225, 240), w="Bold", stroke=3)
        q = ease((bp - 0.2) / 0.4); d = ImageDraw.Draw(img)
        d.line([(ex, 900), (ex + gw * q, 900)], fill=acc2, width=6)
        text(img, (ex + gw / 2, 860), "the Milky Way, at this scale: 680,000 km", 34, acc2, a=q, stroke=3)
        text(img, (W / 2, 1330), "1.8× the trip to the Moon", 60, acc, a=ease((bp - 0.55) / 0.3), stroke=4)

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
    elif v["type"] in ("ballearth", "marble"):
        (ballearth_vis if v["type"] == "ballearth" else marble_vis)(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] in ("jupsun", "andromeda", "redgiant", "sand"):
        {"jupsun": jupsun_vis, "andromeda": andromeda_vis, "redgiant": redgiant_vis, "sand": globals().get("sand_vis")}[v["type"]](img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 170), hl["num"], 124 if len(hl["num"]) < 12 else 100, tuple(th["accent"]), stroke=4)
        text(img, (W / 2, 280), hl["top"], 52, (255, 255, 255), stroke=3)
    elif v["type"] == "dwarf":
        dwarf_vis(img, v, th, t, d, easeio((t - 0.2) / max(0.8, d * 0.8)))
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
