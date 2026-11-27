"""Dia 8B — "E se você fosse uma capivara na represa?" (formato CURTO; paleta: manhã de neblina prata-azulada, concreto
bege-quente da barragem, rio verde-jade, morros verde-musgo, capivara caramelo; raio-X azul-noite com água em verde,
corrente em amarelo e bobinas cor de cobre).

Cenas: hook (no rio, rente à água: a capivara com só a cabeça de fora e a parede gigante da barragem atrás, régua 196 m),
behind (corte lateral: lago lá no alto, barragem, rio embaixo), vision (Visão do Bicho: periscópio — olhos, orelhas e narinas
na mesma linha, no topo da cabeça), vision2 (POV metade fora/metade dentro d'água: o corpo escondido, patas remando),
fall (raio-X: a água despenca pelo tubo até a turbina, régua de 100 m), pool (uma piscina olímpica sendo engolida a cada
4 s), magnet (gerador em corte: rotor com ímãs girando dentro das bobinas de cobre), electrons (elétrons amarelos correndo
no fio até as casas), brasil (lâmpada gigante cheia de água: mais da metade), loop (a água sai e volta ao quadro inicial).
A capivara fica sempre no rio, longe das turbinas e das comportas.
Fatos: Itaipu Binacional; Water Power Magazine; EPE.
"""
import math
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

FUR = (170, 112, 66); FUR_D = (120, 76, 44); FUR_L = (204, 150, 98); NOSE = (70, 46, 36)
CONC = (222, 204, 176); CONC_D = (180, 160, 134); CONC_L = (240, 228, 206)
JADE = (40, 150, 130); JADE_D = (20, 100, 92); JADE_L = (120, 210, 190)
MIST0 = (196, 210, 222); MIST1 = (232, 236, 236)
HILL = (96, 130, 96); HILL_D = (70, 104, 76)
YEL = (255, 222, 40); COPPER = (214, 120, 60); GREEN = (80, 230, 140); WATERX = (60, 200, 150)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


def glow_at(img, x, y, r, col, a):
    A.paste_c(img, A.glow(int(r), col, int(a)), x, y)


# ======================================================================= capivara (de lado, olhando para a direita)
def capy(ss, x, y, s, flip=1, t=0.0, eye=1.0, head_only=False, alpha=255, legs=True):
    """origem = centro do corpo; s = comprimento do corpo/2"""
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    a = alpha; iw = max(2, s * 0.02)
    if not head_only:
        if legs:
            for lx in (-0.55, -0.3, 0.35, 0.6):
                sw = 0.06 * math.sin(t * 4 + lx * 5)
                ss.line(P([(lx, 0.2), (lx + sw, 0.72)]), (*FUR_D, a), max(3, s * 0.14))
        ss.poly(P(A.spline([(-0.95, 0.1), (-0.85, -0.35), (-0.3, -0.52), (0.4, -0.45), (0.8, -0.25), (0.85, 0.2), (0.4, 0.42),
                            (-0.4, 0.45), (-0.85, 0.35)], n=8)), fill=(*FUR, a), ink=(*INK, a), w=iw)
        for k in range(8):  # pelagem
            px, py = -0.7 + k * 0.18, -0.38 + 0.05 * math.sin(k)
            ss.line(P([(px, py), (px + 0.06, py + 0.1)]), (*FUR_D, a), max(1, s * 0.012))
    # cabeça (bloco com focinho rombudo)
    ss.poly(P(A.spline([(0.6, -0.42), (0.9, -0.62), (1.35, -0.58), (1.55, -0.42), (1.58, -0.12), (1.4, 0.05), (0.95, 0.08),
                        (0.65, -0.05)], n=8)), fill=(*FUR_L, a), ink=(*INK, a), w=iw)
    # orelha
    ss.oval(*P([(0.86, -0.68)])[0], s * 0.08, s * 0.06, 0.2, fill=(*FUR_D, a), ink=(*INK, a), w=iw)
    # olho (alto)
    ex, ey = P([(1.08, -0.5)])[0]; er = s * 0.055 * eye
    ss.circle(ex, ey, er, fill=(22, 16, 14, a))
    ss.circle(ex + er * 0.3 * flip, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, int(240 * a / 255)))
    # narina (no alto do focinho) e boca
    nx, ny = P([(1.5, -0.4)])[0]
    ss.oval(nx, ny, s * 0.035, s * 0.018, 0.4, fill=(*NOSE, a))
    ss.line(P([(1.48, -0.12), (1.38, -0.06)]), (*NOSE, a), max(1, s * 0.015))


def waterline_cover(img, y, col=JADE, a=215, t=0.0, amp=8):
    ss = SS(W, H, s=2)
    pts = [(x, y + amp * math.sin(x * 0.02 + t * 3)) for x in range(-20, W + 40, 20)]
    ss.poly(pts + [(W + 40, H + 20), (-20, H + 20)], fill=(*col, a))
    ss.line(pts, (*JADE_L, 230), 6)
    img.alpha_composite(ss.get())


# ======================================================================= paisagem: barragem gigante vista do rio
def dam_bg():
    def mk():
        im = A.vgrad(W, H, [(0, MIST0), (0.5, MIST1), (1, (200, 214, 214))])
        ss = SS(W, H, s=2)
        # morros
        ss.poly([(-20, 620), (200, 480), (420, 560), (-20, 900)], fill=HILL)
        ss.poly([(1100, 600), (900, 470), (700, 540), (1100, 900)], fill=HILL_D)
        # parede da barragem (contrafortes)
        ss.poly([(-20, 300), (W + 20, 300), (W + 20, 1510), (-20, 1510)], fill=CONC, ink=INK, w=6)
        ss.rect(-20, 290, W + 20, 330, CONC_D)
        for k in range(-1, 7):
            x = 90 + k * 180
            ss.poly([(x - 40, 330), (x + 40, 330), (x + 80, 1510), (x - 80, 1510)], fill=CONC_L, ink=CONC_D, w=4)
            ss.line([(x, 340), (x, 1500)], CONC_D, 3)
        # manchas de umidade
        rng = np.random.default_rng(4)
        for k in range(30):
            ss.circle(rng.uniform(0, W), rng.uniform(400, 1450), rng.uniform(8, 30), fill=(190, 176, 150, 70))
        im.alpha_composite(ss.get())
        # neblina
        mist = A.vgrad(W, H, [(0, (255, 255, 255, 0)), (0.68, (240, 244, 246, 0)), (0.77, (240, 244, 246, 150)), (0.81, (240, 244, 246, 0))])
        im.alpha_composite(mist)
        return im
    return cached("cp_dam", mk).copy()


CX, CY = 560, 1560   # capivara no gancho


def hook_frame(t, show_capy=True, ruler=True):
    img = dam_bg()
    ss = SS(W, H, s=2)
    # régua de altura
    if ruler:
        ss.line([(990, 320), (990, 1490)], (255, 255, 255), 8)
        for y in (320, 1490): ss.line([(960, y), (1020, y)], (255, 255, 255), 8)
        ss.text((975, 900), "196 m", 64, "anton", fill=(255, 255, 255), anchor="rm", stroke=7)
    img.alpha_composite(ss.get())
    # rio
    waterline_cover(img, 1510, col=JADE, a=255, t=t, amp=6)
    ss = SS(W, H, s=2)
    for k in range(10):  # reflexos
        u = (t * 0.2 + k / 10) % 1
        ss.line([(80 + k * 95, 1640 + 40 * k % 240), (140 + k * 95, 1640 + 40 * k % 240)], (*JADE_L, int(180 * math.sin(u * math.pi))), 6)
    img.alpha_composite(ss.get())
    if show_capy:
        bob = 6 * math.sin(t * 2.0)
        ss = SS(W, H, s=2)
        capy(ss, CX - 380, CY + 30 + bob, 300, t=t, eye=1.4)
        for k in range(3):  # ondinhas em volta
            r = ((t * 0.8 + k / 3) % 1)
            ss.ellipse(CX + 20, CY + 10, 140 + 260 * r, 24 + 40 * r, ink=(255, 255, 255, int(200 * (1 - r))), w=5)
        img.alpha_composite(ss.get())
        waterline_cover(img, CY + 10, col=JADE, a=200, t=t, amp=6)
    ss = SS(W, H, s=2)
    if show_capy: ss.text((CX + 260, CY + 160), "0,5 m", 50, "anton", fill=(255, 255, 255), stroke=6)
    img.alpha_composite(ss.get())
    return A.vignette(img, 0.3)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.05 + 0.012 * math.sin(lt * 0.9), dy=-6 * math.sin(lt * 0.7), rot=0.4 * math.sin(lt * 0.6))


# ======================================================================= cena 2: corte lateral, lago no alto
def section(ss, t, q=1.0, xray=False):
    """corte da barragem: lago à esquerda (alto), rio à direita (baixo)"""
    wl, wr = 760, 1500
    # lago
    ss.poly([(-20, wl + 6 * math.sin(t * 2)), (470, wl), (470, 1800), (-20, 1800)], fill=(*JADE, 230 if not xray else 120))
    # barragem
    ss.poly([(450, 620), (560, 620), (760, 1800), (420, 1800)], fill=CONC if not xray else (120, 140, 170, 120), ink=INK, w=6)
    # rio
    ss.poly([(700, wr + 4 * math.sin(t * 3)), (W + 20, wr), (W + 20, 1800), (700, 1800)], fill=(*JADE, 230 if not xray else 120))
    ss.rect(-20, 1800, W + 20, H + 20, (110, 90, 70))


def behind(ctx, lt):
    img = A.vgrad(W, H, [(0, MIST0), (1, MIST1)])
    ta = ctx.wt("alto"); tl = ctx.wt("lago")
    ss = SS(W, H, s=2)
    ss.poly([(-20, 760), (200, 620), (420, 700), (420, 1800), (-20, 1800)], fill=HILL)
    section(ss, lt)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    q = ease((lt - tl + 0.3) / 0.5)
    # lago "enchendo" a vista
    for k in range(6):
        ss.line([(30 + k * 70, 800 + k * 7), (80 + k * 70, 800 + k * 7)], (*JADE_L, 200), 6)
    # capivara pequenininha no rio
    capy(ss, 860, 1500, 40, t=lt, eye=1.2)
    # seta de altura
    aq = ease((lt - ta + 0.5) / 0.5)
    if aq > 0:
        A.arrow(ss, 330, 1480, 330, lerp(1480, 790, aq), (255, 222, 40), w=34)
        ss.rrect(60, 520, 520, 640, 30, fill=(255, 255, 255, int(235 * aq)), ink=(*INK, int(255 * aq)), w=6)
        ss.text((290, 582), "LAGO NO ALTO", 60, "anton", fill=(*JADE_D, int(255 * aq)))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ss.ellipse(860, 1500, 80 + 10 * math.sin(lt * 3), 20, ink=(255, 255, 255, 200), w=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * q, dy=20 * (1 - q))


# ======================================================================= cena 3: Visão do Bicho — periscópio
def vision(ctx, lt):
    img = A.vgrad(W, H, [(0, (150, 190, 200)), (0.55, MIST1), (0.56, JADE), (1, JADE_D)])
    to = ctx.wt("olhos"); tor = ctx.wt("orelhas"); tn = ctx.wt("narinas")
    wy = 1030
    ss = SS(W, H, s=2)
    bob = 8 * math.sin(lt * 2)
    capy(ss, -560, 1300 + bob, 900, t=lt, eye=1.2)
    img.alpha_composite(ss.get())
    waterline_cover(img, wy, col=JADE, a=170, t=lt, amp=8)
    ss = SS(W, H, s=2)
    # linha d'água tracejada passando pelos três
    for k in range(0, W, 60):
        ss.line([(k, 760 + bob), (k + 30, 760 + bob)], (255, 255, 255, 220), 6)
    P = lambda pts: A.xf(pts, -560, 1300 + bob, 900, 0, 1)
    marks = [(to, P([(1.08, -0.5)])[0], "OLHO"), (tor, P([(0.86, -0.68)])[0], "ORELHA"), (tn, P([(1.5, -0.4)])[0], "NARINA")]
    for tt, (mx, my), name in marks:
        q = ease((lt - tt + 0.15) / 0.3)
        if q <= 0: continue
        ss.circle(mx, my, 70 * A.back(q), ink=(255, 222, 40), w=10)
        ss.text((mx, my - 120), name, 46, "anton", fill=(255, 255, 255, int(255 * q)), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt))


# ======================================================================= cena 4: POV metade fora, metade dentro
def vision2(ctx, lt):
    above = hook_frame(lt + 3.0, show_capy=False, ruler=False)
    above = A.cam(above, zoom=1.25, dy=-240)
    wy = 1000 + 14 * math.sin(lt * 2.2)
    under = A.vgrad(W, H, [(0, (60, 170, 150)), (1, (14, 70, 70))])
    ss = SS(W, H, s=2)
    # raios de luz e bolhas
    for k in range(6):
        x = 100 + k * 180 + 30 * math.sin(lt + k)
        ss.poly([(x, wy), (x + 60, wy), (x + 160, H), (x + 40, H)], fill=(200, 255, 230, 40))
    for k in range(12):
        u = (lt * 0.5 + k / 12) % 1
        ss.circle(200 + k * 60, lerp(1800, wy + 40, u), 8 + k % 3 * 4, ink=(220, 255, 240, 200), w=3)
    # o próprio corpo escondido: peito e patas remando
    ss.poly(A.spline([(120, H + 40), (260, 1300), (540, 1230), (820, 1300), (960, H + 40)], n=8), fill=(*FUR_D, 200))
    for k, lx in enumerate((330, 750)):
        sw = 50 * math.sin(lt * 4 + k * 2.5)
        ss.line([(lx, 1420), (lx + sw, 1620), (lx + sw * 1.5, 1720)], (*FUR, 235), 64)
        for j in range(4):  # dedos com membrana
            ss.circle(lx + sw * 1.5 + (j - 1.5) * 26, 1760, 22, fill=(*FUR, 235))
    under.alpha_composite(ss.get())
    under = under.filter(ImageFilter.GaussianBlur(3))
    mask = Image.new("L", (W, H), 0)
    m = SS(W, H, s=1)
    pts = [(x, wy + 10 * math.sin(x * 0.015 + lt * 3)) for x in range(-20, W + 40, 20)]
    m.poly(pts + [(W + 40, H + 20), (-20, H + 20)], fill=(255, 255, 255))
    mask = m.get().split()[3]
    img = above.copy()
    img.paste(under, (0, 0), mask)
    ss = SS(W, H, s=2)
    ss.line(pts, (220, 255, 240), 8)
    # focinho e bigodes na borda (POV, logo acima da água)
    ss.poly(A.spline([(380, wy + 20), (460, wy - 90), (620, wy - 90), (700, wy + 20)], n=8), fill=FUR_L, ink=INK, w=6)
    ss.oval(490, wy - 60, 18, 9, 0.3, fill=NOSE); ss.oval(590, wy - 60, 18, 9, -0.3, fill=NOSE)
    for sg in (-1, 1):
        for k in range(3):
            ss.line([(540 + sg * 120, wy - 30 + k * 12), (540 + sg * 320, wy - 80 + k * 40)], (60, 40, 30), 4)
    img.alpha_composite(ss.get())
    return img


# ======================================================================= cena 5: raio-X — a água cai pelo tubo
def xray_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (12, 20, 38)), (1, (22, 30, 56))])
        ss = SS(W, H, s=1)
        for k in range(0, W, 60): ss.line([(k, 0), (k, H)], (60, 80, 120, 60), 2)
        for k in range(0, H, 60): ss.line([(0, k), (W, k)], (60, 80, 120, 60), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("cp_xray", mk).copy()


PEN = [(150, 560), (330, 640), (640, 1440), (820, 1520)]  # tubo: tomada d'água -> turbina


def pen_pt(u):
    segs = [math.dist(PEN[i], PEN[i + 1]) for i in range(3)]; L = sum(segs); d = u * L
    for i in range(3):
        if d <= segs[i]:
            v = d / segs[i]
            return lerp(PEN[i][0], PEN[i + 1][0], v), lerp(PEN[i][1], PEN[i + 1][1], v)
        d -= segs[i]
    return PEN[-1]


def turbine(ss, x, y, r, ang, col=(170, 190, 220)):
    ss.circle(x, y, r * 1.25, fill=(60, 70, 100), ink=INK, w=6)
    for k in range(7):
        a = ang + k * 2 * math.pi / 7
        ss.poly([(x + r * 0.25 * math.cos(a - 0.3), y + r * 0.25 * math.sin(a - 0.3)),
                 (x + r * math.cos(a + 0.25), y + r * math.sin(a + 0.25)),
                 (x + r * 0.95 * math.cos(a + 0.6), y + r * 0.95 * math.sin(a + 0.6))], fill=col, ink=INK, w=4)
    ss.circle(x, y, r * 0.25, fill=(220, 230, 240), ink=INK, w=5)


def fall(ctx, lt):
    img = xray_bg()
    tc = ctx.wt("cai"); tt = ctx.wt("tubo")
    ss = SS(W, H, s=2)
    # lago (verde) à esquerda e barragem translúcida
    ss.poly([(-20, 520), (260, 520), (260, 900), (-20, 900)], fill=(*WATERX, 110))
    ss.poly([(240, 440), (380, 440), (760, 1640), (240, 1640)], fill=(120, 140, 180, 70), ink=(160, 180, 220), w=4)
    ss.line(PEN, (150, 170, 200), 70)
    ss.line(PEN, (30, 40, 60), 50)
    q = ease((lt - tc + 0.4) / 0.4)
    for k in range(18):
        u = (lt * 0.5 + k / 18) % 1
        u2 = u ** 1.6  # acelera
        px, py = pen_pt(u2)
        ss.circle(px, py, 18, fill=(*GREEN, int(255 * (0.3 + 0.7 * q))), ink=INK, w=2)
    turbine(ss, 870, 1530, 110, lt * 6)
    # régua de 100 m
    rq = ease((lt - tt + 0.8) / 0.5)
    ss.line([(960, 640), (960, lerp(640, 1440, rq))], (255, 222, 40), 8)
    ss.text((940, 1000), "100 m", 60, "anton", fill=(255, 255, 255, int(255 * rq)), anchor="rm", stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * q)


# ======================================================================= cena 6: uma piscina olímpica a cada 4 s
def pool(ctx, lt):
    img = xray_bg()
    tp = ctx.wt("piscina"); ts = ctx.wt("segundos")
    ss = SS(W, H, s=2)
    q = ease((lt - tp + 0.3) / 0.4)
    # piscina em perspectiva, esvaziando num ciclo de ~4 s (acelerado para caber)
    cyc = ((lt - tp) % 2.2) / 2.2 if lt > tp else 0.0
    lvl = 1 - cyc
    x0, x1, y0, y1 = 140, 940, 560, 960
    ss.poly([(x0 + 80, y0), (x1 - 80, y0), (x1, y1), (x0, y1)], fill=(230, 240, 250, int(240 * q)), ink=(*INK, int(255 * q)), w=6)
    wy0 = lerp(y1, y0 + 20, lvl)
    ss.poly([(lerp(x0, x0 + 80, (y1 - wy0) / (y1 - y0)) + 6, wy0), (lerp(x1, x1 - 80, (y1 - wy0) / (y1 - y0)) - 6, wy0), (x1 - 8, y1 - 6),
             (x0 + 8, y1 - 6)], fill=(60, 170, 230, int(230 * q)))
    for k in range(1, 8):
        u = k / 8
        ss.line([(lerp(x0 + 80, x0, 0) + u * (x1 - x0 - 160), y0 + 4), (x0 + u * (x1 - x0), y1 - 4)], (255, 255, 255, int(150 * q)), 4)
    ss.text((540, y0 - 50), "PISCINA OLÍMPICA · 2.500 m³", 44, "anton", fill=(255, 255, 255, int(255 * q)), stroke=5)
    # funil de água descendo para a turbina
    for k in range(16):
        u = (lt * 1.2 + k / 16) % 1
        ss.circle(540 + 60 * math.sin(k * 2.3) * (1 - u), lerp(y1, 1440, u), 14, fill=(*GREEN, int(230 * q)))
    turbine(ss, 540, 1560, 150, lt * 7)
    # relógio de 4 s
    cq = ease((lt - ts + 0.6) / 0.4)
    ss.circle(900, 1560, 100, fill=(240, 244, 250, int(240 * cq)), ink=(*INK, int(255 * cq)), w=6)
    a = -math.pi / 2 + cyc * 2 * math.pi
    ss.line([(900, 1560), (900 + 80 * math.cos(a), 1560 + 80 * math.sin(a))], (*INK, int(255 * cq)), 8)
    ss.text((900, 1700), "4 s", 54, "anton", fill=(255, 255, 255, int(255 * cq)), stroke=5)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.8))


# ======================================================================= cena 7: gerador — ímã dentro do cobre
def generator(ss, cx, cy, R, ang, q=1.0, glow=0.0):
    # estator: bobinas de cobre
    ss.circle(cx, cy, R * 1.32, fill=(70, 80, 110), ink=INK, w=6)
    for k in range(16):
        a = k * 2 * math.pi / 16
        bx, by = cx + R * 1.12 * math.cos(a), cy + R * 1.12 * math.sin(a)
        col = A.mixc(COPPER, (255, 230, 120), glow * (0.5 + 0.5 * math.sin(ang * 4 + k)))
        ss.oval(bx, by, R * 0.16, R * 0.1, a, fill=col, ink=INK, w=4)
        for j in range(3):
            ss.line([(bx + R * (j - 1) * 0.06 * math.cos(a + 1.57) - R * 0.1 * math.cos(a), by + R * (j - 1) * 0.06 * math.sin(a + 1.57) - R * 0.1 * math.sin(a)),
                     (bx + R * (j - 1) * 0.06 * math.cos(a + 1.57) + R * 0.1 * math.cos(a), by + R * (j - 1) * 0.06 * math.sin(a + 1.57) + R * 0.1 * math.sin(a))],
                    (150, 70, 30), 3)
    # rotor: ímãs N/S
    ss.circle(cx, cy, R * 0.92, fill=(40, 46, 64), ink=INK, w=5)
    for k in range(8):
        a = ang + k * 2 * math.pi / 8
        col = (230, 232, 240) if k % 2 == 0 else (150, 156, 170)
        px, py = cx + R * 0.66 * math.cos(a), cy + R * 0.66 * math.sin(a)
        ss.oval(px, py, R * 0.22, R * 0.15, a, fill=col, ink=INK, w=4)
        ss.text((px, py), "N" if k % 2 == 0 else "S", int(R * 0.16), "anton", fill=INK)
    ss.circle(cx, cy, R * 0.2, fill=(200, 210, 220), ink=INK, w=5)


def magnet(ctx, lt):
    img = xray_bg()
    ti = ctx.wt("ímã"); tc = ctx.wt("cobre")
    ang = lt * 1.4
    ss = SS(W, H, s=2)
    # eixo descendo até a turbina
    ss.rect(515, 900, 565, 1560, (170, 180, 200))
    turbine(ss, 540, 1600, 130, lt * 1.4)
    for k in range(10):
        u = (lt * 1.0 + k / 10) % 1
        ss.circle(lerp(80, 400, u), 1600 + 20 * math.sin(u * 7), 14, fill=GREEN)
    generator(ss, 540, 760, 260, ang, glow=ease((lt - tc + 0.3) / 0.4))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    q = ease((lt - ti + 0.2) / 0.4)
    for k in range(3):  # setas de giro
        a = ang + k * 2.1
        A.arrow(ss, 540 + 150 * math.cos(a), 760 + 150 * math.sin(a), 540 + 150 * math.cos(a + 0.6), 760 + 150 * math.sin(a + 0.6),
                (255, 255, 255, int(220 * q)), w=14)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * q)


# ======================================================================= cena 8: elétrons — eletricidade
def electrons(ctx, lt):
    img = xray_bg()
    te = ctx.wt("elétrons"); tl = ctx.wt("eletricidade")
    q = ease((lt - te + 0.3) / 0.4); lq = ease((lt - tl + 0.2) / 0.4)
    ss = SS(W, H, s=2)
    # fio de cobre grosso em zigue-zague (bobina ampliada)
    path = [(-20, 640), (300, 640), (300, 820), (780, 820), (780, 640), (1100, 640)]
    ss.line(path, COPPER, 60)
    ss.line(path, (240, 160, 100), 20)
    # ímã passando por baixo
    mx = 540 + 300 * math.sin(lt * 2.2)
    ss.rrect(mx - 110, 930, mx + 110, 1040, 20, fill=(230, 232, 240), ink=INK, w=5)
    ss.text((mx - 55, 985), "N", 60, "anton", fill=INK); ss.text((mx + 55, 985), "S", 60, "anton", fill=INK)
    # elétrons amarelos empurrados ao longo do fio
    segs = [math.dist(path[i], path[i + 1]) for i in range(len(path) - 1)]; L = sum(segs)
    for k in range(18):
        d = ((lt * 0.35 * (0.3 + 0.7 * q) + k / 18) % 1) * L
        for i in range(len(segs)):
            if d <= segs[i]:
                v = d / segs[i]; x = lerp(path[i][0], path[i + 1][0], v); y = lerp(path[i][1], path[i + 1][1], v); break
            d -= segs[i]
        ss.circle(x, y, 16, fill=YEL, ink=INK, w=3)
    # casas acendendo lá embaixo
    for k in range(5):
        hx = 120 + k * 200; hy = 1560
        lit = lq * clamp01((lt - tl + 0.2 - k * 0.08) / 0.2)
        ss.poly([(hx - 80, hy), (hx, hy - 80), (hx + 80, hy)], fill=(150, 80, 70), ink=INK, w=4)
        ss.rect(hx - 70, hy, hx + 70, hy + 140, (200, 190, 170))
        ss.rect(hx - 30, hy + 30, hx + 30, hy + 90, A.mixc((50, 60, 80), (255, 230, 120), lit))
    ss.line([(1060, 640), (1060, 1420), (40, 1420)], (90, 100, 120), 8)
    img.alpha_composite(ss.get())
    for k in range(5):
        glow_at(img, 120 + k * 200, 1620, 130, (255, 220, 100), 150 * lq * clamp01((lt - tl + 0.2 - k * 0.08) / 0.2))
    return A.cam(img, zoom=1.0 + 0.03 * q)


# ======================================================================= cena 9: mais da metade vem da água
def brasil(ctx, lt):
    img = A.vgrad(W, H, [(0, (232, 240, 238)), (1, (200, 222, 216))])
    tm = ctx.wt("metade"); ta = ctx.wt("água")
    lvl = 0.55 * ease((lt - tm + 0.4) / max(0.6, ta - tm + 0.4))
    cx, cy, r = 540, 860, 300
    ss = SS(W, H, s=2)
    # lâmpada gigante
    bulb = A.spline([(cx - 0.45 * r, cy + 0.9 * r), (cx - 1.0 * r, cy), (cx - 0.7 * r, cy - 0.85 * r), (cx, cy - 1.05 * r),
                     (cx + 0.7 * r, cy - 0.85 * r), (cx + 1.0 * r, cy), (cx + 0.45 * r, cy + 0.9 * r)], n=10)
    ss.poly(bulb, fill=(250, 252, 255), ink=INK, w=8)
    img.alpha_composite(ss.get())
    # água dentro da lâmpada (máscara)
    wat = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ws = SS(W, H, s=2)
    top = cy + 0.95 * r - lvl * 2.0 * r
    pts = [(x, top + 12 * math.sin(x * 0.03 + lt * 4)) for x in range(cx - r - 20, cx + r + 40, 20)]
    ws.poly(pts + [(cx + r + 40, cy + r + 40), (cx - r - 20, cy + r + 40)], fill=(*JADE, 255))
    wat.alpha_composite(ws.get())
    ms = SS(W, H, s=2); ms.poly(bulb, fill=(255, 255, 255))
    mask = ms.get().split()[3]
    inner = Image.new("RGBA", (W, H), (0, 0, 0, 0)); inner.paste(wat, (0, 0), mask)
    img.alpha_composite(inner)
    ss = SS(W, H, s=2)
    ss.poly(bulb, ink=INK, w=8)
    # rosca
    ss.rrect(cx - 0.45 * r, cy + 0.9 * r, cx + 0.45 * r, cy + 1.35 * r, 20, fill=(170, 170, 180), ink=INK, w=6)
    for j in range(3): ss.line([(cx - 0.45 * r, cy + r * (1.0 + j * 0.12)), (cx + 0.45 * r, cy + r * (1.04 + j * 0.12))], (120, 120, 130), 5)
    # marca de 50%
    ss.line([(cx - r - 40, cy - 0.05 * r), (cx + r + 40, cy - 0.05 * r)], (230, 60, 60), 6)
    ss.text((cx + r + 30, cy - 0.05 * r - 40), "50%", 50, "anton", fill=(230, 60, 60), anchor="rm")
    # capivara pequena olhando (no chão, na grama)
    capy(ss, 220, 1640, 90, t=lt, eye=1.3)
    ss.text((760, 1640), "BRASIL", 80, "anton", fill=(30, 120, 80), stroke=0)
    img.alpha_composite(ss.get())
    glow_at(img, cx, cy - 0.2 * r, 420, (255, 250, 200), 120 * lvl / 0.55)
    return A.cam(img, zoom=1.02 + 0.03 * lvl)


# ======================================================================= cena 10: loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    u = easeio(clamp01(lt / max(0.6, ctx.dur * 0.6)))
    img = hook_frame(tr)
    ss = SS(W, H, s=2)
    for k in range(10):  # água saindo pelo pé da barragem
        v = (lt * 0.8 + k / 10) % 1
        ss.circle(200 + k * 70, 1520 + 40 * v, 10, fill=(255, 255, 255, int(200 * (1 - u) * (1 - v))))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=lerp(1.14, 1.05 + 0.012 * math.sin(tr * 0.9), u), dy=-6 * math.sin(tr * 0.7) * u,
                 rot=0.4 * math.sin(tr * 0.6) * u)


# ======================================================================= capa
def cover_bg(cv):
    img = hook_frame(0.0, show_capy=False, ruler=False)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 700) * 0.42
    ss = SS(int(2.9 * s), int(2.0 * s), s=2)
    capy(ss, 1.05 * s, 1.0 * s, s, t=0.3, eye=2.0)
    return ss.get()
