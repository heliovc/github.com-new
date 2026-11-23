"""Dia 4A — "E se você fosse um peixe a 8.000 metros?" (formato CURTO; paleta: breu verde-petróleo abissal,
peixe-caracol rosa pálido translúcido, luz branca-fria do robô de pesquisa, neve marinha).

Cenas: hook (o peixe na luz do robô, medidor de profundidade em 8.000 m), vision/vision2 (Visão do Bicho: linha
lateral sentindo as ondinhas de um anfípode), press (coluna de 8 km de água: 800×), press2 (um carro no dedão),
bubble (peixe comum com bexiga de ar sendo amassada), water (pistão: ar encolhe, água não), cells (molécula escudo
em volta da proteína), cells2 (mais fundo = mais molécula), limit (8.200 m: o limite), loop (volta ao quadro inicial).
Fatos: Yancey et al. (2014, PNAS); UWA/Tokyo (2023), peixe-caracol filmado a 8.336 m.
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

BODY = (248, 196, 210); BODY_D = (214, 128, 160); BODY_L = (255, 230, 236)
FIN = (255, 214, 226)
LAMP = (225, 245, 255)
ABY = [(0, (8, 30, 34)), (0.5, (4, 16, 20)), (1, (2, 7, 9))]
WATER = (80, 230, 150)
SENSE = (120, 255, 240)
AMPH = (250, 190, 140)
TM = (255, 120, 170)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= peixe-caracol (cabeça para a direita)
def _outline(t, sq=0.0):
    pts = [(0.52, 0.01), (0.47, -0.12), (0.34, -0.2), (0.14, -0.21), (-0.08, -0.15), (-0.3, -0.09), (-0.5, -0.045),
           (-0.66, 0.0), (-0.5, 0.05), (-0.3, 0.1), (-0.08, 0.16), (0.14, 0.22), (0.34, 0.2), (0.47, 0.13)]
    out = []
    for x, y in pts:
        w = 0.05 * math.sin(t * 4.2 - x * 6) * clamp01(-x * 2 + 0.2)
        out.append((x, y * (1 - sq) + w))
    return out


def fish(ss, x, y, s, t=0.0, rot=0.0, flip=1, eye=1.0, line=0.0, pores=None, sq=0.0):
    """pores: lista de 0..1 (brilho de cada poro da linha lateral)"""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.5, s * 0.007)
    wv = lambda xx: 0.05 * math.sin(t * 4.2 - xx * 6) * clamp01(-xx * 2 + 0.2)
    # nadadeiras dorsal e anal (membrana contínua até a cauda)
    for sg in (-1, 1):
        fin = [(0.15, sg * 0.19)]
        for k in range(12):
            u = k / 11; xx = lerp(0.12, -0.7, u)
            hh = (0.2 - 0.17 * u) if sg < 0 else (0.21 - 0.16 * u)
            fin.append((xx, sg * (hh + 0.07 * math.sin(u * math.pi)) + wv(xx)))
        for k in range(12):
            u = 1 - k / 11; xx = lerp(0.12, -0.66, u)
            hh = (0.13 - 0.12 * u) if sg < 0 else (0.15 - 0.12 * u)
            fin.append((xx, sg * hh * 0.6 + wv(xx)))
        ss.poly(P(fin), fill=(*FIN, 140), ink=(*BODY_D, 160), w=iw * 0.7)
        for k in range(10):  # raios
            u = k / 9; xx = lerp(0.1, -0.62, u)
            hh = (0.2 - 0.17 * u) if sg < 0 else (0.21 - 0.16 * u)
            ss.line(P([(xx, sg * hh * 0.55 + wv(xx)), (xx - 0.03, sg * (hh + 0.06 * math.sin(u * math.pi)) + wv(xx))]),
                    (*BODY_D, 110), max(1, s * 0.004), cap=False)
    # corpo
    body = A.spline(_outline(t, sq), 6)
    ss.poly(P(body), fill=(*BODY, 245), ink=(*INK, 220), w=iw)
    ss.poly(P(A.spline([(0.42, -0.1), (0.2, -0.17), (-0.1, -0.12), (-0.4, -0.06), (-0.1, -0.06), (0.2, -0.07)], 5)),
            fill=(*BODY_L, 170))
    # órgãos aparecendo pela pele (translúcido)
    ss.poly(P(A.ell_pts(0.16, 0.07, 0.13, 0.07, -8, 24)), fill=(*BODY_D, 90))
    ss.poly(P(A.ell_pts(0.0, 0.05, 0.08, 0.045, -6, 20)), fill=(200, 110, 140, 70))
    # nadadeira peitoral grande (leque)
    fa = 8 * math.sin(t * 2.6)
    pec = [(0.2, 0.1)] + [(0.2 + 0.24 * math.cos(math.radians(a + fa)), 0.1 + 0.24 * math.sin(math.radians(a + fa)))
                          for a in range(95, 165, 7)]
    ss.poly(P(pec), fill=(*FIN, 170), ink=(*BODY_D, 170), w=iw * 0.7)
    for a in range(100, 165, 12):
        ss.line(P([(0.2, 0.1), (0.2 + 0.23 * math.cos(math.radians(a + fa)), 0.1 + 0.23 * math.sin(math.radians(a + fa)))]),
                (*BODY_D, 120), max(1, s * 0.004), cap=False)
    # boca
    ss.line(P(A.bez((0.52, 0.03), (0.49, 0.06), (0.45, 0.07), (0.42, 0.065), 6)), (*INK, 200), max(1.5, s * 0.008), cap=True)
    # linha lateral
    n = 11
    for k in range(n):
        u = k / (n - 1); xx = lerp(0.3, -0.5, u); yy = lerp(-0.01, 0.0, u) + wv(xx)
        q = P([(xx, yy)])[0]
        g = line * (pores[k] if pores is not None else 0.6)
        if g > 0.02:
            ss.circle(q[0], q[1], s * (0.02 + 0.03 * g), fill=(*SENSE, int(110 * g)))
        ss.circle(q[0], q[1], s * 0.008, fill=(*SENSE, int(120 + 135 * g)) if line > 0 else (*BODY_D, 200))
    # olho (pequeno; maior na capa)
    ex, ey = P([(0.37, -0.06)])[0]; er = s * 0.026 * eye
    ss.circle(ex, ey, er * 1.25, fill=(*BODY_D, 230))
    ss.circle(ex, ey, er, fill=(20, 26, 50), ink=INK, w=max(1, iw * 0.6))
    ss.circle(ex - er * 0.35, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, 240))
    ss.circle(ex + er * 0.3, ey + er * 0.32, er * 0.14, fill=(255, 255, 255, 170))
    return [P([(lerp(0.3, -0.5, k / (n - 1)), wv(lerp(0.3, -0.5, k / (n - 1))))])[0] for k in range(n)]


def amphipod(ss, x, y, s, t=0.0, flip=1, col=AMPH, a=255):
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    for k in range(7):
        u = k / 6; ang = math.radians(lerp(-150, -20, u))
        cx, cy = 0.3 * math.cos(ang), 0.3 * math.sin(ang) + 0.25
        ss.poly(P(A.ell_pts(cx, cy, 0.09, 0.07, math.degrees(ang) + 90, 14)), fill=(*col, a), ink=(*INK, int(a * 0.8)), w=1.5)
        lx = cx * 1.15; ly = cy + 0.16 + 0.03 * math.sin(t * 12 + k)
        ss.line(P([(cx, cy + 0.05), (lx, ly)]), (*col, a), max(1, s * 0.02))
    ss.line(P([(0.26, 0.1), (0.5, -0.12 + 0.04 * math.sin(t * 5))]), (*col, a), max(1, s * 0.02))
    q = P([(0.22, 0.12)])[0]
    ss.circle(q[0], q[1], s * 0.03, fill=(20, 10, 10, a))


# ======================================================================= fundo abissal
def abyss(lamp=1.0):
    def mk():
        im = A.vgrad(W, H, ABY)
        return im
    im = cached("aby", mk).copy()
    if lamp > 0:
        cone = cached("cone", lambda: _cone())
        A.paste(im, cone, 0, 0, lamp)
    return im


def _cone():
    ss = SS(W, H, s=1)
    ss.poly([(-80, -40), (360, -40), (1200, 1900), (-200, 1900)], fill=(*LAMP, 46))
    ss.poly([(40, -40), (240, -40), (900, 1900), (60, 1900)], fill=(*LAMP, 40))
    im = ss.get().filter(ImageFilter.GaussianBlur(50))
    im.alpha_composite(A.glow(380, LAMP, 170), (-260, -300))
    return im


def snow(img, t, n=90, seed=3, a=150, spd=30):
    rng = np.random.default_rng(seed); ss = SS(W, H, s=1)
    for _ in range(n):
        x0 = rng.uniform(0, W); y0 = rng.uniform(0, H); r = rng.uniform(1.5, 4.5)
        y = (y0 + t * spd * (0.5 + r / 4)) % (H + 20) - 10
        ss.circle(x0 + 10 * math.sin(t * 0.7 + y0), y, r, fill=(235, 245, 240, int(a * rng.uniform(0.3, 1))))
    img.alpha_composite(ss.get())


def gauge(img, depth, y0=520, y1=1680, x=985, maxd=9000, limit=None, alpha=1.0):
    """régua de profundidade vertical à direita"""
    ss = SS(W, H, s=2)
    ss.rrect(x - 42, y0 - 30, x + 42, y1 + 30, 22, fill=(10, 24, 28, int(200 * alpha)), ink=(*INK, int(255 * alpha)), w=4)
    for k in range(0, maxd + 1, 1000):
        yy = lerp(y0, y1, k / maxd)
        ss.line([(x - 30, yy), (x - 8, yy)], (200, 230, 225, int(220 * alpha)), 3)
        if k % 2000 == 0:
            ss.text((x - 52, yy), f"{k // 1000} km", 30, "mont-ExtraBold", fill=(220, 240, 235, int(230 * alpha)), anchor="rm", stroke=4)
    if limit is not None:
        yl = lerp(y0, y1, limit / maxd)
        ss.rect(x - 40, yl, x + 40, y1 + 28, (220, 40, 60, int(150 * alpha)))
        ss.line([(x - 60, yl), (x + 40, yl)], (255, 60, 80, int(255 * alpha)), 6)
    yd = lerp(y0, y1, clamp01(depth / maxd))
    ss.rrect(x - 30, y0, x + 30, yd, 16, fill=(*WATER, int(120 * alpha)))
    ss.poly([(x + 40, yd), (x + 70, yd - 22), (x + 70, yd + 22)], fill=(255, 222, 40, int(255 * alpha)), ink=INK, w=3)
    img.alpha_composite(ss.get())


# ======================================================================= cena 1: gancho
def hook_frame(t, fs=None, fx=None, fy=None):
    img = abyss()
    snow(img, t)
    ss = SS(W, H, s=2)
    amphipod(ss, 200 + 20 * math.sin(t), 1720, 120, t=t)
    amphipod(ss, 880, 1630 + 10 * math.sin(t * 1.3), 80, t=t + 1, flip=-1)
    img.alpha_composite(ss.get())
    fs = 640 if fs is None else fs
    fx = 500 + 18 * math.sin(t * 0.8) if fx is None else fx
    fy = 1470 + 14 * math.sin(t * 1.4) if fy is None else fy
    ss = SS(W, H, s=2)
    fish(ss, fx, fy, fs, t=t, rot=-6 + 3 * math.sin(t * 0.9), eye=1.15)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 26, 0.4, col=(0, 0, 0))
    A.paste(img, sh, -pad + 10, -pad + 40)
    img.alpha_composite(sp)
    gauge(img, 8000 + 40 * math.sin(t * 2))
    # coluna de água pesando (setas para baixo, fracas)
    ss = SS(W, H, s=2)
    for k in range(3):
        yy = 560 + ((t * 120 + k * 150) % 450)
        a = int(170 * math.sin(math.pi * ((t * 120 + k * 150) % 450) / 450))
        A.arrow(ss, 300 + k * 220, yy, 300 + k * 220, yy + 120, (220, 240, 255, a), w=26, ink=(*INK, a), iw=3)
    img.alpha_composite(ss.get())
    return A.vignette(img, 0.5)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.03 + 0.012 * math.sin(lt * 1.1), rot=0.5 * math.sin(lt * 0.6))


# ======================================================================= cenas 2-3: Visão do Bicho (linha lateral)
def vision(ctx, lt):
    second = ctx.sc["id"] == "vision2"
    t = lt + (3.7 if second else 0.0)
    img = A.vgrad(W, H, [(0, (2, 6, 8)), (1, (0, 2, 4))])
    snow(img, t, 40, 9, a=50)
    fx, fy, fs = 640, 1480, 760
    # fonte das ondinhas: um anfípode à esquerda (aparece aos poucos na segunda tomada)
    sx, sy = 170, 760
    ss = SS(W, H, s=2)
    rings = []
    for k in range(6):
        r = ((t * 260 + k * 170) % 1100)
        a = int(200 * (1 - r / 1100))
        ss.ellipse(sx, sy, r, r, ink=(*SENSE, a), w=6)
        rings.append(r)
    img.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(1.5)))
    ss = SS(W, H, s=2)
    pts = fish(SS(W, H, s=1), fx, fy, fs, t=t, rot=-4)  # só para pegar a posição dos poros
    pores = []
    for (px, py) in pts:
        d = math.hypot(px - sx, py - sy)
        g = max([math.exp(-((d - r) / 60) ** 2) for r in rings] + [0])
        pores.append(min(1.0, 0.25 + g))
    fish(ss, fx, fy, fs, t=t, rot=-4, line=1.0, pores=pores)
    sp = ss.get()
    dim = Image.new("RGBA", sp.size, (0, 0, 0, 0))
    # o corpo some no escuro: só a linha lateral brilha
    arr = np.asarray(sp, np.float32).copy()
    lum = arr[..., :3].mean(axis=2, keepdims=True)
    cy = arr[..., 1:2] > arr[..., 0:1] + 40
    arr[..., :3] = np.where(cy, arr[..., :3], arr[..., :3] * 0.22 + lum * 0.03)
    img.alpha_composite(Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA"))
    if second:
        tc = ctx.wt("comida")
        q = ease((lt - tc + 0.8) / 0.8)
        ss = SS(W, H, s=2)
        amphipod(ss, sx, sy - 40, 160, t=t, col=SENSE, a=int(60 + 195 * q))
        if q > 0.05:
            ss.ellipse(sx, sy - 10, 150 + 10 * math.sin(lt * 8), 150 + 10 * math.sin(lt * 8), ink=(255, 222, 40, int(255 * q)), w=8)
            A.arrow(ss, fx - 200, fy - 220, sx + 150, sy + 130, (255, 222, 40, int(255 * q)), w=26, ink=(*INK, int(255 * q)))
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.9), dx=6 * math.sin(lt * 1.2))


# ======================================================================= cena 4: 800× a pressão
def press(ctx, lt):
    img = abyss(0.5); snow(img, lt, 60, 5)
    t8 = ctx.wt("800")
    q = ease((lt - t8 + 0.5) / 1.2)
    ss = SS(W, H, s=2)
    # coluna de água: 8 blocos de 1 km empilhados (verde = água)
    for k in range(8):
        y = 470 + k * 92 * (0.6 + 0.4 * ease(clamp01(lt / 0.9 - k * 0.08)))
        ss.rrect(330, y, 750, y + 84, 14, fill=(*WATER, 70 + k * 14), ink=(20, 90, 60), w=4)
        ss.text((540, y + 42), "1 km", 40, "anton", fill=(230, 255, 240), stroke=5)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    fish(ss, 540, 1600, 420, t=lt, rot=-4, sq=0.03 * q)
    # setas apertando de todos os lados
    for k in range(10):
        a = math.radians(k * 36 + 18)
        r0 = 470 - 70 * q; r1 = 300 - 50 * q
        A.arrow(ss, 540 + r0 * math.cos(a), 1600 + r0 * math.sin(a) * 0.75, 540 + r1 * math.cos(a), 1600 + r1 * math.sin(a) * 0.75,
                (255, 255, 255, int(255 * clamp01(q * 2))), w=30, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * q, dx=4 * q * math.sin(lt * 30))


# ======================================================================= cena 5: um carro no dedão
def car(ss, x, y, s, col=(230, 70, 80)):
    P = lambda pts: [(x + px * s, y + py * s) for px, py in pts]
    ss.poly(P(A.spline([(-0.5, 0.0), (-0.48, -0.16), (-0.25, -0.2), (-0.12, -0.38), (0.18, -0.38), (0.32, -0.2),
                        (0.5, -0.16), (0.52, 0.0)], 6)), fill=col, ink=INK, w=5)
    ss.poly(P([(-0.08, -0.33), (0.12, -0.33), (0.24, -0.2), (-0.18, -0.2)]), fill=(170, 220, 250), ink=INK, w=4)
    ss.line(P([(0.02, -0.33), (0.02, -0.2)]), INK, 4)
    for wx in (-0.3, 0.32):
        ss.circle(*P([(wx, 0.0)])[0], s * 0.1, fill=(40, 40, 46), ink=INK, w=4)
        ss.circle(*P([(wx, 0.0)])[0], s * 0.045, fill=(190, 190, 200))
    ss.ellipse(*P([(0.47, -0.12)])[0], s * 0.03, s * 0.02, fill=(255, 240, 160))


def press2(ctx, lt):
    img = A.vgrad(W, H, [(0, (18, 40, 44)), (1, (6, 18, 22))])
    tc = ctx.wt("carro")
    drop = ease((lt - tc + 0.6) / 0.5)
    sq = clamp01((lt - tc + 0.1) / 0.15) * (1 - 0.5 * clamp01((lt - tc - 0.2) / 0.5))
    ss = SS(W, H, s=2)
    OY = -380
    # polegar (pele) vindo de baixo
    th = A.spline([(380, 1960), (400, 1500 + OY), (430, 1320 + OY + 18 * sq), (540, 1270 + OY + 22 * sq), (650, 1320 + OY + 18 * sq),
                   (690, 1500 + OY), (710, 1960)], 8)
    ss.poly(th, fill=(236, 178, 140), ink=INK, w=6)
    ss.poly(A.spline([(470, 1350 + OY + 18 * sq), (540, 1318 + OY + 22 * sq), (610, 1350 + OY + 18 * sq), (620, 1470 + OY), (460, 1470 + OY)], 6),
            fill=(250, 214, 196), ink=(*INK, 160), w=3)
    for k in range(3):
        ss.line(A.bez((440, 1600 + OY + k * 40), (500, 1585 + OY + k * 40), (580, 1585 + OY + k * 40), (650, 1600 + OY + k * 40), 8), (200, 130, 100), 4, cap=False)
    # carro descendo e apoiando em cima
    cy = lerp(380, 1265 + OY + 22 * sq, drop)
    car(ss, 540, cy - 30, 560)
    if drop > 0.95:
        for sg in (-1, 1):
            A.arrow(ss, 540 + sg * 300, 1180 + OY - 120, 540 + sg * 140, 1290 + OY - 140, (255, 222, 40), w=24, iw=4)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ss.text((540, 1560), "~1,5 tonelada", 70, "anton", fill=(255, 222, 40, int(255 * drop)), stroke=8)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dy=-14 * sq, dx=10 * sq * math.sin(lt * 50))


# ======================================================================= cena 6: peixe comum com bexiga de ar
def bubble(ctx, lt):
    img = abyss(0.6); snow(img, lt, 50, 6)
    ta = ctx.wt("amassado")
    q = ease((lt - ta + 0.5) / 0.6)
    ss = SS(W, H, s=2)
    cx, cy, s = 540, 1450, 760
    P = lambda pts: [(cx + px * s, cy + py * s) for px, py in pts]
    body = A.spline([(0.48, 0.0), (0.3, -0.18), (0.0, -0.22), (-0.3, -0.15), (-0.45, -0.03), (-0.62, -0.17), (-0.6, 0.0),
                     (-0.62, 0.17), (-0.45, 0.03), (-0.3, 0.15), (0.0, 0.22), (0.3, 0.18)], 6)
    ss.poly(P(body), fill=(150, 170, 190, 150), ink=(*INK, 230), w=5)  # raio-X: corpo translúcido
    ss.circle(*P([(0.34, -0.05)])[0], 16, fill=(20, 20, 30))
    # espinha
    ss.line(P([(0.3, 0.0), (-0.48, 0.0)]), (230, 230, 240, 200), 6)
    for k in range(9):
        xx = lerp(0.2, -0.4, k / 8)
        ss.line(P([(xx, 0.0), (xx - 0.04, -0.12)]), (230, 230, 240, 150), 3)
    # bexiga de ar (verde = ar) encolhendo e amassando
    rx = 0.22 * (1 - 0.7 * q); ry = 0.075 * (1 - 0.75 * q)
    pts = []
    for k in range(40):
        a = k / 40 * 2 * math.pi
        wob = 1 + 0.25 * q * math.sin(a * 7 + 1)
        pts.append((0.0 + rx * math.cos(a) * wob, 0.07 + ry * math.sin(a) * wob))
    ss.poly(P(pts), fill=(*WATER, 200), ink=(20, 90, 60), w=5)
    for k in range(8):
        a = math.radians(k * 45 + 22)
        r0 = 520 - 120 * q; r1 = 330 - 120 * q
        A.arrow(ss, cx + r0 * math.cos(a), cy + 50 + r0 * math.sin(a) * 0.6, cx + r1 * math.cos(a), cy + 50 + r1 * math.sin(a) * 0.6,
                (255, 255, 255, 230), w=28, iw=4)
    ss.text((540, 760), "BEXIGA DE AR", 64, "anton", fill=(*WATER, 255), stroke=7)
    A.arrow(ss, 540, 820, cx, cy - 20, (*WATER, 255), w=20, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.05 * q, dx=10 * q * math.sin(lt * 40))


# ======================================================================= cena 7: ar encolhe, água não
def piston(ss, x, y, h, fill_col, frac, label):
    ss.rrect(x - 150, y - h, x + 150, y, 18, fill=(30, 50, 56, 200), ink=INK, w=6)
    top = y - h * frac
    ss.rrect(x - 140, top, x + 140, y - 10, 12, fill=fill_col)
    ss.rect(x - 150, top - 40, x + 150, top, (190, 196, 206))
    ss.rect(x - 22, top - 260, x + 22, top - 40, (160, 166, 176))
    ss.text((x, y + 70), label, 64, "anton", fill=(255, 255, 255), stroke=7)


def water(ctx, lt):
    img = abyss(0.4); snow(img, lt, 40, 7)
    ta = ctx.wt("água"); te = ctx.wt("encolhe")
    q = ease((lt - 0.2) / 1.6)
    ss = SS(W, H, s=2)
    piston(ss, 290, 1720, 560, (*WATER, 120), 1 - 0.65 * q, "AR")
    piston(ss, 790, 1720, 560, (*WATER, 230), 1 - 0.04 * q, "ÁGUA")
    for x in (290, 790):
        A.arrow(ss, x, 1720 - 560 * (1 - (0.65 if x < 500 else 0.04) * q) - 470, x,
                1720 - 560 * (1 - (0.65 if x < 500 else 0.04) * q) - 320, (255, 255, 255), w=34, iw=4)
    # bolinhas: ar (poucas, separadas) × água (cheia)
    rng = np.random.default_rng(2)
    for k in range(18):
        yy = 1710 - rng.uniform(0, 560 * (1 - 0.65 * q) - 30)
        ss.circle(290 + rng.uniform(-110, 110), yy, 12, fill=(220, 255, 235, 220))
    img.alpha_composite(ss.get())
    # o peixe (corpo de água) passa por cima, depois de "água"
    qa = ease((lt - ta + 0.3) / 0.8)
    ss = SS(W, H, s=2)
    fish(ss, lerp(-300, 560, qa), 760, 520, t=lt, rot=-3, eye=1.1)
    img.alpha_composite(ss.get())
    if qa > 0.05:
        ss = SS(W, H, s=2)
        ss.text((560, 960), "~ só água", 58, "anton", fill=(*WATER, int(255 * qa)), stroke=7)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cenas 8-9: a molécula escudo
def protein(ss, cx, cy, s, t, crush=0.0):
    pts = []
    for k in range(60):
        u = k / 59
        a = u * 5.5 * math.pi
        r = s * (0.25 + 0.2 * math.sin(u * 7)) * (1 - 0.5 * crush * (0.5 + 0.5 * math.sin(a * 2)))
        pts.append((cx + r * math.cos(a) + s * 0.3 * (u - 0.5), cy + r * math.sin(a) * (1 - 0.6 * crush)))
    ss.line(pts, (*INK, 255), 30); ss.line(pts, (120, 200, 255), 20)
    ss.line(pts, (210, 240, 255, 180), 6)


def cells(ctx, lt):
    img = A.vgrad(W, H, [(0, (48, 18, 40)), (1, (22, 8, 24))])
    img.alpha_composite(A.glow(700, (255, 120, 170), 60), (-160, 300))
    tp = ctx.wt("protege")
    q = ease((lt - tp + 0.3) / 0.9)
    ss = SS(W, H, s=2)
    cx, cy = 540, 1450
    protein(ss, cx, cy, 380, lt, crush=0.0)
    # moléculas escudo (TMAO) chegando e formando um anel
    for k in range(18):
        a = k / 18 * 2 * math.pi + lt * 0.4
        r = lerp(900, 330, ease(clamp01(q * 1.3 - k * 0.02)))
        x = cx + r * math.cos(a); y = cy + r * math.sin(a) * 0.8
        ss.circle(x, y, 38, fill=TM, ink=INK, w=4)
        ss.circle(x + 26, y - 18, 18, fill=(255, 255, 255), ink=INK, w=3)
        ss.circle(x - 12, y - 12, 10, fill=(255, 220, 235))
    # setas da pressão batendo e voltando
    for k in range(6):
        a = math.radians(k * 60 + 30)
        r0 = 720; r1 = lerp(420, 520, q)
        ss_c = (255, 255, 255, 220)
        A.arrow(ss, cx + r0 * math.cos(a), cy + r0 * math.sin(a) * 0.8, cx + r1 * math.cos(a), cy + r1 * math.sin(a) * 0.8, ss_c, w=26, iw=4)
    ss.text((540, 700), "PROTEÍNA", 70, "anton", fill=(120, 200, 255), stroke=8)
    ss.text((540, 800), "+ molécula escudo", 56, "anton", fill=(*TM, int(255 * q)), stroke=7)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)), rot=0.6 * math.sin(lt))


def depth_meter(img, lt, depth, fill, limit=False, red=0.0):
    """régua de profundidade grande + medidor da molécula (barra rosa)"""
    gauge(img, depth, y0=560, y1=1760, x=880, limit=8200 if limit else None)
    ss = SS(W, H, s=2)
    x0, x1, y0, y1 = 110, 260, 600, 1760
    ss.rrect(x0, y0, x1, y1, 28, fill=(20, 10, 22, 220), ink=INK, w=6)
    top = lerp(y1 - 14, y0 + 14, clamp01(fill))
    col = (255, int(lerp(120, 60, red)), int(lerp(170, 80, red)))
    ss.rrect(x0 + 14, top, x1 - 14, y1 - 14, 18, fill=col)
    for k in range(6):
        yy = lerp(y0, y1, k / 6)
        ss.line([(x0 + 14, yy), (x0 + 50, yy)], (255, 255, 255, 120), 3)
    ss.text(((x0 + x1) / 2, y0 - 50), "MOLÉCULA", 40, "anton", fill=TM, stroke=6)
    img.alpha_composite(ss.get())


def cells2(ctx, lt):
    img = abyss(0.3); snow(img, lt, 60, 11, spd=-160)
    tf = ctx.wt("fundo")
    q = easeio(clamp01((lt - tf + 0.2) / max(0.5, ctx.dur - 0.4)))
    d = lerp(3000, 7600, q)
    depth_meter(img, lt, d, lerp(0.3, 0.85, q))
    ss = SS(W, H, s=2)
    fy = lerp(700, 1500, q)
    fish(ss, 560, fy, 430, t=lt, rot=24, eye=1.1)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dy=-6 * math.sin(lt * 1.3))


def limit(ctx, lt):
    img = abyss(0.2); snow(img, lt, 60, 13, spd=-60)
    tl = ctx.wt("limite"); tm = ctx.wt("metros")
    q = ease((lt - tl + 0.2) / 1.2)
    hit = clamp01((lt - tm) / 0.2)
    d = lerp(7600, 8200, q)
    depth_meter(img, lt, d, lerp(0.85, 1.0, q), limit=True, red=hit)
    ss = SS(W, H, s=2)
    fy = lerp(1500, 1570, q) - 30 * hit * math.sin(lt * 10) * math.exp(-max(0, lt - tm) * 2)
    fish(ss, 560, fy, 430, t=lt, rot=lerp(24, 0, hit), eye=1.1)
    if hit > 0:
        ss.line([(330, 1640), (790, 1640)], (255, 60, 80, int(255 * hit)), 10)
        ss.text((560, 1720), "LIMITE", 90, "anton", fill=(255, 80, 90, int(255 * hit)), stroke=9)
    img.alpha_composite(ss.get())
    if hit > 0:
        img.alpha_composite(Image.new("RGBA", (W, H), (255, 40, 60, int(40 * hit * math.exp(-max(0, lt - tm) * 3)))))
    return A.cam(img, zoom=1.0 + 0.05 * hit, dx=8 * hit * math.sin(lt * 40) * math.exp(-max(0, lt - tm) * 3))


# ======================================================================= cena 11: loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    back = easeio((lt - 0.5) / max(0.3, ctx.dur - 0.6))
    fs = lerp(520, 640, back)
    fx = lerp(540, 500 + 18 * math.sin(tr * 0.8), back)
    fy = lerp(1300, 1470 + 14 * math.sin(tr * 1.4), back)
    img = hook_frame(tr, fs=fs, fx=fx, fy=fy)
    return A.cam(img, zoom=lerp(1.1, 1.03 + 0.012 * math.sin(tr * 1.1), back), rot=0.5 * math.sin(tr * 0.6) * back)


# ======================================================================= capa
def cover_bg(cv):
    img = abyss(1.2)
    snow(img, 1.0, 120, 3, a=200)
    ss = SS(W, H, s=2)
    amphipod(ss, 180, 1700, 140, t=1.0)
    amphipod(ss, 900, 1560, 100, t=2.0, flip=-1)
    img.alpha_composite(ss.get())
    gauge(img, 8000)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 520)
    ss = SS(int(1.35 * s), int(0.72 * s), s=2)
    fish(ss, 0.68 * s, 0.36 * s, s, t=0.6, eye=1.9)
    return ss.get()
