"""Dia 2A — "E se você fosse um mosquito atingido por uma gota de chuva?" (formato CURTO; paleta: tempestade
verde-azulada, folhas escuras, gotas ciano).

Cenas: rain (gancho: gota gigante descendo sobre o mosquito), vision (Visão do Bicho: gás carbônico do bafo humano
em verde, visto a mais de 10 m — van Breugel et al. 2015), drop (50x o meu peso, +30 km/h), ride (a gota quase não
freia e carrega o mosquito), gforce (300 G x 9 G do piloto), slip (pelos que repelem água), ground (perigo perto do
chão -> volta ao quadro inicial = loop).
Fatos: Dickerson et al. (2012), PNAS.
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached

BODY = (58, 52, 72); STRIPE = (236, 238, 244); LEG = (44, 40, 56); LEG_FAR = (96, 92, 110)
EYE = (92, 30, 52); EYE2 = (170, 60, 84)
DROP = (176, 226, 246); DROP_D = (96, 168, 206)
CO2 = (90, 255, 150)
GROUND_Y = 1660          # chão no quadro inicial (fora da área da legenda)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= mosquito (perfil, cabeça para a direita)
def _wing(ss, P, a_deg, alpha, iw):
    a = math.radians(a_deg); bx, by = 0.12, -0.07
    cx, cy = bx + 0.31 * math.cos(a), by + 0.31 * math.sin(a)
    ss.poly(P(A.ell_pts(cx, cy, 0.33, 0.075, a_deg, 30)), fill=(214, 238, 255, alpha), ink=(*INK, int(alpha * 1.3)), w=iw * 0.8)
    ss.line(P([(bx, by), (bx + 0.58 * math.cos(a), by + 0.58 * math.sin(a))]), (120, 150, 180, alpha), iw * 0.7, cap=False)


def mosquito(ss, x, y, s, t=0.0, rot=0.0, flip=1, flap=True, wet=0.0, spread=0.0, hairs=False):
    """(x,y) = tórax; corpo ~1,5 s do fim do abdome à ponta da tromba"""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.4, s * 0.011)
    ph = t * 47.0 if flap else 0.0
    _wing(ss, P, 205 + 30 * math.sin(ph + 0.6), 70, iw)
    legs = [((0.25, 0.09), (0.44, 0.24), (0.58, 0.62)), ((0.18, 0.10), (0.13, 0.33), (0.03, 0.68)),
            ((0.10, 0.09), (-0.16, 0.20), (-0.46, 0.52))]

    def leg(hip, knee, foot, col, k, off):
        sw = 0.025 * math.sin(t * 3.1 + k * 1.7)
        kx, ky = knee; fx, fy = foot
        fx += sw + spread * (0.18 if fx > hip[0] else -0.18); fy += sw * 0.5 - spread * 0.12
        pts = P([(hip[0] + off[0], hip[1] + off[1]), (kx + off[0], ky + off[1]), (fx + off[0], fy + off[1])])
        ss.line(pts, INK, s * 0.024 + 1.5 * iw); ss.line(pts, col, s * 0.024)
        for u in (0.35, 0.6, 0.85):
            bx, by = lerp(pts[1][0], pts[2][0], u), lerp(pts[1][1], pts[2][1], u)
            ss.circle(bx, by, s * 0.014, fill=STRIPE)
        if hairs:
            for u in (0.2, 0.5, 0.8):
                bx, by = lerp(pts[1][0], pts[2][0], u), lerp(pts[1][1], pts[2][1], u)
                ss.line([(bx, by), (bx + s * 0.03, by - s * 0.03)], (200, 210, 230), max(1, s * 0.006), cap=False)

    for k, (h, kn, f) in enumerate(legs): leg(h, kn, f, LEG_FAR, k, (-0.05, -0.03))
    # abdome listrado
    ss.poly(P(A.ell_pts(-0.28, 0.04, 0.34, 0.085, -8, 40)), fill=BODY, ink=INK, w=iw)
    for k in range(5):
        xx = -0.06 - k * 0.11; yy = 0.04 - (xx + 0.28) * 0.14
        ss.poly(P(A.ell_pts(xx, yy + 0.01, 0.016, 0.07 - 0.008 * k, -8, 14)), fill=STRIPE)
    ss.poly(P(A.ell_pts(-0.3, 0.0, 0.26, 0.025, -8, 20)), fill=(255, 255, 255, 50))
    # tórax com a "lira" branca
    ss.poly(P(A.ell_pts(0.18, -0.01, 0.17, 0.13, -12, 36)), fill=BODY, ink=INK, w=iw)
    ss.line(P(A.bez((0.11, -0.1), (0.16, -0.04), (0.2, -0.04), (0.25, -0.1), 10)), STRIPE, max(1.5, s * 0.012), cap=False)
    ss.line(P([(0.18, -0.12), (0.18, 0.05)]), STRIPE, max(1.2, s * 0.008), cap=False)
    for k, (h, kn, f) in enumerate(legs): leg(h, kn, f, LEG, k + 3, (0.0, 0.0))
    # tromba, palpos, antenas
    ss.line(P([(0.46, 0.08), (0.84, 0.25)]), INK, s * 0.024); ss.line(P([(0.80, 0.23), (0.85, 0.255)]), (200, 120, 130), s * 0.016)
    ss.line(P([(0.46, 0.07), (0.6, 0.15)]), (70, 66, 86), s * 0.03)
    for ax, ay, tx, ty in ((0.46, -0.03, 0.64, -0.23), (0.44, -0.04, 0.55, -0.27)):
        ss.line(P([(ax, ay), (tx, ty)]), INK, max(1.5, s * 0.012), cap=False)
        for u in (0.25, 0.45, 0.65, 0.85):
            px, py = lerp(ax, tx, u), lerp(ay, ty, u)
            ss.line(P([(px - 0.03, py - 0.005), (px + 0.03, py + 0.01)]), INK, max(1, s * 0.006), cap=False)
    # cabeça e olho grande
    ss.poly(P(A.ell_pts(0.4, 0.04, 0.09, 0.085, 0, 24)), fill=BODY, ink=INK, w=iw)
    ex, ey = P([(0.418, 0.025)])[0]; er = s * 0.074
    ss.circle(ex, ey, er, fill=EYE, ink=INK, w=iw)
    ss.circle(ex + er * 0.12 * flip, ey + er * 0.12, er * 0.62, fill=EYE2)
    ss.circle(ex + er * 0.2 * flip, ey + er * 0.18, er * 0.36, fill=(40, 14, 26))
    ss.circle(ex - er * 0.3 * flip, ey - er * 0.35, er * 0.26, fill=(255, 255, 255, 235))
    ss.circle(ex + er * 0.35 * flip, ey + er * 0.4, er * 0.1, fill=(255, 255, 255, 180))
    if wet > 0:
        for (dx, dy, r) in ((-0.2, -0.06, 0.03), (-0.42, 0.0, 0.025), (0.15, -0.13, 0.025), (0.0, 0.1, 0.02)):
            px, py = P([(dx, dy)])[0]
            ss.circle(px, py, s * r * wet, fill=(200, 240, 255, 220), ink=(*INK, 120), w=1)
            ss.circle(px - s * r * 0.3, py - s * r * 0.3, s * r * 0.3 * wet, fill=(255, 255, 255, 230))
    _wing(ss, P, 198 + 34 * math.sin(ph), 105, iw)


def mini_sprite():
    def mk():
        s = 56; ss = SS(int(1.7 * s), int(1.15 * s), s=2)
        mosquito(ss, 0.8 * s, 0.42 * s, s, t=0.3)
        return ss.get()
    return cached("mini", mk)


# ======================================================================= gota de chuva
def raindrop(ss, cx, cy, r, t=0.0, a=225, wob=1.0):
    sx = 1 + 0.035 * math.sin(t * 9) * wob; sy = 1 / sx
    base = [(0, -1.5), (0.5, -0.78), (0.96, 0.05), (0.72, 0.74), (0, 1.0), (-0.72, 0.74), (-0.96, 0.05), (-0.5, -0.78)]
    pts = A.spline([(cx + px * r * sx, cy + py * r * sy) for px, py in base], 8)
    ss.poly(pts, fill=(*DROP, a), ink=(*INK, min(255, a + 20)), w=max(2, r * 0.025))
    ss.poly(A.spline([(cx + px * r * 0.8 * sx, cy + 0.12 * r + py * r * 0.72 * sy) for px, py in base[2:7]] + [(cx, cy + 0.05 * r)], 6),
            fill=(*DROP_D, int(a * 0.55)))
    ss.oval(cx - 0.42 * r, cy - 0.25 * r, 0.16 * r, 0.32 * r, 25, fill=(255, 255, 255, int(a * 0.9)))
    ss.circle(cx - 0.18 * r, cy - 0.62 * r, 0.07 * r, fill=(255, 255, 255, int(a * 0.8)))


# ======================================================================= cenário: tempestade
def sky_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (30, 52, 72)), (0.5, (70, 106, 122)), (1, (48, 86, 84))])
        from scenes.common import cloud
        for k, (x, y, w) in enumerate(((180, 60, 900), (760, 0, 1000), (420, 260, 800))):
            c = cloud(w, int(w * 0.6), seed=k + 2, col=(22, 36, 52), a=170, blur=26)
            A.paste_c(im, c, x, y + 120)
        A.paste_c(im, A.glow(700, (150, 210, 220), 70), 540, 900)
        return im
    return cached("sky", mk)


def leaves_layer():
    """folhas grandes nas bordas (silhueta), dão a escala de inseto"""
    def mk():
        ss = SS(W, H, s=2)
        for (bx, by, L, ang, col) in ((-60, 760, 520, -18, (22, 62, 52)), (-40, 1180, 460, 12, (28, 74, 58)),
                                      (1140, 620, 560, 200, (20, 58, 50)), (1130, 1050, 470, 165, (26, 70, 56))):
            a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux
            tip = (bx + ux * L, by + uy * L)
            pts = A.bez((bx, by), (bx + ux * L * 0.3 + px * L * 0.28, by + uy * L * 0.3 + py * L * 0.28),
                        (bx + ux * L * 0.75 + px * L * 0.18, by + uy * L * 0.75 + py * L * 0.18), tip, 16)
            pts2 = A.bez(tip, (bx + ux * L * 0.75 - px * L * 0.18, by + uy * L * 0.75 - py * L * 0.18),
                         (bx + ux * L * 0.3 - px * L * 0.28, by + uy * L * 0.3 - py * L * 0.28), (bx, by), 16)
            ss.poly(pts + pts2, fill=col, ink=(12, 30, 28), w=4)
            ss.line([(bx, by), tip], (60, 120, 90), 5)
            for k in range(1, 6):
                u = k / 6; mx, my = bx + ux * L * u, by + uy * L * u
                for sg in (-1, 1):
                    ss.line([(mx, my), (mx + (ux * 0.5 + px * sg) * L * 0.12, my + (uy * 0.5 + py * sg) * L * 0.12)], (50, 104, 80), 3)
            for k in range(4):
                u = 0.3 + 0.15 * k
                ss.circle(bx + ux * L * u + px * 30, by + uy * L * u + py * 30, 9, fill=(190, 230, 245, 200), ink=(12, 30, 28, 160), w=2)
        return ss.get()
    return cached("leaves", mk)


def grass_strip():
    def mk():
        ss = SS(W, 900, s=2); rng = np.random.default_rng(5)
        ss.rect(0, 120, W, 900, fill=(30, 72, 52))
        ss.ellipse(700, 330, 300, 70, fill=(40, 70, 90), ink=(14, 34, 32), w=4)
        ss.ellipse(660, 315, 180, 30, fill=(120, 170, 190, 120))
        for _ in range(170):
            x = rng.uniform(-20, W + 20); h = rng.uniform(60, 180); lean = rng.uniform(-40, 40)
            if 420 < x < 980 and h < 120: continue
            col = mixc((36, 96, 62), (70, 140, 80), rng.random())
            ss.poly([(x - 9, 150), (x + lean, 150 - h), (x + 9, 150)], fill=col, ink=(14, 34, 28), w=2)
        return ss.get()
    return cached("grass", mk)


def streaks(img, t, n=70, seed=3, speed=1.0, alpha=150, length=90, up=False):
    rng = np.random.default_rng(seed); ss = SS(W, H, s=1)
    for k in range(n):
        x0, y0 = rng.uniform(-100, W + 100), rng.uniform(0, 2100)
        ksp = rng.integers(1, 3)
        y = (y0 + (-1 if up else 1) * ksp * 1500 * speed * t) % 2100 - 100
        x = x0 - 0.18 * y * 0.3
        L = length * (0.6 + 0.5 * ksp)
        ss.line([(x, y), (x - 0.18 * L, y + L)], (200, 230, 245, int(alpha * rng.uniform(0.5, 1))), rng.uniform(2, 4.5), cap=False)
    img.alpha_composite(ss.get())


def ripples(img, t, gy):
    ss = SS(W, H, s=1)
    for k in range(3):
        u = (t * 0.8 + k / 3) % 1.0
        ss.ellipse(700 + 60 * (k - 1), gy + 210, 40 + 200 * u, 10 + 46 * u, ink=(200, 235, 245, int(160 * (1 - u))), w=3)
    img.alpha_composite(ss.get())


def drop_y_at(t):
    return 470 + 60 * t


def rain_frame(t, gy=GROUND_Y, drop_y=None, mos_y=None, danger=0.0, drop=True):
    img = sky_bg().copy()
    streaks(img, t, 40, 7, 0.7, 90, 60)
    img.alpha_composite(leaves_layer())
    A.paste(img, grass_strip(), 0, gy - 150)
    ripples(img, t, gy)
    streaks(img, t, 50, 3, 1.0, 150, 100)
    ss = SS(W, H, s=2)
    dy = drop_y_at(t) if drop_y is None else drop_y
    if drop:
        for k in range(7):
            xx = 540 + (k - 3) * 52
            ss.line([(xx, dy - 330 - 40 * (k % 2)), (xx, dy - 470 - 60 * (k % 3))], (230, 245, 255, 150), 5)
        raindrop(ss, 540, dy, 190, t)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    my = (1010 + 12 * math.sin(t * 3.0)) if mos_y is None else mos_y + 12 * math.sin(t * 3.0)
    mosquito(ss, 520, my, 300, t=t, rot=-12, flip=1)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 18, 0.35)
    A.paste(img, sh, -pad + 14, -pad + 30)
    img.alpha_composite(sp)
    if danger > 0:
        img.alpha_composite(A.rgrad(1100, [(0, (255, 40, 40, 0)), (0.6, (255, 40, 40, int(40 * danger))), (1, (180, 0, 0, int(150 * danger)))],
                                    w=W, h=H, cx=540, cy=1000))
    return img


# ======================================================================= cena 1: gancho
def rain(ctx, lt):
    return A.cam(rain_frame(lt), zoom=1.02 + 0.01 * math.sin(lt * 1.3), rot=0.3 * math.sin(lt * 0.9))


# ======================================================================= cena 2: Visão do Bicho (gás carbônico)
def person_layer():
    def mk():
        ss = SS(W, H, s=2)
        prof = [(1120, 420), (980, 430), (900, 500), (870, 600), (860, 690), (820, 760), (845, 790), (850, 820),
                (835, 845), (850, 870), (850, 920), (880, 960), (950, 980), (960, 1080), (1120, 1120)]
        ss.poly(A.spline(prof, 6), fill=(26, 40, 52), ink=(12, 20, 28), w=4)
        ss.circle(925, 640, 16, fill=(60, 80, 96))
        return ss.get()
    return cached("person", mk)


def plume_pts(lt, n=26):
    out = []
    for i in range(n):
        u = (i / n + lt * 0.22) % 1.0
        x = lerp(830, 540, u) + 70 * math.sin(u * 7 + i) * u
        y = lerp(850, 1560, u ** 1.15) + 40 * math.sin(u * 5 + i * 0.7)
        out.append((x, y, 30 + 120 * u, u))
    return out


def pov_antennae(img, t):
    ss = SS(W, 560, s=2)
    for side in (-1, 1):
        bx, by = 540 + side * 170, 600
        tx, ty = 540 + side * 330 + 14 * math.sin(t * 2 + side), 90 + 10 * math.sin(t * 2.6 + side)
        ss.line([(bx, by), (tx, ty)], INK, 20); ss.line([(bx, by), (tx, ty)], (70, 66, 88), 12)
        for k in range(1, 9):
            u = k / 9; px, py = lerp(bx, tx, u), lerp(by, ty, u)
            ss.line([(px - 40 * (1 - u * 0.5), py + 8), (px + 40 * (1 - u * 0.5), py - 8)], INK, 5)
    ss.line([(540, 620), (540, 260)], INK, 30); ss.line([(540, 620), (540, 260)], (70, 66, 88), 20)
    ss.circle(540, 262, 12, fill=(200, 120, 130), ink=INK, w=3)
    img.alpha_composite(ss.get(), (0, H - 560))


def vision(ctx, lt):
    base = sky_bg().copy()
    streaks(base, lt, 40, 7, 0.25, 90, 60)
    base.alpha_composite(leaves_layer())
    base.alpha_composite(person_layer())
    streaks(base, lt, 40, 3, 0.35, 140, 90)
    wide = ctx.sc["id"] == "vision2"
    u = 1.0 if wide else ease((lt - 0.25) / 0.7)
    if u > 0:
        rgb = np.asarray(base.convert("RGB"), dtype=np.float32)
        g = rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
        dark = np.stack([g * 0.18, g * 0.26, g * 0.42], axis=2) + np.array([6, 10, 22], np.float32)
        out = rgb * (1 - u) + dark * u
        base = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).convert("RGBA")
    for (x, y, r, v) in plume_pts(lt):
        a = int((60 + 170 * u) * math.sin(math.pi * v) ** 0.6)
        A.paste_c(base, A.glow(int(r), CO2, a), x, y)
    ss = SS(W, H, s=2)
    for k in range(3):
        w_ = ((lt * 0.9 + k / 3) % 1.0)
        ss.ellipse(830, 850, 30 + 120 * w_, 22 + 90 * w_, ink=(*CO2, int(200 * (1 - w_) * u)), w=5)
    t10 = ctx.wt("10", default=99.0)
    q = ease((lt - t10 + 0.1) / 0.4)
    if q > 0:
        for k in range(12):
            f0, f1 = k / 12, (k + 0.5) / 12
            if f1 > q: break
            ss.line([(lerp(540, 820, f0), lerp(1500, 860, f0)), (lerp(540, 820, f1), lerp(1500, 860, f1))], (255, 255, 255, 230), 7)
        ss.text((610, 980), "10 m", 70, "anton", fill=(255, 255, 255, int(255 * q)), stroke=6)
    base.alpha_composite(ss.get())
    pov_antennae(base, lt)
    if wide:   # segunda tomada: câmera abre e sobe pelo rastro até a boca
        z = lerp(1.18, 1.0, easeio(lt / max(1, ctx.dur)))
        return A.cam(base, zoom=z, dx=lerp(-120, 0, easeio(lt / max(1, ctx.dur))), dy=lerp(160, 0, easeio(lt / max(1, ctx.dur))))
    return A.cam(base, zoom=1.03 + 0.02 * math.sin(lt * 0.8), dx=10 * math.sin(lt * 1.7), dy=8 * math.sin(lt * 2.3))


# ======================================================================= cena 3: 50x o meu peso, +30 km/h
def drop(ctx, lt):
    t30 = ctx.wt("30", default=ctx.dur * 0.8)
    fast = clamp01((lt - t30 + 0.2) / 0.5)
    img = sky_bg().copy()
    streaks(img, lt, 40, 7, 0.7 + 0.8 * fast, 90, 60)
    img.alpha_composite(leaves_layer())
    streaks(img, lt, 50, 3, 1.0 + 1.2 * fast, 150, 100 + 80 * fast)
    ss = SS(W, H, s=2)
    dy = lerp(560, 760, easeio(lt / max(1, ctx.dur))) + 60 * fast * (lt - t30)
    for k in range(9):
        xx = 330 + (k - 4) * 46; L = 160 + 220 * fast
        ss.line([(xx, dy - 300), (xx, dy - 300 - L - 40 * (k % 3))], (230, 245, 255, 170), 6)
    raindrop(ss, 330, dy, 200, lt)
    img.alpha_composite(ss.get())
    t50 = ctx.wt("50")
    k_on = int(clamp01((lt - t50 + 0.1) / 0.9) * 50)
    mini = mini_sprite()
    for k in range(k_on):
        c, r = k % 5, k // 5
        A.paste_c(img, mini, 650 + c * 82, 520 + r * 50 - 5 * math.sin(lt * 4 + k))
    if k_on > 0:
        ss = SS(W, H, s=2)
        ss.text((818, 1040), "= 50 de mim", 54, "anton", fill=(255, 255, 255), stroke=6)
        img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    mosquito(ss, 790, 1480 + 10 * math.sin(lt * 3), 170, t=lt, rot=-6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)), dx=6 * fast * math.sin(lt * 31))


# ======================================================================= cena 3b: velocímetro (+30 km/h)
def speed(ctx, lt):
    img = A.vgrad(W, H, [(0, (26, 50, 70)), (1, (52, 92, 104))])
    streaks(img, lt, 90, 9, 2.6, 190, 260)
    t30 = ctx.wt("30", default=0.6)
    v = 34 * ease((lt - t30 + 0.5) / 0.9)
    ss = SS(W, H, s=2)
    for k in range(11):
        xx = 540 + (k - 5) * 60
        ss.line([(xx, 380), (xx, 380 - 300 - 80 * (k % 3))], (230, 245, 255, 170), 7)
    raindrop(ss, 540, 700 + 8 * math.sin(lt * 20), 260, lt * 2)
    gx, gy, R = 540, 1560, 230
    ss.ellipse(gx, gy, R + 18, R + 18, fill=(14, 24, 34, 230), ink=INK, w=6)
    for k in range(9):
        a = math.radians(200 + k * 17.5)
        ss.line([(gx + math.cos(a) * (R - 40), gy + math.sin(a) * (R - 40)), (gx + math.cos(a) * R, gy + math.sin(a) * R)], (220, 235, 245), 6)
    a = math.radians(200 + 140 * v / 40)
    ss.line([(gx, gy), (gx + math.cos(a) * (R - 30), gy + math.sin(a) * (R - 30))], (255, 90, 70), 14)
    ss.circle(gx, gy, 22, fill=(255, 90, 70), ink=INK, w=4)
    ss.text((gx, gy + 110), f"{int(v)} km/h", 70, "anton", fill=(255, 222, 40), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.04, dx=5 * math.sin(lt * 33), dy=4 * math.cos(lt * 29))


# ======================================================================= cena 4: a gota me carrega
def ride(ctx, lt):
    img = sky_bg().copy()
    streaks(img, lt, 40, 7, 0.9, 110, 140, up=True)
    lv = leaves_layer()
    off = (lt * 900) % 1900
    A.paste(img, lv, 0, -off); A.paste(img, lv, 0, 1900 - off)
    streaks(img, lt, 40, 3, 1.4, 170, 200, up=True)
    hit = clamp01(lt / 0.35)
    ss = SS(W, H, s=2)
    cx, cy = 540, 720
    if lt < 0.6:
        for k in range(10):
            a = math.radians(20 + k * 14); r = 240 + 260 * ease(lt / 0.6)
            ss.circle(cx + math.cos(a) * r * 1.1 - 120, cy + 230 + math.sin(a) * r * 0.25, 12 * (1 - lt / 0.6) + 2, fill=(220, 245, 255, 220))
    raindrop(ss, cx, cy, 230, lt * 2, wob=2.0 - hit)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    mosquito(ss, 560, 990, 220, t=lt, rot=-28, flip=1, flap=False, spread=0.6, wet=1.0)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    tf = ctx.wt("freia")
    q = ease((lt - tf + 0.2) / 0.4)
    if q > 0:
        A.arrow(ss, 880, 560, 880, 560 + 540 * q, (120, 230, 255), w=44, iw=5)
        A.arrow(ss, 210, 560, 210, 560 + 525 * q, (120, 230, 255, 200), w=44, iw=5)
        ss.text((210, 500), "antes", 44, "anton", fill=(255, 255, 255, int(255 * q)), stroke=5)
        ss.text((880, 500), "depois", 44, "anton", fill=(255, 255, 255, int(255 * q)), stroke=5)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03, dx=8 * math.sin(lt * 19) * (1 - hit), rot=0.6 * math.sin(lt * 1.4))


# ======================================================================= cena 5: 300 G x 9 G
def jet(ss, x, y, s, col=(210, 220, 235)):
    pts = [(-1, 0.05), (-0.75, -0.12), (0.5, -0.1), (1.0, 0.0), (0.5, 0.1), (-0.75, 0.12)]
    wing = [(0.1, 0.0), (-0.35, -0.55), (-0.5, -0.55), (-0.25, 0.0), (-0.5, 0.55), (-0.35, 0.55)]
    tail = [(-0.7, 0), (-0.95, -0.35), (-1.02, -0.35), (-0.92, 0)]
    for p in (wing, pts, tail): ss.poly(A.xf(p, x, y, s), fill=col, ink=INK, w=4)
    ss.poly(A.xf(A.ell_pts(0.45, -0.05, 0.16, 0.05, 0, 16), x, y, s), fill=(80, 150, 210), ink=INK, w=3)


def gforce(ctx, lt):
    img = A.vgrad(W, H, [(0, (16, 34, 50)), (1, (24, 60, 66))])
    t3 = ctx.wt("300"); tp = ctx.wt("piloto")
    q3 = ease((lt - t3 + 0.1) / 0.8); qp = ease((lt - tp) / 0.4)
    A.paste_c(img, A.glow(600, (60, 200, 230), int(40 + 80 * q3)), 540, 1050)
    ss = SS(W, H, s=2)
    for k in range(18):
        a = k * math.pi / 9 + lt * 0.2
        ss.line([(540 + math.cos(a) * 200, 1500 + math.sin(a) * 200), (540 + math.cos(a) * 900, 1500 + math.sin(a) * 900)],
                (80, 200, 230, int(40 * q3)), 30, cap=False)
    x0, x1 = 250, 1000
    ss.rrect(x0, 560, x1, 640, 18, fill=(10, 20, 30, 180), ink=(*INK, 200), w=4)
    ss.rrect(x0, 560, x0 + max(36, (x1 - x0) * q3), 640, 18, fill=(255, 222, 40), ink=INK, w=4)
    ss.text((x0 + max(36, (x1 - x0) * q3) - 70, 600), f"{int(300 * q3)}", 54, "anton", fill=INK)
    ss.rrect(x0, 760, x1, 840, 18, fill=(10, 20, 30, 180), ink=(*INK, 200), w=4)
    if qp > 0:
        ss.rrect(x0, 760, x0 + 36 * qp + 1, 840, 14, fill=(255, 120, 90), ink=INK, w=4)
        ss.text((x0 + 90, 800), "9", 60, "anton", fill=(255, 255, 255, int(255 * qp)), stroke=5)
    jet(ss, 140, 800, 85)
    img.alpha_composite(ss.get())
    A.paste_c(img, mini_sprite().resize((130, 88), Image.LANCZOS), 140, 600)
    ss = SS(W, H, s=2)
    sq = 1 - 0.18 * q3 * (0.5 + 0.5 * math.sin(lt * 26))
    mosquito(ss, 520, 1500, 320 * sq, t=lt, rot=-8 + 6 * q3 * math.sin(lt * 23), flap=True)
    img.alpha_composite(ss.get())
    sh = 12 * q3 * clamp01(1.2 - (lt - t3)) + 3
    return A.cam(img, dx=sh * math.sin(lt * 41), dy=sh * 0.6 * math.cos(lt * 37))


# ======================================================================= cena 6: pelos repelem água
def slip(ctx, lt):
    img = A.vgrad(W, H, [(0, (40, 78, 96)), (1, (30, 66, 70))])
    A.paste_c(img, A.glow(700, (160, 220, 235), 90), 300, 800)
    ss = SS(W, H, s=2)
    ss.circle(180, 820, 470, fill=(*DROP, 200), ink=INK, w=6)
    ss.circle(120, 760, 380, fill=(210, 240, 252, 120))
    ss.oval(-20, 520, 70, 170, 25, fill=(255, 255, 255, 200))
    img.alpha_composite(ss.get())
    te = ctx.wt("escorrego", default=ctx.dur * 0.5)
    u = easeio((lt - te + 0.4) / 1.2)
    mx = lerp(560, 840, u); my = lerp(900, 760, u)
    ss = SS(W, H, s=2)
    mosquito(ss, mx, my, 330, t=lt, rot=lerp(-30, -10, u), flap=u > 0.6, hairs=True, wet=1.0 - 0.7 * u)
    for k in range(10):
        a = k * 0.6 + lt * 2
        bx = mx - 120 + 60 * math.cos(a) * 1.5; by = my + 40 + 40 * math.sin(a)
        ss.circle(bx, by, 9, fill=(235, 250, 255, 200), ink=(*INK, 120), w=1.5)
    for k in range(5):
        v = (lt * 0.9 + k / 5) % 1.0
        ss.circle(mx + 60 + k * 30, my + 220 + v * 500, 14 * (1 - v) + 4, fill=(*DROP, int(220 * (1 - v))), ink=(*INK, int(150 * (1 - v))), w=2)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.04 - 0.03 * u, rot=0.4 * math.sin(lt))


# ======================================================================= cena 7: perigo perto do chão -> loop
def ground(ctx, lt):
    tpay = ctx.beat_t(1)
    voice_end = ctx.beat_t(1, end=True)
    tr = rain_t = lt - ctx.dur + 1 / 30.0          # termina exatamente em t = 0 do gancho
    down = easeio(lt / 1.0)
    back = easeio((lt - voice_end - 0.02) / max(0.2, ctx.dur - voice_end - 0.06))
    gy = lerp(lerp(GROUND_Y, 1185, down), GROUND_Y, back)
    my = lerp(lerp(1010, 1030, down), 1010, back)
    dy = lerp(lerp(drop_y_at(rain_t), 640, down), drop_y_at(rain_t), back)
    danger = clamp01((lt - tpay) / 0.25) * (1 - back) * (0.7 + 0.3 * math.sin(lt * 9))
    img = rain_frame(tr, gy=gy, drop_y=dy, mos_y=my, danger=danger)
    return A.cam(img, zoom=lerp(1.0 + 0.06 * down, 1.02, back) + 0.01 * math.sin(tr * 1.3) * back,
                 rot=0.3 * math.sin(tr * 0.9) * back)


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    img = sky_bg().copy()
    streaks(img, 0.4, 40, 7, 0.7, 90, 60)
    img.alpha_composite(leaves_layer())
    A.paste(img, grass_strip(), 0, GROUND_Y - 150)
    streaks(img, 0.4, 50, 3, 1.0, 150, 100)
    ss = SS(W, H, s=2)
    for k in range(7):
        xx = 560 + (k - 3) * 44
        ss.line([(xx, 640 - 40 * (k % 2)), (xx, 520 - 60 * (k % 3))], (230, 245, 255, 170), 6)
    raindrop(ss, 560, 860, 165, 0.0)
    img.alpha_composite(ss.get())
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 360)
    ss = SS(int(1.75 * s), int(1.2 * s), s=2)
    mosquito(ss, 0.82 * s, 0.45 * s, s, t=0.21)
    return ss.get()
