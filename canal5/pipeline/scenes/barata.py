"""Dia 2B — "E se você fosse uma barata no ralo?" (formato ATUAL; paleta: banheiro creme e menta x esgoto oliva).

Cenas: grate (gancho: de dentro do ralo olhando a grelha iluminada), curve (corte do sifão: a água fica presa na
curva), seal (fecho hídrico de ~5 cm barra o gás), flush (água nova empurra a velha), vision (Visão do Bicho: o
cheiro pelas antenas — o fedor para na água), vent (ventilação até o telhado), dry (ralo sem uso seca, o cheiro
sobe -> volta para a grelha = loop).
Raio-X: verde = água/ar, oliva/roxo = gás do esgoto (fedor).
Fontes: ABNT NBR 8160 (fecho hídrico >= 50 mm); apostila de esgoto sanitário da Poli-USP.
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached

RB = dict(wing=(150, 76, 36), wing2=(178, 98, 48), pro=(214, 168, 92), pro_d=(112, 56, 30), head=(90, 46, 26),
          leg=(120, 62, 32), ant=(104, 54, 28))
WATER = (70, 214, 170); WATER_OLD = (150, 160, 90); STINK = (150, 140, 60); STINK2 = (170, 90, 160)
AIR = (110, 240, 120)
FLOOR_Y = 640; PIPE_W = 110; Y_W = 1385
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= barata (vista de cima, cabeça para cima)
def roach(ss, x, y, s, rot=0.0, t=0.0, walk=1.0, ant=1.0):
    P = lambda pts: A.xf(pts, x, y, s, rot)
    iw = max(1.4, s * 0.012)
    ph = t * 14 * walk

    def leg(hx, hy, kx, ky, fx, fy, k):
        side = 1 if hx > 0 else -1
        tri = (k + (0 if side > 0 else 1)) % 2
        sw = 0.06 * math.sin(ph + tri * math.pi) * walk
        pts = P([(hx, hy), (kx, ky + sw * 0.5), (fx, fy + sw)])
        ss.line(pts, INK, s * 0.04 + 2 * iw); ss.line(pts, RB["leg"], s * 0.04)
        for u in (0.35, 0.65):
            bx, by = lerp(pts[1][0], pts[2][0], u), lerp(pts[1][1], pts[2][1], u)
            ss.line([(bx, by), (bx + side * s * 0.03, by - s * 0.03)], INK, max(1, s * 0.01), cap=False)

    for k, (hy, kx, ky, fx, fy) in enumerate(((-0.12, 0.3, -0.24, 0.42, -0.42), (0.0, 0.34, 0.02, 0.5, 0.06),
                                              (0.12, 0.32, 0.3, 0.46, 0.62))):
        for side in (-1, 1):
            leg(side * 0.1, hy, side * kx, ky, side * fx, fy, k)
    for side in (-1, 1):
        ss.line(P([(side * 0.05, 0.5), (side * 0.11, 0.66)]), INK, s * 0.03); ss.line(P([(side * 0.05, 0.5), (side * 0.11, 0.66)]), RB["leg"], s * 0.018)
    ss.poly(P(A.ell_pts(0, 0.12, 0.24, 0.43, 0, 40)), fill=RB["wing"], ink=INK, w=iw)
    ss.poly(P(A.ell_pts(-0.11, 0.1, 0.1, 0.36, 4, 24)), fill=(*RB["wing2"], 200))
    ss.line(P([(0, -0.12), (0.02, 0.54)]), INK, max(1.2, s * 0.01), cap=False)
    ss.poly(P(A.ell_pts(-0.08, -0.02, 0.05, 0.2, 4, 20)), fill=(255, 220, 180, 90))
    ss.poly(P(A.ell_pts(0, -0.24, 0.22, 0.14, 0, 32)), fill=RB["pro"], ink=INK, w=iw)
    for side in (-1, 1):
        ss.poly(P(A.ell_pts(side * 0.07, -0.25, 0.065, 0.085, side * 15, 18)), fill=RB["pro_d"])
    ss.poly(P(A.ell_pts(0, -0.4, 0.1, 0.075, 0, 24)), fill=RB["head"], ink=INK, w=iw)
    for side in (-1, 1):
        ex, ey = P([(side * 0.065, -0.42)])[0]; er = s * 0.042
        ss.circle(ex, ey, er, fill=(250, 250, 245), ink=INK, w=iw)
        px, py = P([(side * 0.068, -0.432)])[0]
        ss.circle(px, py, er * 0.55, fill=(20, 12, 10))
        ss.circle(px - er * 0.2, py - er * 0.25, er * 0.2, fill=(255, 255, 255))
    for side in (-1, 1):
        pts = []
        for k in range(12):
            u = k / 11
            wv = 0.08 * math.sin(t * 3.0 * ant + u * 3 + side) * u * ant
            pts.append((side * (0.04 + 0.42 * u ** 0.9) + wv, -0.46 - 0.75 * u))
        ss.line(P(pts), INK, s * 0.022 + iw); ss.line(P(pts), RB["ant"], s * 0.022)


# ======================================================================= cena 1: dentro do ralo, olhando a grelha
GX, GY, GR = 540, 700, 320


def grate_bg():
    def mk():
        im = Image.new("RGBA", (W, H), (20, 18, 16, 255))
        ss = SS(W, H, s=2)
        for k in range(14, 0, -1):
            r = GR + k * 90
            ss.circle(GX, GY + k * 70, r, fill=mixc((26, 24, 18), (92, 92, 74), 1 - k / 14), ink=(14, 12, 10), w=4)
        ss.circle(GX, GY, GR + 40, fill=(150, 156, 160), ink=INK, w=6)
        ss.circle(GX, GY, GR, fill=(255, 246, 222))
        img = ss.get(); im.alpha_composite(img)
        ss = SS(W, H, s=2)
        for k in range(-5, 6):
            ss.line([(GX + k * 56, GY - GR), (GX + k * 56, GY + GR)], (150, 156, 160), 26, cap=False)
            ss.line([(GX + k * 56 - 8, GY - GR), (GX + k * 56 - 8, GY + GR)], (220, 226, 230), 5, cap=False)
        ss.circle(GX, GY, 70, fill=(150, 156, 160), ink=INK, w=4)
        ring = SS(W, H, s=2)
        ring.circle(GX, GY, GR + 200, fill=(0, 0, 0, 0))
        g = ss.get()
        m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).ellipse([GX - GR, GY - GR, GX + GR, GY + GR], fill=255)
        g.putalpha(Image.fromarray(np.minimum(np.asarray(g.split()[3]), np.asarray(m))))
        im.alpha_composite(g)
        A.paste_c(im, A.glow(520, (255, 240, 200), 120), GX, GY)
        return im
    return cached("grate_bg", mk)


def pov_antennae(img, t, reach=0.0):
    ss = SS(W, 820, s=2)
    for side in (-1, 1):
        bx, by = 540 + side * 120, 860
        pts = []
        for k in range(14):
            u = k / 13
            x = bx + side * (180 * u) + 30 * math.sin(t * 2.4 + u * 3 + side) * u
            y = by - u * (640 + 120 * reach)
            pts.append((x, y))
        ss.line(pts, INK, 26); ss.line(pts, RB["ant"], 18)
        for k in range(1, 13):
            ss.circle(pts[k][0], pts[k][1], 7, fill=(80, 40, 20))
    ss.ellipse(540, 860, 300, 150, fill=RB["head"], ink=INK, w=6)
    img.alpha_composite(ss.get(), (0, H - 820))


def stink(img, t, amt, y0=1300, seed=2):
    if amt <= 0: return
    rng = np.random.default_rng(seed)
    for k in range(16):
        x0 = rng.uniform(80, 1000); sp = rng.uniform(0.15, 0.3)
        u = (t * sp + k / 16) % 1.0
        x = x0 + 60 * math.sin(t * 0.9 + k); y = y0 + 500 - u * 700
        col = STINK if k % 3 else STINK2
        A.paste_c(img, A.glow(int(120 + 80 * u), col, int(230 * amt * math.sin(math.pi * u))), x, y)


def grate_frame(t, fog=0.0, reach=0.0):
    img = grate_bg().copy()
    ss = SS(W, H, s=2)
    for k in range(-4, 5):
        x = GX + k * 56 + 28
        ss.poly([(x - 18, GY - GR + 40), (x + 18, GY - GR + 40), (x + 80 + k * 40, H), (x - 80 + k * 40, H)], fill=(255, 240, 200, 26))
    for k in range(4):
        u = (t * 0.45 + k / 4) % 1.0
        x = GX + (k - 1.5) * 150 * (1 + u); y = GY + u * 900
        r = 10 + 40 * u ** 2
        ss.ellipse(x, y, r * 0.8, r, fill=(190, 240, 225, int(230 * (1 - u * 0.4))), ink=(*INK, 150), w=2)
        ss.circle(x - r * 0.25, y - r * 0.35, r * 0.22, fill=(255, 255, 255, 220))
    img.alpha_composite(ss.get())
    stink(img, t, fog)
    pov_antennae(img, t, reach)
    return A.cam(img, zoom=1.03 + 0.02 * math.sin(t * 0.7), rot=0.5 * math.sin(t * 0.5))


def grate(ctx, lt):
    tf = ctx.wt("fede"); tn = ctx.beat_t(2)
    fog = ease((lt - tf + 0.3) / 0.6) * (1 - 0.7 * ease((lt - tn) / 0.8))
    return grate_frame(lt, fog=fog)


# ======================================================================= corte do banheiro + sifão (cenas 2–4, 6, 7)
def trap_pts():
    def mk():
        pts = [(420, FLOOR_Y + 10)]
        pts += [(420, y) for y in range(FLOOR_Y + 40, 1401, 30)]
        for k in range(1, 31):
            a = math.radians(180 - 6 * k)
            pts.append((540 + 120 * math.cos(a), 1400 + 120 * math.sin(a) * -1 * -1))
        pts += [(660, 1370), (660, 1345)]
        out = [(660 + 30 * k, 1330 + 2.5 * k) for k in range(0, 16)]
        return pts, out
    return cached("trap", mk)


def _arc_fix(pts):
    # o arco do sifão passa por BAIXO (y maior): reflete os pontos do arco em torno de y = 1400
    return [(x, 1400 + abs(y - 1400)) if y != 1400 and 420 < x < 660 else (x, y) for x, y in pts]


def all_pipe():
    p, o = trap_pts()
    return _arc_fix(p), o


def section_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (250, 240, 222)), (0.33, (236, 226, 206)), (0.34, (120, 104, 84)), (1, (66, 54, 44))])
        ss = SS(W, H, s=2)
        for y in range(0, FLOOR_Y, 120):
            for x in range(-60 if (y // 120) % 2 else 0, W, 120):
                ss.rrect(x + 4, y + 4, x + 116, y + 116, 8, fill=(206, 236, 222), ink=(170, 200, 186), w=2)
        ss.rect(0, FLOOR_Y, W, FLOOR_Y + 22, fill=(236, 230, 218))
        ss.rect(0, FLOOR_Y + 22, W, FLOOR_Y + 130, fill=(150, 146, 140))
        for x in range(-40, W, 36):
            ss.line([(x, FLOOR_Y + 128), (x + 40, FLOOR_Y + 24)], (126, 122, 116), 3, cap=False)
        rng = np.random.default_rng(3)
        for _ in range(140):
            ss.circle(rng.uniform(0, W), rng.uniform(FLOOR_Y + 160, H), rng.uniform(3, 9), fill=(88, 72, 58))
        p, o = all_pipe()
        for pts in (p, o):
            ss.line(pts, INK, PIPE_W + 16); ss.line(pts, (196, 200, 206), PIPE_W + 8)
            ss.line(pts, (236, 240, 244, 255), PIPE_W)
        ss.rrect(960, 1240, 1090, 1560, 14, fill=(48, 44, 30), ink=INK, w=5)
        ss.text((1020, 1600), "ESGOTO", 34, "mont-Black", fill=(220, 210, 150))
        ss.rrect(350, FLOOR_Y - 8, 490, FLOOR_Y + 12, 6, fill=(170, 176, 182), ink=INK, w=4)
        im.alpha_composite(ss.get())
        return im
    return cached("section", mk)


def water_layer(level, col, a=235):
    p, o = all_pipe()
    ss = SS(W, H, s=1)
    ss.line([q for q in p if q[1] > FLOOR_Y + 300] + [o[0]], (*col, a), PIPE_W)
    im = ss.get()
    arr = np.asarray(im).copy()
    arr[:int(level)] = 0
    arr[:, 700:] = 0
    surf = SS(W, H, s=1)
    surf.line([(365, level + 2), (475, level + 2)], (255, 255, 255, 200), 5, cap=False)
    surf.line([(605, level + 2), (700, level + 2)], (255, 255, 255, 200), 5, cap=False)
    out = Image.fromarray(arr, "RGBA")
    if level < 1500: out.alpha_composite(surf.get())
    return out


def path_point(u, p, o):
    pts = p + o
    seg = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    d = (u % 1.0) * sum(seg)
    for (a, b), l in zip(zip(pts, pts[1:]), seg):
        if d <= l:
            q = d / max(l, 1e-6); return a[0] + (b[0] - a[0]) * q, a[1] + (b[1] - a[1]) * q
        d -= l
    return pts[-1]


def gas_puffs(img, t, amt, stop_x=700, level=Y_W, through=0.0):
    """gás do esgoto vem do lado direito pelo cano; para na água (stop_x) a menos que 'through' > 0"""
    if amt <= 0: return
    for k in range(9):
        u = (t * 0.35 + k / 9) % 1.0
        if through <= 0:
            x = lerp(1060, stop_x, min(1, u * 1.4)); y = 1335 + 2.5 * (x - 660) / 30 + 8 * math.sin(t * 3 + k)
            if u > 0.7: x += 25 * math.sin((u - 0.7) * 20)
        else:
            if u < 0.4: x, y = lerp(1060, 660, u / 0.4), 1345
            elif u < 0.6: x, y = lerp(660, 420, (u - 0.4) / 0.2), lerp(1345, 1300, (u - 0.4) / 0.2)
            else: x, y = 420, lerp(1300, FLOOR_Y - 200, (u - 0.6) / 0.4)
        col = STINK if k % 2 else STINK2
        A.paste_c(img, A.glow(int(46 + 10 * math.sin(t * 4 + k)), col, int(230 * amt)), x, y)


def section(t, level=Y_W, wcol=WATER, roach_on=True, zoom=1.0, cx=540, cy=1000):
    img = section_bg().copy()
    img.alpha_composite(water_layer(level, wcol))
    if roach_on:
        ss = SS(W, H, s=2)
        roach(ss, 760 + 30 * math.sin(t * 0.6), FLOOR_Y - 60, 130, rot=-80, t=t, walk=0.4)
        img.alpha_composite(ss.get())
    return img


def camz(img, zoom, cx, cy):
    return A.cam(img, zoom=zoom, dx=(540 - cx) * (zoom - 1) / zoom, dy=(960 - cy) * (zoom - 1) / zoom, cx=540, cy=960)


def flow_particles(img, t, n, col, rate=0.25, from_u=0.0, to_u=1.0, a=255):
    p, o = all_pipe(); ss = SS(W, H, s=2)
    for i in range(n):
        u = lerp(from_u, to_u, (i / n + t * rate) % 1.0)
        x, y = path_point(u, p, o)
        ss.circle(x + 18 * math.sin(i * 2.1), y, 11, fill=(*col, a), ink=(*INK, int(a * 0.6)), w=1.5)
    img.alpha_composite(ss.get())


def curve(ctx, lt):
    tfi = ctx.wt("fica"); td = ctx.wt("desce")
    lev = lerp(1600, Y_W, ease((lt - tfi) / 1.0))
    img = section(lt, level=lev)
    if lt > td - 0.3:
        q = clamp01((lt - td + 0.3) / 0.4) * (1 - clamp01((lt - tfi - 1.2) / 0.5))
        flow_particles(img, lt, 26, WATER, 0.35, a=int(255 * q))
    ts = ctx.wt("sifão")
    q = ease((lt - ts) / 0.4) * (1 - ease((lt - tfi + 0.2) / 0.3))
    if q > 0:
        ss = SS(W, H, s=2)
        ss.circle(540, 1430, 200 + 20 * math.sin(lt * 5), ink=(255, 222, 40, int(255 * q)), w=10)
        img.alpha_composite(ss.get())
    return camz(img, 1.0 + 0.12 * easeio(lt / max(1, ctx.dur)), 560, 1200)


def seal(ctx, lt):
    img = section(lt, roach_on=False)
    t5 = ctx.wt("5"); tt = ctx.wt("tampa")
    gas_puffs(img, lt, ease((lt - tt + 1.0) / 0.6))
    ss = SS(W, H, s=2)
    q = ease((lt - t5 + 0.1) / 0.4)
    if q > 0:
        top, bot = Y_W, 1465
        for x in (720,):
            ss.line([(x, top), (x, top + (bot - top) * q)], (255, 222, 40), 8, cap=False)
            ss.line([(x - 22, top), (x + 22, top)], (255, 222, 40), 8, cap=False)
            if q > 0.95: ss.line([(x - 22, bot), (x + 22, bot)], (255, 222, 40), 8, cap=False)
        ss.text((800, (top + bot) / 2), "5 cm", 54, "anton", fill=(255, 222, 40), stroke=6)
    qb = ease((lt - tt - 0.2) / 0.3)
    if qb > 0:
        ss.line([(690, 1300), (760, 1370)], (230, 50, 60, int(255 * qb)), 16)
        ss.line([(690, 1370), (760, 1300)], (230, 50, 60, int(255 * qb)), 16)
    img.alpha_composite(ss.get())
    return camz(img, 1.75, 600, 1400)


def flush(ctx, lt):
    te = ctx.wt("empurra"); tr = ctx.wt("renova")
    mixu = clamp01((lt - te + 0.2) / max(0.6, tr - te + 0.8))
    img = section(lt, level=Y_W, wcol=mixc(WATER_OLD, WATER, mixu))
    flow_particles(img, lt, 34, (150, 240, 255), 0.4, 0.0, 0.62, a=int(255 * clamp01(lt / 0.4) * (1 - clamp01((lt - tr - 0.8) / 0.5))))
    p, o = all_pipe(); ss = SS(W, H, s=2)
    for i in range(14):
        u = 0.55 + 0.45 * ((i / 14 + lt * 0.3) % 1.0)
        x, y = path_point(u, p, o)
        ss.circle(x, y + 8 * math.sin(i), 12, fill=(*WATER_OLD, int(230 * (1 - mixu * 0.7))), ink=(*INK, 120), w=1.5)
    for k in range(10):
        v = (lt * 1.2 + k / 10) % 1.0
        ss.line([(380 + k * 9, v * FLOOR_Y - 60), (380 + k * 9, v * FLOOR_Y)], (150, 220, 255, 200), 6)
    img.alpha_composite(ss.get())
    return camz(img, 1.08, 560, 1100)


# ======================================================================= cena 5: Visão do Bicho (o cheiro)
def vision(ctx, lt):
    img = section(lt, roach_on=False)
    u = ease((lt - 0.25) / 0.7)
    rgb = np.asarray(img.convert("RGB"), dtype=np.float32)
    g = rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    dark = np.stack([g * 0.22, g * 0.2, g * 0.3], axis=2)
    img = Image.fromarray(np.clip(rgb * (1 - u) + dark * u, 0, 255).astype(np.uint8)).convert("RGBA")
    img.alpha_composite(water_layer(Y_W, WATER, int(120 + 120 * u)))
    for k in range(14):
        v = (lt * 0.3 + k / 14) % 1.0
        x = lerp(1060, 690, min(1, v * 1.3)) + (20 * math.sin((v - 0.77) * 25) if v > 0.77 else 0)
        y = 1350 + 25 * math.sin(lt * 2 + k * 1.3)
        col = STINK2 if k % 2 else (220, 200, 70)
        A.paste_c(img, A.glow(int(60 + 30 * math.sin(lt * 3 + k)), col, int(80 + 170 * u)), x, y)
    ss = SS(W, H, s=2)
    rx, ry = 420, lerp(1080, 1180, easeio(lt / max(1, ctx.dur)))
    for k in range(3):
        w_ = (lt * 0.9 + k / 3) % 1.0
        ss.ellipse(rx, ry + 140, 40 + 140 * w_, 30 + 90 * w_, ink=(255, 230, 120, int(200 * (1 - w_) * u)), w=5)
    roach(ss, rx, ry, 110, rot=180, t=lt, walk=0.5, ant=2.0)
    img.alpha_composite(ss.get())
    tp = ctx.wt("para")
    q = ease((lt - tp) / 0.3)
    if q > 0:
        ss = SS(W, H, s=2)
        ss.line([(700, 1280), (700, 1420)], (255, 222, 40, int(255 * q)), 10, cap=False)
        img.alpha_composite(ss.get())
    return camz(img, 1.55 + 0.04 * math.sin(lt * 0.6), 560, 1300)


# ======================================================================= cena 6: ventilação até o telhado
def house_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (150, 200, 230)), (0.25, (200, 226, 236)), (0.26, (236, 226, 206)), (0.7, (230, 220, 200)),
                            (0.71, (110, 94, 76)), (1, (66, 54, 44))])
        ss = SS(W, H, s=2)
        ss.poly([(-20, 520), (540, 300), (1100, 520)], fill=(196, 92, 70), ink=INK, w=6)
        ss.rect(0, 1000, W, 1030, fill=(150, 146, 140))
        ss.line([(820, 250), (820, 1700)], INK, 76); ss.line([(820, 250), (820, 1700)], (236, 240, 244), 62)
        ss.rrect(790, 220, 850, 262, 8, fill=(196, 200, 206), ink=INK, w=4)
        ss.line([(200, 1350), (300, 1450), (300, 1430), (800, 1480)], INK, 66)
        ss.line([(200, 1350), (300, 1450), (300, 1430), (800, 1480)], (236, 240, 244), 52)
        ss.line([(200, 1000), (200, 1340)], INK, 66); ss.line([(200, 1000), (200, 1340)], (236, 240, 244), 52)
        ss.rrect(560, 860, 720, 1000, 30, fill=(250, 250, 250), ink=INK, w=5)
        ss.rrect(600, 760, 720, 870, 16, fill=(250, 250, 250), ink=INK, w=5)
        ss.line([(660, 1000), (660, 1100), (800, 1140)], INK, 60); ss.line([(660, 1000), (660, 1100), (800, 1140)], (236, 240, 244), 48)
        ss.text((260, 940), "ralo", 40, "mont-Black", fill=(70, 70, 80))
        ss.text((640, 720), "vaso", 40, "mont-Black", fill=(70, 70, 80))
        im.alpha_composite(ss.get())
        return im
    return cached("house", mk)


def vent(ctx, lt):
    img = house_bg().copy()
    ts = ctx.wt("sugar")
    fl = ease((lt - ts + 0.4) / 0.5)
    ss = SS(W, H, s=2)
    for k in range(8):
        u = (lt * 0.5 + k / 8) % 1.0
        y = lerp(200, 1600, u)
        A.arrow(ss, 820, y - 50, 820, y + 20, (*AIR, int(240 * math.sin(math.pi * u))), w=22, iw=3)
    ss.text((930, 200), "ar", 50, "anton", fill=(40, 140, 60), stroke=0)
    if fl > 0:
        for k in range(10):
            u = (lt * 0.9 + k / 10) % 1.0
            if u < 0.4: x, y = 660, lerp(1000, 1100, u / 0.4)
            else: x, y = lerp(660, 800, (u - 0.4) / 0.6), lerp(1100, 1140, (u - 0.4) / 0.6)
            if k / 10 < fl: ss.circle(x, y, 12, fill=(120, 210, 255), ink=INK, w=2)
            ss.circle(820, lerp(1150, 1650, u), 12 * fl, fill=(120, 210, 255), ink=INK, w=2)
    ss.ellipse(250, 1405, 46, 18, fill=(*WATER, 255), ink=INK, w=3)
    if fl > 0.5:
        ss.text((250, 1520), "o sifão continua cheio", 34, "mont-Black", fill=(255, 255, 255), stroke=5)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    roach(ss, 110 + 40 * math.sin(lt * 0.5), 1000 - 40, 90, rot=80, t=lt, walk=0.6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * easeio(lt / max(1, ctx.dur)), rot=0.3 * math.sin(lt * 0.7))


# ======================================================================= cena 7: ralo seco -> loop para a grelha
def dry(ctx, lt):
    tpay = ctx.beat_t(2)
    if lt >= tpay - 0.05:
        tt = lt - ctx.dur + 1 / 30.0
        return grate_frame(tt, fog=0.0, reach=0.0)
    tev = ctx.wt("evapora")
    lev = lerp(Y_W, 1530, easeio((lt - 0.3) / max(0.8, tev + 0.6)))
    img = section(lt, level=lev, wcol=mixc(WATER, WATER_OLD, clamp01(lt / 2)))
    ss = SS(W, H, s=2)
    for k in range(6):
        u = (lt * 0.7 + k / 6) % 1.0
        x = 420 + 30 * math.sin(u * 8 + k); y = lev - 20 - u * 300
        ss.line([(x, y), (x + 10 * math.sin(u * 12), y - 50)], (255, 255, 255, int(160 * (1 - u))), 6)
    img.alpha_composite(ss.get())
    gas_puffs(img, lt, ease((lt - tev) / 0.5), through=1.0)
    return camz(img, 1.12, 540, 1150)


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    img = grate_bg().copy()
    ss = SS(W, H, s=2)
    for k in range(-4, 5):
        x = GX + k * 56 + 28
        ss.poly([(x - 18, GY - GR + 40), (x + 18, GY - GR + 40), (x + 80 + k * 40, H), (x - 80 + k * 40, H)], fill=(255, 240, 200, 30))
    img.alpha_composite(ss.get())
    stink(img, 1.0, 0.7)
    return A.cam(img, dy=300)


def cover_sprite(cv):
    s = cv.get("sprite_s", 330)
    ss = SS(int(1.35 * s), int(2.05 * s), s=2)
    roach(ss, 0.675 * s, 1.3 * s, s, t=0.2, walk=0.6)
    return ss.get()
