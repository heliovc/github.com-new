"""Dia 3A — "E se você fosse um krill na boca da baleia-azul?" (formato CURTO; paleta: azul-cobalto ensolarado,
krill coral translúcido, barbatanas grafite).

Cenas: mouth (gancho: a boca da baleia vindo do fundo, de frente), vision/vision2 (Visão do Bicho: olho composto
olhando para a luz de cima; a sombra da baleia apaga a luz), gulp (abre a boca, a garganta estica como sanfona),
gulp2 (mais água que o corpo dela), pool (milhares de krill lá dentro), filter (fecha e espreme a água: verde = água),
filter2 (a água passa pelas barbatanas), stuck (o krill fica), count (16 toneladas por dia), loop (volta ao quadro
inicial).
Fatos: Goldbogen et al. (2011, 2016), Savoca et al. (2021, Nature).
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, mixc, INK
from scenes.common import cached

KR = (255, 118, 104); KR_L = (255, 186, 160); KR_D = (196, 64, 66)
PHOTO = (110, 230, 255)
WH = (52, 74, 104); WH_D = (34, 50, 76); WH_L = (120, 146, 170)
BALEEN = (44, 42, 48); FRINGE = (150, 140, 128)
MOUTH = (34, 16, 34); TONGUE = (206, 96, 118)
WATER = (80, 230, 150)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= krill (perfil, cabeça para a direita)
def krill(ss, x, y, s, t=0.0, rot=0.0, flip=1, eye=1.0):
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.2, s * 0.010)
    # antenas longas
    for (tx, ty, k) in ((1.05, -0.36, 0), (0.98, -0.16, 1)):
        wv = 0.03 * math.sin(t * 3 + k)
        pts = A.bez((0.44, -0.04), (0.62, -0.12 + wv), (0.82, ty * 0.6 - wv), (tx, ty + wv), 12)
        ss.line(P(pts), (*KR_D, 230), max(1.2, s * 0.008), cap=False)
    # patas nadadoras (batem)
    for k in range(5):
        hx = -0.02 - k * 0.09; ph = t * 14 + k * 0.9
        ex = hx - 0.05 + 0.05 * math.sin(ph); ey = 0.17 + 0.03 * math.cos(ph)
        ss.line(P([(hx, 0.06), (ex, ey)]), (*KR_D, 220), max(1.2, s * 0.014))
    # cesto de alimentação (patas do tórax, em pente)
    for k in range(6):
        hx = 0.12 + k * 0.045
        ss.line(P([(hx, 0.07), (hx + 0.02, 0.16 + 0.01 * math.sin(t * 6 + k))]), (*KR_D, 200), max(1, s * 0.008))
    # abdome em segmentos, curvando para baixo até a cauda
    segs = []
    for k in range(6):
        u = k / 5
        cx = lerp(0.02, -0.40, u); cy = 0.015 + 0.09 * u * u
        segs.append((cx, cy, lerp(0.078, 0.045, u)))
    for (cx, cy, r) in reversed(segs):
        ss.poly(P(A.ell_pts(cx, cy, r * 1.05, r, -10, 22)), fill=(*KR, 236), ink=(*INK, 200), w=iw)
        ss.poly(P(A.ell_pts(cx, cy - r * 0.35, r * 0.7, r * 0.35, -10, 16)), fill=(*KR_L, 160))
    # cauda em leque
    tx, ty = -0.47, 0.14
    for ang in (-28, 0, 28):
        a = math.radians(200 + ang)
        ss.poly(P(A.ell_pts(tx + 0.07 * math.cos(a), ty + 0.07 * math.sin(a), 0.085, 0.03, 200 + ang, 16)),
                fill=(*KR, 220), ink=(*INK, 180), w=iw * 0.8)
    # carapaça
    ss.poly(P(A.ell_pts(0.25, 0.0, 0.22, 0.095, -4, 36)), fill=(*KR, 240), ink=(*INK, 220), w=iw)
    ss.poly(P(A.ell_pts(0.22, -0.04, 0.16, 0.035, -4, 20)), fill=(*KR_L, 170))
    # vísceras verdes (comida) e fotóforos azuis
    ss.poly(P(A.ell_pts(0.18, 0.025, 0.08, 0.035, 0, 16)), fill=(120, 170, 70, 150))
    for (px, py) in ((0.30, 0.07), (0.08, 0.07), (-0.1, 0.08), (-0.25, 0.11)):
        q = P([(px, py)])[0]
        ss.circle(q[0], q[1], s * 0.016, fill=(*PHOTO, 230), ink=(*INK, 120), w=1)
    # olho grande e preto, com pedúnculo
    ex, ey = P([(0.42, -0.035)])[0]; er = s * 0.062 * eye
    ss.circle(ex, ey, er * 1.12, fill=KR_D)
    ss.circle(ex, ey, er, fill=(16, 10, 20), ink=INK, w=iw)
    ss.circle(ex - er * 0.32, ey - er * 0.34, er * 0.34, fill=(255, 255, 255, 240))
    ss.circle(ex + er * 0.3, ey + er * 0.3, er * 0.12, fill=(255, 255, 255, 170))


def mini(col_a=235, s=60):
    def mk():
        ss = SS(int(1.7 * s), int(0.75 * s), s=2)
        krill(ss, 0.82 * s, 0.32 * s, s, t=0.4)
        return ss.get()
    return cached(("mini", s), mk)


def swarm(img, t, n, seed, box, size=(26, 60), drift=(30, 8), alpha=1.0, to=None, pull=0.0):
    """cardume de krill (sprites pequenos); to=(x,y) puxa o cardume para lá (pull 0..1)"""
    rng = np.random.default_rng(seed)
    x0, y0, x1, y1 = box
    for k in range(n):
        bx, by = rng.uniform(x0, x1), rng.uniform(y0, y1)
        sz = int(rng.uniform(*size)); ph = rng.uniform(0, 6.28)
        x = bx + drift[0] * math.sin(t * 0.7 + ph); y = by + drift[1] * math.sin(t * 1.3 + ph * 1.7)
        if to is not None and pull > 0:
            q = clamp01(pull * (1.2 + 0.6 * rng.random()) - rng.random() * 0.25)
            q = ease(q)
            x, y = lerp(x, to[0], q), lerp(y, to[1], q)
            sz = int(sz * (1 - 0.5 * q))
        if sz < 6: continue
        sp = mini(s=60).resize((int(sz * 1.7), int(sz * 0.75)), Image.BILINEAR)
        if rng.random() < 0.4: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
        A.paste_c(img, sp, x, y, alpha * (0.6 + 0.4 * rng.random()))


# ======================================================================= oceano
def ocean_bg(dark=0.0):
    def mk():
        im = A.vgrad(W, H, [(0, (120, 210, 245)), (0.18, (40, 140, 220)), (0.55, (18, 72, 168)), (1, (8, 26, 90))])
        A.paste_c(im, A.glow(800, (200, 245, 255), 120), 540, -120)
        return im
    base = cached("ocean", mk)
    if dark <= 0: return base.copy()
    im = base.copy()
    im.alpha_composite(Image.new("RGBA", (W, H), (4, 10, 30, int(220 * clamp01(dark)))))
    return im


def rays(img, t, a=60):
    ss = SS(W, H, s=1)
    for k in range(7):
        x = 120 + k * 150 + 40 * math.sin(t * 0.4 + k)
        w = 60 + 30 * math.sin(t * 0.6 + k * 2)
        ss.poly([(x - w, -10), (x + w, -10), (x + w * 3 + 160, H), (x - w + 160, H)],
                fill=(220, 250, 255, int(a * (0.5 + 0.5 * math.sin(t * 0.8 + k * 1.3)) ** 2)))
    img.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(18)))


def specks(img, t, n=60, seed=4, a=110):
    rng = np.random.default_rng(seed); ss = SS(W, H, s=1)
    for _ in range(n):
        x = rng.uniform(0, W); y0 = rng.uniform(0, H); r = rng.uniform(1.5, 4)
        y = (y0 - t * 25 * r) % H
        ss.circle(x + 8 * math.sin(t + y0), y, r, fill=(230, 250, 255, int(a * rng.uniform(0.4, 1))))
    img.alpha_composite(ss.get())


# ======================================================================= baleia de frente (boca aberta)
def whale_front(cx, cy, s, open_u):
    """sprite da cabeça da baleia vista de frente; s = meia largura da cabeça (px)"""
    w, h = int(2.3 * s), int(2.2 * s)
    ss = SS(w, h, s=2)
    ox, oy = w / 2, h * 0.45
    P = lambda pts: [(ox + px * s, oy + py * s) for px, py in pts]
    head = A.spline([(-1.0, -0.1), (-0.8, -0.55), (-0.3, -0.72), (0.3, -0.72), (0.8, -0.55), (1.0, -0.1),
                     (0.95, 0.4 + 0.3 * open_u), (0.5, 0.75 + 0.35 * open_u), (0, 0.85 + 0.4 * open_u),
                     (-0.5, 0.75 + 0.35 * open_u), (-0.95, 0.4 + 0.3 * open_u)], 8)
    ss.poly(P(head), fill=WH, ink=INK, w=6)
    rng = np.random.default_rng(3)
    for _ in range(40):
        px, py = rng.uniform(-0.8, 0.8), rng.uniform(-0.6, 0.0)
        ss.oval(ox + px * s, oy + py * s, s * rng.uniform(0.02, 0.06), s * rng.uniform(0.015, 0.04), rng.uniform(0, 180),
                fill=(*WH_L, 110))
    # boca
    mo = 0.12 + 0.62 * open_u
    mouth = A.spline([(-0.86, 0.0), (-0.5, -0.12), (0, -0.16), (0.5, -0.12), (0.86, 0.0),
                      (0.7, mo * 0.8), (0, mo + 0.05), (-0.7, mo * 0.8)], 8)
    ss.poly(P(mouth), fill=MOUTH, ink=INK, w=5)
    if open_u > 0.2:
        ss.poly(P(A.ell_pts(0, mo * 0.75, 0.42, 0.14 * open_u, 0, 30)), fill=(*TONGUE, int(230 * open_u)))
    # barbatanas: cortina pendurada da mandíbula de cima
    nb = 34
    for k in range(nb):
        u = k / (nb - 1); bx = lerp(-0.8, 0.8, u)
        top = -0.12 - 0.04 * math.cos(u * math.pi - math.pi / 2) - 0.0
        top = lerp(-0.02, -0.16, math.sin(u * math.pi))
        L = (0.12 + 0.22 * open_u) * math.sin(0.2 + u * 2.74) + 0.04
        ss.poly(P([(bx - 0.022, top), (bx + 0.022, top), (bx + 0.01, top + L), (bx - 0.01, top + L * 1.05)]),
                fill=BALEEN, ink=(*INK, 200), w=1.5)
        ss.line(P([(bx, top + L * 0.6), (bx + 0.01, top + L * 1.15)]), (*FRINGE, 200), max(1, s * 0.008), cap=False)
    # pregas da garganta
    for k in range(9):
        u = (k - 4) / 4.5
        ss.line(P(A.bez((u * 0.75, mo + 0.12), (u * 0.8, mo + 0.3), (u * 0.6, 0.7 + 0.35 * open_u), (u * 0.35, 0.82 + 0.38 * open_u), 10)),
                (*WH_L, 150), max(2, s * 0.012), cap=False)
    # olhinhos nas laterais
    for sg in (-1, 1):
        ss.circle(ox + sg * 0.93 * s, oy + 0.02 * s, s * 0.035, fill=(12, 10, 16), ink=INK, w=2)
    return ss.get()


def whale_far(img, cx, cy, s, open_u, dark=0.0):
    sp = whale_front(cx, cy, s, open_u)
    if dark > 0:
        ov = Image.new("RGBA", sp.size, (10, 30, 80, 0))
        tint = Image.new("RGBA", sp.size, (10, 30, 80, int(200 * dark)))
        tint.putalpha(Image.fromarray((np.asarray(sp.split()[3], np.float32) * dark * 0.8).astype(np.uint8)))
        sp = sp.copy(); sp.alpha_composite(tint)
    A.paste_c(img, sp, cx, cy + sp.height * 0.05)


# ======================================================================= cena 1: gancho (boca vindo)
def mouth_frame(t, ws=None, op=None, haze=None):
    img = ocean_bg()
    rays(img, t)
    ws = (360 + 22 * t) if ws is None else ws
    op = (0.55 + 0.08 * math.sin(t * 0.9) + 0.06 * t) if op is None else op
    hz = clamp01(0.35 - 0.03 * t) if haze is None else haze
    whale_far(img, 540, 760, ws, clamp01(op), dark=hz)
    specks(img, t)
    swarm(img, t, 26, 7, (60, 300, 1020, 1100), size=(16, 34), alpha=0.85)
    ss = SS(W, H, s=2)
    krill(ss, 480, 1500 + 12 * math.sin(t * 2.2), 520, t=t, rot=-8 + 3 * math.sin(t * 1.4), flip=1)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 20, 0.3, col=(4, 14, 50))
    A.paste(img, sh, -pad + 10, -pad + 30)
    img.alpha_composite(sp)
    swarm(img, t, 6, 11, (-40, 1300, 1120, 1800), size=(60, 90), drift=(40, 12), alpha=0.95)
    return img


def mouth(ctx, lt):
    return A.cam(mouth_frame(lt), zoom=1.02 + 0.01 * math.sin(lt * 1.1), rot=0.4 * math.sin(lt * 0.7))


# ======================================================================= cenas 2-3: Visão do Bicho (olho composto)
def pov_antennae(img, t):
    ss = SS(W, H, s=2)
    for sg in (-1, 1):
        pts = A.bez((540 + sg * 260, H + 20), (540 + sg * 330, 1500), (540 + sg * 420 + 30 * math.sin(t * 1.6 + sg), 1000),
                    (540 + sg * 560 + 40 * math.sin(t * 1.2 + sg), 640), 16)
        ss.line(pts, (*KR_D, 255), 16); ss.line(pts, (*KR, 255), 9)
    for sg in (-1, 1):
        ss.circle(540 + sg * 420, H + 60, 150, fill=(*KR, 255), ink=INK, w=6)
    img.alpha_composite(ss.get())


def whale_shadow(cov):
    """silhueta da baleia vista de baixo, cobrindo a luz"""
    ss = SS(W, H, s=2)
    x = lerp(1700, 540, ease(cov)); y = 620
    body = A.spline([(x - 1300, y + 40), (x - 700, y - 160), (x, y - 230), (x + 600, y - 170), (x + 900, y),
                     (x + 600, y + 170), (x, y + 230), (x - 700, y + 160)], 8)
    ss.poly(body, fill=(6, 16, 40, 245))
    for sg in (-1, 1):
        ss.poly([(x + 200, y + sg * 170), (x - 80, y + sg * 520), (x - 200, y + sg * 520), (x - 60, y + sg * 160)], fill=(6, 16, 40, 245))
    ss.poly([(x - 1250, y), (x - 1500, y - 260), (x - 1420, y), (x - 1500, y + 260)], fill=(6, 16, 40, 245))
    return ss.get().filter(ImageFilter.GaussianBlur(6))


def vision(ctx, lt):
    second = ctx.sc["id"] == "vision2"
    t = lt + (3.0 if second else 0.0)
    img = A.vgrad(W, H, [(0, (210, 250, 255)), (0.25, (60, 170, 240)), (0.7, (16, 70, 170)), (1, (8, 30, 100))])
    ss = SS(W, H, s=1)
    for k in range(14):  # ondas da superfície
        y = 90 + k * 34 + 6 * math.sin(t * 2 + k)
        ss.line([(x, y + 12 * math.sin(x / 70 + t * 2 + k)) for x in range(-20, W + 40, 40)], (255, 255, 255, 120 - k * 7), 5, cap=False)
    img.alpha_composite(ss.get())
    rays(img, t, 90)
    swarm(img, t, 30, 21, (40, 380, 1040, 1250), size=(24, 46), alpha=0.9)
    if second:
        cov = ease((lt - ctx.wt("sombra") + 0.2) / 1.6)
        img.alpha_composite(whale_shadow(cov))
        da = clamp01((lt - ctx.wt("apaga")) / 0.7)
        if da > 0: img.alpha_composite(Image.new("RGBA", (W, H), (2, 8, 30, int(150 * da))))
    pov_antennae(img, t)
    rgb = np.asarray(img.convert("RGB"), np.float32)
    rgb[..., 0] *= 0.55; rgb[..., 1] *= 0.9          # o olho do krill vê melhor o azul
    img = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA")
    return A.cam(img, zoom=1.03 + 0.02 * math.sin(lt * 0.8), dx=8 * math.sin(lt * 1.3))


# ======================================================================= baleia de lado
def whale_side(ss, x, y, s, mouth_u=0.0, pouch=0.0, xray=0.0, water=0.0, tongue=0.0):
    """cabeça para a direita; (x,y) = ponta do focinho; s = escala (comprimento da cabeça ~ s)"""
    P = lambda pts: [(x + px * s, y + py * s) for px, py in pts]
    ang = math.radians(32 * mouth_u)
    hinge = (-0.95, 0.1)
    def rot(p):
        dx, dy = p[0] - hinge[0], p[1] - hinge[1]
        return (hinge[0] + dx * math.cos(ang) - dy * math.sin(ang), hinge[1] + dx * math.sin(ang) + dy * math.cos(ang))
    # corpo (vai para fora da tela à esquerda)
    body = [(-3.2, -0.55), (-2.0, -0.62), (-1.0, -0.42), (0.0, -0.12), (0.05, 0.0), (-0.95, 0.1), (-1.6, 0.5), (-3.2, 0.5)]
    ss.poly(P(body), fill=WH, ink=INK, w=5)
    # mandíbula de baixo + bolsa da garganta (estica)
    pb = 0.25 + 0.95 * pouch
    jaw = [rot(p) for p in [(-0.95, 0.1), (0.0, 0.05), (-0.05, 0.12)]]
    poch = [rot(p) for p in [(-0.15, 0.14 + 0.25 * pouch), (-0.5, 0.2 + pb * 0.9), (-1.0, 0.25 + pb), (-1.6, 0.25 + pb * 0.75)]] + [(-2.1, 0.45)]
    shape = jaw + poch + [(-1.6, 0.5)]
    ss.poly(P(A.spline(shape, 6)), fill=(220, 212, 214), ink=INK, w=5)
    # pregas (sanfona): mais afastadas quando estica
    for k in range(10):
        u = (k + 0.5) / 10
        a0 = rot((lerp(-0.05, -1.8, u * 0.1 + 0.0), 0.12))
        pts = [rot((lerp(-0.1, -1.9, v), lerp(0.12, 0.2 + pb * 0.95 * math.sin(v * math.pi * 0.9 + 0.2), 0) + u * (0.06 + pb * 0.85) * math.sin(0.25 + v * 2.6)))
               for v in np.linspace(0, 1, 14)]
        ss.line(P(pts), (150, 140, 150), max(2, s * (0.008 + 0.006 * pouch)), cap=False)
    # boca por dentro + barbatanas
    if mouth_u > 0.02:
        inside = [(-0.95, 0.1), (0.0, -0.1)] + [rot(p) for p in [(0.0, 0.05), (-0.95, 0.1)]]
        ss.poly(P(inside), fill=MOUTH)
        nb = 24
        for k in range(nb):
            u = k / nb; bx = lerp(-0.05, -0.9, u); by = lerp(-0.1, 0.08, u)
            L = 0.22 * mouth_u * (0.6 + 0.4 * math.sin(u * math.pi))
            ss.line(P([(bx, by), (bx - 0.01, by + L)]), BALEEN, max(3, s * 0.016), cap=False)
            ss.line(P([(bx - 0.01, by + L * 0.7), (bx - 0.02, by + L * 1.1)]), FRINGE, max(1.5, s * 0.006), cap=False)
    if xray > 0:
        cav = [(-0.1, -0.06), (-0.9, 0.08)] + [rot(p) for p in [(-1.0, 0.22 + pb * 0.85), (-0.5, 0.18 + pb * 0.75), (-0.1, 0.08)]]
        ss.poly(P(A.spline(cav, 6)), fill=(*WATER, int(150 * water * xray)))
        if tongue > 0:
            tg = [rot(p) for p in [(-1.0, 0.2 + pb * (0.85 - 0.6 * tongue)), (-0.55, 0.12 + pb * (0.7 - 0.55 * tongue)),
                                   (-0.15, 0.1), (-0.6, 0.25 + pb * 0.9), (-1.05, 0.3 + pb * 0.9)]]
            ss.poly(P(A.spline(tg, 6)), fill=(*TONGUE, int(230 * xray)), ink=(*INK, 180), w=3)
    # olho e nadadeira
    ss.circle(*P([(-1.05, 0.02)])[0], s * 0.03, fill=(12, 10, 16), ink=INK, w=2)
    ss.circle(*P([(-1.06, 0.01)])[0], s * 0.01, fill=(255, 255, 255))
    ss.poly(P([(-1.5, 0.35), (-1.9, 0.95), (-2.05, 0.9), (-1.85, 0.35)]), fill=WH_D, ink=INK, w=4)
    for k in range(16):
        ss.circle(*P([(-0.4 - k * 0.17, -0.3 + 0.12 * math.sin(k * 2.1))])[0], s * 0.015, fill=(*WH_L, 140))


# ======================================================================= cena 4: abre a boca, garganta estica
def gulp(ctx, lt):
    img = ocean_bg(); rays(img, lt + 5, 50); specks(img, lt, 40, 8)
    mu = ease(lt / 0.9)
    pu = ease((lt - ctx.wt("estica") + 0.2) / 1.6)
    mx, my = 960, 760
    swarm(img, lt, 50, 31, (650, 500, 1100, 1100), size=(14, 30), to=(mx - 200, my + 120), pull=pu * 0.8)
    ss = SS(W, H, s=2)
    whale_side(ss, mx, my, 620, mouth_u=mu, pouch=pu)
    img.alpha_composite(ss.get())
    swarm(img, lt, 10, 33, (700, 400, 1100, 1300), size=(30, 50), to=(mx - 150, my + 100), pull=pu)
    if pu > 0.05:
        ss = SS(W, H, s=2)
        for k in range(2):
            A.arrow(ss, 300 + k * 260, 1340, 300 + k * 260, 1340 + 260 * pu, (255, 222, 40), w=34, iw=5)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.05 - 0.05 * easeio(lt / max(1, ctx.dur)), dx=-40 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 5: mais água que o corpo dela
def gulp2(ctx, lt):
    img = A.vgrad(W, H, [(0, (24, 96, 190)), (1, (10, 36, 110))])
    specks(img, lt, 40, 9)
    tc = ctx.wt("corpo")
    q = ease((lt - tc + 0.9) / 1.3)
    ss = SS(W, H, s=2)
    # baleia inteira (silhueta) em cima
    cx, cy, L = 540, 560, 880
    body = A.spline([(cx - L / 2, cy), (cx - L * 0.2, cy - 70), (cx + L * 0.3, cy - 80), (cx + L / 2, cy - 10),
                     (cx + L * 0.3, cy + 70), (cx - L * 0.2, cy + 60)], 8)
    ss.poly(body, fill=WH, ink=INK, w=5)
    ss.poly([(cx - L / 2 + 20, cy), (cx - L / 2 - 90, cy - 80), (cx - L / 2 - 60, cy), (cx - L / 2 - 90, cy + 80)], fill=WH, ink=INK, w=5)
    ss.circle(cx + L * 0.36, cy - 10, 9, fill=(12, 10, 16))
    ss.text((cx, cy + 150), "o corpo dela", 52, "anton", fill=(255, 255, 255), stroke=6)
    # bolha de água (verde) crescendo até passar do tamanho da baleia
    r = lerp(60, 330, q) + 8 * math.sin(lt * 4)
    by = 1550
    ss.ellipse(cx, by, r * 1.45, r * 0.95, fill=(*WATER, 150), ink=(20, 90, 60), w=6)
    ss.ellipse(cx - r * 0.5, by - r * 0.4, r * 0.4, r * 0.2, fill=(255, 255, 255, 90))
    # contorno tracejado da baleia sobre a bolha (para comparar)
    if q > 0.6:
        a = int(255 * clamp01((q - 0.6) / 0.3))
        sb = A.spline([(cx - L / 2 * 0.62, by), (cx - L * 0.12, by - 44), (cx + L * 0.19, by - 50), (cx + L / 2 * 0.62, by - 6),
                       (cx + L * 0.19, by + 44), (cx - L * 0.12, by + 38)], 8)
        for k in range(0, len(sb) - 1, 2):
            ss.line([sb[k], sb[k + 1]], (255, 255, 255, a), 6)
    img.alpha_composite(ss.get())
    swarm(img, lt, 40, 41, (cx - r, by - r * 0.6, cx + r, by + r * 0.6), size=(10, 22), alpha=min(1.0, q * 1.5))
    return A.cam(img, zoom=1.0 + 0.03 * q, dy=-10 * q)


# ======================================================================= cena 6: piscina cheia de krill
def pool(ctx, lt):
    img = A.vgrad(W, H, [(0, (40, 14, 34)), (0.6, (70, 24, 48)), (1, (120, 44, 66))])
    ss = SS(W, H, s=2)
    for k in range(30):  # cortina de barbatanas em cima
        x = k * 38; L = 300 + 60 * math.sin(k * 1.7)
        ss.poly([(x, -10), (x + 34, -10), (x + 26, L), (x + 8, L + 10)], fill=BALEEN, ink=(*INK, 200), w=2)
        ss.line([(x + 17, L - 40), (x + 15, L + 60)], (*FRINGE, 200), 3, cap=False)
    ss.poly(A.spline([(-50, 1500), (300, 1420), (800, 1430), (1130, 1500), (1130, 1980), (-50, 1980)], 6), fill=TONGUE, ink=INK, w=5)
    img.alpha_composite(ss.get())
    img.alpha_composite(A.glow(700, (80, 230, 150), 50), (-160, 160))
    tm = ctx.wt("milhares")
    q = ease((lt - tm + 0.6) / 1.0)
    n = int(40 + 220 * q)
    rng = np.random.default_rng(5)
    for k in range(n):
        a = rng.uniform(0, 6.28) + lt * (0.3 + 0.4 * rng.random()); rr = rng.uniform(40, 520)
        x = 540 + rr * math.cos(a) * 1.0; y = 900 + rr * math.sin(a) * 0.95
        sz = int(rng.uniform(14, 34))
        sp = mini(s=60).resize((int(sz * 1.7), int(sz * 0.75)), Image.BILINEAR)
        if math.sin(a) > 0: sp = sp.transpose(Image.FLIP_LEFT_RIGHT)
        A.paste_c(img, sp, x, y, 0.95)
    ss = SS(W, H, s=2)
    krill(ss, 540, 1620, 300, t=lt, rot=-6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)), rot=1.2 * math.sin(lt * 0.6))


# ======================================================================= cena 7: fecha e espreme
def filter(ctx, lt):
    img = ocean_bg(); rays(img, lt + 9, 40); specks(img, lt, 40, 12)
    tf = ctx.wt("fecha"); te = ctx.wt("espreme")
    mu = 1 - ease((lt - tf + 0.2) / 0.7)
    tg = ease((lt - te + 0.1) / 1.4)
    pouch = 1 - 0.6 * tg
    mx, my = 860, 760
    ss = SS(W, H, s=2)
    whale_side(ss, mx, my, 640, mouth_u=0.35 * mu, pouch=pouch, xray=1.0, water=1 - 0.8 * tg, tongue=tg)
    img.alpha_composite(ss.get())
    # krill ficam dentro (pontinhos rosa)
    rng = np.random.default_rng(8); ss = SS(W, H, s=2)
    for k in range(60):
        x = mx + rng.uniform(-0.95, -0.15) * 640; y = my + rng.uniform(0.1, 0.25 + 0.6 * pouch) * 640 * 0.85
        ss.circle(x + 6 * math.sin(lt * 3 + k), y, 7, fill=KR, ink=INK, w=1.5)
    # água saindo pelas laterais (verde)
    if tg > 0:
        for k in range(5):
            u = (lt * 1.2 + k / 5) % 1.0
            x0 = mx - 80 - k * 90; y0 = my + 30
            A.arrow(ss, x0, y0 - 10, x0 + 30, y0 - 120 - 260 * u, (*WATER, int(255 * tg * (1 - u * 0.6))), w=26, iw=4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03, dx=-30, dy=6 * tg * math.sin(lt * 9))


# ======================================================================= cena 8: barbatanas de perto
def baleen_close(img, t, hero_x=None, hero_rot=0.0):
    ss = SS(W, H, s=2)
    for k in range(9):  # placas verticais (vistas de dentro: franja na frente)
        x = -60 + k * 150
        ss.poly([(x, -20), (x + 110, -20), (x + 96, 1900), (x + 14, 1900)], fill=BALEEN, ink=(*INK, 230), w=4)
        ss.line([(x + 30, 0), (x + 30, 1900)], (70, 66, 74), 6, cap=False)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2); rng = np.random.default_rng(12)
    for k in range(420):  # franja (cerdas) por cima: a rede
        x = rng.uniform(-20, W + 20); y = rng.uniform(0, H)
        L = rng.uniform(80, 200); a = rng.uniform(-0.6, 0.6)
        ss.line([(x, y), (x + L * math.sin(a), y + L * math.cos(a))], (*FRINGE, 210), rng.uniform(2, 4), cap=False)
    img.alpha_composite(ss.get())


def filter2(ctx, lt):
    img = A.vgrad(W, H, [(0, (40, 18, 40)), (1, (74, 30, 56))])
    baleen_close(img, lt)
    ss = SS(W, H, s=2); rng = np.random.default_rng(14)
    for k in range(80):  # água atravessa (verde)
        y = rng.uniform(150, 1800); sp = rng.uniform(500, 900)
        x = (rng.uniform(0, W) + lt * sp) % (W + 200) - 100
        ss.line([(x - 70, y), (x, y)], (*WATER, 200), 5, cap=True)
        ss.circle(x, y, 6, fill=(*WATER, 230))
    img.alpha_composite(ss.get())
    rng = np.random.default_rng(15)  # krill batem e param
    for k in range(9):
        y = rng.uniform(300, 1700); t0 = rng.uniform(0, 1.6)
        x = lerp(-120, 520 + rng.uniform(-80, 80), ease(clamp01((lt - t0) / 0.8)))
        ss2 = SS(W, H, s=2); krill(ss2, x, y, rng.uniform(130, 200), t=lt + k, rot=rng.uniform(-15, 15))
        img.alpha_composite(ss2.get())
    return A.cam(img, zoom=1.04 + 0.02 * math.sin(lt), dx=6 * math.sin(lt * 7))


# ======================================================================= cena 9: eu fico
def stuck(ctx, lt):
    img = A.vgrad(W, H, [(0, (40, 18, 40)), (1, (74, 30, 56))])
    ss = SS(W, H, s=2); rng = np.random.default_rng(16)
    for k in range(60):
        y = rng.uniform(100, 1850); x = (rng.uniform(0, W) + lt * rng.uniform(700, 1100)) % (W + 200) - 100
        ss.line([(x - 90, y), (x, y)], (*WATER, 190), 6)
    img.alpha_composite(ss.get())
    tf = ctx.wt("fico")
    bump = clamp01((lt - tf + 0.1) / 0.15) * (1 - clamp01((lt - tf - 0.15) / 0.4))
    ss = SS(W, H, s=2)
    krill(ss, 520 + 30 * bump, 900, 760, t=lt, rot=-4, eye=1.0 + 0.25 * bump)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2); rng = np.random.default_rng(17)
    for k in range(70):  # cerdas na frente (o krill está preso nelas)
        x = 760 + rng.uniform(0, 380); y = rng.uniform(-50, H)
        L = rng.uniform(160, 320); a = rng.uniform(-0.4, 0.4)
        ss.line([(x, y), (x + L * math.sin(a), y + L * math.cos(a))], (*FRINGE, 235), rng.uniform(4, 8), cap=False)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.04 * bump, dx=-14 * bump * math.sin(lt * 40))


# ======================================================================= cena 10: 16 toneladas por dia
def count(ctx, lt):
    img = ocean_bg(); rays(img, lt, 70); specks(img, lt, 30, 18)
    t16 = ctx.wt("16")
    q = ease((lt - t16 + 0.3) / 1.6)
    ss = SS(W, H, s=2)
    # sol andando (um dia de caça) na superfície
    sx = lerp(140, 940, clamp01(lt / max(1, ctx.dur)))
    ss.circle(sx, 120, 50, fill=(255, 236, 150, 220))
    # 16 caixas de 1 tonelada, empilhando
    n = int(round(16 * q))
    for k in range(n):
        c, r = k % 4, k // 4
        x = 270 + c * 180; y = 1760 - r * 130
        ss.rrect(x - 80, y - 60, x + 80, y + 60, 14, fill=KR, ink=INK, w=5)
        ss.rrect(x - 66, y - 48, x + 66, y - 20, 8, fill=(*KR_L, 200))
        ss.text((x, y + 12), "1 t", 58, "anton", fill=(255, 255, 255), stroke=5)
    ss.text((540, 610), f"{int(16 * q)} t", 150, "anton", fill=(255, 222, 40, int(255 * clamp01(q * 3))), stroke=10)
    img.alpha_composite(ss.get())
    # baleia em silhueta passando ao fundo
    ss = SS(W, H, s=2)
    whale_side(ss, lerp(-100, 1300, lt / max(1, ctx.dur)), 860, 220, mouth_u=0.5 + 0.5 * math.sin(lt * 3), pouch=0.4)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dy=-8 * q)


# ======================================================================= cena 11: loop (volta ao quadro inicial)
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0                 # último quadro = t 0 do gancho
    back = easeio((lt - 0.6) / max(0.3, ctx.dur - 0.7))
    ws = lerp(600, 360 + 22 * tr, back)
    op = lerp(1.0, 0.55 + 0.08 * math.sin(tr * 0.9) + 0.06 * tr, back)
    hz = lerp(0.1, clamp01(0.35 - 0.03 * tr), back)
    img = mouth_frame(tr, ws=ws, op=op, haze=hz)
    return A.cam(img, zoom=lerp(1.12, 1.02 + 0.01 * math.sin(tr * 1.1), back), rot=0.4 * math.sin(tr * 0.7) * back)


# ======================================================================= capa (engine.write_cover v2)
def cover_bg(cv):
    img = ocean_bg(); rays(img, 1.0, 80)
    whale_far(img, 540, 900, 480, 0.9, dark=0.1)
    specks(img, 1.0)
    swarm(img, 1.0, 20, 7, (40, 300, 1040, 1700), size=(20, 40), alpha=0.8)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 340)
    ss = SS(int(1.75 * s), int(0.9 * s), s=2)
    krill(ss, 0.62 * s, 0.42 * s, s, t=0.3)
    return ss.get()
