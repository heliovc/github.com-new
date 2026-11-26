"""Dia 7A — "E se você fosse um elefante ouvindo pelos pés?" (formato CURTO; paleta: savana ao amanhecer, céu pêssego e
coral, chão de terra vermelha, acácias em silhueta vinho, elefante cinza-azulado, tremor do chão em magenta).

Cenas: hook (câmera rasteira: a pata gigante pisa e o chão ondula em anéis magenta), far (plano aberto: outro elefante no
horizonte chamando; você, pequeno, não ouve nada), vision (Visão do Bicho: tremor — o chão escuro com as ondas acesas
chegando nas minhas patas), rumble (barra de frequência: o ronco fica abaixo do que o ouvido humano pega), ground (corte:
onda no ar em verde e no chão em magenta), foot (raio-X do pé: almofada com sensores acendendo em amarelo), bones (o tremor
sobe pelos ossos até o ouvido), km (mapa: 2 km ≈ 19 campos de futebol), family (balão: família ✓ × estranho ✗),
loop (volta ao quadro inicial).
Fatos: O'Connell-Rodwell (2007, Physiology); O'Connell-Rodwell et al. (2007, JASA); Günther et al. (2004, J. Theor. Biol.).
"""
import math
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

SKIN = (132, 140, 156); SKIN_D = (92, 98, 116); SKIN_L = (172, 178, 192)
EAR_IN = (196, 150, 160)
TUSK = (246, 236, 210)
MAG = (255, 70, 170)        # tremor do chão
AIRG = (90, 230, 150)       # onda no ar (verde = ar)
YEL = (255, 222, 40)        # sinal nervoso (amarelo = eletricidade)
SOIL = (176, 84, 52); SOIL_D = (120, 54, 38); SOIL_L = (206, 120, 76)
WINE = (92, 36, 46)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= elefante (de lado, olhando para a direita)
def _leg(ss, P, hx, ph, s, iw, alpha, lift=0.1, swing=0.13, shade=False):
    l = max(0.0, math.sin(ph)) * lift
    fx = hx + swing * math.cos(ph)
    col = SKIN_D if shade else SKIN
    pts = [(hx - 0.13, -0.8), (hx + 0.13, -0.8), (fx + 0.12, -0.06 - l), (fx + 0.13, -l), (fx - 0.13, -l), (fx - 0.12, -0.06 - l)]
    ss.poly(P(pts), fill=(*col, alpha), ink=(*INK, alpha), w=iw)
    for k in (-0.07, 0.0, 0.07):
        x0, y0 = P([(fx + k, -l - 0.005)])[0]
        ss.circle(x0, y0, max(2, s * 0.018), fill=(*TUSK, alpha))
    return P([(fx, -l)])[0], l


def elephant(ss, x, y, s, t=0.0, walk=1.0, ear=0.0, trunk=0.0, eye=1.0, flip=1, alpha=255, mouth=0.0, phase=0.0):
    """origem = chão sob o meio do corpo; s = altura até o ombro (~1 unidade). walk: 0 parado .. 1 andando.
    Devolve a posição da pata dianteira da frente (para ondas no chão) e quanto ela está levantada."""
    P = lambda pts: A.xf(pts, x, y, s, 0.0, flip)
    iw = max(2, s * 0.008)
    ph = t * 3.2 + phase
    # pernas do fundo (mais escuras)
    _leg(ss, P, -0.48, ph + math.pi, s, iw, alpha, lift=0.1 * walk, swing=0.13 * walk, shade=True)
    _leg(ss, P, 0.42, ph, s, iw, alpha, lift=0.1 * walk, swing=0.13 * walk, shade=True)
    # cauda
    tw = 0.06 * math.sin(t * 2.1)
    ss.line(P([(-0.8, -1.12), (-0.9 + tw, -0.85), (-0.88 + tw, -0.62)]), (*SKIN_D, alpha), max(2, s * 0.025))
    ss.circle(*P([(-0.88 + tw, -0.6)])[0], max(2, s * 0.03), fill=(*INK, alpha))
    # corpo
    bob = 0.015 * math.sin(ph * 2) * walk
    body = A.spline([(-0.85, -1.05 + bob), (-0.6, -1.5 + bob), (0.1, -1.62 + bob), (0.62, -1.48 + bob), (0.78, -1.0 + bob),
                     (0.6, -0.68 + bob), (-0.1, -0.62 + bob), (-0.7, -0.7 + bob)], n=8)
    ss.poly(P(body), fill=(*SKIN, alpha), ink=(*INK, alpha), w=iw)
    for k in range(4):  # rugas
        xx = -0.5 + k * 0.25
        ss.line(P(A.bez((xx, -1.4 + bob), (xx + 0.05, -1.2 + bob), (xx - 0.03, -1.0 + bob), (xx + 0.02, -0.8 + bob), 8)),
                (*SKIN_D, int(alpha * 0.6)), max(1, s * 0.006))
    # pernas da frente
    _leg(ss, P, -0.36, ph, s, iw, alpha, lift=0.1 * walk, swing=0.13 * walk)
    foot, lift = _leg(ss, P, 0.5, ph + math.pi, s, iw, alpha, lift=0.1 * walk, swing=0.13 * walk)
    # cabeça
    hy = -1.42 + bob
    head = A.spline([(0.55, hy - 0.05), (0.75, hy - 0.32), (1.05, hy - 0.3), (1.2, hy - 0.05), (1.18, hy + 0.3),
                     (0.95, hy + 0.42), (0.68, hy + 0.3)], n=8)
    # tromba
    tr = trunk + 0.12 * math.sin(t * 1.7)
    tb = A.bez((1.12, hy + 0.15), (1.32, hy + 0.45), (1.25 + 0.25 * tr, hy + 1.0 - 0.4 * tr),
               (1.38 + 0.45 * tr, hy + 1.32 - 0.75 * tr), 18)
    wts = [lerp(0.13, 0.055, i / (len(tb) - 1)) for i in range(len(tb))]
    left, right = [], []
    for i, (px, py) in enumerate(tb):
        qx, qy = tb[min(i + 1, len(tb) - 1)] if i < len(tb) - 1 else tb[i]
        ox, oy = tb[i - 1] if i > 0 else tb[i]
        dx, dy = qx - ox, qy - oy; n = math.hypot(dx, dy) or 1
        nx, ny = -dy / n, dx / n
        left.append((px + nx * wts[i], py + ny * wts[i])); right.append((px - nx * wts[i], py - ny * wts[i]))
    ss.poly(P(left + right[::-1]), fill=(*SKIN, alpha), ink=(*INK, alpha), w=iw)
    for i in range(3, len(tb) - 2, 2):
        ss.line(P([left[i], right[i]]), (*SKIN_D, int(alpha * 0.5)), max(1, s * 0.005))
    ss.poly(P(head), fill=(*SKIN, alpha), ink=(*INK, alpha), w=iw)
    # presa
    ss.poly(P(A.bez((1.05, hy + 0.32), (1.2, hy + 0.5), (1.35, hy + 0.5), (1.42, hy + 0.36), 10) +
              A.bez((1.4, hy + 0.42), (1.3, hy + 0.58), (1.12, hy + 0.5), (1.0, hy + 0.36), 10)),
            fill=(*TUSK, alpha), ink=(*INK, alpha), w=iw * 0.8)
    if mouth > 0:
        ss.ellipse(*P([(1.0, hy + 0.36)])[0], s * 0.05, s * 0.03 * mouth, fill=(110, 40, 60, alpha))
    # orelha (grande, abana)
    ef = 0.08 * math.sin(t * 1.3) + ear
    ear_pts = A.spline([(0.72, hy - 0.22), (0.45 - ef * 0.4, hy - 0.42), (0.18 - ef, hy - 0.1), (0.2 - ef * 0.8, hy + 0.4),
                        (0.42 - ef * 0.3, hy + 0.7), (0.66, hy + 0.36)], n=8)
    ss.poly(P(ear_pts), fill=(*SKIN_L, alpha), ink=(*INK, alpha), w=iw)
    inner = [(lerp(0.6, px, 0.72), lerp(hy + 0.12, py, 0.72)) for px, py in ear_pts]
    ss.poly(P(inner), fill=(*EAR_IN, int(alpha * 0.8)))
    # olho grande e expressivo
    ex, ey = P([(0.98, hy - 0.06)])[0]; er = s * 0.045 * eye
    ss.circle(ex, ey, er * 1.25, fill=(*SKIN_D, alpha))
    ss.circle(ex, ey, er, fill=(30, 20, 18, alpha), ink=(*INK, alpha), w=max(1, iw * 0.6))
    ss.circle(ex - er * 0.3, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, int(240 * alpha / 255)))
    ss.line(P([(0.9, hy - 0.16), (1.06, hy - 0.17)]), (*INK, alpha), max(1, s * 0.01))
    return foot, lift


# ======================================================================= savana
def sky():
    def mk():
        im = A.vgrad(W, H, [(0, (250, 150, 120)), (0.35, (255, 196, 150)), (0.55, (255, 222, 170)), (1, (255, 222, 170))])
        A.paste_c(im, A.glow(460, (255, 240, 190), 160), 300, 980)
        ss = SS(W, H, s=2)
        ss.circle(300, 980, 120, fill=(255, 238, 190))
        im.alpha_composite(ss.get())
        return im
    return cached("sky", mk).copy()


def acacia(ss, x, y, s, col=WINE):
    ss.line([(x, y), (x - 0.05 * s, y - 0.6 * s), (x + 0.1 * s, y - 1.0 * s)], col, max(3, s * 0.06))
    ss.line([(x - 0.04 * s, y - 0.55 * s), (x - 0.35 * s, y - 0.92 * s)], col, max(2, s * 0.04))
    ss.oval(x - 0.05 * s, y - 1.0 * s, 0.75 * s, 0.14 * s, 0, fill=col)
    ss.oval(x + 0.2 * s, y - 1.08 * s, 0.45 * s, 0.1 * s, 0, fill=col)


def savanna(horizon=1180, t=0.0):
    key = f"sav{horizon}"

    def mk():
        im = sky()
        ss = SS(W, H, s=2)
        ss.poly([(0, horizon), (260, horizon - 40), (520, horizon - 10), (820, horizon - 60), (W, horizon - 20), (W, H), (0, H)],
                fill=(200, 120, 110))
        ss.rect(0, horizon, W, H, SOIL_L)
        acacia(ss, 840, horizon - 6, 260, (150, 80, 90))
        acacia(ss, 140, horizon, 180, (150, 80, 90))
        im.alpha_composite(ss.get())
        g = A.vgrad(W, H - horizon, [(0, SOIL_L), (1, SOIL)])
        im.alpha_composite(g, (0, horizon))
        ss = SS(W, H, s=1)
        rng = np.random.default_rng(4)
        for _ in range(260):
            y = rng.uniform(horizon + 10, H)
            ln = 6 + (y - horizon) * 0.05
            x = rng.uniform(0, W)
            ss.line([(x, y), (x + rng.uniform(-3, 3), y - ln)], (226, 170, 90, 200), 2 + (y - horizon) * 0.004)
        im.alpha_composite(ss.get())
        return im
    return cached(key, mk).copy()


def ripples(ss, cx, cy, t, n=4, period=0.8, rmax=900, sy=0.22, col=MAG, w=8, a=230, t0=None):
    """anéis achatados no chão (perspectiva) saindo de (cx, cy)"""
    for k in range(n):
        age = ((t if t0 is None else t - t0) / period - k / n) % 1.0
        if t0 is not None and t - t0 < 0: return
        r = 30 + age * rmax
        fa = (1 - age) ** 1.3
        ss.line(A.ell_pts(cx, cy, r, r * sy, 0, 48), (*col, int(a * fa)), w * (1 - 0.5 * age))


# ======================================================================= cena 1: gancho (pisada rasteira)
EX, EY, ES = 330, 1640, 480


def hook_frame(t, wk=1.0, extra=None):
    img = savanna(1120)
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(1)
    # poeira de fundo
    for k in range(18):
        u = (t * 0.15 + rng.uniform(0, 1)) % 1
        ss.circle(rng.uniform(0, W), 1120 - u * 300, rng.uniform(4, 10), fill=(255, 230, 190, int(90 * (1 - u))))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    foot, lift = elephant(SS(8, 8, s=1), EX, EY, ES, t=t, walk=wk)  # só para saber onde a pata cai
    # anel do tremor saindo de cada pisada da pata da frente
    ph = t * 3.2 + math.pi
    land = (ph - math.pi) % (2 * math.pi)  # 0 = acabou de pisar
    for k in range(3):
        age = (land + k * 2 * math.pi) / (2 * math.pi * 3.2 / 3.2) / 1.9
        r = 40 + age * 1200
        fa = max(0.0, 1 - age / 1.6)
        ss.line(A.ell_pts(foot[0], EY + 6, r, r * 0.2, 0, 56), (*MAG, int(255 * fa)), 16 * fa + 4)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    elephant(ss, EX, EY, ES, t=t, walk=wk, eye=1.2)
    sp = ss.get()
    sh = Image.new("RGBA", (W, H)); s2 = SS(W, H, s=1)
    s2.oval(EX + 60, EY + 10, ES * 0.95, 40, 0, fill=(60, 20, 20, 90))
    img.alpha_composite(s2.get().filter(ImageFilter.GaussianBlur(10)))
    img.alpha_composite(sp)
    # poeira na pisada
    ss = SS(W, H, s=2)
    pu = (land / (2 * math.pi))
    if pu < 0.35:
        q = pu / 0.35
        for k in range(10):
            a = math.pi + k * math.pi / 9
            ss.circle(foot[0] + math.cos(a) * (60 + 140 * q), EY - 10 + math.sin(a) * 40 * q - 30 * q, 18 * (1 - q) + 6,
                      fill=(240, 200, 150, int(180 * (1 - q))))
    if extra: extra(ss)
    img.alpha_composite(ss.get())
    return A.vignette(img, 0.35)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.04, dy=-6 * abs(math.sin((lt * 3.2) / 2)))


# ======================================================================= cena 2: lá longe (você não ouve)
def person(ss, x, y, s, col=(60, 40, 60)):
    ss.circle(x, y - 0.88 * s, 0.11 * s, fill=col)
    ss.poly([(x - 0.14 * s, y - 0.74 * s), (x + 0.14 * s, y - 0.74 * s), (x + 0.11 * s, y - 0.32 * s), (x - 0.11 * s, y - 0.32 * s)], fill=col)
    ss.line([(x - 0.06 * s, y - 0.34 * s), (x - 0.07 * s, y)], col, 0.07 * s)
    ss.line([(x + 0.06 * s, y - 0.34 * s), (x + 0.07 * s, y)], col, 0.07 * s)


def far(ctx, lt):
    img = savanna(1180)
    tn = ctx.wt("nada")
    ss = SS(W, H, s=2)
    # elefante distante chamando (anéis no chão e no ar, fracos)
    ripples(ss, 860, 1196, lt, n=4, period=1.4, rmax=1200, sy=0.12, w=6, a=200)
    for k in range(3):
        age = (lt / 1.4 + k / 3) % 1
        r = 40 + age * 260
        ss.line(A.ell_pts(925, 1110, r, r, 0, 20, -0.9, 0.9), (*AIRG, int(160 * (1 - age))), 5)
    elephant(ss, 860, 1196, 120, t=lt, walk=0.0, trunk=0.7, mouth=0.6)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    elephant(ss, 250, 1640, 360, t=lt + 1, walk=0.0, ear=0.12 * ease((lt - 0.8) / 0.6), eye=1.2)
    # você, pequeno, à direita, sem ouvir nada
    q = ease((lt - tn + 0.4) / 0.4)
    person(ss, 860, 1700, 300)
    if q > 0:
        ss.rrect(740, 1240, 980, 1360, 40, fill=(255, 255, 255, int(235 * q)), ink=(*INK, int(255 * q)), w=6)
        ss.poly([(850, 1358), (880, 1358), (865, 1390)], fill=(255, 255, 255, int(235 * q)))
        for k in range(3):
            ss.circle(810 + k * 50, 1300, 12, fill=(*INK, int(255 * q)))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * easeio(lt / max(1, ctx.dur)), dx=-20 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 3: Visão do Bicho (tremor)
_DIST = {}


def _dist_ell(cx, cy, sy):
    key = (cx, cy, sy)
    if key not in _DIST:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        _DIST[key] = np.sqrt((xx - cx) ** 2 + ((yy - cy) / sy) ** 2)
    return _DIST[key]


def _ground_grid():
    def mk():
        ss = SS(W, H, s=2)
        hz = 560
        for k in range(-12, 13):
            ss.line([(540 + k * 30, hz), (540 + k * 260, H)], (255, 120, 200), 3)
        y = hz; step = 14
        while y < H:
            ss.line([(0, y), (W, y)], (255, 120, 200), 3)
            step *= 1.18; y += step
        return ss.get()
    return cached("grid", mk)


def vision(ctx, lt):
    img = A.vgrad(W, H, [(0, (20, 6, 26)), (0.3, (34, 8, 40)), (1, (50, 10, 46))])
    d = _dist_ell(540, 560, 0.35)
    m = np.zeros((H, W), np.float32)
    per = 0.5
    for k in range(4):
        age = ((lt % per) + k * per)
        r = age * 2400
        m += np.exp(-((d - r) / 160.0) ** 2) * math.exp(-age * 0.5)
    m = np.clip(m * 1.4 + 0.12, 0, 1)
    gr = _ground_grid()
    a = np.asarray(gr.split()[3], np.float32) * m
    lay = gr.copy(); lay.putalpha(Image.fromarray(a.astype(np.uint8)))
    img.alpha_composite(lay)
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(9)))
    ss = SS(W, H, s=2)
    # a fonte: o outro elefante, longe, no horizonte
    elephant(ss, 540, 560, 60, t=lt, walk=0.0, trunk=0.7, alpha=200)
    # minhas patas (POV olhando para baixo) acendem quando a onda chega
    hit = 0.0
    for k in range(4):
        age = ((lt % per) + k * per)
        hit = max(hit, math.exp(-((age * 2400 - 1200 / 0.35 * 0.35 * 3.3) / 500.0) ** 2))
    glow = 0.35 + 0.65 * (0.5 + 0.5 * math.sin(lt * 2 * math.pi / per))
    for sg in (-1, 1):
        fx = 540 + sg * 290
        ss.ellipse(fx, 1820, 230, 70, fill=(*MAG, int(110 * glow)))
        ss.poly([(fx - 170, H + 40), (fx - 160, 1540), (fx + 160, 1540), (fx + 170, H + 40)], fill=SKIN_D, ink=INK, w=6)
        ss.ellipse(fx, 1830, 175, 56, fill=SKIN, ink=INK, w=6)
        for k in (-80, 0, 80):
            ss.circle(fx + k, 1860, 26, fill=TUSK, ink=INK, w=3)
        ss.ellipse(fx, 1830, 175, 56, ink=(*MAG, int(255 * glow)), w=10)
    # tromba no topo (borda da tela)
    sway = 30 * math.sin(lt * 1.5)
    ss.line([(540 + sway, -40), (560 + sway, 180), (520 + sway * 1.4, 330)], SKIN, 120)
    ss.line([(540 + sway, -40), (560 + sway, 180), (520 + sway * 1.4, 330)], SKIN_D, 10)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.01 * math.sin(lt * 9), dy=3 * math.sin(lt * 31))


# ======================================================================= cena 4: grave demais pro seu ouvido
def ear_icon(ss, x, y, s, col=(255, 210, 190)):
    ss.poly(A.spline([(x - 0.3 * s, y - 0.6 * s), (x + 0.35 * s, y - 0.7 * s), (x + 0.5 * s, y), (x + 0.1 * s, y + 0.75 * s),
                      (x - 0.2 * s, y + 0.55 * s), (x - 0.05 * s, y + 0.1 * s), (x - 0.35 * s, y - 0.2 * s)], n=6),
            fill=col, ink=INK, w=6)
    ss.line(A.bez((x - 0.1 * s, y - 0.35 * s), (x + 0.3 * s, y - 0.45 * s), (x + 0.3 * s, y + 0.1 * s), (x, y + 0.2 * s), 12),
            (190, 120, 110), 0.06 * s)


def rumble(ctx, lt):
    img = A.vgrad(W, H, [(0, (64, 24, 44)), (1, (120, 46, 60))])
    tg = ctx.wt("grave"); to = ctx.wt("ouvido")
    ss = SS(W, H, s=2)
    go = ease((lt - tg + 0.3) / 0.4)
    # onda grave: lenta, enorme
    for k in range(3):
        y0 = 1500 + k * 70
        amp = 90 * (1 - k * 0.25) * (0.3 + 0.7 * go)
        pts = [(x, y0 + amp * math.sin(x * 0.006 - lt * 3.0 + k)) for x in range(-20, W + 21, 10)]
        ss.line(pts, (*MAG, int(230 * (1 - k * 0.3))), 12 - k * 3)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    elephant(ss, 170, 1760, 400, t=lt, walk=0.0, trunk=0.6 + 0.2 * go, mouth=go)
    img.alpha_composite(ss.get())
    # régua de frequências
    hb = ease((lt - to + 0.8) / 0.5)
    if hb > 0:
        ss = SS(W, H, s=2)
        ss.rrect(80, 480, 1000, 860, 36, fill=(20, 8, 20, int(225 * hb)), ink=(*INK, int(255 * hb)), w=6)
        ss.text((540, 535), "VIBRAÇÕES POR SEGUNDO", 40, "anton", fill=(255, 255, 255, int(255 * hb)))
        x0, x1 = 140, 940
        ss.rrect(x0, 620, x1, 660, 18, fill=(70, 50, 80, int(255 * hb)))
        xh = lerp(x0, x1, 0.45)  # 20/s
        ss.rrect(xh, 620, x1, 660, 18, fill=(255, 255, 255, int(255 * hb)))
        ss.text(((xh + x1) / 2, 700), "VOCÊ OUVE", 34, "mont-ExtraBold", fill=(255, 255, 255, int(255 * hb)))
        ss.line([(xh, 600), (xh, 680)], (255, 255, 255, int(255 * hb)), 5)
        ss.text((xh, 585), "20", 36, "anton", fill=(255, 255, 255, int(255 * hb)))
        rx0, rx1 = lerp(x0, x1, 0.16), lerp(x0, x1, 0.6)
        ss.rrect(rx0, 760, rx1, 800, 18, fill=(*MAG, int(255 * hb)))
        ss.text(((rx0 + rx1) / 2, 830), "RONCO", 34, "mont-ExtraBold", fill=(*MAG, int(255 * hb)))
        # o que fica abaixo do seu ouvido pisca
        bl = 0.5 + 0.5 * math.sin(lt * 10)
        ss.rrect(rx0, 760, xh, 800, 18, fill=(255, 255, 255, int(120 * hb * bl)))
        img.alpha_composite(ss.get())
        ss = SS(W, H, s=2)
        ear_icon(ss, 880, 1000, 120)
        ss.line([(780, 900), (980, 1100)], (255, 60, 60, int(255 * hb)), 18)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * go, dx=6 * go * math.sin(lt * 18), dy=4 * go * math.sin(lt * 15))


# ======================================================================= cena 5: o ar e o chão
def ground(ctx, lt):
    img = sky()
    tc = ctx.wt("chão")
    ss = SS(W, H, s=2)
    gy = 1180
    # corte do solo em camadas
    for k, col in enumerate(((176, 84, 52), (150, 70, 46), (124, 58, 42), (98, 46, 38))):
        ss.rect(0, gy + k * 190, W, H, col)
    for k in range(40):
        rng = np.random.default_rng(k)
        ss.circle(rng.uniform(0, W), rng.uniform(gy + 30, H), rng.uniform(6, 20), fill=(90, 40, 34))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    # onda no ar (verde) e no chão (magenta, só depois de "chão")
    for k in range(4):
        age = (lt / 1.2 + k / 4) % 1
        r = 60 + age * 900
        ss.line(A.ell_pts(250, 900, r, r, 0, 30, -0.75, 0.6), (*AIRG, int(220 * (1 - age))), 9)
    gq = ease((lt - tc + 0.5) / 0.4)
    if gq > 0:
        for k in range(4):
            age = (lt / 1.0 + k / 4) % 1
            r = 60 + age * 1000
            ss.line(A.ell_pts(250, gy, r, r * 0.8, 0, 30, -0.05, 1.3), (*MAG, int(240 * (1 - age) * gq)), 12)
    elephant(ss, 180, gy, 300, t=lt, walk=0.0, trunk=0.6, mouth=0.6)
    ss.rrect(600, 640, 960, 740, 30, fill=(255, 255, 255, 230), ink=INK, w=5)
    ss.text((780, 690), "AR", 54, "anton", fill=(30, 140, 80))
    if gq > 0:
        ss.rrect(560, 1460, 1000, 1560, 30, fill=(255, 255, 255, int(230 * gq)), ink=(*INK, int(255 * gq)), w=5)
        ss.text((780, 1510), "CHÃO", 54, "anton", fill=(*MAG, int(255 * gq)))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt), dy=3 * gq * math.sin(lt * 27))


# ======================================================================= cena 6: raio-X do pé
def foot(ctx, lt):
    img = A.vgrad(W, H, [(0, (16, 30, 56)), (1, (28, 52, 86))])
    ta = ctx.wt("almofada"); ts = ctx.wt("sensores")
    ss = SS(W, H, s=2)
    # grade de raio-X
    for k in range(0, W, 60): ss.line([(k, 0), (k, H)], (60, 100, 150, 70), 2)
    for k in range(0, H, 60): ss.line([(0, k), (W, k)], (60, 100, 150, 70), 2)
    # pé translúcido
    leg = [(300, 300), (780, 300), (820, 1200), (900, 1480), (180, 1480), (260, 1200)]
    ss.poly(leg, fill=(170, 200, 230, 70), ink=(200, 230, 255), w=6)
    # ossos (azul claro)
    for bx, by0, by1 in ((540, 320, 1060), (450, 1080, 1300), (540, 1080, 1320), (630, 1080, 1300)):
        ss.line([(bx, by0), (bx + (bx - 540) * 0.6, by1)], (220, 235, 255), 46 if by0 == 320 else 30)
    # almofada (gordura)
    pq = ease((lt - ta + 0.4) / 0.4)
    ss.ellipse(540, 1400, 330, 80 + 20 * pq, fill=(255, 220, 140, int(70 + 150 * pq)), ink=(255, 230, 160), w=5)
    # chão com a onda chegando
    ss.rect(0, 1490, W, H, (90, 40, 34))
    for k in range(3):
        age = (lt / 0.9 + k / 3) % 1
        x = lerp(-100, 540, age)
        ss.line([(x - 60, 1530), (x, 1500), (x + 60, 1530)], (*MAG, int(255 * age)), 10)
        ss.line([(W - x + 60, 1530), (W - x, 1500), (W - x - 60, 1530)], (*MAG, int(255 * age)), 10)
    # sensores acendendo em amarelo e sinal subindo
    sq = ease((lt - ts + 0.3) / 0.3)
    rng = np.random.default_rng(9)
    for k in range(16):
        x = 540 + rng.uniform(-280, 280); y = 1400 + rng.uniform(-55, 55)
        fl = sq * (0.5 + 0.5 * math.sin(lt * 14 + k))
        ss.circle(x, y, 16, fill=(*YEL, int(60 + 195 * fl)), ink=INK, w=2)
        if fl > 0.6:
            ss.circle(x, y, 32, fill=(*YEL, int(80 * fl)))
    if sq > 0:
        for k in range(3):
            u = (lt * 0.9 + k / 3) % 1
            ss.circle(540, lerp(1330, 380, u), 22, fill=(*YEL, int(255 * sq * (1 - u * 0.6))))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 7: pelos ossos até o ouvido
def bones(ctx, lt):
    img = A.vgrad(W, H, [(0, (14, 24, 48)), (1, (26, 44, 78))])
    to = ctx.wt("ouvido"); tsub = ctx.wt("sobe")
    ss = SS(W, H, s=2)
    # silhueta translúcida do elefante
    s2 = SS(W, H, s=2)
    elephant(s2, 420, 1700, 820, t=0.4, walk=0.0, trunk=0.5)
    sil = s2.get(); sil.putalpha(sil.split()[3].point(lambda v: int(v * 0.32)))
    img.alpha_composite(sil)
    # caminho: pata dianteira -> ombro -> crânio -> ouvido
    path = [(830, 1690), (820, 1400), (800, 1100), (860, 900), (900, 760), (830, 640)]
    P = A.spline(path, n=10, closed=False)
    ss.line(P, (220, 235, 255), 34)
    ss.line(P, (160, 190, 230), 14)
    ss.circle(830, 640, 50, fill=(255, 255, 255, 60), ink=(255, 255, 255), w=5)
    u = ease((lt - tsub + 0.2) / max(0.5, to - tsub + 0.2))
    n = int(u * (len(P) - 1))
    if n > 0:
        ss.line(P[:n + 1], (*MAG, 255), 18)
        hx, hy = P[n]
        ss.circle(hx, hy, 34, fill=(*MAG, 255), ink=INK, w=4)
        ss.circle(hx, hy, 70, fill=(*MAG, 80))
    oq = ease((lt - to) / 0.3)
    if oq > 0:
        for k in range(3):
            r = 60 + k * 40 + 20 * math.sin(lt * 8)
            ss.circle(830, 640, r, ink=(*YEL, int(220 * oq * (1 - k * 0.3))), w=6)
    # ondas entrando pela pata
    for k in range(3):
        age = (lt / 0.8 + k / 3) % 1
        r = 40 + age * 300
        ss.line(A.ell_pts(830, 1700, r, r * 0.2, 0, 40), (*MAG, int(220 * (1 - age))), 7)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=lerp(1.0, 1.12, easeio(clamp01(lt / max(1, ctx.dur)))), cx=830, cy=lerp(1500, 700, easeio(clamp01(lt / max(1, ctx.dur)))))


# ======================================================================= cena 8: 2 km pelo chão (mapa)
def km(ctx, lt):
    img = A.vgrad(W, H, [(0, (226, 160, 100)), (1, (196, 120, 76))])
    tq = ctx.wt("quilômetros")
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(5)
    for _ in range(26):  # arbustos vistos de cima
        x, y = rng.uniform(0, W), rng.uniform(450, 1900)
        ss.circle(x, y, rng.uniform(22, 50), fill=(130, 110, 60))
        ss.circle(x - 8, y - 8, rng.uniform(10, 20), fill=(160, 140, 80))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ax, ay, bx, by = 260, 1600, 820, 600
    u = ease(lt / max(0.8, tq + 0.2))
    for k in range(5):
        age = (lt / 1.1 + k / 5) % 1
        r = 40 + age * 1250
        if r < math.hypot(bx - ax, by - ay) * u + 60:
            ss.circle(bx, by, r, ink=(*MAG, int(220 * (1 - age))), w=8)
    # linha tracejada até mim
    dist = math.hypot(ax - bx, ay - by)
    nd = int(22 * u)
    for k in range(nd):
        p0 = k / 22; p1 = (k + 0.55) / 22
        ss.line([(lerp(bx, ax, p0), lerp(by, ay, p0)), (lerp(bx, ax, p1), lerp(by, ay, p1))], (255, 255, 255), 9)
    # elefantes vistos de cima (ovais)
    for x, y, s, col in ((bx, by, 1.0, SKIN), (ax, ay, 1.2, SKIN)):
        ss.oval(x, y, 60 * s, 90 * s, 0.5, fill=col, ink=INK, w=5)
        ss.oval(x + 50 * s, y - 70 * s, 46 * s, 36 * s, 0.5, fill=col, ink=INK, w=5)
        for sg in (-1, 1):
            ss.oval(x + 50 * s + sg * 46 * s, y - 60 * s + sg * 30 * s, 34 * s, 20 * s, 0.5 + sg * 0.6, fill=SKIN_L, ink=INK, w=4)
    lq = ease((lt - tq + 0.3) / 0.35)
    if lq > 0:
        mx, my = 300, 820
        ss.rrect(mx - 200, my - 90, mx + 200, my + 90, 36, fill=(255, 255, 255, int(240 * lq)), ink=(*INK, int(255 * lq)), w=6)
        ss.text((mx, my - 20), "2 km", 86, "anton", fill=(*MAG, int(255 * lq)))
        ss.text((mx, my + 52), "≈ 19 campos de futebol", 28, "mont-ExtraBold", fill=(*INK, int(255 * lq)))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=lerp(1.15, 1.0, easeio(clamp01(lt / 1.5))))


# ======================================================================= cena 9: é da família?
def family(ctx, lt):
    img = savanna(1300)
    tf = ctx.wt("família")
    ss = SS(W, H, s=2)
    ripples(ss, 1100, 1330, lt, n=4, period=1.0, rmax=1400, sy=0.15, w=7)
    elephant(ss, 420, 1760, 560, t=lt, walk=0.0, ear=0.2 + 0.08 * math.sin(lt * 4), eye=1.3, trunk=0.2)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    q = ease((lt - 0.2) / 0.4)
    # balão de pensamento
    ss.circle(560, 1050, 22 * q, fill=(255, 255, 255, int(240 * q)), ink=(*INK, int(255 * q)), w=4)
    ss.circle(620, 970, 34 * q, fill=(255, 255, 255, int(240 * q)), ink=(*INK, int(255 * q)), w=4)
    ss.rrect(110, 500, 970, 910, 60, fill=(255, 255, 255, int(240 * q)), ink=(*INK, int(255 * q)), w=6)
    if q > 0.5:
        # família (mãe + filhote)
        elephant(ss, 270, 840, 150, t=lt, walk=0.0, alpha=255)
        elephant(ss, 380, 850, 80, t=lt + 1, walk=0.0, alpha=255)
        # estranho
        elephant(ss, 750, 840, 150, t=lt + 2, walk=0.0, alpha=255)
        fq = ease((lt - tf + 0.6) / 0.35)
        if fq > 0:
            ss.circle(330, 560, 50 * fq, fill=(80, 200, 110), ink=INK, w=5)
            ss.line([(305, 560), (325, 582), (360, 538)], (255, 255, 255), 12)
            ss.circle(790, 560, 50 * fq, fill=(235, 70, 70), ink=INK, w=5)
            ss.line([(770, 540), (810, 580)], (255, 255, 255), 12); ss.line([(810, 540), (770, 580)], (255, 255, 255), 12)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 10: loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    tf = ctx.wt("falando")
    back = easeio(clamp01((lt - 0.0) / max(0.5, ctx.dur * 0.7)))
    q = (1 - ease((lt - tf) / 0.5)) if lt > tf else 1.0

    def extra(ss):
        if q <= 0.01: return
        # você, no canto, com "silêncio"
        ss.rrect(600, 480, 1000, 600, 40, fill=(255, 255, 255, int(235 * q)), ink=(*INK, int(255 * q)), w=6)
        ss.text((800, 540), "silêncio…", 48, "mont-ExtraBold", fill=(*INK, int(255 * q)))

    img = hook_frame(tr, extra=extra)
    return A.cam(img, zoom=lerp(1.12, 1.04, back), dy=-6 * abs(math.sin((tr * 3.2) / 2)))


# ======================================================================= capa
def cover_bg(cv):
    img = savanna(1120)
    ss = SS(W, H, s=2)
    for k in range(4):
        r = 120 + k * 260
        ss.line(A.ell_pts(540, 1450, r, r * 0.22, 0, 56), (*MAG, 230 - k * 45), 14 - k * 2)
    img.alpha_composite(ss.get())
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 560)
    ss = SS(int(2.75 * s), int(2.3 * s), s=2)
    elephant(ss, 0.95 * s, 2.15 * s, s, t=0.2, walk=0.6, trunk=0.8, eye=1.8, ear=0.1, mouth=0.5)
    return ss.get()
