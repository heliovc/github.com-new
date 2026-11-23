"""Dia 4B — "E se você fosse um rato no poço do elevador?" (formato ATUAL; paleta: concreto cinza-quente,
luz de lâmpada de sódio laranja, aço prateado, faixas de segurança amarelo × preto; flashback 1854 em sépia).

Cenas: hook (contra-plongée do fundo do poço: a cabine descendo, o rato em primeiro plano), hang (cabine de ~1 t
pendurada nos cabos), motor (raio-X da casa de máquinas: roda com sulcos, atrito, eletricidade em amarelo),
counter (o contrapeso do outro lado; metade da lotação), counter2 (balança: o motor só levanta a diferença),
vision (Visão do Bicho: os bigodes sentem o vento que a cabine empurra; ar em verde), brake (cabo arrebenta;
limitador de velocidade), brake2 (cunhas mordem o trilho), otis (1854: mandou cortar a corda), loop (caiu uns
centímetros e parou; volta ao quadro inicial).
Fatos: ASME (Otis, 1854); ASME A17.1; Yu et al. (2016, Science Advances).
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

FUR = (138, 124, 120); FUR_D = (94, 82, 84); FUR_L = (196, 184, 176); PINK = (246, 162, 172)
CONC = (150, 138, 126); CONC_D = (98, 88, 84); CONC_L = (186, 174, 160)
SOD = (255, 160, 60)
STEEL = (196, 202, 212); STEEL_D = (112, 118, 132)
CAB = (72, 82, 98); CAB_L = (120, 132, 150)
IRON = (60, 58, 64)
YEL = (255, 206, 40); ELEC = (255, 230, 60)
AIR = (80, 230, 150)
SEP = (236, 214, 176); SEP_D = (120, 88, 60); SEP_M = (180, 140, 100)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= rato (perfil, focinho para a direita)
def rat(ss, x, y, s, t=0.0, rot=0.0, flip=1, eye=1.0, look=0.0, whisk=0.0, tail_up=0.0):
    """look: 0 = olha para frente, 1 = cabeça erguida olhando para cima; whisk: curvatura dos bigodes (vento)"""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.5, s * 0.008)
    br = 0.012 * math.sin(t * 3.0)
    # rabo
    tl = A.bez((-0.42, 0.12), (-0.8, 0.3), (-1.05, 0.05 - 0.3 * tail_up + 0.06 * math.sin(t * 1.5)),
               (-1.35, 0.12 - 0.2 * tail_up + 0.08 * math.sin(t * 1.9)), 22)
    ss.line(P(tl), (*INK, 255), max(3, s * 0.05)); ss.line(P(tl), PINK, max(2, s * 0.036))
    # patas de trás
    ss.poly(P(A.ell_pts(-0.25, 0.2, 0.16, 0.1, 10, 20)), fill=FUR_D, ink=INK, w=iw)
    ss.poly(P(A.ell_pts(-0.16, 0.3, 0.1, 0.03, 0, 14)), fill=PINK, ink=INK, w=iw * 0.8)
    # corpo
    body = A.spline([(-0.45, 0.12), (-0.42, -0.08), (-0.2, -0.22 - br), (0.1, -0.22 - br), (0.28, -0.12), (0.3, 0.12),
                     (0.05, 0.24), (-0.3, 0.25)], 8)
    ss.poly(P(body), fill=FUR, ink=INK, w=iw)
    ss.poly(P(A.spline([(-0.3, 0.16), (0.0, 0.2), (0.22, 0.12), (0.0, 0.1)], 6)), fill=FUR_L)
    for k in range(7):  # pelos
        xx = -0.32 + k * 0.08
        ss.line(P([(xx, -0.16 - br), (xx - 0.03, -0.12 - br)]), (*FUR_D, 200), max(1, s * 0.006))
    # cabeça (gira para cima com look)
    hx, hy = 0.3, -0.06
    hr = -28 * look
    def HP(pts):
        c, sn = math.cos(math.radians(hr)), math.sin(math.radians(hr))
        return P([(hx + px * c - py * sn, hy + px * sn + py * c) for px, py in pts])
    head = A.spline([(-0.08, -0.12), (0.1, -0.13), (0.24, -0.06), (0.3, 0.0), (0.24, 0.05), (0.08, 0.1), (-0.08, 0.12)], 8)
    ss.poly(HP(head), fill=FUR, ink=INK, w=iw)
    ss.poly(HP(A.spline([(0.02, 0.06), (0.2, 0.04), (0.26, 0.02), (0.1, 0.09)], 5)), fill=FUR_L)
    # bigodes
    for k in range(4):
        a0 = -0.25 + k * 0.17
        bend = whisk * (0.6 + 0.2 * k) + 0.02 * math.sin(t * 9 + k)
        pts = A.bez((0.26, 0.0), (0.38, a0 * 0.3), (0.5, a0 * 0.6 + bend * 0.3), (0.6 - 0.05 * abs(bend), a0 * 0.9 + bend * 0.6), 10)
        ss.line(HP(pts), (40, 34, 40, 230), max(1, s * 0.005), cap=False)
    # focinho
    nx, ny = HP([(0.3, 0.0)])[0]
    ss.circle(nx, ny, s * 0.028, fill=PINK, ink=INK, w=iw * 0.8)
    # orelha
    ex, ey = HP([(-0.02, -0.14)])[0]
    ss.poly(HP(A.ell_pts(-0.03, -0.17, 0.1, 0.11, -15, 24)), fill=FUR, ink=INK, w=iw)
    ss.poly(HP(A.ell_pts(-0.025, -0.17, 0.07, 0.075, -15, 20)), fill=PINK)
    # olho
    ox, oy = HP([(0.13, -0.05)])[0]; er = s * 0.032 * eye
    ss.circle(ox, oy, er, fill=(16, 10, 14), ink=INK, w=iw * 0.6)
    ss.circle(ox - er * 0.3 + er * 0.15 * look, oy - er * 0.35, er * 0.38, fill=(255, 255, 255, 240))
    ss.circle(ox + er * 0.32, oy + er * 0.3, er * 0.14, fill=(255, 255, 255, 170))
    # pata da frente
    ss.poly(P(A.ell_pts(0.2, 0.22, 0.05, 0.07, 0, 14)), fill=FUR_D, ink=INK, w=iw * 0.8)
    ss.poly(P(A.ell_pts(0.24, 0.29, 0.05, 0.02, 0, 12)), fill=PINK, ink=INK, w=iw * 0.6)


# ======================================================================= peças: cabine, roda, contrapeso
def cabin_side(ss, x0, y0, x1, y1, light=1.0, people=0):
    ss.rrect(x0, y0, x1, y1, 10, fill=CAB, ink=INK, w=5)
    ss.rect(x0 + 16, y0 + 16, x1 - 16, y1 - 16, (*CAB_L, 255))
    ss.rect(x0 + 16, y0 + 16, x1 - 16, y0 + 40, (255, 236, 170, int(200 * light)))
    ss.line([((x0 + x1) / 2, y0 + 40), ((x0 + x1) / 2, y1 - 16)], (*CAB, 255), 4)
    for k in range(people):
        px = lerp(x0 + 50, x1 - 50, (k + 0.5) / people); py = y1 - 16
        h = (y1 - y0) * 0.5
        ss.rrect(px - 18, py - h, px + 18, py, 12, fill=(80, 110, 170), ink=INK, w=3)
        ss.circle(px, py - h - 16, 18, fill=(240, 196, 160), ink=INK, w=3)
    # sapata de freio nas laterais
    for xx in (x0 - 12, x1 + 12):
        ss.rrect(xx - 12, y1 - 60, xx + 12, y1 - 10, 4, fill=YEL, ink=INK, w=3)


def sheave(ss, cx, cy, r, ang):
    ss.circle(cx, cy, r, fill=STEEL_D, ink=INK, w=6)
    for k in range(5):  # sulcos
        ss.circle(cx, cy, r - 10 - k * 10, ink=(70, 74, 86), w=3)
    ss.circle(cx, cy, r * 0.55, fill=STEEL, ink=INK, w=5)
    for k in range(6):
        a = ang + k * math.pi / 3
        ss.line([(cx + r * 0.18 * math.cos(a), cy + r * 0.18 * math.sin(a)), (cx + r * 0.52 * math.cos(a), cy + r * 0.52 * math.sin(a))],
                STEEL_D, max(4, r * 0.08))
    ss.circle(cx, cy, r * 0.16, fill=(80, 84, 96), ink=INK, w=4)


def cweight(ss, x0, y0, x1, y1, label=True):
    ss.rrect(x0, y0, x1, y1, 8, fill=IRON, ink=INK, w=5)
    n = max(2, int((y1 - y0) / 46))
    for k in range(1, n):
        yy = lerp(y0, y1, k / n)
        ss.line([(x0 + 6, yy), (x1 - 6, yy)], (100, 98, 108), 4)


def cables(ss, pts_list, w=8):
    for pts in pts_list:
        ss.line(pts, (*INK, 255), w + 4); ss.line(pts, STEEL, w)


def stripes(ss, x0, y0, x1, y1, off=0):
    ss.rect(x0, y0, x1, y1, (20, 18, 20))
    k = -2
    while True:
        xa = x0 + k * 70 + off
        if xa > x1 + 70: break
        ss.poly([(xa, y1), (xa + 35, y1), (xa + 35 + (y1 - y0), y0), (xa + (y1 - y0), y0)], fill=YEL)
        k += 1


# ======================================================================= cena 1: gancho (contra-plongée do poço)
def shaft_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (40, 34, 34)), (0.6, (88, 78, 72)), (1, (60, 52, 50))])
        ss = SS(W, H, s=1)
        fx0, fy0, fx1, fy1 = 410, 120, 670, 300  # boca lá em cima (longe)
        ss.poly([(0, 0), (fx0, fy0), (fx0, fy1), (0, 1700)], fill=(118, 106, 98))
        ss.poly([(W, 0), (fx1, fy0), (fx1, fy1), (W, 1700)], fill=(96, 86, 82))
        ss.poly([(0, 0), (W, 0), (fx1, fy0), (fx0, fy0)], fill=(70, 62, 60))
        ss.rect(fx0, fy0, fx1, fy1, (24, 20, 22))
        rng = np.random.default_rng(4)
        for k in range(14):  # marcas dos andares (portas) nas paredes
            u = (k / 14) ** 1.7
            xl = lerp(0, fx0, 1 - u); yl = lerp(1700, fy1, 1 - u)
            ss.line([(xl, yl), (lerp(0, fx0, 1 - u * 0.9), lerp(1700, fy1, 1 - u * 0.9))], (60, 54, 52), 3)
        for k in range(10):
            u = 1 - (k / 10) ** 1.4
            yy = lerp(fy1, 1700, u); xl = lerp(fx0, 0, u); xr = lerp(fx1, W, u)
            ss.line([(xl, yy), (lerp(fx0, 0, u * 0.98), yy - 4)], (70, 62, 58), 2)
        for _ in range(500):
            x = rng.uniform(0, W); y = rng.uniform(0, 1700)
            ss.circle(x, y, rng.uniform(1, 3), fill=(40, 34, 34, 90))
        im.alpha_composite(ss.get())
        # trilhos-guia convergindo
        ss = SS(W, H, s=2)
        for (xa, xb) in ((150, 470), (930, 610)):
            ss.poly([(xa - 22, 1700), (xa + 22, 1700), (xb + 5, fy1), (xb - 5, fy1)], fill=STEEL_D, ink=INK, w=3)
            ss.line([(xa, 1700), (xb, fy1)], STEEL, 8)
        im.alpha_composite(ss.get())
        im.alpha_composite(A.glow(500, SOD, 120), (-260, 760))
        im.alpha_composite(A.glow(300, SOD, 160), (-120, 900))
        return im
    return cached("shaft", mk).copy()


def cabin_under(img, u, t):
    """fundo da cabine visto de baixo; u 0 = longe (lá em cima), 1 = perto"""
    fx0, fy0, fx1, fy1 = 410, 120, 670, 300
    x0 = lerp(fx0 + 10, 120, u); x1 = lerp(fx1 - 10, 960, u)
    y0 = lerp(fy0 + 10, 260, u); y1 = lerp(fy1 - 10, 860, u)
    ss = SS(W, H, s=2)
    ss.rrect(x0, y0, x1, y1, 10 + 10 * u, fill=CAB, ink=INK, w=3 + 4 * u)
    for k in range(1, 4):
        xx = lerp(x0, x1, k / 4)
        ss.line([(xx, y0 + 6), (xx, y1 - 6)], (46, 52, 64), 3 + 8 * u)
    yy = (y0 + y1) / 2
    ss.line([(x0 + 6, yy), (x1 - 6, yy)], (46, 52, 64), 3 + 8 * u)
    # para-choque/amortecedor e luz embaixo
    ss.circle((x0 + x1) / 2, yy, 14 + 40 * u, fill=(255, 236, 170, 230), ink=INK, w=2 + 3 * u)
    for xx in (x0, x1):
        ss.rrect(xx - 8 - 18 * u, y1 - 30 - 60 * u, xx + 8 + 18 * u, y1, 4, fill=YEL, ink=INK, w=2 + 2 * u)
    img.alpha_composite(ss.get())
    img.alpha_composite(A.glow(int(60 + 220 * u), (255, 236, 170), int(80 + 70 * u)), (int((x0 + x1) / 2 - (60 + 220 * u)), int(yy - (60 + 220 * u))))


def hook_frame(t, u=None):
    img = shaft_bg()
    u = (0.18 + 0.045 * t) if u is None else u
    cabin_under(img, clamp01(u), t)
    ss = SS(W, H, s=2)
    ss.poly([(0, 1660), (W, 1660), (W, H), (0, H)], fill=(70, 62, 58))
    stripes(ss, 0, 1660, W, 1720)
    # amortecedor (mola) no centro do fundo do poço
    ss.rrect(860, 1440, 1000, 1670, 10, fill=(200, 50, 50), ink=INK, w=5)
    for k in range(6):
        ss.line([(860, 1460 + k * 36), (1000, 1478 + k * 36)], (255, 220, 200), 5)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    rat(ss, 400 + 10 * math.sin(t * 0.7), 1560, 640, t=t, rot=-4, eye=1.2, look=0.85 + 0.1 * math.sin(t * 1.3), tail_up=0.2)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 18, 0.45, col=(10, 6, 6))
    A.paste(img, sh, -pad + 10, -pad + 24)
    img.alpha_composite(sp)
    return A.vignette(img, 0.45)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.02 + 0.01 * math.sin(lt * 1.1), dx=3 * math.sin(lt * 9) * 0.5, rot=0.3 * math.sin(lt * 0.7))


# ======================================================================= cena 2: 1 tonelada pendurada
def shaft_side(img, t, dark=0.0):
    ss = SS(W, H, s=2)
    ss.rect(0, 0, 140, H, CONC_D); ss.rect(W - 140, 0, W, H, CONC_D)
    for y in range(0, H, 260):
        ss.line([(0, y), (140, y)], (70, 62, 60), 4); ss.line([(W - 140, y), (W, y)], (70, 62, 60), 4)
    ss.rect(140, 0, 170, H, STEEL_D); ss.rect(W - 170, 0, W - 140, H, STEEL_D)
    img.alpha_composite(ss.get())


def hang(ctx, lt):
    img = A.vgrad(W, H, [(0, (58, 50, 48)), (1, (34, 28, 28))])
    img.alpha_composite(A.glow(600, SOD, 70), (-300, 900))
    shaft_side(img, lt)
    sw = 6 * math.sin(lt * 1.4)
    y0 = 520 + 30 * math.sin(lt * 0.9)
    ss = SS(W, H, s=2)
    cables(ss, [[(470 + k * 46, -20), (470 + k * 46 + sw, y0)] for k in range(4)], 7)
    cabin_side(ss, 240 + sw, y0, 840 + sw, y0 + 520, people=3)
    tq = ease((lt - ctx.wt("tonelada") + 0.4) / 0.6)
    if tq > 0:
        ss.rrect(380 + sw, y0 + 130, 700 + sw, y0 + 250, 20, fill=(255, 255, 255, int(235 * tq)), ink=(*INK, int(255 * tq)), w=5)
        ss.text((540 + sw, y0 + 192), "~1.000 kg", 72, "anton", fill=(*INK, int(255 * tq)))
    img.alpha_composite(ss.get())
    cq = ease((lt - ctx.wt("cabos") + 0.3) / 0.5)
    if cq > 0:
        ss = SS(W, H, s=2)
        for k in range(4):
            ss.line([(470 + k * 46, 0), (470 + k * 46 + sw * 0.9, y0)], (255, 222, 40, int(200 * cq)), 4)
        img.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(3)))
    ss = SS(W, H, s=2)
    ss.rect(140, 1700, W - 140, H, (70, 62, 58)); stripes(ss, 140, 1700, W - 140, 1740)
    rat(ss, 330, 1650, 260, t=lt, eye=1.2, look=0.9)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * easeio(lt / max(1, ctx.dur)), dy=-12 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 3: raio-X do motor (roda e atrito)
def motor(ctx, lt):
    img = A.vgrad(W, H, [(0, (30, 36, 54)), (1, (14, 16, 28))])
    ss = SS(W, H, s=1)
    for k in range(0, W, 60): ss.line([(k, 0), (k, H)], (40, 52, 80, 120), 2)
    for k in range(0, H, 60): ss.line([(0, k), (W, k)], (40, 52, 80, 120), 2)
    img.alpha_composite(ss.get())
    ta = ctx.wt("atrito"); tm = ctx.wt("motor")
    spin = ease((lt - ta + 0.6) / 0.6)
    ang = lt * 2.2 * spin
    cx, cy, r = 600, 690, 230
    mv = 60 * math.sin(lt * 0.0) + 160 * (lt - ta) * spin if spin > 0 else 0.0
    mv = max(0.0, mv)
    ss = SS(W, H, s=2)
    # motor (caixa) ligado à roda
    ss.rrect(80, 560, 330, 820, 24, fill=(90, 100, 120), ink=INK, w=6)
    ss.rect(330, cy - 26, cx, cy + 26, (150, 156, 168))
    ss.text((205, 860), "MOTOR", 54, "anton", fill=(230, 236, 245), stroke=6)
    sheave(ss, cx, cy, r, ang)
    # cabos passando por cima da roda e descendo dos dois lados
    arc = [(cx + (r - 8) * math.cos(a), cy + (r - 8) * math.sin(a)) for a in np.linspace(math.pi, 2 * math.pi, 30)]
    cables(ss, [[(cx - r + 8, 1960)] + arc + [(cx + r - 8, 1960)]], 12)
    img.alpha_composite(ss.get())
    # eletricidade (amarelo) no motor
    me = ease((lt - tm + 0.2) / 0.4)
    if me > 0:
        ss = SS(W, H, s=2); rng = np.random.default_rng(int(lt * 12))
        for k in range(3):
            pts = [(110 + rng.uniform(0, 190), 580)]
            for j in range(5): pts.append((110 + rng.uniform(0, 190), 600 + j * 44))
            ss.line(pts, (*ELEC, int(255 * me)), 6)
        img.alpha_composite(ss.get())
        img.alpha_composite(A.glow(200, ELEC, int(90 * me)), (5, 490))
    # atrito: brilho laranja onde o cabo encosta + setas da rotação
    if spin > 0:
        ss = SS(W, H, s=2)
        for k in range(14):
            a = math.pi + k / 13 * math.pi
            ss.circle(cx + r * math.cos(a), cy + r * math.sin(a), 18, fill=(255, 140, 40, int(150 * spin)))
        for sg in (0, 1):
            a0 = math.pi * 1.15 + sg * 0.75; pts = [(cx + (r + 70) * math.cos(a0 + j * 0.05), cy + (r + 70) * math.sin(a0 + j * 0.05)) for j in range(12)]
            ss.line(pts, (255, 222, 40, int(255 * spin)), 16)
            e = pts[-1]; p = pts[-2]
            A.arrow(ss, p[0], p[1], e[0] + (e[0] - p[0]) * 2.5, e[1] + (e[1] - p[1]) * 2.5, (255, 222, 40, int(255 * spin)), w=16, iw=3)
        img.alpha_composite(ss.get())
    # embaixo: cabine sobe (esq.) e contrapeso desce (dir.)
    ss = SS(W, H, s=2)
    cabin_side(ss, cx - r - 170, 1380 - mv, cx - r + 170, 1720 - mv, people=2)
    cweight(ss, cx + r - 70, 1300 + mv, cx + r + 70, 1640 + mv)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03 + 0.02 * math.sin(lt * 0.6), rot=0.3 * math.sin(lt * 0.8))


# ======================================================================= cena 4: o contrapeso
def people_row(ss, x, y, n, hi, a=255, sz=1.0):
    for k in range(n):
        px = x + k * 70 * sz
        col = (255, 150, 40) if k < hi else (150, 150, 160)
        ss.circle(px, y - 70 * sz, 18 * sz, fill=(*col, a), ink=(*INK, a), w=3)
        ss.rrect(px - 20 * sz, y - 48 * sz, px + 20 * sz, y, 10, fill=(*col, a), ink=(*INK, a), w=3)


def counter(ctx, lt):
    img = A.vgrad(W, H, [(0, (64, 56, 52)), (1, (36, 30, 30))])
    img.alpha_composite(A.glow(600, SOD, 60), (500, -200))
    shaft_side(img, lt)
    tc = ctx.wt("contrapeso"); th = ctx.wt("metade")
    cq = ease((lt - tc + 0.9) / 0.9)
    cx, cy, r = 540, 540, 170
    ss = SS(W, H, s=2)
    sheave(ss, cx, cy, r, lt * 0.6)
    arc = [(cx + (r - 6) * math.cos(a), cy + (r - 6) * math.sin(a)) for a in np.linspace(math.pi, 2 * math.pi, 24)]
    cwy = lerp(-300, 1340, cq)
    cables(ss, [[(cx - r + 6, 1300)] + arc + [(cx + r - 6, cwy)]], 10)
    cabin_side(ss, cx - r - 190, 1300, cx - r + 190, 1700, people=3)
    cweight(ss, cx + r - 80, cwy, cx + r + 80, cwy + 380)
    img.alpha_composite(ss.get())
    hq = ease((lt - th + 0.3) / 0.6)
    if hq > 0:
        ss = SS(W, H, s=2)
        ss.rrect(600, 760, 1000, 1010, 24, fill=(255, 255, 255, int(235 * hq)), ink=(*INK, int(255 * hq)), w=5)
        ss.text((800, 805), "contrapeso =", 44, "anton", fill=(*INK, int(255 * hq)))
        ss.text((800, 860), "cabine + ~45%", 50, "anton", fill=(200, 90, 20, int(255 * hq)))
        people_row(ss, 680, 990, 6, 3, a=int(255 * hq), sz=0.85)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * easeio(lt / max(1, ctx.dur)), dy=8 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 5: só a diferença (balança)
def counter2(ctx, lt):
    img = A.vgrad(W, H, [(0, (250, 226, 196)), (1, (232, 196, 160))])
    td = ctx.wt("diferença")
    q = ease((lt - td + 0.4) / 0.6)
    tilt = lerp(-9, -2, q) + 1.5 * math.sin(lt * 3) * (1 - q)
    ss = SS(W, H, s=2)
    px, py = 540, 1560
    ss.poly([(px - 90, 1760), (px + 90, 1760), (px + 20, py), (px - 20, py)], fill=(120, 100, 90), ink=INK, w=6)
    a = math.radians(tilt); L = 330
    lx, ly = px - L * math.cos(a), py - L * math.sin(a); rx, ry = px + L * math.cos(a), py + L * math.sin(a)
    ss.line([(lx, ly), (rx, ry)], INK, 30); ss.line([(lx, ly), (rx, ry)], (180, 150, 120), 20)
    ss.circle(px, py, 26, fill=STEEL, ink=INK, w=5)
    cabin_side(ss, lx - 125, ly - 260, lx + 125, ly - 20, people=2)
    cweight(ss, rx - 80, ry - 250, rx + 80, ry - 20)
    ss.text((lx, ly + 60), "CABINE + GENTE", 46, "anton", fill=(*INK, 255))
    ss.text((rx, ry + 60), "CONTRAPESO", 46, "anton", fill=(*INK, 255))
    # o motor só puxa a diferença: pesinho pequeno + seta amarela
    if q > 0:
        ss.rrect(px - 70, 560, px + 70, 680, 14, fill=(255, 150, 40, int(255 * q)), ink=(*INK, int(255 * q)), w=5)
        ss.text((px, 620), "Δ", 80, "anton", fill=(255, 255, 255, int(255 * q)), stroke=5)
        A.arrow(ss, px, 700, lx + 30, ly - 290, (255, 222, 40, int(255 * q)), w=30, ink=(*INK, int(255 * q)), iw=5)
        ss.text((px, 520), "DIFERENÇA", 58, "anton", fill=(200, 90, 20, int(255 * q)), stroke=0)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * q, rot=0.5 * math.sin(lt))


# ======================================================================= cena 6: Visão do Bicho (bigodes e vento)
def vision(ctx, lt):
    tv = ctx.wt("vento")
    q = ease((lt - tv + 0.8) / 1.0)
    base = hook_frame(lt + 4.0, u=0.45 + 0.1 * lt / max(1, ctx.dur))
    # rato enxerga pouco: borrado e sem cor
    arr = np.asarray(base.filter(ImageFilter.GaussianBlur(9)).convert("RGB"), np.float32)
    g = arr.mean(axis=2, keepdims=True)
    arr = (arr * 0.25 + g * 0.75) * 0.55
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    # ar empurrado pela cabine (verde), descendo e abrindo para os lados
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(5)
    for k in range(34):
        x0 = rng.uniform(260, 820); ph = rng.uniform(0, 1)
        u = (lt * (0.6 + 0.8 * q) + ph) % 1.0
        pts = []
        for j in range(10):
            v = clamp01(u - j * 0.03)
            yy = lerp(700, 1800, v)
            xx = x0 + (x0 - 540) * 1.4 * v * v
            pts.append((xx, yy))
        ss.line(pts, (*AIR, int((90 + 160 * q) * (1 - u * 0.5))), 8 + 6 * q)
    img.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(2)))
    # bigodes nas bordas (POV), dobrando com o vento
    ss = SS(W, H, s=2)
    for sg in (-1, 1):
        for k in range(5):
            bx = 540 + sg * (120 + k * 30); by = H + 30
            bend = (0.3 + 0.7 * q) * (0.6 + 0.12 * k) + 0.05 * math.sin(lt * 9 + k)
            L = 760 + k * 90
            ang = math.radians(-90 + sg * (28 + k * 9))
            ex = bx + L * math.cos(ang); ey = by + L * math.sin(ang)
            cxm = bx + L * 0.5 * math.cos(ang) + sg * 120 * bend; cym = by + L * 0.5 * math.sin(ang) + 160 * bend
            pts = A.bez((bx, by), (cxm, cym), (ex + sg * 140 * bend, ey + 260 * bend), (ex + sg * 180 * bend, ey + 330 * bend), 16)
            ss.line(pts, (20, 16, 18, 255), 13 - k); ss.line(pts, (230, 226, 220, 255), 8 - k)
        ss.circle(540 + sg * 300, H + 120, 260, fill=FUR, ink=INK, w=6)
    ss.circle(540, H + 40, 70, fill=PINK, ink=INK, w=5)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03 + 0.02 * math.sin(lt), dx=6 * q * math.sin(lt * 11))


# ======================================================================= cena 7: cabo arrebenta + limitador de velocidade
def gauge_speed(ss, cx, cy, r, v, a=255):
    ss.circle(cx, cy, r, fill=(250, 250, 245, a), ink=(*INK, a), w=6)
    for k in range(9):
        an = math.radians(150 + k * 30)
        ss.line([(cx + r * 0.78 * math.cos(an), cy + r * 0.78 * math.sin(an)), (cx + r * 0.92 * math.cos(an), cy + r * 0.92 * math.sin(an))],
                (*INK, a), 5)
    pts = [(cx + r * 0.85 * math.cos(math.radians(an)), cy + r * 0.85 * math.sin(math.radians(an))) for an in range(330, 391, 5)]
    ss.line(pts, (230, 40, 50, a), 14, cap=False)
    an = math.radians(150 + 240 * clamp01(v))
    ss.line([(cx, cy), (cx + r * 0.75 * math.cos(an), cy + r * 0.75 * math.sin(an))], (230, 40, 50, a), 10)
    ss.circle(cx, cy, 16, fill=(*INK, a))


def brake(ctx, lt):
    img = A.vgrad(W, H, [(0, (56, 48, 46)), (1, (30, 26, 26))])
    shaft_side(img, lt)
    ts = ctx.wt("arrebentar"); tf = ctx.wt("freio"); tv = ctx.wt("velocidade")
    snap = clamp01((lt - ts - 0.1) / 0.3)
    gq = ease((lt - tf + 0.2) / 0.6)
    ss = SS(W, H, s=2)
    # limitador lá em cima (roda pequena com contrapesinhos girando) e o cabo dele descendo até a cabine
    gx, gy = 840, 600
    ang = lt * 5
    ss.circle(gx, gy, 90, fill=STEEL_D, ink=INK, w=5)
    for k in range(2):
        a = ang + k * math.pi
        ss.circle(gx + 55 * math.cos(a), gy + 55 * math.sin(a), 22, fill=(255, 150, 40), ink=INK, w=4)
    ss.circle(gx, gy, 14, fill=INK)
    ss.line([(gx + 90, gy), (gx + 90, 1960)], (255, 150, 40, int(80 + 175 * gq)), 6)
    ss.line([(gx - 90, gy), (gx - 90, 1330)], (255, 150, 40, int(80 + 175 * gq)), 6)
    ss.text((gx, gy - 140), "LIMITADOR", 46, "anton", fill=(255, 150, 40, int(255 * gq)), stroke=5)
    # cabine com o cabo principal; o cabo arrebenta
    y0 = 1300 + 30 * snap
    for k in range(3):
        x = 380 + k * 50
        if snap <= 0:
            ss.line([(x, -20), (x, y0)], INK, 12); ss.line([(x, -20), (x, y0)], STEEL, 7)
        else:
            cut = 900
            ss.line([(x, -20), (x - 30 * snap, cut - 200 * snap)], STEEL, 7)
            ss.line([(x + 20 * snap, cut + 40 + 60 * snap), (x, y0)], STEEL, 7)
    cabin_side(ss, 220, y0, 700, y0 + 440, people=2)
    img.alpha_composite(ss.get())
    if 0 < snap < 1:
        img.alpha_composite(Image.new("RGBA", (W, H), (255, 60, 60, int(70 * (1 - snap)))))
    if snap > 0:
        ss = SS(W, H, s=2)
        for k in range(6):
            a = k * math.pi / 3 + 0.3
            ss.line([(420 + 40 * math.cos(a), 920 + 40 * math.sin(a)), (420 + 110 * math.cos(a), 920 + 110 * math.sin(a))], (255, 222, 40, int(255 * (1 - snap * 0.6))), 8)
        img.alpha_composite(ss.get())
    vq = ease((lt - tv + 0.3) / 0.6)
    if vq > 0:
        ss = SS(W, H, s=2)
        gauge_speed(ss, 300, 620, 150, 0.35 + 0.08 * math.sin(lt * 3), a=int(255 * vq))
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dx=12 * (1 - snap) * snap * 4 * math.sin(lt * 50))


# ======================================================================= cena 8: cunhas mordem o trilho
def brake2(ctx, lt):
    img = A.vgrad(W, H, [(0, (44, 40, 40)), (1, (24, 20, 22))])
    tm = ctx.wt("mordem"); td = ctx.wt("dispara")
    fall = clamp01((lt - td + 0.2) / 0.6)
    grip = clamp01((lt - tm + 0.05) / 0.18)
    ss = SS(W, H, s=2)
    # trilho (perfil em T) no centro, com marcas que passam rápido enquanto cai
    ss.rect(480, -10, 600, H + 10, STEEL_D); ss.rect(520, -10, 560, H + 10, STEEL)
    spd = 2200 * fall * (1 - grip)
    off = (lt * spd) % 200
    for k in range(-1, 12):
        yy = k * 200 - off
        ss.line([(482, yy), (598, yy)], (80, 86, 98), 4)
    # bloco do freio preso na cabine
    by = 980
    ss.rrect(300, by - 260, 780, by + 260, 20, fill=(70, 74, 84), ink=INK, w=6)
    ss.rect(470, by - 270, 610, by + 270, (40, 40, 46))
    ss.rect(480, by - 270, 600, by + 270, STEEL_D); ss.rect(520, by - 270, 560, by + 270, STEEL)
    gp = 120 * (1 - grip)
    for sg in (-1, 1):  # cunhas
        x = 540 + sg * (70 + gp)
        ss.poly([(x, by - 180), (x + sg * 70, by - 220), (x + sg * 70, by + 220), (x, by + 180)], fill=YEL, ink=INK, w=6)
    ss.text((540, by + 360), "CUNHAS", 70, "anton", fill=YEL, stroke=8)
    img.alpha_composite(ss.get())
    if grip > 0:
        ss = SS(W, H, s=2); rng = np.random.default_rng(int(lt * 30))
        for k in range(26):
            a = rng.uniform(-math.pi, 0); L = rng.uniform(80, 260) * (1 - 0.6 * clamp01((lt - tm) / 1.2))
            sx = 540 + rng.uniform(-60, 60); sy = by + rng.choice([-200, 200])
            ss.line([(sx, sy), (sx + L * math.cos(a), sy + L * math.sin(a))], (255, rng.integers(140, 230), 40, 230), 5)
        img.alpha_composite(ss.get())
        img.alpha_composite(A.glow(300, (255, 170, 60), int(120 * (1 - clamp01((lt - tm) / 1.0)))), (240, by - 300))
    shake = grip * math.exp(-max(0.0, lt - tm) * 4)
    return A.cam(img, zoom=1.03 + 0.03 * grip, dy=-20 * fall * (1 - grip) * math.sin(lt * 30) + 12 * shake * math.sin(lt * 60))


# ======================================================================= cenas 9-10: 1854 (sépia) e loop
def otis_frame(t, cut=0.0, drop=0.0, man_arm=0.0):
    img = A.vgrad(W, H, [(0, (246, 228, 194)), (1, (222, 196, 156))])
    ss = SS(W, H, s=1); rng = np.random.default_rng(9)
    for _ in range(300):
        ss.circle(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(1, 3), fill=(*SEP_D, 40))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    # torre com cremalheira dentada nos dois lados
    for x in (200, 880):
        ss.rect(x - 34, 300, x + 34, 1800, SEP_M)
        ss.line([(x - 34, 300), (x - 34, 1800)], SEP_D, 5); ss.line([(x + 34, 300), (x + 34, 1800)], SEP_D, 5)
        sg = 1 if x < 540 else -1
        for k in range(30):
            yy = 320 + k * 50
            ss.poly([(x + sg * 34, yy), (x + sg * 60, yy + 40), (x + sg * 34, yy + 46)], fill=SEP_D)
    ss.rect(150, 270, 930, 310, SEP_D)
    ss.circle(540, 300, 40, fill=SEP_M, ink=SEP_D, w=5)
    # plataforma (cai alguns centímetros e trava)
    py = 1320 + 50 * drop
    if cut < 1:
        ss.line([(540, 300), (540, py - 380)], SEP_D, 10)
    else:
        ss.line([(540, 300), (540, 640)], SEP_D, 10)
        ss.line([(540, 720), (540, py - 380)], SEP_D, 10)
    for sg in (-1, 1):
        ss.line([(540, py - 380), (540 + sg * 300, py - 10)], SEP_D, 6)
    ss.rect(220, py - 10, 860, py + 30, SEP_D)
    for sg in (-1, 1):  # linguetas da catraca
        ss.poly([(540 + sg * 320, py), (540 + sg * 300, py - 30), (540 + sg * 344 - sg * 0, py - 34 + 10 * drop)], fill=(150, 60, 40), ink=SEP_D, w=3)
    # o inventor de cartola, braço erguido
    mx = 600
    ss.rrect(mx - 50, py - 250, mx + 50, py - 20, 20, fill=(70, 50, 40), ink=SEP_D, w=4)
    ss.circle(mx, py - 290, 38, fill=(236, 200, 160), ink=SEP_D, w=4)
    ss.rect(mx - 30, py - 400, mx + 30, py - 320, (40, 30, 26)); ss.rect(mx - 48, py - 330, mx + 48, py - 316, (40, 30, 26))
    arm = math.radians(lerp(60, -70, man_arm))
    ss.line([(mx + 40, py - 220), (mx + 40 + 120 * math.cos(arm), py - 220 + 120 * math.sin(arm))], (70, 50, 40), 22)
    ss.line([(mx - 40, py - 220), (mx - 90, py - 120)], (70, 50, 40), 22)
    # público
    for k in range(9):
        hx = 80 + k * 115; hy = 1840 + 20 * math.sin(k * 2.3)
        ss.circle(hx, hy - 60, 36, fill=(90, 70, 56))
        ss.rrect(hx - 50, hy - 30, hx + 50, hy + 120, 30, fill=(90, 70, 56))
    img.alpha_composite(ss.get())
    if cut > 0:
        ss = SS(W, H, s=2)
        ss.poly([(560, 640), (640, 600), (700, 700), (600, 720)], fill=(200, 200, 210), ink=SEP_D, w=4)
        ss.line([(650, 650), (820, 520)], (120, 80, 50), 14)
        img.alpha_composite(ss.get())
    return A.vignette(img, 0.55)


def otis(ctx, lt):
    tc = ctx.wt("cortar")
    arm = ease((lt - 0.4) / 0.8)
    cut = clamp01((lt - ctx.wt("elevador") - 0.2) / 0.1)
    return A.cam(otis_frame(lt, cut=cut, man_arm=arm), zoom=1.0 + 0.05 * easeio(lt / max(1, ctx.dur)), dy=-20 * easeio(lt / max(1, ctx.dur)))


def loop(ctx, lt):
    tp = ctx.wt("parou"); tb = ctx.wt("por")
    if lt < tb - 0.05:
        drop = ease((lt - 0.1) / 0.25) if lt < tp else 1.0
        sh = math.exp(-max(0.0, lt - tp) * 5) if lt >= tp else 0.0
        img = otis_frame(lt + 5, cut=1.0, drop=drop, man_arm=1.0)
        return A.cam(img, zoom=1.05, dy=-20 + 18 * sh * math.sin(lt * 50))
    tr = lt - ctx.dur + 1 / 30.0
    k = (lt - tb) / max(0.3, ctx.dur - tb)
    back = easeio(clamp01(k))
    img = hook_frame(tr, u=lerp(0.1, 0.18 + 0.045 * tr, back))
    return A.cam(img, zoom=lerp(1.08, 1.02 + 0.01 * math.sin(tr * 1.1), back),
                 dx=3 * math.sin(tr * 9) * 0.5 * back, rot=0.3 * math.sin(tr * 0.7) * back)


# ======================================================================= capa
def cover_bg(cv):
    img = shaft_bg()
    cabin_under(img, 0.55, 1.0)
    ss = SS(W, H, s=2)
    ss.poly([(0, 1660), (W, 1660), (W, H), (0, H)], fill=(70, 62, 58))
    stripes(ss, 0, 1660, W, 1720)
    img.alpha_composite(ss.get())
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 600)
    ss = SS(int(2.1 * s), int(0.95 * s), s=2)
    rat(ss, 1.42 * s, 0.6 * s, s, t=0.5, eye=1.7, look=0.6, tail_up=0.3)
    return ss.get()
