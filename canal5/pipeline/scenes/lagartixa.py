"""Dia 1B — "E se você fosse uma lagartixa atrás da geladeira?" (paleta: cozinha à noite, laranja quente x azul frio).

Cenas: behind (gancho), heatmove, pipes, evap, sweat, vision (Visão do Bicho: cores no escuro — lagartixas
noturnas enxergam cores com pouquíssima luz; Roth & Kelber 2004), compress, condenser, icecream (payoff -> volta
para trás da geladeira = loop).
Corte raio-X: azul = frio, vermelho = quente.
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached, motion_blur_v

GK = dict(skin=(236, 208, 190), spot=(190, 146, 132), belly=(250, 232, 218), far=(206, 176, 160), iris=(216, 192, 120))
COLD = (80, 170, 255); HOT = (255, 82, 60); LIQ = (160, 228, 255); GLOW = (255, 140, 50)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= lagartixa
def gecko(ss, x, y, s, flip=-1, t=0.0, blink=0.0, relax=0.0, tail_amp=1.0, walk=0.0):
    """lagartixa de perfil; (x,y) = centro do corpo; pés em y + 0,32 s. flip=-1 -> cabeça para a esquerda"""
    P = lambda pts: A.xf(pts, x, y, s, 0, flip)
    iw = max(1.4, s * 0.016)
    sway = math.sin(t * 2.3) * 0.13 * tail_amp
    curl = relax * 0.35
    cl = [(-0.48, 0.03), (-0.85, 0.07 + sway * 0.3), (-1.25, 0.12 + sway * 0.7 - curl * 0.3),
          (-1.6, 0.10 + sway - curl * 0.9), (-1.92, 0.02 + sway * 1.25 - curl * 1.6)]
    c = A.spline(cl, 7, closed=False)
    n = len(c); L, R = [], []
    for i, (px, py) in enumerate(c):
        qx, qy = c[min(i + 1, n - 1)]; ox, oy = c[max(i - 1, 0)]
        dx, dy = qx - ox, qy - oy; ln = math.hypot(dx, dy) or 1
        nx, ny = -dy / ln, dx / ln
        wdt = lerp(0.14, 0.012, (i / (n - 1)) ** 0.9)
        L.append((px + nx * wdt, py + ny * wdt)); R.append((px - nx * wdt, py - ny * wdt))
    tail = L + R[::-1]

    def leg(hip, foot, far, ph):
        hx, hy = hip; fx, fy = foot
        lift = max(0.0, math.sin(ph)) * 0.06 * walk
        fx += math.cos(ph) * 0.06 * walk; fy -= lift
        ex, ey = (hx + fx) / 2 + (0.07 if fx > hx else -0.07), min(hy, fy) - 0.06
        col = GK["far"] if far else GK["skin"]
        pts = P([(hx, hy), (ex, ey), (fx, fy)])
        ss.line(pts, INK, s * 0.075 + 2 * iw); ss.line(pts, col, s * 0.075)
        for a in (-62, -24, 14, 52):
            ang = math.radians(a + (180 if fx < hx else 0))
            tx, ty = fx + 0.1 * math.cos(ang) * (1 if fx >= hx else 1), fy + 0.02 * math.sin(ang)
            q = P([(fx, fy), (fx + 0.11 * math.cos(math.radians(a)) * (1 if fx >= hx else -1), fy + 0.015)])
            ss.line(q, INK, s * 0.028 + 2 * iw); ss.line(q, col, s * 0.028)
            ss.circle(q[1][0], q[1][1], s * 0.03, fill=col, ink=INK, w=iw)

    ph = t * 9
    leg((0.36, 0.1), (0.30, 0.32), True, ph + math.pi)
    leg((-0.40, 0.1), (-0.55, 0.32), True, ph)
    ss.poly(P(tail), fill=GK["skin"], ink=INK, w=iw)
    for k, u in enumerate((0.2, 0.42, 0.62, 0.8)):
        i = int(u * (n - 1)); px, py = c[i]
        ss.poly(P(A.ell_pts(px, py - 0.03, lerp(0.06, 0.02, u), lerp(0.035, 0.012, u), 0, 14)), fill=GK["spot"])
    ss.poly(P(A.ell_pts(0.0, 0.0, 0.62, 0.21, 0, 44)), fill=GK["skin"], ink=INK, w=iw)
    ss.poly(P(A.ell_pts(0.0, 0.1, 0.5, 0.07, 0, 30)), fill=GK["belly"])
    for (sx, sy, r) in ((-0.3, -0.08, 0.07), (0.0, -0.11, 0.08), (0.28, -0.08, 0.06), (-0.12, -0.02, 0.04), (0.16, -0.03, 0.04)):
        ss.poly(P(A.ell_pts(sx, sy, r, r * 0.6, 0, 16)), fill=GK["spot"])
    thr = 1 + 0.15 * math.sin(t * 7)
    ss.poly(P(A.ell_pts(0.74, 0.08, 0.16 * thr, 0.07 * thr, 0, 20)), fill=GK["belly"], ink=INK, w=iw)
    head = A.spline([(0.5, -0.13), (0.78, -0.2), (1.02, -0.14), (1.17, -0.01), (1.04, 0.08), (0.74, 0.11), (0.52, 0.1)], 6)
    ss.poly(P(head), fill=GK["skin"], ink=INK, w=iw)
    ss.poly(P(A.ell_pts(0.8, -0.15, 0.14, 0.035, -8, 16)), fill=(250, 232, 220, 200))
    mouth = A.bez((1.13, 0.02), (1.0, 0.07 + 0.03 * relax), (0.88, 0.06 + 0.02 * relax), (0.8, 0.03 - 0.02 * relax), 10)
    ss.line(P(mouth), INK, max(1.5, s * 0.014), cap=False)
    nx, ny = P([(1.1, -0.07)])[0]; ss.circle(nx, ny, s * 0.012, fill=INK)
    ex, ey = P([(0.86, -0.08)])[0]; er = s * 0.088
    ss.circle(ex, ey, er, fill=GK["iris"], ink=INK, w=iw)
    ss.ellipse(ex, ey, er * 0.16, er * 0.82, fill=(26, 18, 22))
    ss.circle(ex - er * 0.35 * flip, ey - er * 0.4, er * 0.22, fill=(255, 255, 255, 220))
    bl = max(blink, relax * 0.55)
    if bl > 0.02:
        lid = A.ell_pts(ex, ey - er + er * bl, er * 1.08, er * bl, 0, 24, 0, 2 * math.pi)
        ss.poly([p for p in lid], fill=GK["skin"], ink=INK, w=iw)
    leg((0.38, 0.12), (0.55, 0.32), False, ph)
    leg((-0.38, 0.12), (-0.25, 0.32), False, ph + math.pi)


def blink_at(t, times=(1.3, 3.9), d=0.18):
    for b in times:
        if b <= t <= b + d: return math.sin(math.pi * (t - b) / d)
    return 0.0


# ======================================================================= cena 1: atrás da geladeira (gancho e loop)
def behind_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (38, 30, 40)), (0.6, (70, 44, 40)), (1, (40, 30, 34))])
        ss = SS(W, H, s=2)
        ss.rect(0, 0, W, 1300, fill=(46, 42, 50))
        rows = list(range(120, 1260, 92))
        for k, y in enumerate(rows):
            ss.line([(-40, y), (W + 40, y)], (24, 22, 28), 30, cap=False)
            ss.line([(-40, y - 9), (W + 40, y - 9)], (255, 150, 70, 150), 5, cap=False)
            ss.line([(-40, y + 10), (W + 40, y + 10)], (10, 8, 12, 160), 4, cap=False)
        for x in range(10, W, 22):
            ss.line([(x, 90), (x, 1270)], (30, 28, 34), 5, cap=False)
            ss.line([(x - 2, 90), (x - 2, 1270)], (255, 160, 90, 70), 1.5, cap=False)
        for k, y in enumerate(rows[:-1]):
            sx = -10 if k % 2 == 0 else W + 10
            ss.ellipse(sx, y + 46, 50, 46, ink=(24, 22, 28), w=30)
        im.alpha_composite(ss.get())
        fl = A.vgrad(W, H - 1290, [(0, (150, 112, 90)), (1, (64, 48, 46))])
        im.alpha_composite(fl, (0, 1290))
        d = ImageDraw.Draw(im)
        for k in range(-8, 9):
            d.line([(540 + k * 60, 1290), (540 + k * 260, H)], fill=(110, 82, 70), width=3)
        for y in (1330, 1420, 1560, 1760):
            d.line([(0, y), (W, y)], fill=(110, 82, 70), width=3)
        A.paste_c(im, A.glow(700, GLOW, 120), 540, 900)
        A.paste_c(im, A.glow(500, (255, 170, 90), 90), 540, 1300)
        ss = SS(W, H, s=2); rng = np.random.default_rng(4)
        for (cx, cy, r) in ((140, 1420, 60), (930, 1380, 45), (300, 1650, 38)):
            for _ in range(30):
                a = rng.uniform(0, 2 * math.pi); rr = r * rng.uniform(0.3, 1)
                ss.circle(cx + math.cos(a) * rr, cy + math.sin(a) * rr * 0.6, rng.uniform(6, 14), fill=(150, 140, 140, 150))
        im.alpha_composite(ss.get())
        return im
    return cached("behind_bg", mk)


def shimmer(img, t, amp=3.0, y0=0, y1=1300):
    a = np.asarray(img).copy()
    ys = np.arange(y0, y1)
    off = (amp * np.sin(ys * 0.035 + t * 5.0) + amp * 0.5 * np.sin(ys * 0.09 - t * 7.0)).astype(int)
    idx = (np.arange(W)[None, :] - off[:, None]) % W
    a[y0:y1] = np.take_along_axis(a[y0:y1], idx[..., None].repeat(4, axis=2), axis=1)
    return Image.fromarray(a, "RGBA")


def motes(img, t, n=24, seed=1, col=(255, 200, 140)):
    rng = np.random.default_rng(seed); ss = SS(W, H, s=1)
    for k in range(n):
        x0, y0, sp, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(30, 90), rng.uniform(2, 5)
        y = (y0 - t * sp) % H; x = x0 + 20 * math.sin(t * 0.8 + k)
        ss.circle(x, y, r, fill=(*col, int(rng.uniform(90, 200))))
    img.alpha_composite(ss.get())


def behind_frame(lt, relax=0.0):
    img = shimmer(behind_bg().copy(), lt, 3.0)
    ss = SS(W, H, s=2)
    for k in range(6):
        u = ((lt * 0.35 + k / 6) % 1.0)
        x0 = 120 + k * 170; pts = [(x0 + 30 * math.sin(u * 9 + j * 0.6 + k), 1250 - u * 900 - j * 40) for j in range(8)]
        ss.line(pts, (255, 150, 80, int(110 * math.sin(math.pi * u))), 6)
    img.alpha_composite(ss.get())
    gl = 0.6 + 0.4 * math.sin(lt * 2.5) if relax > 0 else 0.0
    if relax > 0:
        A.paste_c(img, A.glow(520, (255, 150, 70), int(120 * relax * gl)), 520, 1300)
    s = 300; gx, gy = 560, 1420 - 0.32 * s
    ss = SS(W, H, s=2)
    gecko(ss, gx, gy + 4 * math.sin(lt * 1.6), s, flip=-1, t=lt, blink=blink_at(lt), relax=relax, tail_amp=1.0 - 0.6 * relax)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 16, 0.45)
    A.paste(img, sh, -pad + 18, -pad + 26)
    img.alpha_composite(sp)
    motes(img, lt)
    return A.cam(img, zoom=1.03 + 0.03 * math.sin(lt * 0.5), rot=0.4 * math.sin(lt * 0.9))


def behind(ctx, lt):
    return behind_frame(lt)


# ======================================================================= corte da geladeira (cenas 2, 3)
FX0, FY0, FX1, FY1 = 190, 380, 760, 1560
FLOOR_Y = 1560


def kitchen_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (34, 32, 52)), (0.8, (52, 44, 64)), (1, (40, 34, 48))])
        d = ImageDraw.Draw(im)
        d.rectangle([0, FLOOR_Y, W, H], fill=(72, 60, 66))
        for x in range(0, W, 120): d.line([(x, FLOOR_Y), (x - 60, H)], fill=(60, 50, 56), width=3)
        d.line([(0, FLOOR_Y + 120), (W, FLOOR_Y + 120)], fill=(60, 50, 56), width=3)
        A.paste_c(im, A.glow(420, GLOW, 110), 860, 1300)
        return im
    return cached("kitchen", mk)


def _row(xa, xb, y):
    return [(xa, y), (xb, y)]


def pipe_path():
    """caminho do gás: (segmento, pontos). evap -> suction -> comp -> disch -> cond -> cap"""
    def mk():
        ev = [(560, 450)]
        ys = [450, 500, 550, 600, 650, 700, 742]
        for i, y in enumerate(ys):
            a, b = (560, 712) if i % 2 == 0 else (712, 560)
            if i > 0: ev.append((a, y))
            ev.append((b, y))
        su = [ev[-1], (744, 742), (744, 1470), (706, 1492)]
        co = [(706, 1492), (690, 1522), (676, 1500), (700, 1470), (722, 1462)]
        di = [(722, 1462), (850, 1462), (850, 520)]
        cd = [(850, 520)]
        y = 520; k = 0
        while y <= 1420:
            a, b = (850, 784) if k % 2 == 0 else (784, 850)
            cd.append((b, y)); y += 60; k += 1
            if y <= 1420: cd.append((b, y))
        ca = [cd[-1], (770, cd[-1][1] + 14), (754, 1440), (754, 432), (560, 432), (560, 450)]
        return [("evap", ev), ("suction", su), ("comp", co), ("disch", di), ("cond", cd), ("cap", ca)]
    return cached("path", mk)


SPEED = {"evap": 1.6, "suction": 2.2, "comp": 0.9, "disch": 2.0, "cond": 0.75, "cap": 0.6}


def path_table():
    def mk():
        segs = []
        for name, pts in pipe_path():
            L = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:]))
            segs.append((name, pts, L, L / SPEED[name]))
        return segs, sum(s[3] for s in segs)
    return cached("ptable", mk)


def path_point(u):
    segs, TT = path_table()
    tt = (u % 1.0) * TT
    for name, pts, L, dt in segs:
        if tt <= dt:
            f = tt / dt; d = f * L
            for a, b in zip(pts, pts[1:]):
                l = math.hypot(b[0] - a[0], b[1] - a[1])
                if d <= l:
                    q = d / max(l, 1e-6); return name, f, (a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q)
                d -= l
            return name, f, pts[-1]
        tt -= dt
    return "cap", 1.0, segs[-1][1][-1]


def particle_style(name, f):
    if name == "cap": return LIQ, 5
    if name == "evap": return mixc(LIQ, COLD, f), 5 + 4 * f
    if name == "suction": return COLD, 9
    if name == "comp": return mixc(COLD, HOT, f), 9
    if name == "disch": return HOT, 9
    if f < 0.6: return mixc(HOT, (255, 160, 60), f / 0.6), 9 - 3 * f
    return mixc((255, 160, 60), LIQ, (f - 0.6) / 0.4), 6 - (f - 0.6) * 2.5


def draw_pipes(ss, alpha=255, glow_u=1.0):
    for name, pts in pipe_path():
        col = {"evap": (70, 140, 230), "suction": (70, 140, 230), "comp": (150, 100, 200), "disch": (220, 80, 60),
               "cond": (220, 90, 60), "cap": (130, 200, 240)}[name]
        w = 5 if name == "cap" else 13
        ss.line(pts, (*INK, alpha), w + 6); ss.line(pts, (*col, alpha), w)


def draw_particles(ss, t, n=150, rate=0.06, a=255):
    for i in range(n):
        name, f, (x, y) = path_point(i / n + t * rate)
        col, r = particle_style(name, f)
        ss.circle(x, y, r, fill=(*col, a), ink=(*INK, int(a * 0.6)), w=1.2)


def fridge_body(xray=True):
    def mk():
        ss = SS(W, H, s=2)
        body = (225, 232, 242, 130) if xray else (228, 234, 242)
        ss.rrect(FX0, FY0, FX1, FY1, 28, fill=body, ink=INK, w=5)
        ss.rrect(224, 414, 726, 760, 14, fill=(176, 220, 246, 200), ink=INK, w=4)
        ss.rrect(224, 800, 726, 1440, 14, fill=(206, 234, 248, 200), ink=INK, w=4)
        for y in (1020, 1230): ss.line([(232, y), (718, y)], (150, 190, 210), 5, cap=False)
        ss.rrect(194, 560, 206, 700, 5, fill=(150, 160, 175), ink=INK, w=3)
        ss.rrect(194, 860, 206, 1060, 5, fill=(150, 160, 175), ink=INK, w=3)
        ss.rect(224, 1462, 600, 1548, fill=(70, 72, 82))
        for x in range(236, 596, 18): ss.line([(x, 1470), (x, 1540)], (40, 40, 48), 6, cap=False)
        # comida
        ss.rrect(270, 640, 420, 742, 12, fill=(250, 196, 214), ink=INK, w=4)
        ss.rrect(270, 640, 420, 664, 8, fill=(140, 90, 70), ink=INK, w=3)
        ss.text((345, 705), "SORVETE", 20, "mont-Black", fill=(140, 60, 90))
        ss.rrect(440, 690, 530, 742, 8, fill=(200, 235, 255), ink=INK, w=3)
        for k, (x, col) in enumerate(((270, (90, 170, 90)), (330, (240, 150, 50)), (390, (200, 60, 60)))):
            ss.rrect(x, 880, x + 44, 1018, 12, fill=col, ink=INK, w=3)
            ss.rect(x + 14, 862, x + 30, 882, fill=col)
        ss.rrect(470, 900, 600, 1018, 10, fill=(250, 250, 250), ink=INK, w=3)
        ss.text((535, 960), "LEITE", 20, "mont-Black", fill=(60, 120, 200))
        for k in range(5):
            ss.circle(280 + k * 70, 1200, 30, fill=[(230, 70, 60), (120, 190, 80), (250, 160, 40), (230, 70, 60), (120, 190, 80)][k], ink=INK, w=3)
        return ss.get()
    return cached(("fbody", xray), mk)


def condenser_static(ss):
    for name, pts in pipe_path():
        if name == "cond":
            ss.line(pts, (24, 22, 28), 16)
    for x in range(784, 852, 10):
        ss.line([(x, 505), (x, 1435)], (40, 38, 46, 200), 2, cap=False)


def compressor_dome(ss):
    ss.ellipse(690, 1508, 58, 44, fill=(36, 36, 44), ink=INK, w=4)
    ss.ellipse(672, 1492, 20, 10, fill=(120, 120, 140, 160))


def fridge_wide(lt, pipes=0.0, heat=None, gecko_warm=0.0, zoom=1.0, cx=540, cy=1000):
    img = kitchen_bg().copy()
    ss = SS(W, H, s=2)
    condenser_static(ss)
    img.alpha_composite(ss.get())
    img.alpha_composite(fridge_body(True))
    ss = SS(W, H, s=2)
    compressor_dome(ss)
    if pipes > 0:
        draw_pipes(ss, int(255 * pipes))
        draw_particles(ss, lt, a=int(255 * pipes))
    img.alpha_composite(ss.get())
    if heat is not None: heat(img)
    gs = 42; gx, gy = 930, FLOOR_Y - 0.32 * gs
    if gecko_warm > 0: A.paste_c(img, A.glow(110, (255, 120, 60), int(200 * gecko_warm)), gx, gy)
    ss = SS(W, H, s=2)
    gecko(ss, gx, gy, gs, flip=-1, t=lt, blink=blink_at(lt, (0.8, 3.0)), relax=gecko_warm * 0.8)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=zoom, dx=(540 - cx) * (zoom - 1) / zoom, dy=(1000 - cy) * (zoom - 1) / zoom)


def heatmove(ctx, lt):
    ttira = ctx.wt("tira")
    act = ease((lt - ttira + 0.6) / 0.6)

    def heat(img):
        if act <= 0: return
        starts = [(345, 690), (300, 950), (535, 960), (420, 1200), (300, 1200), (480, 600)]
        for k, (sx, sy) in enumerate(starts):
            for j in range(3):
                u = ((lt - ttira + 0.6) * 0.42 + k * 0.17 + j / 3) % 1.0
                if u < 0.35: x, y = lerp(sx, 745, u / 0.35), sy
                elif u < 0.55: x, y = lerp(745, 815, (u - 0.35) / 0.2), sy
                else:
                    v = (u - 0.55) / 0.45; x, y = lerp(815, 930, v), lerp(sy, FLOOR_Y - 20, v ** 1.5)
                r = 26 + 8 * math.sin(lt * 6 + k + j)
                A.paste_c(img, A.glow(int(r), (255, 80, 50), int(230 * act)), x + 6 * math.sin(lt * 5 + k), y)

    img = fridge_wide(lt, pipes=0.0, heat=heat, gecko_warm=act * clamp01((lt - ttira - 0.8) / 1.0), zoom=1.0 + 0.04 * lt / max(1, ctx.dur))
    tcria = ctx.wt("cria")
    q = ease((lt - tcria) / 0.3) * (1 - ease((lt - ttira + 0.2) / 0.3))
    if q > 0:
        ss = SS(W, H, s=2)
        for k in range(6):
            a = k * math.pi / 3
            ss.line([(475, 600), (475 + 70 * math.cos(a), 600 + 70 * math.sin(a))], (120, 210, 255, int(255 * q)), 10)
        ss.line([(390, 515), (560, 685)], (230, 60, 70, int(255 * q)), 18)
        ss.line([(390, 685), (560, 515)], (230, 60, 70, int(255 * q)), 18)
        img.alpha_composite(ss.get())
    return img


def pipes(ctx, lt):
    q = ease((lt - 0.1) / 0.6)
    return fridge_wide(lt, pipes=q, zoom=1.0 + 0.10 * easeio(lt / max(1, ctx.dur)), cx=640, cy=950)


# ======================================================================= cena 4: evaporador (pressão baixa)
def frost_star(ss, x, y, r, a=230):
    for k in range(3):
        an = k * math.pi / 3
        ss.line([(x - r * math.cos(an), y - r * math.sin(an)), (x + r * math.cos(an), y + r * math.sin(an))], (255, 255, 255, a), 2.5)


def evap(ctx, lt):
    img = A.vgrad(W, H, [(0, (200, 236, 252)), (1, (110, 170, 226))])
    ss = SS(W, H, s=2)
    py, R, r0, xf = 860, 120, 20, 300
    ss.poly([(-20, py - r0 - 14), (xf, py - r0 - 14), (xf + 80, py - R - 14), (W + 20, py - R - 14),
             (W + 20, py + R + 14), (xf + 80, py + R + 14), (xf, py + r0 + 14), (-20, py + r0 + 14)], fill=(214, 226, 238), ink=INK, w=5)
    ss.poly([(-20, py - r0), (xf, py - r0), (xf + 80, py - R), (W + 20, py - R),
             (W + 20, py + R), (xf + 80, py + R), (xf, py + r0), (-20, py + r0)], fill=(150, 200, 240, 200))
    rng = np.random.default_rng(3)
    for k in range(60):
        x = rng.uniform(0, W); top = rng.random() < 0.5
        yy = (py - (r0 if x < xf else R) - 20 - rng.uniform(0, 26)) if top else (py + (r0 if x < xf else R) + 20 + rng.uniform(0, 26))
        frost_star(ss, x, yy, rng.uniform(6, 13) * (0.5 + 0.5 * ease(lt / 1.5)))
    n = 70
    for i in range(n):
        u = (i / n + lt * 0.11) % 1.0
        if u < 0.3:
            x = lerp(-20, xf, u / 0.3); y = py + 8 * math.sin(i * 2.3); r = 7; col = LIQ; a = 255
        else:
            v = (u - 0.3) / 0.7
            x = lerp(xf, W + 40, v ** 0.8); y = py + (R - 26) * math.sin(i * 2.17 + lt * 1.5) * min(1, v * 3)
            r = 7 + 22 * min(1, v * 2.5); col = mixc(LIQ, COLD, min(1, v * 2)); a = int(255 - 120 * min(1, v * 2))
        ss.circle(x, y, r, fill=(*col, a), ink=(*INK, a // 2), w=1.5)
    tbx, tby = 300, 1300
    ss.rrect(tbx - 140, tby - 90, tbx + 140, tby + 90, 18, fill=(250, 196, 214), ink=INK, w=5)
    ss.rrect(tbx - 140, tby - 90, tbx + 140, tby - 50, 12, fill=(140, 90, 70), ink=INK, w=4)
    ss.text((tbx, tby + 20), "SORVETE", 34, "mont-Black", fill=(140, 60, 90))
    img.alpha_composite(ss.get())
    for k in range(7):
        u = (lt * 0.5 + k / 7) % 1.0
        x = lerp(tbx - 60 + k * 20, 560 + k * 70, u); y = lerp(tby - 110, py + R * 0.6, u)
        col = mixc((255, 90, 60), COLD, clamp01((u - 0.7) / 0.3))
        A.paste_c(img, A.glow(30, col, int(220 * math.sin(math.pi * u))), x + 10 * math.sin(lt * 4 + k), y)
    ss = SS(W, H, s=2)
    tpb = ctx.wt("pressão")
    q = ease((lt - tpb) / 0.3)
    if q > 0:
        A.arrow(ss, 140, 700, 140, py - r0 - 30, (40, 80, 140, int(255 * q)), w=12, head=2.4, iw=3)
        ss.text((140, 670), "cano fino", 34, "mont-Black", fill=(30, 60, 120, int(255 * q)))
        A.arrow(ss, 720, 640, 720, py - R - 30, (40, 80, 140, int(255 * q)), w=12, head=2.4, iw=3)
        ss.text((720, 610), "cano largo = pressão baixa", 34, "mont-Black", fill=(30, 60, 120, int(255 * q)))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * easeio(lt / max(1, ctx.dur)), rot=0.3 * math.sin(lt))


# ======================================================================= cena 5: suor (evaporar rouba calor)
def skin_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (60, 44, 60)), (1, (40, 30, 44))])
        ss = SS(W, H, s=2)
        top = [(x, 760 + 90 * math.sin(x / 360 + 0.6)) for x in range(-20, W + 40, 20)]
        ss.poly(top + [(W + 20, H + 20), (-20, H + 20)], fill=(226, 166, 136), ink=INK, w=5)
        top2 = [(x, y + 70) for x, y in top]
        ss.poly(top2 + [(W + 20, H + 20), (-20, H + 20)], fill=(214, 152, 122))
        rng = np.random.default_rng(6)
        for _ in range(160):
            x = rng.uniform(0, W); y0 = 760 + 90 * math.sin(x / 360 + 0.6)
            y = rng.uniform(y0 + 30, H)
            ss.circle(x, y, rng.uniform(2, 4), fill=(170, 110, 90, 160))
        im.alpha_composite(ss.get())
        return im
    return cached("skin", mk)


def freezer_inside(lt):
    img = A.vgrad(W, H, [(0, (210, 240, 255)), (1, (130, 190, 235))])
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(9)
    for _ in range(90): frost_star(ss, rng.uniform(0, W), rng.uniform(0, H), rng.uniform(5, 14), 180)
    ss.rrect(160, 1240, 640, 1520, 26, fill=(250, 196, 214), ink=INK, w=6)
    ss.rrect(160, 1240, 640, 1310, 18, fill=(140, 90, 70), ink=INK, w=5)
    ss.text((400, 1420), "SORVETE", 60, "mont-Black", fill=(140, 60, 90))
    tx, ty0, ty1 = 860, 640, 1020
    ss.rrect(tx - 34, ty0, tx + 34, ty1, 34, fill=(255, 255, 255), ink=INK, w=5)
    ss.circle(tx, ty1 + 20, 56, fill=(80, 160, 255), ink=INK, w=5)
    lev = lerp(0.62, 0.18, ease(lt / 1.2))
    ss.rrect(tx - 16, lerp(ty1, ty0 + 30, lev), tx + 16, ty1 + 10, 16, fill=(80, 160, 255))
    for k in range(6):
        y = lerp(ty0 + 40, ty1 - 40, k / 5); ss.line([(tx + 34, y), (tx + 54, y)], INK, 4, cap=False)
    t18 = int(round(lerp(4, -18, ease(lt / 1.2))))
    ss.text((tx - 250, 820), f"{t18} °C", 110, "anton", fill=(255, 255, 255), stroke=8)
    img.alpha_composite(ss.get())
    motes(img, lt, 30, 5, (255, 255, 255))
    return img


def sweat(ctx, lt):
    t2 = ctx.beat_t(1) - 0.05
    if lt >= t2:
        return freezer_inside(lt - t2)
    img = skin_bg().copy()
    cool = clamp01(lt / max(0.5, t2))
    img.alpha_composite(Image.new("RGBA", (W, H), (120, 170, 255, int(50 * cool))))
    ss = SS(W, H, s=2)
    drops = [(130, 0.9), (290, 1.4), (450, 1.1), (610, 1.7), (770, 1.0), (930, 1.5)]
    for k, (x, life) in enumerate(drops):
        y = 760 + 90 * math.sin(x / 360 + 0.6) - 6
        r = 46 * max(0.0, 1 - lt / (life * t2 * 0.9 + 0.3)) ** 0.6
        if r > 2:
            ss.ellipse(x, y - r * 0.55, r, r * 0.75, fill=(200, 235, 255, 210), ink=INK, w=3)
            ss.ellipse(x - r * 0.35, y - r * 0.85, r * 0.25, r * 0.15, fill=(255, 255, 255, 230))
        for j in range(3):
            u = (lt * 0.7 + j / 3 + k * 0.13) % 1.0
            pts = [(x + 18 * math.sin(u * 8 + i * 0.7 + k), y - 60 - u * 520 - i * 26) for i in range(6)]
            ss.line(pts, (255, 255, 255, int(150 * math.sin(math.pi * u))), 5)
            hx, hy = pts[2]
            ss.circle(hx, hy, 10, fill=(255, 90, 60, int(230 * math.sin(math.pi * u))))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    tx, ty0, ty1 = 960, 500, 760
    ss.rrect(tx - 28, ty0, tx + 28, ty1, 28, fill=(255, 255, 255), ink=INK, w=5)
    ss.circle(tx, ty1 + 16, 46, fill=(240, 80, 60), ink=INK, w=5)
    lev = lerp(0.7, 0.45, cool)
    ss.rrect(tx - 13, lerp(ty1, ty0 + 24, lev), tx + 13, ty1 + 10, 13, fill=(240, 80, 60))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(0.5, t2)))


# ======================================================================= cena 6: Visão do Bicho (cores no escuro)
def under_scene():
    def mk():
        im = A.vgrad(W, H, [(0, (60, 54, 70)), (0.55, (84, 70, 76)), (1, (120, 96, 86))])
        ss = SS(W, H, s=2)
        ss.rect(0, 0, W, 380, fill=(70, 74, 84))
        for x in range(30, W, 46): ss.line([(x, 300), (x, 372)], (40, 40, 48), 10, cap=False)
        ss.rect(0, 1240, W, 1290, fill=(96, 98, 110))
        cx, cy = 560, 1000
        ss.ellipse(cx, cy + 250, 330, 50, fill=(30, 26, 30, 160))
        for fx in (cx - 240, cx + 240):
            ss.rrect(fx - 40, cy + 200, fx + 40, cy + 262, 14, fill=(40, 40, 46), ink=INK, w=4)
        ss.ellipse(cx, cy, 270, 225, fill=(34, 36, 46), ink=INK, w=6)
        ss.ellipse(cx - 90, cy - 110, 90, 45, fill=(110, 120, 150, 170))
        ss.rect(cx - 280, cy + 40, cx + 280, cy + 80, fill=(30, 30, 38))
        cop, cop2 = (196, 120, 58), (232, 160, 90)
        for pts in ([(cx - 120, cy - 200), (cx - 140, cy - 420), (cx - 300, cy - 520), (cx - 520, cy - 520)],
                    [(cx + 80, cy - 215), (cx + 100, cy - 380), (cx + 330, cy - 400), (cx + 340, cy - 720)],
                    [(cx + 250, cy - 60), (cx + 420, cy - 60), (cx + 470, cy - 200), (cx + 600, cy - 220)]):
            ss.line(pts, INK, 34); ss.line(pts, cop, 26); ss.line([(x - 4, y - 6) for x, y in pts], cop2, 7)
        ss.rrect(cx + 150, cy - 140, cx + 260, cy - 40, 12, fill=(60, 64, 76), ink=INK, w=4)
        for pts, col in (([(cx + 205, cy - 90), (cx + 330, cy + 60), (cx + 520, cy + 120)], (220, 60, 50)),
                         ([(cx + 215, cy - 80), (cx + 350, cy + 90), (cx + 540, cy + 170)], (60, 120, 220))):
            ss.line(pts, INK, 16); ss.line(pts, col, 10)
        ss.text((cx, cy + 60), "COMPRESSOR", 34, "mont-Black", fill=(200, 205, 220))
        rng = np.random.default_rng(14)
        for (bx, by, br) in ((150, 1500, 70), (880, 1560, 60)):
            for _ in range(36):
                a = rng.uniform(0, 2 * math.pi); rr = br * rng.uniform(0.2, 1)
                ss.circle(bx + math.cos(a) * rr, by + math.sin(a) * rr * 0.6, rng.uniform(7, 15), fill=(170, 160, 160, 170))
        ss.circle(330, 1430, 40, fill=(210, 60, 50), ink=INK, w=5); ss.circle(330, 1430, 28, ink=(240, 200, 200), w=3)
        im.alpha_composite(ss.get())
        return im
    return cached("under", mk)


def toe_pads(img, t):
    ss = SS(W, 520, s=2)
    for side in (-1, 1):
        bx = 540 + side * 330; by = 560 + 10 * math.sin(t * 2 + side)
        ss.line([(540 + side * 600, 640), (bx, by)], INK, 120); ss.line([(540 + side * 600, 640), (bx, by)], GK["skin"], 108)
        for k, a in enumerate((-70, -35, 0, 35)):
            ang = math.radians(-90 + a * side + (0 if side > 0 else 0))
            tx = bx + 150 * math.cos(math.radians(-90 - side * 30 + a)); ty = by + 150 * math.sin(math.radians(-90 - side * 30 + a))
            ss.line([(bx, by), (tx, ty)], INK, 46); ss.line([(bx, by), (tx, ty)], GK["skin"], 36)
            ss.ellipse(tx, ty, 40, 34, fill=GK["belly"], ink=INK, w=5)
            for j in range(3): ss.line([(tx - 24, ty - 10 + j * 10), (tx + 24, ty - 10 + j * 10)], (200, 170, 160), 3, cap=False)
    img.alpha_composite(ss.get(), (0, H - 520))


def vision(ctx, lt):
    img = under_scene().copy()
    tz = ctx.wt("zumbido")
    ss = SS(W, H, s=2)
    if lt > tz - 0.3:
        for k in range(4):
            u = ((lt - tz + 0.3) * 0.8 + k / 4) % 1.0
            r = 280 + 520 * u
            ss.ellipse(560, 1000, r, r * 0.85, ink=(255, 230, 120, int(170 * (1 - u))), w=8)
    img.alpha_composite(ss.get())
    toe_pads(img, lt)
    v = img
    img = A.cam(v, zoom=1.02 + 0.02 * math.sin(lt * 0.8), dx=4 * math.sin(lt * 23) * clamp01((lt - tz) / 0.3))
    u = ease((lt - 0.35) / 1.1)
    return A.night_reveal(img, u, 540, 1750)


# ======================================================================= cena 7: compressor espreme
def compress(ctx, lt):
    img = A.vgrad(W, H, [(0, (26, 24, 40)), (1, (50, 34, 46))])
    cx, cy = 540, 920
    tq = ctx.wt("quente", n=1, default=ctx.dur * 0.7)
    heat = clamp01(lt / max(0.5, ctx.dur))
    A.paste_c(img, A.glow(520, (255, 90, 50), int(60 + 120 * heat)), cx, cy)
    ss = SS(W, H, s=2)
    ss.ellipse(cx, cy, 400, 360, fill=(60, 64, 80, 120), ink=(200, 210, 230, 200), w=5)
    om = 2 * math.pi * (1.6 + 1.4 * heat)
    ang = om * lt
    yc0, yc1 = 560, 980
    pis = 820 + 110 * math.sin(ang)
    ss.rect(cx - 150, yc0, cx + 150, yc1, fill=(30, 30, 40, 200))
    ss.line([(cx - 150, yc0), (cx - 150, yc1)], (200, 210, 230), 8, cap=False)
    ss.line([(cx + 150, yc0), (cx + 150, yc1)], (200, 210, 230), 8, cap=False)
    ss.line([(cx - 150, yc0), (cx + 150, yc0)], (200, 210, 230), 8, cap=False)
    h = pis - yc0
    comp = clamp01(1 - (h - 150) / 220)
    rng = np.random.default_rng(2)
    for k in range(34):
        u, v = rng.random(), rng.random()
        jit = (3 + 10 * comp + 8 * heat)
        x = cx - 130 + 260 * u + jit * math.sin(lt * 20 + k * 3)
        y = yc0 + 16 + (h - 34) * v + jit * math.cos(lt * 23 + k * 5)
        col = mixc(COLD, HOT, clamp01(comp * 0.7 + heat * 0.5))
        ss.circle(x, y, 13, fill=col, ink=INK, w=2)
    ss.rrect(cx - 140, pis, cx + 140, pis + 70, 10, fill=(170, 176, 196), ink=INK, w=5)
    wx, wy = cx, 1150
    px, py = wx + 80 * math.cos(ang), wy + 80 * math.sin(ang)
    ss.line([(cx, pis + 35), (px, py)], (150, 156, 176), 26)
    ss.circle(wx, wy, 110, fill=(90, 94, 110), ink=INK, w=5)
    ss.circle(px, py, 18, fill=(220, 220, 230), ink=INK, w=4)
    for k in range(10):
        ss.line([(cx - 260, 1080 + k * 14), (cx - 170, 1080 + k * 14)], (200, 120, 60), 8, cap=False)
        ss.line([(cx + 170, 1080 + k * 14), (cx + 260, 1080 + k * 14)], (200, 120, 60), 8, cap=False)
    ss.line([(-20, 600), (cx - 150, 600)], INK, 40); ss.line([(-20, 600), (cx - 150, 600)], (70, 140, 230), 30)
    ss.line([(cx + 150, 600), (W + 20, 600)], INK, 40); ss.line([(cx + 150, 600), (W + 20, 600)], (220, 80, 60), 30)
    for k in range(6):
        u = (lt * 0.8 + k / 6) % 1.0
        ss.circle(lerp(-20, cx - 160, u), 600, 10, fill=COLD, ink=INK, w=2)
        ss.circle(lerp(cx + 160, W + 20, u), 600, 10, fill=HOT, ink=INK, w=2)
    ss.text((160, 540), "gás frio", 34, "mont-Black", fill=(140, 200, 255))
    ss.text((930, 540), "gás quente", 34, "mont-Black", fill=(255, 140, 110))
    img.alpha_composite(ss.get())
    sh = (4 + 14 * heat + 10 * clamp01((lt - tq) / 0.3))
    return A.cam(img, dx=sh * math.sin(lt * 41), dy=sh * 0.6 * math.cos(lt * 37), rot=0.25 * math.sin(lt * 29) * heat)


# ======================================================================= cena 8: grade (condensador) + ciclo
def grade_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (40, 30, 40)), (1, (70, 44, 40))])
        A.paste_c(im, A.glow(720, GLOW, 90), 540, 900)
        return im
    return cached("grade_bg", mk)


GROWS = list(range(470, 1330, 86))


def grade_path():
    pts = [(-40, GROWS[0])]
    for k, y in enumerate(GROWS):
        a, b = (100, 980) if k % 2 == 0 else (980, 100)
        if k == 0: pts = [(-40, y), (b, y)]
        else: pts += [(a, y), (b, y)]
    return pts


def condenser(ctx, lt):
    img = grade_bg().copy()
    ss = SS(W, H, s=2)
    pts = grade_path()
    ss.line(pts, INK, 50); ss.line(pts, (60, 56, 66, 255), 40)
    for x in range(110, 980, 24): ss.line([(x, GROWS[0] - 30), (x, GROWS[-1] + 30)], (34, 32, 38, 200), 3, cap=False)
    segs = list(zip(pts, pts[1:])); Ls = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in segs]; TL = sum(Ls)
    n = 90
    for i in range(n):
        u = (i / n + lt * 0.05) % 1.0
        uu = u ** 0.75
        d = uu * TL
        for (a, b), l in zip(segs, Ls):
            if d <= l:
                q = d / l; x, y = a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q; break
            d -= l
        f = uu
        col = mixc(HOT, (255, 160, 60), f / 0.6) if f < 0.6 else mixc((255, 160, 60), LIQ, (f - 0.6) / 0.4)
        r = 13 if f < 0.6 else lerp(13, 8, (f - 0.6) / 0.4)
        ss.circle(x, y, r, fill=col, ink=INK, w=2)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    for k in range(5):
        u = (lt * 0.6 + k / 5) % 1.0
        r = 100 + 520 * u
        ss.ellipse(540, 760, r, r * 0.8, ink=(255, 150, 70, int(140 * (1 - u))), w=7)
    img.alpha_composite(ss.get())
    gs = 150; gx, gy = 760, 1460 - 0.32 * gs
    A.paste_c(img, A.glow(220, (255, 130, 60), 120), gx, gy)
    ss = SS(W, H, s=2)
    gecko(ss, gx, gy, gs, flip=-1, t=lt, blink=blink_at(lt, (1.0,)), relax=0.4)
    img.alpha_composite(ss.get())
    trec = ctx.wt("recomeça")
    q = ease((lt - trec + 0.15) / 0.35)
    if q > 0:
        img = cycle_overlay(img, lt - trec, q)
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.7))


def cycle_overlay(img, t, q):
    ov = SS(W, H, s=2)
    cx, cy, R = 540, 830, 270
    ov.circle(cx, cy, R + 120, fill=(18, 14, 30, int(225 * q)))
    ov.circle(cx, cy, R, ink=(255, 255, 255, int(200 * q)), w=10)
    nodes = [(-90, "EVAPORA", COLD), (0, "COMPRIME", (180, 120, 230)), (90, "SOLTA CALOR", HOT), (180, "VIRA LÍQUIDO", LIQ)]
    for a, txt, col in nodes:
        x, y = cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))
        ov.circle(x, y, 58 * A.back(q), fill=(*col, 255), ink=INK, w=5)
        ty = y - 92 if a == -90 else y + 92 if a == 90 else y
        tx = x if a in (-90, 90) else (x + 0 if a == 0 else x)
        if a == 0: ov.text((x - 10, y + 92), txt, 30, "mont-Black", fill=(255, 255, 255, int(255 * q)))
        elif a == 180: ov.text((x + 10, y + 92), txt, 30, "mont-Black", fill=(255, 255, 255, int(255 * q)))
        else: ov.text((tx, ty), txt, 30, "mont-Black", fill=(255, 255, 255, int(255 * q)))
    a = math.radians(-90 + 360 * ((t * 0.6) % 1.0))
    ov.circle(cx + R * math.cos(a), cy + R * math.sin(a), 22, fill=(255, 222, 40, int(255 * q)), ink=INK, w=4)
    img.alpha_composite(ov.get())
    return img


# ======================================================================= cena 9: sorvete (payoff) -> volta para trás da geladeira
def front_kitchen():
    def mk():
        im = A.vgrad(W, H, [(0, (40, 36, 58)), (1, (60, 50, 66))])
        d = ImageDraw.Draw(im)
        d.rectangle([0, 1600, W, H], fill=(80, 66, 70))
        ss = SS(W, H, s=2)
        ss.rrect(240, 300, 840, 1610, 34, fill=(234, 238, 246), ink=INK, w=6)
        ss.line([(240, 720), (840, 720)], INK, 6, cap=False)
        ss.rrect(780, 820, 800, 1080, 8, fill=(160, 170, 186), ink=INK, w=3)
        ss.rrect(250, 1560, 830, 1600, 10, fill=(70, 72, 82))
        im.alpha_composite(ss.get())
        return im
    return cached("front", mk)


def hand(ss, x, y, s, grip=0.0):
    skin, sk2 = (238, 190, 156), (214, 164, 132)
    ss.line([(x + 700, y + 160), (x + 60, y + 10)], INK, 150 * s + 8); ss.line([(x + 700, y + 160), (x + 60, y + 10)], skin, 150 * s)
    ss.ellipse(x, y, 95 * s, 80 * s, fill=skin, ink=INK, w=5)
    for k in range(4):
        fy = y - 50 * s + k * 34 * s
        ex = x - 110 * s + 40 * s * grip
        ss.line([(x - 20 * s, fy), (ex, fy + 14 * s * grip)], INK, 32 * s + 8); ss.line([(x - 20 * s, fy), (ex, fy + 14 * s * grip)], sk2, 32 * s)
    ss.line([(x - 10 * s, y + 60 * s), (x - 80 * s, y + 90 * s)], INK, 34 * s + 8); ss.line([(x - 10 * s, y + 60 * s), (x - 80 * s, y + 90 * s)], skin, 34 * s)


def icecream(ctx, lt):
    tpay = ctx.beat_t(1)
    if lt >= tpay:
        return behind_frame(lt - tpay + 0.0, relax=ease((lt - tpay) / 0.6))
    img = front_kitchen().copy()
    ss = SS(W, H, s=2)
    op = ease(lt / 0.5)
    ss.rrect(250, 310, 830, 712, 20, fill=(200, 236, 255), ink=INK, w=4)
    if op > 0:
        A.paste_c(img, A.glow(500, (200, 240, 255), int(160 * op)), 540, 510)
    tub_out = easeio((lt - 1.3) / 0.8)
    tx = lerp(420, 980, tub_out); ty = lerp(560, 640, tub_out)
    ss.rrect(330, 640, 470, 700, 10, fill=(200, 235, 255), ink=INK, w=3)
    for k in range(5): frost_star(ss, 300 + k * 110, 340 + (k % 2) * 30, 12, 200)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ss.rrect(tx - 110, ty - 70, tx + 110, ty + 70, 16, fill=(250, 196, 214), ink=INK, w=5)
    ss.rrect(tx - 110, ty - 70, tx + 110, ty - 40, 10, fill=(140, 90, 70), ink=INK, w=4)
    ss.text((tx, ty + 15), "SORVETE", 28, "mont-Black", fill=(140, 60, 90))
    reach = easeio((lt - 0.4) / 0.8)
    hx = lerp(1250, tx + 120, reach) if lt < 1.3 else tx + 120
    hand(ss, hx, ty - 10, 1.0, grip=clamp01((lt - 1.1) / 0.2))
    w = lerp(580, 60, op)
    ss.poly([(240, 300), (240 + w, 300 + 40 * op), (240 + w, 720 - 40 * op), (240, 720)], fill=(236, 240, 248), ink=INK, w=6)
    if w > 120: ss.rrect(240 + w - 50, 420, 240 + w - 30, 600, 8, fill=(160, 170, 186), ink=INK, w=3)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.05 * easeio(lt / max(0.5, tpay)))


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    """atrás da geladeira (grade quente) sem a lagartixa"""
    img = shimmer(behind_bg().copy(), 0.6, 3.0)
    motes(img, 0.6)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 330)
    ss = SS(int(3.4 * s), int(1.0 * s), s=2)
    gecko(ss, 1.30 * s, 0.42 * s, s, flip=-1, t=0.4, tail_amp=0.6)
    return ss.get()
