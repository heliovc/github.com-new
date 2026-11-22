"""Dia 3B — "E se você fosse um pombo no semáforo?" (formato ATUAL; paleta: crepúsculo roxo e rosa, asfalto
grafite, luzes do semáforo; campo magnético em violeta, eletricidade em amarelo).

Cenas: perch (gancho: pombo em cima do semáforo, carros lá embaixo), cut (o fio enrolado embaixo do asfalto e o corte
em quadrado), field (corrente -> campo magnético), car (o metal do carro mexe no campo; a frequência sobe), vision
(Visão do Bicho: o campo magnético da Terra, que o pombo sente para voltar para casa), box (a caixa da esquina avisa o
semáforo: verde), land/land2 (o pombo pousa no quadrado e nada acontece -> volta ao quadro inicial = loop).
Fatos: FHWA Traffic Detector Handbook (laço indutivo); Keeton (1971, PNAS); Wiltschko & Wiltschko.
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached, noise_tex

GRAY = (150, 158, 178); GRAY_L = (196, 202, 218); GRAY_D = (96, 102, 128); HEAD = (104, 110, 140)
NECK_G = (80, 190, 150); NECK_P = (170, 90, 190); FOOT = (236, 120, 130); EYE = (255, 140, 40)
ASPH = (62, 60, 70); LINE = (236, 232, 222); COPPER = (222, 132, 64)
ELEC = (255, 222, 40); MAG = (190, 120, 255)
RED = (255, 60, 60); AMB = (255, 180, 40); GRN = (60, 240, 120)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= pombo (perfil, cabeça para a direita)
def pigeon(ss, x, y, s, t=0.0, flip=1, bob=0.0, wing=0.0, feet=True, peck=0.0):
    """(x,y) = centro do corpo; s = comprimento do corpo"""
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    iw = max(1.5, s * 0.012)
    hx = 0.36 + 0.05 * bob; hy = -0.36 + 0.18 * peck
    if feet:
        for dx in (-0.02, 0.1):
            ss.line(P([(dx, 0.22), (dx + 0.02, 0.38)]), FOOT, s * 0.03)
            for a in (-0.09, 0.0, 0.09):
                ss.line(P([(dx + 0.02, 0.38), (dx + 0.02 + a, 0.42)]), FOOT, s * 0.022)
    # cauda
    ss.poly(P([(-0.32, -0.02), (-0.72, 0.1), (-0.74, 0.2), (-0.3, 0.14)]), fill=GRAY_D, ink=INK, w=iw)
    ss.line(P([(-0.64, 0.12), (-0.66, 0.19)]), (40, 40, 56), s * 0.04, cap=False)
    # corpo
    ss.poly(P(A.ell_pts(0.0, 0.04, 0.4, 0.22, -8, 40)), fill=GRAY, ink=INK, w=iw)
    ss.poly(P(A.ell_pts(0.05, 0.13, 0.28, 0.08, -8, 24)), fill=(*GRAY_L, 200))
    # pescoço iridescente
    ss.poly(P(A.spline([(0.12, -0.12), (hx - 0.06, hy + 0.08), (hx + 0.08, hy + 0.06), (0.36, 0.05), (0.2, 0.1)], 6)),
            fill=HEAD, ink=INK, w=iw)
    ss.poly(P(A.spline([(0.2, -0.06), (hx - 0.02, hy + 0.16), (hx + 0.07, hy + 0.15), (0.32, 0.02)], 6)), fill=(*NECK_G, 220))
    ss.poly(P(A.spline([(0.24, -0.02), (hx + 0.0, hy + 0.22), (hx + 0.06, hy + 0.22), (0.31, 0.04)], 6)), fill=(*NECK_P, 200))
    # asa com 2 faixas pretas
    wa = -55 * wing
    wpts = A.xf([(0.0, 0.0), (-0.52, 0.06), (-0.5, 0.14), (0.02, 0.12)], 0.14, -0.06, 1, wa)
    ss.poly(P(wpts), fill=GRAY_L, ink=INK, w=iw)
    for u in (0.45, 0.7):
        a = A.xf([(-0.52 * u, 0.05), (-0.52 * u + 0.03, 0.13)], 0.14, -0.06, 1, wa)
        ss.line(P(a), (36, 36, 50), s * 0.03, cap=False)
    # cabeça, bico, olho
    ss.poly(P(A.ell_pts(hx, hy, 0.11, 0.095, 0, 24)), fill=HEAD, ink=INK, w=iw)
    ss.poly(P([(hx + 0.09, hy - 0.01), (hx + 0.21, hy + 0.02), (hx + 0.09, hy + 0.04)]), fill=(60, 50, 60), ink=INK, w=iw * 0.7)
    ss.poly(P(A.ell_pts(hx + 0.1, hy - 0.015, 0.03, 0.02, 0, 12)), fill=(240, 240, 236))
    ex, ey = P([(hx + 0.03, hy - 0.02)])[0]; er = s * 0.036
    ss.circle(ex, ey, er, fill=EYE, ink=INK, w=iw * 0.7)
    ss.circle(ex + er * 0.15 * flip, ey, er * 0.5, fill=(20, 14, 20))
    ss.circle(ex - er * 0.25 * flip, ey - er * 0.3, er * 0.28, fill=(255, 255, 255))


# ======================================================================= cidade ao entardecer
def sky_city():
    def mk():
        im = A.vgrad(W, H, [(0, (52, 30, 98)), (0.35, (130, 64, 150)), (0.62, (246, 138, 140)), (0.75, (255, 190, 140)), (1, (90, 60, 90))])
        A.paste_c(im, A.glow(500, (255, 220, 170), 140), 760, 1180)
        ss = SS(W, H, s=2); rng = np.random.default_rng(4)
        for layer, (base, col, wc) in enumerate(((1180, (120, 70, 130), (255, 214, 150, 140)), (1290, (70, 40, 90), (255, 220, 140, 200)))):
            x = -40
            while x < W + 40:
                bw = rng.uniform(70, 170); bh = rng.uniform(160, 520) * (1.0 - 0.3 * layer)
                ss.rect(x, base - bh, x + bw, 1500, fill=col)
                for wy in np.arange(base - bh + 24, 1450, 34):
                    for wx in np.arange(x + 14, x + bw - 14, 26):
                        if rng.random() < 0.35: ss.rect(wx, wy, wx + 12, wy + 16, fill=wc)
                x += bw + rng.uniform(4, 20)
        im.alpha_composite(ss.get())
        return im
    return cached("sky", mk)


def street_layer():
    def mk():
        ss = SS(W, 520, s=2)
        ss.rect(0, 0, W, 520, fill=ASPH)
        ss.rect(0, 0, W, 40, fill=(120, 110, 120))
        for k in range(9):
            x = 40 + k * 120
            ss.poly([(x, 120), (x + 70, 120), (x + 90, 300), (x + 10, 300)], fill=(*LINE, 230))
        ss.rect(0, 420, W, 432, fill=(240, 200, 60))
        return ss.get()
    return cached("street", mk)


def car_sprite(col, s=1.0):
    def mk():
        w, h = int(320 * s), int(150 * s)
        ss = SS(w, h, s=2)
        k = s
        ss.poly([(10 * k, 110 * k), (20 * k, 70 * k), (80 * k, 60 * k), (120 * k, 20 * k), (230 * k, 20 * k), (270 * k, 62 * k),
                 (310 * k, 72 * k), (312 * k, 110 * k)], fill=col, ink=INK, w=4)
        ss.poly([(130 * k, 30 * k), (180 * k, 30 * k), (180 * k, 62 * k), (100 * k, 62 * k)], fill=(170, 210, 240), ink=INK, w=3)
        ss.poly([(190 * k, 30 * k), (226 * k, 30 * k), (258 * k, 62 * k), (190 * k, 62 * k)], fill=(170, 210, 240), ink=INK, w=3)
        ss.circle(300 * k, 84 * k, 8 * k, fill=(255, 240, 180))
        for wx in (75, 245):
            ss.circle(wx * k, 112 * k, 28 * k, fill=(30, 28, 34), ink=INK, w=3)
            ss.circle(wx * k, 112 * k, 12 * k, fill=(170, 170, 180))
        return ss.get()
    return cached(("car", col, s), mk)


def signal_head(ss, x, y, s, lit="red", glow=1.0):
    """semáforo vertical: (x,y) = topo central; s = largura"""
    h = s * 2.7
    ss.rrect(x - s * 0.62, y - s * 0.08, x + s * 0.62, y + h + s * 0.08, s * 0.16, fill=(250, 196, 40), ink=INK, w=5)
    ss.rrect(x - s / 2, y, x + s / 2, y + h, s * 0.12, fill=(36, 38, 44), ink=INK, w=5)
    for k, (name, col) in enumerate((("red", RED), ("amber", AMB), ("green", GRN))):
        cy = y + s * 0.47 + k * s * 0.88
        on = name == lit
        c = col if on else mixc(col, (30, 30, 36), 0.78)
        ss.circle(x, cy, s * 0.34, fill=c, ink=INK, w=4)
        ss.poly(A.ell_pts(x, cy - s * 0.3, s * 0.42, s * 0.14, 0, 20, math.pi, 2 * math.pi), fill=(24, 24, 30))
        if on: ss.circle(x - s * 0.12, cy - s * 0.1, s * 0.08, fill=(255, 255, 255, 200))
    return [(y + s * 0.47 + k * s * 0.88) for k in range(3)]


# ======================================================================= cena 1: gancho
def perch_frame(t, lit="red"):
    img = sky_city().copy()
    A.paste(img, street_layer(), 0, 1460)
    for k, (col, sp, y0, ph) in enumerate((((60, 120, 220), 260, 1610, 0.0), ((220, 70, 70), -320, 1720, 0.4), ((240, 200, 70), 300, 1820, 0.7))):
        cs = car_sprite(col, 1.0 if k < 2 else 1.15)
        if sp < 0: cs = cs.transpose(Image.FLIP_LEFT_RIGHT)
        x = ((ph * 1500 + sp * t) % 1500) - 300
        A.paste(img, cs, x, y0 - cs.height)
    ss = SS(W, H, s=2)
    ss.rect(990, 520, 1010, 1640, fill=(60, 64, 72))          # poste
    ss.rect(430, 740, 1010, 768, fill=(60, 64, 72))           # braço
    ys = signal_head(ss, 470, 830, 180, lit)
    img.alpha_composite(ss.get())
    for cy, col, name in zip(ys, (RED, AMB, GRN), ("red", "amber", "green")):
        if name == lit: A.paste_c(img, A.glow(170, col, 120), 470, cy)
    ss = SS(W, H, s=2)
    bob = 0.5 + 0.5 * math.sin(t * 5.5)
    pigeon(ss, 470, 690 + 4 * math.sin(t * 5.5), 400, t=t, bob=bob)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 14, 0.3)
    A.paste(img, sh, -pad + 10, -pad + 16)
    img.alpha_composite(sp)
    return img


def perch(ctx, lt):
    return A.cam(perch_frame(lt), zoom=1.03 + 0.01 * math.sin(lt * 0.9), dx=10 * math.sin(lt * 0.5), rot=0.3 * math.sin(lt * 0.7))


# ======================================================================= asfalto visto de cima
def asphalt_top():
    def mk():
        n = noise_tex(W, H, seed=7, amp=9)
        base = np.array(ASPH, np.float32)[None, None, :] + n[..., None]
        im = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")
        ss = SS(W, H, s=2)
        for k in range(8):   # faixa de pedestres no topo
            x = 30 + k * 136
            ss.rect(x, 260, x + 84, 420, fill=(*LINE, 235))
        ss.rect(0, 470, W, 490, fill=(*LINE, 235))          # linha de retenção
        ss.rect(1030, 0, 1050, H, fill=(240, 200, 60, 220))
        im.alpha_composite(ss.get())
        return im
    return cached("asph", mk)


SQ = (290, 640, 790, 1060)   # quadrado do laço visto de cima (fora da legenda)


def sawcut(ss, glow=0.0):
    x0, y0, x1, y1 = SQ
    col = mixc((24, 22, 28), ELEC, glow)
    for (a, b) in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        ss.line([a, b], col, 12 + 6 * glow)
    ss.line([(x1, (y0 + y1) / 2), (1040, (y0 + y1) / 2)], col, 12 + 6 * glow)


def coil_top(ss, t, cur=0.0, a=255):
    x0, y0, x1, y1 = SQ
    for k in range(3):
        d = 14 + k * 16
        pts = [(x0 + d, y0 + d), (x1 - d, y0 + d), (x1 - d, y1 - d), (x0 + d, y1 - d), (x0 + d, y0 + d)]
        ss.line(pts, (*COPPER, a), 9)
    if cur > 0:
        per = 2 * ((x1 - x0) + (y1 - y0)) - 8 * 30
        for j in range(12):
            u = ((t * 0.5 + j / 12) % 1.0) * per
            px, py = _along(SQ, 30, u)
            ss.circle(px, py, 11, fill=(*ELEC, int(255 * cur)), ink=(*INK, int(200 * cur)), w=2)


def _along(box, d, u):
    x0, y0, x1, y1 = box; x0 += d; y0 += d; x1 -= d; y1 -= d
    w, h = x1 - x0, y1 - y0
    u %= 2 * (w + h)
    if u < w: return x0 + u, y0
    u -= w
    if u < h: return x1, y0 + u
    u -= h
    if u < w: return x1 - u, y1
    u -= w
    return x0, y1 - u


def cut(ctx, lt):
    img = asphalt_top().copy()
    ta = ctx.wt("asfalto"); tq = ctx.wt("quadrado")
    rev = ease((lt - ta + 0.5) / 0.8) * (1 - ease((lt - tq + 0.5) / 0.6))
    gl = ease((lt - tq + 0.1) / 0.4) * (0.7 + 0.3 * math.sin(lt * 8))
    ss = SS(W, H, s=2)
    sawcut(ss, gl)
    img.alpha_composite(ss.get())
    if rev > 0:   # raio-X: o asfalto fica translúcido e mostra o fio enrolado
        ov = Image.new("RGBA", (W, H), (20, 30, 60, int(150 * rev)))
        img.alpha_composite(ov)
        ss = SS(W, H, s=2)
        coil_top(ss, lt, a=int(255 * rev))
        ss.line([(SQ[2] - 14, (SQ[1] + SQ[3]) / 2), (1040, (SQ[1] + SQ[3]) / 2)], (*COPPER, int(255 * rev)), 9)
        img.alpha_composite(ss.get())
    if gl > 0:
        ss = SS(W, H, s=2)
        A.arrow(ss, 160, 1500, SQ[0] + 20, SQ[3] - 10, (255, 222, 40), w=30, iw=5)
        img.alpha_composite(ss.get())
    z = 1.0 + 0.06 * easeio(lt / max(1, ctx.dur))
    return A.cam(img, zoom=z, cx=540, cy=850, rot=-0.6 + 0.6 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= vista 3/4: laço na pista + campo
GY = 1480            # altura da pista na vista 3/4


def road34():
    def mk():
        im = A.vgrad(W, H, [(0, (48, 28, 86)), (0.45, (150, 74, 140)), (0.62, (240, 140, 140)), (1, (60, 40, 70))])
        ss = SS(W, H, s=2)
        ss.poly([(-200, H), (W + 200, H), (W + 40, GY - 200), (40, GY - 200)], fill=ASPH)
        for k in range(6):
            ss.poly([(80 + k * 180, GY + 260), (180 + k * 180, GY + 260), (170 + k * 172, GY + 380), (60 + k * 172, GY + 380)], fill=(*LINE, 220))
        img = ss.get(); im.alpha_composite(img)
        return im
    return cached("road34", mk)


def coil34_pts(d=0):
    cx, cy, rx, ry = 540, GY, 330 - d, 110 - d * 0.33
    return [(cx - rx, cy - ry), (cx + rx, cy - ry), (cx + rx + 40, cy + ry), (cx - rx - 40, cy + ry)]


def _poly_along(pts, u):
    segs = list(zip(pts, pts[1:] + pts[:1]))
    L = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in segs]
    u = (u % 1.0) * sum(L)
    for (a, b), l in zip(segs, L):
        if u <= l: return lerp(a[0], b[0], u / l), lerp(a[1], b[1], u / l)
        u -= l
    return pts[0]


def coil34(ss, t, cur=1.0):
    for k in range(3):
        p = coil34_pts(k * 18)
        ss.line(p + p[:1], COPPER, 8)
    p = coil34_pts(18)
    for j in range(14):
        x, y = _poly_along(p, t * 0.35 + j / 14)
        ss.circle(x, y, 10, fill=(*ELEC, int(255 * cur)), ink=INK, w=2)


def field_lines(ss, t, amp=1.0, squash=0.0, a=220):
    """laços do campo magnético saindo da bobina (violeta); squash = achatado embaixo do carro"""
    for k in range(6):
        r = 120 + k * 70
        h = (180 + k * 95) * amp * (1 - 0.65 * squash)
        ph = (t * 0.8 + k * 0.15) % 1.0
        pts = []
        for v in np.linspace(0, 1, 40):
            x = 540 + (v - 0.5) * 2 * r
            y = GY - h * math.sin(v * math.pi)
            pts.append((x, y))
        ss.line(pts, (*MAG, int(a * (0.7 + 0.3 * (1 - k / 6)))), 9, cap=False)
        x, y = pts[int(ph * 39)]
        ss.circle(x, y, 9, fill=(255, 240, 255, a))


def scope(ss, lt, freq=3.0, label=True, hot=0.0):
    x0, y0, x1, y1 = 140, 380, 940, 600
    ss.rrect(x0, y0, x1, y1, 24, fill=(14, 20, 30, 230), ink=INK, w=5)
    for k in range(1, 8): ss.line([(x0 + k * 100, y0 + 10), (x0 + k * 100, y1 - 10)], (60, 90, 80, 120), 2, cap=False)
    pts = [(x, (y0 + y1) / 2 + 70 * math.sin((x - x0) / (x1 - x0) * freq * 2 * math.pi - lt * 6)) for x in np.linspace(x0 + 20, x1 - 20, 160)]
    ss.line(pts, mixc((120, 255, 170), ELEC, hot), 7, cap=False)


# ======================================================================= cena 3: corrente -> campo magnético
def field(ctx, lt):
    img = road34().copy()
    tm = ctx.wt("magnético")
    cur = ease((lt - ctx.wt("corrente") + 0.2) / 0.5)
    fa = ease((lt - tm + 0.6) / 1.0)
    ss = SS(W, H, s=2)
    coil34(ss, lt, cur)
    if fa > 0: field_lines(ss, lt, amp=fa)
    img.alpha_composite(ss.get())
    A.paste_c(img, A.glow(380, MAG, int(70 * fa)), 540, GY - 300)
    return A.cam(img, zoom=1.04 - 0.03 * easeio(lt / max(1, ctx.dur)), dy=20 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 4: o carro mexe no campo
def car(ctx, lt):
    img = road34().copy()
    tm = ctx.wt("metal"); ts = ctx.wt("sobe")
    arrive = easeio((lt) / max(0.5, tm + 0.2))
    sq = ease((lt - tm + 0.3) / 0.6)
    fq = lerp(3.0, 6.0, ease((lt - ts + 0.1) / 0.6))
    ss = SS(W, H, s=2)
    coil34(ss, lt)
    field_lines(ss, lt, amp=1.0, squash=sq)
    img.alpha_composite(ss.get())
    cs = car_sprite((70, 130, 230), 2.4)
    cx = lerp(-700, 540, arrive)
    A.paste(img, cs, cx - cs.width / 2, GY + 60 - cs.height)
    if sq > 0:   # correntes induzidas na lataria (amarelo = eletricidade)
        ss = SS(W, H, s=2)
        for k in range(4):
            a0 = lt * 6 + k * 1.6
            ex, ey = cx - 240 + k * 160, GY - 40
            ss.poly(A.ell_pts(ex, ey, 46, 16, 0, 20, a0, a0 + 4.2) + A.ell_pts(ex, ey, 34, 10, 0, 20, a0 + 4.2, a0)[::1],
                    fill=(*ELEC, int(220 * sq)))
        img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    scope(ss, lt, fq, hot=clamp01((fq - 3) / 3))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dx=4 * sq * math.sin(lt * 30) * (1 - clamp01(lt - tm)))


# ======================================================================= cena 5: Visão do Bicho (campo da Terra)
def vision(ctx, lt):
    img = sky_city().copy()
    rgb = np.asarray(img.convert("RGB"), np.float32)
    g = rgb @ np.array([0.3, 0.59, 0.11], np.float32)
    dark = np.stack([g * 0.35, g * 0.3, g * 0.5], 2)
    img = Image.fromarray(np.clip(dark, 0, 255).astype(np.uint8)).convert("RGBA")
    u = ease(lt / 0.6)
    ss = SS(W, H, s=2)
    for k in range(10):   # linhas do campo da Terra: arcos que mergulham no horizonte
        r = 600 + k * 220
        pts = []
        for v in np.linspace(0, 1, 50):
            x = lerp(-300, W + 300, v)
            y = 1300 - (220 + k * 120) * math.sin(v * math.pi) + 30 * math.sin(lt * 1.5 + k + v * 4)
            pts.append((x, y))
        ss.line(pts, (*MAG, int(200 * u * (1 - k / 12))), 7, cap=False)
        ph = (lt * 0.35 + k * 0.13) % 1.0
        x, y = pts[int(ph * 49)]
        ss.circle(x, y, 12, fill=(255, 240, 255, int(255 * u)))
    # casa (pombal) no horizonte e o caminho até ela
    hx, hy = 860, 1250
    ss.poly([(hx - 50, hy), (hx, hy - 50), (hx + 50, hy), (hx + 40, hy + 50), (hx - 40, hy + 50)], fill=(255, 220, 140, int(255 * u)), ink=INK, w=4)
    q = ease((lt - ctx.wt("casa") + 0.3) / 0.8)
    for k in range(int(14 * q)):
        f = k / 14
        ss.circle(lerp(540, hx, f), lerp(1750, hy + 60, f) - 120 * math.sin(f * math.pi), 9, fill=(255, 255, 255, 230))
    img.alpha_composite(ss.get())
    A.paste_c(img, A.glow(500, MAG, int(60 * u)), 540, 1000)
    ss = SS(W, H, s=2)   # bico e pontas das asas na borda (POV voando)
    fl = math.sin(lt * 7)
    for sg in (-1, 1):
        ss.poly([(540 + sg * 560, 1500 - 140 * fl), (540 + sg * 300, 1880), (540 + sg * 700, 2000)], fill=GRAY_L, ink=INK, w=5)
        ss.line([(540 + sg * 470, 1600 - 100 * fl), (540 + sg * 360, 1880)], (36, 36, 50), 16, cap=False)
    ss.poly([(470, 1980), (540, 1800), (610, 1980)], fill=(60, 50, 60), ink=INK, w=5)
    ss.poly(A.ell_pts(540, 1890, 40, 22, 0, 16), fill=(240, 240, 236))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.04 + 0.02 * math.sin(lt * 0.7), rot=2.0 * math.sin(lt * 0.8), dy=12 * fl)


# ======================================================================= cena 6: a caixa da esquina -> verde
def box(ctx, lt):
    img = sky_city().copy()
    A.paste(img, street_layer(), 0, 1460)
    tmu = ctx.wt("mudança"); tv = ctx.wt("verde")
    lit = "green" if lt > tv else "red"
    ss = SS(W, H, s=2)
    # caixa do controlador, porta aberta
    bx0, by0, bx1, by1 = 90, 760, 470, 1420
    ss.rect(260, by1, 300, 1500, fill=(70, 74, 82))
    ss.rrect(bx0, by0, bx1, by1, 18, fill=(150, 156, 160), ink=INK, w=6)
    ss.rrect(bx0 + 24, by0 + 24, bx1 - 24, by1 - 24, 10, fill=(30, 60, 50), ink=INK, w=4)
    for r in range(5):
        for c in range(3):
            ss.rect(bx0 + 60 + c * 100, by0 + 60 + r * 110, bx0 + 130 + c * 100, by0 + 110 + r * 110, fill=(20, 24, 26))
    for k in range(6):
        on = (int(lt * 6) + k) % 3 == 0 or (lt > tmu and k < 3)
        ss.circle(bx0 + 70 + k * 46, by1 - 70, 12, fill=(GRN if lt > tmu else RED) if on else (60, 60, 60))
    # fio do laço até a caixa, com o pulso amarelo
    path = [(540, 1700), (540, 1520), (280, 1520), (280, by1)]
    ss.line(path, COPPER, 8)
    q = clamp01((lt - tmu + 0.8) / 0.8)
    if q > 0 and q < 1:
        segs = list(zip(path, path[1:])); L = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in segs]
        d = q * sum(L)
        for (a, b), l in zip(segs, L):
            if d <= l:
                px, py = lerp(a[0], b[0], d / l), lerp(a[1], b[1], d / l); break
            d -= l
        ss.circle(px, py, 22, fill=ELEC, ink=INK, w=4)
    ss.rect(870, 300, 890, 1500, fill=(60, 64, 72))
    ys = signal_head(ss, 760, 440, 170, lit)
    img.alpha_composite(ss.get())
    col = GRN if lit == "green" else RED
    A.paste_c(img, A.glow(220, col, 140), 760, ys[2] if lit == "green" else ys[0])
    cs = car_sprite((70, 130, 230), 1.6)
    A.paste(img, cs, 380 + 30 * ease(lt - tv), 1700 - cs.height)
    return A.cam(img, zoom=1.03, dx=-10 + 20 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cenas 7-8: pouso no quadrado -> loop
def ground_frame(lt, ctx, land_t, settled=False):
    img = road34().copy()
    ss = SS(W, H, s=2)
    coil34(ss, lt)
    field_lines(ss, lt)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    scope(ss, lt, 3.0)
    img.alpha_composite(ss.get())
    u = 1.0 if settled else ease((lt - land_t + 0.6) / 0.9)
    py = lerp(-300, GY - 150, u); wing = 0.0 if u >= 1 else 0.5 + 0.5 * math.sin(lt * 22)
    ss = SS(W, H, s=2)
    pigeon(ss, 520, py, 360, t=lt, wing=wing, bob=0.5 + 0.5 * math.sin(lt * 5), peck=0.0)
    img.alpha_composite(ss.get())
    return img


def land(ctx, lt):
    if ctx.sc["id"] == "land":
        img = ground_frame(lt, ctx, ctx.wt("pouso"))
        tn = ctx.wt("=nada")
        q = ease((lt - tn) / 0.3)
        return A.cam(img, zoom=1.0 + 0.04 * q, dy=10 * q)
    # land2: "não existo" no chão; em "Então" sobe de volta ao gancho (o último quadro = quadro 0)
    te = ctx.wt("então", default=ctx.dur - 1.4)
    tr = lt - ctx.dur + 1 / 30.0
    g = ground_frame(lt + 10, ctx, 0, settled=True)
    u = easeio((lt - te + 0.1) / 0.7)
    if u <= 0: return A.cam(g, zoom=1.04)
    p = perch_frame(tr)
    if u >= 1: return A.cam(p, zoom=1.03 + 0.01 * math.sin(tr * 0.9), dx=10 * math.sin(tr * 0.5), rot=0.3 * math.sin(tr * 0.7))
    g = A.cam(g, zoom=1.04 + 0.2 * u, dy=300 * u)
    p = A.cam(p, zoom=lerp(1.25, 1.03 + 0.01 * math.sin(tr * 0.9), u), dy=lerp(-300, 0, u), dx=10 * math.sin(tr * 0.5) * u)
    return Image.blend(g.convert("RGB"), p.convert("RGB"), u).convert("RGBA")


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    img = sky_city().copy()
    A.paste(img, street_layer(), 0, 1460)
    ss = SS(W, H, s=2)
    ss.rect(990, 520, 1010, 1640, fill=(60, 64, 72))
    ss.rect(430, 900, 1010, 928, fill=(60, 64, 72))
    ys = signal_head(ss, 470, 980, 200, "red")
    img.alpha_composite(ss.get())
    A.paste_c(img, A.glow(260, RED, 160), 470, ys[0])
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 420)
    ss = SS(int(1.3 * s), int(1.05 * s), s=2)
    pigeon(ss, 0.6 * s, 0.5 * s, s, t=0.2, bob=0.6)
    return ss.get()
