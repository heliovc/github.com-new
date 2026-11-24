"""Dia 5B — "E se você fosse um cachorro no banco de trás do carro?" (formato ATUAL; paleta: céu de meio-dia,
carro amarelo-mostarda em corte, estofado azul-petróleo, cachorro caramelo de peitoral vermelho; motor em raio-X:
verde = ar, âmbar = gasolina, vermelho/laranja = fogo, amarelo = faísca, cinza = fumaça).

Cenas: hook (corte lateral do carro: o cachorro no banco de trás de peitoral e cinto, o capô em raio-X com 4 cilindros
piscando), xray (zoom no bloco do motor), tempos (os 4 tempos lado a lado), intake (pistão desce e puxa ar +
gasolina), compress (sobe e espreme 10×), spark (a vela solta a faísca: explode), power (empurra o pistão, gira o
virabrequim e a roda), vision (Visão do Bicho: o ouvido do cachorro, faixa até 45 mil × 20 mil), exhaust (sobe e
expulsa a fumaça), rpm (conta-giros em 2 mil: 17 explosões por segundo), loop (os 4 juntos, ~70/s; volta ao quadro
inicial). Cachorro sempre de peitoral preso ao cinto (sem cabeça para fora da janela).
Fatos: U.S. DOE (ciclo de 4 tempos); Heffner (1983).
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

FUR = (214, 150, 80); FUR_D = (150, 92, 46); FUR_L = (246, 214, 170); EAR = (120, 70, 36)
HARN = (220, 50, 60)
CAR = (236, 182, 52); CAR_D = (178, 126, 24); CAR_L = (255, 222, 120)
SEAT = (40, 92, 112); SEAT_D = (24, 60, 76)
GLASS = (190, 226, 245)
AIR = (80, 230, 150); FUEL = (255, 176, 40); FIRE = (255, 80, 40); SPARK = (255, 240, 60); SMOKE = (150, 150, 160)
STEEL = (196, 204, 214); STEEL_D = (110, 118, 132)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= cachorro sentado (perfil, olhando para a direita)
def dog(ss, x, y, s, t=0.0, eye=1.0, sleep=0.0, ear=0.0, harness=True, pant=0.0):
    """origem = centro do corpo; assento em y + 0.42 s. sleep: 0 aberto, 1 olho fechado. ear: 0 caída, 1 erguida."""
    P = lambda pts: A.xf(pts, x, y, s)
    iw = max(1.5, s * 0.008)
    br = 0.01 * math.sin(t * 2.2)
    # rabo
    tl = A.bez((-0.3, 0.32), (-0.55, 0.36), (-0.62, 0.22 + 0.04 * math.sin(t * 5)), (-0.7, 0.12 + 0.06 * math.sin(t * 5)), 14)
    ss.line(P(tl), (*INK, 255), max(4, s * 0.075)); ss.line(P(tl), FUR, max(3, s * 0.055))
    # corpo
    body = A.spline([(-0.32, 0.4), (-0.38, 0.1), (-0.26, -0.18 - br), (0.02, -0.26 - br), (0.2, -0.16), (0.24, 0.15),
                     (0.16, 0.42)], 8)
    ss.poly(P(body), fill=FUR, ink=INK, w=iw)
    ss.poly(P(A.spline([(0.08, -0.12), (0.2, -0.08), (0.2, 0.2), (0.1, 0.28), (0.04, 0.05)], 6)), fill=FUR_L)
    # coxa de trás
    ss.poly(P(A.ell_pts(-0.17, 0.26, 0.21, 0.17, -10, 26)), fill=FUR, ink=INK, w=iw)
    ss.poly(P(A.ell_pts(-0.02, 0.4, 0.12, 0.04, 0, 16)), fill=FUR_D, ink=INK, w=iw * 0.8)
    # pata da frente
    ss.poly(P([(0.08, 0.02), (0.2, 0.02), (0.21, 0.4), (0.07, 0.4)]), fill=FUR, ink=INK, w=iw)
    ss.poly(P(A.ell_pts(0.17, 0.41, 0.09, 0.035, 0, 14)), fill=FUR_L, ink=INK, w=iw * 0.8)
    # peitoral
    if harness:
        ss.poly(P([(-0.06, -0.2), (0.04, -0.24), (0.22, 0.08), (0.14, 0.12)]), fill=HARN, ink=INK, w=iw)
        ss.poly(P([(-0.2, -0.1), (-0.1, -0.16), (0.0, 0.2), (-0.1, 0.24)]), fill=HARN, ink=INK, w=iw)
        ss.circle(*P([(-0.08, -0.17)])[0], s * 0.03, fill=(200, 200, 210), ink=INK, w=iw * 0.7)
    # pescoço
    ss.poly(P(A.spline([(-0.04, -0.2), (0.04, -0.42), (0.26, -0.44), (0.24, -0.1), (0.12, -0.08)], 6)), fill=FUR, ink=INK, w=iw)
    if harness:
        ss.poly(P([(0.0, -0.3), (0.06, -0.33), (0.2, -0.1), (0.14, -0.08)]), fill=HARN, ink=INK, w=iw)
    # cabeça
    hx, hy = 0.2, -0.44
    HP = lambda pts: P([(hx + px, hy + py) for px, py in pts])
    ss.poly(HP(A.spline([(-0.16, 0.02), (-0.12, -0.16), (0.04, -0.2), (0.16, -0.12), (0.3, -0.04), (0.33, 0.06),
                         (0.24, 0.12), (0.06, 0.16), (-0.12, 0.14)], 8)), fill=FUR, ink=INK, w=iw)
    ss.poly(HP(A.spline([(0.14, 0.0), (0.3, -0.02), (0.32, 0.07), (0.2, 0.12), (0.1, 0.1)], 6)), fill=FUR_L)
    # nariz e boca
    ss.circle(*HP([(0.315, -0.02)])[0], s * 0.032, fill=(30, 22, 26), ink=INK, w=iw * 0.6)
    ss.line(HP(A.bez((0.31, 0.04), (0.28, 0.09), (0.22, 0.1), (0.17, 0.08), 6)), INK, max(1.5, s * 0.008))
    if pant > 0.02:
        ss.poly(HP(A.ell_pts(0.22, 0.12 + 0.02 * pant, 0.04, 0.05 * pant, 10, 14)), fill=(240, 110, 130), ink=INK, w=iw * 0.6)
    # olho
    ex, ey = HP([(0.1, -0.06)])[0]; er = s * 0.036 * eye
    if sleep > 0.6:
        ss.line([(ex - er, ey), (ex - er * 0.3, ey + er * 0.45), (ex + er * 0.4, ey + er * 0.45), (ex + er, ey)], INK, max(2, s * 0.01))
    else:
        ss.circle(ex, ey, er, fill=(30, 18, 14), ink=INK, w=iw * 0.6)
        ss.circle(ex - er * 0.3, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, 240))
        ss.circle(ex + er * 0.32, ey + er * 0.3, er * 0.14, fill=(255, 255, 255, 170))
        if sleep > 0.02:  # pálpebra descendo
            ss.poly([(ex - er * 1.2, ey - er * 1.3), (ex + er * 1.2, ey - er * 1.3), (ex + er * 1.2, ey - er * 1.3 + 2.3 * er * sleep / 0.6),
                     (ex - er * 1.2, ey - er * 1.3 + 2.3 * er * sleep / 0.6)], fill=FUR)
    ss.line(HP(A.bez((0.04, -0.13), (0.08, -0.16), (0.13, -0.15), (0.16, -0.12), 5)), FUR_D, max(2, s * 0.012))
    # orelha caída (ou erguida, ouvindo)
    e = clamp01(ear)
    tip = (lerp(-0.1, -0.02, e), lerp(0.18, -0.34, e))
    ear_pts = [(-0.04, -0.16), (-0.12, -0.14), (lerp(-0.18, -0.12, e), lerp(0.0, -0.26, e)), tip,
               (lerp(-0.02, 0.04, e), lerp(0.08, -0.26, e)), (0.02, -0.12)]
    ss.poly(HP(A.spline(ear_pts, 6)), fill=EAR, ink=INK, w=iw)


# ======================================================================= peças do motor
def cyl_state(phi):
    """phi em graus (0..720) -> (posição do pistão 0 = em cima .. 1 = embaixo, tempo 0..3)"""
    phi %= 720
    pos = 0.5 - 0.5 * math.cos(math.radians(phi))
    return pos, int(phi // 180)


def cylinder(ss, cx, top, w, h, phi, t=0.0, big=False, a=255, show_valves=True, flash_boost=1.0):
    """um cilindro em corte: paredes, pistão, biela, válvulas, vela e o conteúdo colorido pelo tempo."""
    pos, st = cyl_state(phi)
    u = (phi % 180) / 180
    ch = h * 0.62                       # curso livre
    py = top + 0.12 * h + ch * pos      # topo do pistão
    iw = 6 if big else 4
    # conteúdo da câmara
    cx0, cx1 = cx - w / 2 + iw, cx + w / 2 - iw
    if st == 0:
        col = (*AIR, int(150 * a / 255))
    elif st == 1:
        col = (*A.mixc(AIR, FUEL, 0.35 + 0.4 * u), int((150 + 80 * u) * a / 255))
    elif st == 2:
        col = (*A.mixc(SPARK, FIRE, clamp01(u * 3)), int(lerp(250, 140, u) * a / 255))
    else:
        col = (*SMOKE, int(lerp(200, 80, u) * a / 255))
    ss.rect(cx0, top + 4, cx1, py, col)
    if st in (0, 1):  # gotinhas de gasolina
        rng = np.random.default_rng(int(cx) + 7)
        for k in range(10 if big else 5):
            gx = rng.uniform(cx0 + 10, cx1 - 10)
            gy = lerp(top + 10, py - 10, (rng.uniform(0, 1) + t * 0.8 * (1 if st == 0 else 0)) % 1.0)
            ss.circle(gx, gy, (9 if big else 4) * (1 - 0.4 * u * (st == 1)), fill=(*FUEL, a), ink=(*INK, a), w=2)
    if st == 2 and u < 0.35:
        f = (1 - u / 0.35) * flash_boost
        g = A.glow(int(w * 0.9), FIRE, int(200 * f * a / 255))
        ss.paste(g.resize((g.width * ss.s, g.height * ss.s)), cx - g.width / 2, top + 0.1 * h - g.height / 2)
    # paredes
    ss.rrect(cx - w / 2 - iw, top - 4, cx + w / 2 + iw, top + h, 10, ink=(*STEEL_D, a), w=iw * 2)
    # pistão e biela
    ss.rrect(cx - w / 2 + iw + 2, py, cx + w / 2 - iw - 2, py + h * 0.2, 8, fill=(*STEEL, a), ink=(*INK, a), w=iw * 0.8)
    for k in range(2):
        ss.line([(cx - w / 2 + iw + 2, py + 14 + k * 14), (cx + w / 2 - iw - 2, py + 14 + k * 14)], (*STEEL_D, a), 3)
    cr = h * 0.31 * 0.5 * 2 * 0.5 * 2   # raio da manivela = metade do curso
    cr = ch * 0.5
    ccy = top + h + cr * 0.3 + h * 0.3
    ang = math.radians(phi)
    pinx, piny = cx + cr * math.sin(ang), ccy - cr * math.cos(ang)
    ss.line([(cx, py + h * 0.12), (pinx, piny)], (*INK, a), iw * 3.2)
    ss.line([(cx, py + h * 0.12), (pinx, piny)], (*STEEL, a), iw * 2.2)
    ss.circle(cx, ccy, cr * 1.05, ink=(*STEEL_D, int(a * 0.6)), w=iw)
    ss.circle(pinx, piny, iw * 2, fill=(*STEEL_D, a), ink=(*INK, a), w=3)
    # válvulas (esquerda = admissão, direita = escape) e vela no meio
    if show_valves:
        vo_in = 1.0 if st == 0 else 0.0
        vo_ex = 1.0 if st == 3 else 0.0
        for sg, vo in ((-1, vo_in), (1, vo_ex)):
            vx = cx + sg * w * 0.28; vy = top + 4 + vo * h * 0.06
            ss.line([(vx, vy - h * 0.22), (vx, vy)], (*INK, a), iw * 2.2)
            ss.line([(vx, vy - h * 0.22), (vx, vy)], (*STEEL, a), iw * 1.2)
            ss.ellipse(vx, vy, w * 0.13, iw * 1.6, fill=(*STEEL, a), ink=(*INK, a), w=3)
            # duto
            dx = cx + sg * w * 0.62
            dcol = AIR if sg < 0 else SMOKE
            ss.line([(vx, top - h * 0.04), (dx, top - h * 0.14)], (*INK, a), iw * 5.2)
            ss.line([(vx, top - h * 0.04), (dx, top - h * 0.14)], (*dcol, int(a * (0.5 + 0.5 * vo))), iw * 4)
        ss.rrect(cx - w * 0.05, top - h * 0.2, cx + w * 0.05, top + 6, 4, fill=(230, 230, 236, a), ink=(*INK, a), w=3)
        if st == 1 and u > 0.9 or st == 2 and u < 0.06:
            for k in range(6):
                aa = k / 6 * 2 * math.pi + t * 30
                r1 = w * 0.16
                ss.line([(cx, top + 10), (cx + r1 * math.cos(aa), top + 10 + r1 * math.sin(aa))], (*SPARK, a), iw * 1.4)
    return py


def engine_row(ss, x0, top, w, h, gap, theta, t, a=255, boost=1.0):
    """4 cilindros, ordem de ignição 1-3-4-2"""
    offs = [0, 540, 180, 360]
    for k in range(4):
        cylinder(ss, x0 + k * (w + gap), top, w, h, theta + offs[k], t=t, a=a, show_valves=w > 60, flash_boost=boost)


# ======================================================================= o carro em corte
def scenery(img, t, speed=420.0, y_ground=1560):
    ss = SS(W, H, s=1)
    off = (t * speed * 0.25) % 700
    for k in range(-1, 4):  # prédios distantes
        bx = k * 700 - off
        for j, (dx, hh, c) in enumerate(((0, 420, (170, 196, 220)), (220, 560, (150, 180, 210)), (430, 360, (186, 206, 226)))):
            ss.rect(bx + dx, y_ground - 500 - hh, bx + dx + 190, y_ground, c)
    off = (t * speed) % 380
    for k in range(-1, 5):  # árvores próximas
        tx = k * 380 - off
        ss.rect(tx + 70, y_ground - 520, tx + 96, y_ground, (110, 80, 50))
        ss.circle(tx + 83, y_ground - 600, 140, fill=(70, 150, 80))
        ss.circle(tx + 20, y_ground - 520, 90, fill=(90, 170, 90))
    img.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(4)))


def sky_road(t):
    img = cached("sky", lambda: A.vgrad(W, H, [(0, (110, 180, 250)), (0.55, (200, 232, 255)), (0.8, (220, 230, 236)), (1, (120, 124, 130))])).copy()
    scenery(img, t)
    ss = SS(W, H, s=1)
    ss.rect(0, 1560, W, H, (96, 100, 108))
    off = (t * 900) % 260
    for k in range(-1, 6):
        ss.rect(k * 260 - off, 1840, k * 260 - off + 140, 1860, (240, 240, 230))
    img.alpha_composite(ss.get())
    return img


def wheel(ss, cx, cy, r, ang):
    ss.circle(cx, cy, r, fill=(36, 36, 42), ink=INK, w=6)
    ss.circle(cx, cy, r * 0.58, fill=(190, 196, 206), ink=INK, w=5)
    for k in range(5):
        a = ang + k * 2 * math.pi / 5
        ss.line([(cx, cy), (cx + r * 0.5 * math.cos(a), cy + r * 0.5 * math.sin(a))], (120, 126, 138), 14)
    ss.circle(cx, cy, r * 0.14, fill=(90, 94, 104), ink=INK, w=4)


def car_frame(t, sleep=0.0, eng_a=1.0, theta=None, ear=0.0, boost=1.0):
    img = sky_road(t)
    bob = 4 * math.sin(t * 9) + 2 * math.sin(t * 23)
    ss = SS(W, H, s=2)
    oy = bob
    # carroceria (corte: só o contorno + painel inferior)
    shell = [(-60, 1560 + oy), (-60, 1020 + oy), (60, 760 + oy), (640, 740 + oy), (830, 1030 + oy), (1090, 1090 + oy),
             (1120, 1580 + oy)]
    ss.poly(shell, fill=(*GLASS, 90), ink=INK, w=8)
    ss.poly([(-60, 1360 + oy), (1120, 1360 + oy), (1120, 1600 + oy), (-60, 1600 + oy)], fill=CAR, ink=INK, w=8)
    ss.line([(-60, 1440 + oy), (1120, 1440 + oy)], CAR_D, 6)
    ss.line([(-60, 1040 + oy), (830, 1040 + oy)], (*CAR_D, 255), 10)
    ss.line([(560, 760 + oy), (560, 1360 + oy)], (*CAR_D, 255), 14)  # coluna B
    # banco de trás
    ss.rrect(40, 1000 + oy, 150, 1400 + oy, 40, fill=SEAT, ink=INK, w=6)
    ss.rrect(60, 1320 + oy, 520, 1420 + oy, 34, fill=SEAT, ink=INK, w=6)
    ss.line([(150, 1350 + oy), (500, 1350 + oy)], SEAT_D, 5)
    # banco da frente (encosto)
    ss.rrect(600, 1040 + oy, 690, 1380 + oy, 36, fill=SEAT, ink=INK, w=6)
    ss.rrect(615, 975 + oy, 675, 1040 + oy, 22, fill=SEAT, ink=INK, w=5)
    img.alpha_composite(ss.get())
    # cachorro no banco de trás, preso ao cinto pelo peitoral
    ss = SS(W, H, s=2)
    dx, dy, ds = 300, 1168 + oy, 380
    dog(ss, dx, dy, ds, t=t, sleep=sleep, ear=ear, pant=0.6 * (1 - sleep))
    bx, by = A.xf([(-0.08, -0.17)], dx, dy, ds)[0]
    ss.line(A.bez((110, 1060 + oy), (160, 1150 + oy), (bx - 60, by + 40), (bx, by), 10), (*INK, 255), 14)
    ss.line(A.bez((110, 1060 + oy), (160, 1150 + oy), (bx - 60, by + 40), (bx, by), 10), (70, 70, 80), 8)
    img.alpha_composite(ss.get())
    # capô em raio-X com o motor
    ss = SS(W, H, s=2)
    ss.rrect(760, 1130 + oy, 1080, 1440 + oy, 20, fill=(20, 40, 70, int(190 * eng_a)), ink=(*INK, int(255 * eng_a)), w=5)
    th = t * 720 * 2.2 if theta is None else theta
    engine_row(ss, 785, 1190 + oy, 50, 120, 22, th, t, a=int(255 * eng_a), boost=boost)
    wheel(ss, 230, 1600 + oy, 130, t * 9)
    wheel(ss, 900, 1600 + oy, 130, t * 9)
    img.alpha_composite(ss.get())
    return A.vignette(img, 0.3)


# ======================================================================= cena 1: gancho
def hook(ctx, lt):
    te = ctx.wt("explosões")
    pop = math.exp(-max(0, lt - te) * 3) if lt >= te else 0
    img = car_frame(lt, boost=1.0 + 1.5 * pop)
    return A.cam(img, zoom=HZ + 0.03 * pop, dx=6 * pop * math.sin(lt * 50), rot=0.3 * math.sin(lt * 0.8), cx=HCX, cy=HCY)


HZ, HCX, HCY = 1.2, 1000, 1200


# ======================================================================= cena 2: zoom no bloco do motor
def blueprint():
    def mk():
        im = A.vgrad(W, H, [(0, (16, 34, 64)), (1, (8, 16, 36))])
        ss = SS(W, H, s=1)
        for k in range(0, H, 54): ss.line([(0, k), (W, k)], (80, 140, 220, 40), 2)
        for k in range(0, W, 54): ss.line([(k, 0), (k, H)], (80, 140, 220, 40), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("bp", mk).copy()


def xray(ctx, lt):
    img = blueprint()
    tm = ctx.wt("metal")
    zin = ease(lt / 0.8)
    ss = SS(W, H, s=2)
    engine_row(ss, 195, 1330, 150, 300, 80, lt * 720 * 1.2, lt)
    ss.rrect(80, 1260, 1000, 1860, 30, ink=(120, 170, 240), w=6)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    q = ease((lt - tm + 0.3) / 0.5)
    ss.text((540, 760), "BLOCO DO MOTOR", 76, "anton", fill=(170, 210, 255), stroke=8)
    ss.text((540, 860), "4 cilindros de metal", 46, "mont-ExtraBold", fill=(255, 255, 255, int(255 * q)), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=lerp(1.25, 1.0, zin), dy=lerp(-160, 0, zin))


# ======================================================================= cena 3: os 4 tempos
NAMES = ["PUXA", "ESPREME", "EXPLODE", "SOLTA"]


def tempos(ctx, lt):
    img = blueprint()
    tq = ctx.wt("quatro")
    ss = SS(W, H, s=2)
    for k in range(4):
        cx = 150 + k * 260
        phi = k * 180 + 90 + 30 * math.sin(lt * 2)
        q = ease((lt - tq + 0.6 - k * 0.15) / 0.4)
        cylinder(ss, cx, 1330, 170, 300, phi, t=lt, a=int(110 + 145 * q))
        ss.circle(cx, 900, 56, fill=(255, 222, 40, int(255 * q)), ink=(*INK, int(255 * q)), w=5)
        ss.text((cx, 900), str(k + 1), 64, "anton", fill=(*INK, int(255 * q)))
        ss.text((cx, 1840), NAMES[k], 44, "anton", fill=(255, 255, 255, int(255 * q)), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cenas 4-7, 9: um cilindro grande
def big_cyl(img, phi, lt, labels=None):
    ss = SS(W, H, s=2)
    py = cylinder(ss, 540, 660, 440, 760, phi, t=lt, big=True)
    img.alpha_composite(ss.get())
    return py


def intake(ctx, lt):
    img = blueprint()
    td = ctx.wt("desce"); tg = ctx.wt("gasolina")
    u = easeio(clamp01((lt - td + 0.2) / max(0.8, tg - td + 0.6)))
    phi = lerp(5, 178, u)
    big_cyl(img, phi, lt)
    ss = SS(W, H, s=2)
    for k in range(3):  # ar entrando pelo duto (verde)
        uu = (lt * 1.2 + k / 3) % 1.0
        A.arrow(ss, 140 + 120 * uu, 470 + 40 * uu, 220 + 120 * uu, 520 + 40 * uu, (*AIR, int(255 * u * (1 - uu))), w=28, iw=3)
    ss.text((150, 420), "AR", 60, "anton", fill=AIR, stroke=7)
    qg = ease((lt - tg + 0.3) / 0.5)
    ss.text((150, 610), "+ gasolina", 40, "mont-ExtraBold", fill=(*FUEL, int(255 * qg)), anchor="mm", stroke=5)
    A.arrow(ss, 920, 1500, 920, 1720, (255, 255, 255, int(255 * (u < 0.98))), w=34, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * u)


def compress(ctx, lt):
    img = blueprint()
    ts = ctx.wt("sobe"); tm = ctx.wt("menor")
    u = easeio(clamp01((lt - ts + 0.1) / max(0.8, tm - ts + 0.4)))
    phi = lerp(182, 352, u)
    big_cyl(img, phi, lt)
    ss = SS(W, H, s=2)
    A.arrow(ss, 920, 1720, 920, 1500, (255, 255, 255, int(255 * (u < 0.98))), w=34, iw=4)
    q = ease((lt - tm + 0.2) / 0.4)
    ss.text((900, 820), "10×", 110, "anton", fill=(255, 222, 40, int(255 * q)), stroke=9)
    ss.text((900, 920), "menor", 50, "anton", fill=(255, 255, 255, int(255 * q)), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.06 * u, dx=3 * u * math.sin(lt * 40))


def spark(ctx, lt):
    img = blueprint()
    tv = ctx.wt("vela"); te = ctx.wt("explode")
    if lt < te:
        phi = lerp(352, 359.5, clamp01((lt - tv) / max(0.3, te - tv)))
    else:
        phi = 360 + 50 * ease((lt - te) / 1.5)
    big_cyl(img, phi, lt)
    ss = SS(W, H, s=2)
    fv = ease((lt - tv + 0.1) / 0.3) * (1 if lt < te + 0.3 else 0)
    if fv > 0:
        for k in range(10):
            a = k / 10 * 2 * math.pi + lt * 20
            r1 = 70 + 30 * math.sin(lt * 40 + k)
            ss.line([(540, 680), (540 + r1 * math.cos(a), 680 + r1 * math.sin(a))], (*SPARK, int(255 * fv)), 12)
        ss.text((780, 470), "VELA", 56, "anton", fill=(*SPARK, int(255 * fv)), stroke=7)
        A.arrow(ss, 720, 500, 580, 560, (*SPARK, int(255 * fv)), w=20, iw=3)
    img.alpha_composite(ss.get())
    if lt >= te:
        f = math.exp(-(lt - te) * 2.5)
        A.paste_c(img, A.glow(700, FIRE, int(220 * f)), 540, 760)
        img.alpha_composite(Image.new("RGBA", (W, H), (255, 220, 160, int(120 * math.exp(-(lt - te) * 8)))))
    sh = math.exp(-max(0, lt - te) * 5) if lt >= te else 0
    return A.cam(img, zoom=1.02 + 0.06 * sh, dx=16 * sh * math.sin(lt * 60), dy=12 * sh * math.cos(lt * 53))


def power(ctx, lt):
    img = blueprint()
    tg = ctx.wt("gira")
    u = easeio(clamp01(lt / max(0.8, ctx.dur * 0.6)))
    phi = 410 + 130 * u
    # cilindro um pouco menor, à esquerda; roda girando à direita
    ss = SS(W, H, s=2)
    cylinder(ss, 360, 560, 360, 640, phi, t=lt, big=True)
    cr = 640 * 0.62 * 0.5; ccy = 560 + 640 + cr * 0.3 + 640 * 0.3
    ang = math.radians(phi)
    # virabrequim -> eixo -> roda
    ss.line([(360, ccy), (840, ccy)], (*INK, 255), 26); ss.line([(360, ccy), (840, ccy)], STEEL, 16)
    wheel(ss, 840, ccy, 200, ang)
    for k in range(3):
        a0 = ang + k * 2.1
        ss.line(A.ell_pts(840, ccy, 250, 250, 0, 12, a0, a0 + 0.9), (255, 222, 40, int(255 * ease((lt - tg + 0.6) / 0.4))), 12)
    A.arrow(ss, 620, 760, 620, 1000, FIRE, w=36, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 2))


# ======================================================================= cena 8: Visão do Bicho (o ouvido)
def dichro(im):
    """aproxima a visão de 2 cones do cachorro (azul × amarelo)"""
    arr = np.asarray(im.convert("RGB"), np.float32)
    y = (arr[..., 0] + arr[..., 1]) * 0.5; b = arr[..., 2]
    out = np.stack([y, y * 0.95, b], axis=2)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).convert("RGBA")


def vision(ctx, lt):
    base = car_frame(lt + 5, ear=1.0)
    img = dichro(base.filter(ImageFilter.GaussianBlur(10)))
    img.alpha_composite(Image.new("RGBA", (W, H), (10, 10, 30, 120)))
    t45 = ctx.wt("45"); t20 = ctx.wt("20")
    # ondas de som saindo do motor (direita) até a orelha
    ss = SS(W, H, s=2)
    for k in range(7):
        r = (lt * 380 + k * 140) % 980
        a = int(220 * (1 - r / 980))
        ss.ellipse(960, 1280, r, r, ink=(255, 240, 120, a), w=8)
    img.alpha_composite(ss.get())
    # cachorro grande, orelha em pé
    ss = SS(W, H, s=2)
    dog(ss, 330, 1530, 560, t=lt, ear=1.0, eye=1.2)
    img.alpha_composite(ss.get())
    # régua de frequências (topo, acima das legendas)
    ss = SS(W, H, s=2)
    x0, x1, y0 = 110, 970, 720
    ss.rrect(x0 - 30, y0 - 170, x1 + 30, y0 + 110, 30, fill=(10, 14, 30, 220), ink=INK, w=6)
    fx = lambda k: lerp(x0, x1, k / 50)
    q20 = ease((lt - 0.3) / 0.6); q45 = ease((lt - t45 + 0.2) / 0.9)
    ss.rrect(fx(0), y0 - 120, fx(20 * q20 + 0.01), y0 - 70, 20, fill=(255, 255, 255, 230))
    ss.text((fx(0) + 10, y0 - 145), "VOCÊ", 34, "anton", fill=(255, 255, 255), anchor="lm", stroke=4)
    ss.rrect(fx(0), y0 - 40, fx(45 * q45 + 0.01), y0 + 10, 20, fill=(80, 140, 255))
    ss.text((fx(0) + 10, y0 + 50), "CACHORRO", 34, "anton", fill=(140, 180, 255), anchor="lm", stroke=4)
    for k in range(0, 51, 10):
        ss.line([(fx(k), y0 + 14), (fx(k), y0 + 28)], (255, 255, 255, 180), 3)
    if q20 > 0.9:
        ss.text((fx(20) + 10, y0 - 95), "20 mil", 34, "mont-ExtraBold", fill=(255, 255, 255), anchor="lm", stroke=4)
    if q45 > 0.9:
        ss.text((fx(45), y0 + 60), "45 mil", 34, "mont-ExtraBold", fill=(140, 180, 255), anchor="mm", stroke=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.8), dx=4 * math.sin(lt * 1.3))


# ======================================================================= cena 9: escape
def exhaust(ctx, lt):
    img = blueprint()
    tx = ctx.wt("expulsa"); te = ctx.wt("escapamento")
    u = easeio(clamp01((lt - tx + 0.3) / max(0.8, te - tx + 0.6)))
    phi = lerp(542, 718, u)
    big_cyl(img, phi, lt)
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(3)
    for k in range(14):  # fumaça saindo pelo duto da direita (cinza)
        uu = (lt * 0.7 + k / 14) % 1.0
        x = 810 + 260 * uu + rng.uniform(-20, 20); y = 560 - 260 * uu + 30 * math.sin(uu * 6 + k)
        ss.circle(x, y, 26 + 50 * uu, fill=(*SMOKE, int(200 * (1 - uu) * u)))
    ss.text((900, 300), "FUMAÇA", 56, "anton", fill=(220, 220, 230), stroke=7)
    A.arrow(ss, 920, 1720, 920, 1500, (255, 255, 255, int(255 * (u < 0.98))), w=34, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * u)


# ======================================================================= cena 10: conta-giros
def tacho(ss, cx, cy, r, v):
    ss.circle(cx, cy, r + 22, fill=(18, 20, 26), ink=INK, w=8)
    for k in range(0, 81, 5):
        a = math.radians(lerp(140, 400, k / 80))
        r0 = r - (40 if k % 10 == 0 else 20)
        col = (255, 70, 60) if k >= 60 else (235, 235, 235)
        ss.line([(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + r * math.cos(a), cy + r * math.sin(a))], col, 7 if k % 10 == 0 else 3)
        if k % 10 == 0:
            ss.text((cx + (r - 85) * math.cos(a), cy + (r - 85) * math.sin(a)), str(k // 10), 48, "anton", fill=(240, 240, 240))
    a = math.radians(lerp(140, 400, clamp01(v / 8000)))
    ss.line([(cx, cy), (cx + (r - 30) * math.cos(a), cy + (r - 30) * math.sin(a))], (255, 90, 60), 14)
    ss.circle(cx, cy, 28, fill=(255, 90, 60), ink=INK, w=5)
    ss.text((cx, cy + r * 0.5), "×1000 rpm", 36, "mont-ExtraBold", fill=(200, 200, 210))


def rpm(ctx, lt):
    img = blueprint()
    t2 = ctx.wt("mil"); t17 = ctx.wt("17")
    v = 2000 * ease((lt - 0.1) / max(0.5, t2 + 0.3)) + 40 * math.sin(lt * 20)
    ss = SS(W, H, s=2)
    tacho(ss, 540, 720, 300, v)
    img.alpha_composite(ss.get())
    # um cilindro pequeno piscando rápido + contador
    q = ease((lt - t17 + 0.3) / 0.4)
    ss = SS(W, H, s=2)
    cylinder(ss, 300, 1380, 200, 300, lt * 360 * 16.7 * 2 * 0.1 + 300, t=lt, a=int(255 * max(0.4, q)))
    n = int(clamp01((lt - t17 + 0.2) / 1.0) * 17)
    ss.text((740, 1480), f"{n}", 200, "anton", fill=(255, 222, 40, int(255 * q)), stroke=12)
    ss.text((740, 1640), "por segundo", 48, "anton", fill=(255, 255, 255, int(255 * q)), stroke=6)
    img.alpha_composite(ss.get())
    # flash a cada "explosão" (simbólico, 17 Hz ficaria um borrão: 1 a cada 3 quadros)
    if q > 0.5 and int(lt * 30) % 3 == 0:
        A.paste_c(img, A.glow(220, FIRE, 160), 300, 1420)
    return A.cam(img, zoom=1.0 + 0.02 * math.sin(lt * 3))


# ======================================================================= cena 11: loop
def loop(ctx, lt):
    tc = ctx.wt("cochilando")
    tr = lt - ctx.dur + 1 / 30.0
    back = easeio(clamp01((lt - 0.2) / max(0.5, ctx.dur - 0.5)))
    sleep = ease((lt - tc) / 0.4) * (1 - clamp01((lt - ctx.dur + 0.25) / 0.2))
    img = car_frame(tr, sleep=sleep, boost=1.0 + 1.2 * (1 - back))
    z = lerp(2.2, HZ, back)
    cx = lerp(920, HCX, back); cy = lerp(1300, HCY, back)
    return A.cam(img, zoom=z, cx=cx, cy=cy, rot=0.3 * math.sin(tr * 0.8) * back)


# ======================================================================= capa
def cover_bg(cv):
    img = sky_road(1.0)
    ss = SS(W, H, s=2)
    shell = [(-60, 1560), (-60, 1020), (60, 760), (640, 740), (830, 1030), (1090, 1090), (1120, 1580)]
    ss.poly(shell, fill=(*GLASS, 90), ink=INK, w=8)
    ss.poly([(-60, 1360), (1120, 1360), (1120, 1600), (-60, 1600)], fill=CAR, ink=INK, w=8)
    ss.rrect(760, 1130, 1080, 1440, 20, fill=(20, 40, 70, 190), ink=INK, w=5)
    engine_row(ss, 785, 1190, 50, 120, 22, 350, 1.0, boost=2.0)
    wheel(ss, 230, 1600, 130, 0.3); wheel(ss, 900, 1600, 130, 0.3)
    img.alpha_composite(ss.get())
    A.paste_c(img, A.glow(300, FIRE, 200), 920, 1260)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 600)
    ss = SS(int(1.3 * s), int(1.55 * s), s=2)
    dog(ss, 0.62 * s, 0.85 * s, s, t=0.3, eye=1.7, ear=0.5, pant=0.8)
    return ss.get()
