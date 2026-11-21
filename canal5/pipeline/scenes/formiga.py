"""Dia 1A — "E se você fosse uma formiga caindo do 30º andar?" (paleta: fim de tarde dourado).

Cenas (ids do script.json): ledge, pov, surface, tug, speedo, landing (Visão do Bicho: olho composto), xray, lineup, walk.
A última cena (walk) termina subindo a parede de volta ao parapeito = mesmo quadro do início (loop).
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached, calcada, cloud, motion_blur_v

SKY = [(0, (255, 118, 96)), (0.30, (255, 160, 106)), (0.55, (255, 205, 142)), (1, (255, 226, 182))]
ANT = dict(body=(170, 56, 34), hi=(244, 134, 80), dark=(98, 28, 22), leg=(120, 38, 26), far=(86, 26, 22))
NEAR = (62, 74, 120); NEAR_DK = (50, 58, 98); RIM = (255, 172, 110)
FAR = (210, 132, 146); MIDC = (122, 98, 152)
CONC_TOP = (236, 210, 184); CONC_FRONT = (180, 148, 132)
GREEN = (84, 222, 124); ORANGE = (255, 140, 44)

CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= personagens
def ant(ss, x, y, s, rot=0.0, flip=1, phase=0.0, pose="walk", t=0.0, xray=False, alpha=255):
    """formiga de perfil (cabeça para a direita). (x,y) = centro do tórax; s = px por unidade (~2,3 u de comprimento)"""
    C = ANT
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    ink = (210, 248, 255, 255) if xray else (*INK, alpha)
    iw = max(1.4, s * (0.028 if xray else 0.02))

    def fill(c, a=255):
        return (90, 200, 255, 55) if xray else (*c, int(a * alpha / 255))

    hips = [(-0.16, 0.07), (0.02, 0.09), (0.18, 0.07)]

    def leg(i, far):
        hx, hy = hips[i]
        if pose == "fall":
            j = math.sin(t * 15 + i * 2.1 + (1.4 if far else 0))
            fx = hx + [-0.66, 0.02, 0.66][i] + 0.07 * j + (0.07 if far else 0)
            fy = 0.30 + 0.07 * math.sin(t * 13 + i * 1.7 + (0.8 if far else 0))
            kx = (hx + fx) / 2 + [-0.07, 0.0, 0.07][i]; ky = hy - 0.27 + 0.05 * j
        elif pose == "spread":
            j = math.sin(t * 6 + i * 2.1 + (1.4 if far else 0))
            fx = hx + [-0.70, 0.02, 0.70][i] + 0.04 * j + (0.07 if far else 0)
            fy = 0.18 + 0.04 * j
            kx = (hx + fx) / 2 + [-0.05, 0.0, 0.05][i]; ky = hy - 0.30
        else:
            off = [0.0, math.pi, 0.0][i] + (math.pi if far else 0.0)
            ph = phase + off; mv = 1.0 if pose == "walk" else 0.0
            fx = hx + [-0.40, 0.03, 0.40][i] + 0.12 * math.sin(ph) * mv + (0.05 if far else 0)
            fy = 0.50 - 0.07 * max(0.0, math.cos(ph)) * mv
            kx = (hx + fx) / 2 + [-0.09, 0.0, 0.09][i]; ky = min(hy, fy) - 0.19
        col = C["far"] if far else C["leg"]
        pts = P([(hx, hy), (kx, ky), (fx, fy)])
        lw = s * 0.062
        if xray:
            ss.line(pts, (120, 220, 255, 90), lw * 1.2)
            ss.line(pts, (225, 250, 255, 240), max(1.5, lw * 0.32))
        else:
            ss.line(pts, (*INK, alpha), lw + 2 * iw); ss.line(pts, (*col, alpha), lw)

    def antenna(far):
        fast = pose in ("fall",)
        sw = math.sin(t * (10 if fast else 3.2) + (1.1 if far else 0))
        sw2 = math.cos(t * (8 if fast else 2.5) + (0.6 if far else 0))
        dx = 0.05 if far else 0.0
        b = (0.62 - dx, -0.26)
        e = (0.70 + 0.05 * sw - dx, -0.64 + 0.03 * sw2)
        tp = (1.04 + 0.06 * sw - dx, -0.50 + 0.07 * sw2)
        pts = P([b, e, tp]); lw = s * 0.042; col = C["far"] if far else C["leg"]
        if xray:
            ss.line(pts, (225, 250, 255, 230), max(1.5, lw * 0.45))
        else:
            ss.line(pts, (*INK, alpha), lw + 2 * iw); ss.line(pts, (*col, alpha), lw)
            cx, cy = pts[-1]; ss.circle(cx, cy, s * 0.042, fill=(*col, alpha), ink=(*INK, alpha), w=iw)

    for i in range(3): leg(i, True)
    antenna(True)
    ss.poly(P(A.ell_pts(-0.78, 0.0, 0.44, 0.33, -14, 44)), fill=fill(C["body"]), ink=ink, w=iw)
    if not xray:
        ss.poly(P(A.ell_pts(-0.88, -0.13, 0.2, 0.085, -14, 24)), fill=(*C["hi"], int(150 * alpha / 255)))
    for k in (0, 1):
        arc = P([(-0.60 - 0.18 * k + 0.05 * math.sin(a), -0.29 + 0.58 * a / math.pi) for a in np.linspace(0.25, math.pi - 0.25, 10)])
        ss.line(arc, (200, 245, 255, 230) if xray else (*C["dark"], int(110 * alpha / 255)), max(1, s * (0.03 if xray else 0.018)), cap=False)
    ss.poly(P(A.ell_pts(-0.34, 0.03, 0.1, 0.085, 0, 20)), fill=fill(C["body"]), ink=ink, w=iw)
    th = A.spline([(-0.25, 0.04), (-0.14, -0.1), (0.06, -0.15), (0.26, -0.1), (0.34, 0.0), (0.2, 0.1), (-0.05, 0.11)], 6)
    ss.poly(P(th), fill=fill(C["body"]), ink=ink, w=iw)
    if not xray:
        ss.poly(P(A.ell_pts(0.03, -0.09, 0.15, 0.04, -8, 20)), fill=(*C["hi"], int(140 * alpha / 255)))
    ss.poly(P([(0.74, -0.06), (0.92, 0.0), (0.85, 0.07), (0.72, 0.03)]), fill=fill(C["dark"]), ink=ink, w=iw)
    ss.poly(P(A.ell_pts(0.56, -0.11, 0.24, 0.2, 12, 40)), fill=fill(C["body"]), ink=ink, w=iw)
    if xray:
        ss.line(P(A.spline([(0.5, -0.1), (0.2, -0.03), (-0.3, 0.03), (-0.62, 0.0), (-0.98, 0.06)], 6, closed=False)),
                (255, 120, 175, 170), s * 0.05)
        ss.poly(P(A.ell_pts(0.52, -0.16, 0.09, 0.07, 0, 20)), fill=(255, 150, 210, 120))
    else:
        ss.poly(P(A.ell_pts(0.5, -0.2, 0.1, 0.05, 12, 20)), fill=(*C["hi"], int(130 * alpha / 255)))
    ss.poly(P(A.ell_pts(0.63, -0.15, 0.085, 0.072, 12, 24)), fill=(200, 250, 255, 160) if xray else (22, 14, 20, alpha))
    if not xray:
        ss.poly(P(A.ell_pts(0.655, -0.178, 0.03, 0.026, 0, 14)), fill=(255, 255, 255, int(230 * alpha / 255)))
    for i in range(3): leg(i, False)
    antenna(False)


def ant_sprite(s, rot=0.0, pose="walk", phase=0.0, t=0.0, xray=False, flip=1, alpha=255):
    half = int(1.45 * s) + 8
    ss = SS(2 * half, 2 * half, s=2)
    ant(ss, half, half, s, rot, flip, phase, pose, t, xray, alpha)
    return ss.get()


def skydiver(ss, x, y, s, t=0.0, flip=1):
    """humano em queda de barriga para baixo (perfil, cabeça à direita)"""
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    suit, suit2, skin, helm = (44, 124, 228), (30, 98, 200), (240, 192, 152), (255, 206, 46)
    j = math.sin(t * 7) * 0.025

    def limb(pts, w, col):
        q = P(pts); ss.line(q, INK, s * w + 6); ss.line(q, col, s * w)

    limb([(-0.30, 0.02), (-0.64, -0.12 - j), (-0.90, -0.36 - j)], 0.15, suit2)
    limb([(0.30, -0.02), (0.36, -0.40 - j), (0.62, -0.50 - j)], 0.12, suit2)
    ss.poly(P(A.ell_pts(0, 0, 0.52, 0.18, 0, 40)), fill=suit, ink=INK, w=3)
    limb([(-0.38, -0.02), (-0.72, -0.20 + j), (-0.98, -0.44 + j)], 0.15, suit)
    limb([(0.34, -0.06), (0.44, -0.44 + j), (0.74, -0.54 + j)], 0.12, suit)
    hx, hy = P([(0.68, -0.08)])[0]
    ss.circle(hx, hy, s * 0.18, fill=helm, ink=INK, w=3)
    fx, fy = P([(0.74, -0.02)])[0]
    ss.ellipse(fx, fy, s * 0.12, s * 0.1, fill=skin, ink=INK, w=2.5)
    gx, gy = P([(0.78, -0.08)])[0]
    ss.rrect(gx - s * 0.1, gy - s * 0.04, gx + s * 0.1, gy + s * 0.04, s * 0.03, fill=(40, 50, 80), ink=INK, w=2)


def mouse(ss, x, y, s, t=0.0, flip=1):
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    g, g2, pink = (170, 164, 182), (140, 134, 156), (246, 160, 176)
    tail = P(A.bez((-0.48, 0.05), (-0.95, 0.35), (-1.1, -0.15 + 0.05 * math.sin(t * 4)), (-1.35, 0.02), 16))
    ss.line(tail, INK, s * 0.05 + 4); ss.line(tail, pink, s * 0.05)
    for fx in (-0.3, 0.25):
        q = P([(fx, 0.28)])[0]; ss.ellipse(q[0], q[1], s * 0.1, s * 0.05, fill=pink, ink=INK, w=2)
    ss.poly(P(A.ell_pts(0, 0, 0.5, 0.32, 0, 40)), fill=g, ink=INK, w=3)
    ss.poly(P(A.ell_pts(-0.1, -0.12, 0.25, 0.1, 0, 20)), fill=(205, 200, 214, 160))
    ss.poly(P(A.ell_pts(0.5, -0.08, 0.28, 0.22, 15, 30)), fill=g, ink=INK, w=3)
    ex, ey = P([(0.36, -0.33)])[0]
    ss.circle(ex, ey, s * 0.16, fill=g2, ink=INK, w=3); ss.circle(ex, ey, s * 0.09, fill=pink)
    nx, ny = P([(0.78, 0.0)])[0]; ss.circle(nx, ny, s * 0.05, fill=pink, ink=INK, w=2)
    qx, qy = P([(0.6, -0.12)])[0]; ss.circle(qx, qy, s * 0.045, fill=(20, 16, 22))
    for k in (-1, 1):
        ss.line(P([(0.74, 0.02), (0.98, 0.02 + 0.08 * k)]), (60, 50, 60, 200), 2, cap=False)


def horse(ss, x, y, s, t=0.0, flip=1):
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    b, b2, dk = (160, 102, 62), (130, 80, 48), (70, 42, 30)
    for lx, c in ((-0.42, b2), (0.38, b2)):
        ss.line(P([(lx + 0.06, 0.18), (lx + 0.08, 0.95)]), INK, s * 0.11 + 5); ss.line(P([(lx + 0.06, 0.18), (lx + 0.08, 0.95)]), c, s * 0.11)
    tail = P(A.bez((-0.68, -0.12), (-0.95, 0.0), (-0.92, 0.35), (-0.98, 0.55), 14))
    ss.line(tail, INK, s * 0.12 + 5); ss.line(tail, dk, s * 0.12)
    ss.poly(P(A.ell_pts(0, 0, 0.72, 0.32, 0, 44)), fill=b, ink=INK, w=3)
    ss.poly(P([(0.42, -0.16), (0.72, -0.78), (0.94, -0.74), (0.72, 0.02)]), fill=b, ink=INK, w=3)
    ss.poly(P(A.ell_pts(0.98, -0.66, 0.28, 0.13, 32, 30)), fill=b, ink=INK, w=3)
    ss.line(P([(0.50, -0.22), (0.66, -0.62), (0.80, -0.86)]), dk, s * 0.08)
    ss.poly(P([(0.84, -0.84), (0.90, -1.0), (0.94, -0.82)]), fill=b, ink=INK, w=2)
    qx, qy = P([(0.96, -0.74)])[0]; ss.circle(qx, qy, s * 0.03, fill=(20, 16, 22))
    for lx in (-0.5, 0.3):
        ss.line(P([(lx, 0.2), (lx + 0.02, 0.95)]), INK, s * 0.11 + 5); ss.line(P([(lx, 0.2), (lx + 0.02, 0.95)]), b, s * 0.11)
        hx, hy = P([(lx + 0.02, 0.96)])[0]; ss.rrect(hx - s * 0.07, hy - s * 0.04, hx + s * 0.07, hy + s * 0.03, 3, fill=(50, 40, 40))


# ======================================================================= camadas do prédio (cena 1 e loop)
def layer_sky():
    def mk():
        im = A.vgrad(W, 2400, SKY + [(1, (255, 226, 182))])
        A.paste_c(im, A.glow(460, (255, 236, 180), 210), 820, 560)
        ss = SS(W, 2400, s=2); ss.circle(820, 560, 74, fill=(255, 248, 214)); im.alpha_composite(ss.get())
        for k, (cx, cy, w) in enumerate(((240, 330, 520), (700, 210, 420), (520, 690, 640), (150, 860, 380))):
            A.paste_c(im, cloud(w, int(w * 0.5), seed=k, col=(255, 228, 214), a=140), cx, cy)
        return im
    return cached("sky", mk)


def layer_city():
    def mk():
        hz, hh = 880, 2600
        im = Image.new("RGBA", (W, hh))
        d = ImageDraw.Draw(im, "RGBA")
        rng = np.random.default_rng(7)
        x = -20
        while x < W + 20:
            w = int(rng.uniform(38, 110)); h = int(rng.uniform(40, 250))
            d.rectangle([x, hz - h, x + w, hz + 4], fill=mixc(FAR, (255, 196, 170), 0.25))
            if rng.random() < 0.25: d.line([(x + w // 2, hz - h), (x + w // 2, hz - h - 30)], fill=FAR, width=3)
            x += w + int(rng.uniform(-6, 10))
        g = A.vgrad(W, hh - hz, [(0, (214, 140, 150)), (0.35, (150, 104, 146)), (1, (70, 60, 104))])
        im.paste(g, (0, hz))
        d = ImageDraw.Draw(im, "RGBA")
        for k in range(14):
            yk = hz + 18 * (1.3 ** k - 1); hb = 8 * 1.3 ** k
            col = mixc((200, 130, 148), (78, 62, 110), k / 13)
            roof = mixc(col, (255, 190, 150), 0.35)
            x = -int(rng.uniform(0, 40))
            while x < W:
                wb = int(hb * rng.uniform(1.1, 2.6)); hh2 = hb * rng.uniform(0.9, 2.0)
                d.rectangle([x, yk - hh2, x + wb, yk], fill=col)
                d.rectangle([x, yk - hh2, x + wb, yk - hh2 + max(2, hb * 0.1)], fill=roof)
                sz = min(9.0, max(2.0, hb * 0.09)); stp = sz * 2.4
                if hb > 12:
                    yy = yk - hh2 + hb * 0.25
                    while yy < yk - stp * 0.6:
                        xx = x + stp * 0.6
                        while xx < x + wb - sz:
                            if rng.random() < 0.3:
                                d.rectangle([xx, yy, xx + sz, yy + sz * 1.3], fill=(255, 208, 140))
                            xx += stp
                        yy += stp * 1.3
                x += wb + int(rng.uniform(2, hb * 0.5))
        return im
    return cached("city", mk)


LEDGE0 = 1000; FLOOR = 700


def layer_building():
    def mk():
        hh = 3700
        ss = SS(W, hh, s=2)
        ss.rect(0, 0, 470, hh, fill=NEAR)
        for y in range(40, hh, 175): ss.line([(0, y), (470, y)], NEAR_DK, 2, cap=False)
        ss.rect(456, 0, 470, hh, fill=RIM)
        for k in range(-1, 4):
            ly = LEDGE0 + FLOOR * k
            wy0, wy1 = ly - 610, ly - 40
            if wy1 > 0:
                ss.rect(60, max(0, wy0), 440, wy1, fill=(44, 40, 62))
                gl = A.vgrad(360 * 2, int((wy1 - wy0 - 20) * 2), [(0, (255, 150, 132)), (0.5, (255, 196, 140)), (1, (210, 140, 150))])
                ss.paste(gl, 70, wy0 + 10)
                ss.poly([(110, wy0 + 10), (200, wy0 + 10), (90, wy1 - 10), (70, wy1 - 10), (70, wy0 + 90)], fill=(255, 245, 230, 70))
                ss.poly([(250, wy0 + 10), (290, wy0 + 10), (200, wy1 - 10), (170, wy1 - 10)], fill=(255, 245, 230, 50))
                ss.rect(244, wy0 + 10, 256, wy1 - 10, fill=(44, 40, 62))
            ss.rect(0, ly + 60, 470, ly + 95, fill=(20, 16, 40, 90))
            ss.poly([(0, ly), (612, ly), (602, ly + 22), (0, ly + 22)], fill=CONC_TOP, ink=INK, w=3)
            ss.poly([(0, ly + 22), (602, ly + 22), (602, ly + 62), (0, ly + 62)], fill=CONC_FRONT, ink=INK, w=3)
            ss.rect(0, ly + 2, 610, ly + 7, fill=(255, 236, 210, 160))
        return ss.get()
    return cached("bldg", mk)


SLIP = 0.85; V_ANT = 470.0; V_CAM = 430.0; T_TILT = 1.05; S_ANT = 150


def ledge_ant(lt):
    """estado da formiga na cena 1: (x, y_mundo, rot, pose)"""
    if lt < SLIP:
        u = lt / SLIP
        return 538 + 54 * easeio(u), LEDGE0 - 0.47 * S_ANT + 22 * u, 14 + 26 * u + 7 * math.sin(lt * 12), "fall"
    tf = lt - SLIP; ta = V_ANT / 2600
    fall = 0.5 * 2600 * tf * tf if tf < ta else 0.5 * 2600 * ta * ta + V_ANT * (tf - ta)
    return min(830, 592 + 130 * tf), LEDGE0 - 0.47 * S_ANT + 22 + fall, 40 + 55 * tf, "fall"


def ledge_tilt(lt):
    if lt < T_TILT: return 0.0
    x = lt - T_TILT
    return V_CAM * (x - 0.3 * (1 - math.exp(-x / 0.3)))


def ledge_frame(lt, anim_t=None, tilt=None, show_ant=True):
    at = lt if anim_t is None else anim_t
    tl = ledge_tilt(lt) if tilt is None else tilt
    img = Image.new("RGBA", (W, H))
    A.paste(img, layer_sky(), 0, -0.12 * tl)
    A.paste(img, layer_city(), 0, -0.36 * tl)
    ov = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(ov, "RGBA")
    rng = np.random.default_rng(3)
    vert = clamp01((lt - SLIP) / 0.4)
    for k in range(34):
        y0 = rng.uniform(0, H); x0 = rng.uniform(0, W); L = rng.uniform(80, 260); sp = rng.uniform(900, 1600)
        if vert < 1:
            x = (x0 - sp * at) % (W + 400) - 200
            d.line([(x, y0), (x + L, y0 + 6)], fill=(255, 250, 240, int(110 * (1 - vert))), width=3)
        if vert > 0:
            y = (y0 - sp * 0.8 * at) % (H + 400) - 200
            d.line([(x0, y), (x0 + 4, y + L)], fill=(255, 250, 240, int(120 * vert)), width=3)
    img.alpha_composite(ov)
    A.paste(img, layer_building(), 0, -tl)
    if show_ant:
        x, yw, rot, pose = ledge_ant(lt)
        sp = ant_sprite(S_ANT, rot, pose, t=at)
        sh, pad = A.shadow_of(sp, 10, 0.3)
        A.paste_c(img, sh, x + 14, yw - tl + 22)
        A.paste_c(img, sp, x, yw - tl)
    rngp = np.random.default_rng(11)
    for k in range(10):
        px = (rngp.uniform(0, W) - 700 * at * rngp.uniform(0.6, 1.2)) % (W + 100) - 50
        py = (rngp.uniform(0, H) - (500 * at if lt > SLIP else 0) + 40 * math.sin(at * 3 + k)) % H
        ss = SS(40, 40, s=2); ss.oval(20, 20, 10, 5, at * 300 + k * 40, fill=(140, 110, 70, 230), ink=INK, w=1.5)
        A.paste_c(img, ss.get(), px, py)
    return A.cam(img, rot=0.5 * math.sin(at * 1.4), zoom=1.03 + 0.015 * math.sin(at * 0.9))


def ledge(ctx, lt):
    return ledge_frame(lt)


# ======================================================================= cena 2: POV caindo (vista de cima)
def street_tex():
    def mk():
        pxm = 10; w, h = 1240, 2240
        im = Image.new("RGBA", (w, h), (92, 80, 112, 255))
        cal = calcada(int(5 * pxm) + 4, h, 0.35, seed=1)
        im.paste(cal, (w // 2 - 12 * pxm, 0)); im.paste(cal, (w // 2 + 7 * pxm, 0))
        d = ImageDraw.Draw(im, "RGBA")
        d.rectangle([w // 2 - 7 * pxm, 0, w // 2 + 7 * pxm, h], fill=(64, 62, 76))
        for y in range(0, h, 60): d.rectangle([w // 2 - 2, y, w // 2 + 2, y + 32], fill=(255, 214, 80))
        for sx in (-1, 1): d.rectangle([w // 2 + sx * 66 - 2, 0, w // 2 + sx * 66 + 2, h], fill=(220, 220, 224))
        for cy in (h // 2 - 260, h // 2 + 300):
            for k in range(-6, 7): d.rectangle([w // 2 + k * 10 - 3, cy, w // 2 + k * 10 + 3, cy + 40], fill=(240, 240, 240))
        rng = np.random.default_rng(5)
        cols = [(230, 70, 70), (70, 140, 240), (250, 210, 60), (240, 240, 240), (60, 60, 70), (90, 200, 150)]
        for k in range(26):
            lane = rng.choice([-35, 35]); cy = rng.uniform(40, h - 40)
            c = cols[k % len(cols)]
            d.rounded_rectangle([w // 2 + lane - 10, cy - 23, w // 2 + lane + 10, cy + 23], 6, fill=c, outline=(30, 24, 40), width=2)
            d.rectangle([w // 2 + lane - 7, cy - 12, w // 2 + lane + 7, cy - 4], fill=(40, 50, 70))
        for sx in (-1, 1):
            for y in range(30, h, 90):
                cx = w // 2 + sx * 100
                d.ellipse([cx - 26, y - 26, cx + 26, y + 26], fill=(60, 140, 76), outline=(30, 70, 40), width=2)
                d.ellipse([cx - 18, y - 20, cx + 6, y + 4], fill=(110, 190, 110))
        return im
    return cached("street", mk)


def pov_walls(img, h, f=1000, vp=(540, 1080), X=(-12, 12)):
    d = ImageDraw.Draw(img, "RGBA")
    Y0, Y1 = -115, 115

    def clipq(x0, ya0, yb0, x1, ya1, yb1):
        lim = -1500 if x1 < x0 else W + 1500
        if (x1 - lim) * (x0 - lim) < 0 or (x1 < -1500 or x1 > W + 1500):
            if (x1 < -1500 and x0 >= -1500) or (x1 > W + 1500 and x0 <= W + 1500):
                tt = (lim - x0) / (x1 - x0)
                return [(x0, ya0), (x0, yb0), (lim, yb0 + tt * (yb1 - yb0)), (lim, ya0 + tt * (ya1 - ya0))]
        return [(x0, ya0), (x0, yb0), (x1, yb1), (x1, ya1)]

    for X0 in X:
        for k in range(0, 60):
            z0 = 3.4 * k; z1 = z0 + 3.4
            d0 = h - z0
            if d0 <= 0.6: break
            d1 = max(h - z1, 0.6)
            sx0 = vp[0] + f * X0 / d0; sx1 = vp[0] + f * X0 / d1
            if (X0 < 0 and sx0 < -1500) or (X0 > 0 and sx0 > W + 1500): break
            near = 1 - d0 / h
            col = mixc((96, 92, 140), (36, 36, 70), near ** 0.7)
            q = clipq(sx0, vp[1] + f * Y0 / d0, vp[1] + f * Y1 / d0, sx1, vp[1] + f * Y0 / d1, vp[1] + f * Y1 / d1)
            d.polygon(q, fill=col)
            d.line([q[0], q[1]], fill=mixc((255, 190, 130), (60, 50, 90), near), width=2)
            za, zb = z0 + 0.9, z0 + 2.5
            da, db = h - za, max(h - zb, 0.6)
            if da <= 0.6: continue
            xa, xb = vp[0] + f * X0 / da, vp[0] + f * X0 / db
            if abs(xb - xa) < 1: continue
            ylo = -vp[1] * da / f - 3; yhi = (H - vp[1]) * da / f + 3
            for j in range(int((max(Y0, ylo) - Y0) // 3.2), int((min(Y1, yhi) - Y0) // 3.2) + 1):
                ya = Y0 + 3.2 * j + 0.6; yb = ya + 2.0
                pts = [(xa, vp[1] + f * ya / da), (xa, vp[1] + f * yb / da), (xb, vp[1] + f * yb / db), (xb, vp[1] + f * ya / db)]
                if max(abs(p[0]) for p in pts) > 6000: continue
                g = 0.5 + 0.5 * math.sin(j * 1.7 + k * 0.9)
                d.polygon(pts, fill=mixc(mixc((255, 186, 120), (190, 120, 150), g * 0.6), col, near * 0.55))


def pov_limbs(img, t, spread=0.0, bob=0.0):
    """antenas e patas da formiga aparecendo nas bordas (POV olhando para baixo)"""
    ss = SS(W, 900, s=2)
    C = ANT
    sw = math.sin(t * 7); sw2 = math.cos(t * 5.5)
    for side in (-1, 1):
        bx = 540 + side * 110
        el = (540 + side * (250 + 30 * sw), 250 + 40 * sw2 + bob)
        tp = (540 + side * (150 + 40 * sw2), 560 + 30 * sw + bob)
        pts = [(bx, -30), el, tp]
        ss.line(pts, INK, 40); ss.line(pts, C["leg"], 32)
        ss.circle(tp[0], tp[1], 26, fill=C["leg"], ink=INK, w=4)
        kx = 540 + side * (470 + 30 * spread); ky = 330 + 20 * math.sin(t * 9 + side) + bob
        fx = 540 + side * (400 + 60 * spread); fy = 720 + 30 * math.sin(t * 8 + side * 2) + bob
        pts = [(540 + side * 600, 120), (kx, ky), (fx, fy)]
        ss.line(pts, INK, 60); ss.line(pts, C["far"], 50)
    ss.poly([(470, -20), (500, 120 + bob), (530, 140 + bob), (520, -20)], fill=C["dark"], ink=INK, w=4)
    ss.poly([(610, -20), (580, 120 + bob), (550, 140 + bob), (560, -20)], fill=C["dark"], ink=INK, w=4)
    img.alpha_composite(ss.get(), (0, 0))


def pov(ctx, lt):
    h = 84 - 3.4 * lt
    f = 1000; vp = (540, 1080)
    img = A.vgrad(W, H, [(0, (120, 90, 120)), (0.5, (255, 200, 140)), (1, (120, 90, 120))])
    tex = street_tex(); sc = (f / h) / 10
    st = tex.resize((int(tex.width * sc), int(tex.height * sc)), Image.BILINEAR)
    A.paste_c(img, st, vp[0], vp[1])
    A.paste_c(img, A.glow(620, (255, 214, 150), 150), vp[0], vp[1])
    pov_walls(img, h, f, vp)
    tw = ctx.wt("parede")
    wall = clamp01((lt - tw + 0.1) / 0.35)
    ss = SS(W, H, s=1)
    A.speed_lines(ss, lt, int(40 + 140 * wall), vp[0], vp[1], 120, 1500, (255, 250, 240, int(120 + 110 * wall)),
                  w=2 + 3 * wall, seed=2, speed=0.5 + 0.9 * wall)
    img.alpha_composite(ss.get())
    if wall > 0:
        ov = SS(W, H, s=1)
        for k in range(4):
            u = ((lt - tw) * 0.9 + k / 4) % 1.0
            r = 200 + 1300 * u
            ov.ellipse(vp[0], vp[1], r, r * 1.05, ink=(200, 255, 220, int(150 * (1 - u) * wall)), w=10 + 20 * (1 - u))
        img.alpha_composite(ov.get())
        img.alpha_composite(Image.new("RGBA", (W, H), (200, 255, 225, int(40 * wall))))
    pov_limbs(img, lt, spread=wall, bob=6 * math.sin(lt * 11) * (1 + 2 * wall))
    shake = 6 * wall * math.sin(lt * 37)
    return A.cam(img, rot=0.8 * math.sin(lt * 1.2) + 0.3 * wall * math.sin(lt * 23), dx=shake, zoom=1.02)


# ======================================================================= cena 3: pouco peso, muita superfície
def facade_tile():
    def mk():
        im = layer_building().crop((0, LEDGE0 - 640, W, LEDGE0 - 640 + FLOOR))
        return im.filter(ImageFilter.GaussianBlur(5))
    return cached("ftile", mk)


def falling_bg(lt, speed=260.0, blur_city=True):
    img = Image.new("RGBA", (W, H))
    sky = layer_sky(); city = layer_city()
    A.paste(img, sky.crop((0, 300, W, 300 + H)), 0, 0)
    key = "cityblur"
    cb = cached(key, lambda: city.crop((0, 600, W, 600 + H + 400)).filter(ImageFilter.GaussianBlur(4)))
    A.paste(img, cb, 0, -((lt * speed * 0.3) % 400))
    tile = facade_tile(); off = (lt * speed) % FLOOR
    for k in range(-1, 4):
        A.paste(img, tile, 0, k * FLOOR - off)
    return img


def surface(ctx, lt):
    img = falling_bg(lt, 260)
    s = 235; cx, cy = 600, 760
    rot = 6 * math.sin(lt * 1.7)
    sp = ant_sprite(s, rot, "spread", t=lt)
    tsup = ctx.wt("superfície")
    g = clamp01((lt - tsup) / 0.3)
    if g > 0:
        a = sp.split()[3].filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(8))
        gl = Image.new("RGBA", sp.size, (*GREEN, 0)); gl.putalpha(a.point(lambda v: int(v * (0.55 + 0.25 * math.sin(lt * 9)) * g)))
        A.paste_c(img, gl, cx, cy)
    A.paste_c(img, sp, cx, cy)
    ss = SS(W, H, s=2)
    tpeso = ctx.wt("peso")
    k_air = ease((lt - 0.15) / 0.5)
    for k in range(7):
        x = cx - 330 + 110 * k + 10 * math.sin(k * 3)
        top = cy + 70 + 25 * abs(math.cos(k * 0.9))
        L = (150 + 40 * math.sin(lt * 6 + k)) * k_air
        if L > 8: A.arrow(ss, x, top + L + 40, x, top + 40, GREEN, w=24, head=2.0)
    gw = ease((lt - tpeso + 0.1) / 0.35)
    if gw > 0:
        A.arrow(ss, cx - 70, cy - 10, cx - 70, cy - 10 + 110 * gw, ORANGE, w=16, head=2.2)
        ss.text((cx - 70, cy - 10 + 110 * gw + 40), "PESO", 30, "mont-Black", fill=ORANGE, stroke=4)
    img.alpha_composite(ss.get())
    return A.cam(img, rot=0.6 * math.sin(lt * 1.3), zoom=1.0 + 0.03 * lt / max(1, ctx.dur))


# ======================================================================= cena 4: gravidade x ar (tela dividida)
def tug(ctx, lt):
    img = Image.new("RGBA", (W, H))
    for half, (top, bot) in enumerate((((255, 150, 110), (255, 214, 160)), ((150, 170, 230), (230, 210, 220)))):
        g = A.vgrad(W // 2, H, [(0, top), (1, bot)])
        img.paste(g, (half * W // 2, 0))
    vs = (90, 900)
    for half in (0, 1):
        speed = vs[half]
        for k in range(4):
            c = cloud(300, 140, seed=10 + k + half * 5, col=(255, 255, 255), a=120, blur=8)
            y = (k * 520 - lt * speed) % (H + 300) - 150
            A.paste_c(img, c, half * 540 + 120 + (k % 2) * 300, y)
        if half == 1:
            ov = SS(540, H, s=1); rng = np.random.default_rng(4)
            for k in range(26):
                x = rng.uniform(10, 530); L = rng.uniform(120, 300)
                y = (rng.uniform(0, H) - lt * 1800) % (H + 300) - 300
                ov.line([(x, y), (x, y + L)], (255, 255, 255, 140), 3, cap=False)
            img.alpha_composite(ov.get(), (540, 0))
    ss = SS(W, H, s=2)
    ss.rect(536, 0, 544, H, fill=(255, 255, 255))
    ss.circle(540, 760, 52, fill=(255, 255, 255), ink=INK, w=5)
    ss.text((540, 760), "×", 70, "mont-Black", fill=INK)
    ss.text((270, 540), "FORMIGA", 60, "anton", fill=(255, 255, 255), stroke=6)
    ss.text((810, 540), "HUMANO", 60, "anton", fill=(255, 255, 255), stroke=6)
    ant(ss, 255, 700, 140, rot=0, pose="fall", t=lt)
    skydiver(ss, 800, 710, 205, t=lt)
    tg = ctx.wt("gravidade"); ta = ctx.wt("=ar"); tm = ctx.wt("menor"); tgan = ctx.wt("ganha")
    Lg = 250 * ease((lt - tg + 0.1) / 0.4)
    La_ant = 250 * ease((lt - ta + 0.05) / 0.5)
    La_hum = (60 * ease((lt - ta + 0.05) / 0.5) + 60 * easeio((lt - tm) / 2.0))
    for cx, La in ((255, La_ant), (800, La_hum)):
        if Lg > 6: A.arrow(ss, cx - 45, 760, cx - 45, 760 + Lg, ORANGE, w=34, head=2.0)
        if La > 6: A.arrow(ss, cx + 55, 800 + La, cx + 55, 800, GREEN, w=34, head=2.0)
    if Lg > 6:
        ss.text((cx_l := 255 - 45, 760 + Lg + 50), "gravidade", 34, "mont-Black", fill=ORANGE, stroke=5)
        ss.text((800 - 45, 760 + Lg + 50), "gravidade", 34, "mont-Black", fill=ORANGE, stroke=5)
    if La_ant > 6: ss.text((255 + 55, 800 + La_ant + 45), "ar", 38, "mont-Black", fill=(30, 170, 90), stroke=5)
    if La_hum > 6: ss.text((800 + 55, 800 + La_hum + 45), "ar", 38, "mont-Black", fill=(30, 170, 90), stroke=5)
    q = ease((lt - tgan) / 0.3)
    if q > 0:
        for cx, txt, col in ((270, "AR = PESO", (30, 150, 80)), (810, "PESO > AR", (220, 90, 30))):
            ss.rrect(cx - 140, 1330 - 46, cx + 140, 1330 + 46, 22, fill=(255, 255, 255, int(235 * q)), ink=INK, w=4)
            ss.text((cx, 1330), txt, 44, "mont-Black", fill=col)
    img.alpha_composite(ss.get())
    return img


# ======================================================================= cena 5: velocímetros
def gauge(ss, cx, cy, r, v, col, vmax=200):
    ss.circle(cx, cy, r + 26, fill=(14, 18, 40, 230), ink=(255, 255, 255, 80), w=4)
    for k in range(0, vmax + 1, 10):
        a = math.radians(210 - 240 * k / vmax)
        big = k % 40 == 0
        r0 = r - (34 if big else 18)
        ss.line([(cx + r0 * math.cos(a), cy - r0 * math.sin(a)), (cx + r * math.cos(a), cy - r * math.sin(a))],
                (255, 255, 255, 230 if big else 140), 5 if big else 3, cap=False)
        if big:
            ss.text((cx + (r - 70) * math.cos(a), cy - (r - 70) * math.sin(a)), str(k), 30, "mont-Bold", fill=(220, 225, 240))
    a = math.radians(210 - 240 * min(v, vmax) / vmax)
    tip = (cx + (r - 20) * math.cos(a), cy - (r - 20) * math.sin(a))
    pa = (cx + 14 * math.cos(a + math.pi / 2), cy - 14 * math.sin(a + math.pi / 2))
    pb = (cx + 14 * math.cos(a - math.pi / 2), cy - 14 * math.sin(a - math.pi / 2))
    ss.poly([pa, tip, pb], fill=col, ink=INK, w=3)
    ss.circle(cx, cy, 24, fill=(240, 240, 250), ink=INK, w=4)


def speedo(ctx, lt):
    img = A.vgrad(W, H, [(0, (26, 30, 70)), (1, (60, 40, 90))])
    ov = SS(W, H, s=1); rng = np.random.default_rng(9)
    for k in range(40):
        x = rng.uniform(0, W); L = rng.uniform(60, 200); y = (rng.uniform(0, H) - lt * 700) % (H + 200) - 200
        ov.line([(x, y), (x, y + L)], (255, 255, 255, 60), 2, cap=False)
    img.alpha_composite(ov.get())
    ss = SS(W, H, s=2)
    tseg = ctx.wt("segundo"); t190 = ctx.wt("190")
    va = 6 * A.back(clamp01((lt - tseg + 0.35) / 0.35), 1.2)
    tau = max(0.3, (t190 - 0.2) / math.log(39))
    vh = 195 * (1 - math.exp(-max(0.0, lt - 0.2) / tau))
    gauge(ss, 280, 830, 200, va, (255, 214, 40))
    gauge(ss, 800, 830, 200, vh, (255, 90, 70))
    ant(ss, 280, 560, 60, pose="fall", t=lt)
    skydiver(ss, 800, 570, 95, t=lt)
    ss.text((280, 1000), f"{max(0, round(va))} km/h", 74, "anton", fill=(255, 222, 40), stroke=6)
    ss.text((800, 1000), f"{int(vh)} km/h", 74, "anton", fill=(255, 255, 255) if vh < 190 else (255, 222, 40), stroke=6)
    img.alpha_composite(ss.get())
    if lt > tseg:
        q = ease((lt - tseg) / 0.3)
        ring = SS(W, H, s=1); r = 40 + 90 * ((lt - tseg) % 0.9)
        ring.ellipse(280, 830, r, r, ink=(255, 222, 40, int(200 * q * (1 - ((lt - tseg) % 0.9) / 0.9))), w=6)
        img.alpha_composite(ring.get())
    return A.cam(img, dx=3 * math.sin(lt * 31) * clamp01((vh - 120) / 70), rot=0.0)


# ======================================================================= cena 6: pouso (Visão do Bicho: olho composto)
def ground_tex():
    def mk():
        im = calcada(2200, 2200, 1.0, seed=3)
        im.alpha_composite(A.rgrad(1100, [(0, (255, 200, 120, 90)), (0.6, (255, 170, 90, 30)), (1, (0, 0, 0, 0))]), (0, 0))
        ss = SS(2200, 2200, s=2)
        P = A.xf(A.spline([(-1, 0), (-0.3, -0.45), (0.6, -0.35), (1, 0), (0.6, 0.35), (-0.3, 0.45)], 8), 1300, 900, 150, 30)
        ss.poly(P, fill=(98, 170, 70), ink=INK, w=4)
        ss.line(A.xf([(-1.1, 0), (1, 0)], 1300, 900, 150, 30), (60, 120, 50), 6)
        ss.circle(860, 1400, 70, fill=(210, 60, 50), ink=INK, w=5)
        ss.circle(860, 1400, 50, ink=(240, 200, 200), w=4)
        rng = np.random.default_rng(2)
        for _ in range(14):
            x, y = rng.uniform(500, 1700, 2); r = rng.uniform(10, 26)
            ss.ellipse(x, y, r * 1.3, r, fill=(150, 140, 130), ink=INK, w=3)
        im.alpha_composite(ss.get())
        return im
    return cached("ground", mk)


def landing(ctx, lt):
    tc = ctx.wt("minúscula", default=ctx.dur * 0.55)
    s0, s1 = 0.93, 2.6
    if lt < tc:
        sc = s0 / (1 - (1 - s0 / s1) * lt / tc)
    else:
        x = lt - tc
        sc = s1 * (1 + 0.06 * math.exp(-x * 7) * math.sin(x * 26))
    tex = ground_tex()
    cw, chh = W / sc, H / sc
    cx, cy = 1100 + 25 * math.sin(lt * 0.7), 1100 + 8 * lt
    crop = tex.crop((int(cx - cw / 2), int(cy - chh / 2), int(cx + cw / 2), int(cy + chh / 2))).resize((W, H), Image.BILINEAR)
    img = crop
    if lt >= tc:
        x = lt - tc; ss = SS(W, H, s=1); rng = np.random.default_rng(8)
        for k in range(26):
            a = rng.uniform(0, 2 * math.pi); v = rng.uniform(300, 900)
            r = v * (1 - math.exp(-x * 3)) / 3
            ss.circle(540 + math.cos(a) * r, 1150 + math.sin(a) * r * 0.6, 10 + 14 * rng.random(),
                      fill=(230, 210, 180, int(200 * math.exp(-x * 1.5))))
        img.alpha_composite(ss.get())
    bob = -40 * math.exp(-(lt - tc) * 6) * (lt >= tc)
    pov_limbs(img, lt, spread=1.0 if lt < tc else 0.3, bob=bob)
    return img


# ======================================================================= cena 7: raio-X do exoesqueleto
def lab_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (10, 22, 50)), (1, (18, 40, 80))])
        ov = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(ov)
        for x in range(0, W, 60): d.line([(x, 0), (x, H)], fill=(80, 180, 255, 34), width=1)
        for y in range(0, H, 60): d.line([(0, y), (W, y)], fill=(80, 180, 255, 34), width=1)
        im.alpha_composite(ov); d = ImageDraw.Draw(im)
        d.rectangle([0, 1040, W, H], fill=(14, 30, 60))
        d.line([(0, 1040), (W, 1040)], fill=(120, 210, 255, 160), width=3)
        return im
    return cached("lab", mk)


def human_xray(ss, x, y, s):
    c, b = (120, 210, 255, 150), (235, 250, 255, 240)
    ss.circle(x, y - 1.6 * s, 0.22 * s, ink=c, w=3)
    ss.poly([(x - 0.3 * s, y - 1.3 * s), (x + 0.3 * s, y - 1.3 * s), (x + 0.24 * s, y - 0.2 * s), (x - 0.24 * s, y - 0.2 * s)], ink=c, w=3)
    ss.line([(x, y - 1.35 * s), (x, y - 0.25 * s)], b, 4)
    for k in range(5):
        yy = y - 1.2 * s + k * 0.16 * s
        ss.line([(x - 0.2 * s, yy + 0.04 * s), (x, yy), (x + 0.2 * s, yy + 0.04 * s)], b, 3, cap=False)
    for sx in (-1, 1):
        ss.line([(x + sx * 0.32 * s, y - 1.25 * s), (x + sx * 0.42 * s, y - 0.55 * s)], b, 3)
        ss.line([(x + sx * 0.12 * s, y - 0.2 * s), (x + sx * 0.16 * s, y + 0.75 * s)], b, 4)
    ss.circle(x, y - 1.6 * s, 0.15 * s, ink=b, w=3)


def xray(ctx, lt):
    img = lab_bg().copy()
    s = 250; cx, cy = 560, 1040 - 0.5 * s
    ph = lt * 2.0
    norm_sp = ant_sprite(s, 0, "stand", ph, lt)
    xr_sp = ant_sprite(s, 0, "stand", ph, lt, xray=True)
    scan = lerp(-60, W + 60, easeio(lt / 1.1))
    ox, oy = cx - norm_sp.width / 2, cy - norm_sp.height / 2
    cut = int(clamp01((scan - ox) / norm_sp.width) * norm_sp.width)
    if cut < norm_sp.width:
        A.paste(img, norm_sp.crop((cut, 0, norm_sp.width, norm_sp.height)), ox + cut, oy)
    if cut > 0:
        A.paste_c(img, A.glow(int(s * 1.3), (90, 200, 255), 70), cx - 0.2 * s, cy)
        A.paste(img, xr_sp.crop((0, 0, cut, xr_sp.height)), ox, oy)
    tarm = ctx.wt("armadura")
    if lt > tarm - 0.1:
        u = (lt - tarm + 0.1) / 0.7
        if u < 1:
            band = Image.new("RGBA", xr_sp.size); bd = ImageDraw.Draw(band)
            bx = lerp(-200, xr_sp.width + 200, u)
            bd.polygon([(bx, 0), (bx + 90, 0), (bx - 110, xr_sp.height), (bx - 200, xr_sp.height)], fill=(255, 255, 255, 200))
            band.putalpha(Image.fromarray(np.minimum(np.asarray(band.split()[3]), np.asarray(xr_sp.split()[3]))))
            A.paste(img, band, ox, oy)
    if 0 < scan < W:
        ss = SS(W, H, s=1)
        ss.rect(scan - 3, 0, scan + 3, H, fill=(200, 245, 255, 230))
        img.alpha_composite(ss.get())
        A.paste_c(img, A.glow(160, (120, 220, 255), 120), scan, cy)
    tesq = ctx.wt("esqueleto")
    q = ease((lt - tesq) / 0.35)
    if q > 0:
        ss = SS(W, H, s=2)
        ss.rrect(780, 560, 1020, 900, 24, fill=(10, 20, 44, int(220 * q)), ink=(120, 210, 255, int(200 * q)), w=3)
        human_xray(ss, 900, 800, 90)
        ss.text((900, 875), "POR DENTRO", 26, "mont-Black", fill=(200, 235, 255, int(255 * q)))
        ss.text((380, 640), "POR FORA", 52, "mont-Black", fill=(255, 222, 40, int(255 * q)), stroke=5)
        A.arrow(ss, 380, 680, 430, 760, (255, 222, 40, int(255 * q)), w=12, head=2.4, iw=3)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)), dy=-10 * lt)


# ======================================================================= cena 8: tamanho é destino
def lineup(ctx, lt):
    img = A.vgrad(W, H, [(0, (252, 240, 222)), (1, (238, 222, 200))])
    d = ImageDraw.Draw(img)
    for x in range(30, W, 60):
        for y in range(30, H, 60): d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(228, 210, 190))
    ss = SS(W, H, s=2)
    gy = 1010
    ss.rect(0, gy, W, gy + 8, fill=(120, 100, 90))
    tm = ctx.wt("camundongo"); th = ctx.wt("cavalo")
    # formiga + lupa
    ss.circle(175, gy - 175, 125, fill=(255, 255, 255), ink=INK, w=7)
    ant(ss, 175, gy - 175, 74, pose="walk", phase=lt * 9, t=lt)
    ss.line([(265, gy - 88), (318, gy - 12)], INK, 18)
    ant(ss, 318, gy - 4, 4, pose="walk", phase=lt * 9, t=lt)
    # camundongo
    qm = ease((lt - tm + 0.15) / 0.3)
    if qm > 0:
        hop = abs(math.sin((lt - tm) * 7)) * 40 * (lt > tm)
        run = 60 * easeio((lt - tm - 0.4) / 1.2)
        mouse(ss, 480 + run, gy - 0.32 * 150 - 6 - hop + (1 - qm) * 300, 150 * (0.6 + 0.4 * qm), t=lt)
    qh = ease((lt - th + 0.15) / 0.3)
    if qh > 0:
        horse(ss, 790, gy - 0.99 * 205 + (1 - qh) * 600, 205, t=lt)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)

    def badge(x, y, ok, q, txt):
        if q <= 0: return
        r = 50 * A.back(q)
        ss.circle(x, y, r, fill=(60, 190, 100) if ok else (230, 70, 70), ink=INK, w=5)
        if ok: ss.line([(x - r * 0.45, y), (x - r * 0.1, y + r * 0.35), (x + r * 0.5, y - r * 0.35)], (255, 255, 255), r * 0.2)
        else:
            ss.line([(x - r * 0.38, y - r * 0.38), (x + r * 0.38, y + r * 0.38)], (255, 255, 255), r * 0.2)
            ss.line([(x - r * 0.38, y + r * 0.38), (x + r * 0.38, y - r * 0.38)], (255, 255, 255), r * 0.2)
        ss.text((x, y + 82), txt, 30, "mont-Black", fill=INK)

    badge(175, 600, True, ease(lt / 0.3), "SAI ANDANDO")
    badge(500, 640, True, ease((lt - tm - 0.2) / 0.3), "LEVANTA E VAI")
    badge(860, 520, False, ease((lt - th - 0.15) / 0.3), "NÃO")
    for x, txt in ((175, "5 mm"), (500, "8 cm"), (860, "1,6 m")):
        ss.text((x, gy + 60), txt, 40, "anton", fill=(120, 100, 90))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 9: sai andando e sobe de volta (loop)
def walk_bg():
    def mk():
        im = A.vgrad(W, H + 1400, [(0, (255, 170, 120)), (0.5, (230, 150, 140)), (1, (120, 90, 120))])
        rng = np.random.default_rng(12)
        for _ in range(26):
            r = int(rng.uniform(30, 90)); g = A.glow(r, (255, int(rng.uniform(170, 230)), 120), int(rng.uniform(80, 170)))
            A.paste_c(im, g, rng.uniform(0, 760), rng.uniform(H - 300, H + 300))
        ss = SS(W, H + 1400, s=2)
        ss.rect(760, 0, W, H + 1400, fill=(120, 112, 130))
        for k in range(0, H + 1400, 230):
            ss.line([(760, k), (W, k)], (96, 88, 110), 4, cap=False)
        ss.rect(760, 0, 774, H + 1400, fill=(255, 190, 140))
        for _ in range(600):
            x, y = rng.uniform(780, W), rng.uniform(0, H + 1400)
            ss.circle(x, y, rng.uniform(1.5, 4), fill=(160, 150, 170, 160))
        gy = H + 1400 - 770
        for k in range(16):
            x = k * 72 - 20
            ss.oval(x + 36, gy + 40, 46, 34, 0, fill=(196, 184, 172), ink=INK, w=3)
        ss.rect(0, gy + 60, 760, H + 1400, fill=(150, 134, 126))
        im.alpha_composite(ss.get())
        return im
    return cached("walkbg", mk)


def walk(ctx, lt):
    dur = ctx.dur
    t_wall = ctx.beat_t(0, end=True) - 0.1
    t_whip = dur - 0.95; t_hold = dur - 0.32
    if lt >= t_hold:
        return ledge_frame(0.0, anim_t=lt)
    bg = walk_bg(); gy_scr = 1150
    s = 110
    climb = max(0.0, lt - t_wall)
    tilt = 0.0
    if lt < t_wall:
        x = lerp(120, 760 - 0.5 * s - 30, lt / t_wall); y = gy_scr - 0.47 * s; rot = 0
    else:
        x = 760 - 0.5 * s; y = gy_scr - 0.47 * s - 30 - 260 * climb; rot = -90 * ease(climb / 0.25)
        tilt = max(0.0, 260 * climb - 300)
    yoff = -(H + 1400 - H) + tilt
    img = Image.new("RGBA", (W, H)); A.paste(img, bg, 0, yoff)
    sp = ant_sprite(s, rot, "walk", phase=lt * 14, t=lt)
    A.paste_c(img, sp, x, y + tilt)
    if lt >= t_whip:
        u = easeio((lt - t_whip) / (t_hold - t_whip))
        top = ledge_frame(0.0, anim_t=lt)
        out = Image.new("RGBA", (W, H))
        A.paste(out, img, 0, u * H); A.paste(out, top, 0, -(1 - u) * H)
        return motion_blur_v(out, 160 * math.sin(math.pi * u))
    return img


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    """cenário do gancho (parapeito do 30º andar) sem a formiga"""
    return ledge_frame(cv.get("t", 0.4), show_ant=False)


def cover_sprite(cv):
    """formiga da capa com olho maior e brilhante (mais expressiva no tamanho de miniatura)"""
    s = cv.get("sprite_s", 400)
    sp = ant_sprite(s, 0.0, "walk", phase=0.6, t=0.3)
    half = sp.width / 2
    ss = SS(sp.width, sp.height, s=2)
    ex, ey, r = half + 0.635 * s, half - 0.155 * s, 0.125 * s
    ss.circle(ex, ey, r, fill=(22, 14, 20), ink=INK, w=max(2, s * 0.012))
    ss.circle(ex - r * 0.32, ey - r * 0.36, r * 0.36, fill=(255, 255, 255, 240))
    ss.circle(ex + r * 0.34, ey + r * 0.3, r * 0.14, fill=(255, 255, 255, 190))
    sp.alpha_composite(ss.get())
    return sp
