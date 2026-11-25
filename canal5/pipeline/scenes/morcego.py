"""Dia 6A — "E se você fosse um morcego caçando no escuro?" (formato CURTO; paleta: meia-noite azul-marinho,
lua creme, árvores em silhueta índigo, morcego castanho-acinzentado com orelhas rosadas, sonar em ciano e eco em laranja).

Cenas: hook (o morcego vem de frente, batendo as asas, arcos de sonar saindo da boca rumo ao mosquito), dark (o mesmo
lugar visto por você: quase preto), vision (Visão do Bicho: sonar — o mundo aparece em linhas ciano onde o eco bate,
pontas das asas na borda), shout (close da boca aberta + barras: você ouve até 20 mil vibrações/s, o grito passa disso),
echo (o arco vai, bate no mosquito e volta em laranja), near (longe = eco demora; perto = eco rápido), buzz (bote final:
contador até 190 gritos/s), car (sensor de ré apitando cada vez mais rápido perto do muro), wire (desvia de um fio de
0,3 mm), loop (engole o mosquito e volta a caçar: quadro inicial).
Fatos: Elemans et al. (2011, Science); Grinnell & Griffin (1958, Biol. Bull.).
"""
import math
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

FUR = (128, 96, 82); FUR_D = (82, 60, 56); FUR_L = (176, 140, 118)
MEM = (74, 54, 66); MEM_L = (112, 84, 96)
PINK = (236, 150, 160)
SON = (90, 230, 255)       # sonar (ciano)
ECO = (255, 150, 60)       # eco (laranja)
NAVY = (12, 18, 46); NAVY2 = (28, 40, 92); INDIGO = (20, 22, 52)
MOON = (255, 240, 200)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= morcego (de frente)
def _rot(p, o, a):
    c, s = math.cos(a), math.sin(a)
    x, y = p[0] - o[0], p[1] - o[1]
    return (o[0] + x * c - y * s, o[1] + x * s + y * c)


def bat(ss, x, y, s, t=0.0, flap=None, mouth=0.3, eye=1.0, rot=0.0, alpha=255):
    """morcego de frente, asas abertas. flap: -1 (asas baixas) .. 1 (asas altas). Origem = centro do corpo."""
    P = lambda pts: A.xf(pts, x, y, s, rot, 1)
    iw = max(1.5, s * 0.007)
    f = math.sin(t * 9.0) if flap is None else flap
    for sg in (-1, 1):
        sh = (sg * 0.12, -0.1)
        base = [(0.12, -0.1), (0.5, -0.36), (1.06, -0.16), (0.98, 0.16), (0.74, 0.36), (0.16, 0.26)]
        ang = -sg * 0.42 * f
        pts = [_rot((sg * px, py), sh, ang) for px, py in base]
        pts = [(sh[0] + (px - sh[0]) * (0.86 + 0.14 * math.cos(f * 1.2)), py) for px, py in pts]
        sho, wri, t1, t2, t3, hip = pts
        # membrana com borda recortada (entre as pontas dos dedos)
        edge = [sho, wri, t1]
        for a_, b_ in ((t1, t2), (t2, t3), (t3, hip)):
            mx, my = (a_[0] + b_[0]) / 2, (a_[1] + b_[1]) / 2
            mx2, my2 = lerp(mx, wri[0], 0.22), lerp(my, wri[1], 0.22)
            edge += A.bez(a_, (lerp(a_[0], mx2, 0.6), lerp(a_[1], my2, 0.6)), (lerp(b_[0], mx2, 0.6), lerp(b_[1], my2, 0.6)), b_, 8)[1:]
        ss.poly(P(edge), fill=(*MEM, alpha), ink=(*INK, alpha), w=iw)
        # dedos (ossos)
        for tip in (t1, t2, t3):
            ss.line(P([wri, tip]), (*MEM_L, alpha), max(2, s * 0.014))
        ss.line(P([sho, wri]), (*FUR_D, alpha), max(3, s * 0.03))
        ss.circle(*P([wri])[0], max(2, s * 0.018), fill=(*FUR_D, alpha))
        # polegar com garrinha
        tp = P([(wri[0] + sg * 0.03, wri[1] - 0.07)])[0]
        ss.line([P([wri])[0], tp], (*FUR_D, alpha), max(2, s * 0.014))
    # pés
    for sg in (-1, 1):
        ss.line(P([(sg * 0.07, 0.3), (sg * 0.1, 0.4)]), (*FUR_D, alpha), max(2, s * 0.02))
    # corpo peludo
    ss.oval(*P([(0, 0.08)])[0], s * 0.17, s * 0.27, math.radians(rot), fill=(*FUR, alpha), ink=(*INK, alpha), w=iw)
    ss.oval(*P([(0, 0.13)])[0], s * 0.1, s * 0.17, math.radians(rot), fill=(*FUR_L, int(alpha * 0.7)))
    # orelhas
    for sg in (-1, 1):
        ear = [(sg * 0.05, -0.28), (sg * 0.2, -0.58), (sg * 0.2, -0.24)]
        ss.poly(P(ear), fill=(*FUR, alpha), ink=(*INK, alpha), w=iw)
        ss.poly(P([(sg * 0.09, -0.3), (sg * 0.19, -0.5), (sg * 0.18, -0.27)]), fill=(*PINK, alpha))
    # cabeça
    hx, hy = P([(0, -0.2)])[0]
    ss.circle(hx, hy, s * 0.16, fill=(*FUR, alpha), ink=(*INK, alpha), w=iw)
    ss.ellipse(*P([(0, -0.15)])[0], s * 0.09, s * 0.07, fill=(*FUR_L, alpha))
    # olhos
    for sg in (-1, 1):
        ex, ey = P([(sg * 0.065, -0.235)])[0]; er = s * 0.03 * eye
        ss.circle(ex, ey, er, fill=(16, 10, 18, alpha), ink=(*INK, alpha), w=max(1, iw * 0.6))
        ss.circle(ex - er * 0.3, ey - er * 0.35, er * 0.4, fill=(255, 255, 255, int(240 * alpha / 255)))
    # nariz
    ss.ellipse(*P([(0, -0.18)])[0], s * 0.03, s * 0.02, fill=(*PINK, alpha), ink=(*INK, alpha), w=max(1, iw * 0.5))
    # boca (aberta = grito)
    mx, my = P([(0, -0.115)])[0]
    mo = clamp01(mouth)
    if mo > 0.05:
        ss.ellipse(mx, my, s * 0.055, s * 0.012 + s * 0.045 * mo, fill=(90, 20, 40, alpha), ink=(*INK, alpha), w=max(1, iw * 0.6))
        for sg in (-1, 1):
            ss.poly([(mx + sg * s * 0.03, my - s * 0.01 - s * 0.03 * mo), (mx + sg * s * 0.02, my + s * 0.01),
                     (mx + sg * s * 0.04, my - s * 0.005 - s * 0.03 * mo)], fill=(255, 255, 255, alpha))
    else:
        ss.line([(mx - s * 0.03, my), (mx, my + s * 0.01), (mx + s * 0.03, my)], (*INK, alpha), max(1, iw * 0.7))


def mosquito(ss, x, y, s, t=0.0, a=255, glow=0.0, col=(40, 36, 48)):
    if glow > 0:
        ss.circle(x, y, s * 0.9, fill=(*ECO, int(90 * glow * a / 255)))
        ss.circle(x, y, s * 0.55, fill=(*ECO, int(120 * glow * a / 255)))
    wf = 0.5 + 0.5 * math.sin(t * 60)
    for sg in (-1, 1):
        ss.oval(x + sg * s * 0.18, y - s * 0.22, s * 0.32, s * 0.1 + s * 0.05 * wf, -sg * 0.6, fill=(220, 235, 255, int(130 * a / 255)),
                ink=(*INK, int(a * 0.7)), w=2)
    for k in range(3):
        for sg in (-1, 1):
            ss.line([(x + sg * s * 0.05, y + s * 0.02 * k), (x + sg * s * 0.35, y + s * (0.2 + 0.12 * k)),
                     (x + sg * s * 0.42, y + s * (0.45 + 0.1 * k))], (*INK, a), max(1.5, s * 0.025))
    ss.oval(x, y, s * 0.08, s * 0.32, 0.25, fill=(*col, a), ink=(*INK, a), w=2)
    ss.circle(x - s * 0.06, y - s * 0.3, s * 0.08, fill=(*col, a))
    ss.line([(x - s * 0.1, y - s * 0.34), (x - s * 0.3, y - s * 0.5)], (*INK, a), max(1.5, s * 0.02))


def arcs(ss, cx, cy, t, dirn, col=SON, speed=520.0, gap=110.0, rmax=900.0, spread=0.55, w=10, a=255, r0=40, n=None):
    """arcos de sonar saindo de (cx, cy) na direção dirn (rad)"""
    k = 0
    m = int(rmax / gap) + 1 if n is None else n
    for k in range(m):
        r = r0 + ((t * speed + k * gap) % rmax)
        fa = (1 - r / (rmax + r0)) ** 1.2
        if fa <= 0.02: continue
        pts = A.ell_pts(cx, cy, r, r, 0, 24, dirn - spread, dirn + spread)
        ss.line(pts, (*col, int(a * fa)), w)


# ======================================================================= noite
def night_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (8, 12, 34)), (0.55, NAVY2), (1, (18, 28, 64))])
        ss = SS(W, H, s=1)
        rng = np.random.default_rng(6)
        for _ in range(140):
            ss.circle(rng.uniform(0, W), rng.uniform(0, H * 0.6), rng.uniform(1, 3.2), fill=(255, 255, 240, int(rng.uniform(60, 220))))
        im.alpha_composite(ss.get())
        A.paste_c(im, A.glow(420, (255, 230, 170), 90), 800, 470)
        ss = SS(W, H, s=2)
        ss.circle(800, 470, 150, fill=MOON)
        ss.circle(760, 430, 30, fill=(240, 222, 180)); ss.circle(850, 520, 22, fill=(240, 222, 180))
        im.alpha_composite(ss.get())
        return im
    return cached("night", mk).copy()


def trees(img, t, layer=0):
    def mk(layer):
        ss = SS(W + 400, H, s=1)
        rng = np.random.default_rng(10 + layer)
        col = (34, 40, 86) if layer == 0 else INDIGO
        base = 1500 if layer == 0 else 1840
        if layer == 1:
            for k in range(14):
                x = k * (W + 400) / 13 + rng.uniform(-40, 40)
                ss.circle(x, base - rng.uniform(0, 60), rng.uniform(70, 120), fill=col)
        for k in range(9 if layer == 0 else 0):
            x = k * (W + 400) / 8 + rng.uniform(-60, 60)
            hgt = rng.uniform(400, 640)
            ss.rect(x - 22, base - hgt * 0.5, x + 22, H, col)
            for j in range(6):
                ss.circle(x + rng.uniform(-150, 150), base - hgt + rng.uniform(0, hgt * 0.5), rng.uniform(110, 190), fill=col)
        ss.rect(0, base, W + 400, H, col)
        return ss.get()
    lay = cached(f"trees{layer}", lambda: mk(layer))
    dx = -((t * (12 if layer == 0 else 26)) % 200)
    A.paste(img, lay, int(dx - 100), 0)


# ======================================================================= cena 1: gancho
BX, BY, BS = 520, 1440, 620
MX, MY = 800, 760


def hook_frame(t, bx=None, by=None, bs=None, mos=1.0, mouth=None, son=1.0, bright=1.0):
    img = night_bg()
    trees(img, t, 0)
    ss = SS(W, H, s=2)
    mx = MX + 30 * math.sin(t * 2.3) + 14 * math.sin(t * 7.1); my = MY + 24 * math.sin(t * 3.1)
    if mos > 0:
        mosquito(ss, mx, my, 70, t, a=int(255 * mos))
    bx = BX + 14 * math.sin(t * 1.3) if bx is None else bx
    by = BY + 22 * math.sin(t * 4.5) if by is None else by
    bs = BS if bs is None else bs
    if son > 0:
        hx, hy = bx, by - 0.11 * bs
        arcs(ss, hx, hy, t, math.atan2(my - hy, mx - hx), a=int(230 * son), speed=600, gap=120, rmax=560, spread=0.5, w=9, r0=60)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    mo = (0.35 + 0.35 * math.sin(t * 6)) if mouth is None else mouth
    bat(ss, bx, by, bs, t=t, mouth=mo, eye=1.25)
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 22, 0.4)
    A.paste(img, sh, -pad + 10, -pad + 30)
    img.alpha_composite(sp)
    trees(img, t, 1)
    img = A.vignette(img, 0.45)
    if bright < 1:
        img = ImageEnhance.Brightness(img).enhance(bright)
    return img


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.03 + 0.01 * math.sin(lt * 1.2), rot=0.5 * math.sin(lt * 0.8))


# ======================================================================= cena 2: pra você, tudo preto
def dark(ctx, lt):
    t = lt + CTX["hook"].dur
    img = hook_frame(t, bright=0.07, son=0.0)
    ss = SS(W, H, s=2)
    # olho humano tentando enxergar
    q = ease(lt / 0.5)
    ex, ey = 540, 760
    blink = clamp01(1 - abs(math.sin(lt * 1.6 + 0.9)) * 6)
    op = max(0.06, 1 - blink)
    ss.oval(ex, ey, 230 * q + 1, 110 * q * op + 1, 0, fill=(240, 240, 235, int(200 * q)), ink=(*INK, int(255 * q)), w=6)
    if op > 0.4:
        ss.circle(ex + 30 * math.sin(lt * 3), ey, 70 * q + 1, fill=(60, 90, 130, int(255 * q)))
        ss.circle(ex + 30 * math.sin(lt * 3), ey, 34 * q + 1, fill=(10, 10, 14, int(255 * q)))
    for k in range(3):
        ss.text((ex - 160 + k * 160, ey + 230 + 18 * math.sin(lt * 4 + k)), "?", 110, "anton", fill=(200, 210, 240, int(200 * q)), stroke=6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.06 + 0.02 * lt / max(1, ctx.dur))


# ======================================================================= cena 3: Visão do Bicho (sonar)
def _world_lines():
    def mk():
        ss = SS(W, H, s=2)
        rng = np.random.default_rng(3)
        for k in range(5):
            x = 80 + k * 240 + rng.uniform(-40, 40)
            ss.line([(x, H), (x + rng.uniform(-30, 30), 700)], SON, 8)
            for j in range(4):
                y0 = rng.uniform(760, 1500); dx = rng.choice([-1, 1]) * rng.uniform(120, 260)
                ss.line([(x, y0), (x + dx, y0 - rng.uniform(80, 200))], SON, 5)
            for j in range(3):
                ss.circle(x + rng.uniform(-120, 120), rng.uniform(500, 800), rng.uniform(80, 150), ink=SON, w=4)
        for k in range(12):
            ss.line([(k * 100, 1820), (k * 100 + 60, 1790)], SON, 4)
        return ss.get()
    return cached("wlines", mk)


_DIST = {}


def _dist(cx, cy):
    key = (cx, cy)
    if key not in _DIST:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        _DIST[key] = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    return _DIST[key]


def pov_wings(img, t):
    ss = SS(W, H, s=2)
    f = math.sin(t * 9)
    for sg in (-1, 1):
        sx = 540 + sg * 120; sy = H + 60
        tip = (540 + sg * 640, 1560 - 160 * f)
        mid = (540 + sg * 470, 1720 - 80 * f)
        ss.poly([(sx, sy), tip, (lerp(tip[0], mid[0], 0.5) - sg * 30, lerp(tip[1], mid[1], 0.5) + 70), mid,
                 (lerp(mid[0], sx, 0.5), H + 80)], fill=MEM, ink=INK, w=6)
        ss.line([(sx, sy), tip], MEM_L, 10); ss.line([(sx, sy), mid], MEM_L, 8)
    for sg in (-1, 1):
        ss.poly([(540 + sg * 160, -40), (540 + sg * 330, 150 + 10 * math.sin(t * 3)), (540 + sg * 360, -40)], fill=FUR, ink=INK, w=6)
        ss.poly([(540 + sg * 200, -40), (540 + sg * 320, 110 + 10 * math.sin(t * 3)), (540 + sg * 335, -40)], fill=PINK)
    img.alpha_composite(ss.get())


def vision(ctx, lt):
    img = Image.new("RGBA", (W, H), (4, 10, 20, 255))
    cx, cy = 540, 1750
    d = _dist(cx, cy)
    m = np.zeros((H, W), np.float32)
    period = 0.55
    for k in range(4):
        age = (lt % period) + k * period
        r = age * 1500
        m += np.exp(-((d - r) / 120.0) ** 2) * math.exp(-age * 0.9)
    m = np.clip(m * 1.3 + 0.08, 0, 1)
    wl = _world_lines()
    a = np.asarray(wl.split()[3], np.float32) * m
    lay = wl.copy(); lay.putalpha(Image.fromarray(a.astype(np.uint8)))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1)))
    gl = lay.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(gl)
    # anéis visíveis
    ss = SS(W, H, s=2)
    for k in range(4):
        age = (lt % period) + k * period
        r = age * 1500
        ss.circle(cx, cy, r, ink=(*SON, int(120 * math.exp(-age * 1.2))), w=5)
    # o mosquito acende quando o eco volta
    mx, my = 640 + 40 * math.sin(lt * 2.4), 820 + 30 * math.sin(lt * 3.3)
    dm = math.hypot(mx - cx, my - cy)
    hit = 0.0
    for k in range(4):
        age = (lt % period) + k * period
        hit = max(hit, math.exp(-((age * 1500 - dm) / 160.0) ** 2))
    mosquito(ss, mx, my, 90, lt, a=int(110 + 145 * hit), glow=0.4 + 0.6 * hit, col=(255, 190, 120))
    ss.text((mx + 150, my - 40), "jantar", 42, "mont-ExtraBold", fill=(*ECO, int(255 * ease((lt - ctx.wt("som")) / 0.4))), anchor="lm", stroke=5)
    img.alpha_composite(ss.get())
    pov_wings(img, lt)
    return A.cam(img, zoom=1.02 + 0.015 * math.sin(lt * 2), dy=6 * math.sin(lt * 4.5))


# ======================================================================= cena 4: o grito agudo
def shout(ctx, lt):
    img = A.vgrad(W, H, [(0, (16, 24, 60)), (1, (40, 34, 90))])
    tg = ctx.wt("grito"); to = ctx.wt("ouvido")
    ss = SS(W, H, s=2)
    go = ease((lt - tg + 0.2) / 0.3)
    # onda aguda saindo da boca
    for k in range(5):
        y0 = 980 - k * 120 - ((lt * 400) % 120)
        amp = 26 * (1 - k / 6) * go
        pts = [(x, y0 + amp * math.sin(x * 0.11 + lt * 30)) for x in range(220, 861, 8)]
        ss.line(pts, (*SON, int(220 * go * (1 - k / 6))), 7)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    bat(ss, 540, 1580, 980, t=lt * 0.6, flap=0.2 + 0.15 * math.sin(lt * 3), mouth=0.3 + 0.7 * go, eye=1.2)
    img.alpha_composite(ss.get())
    # barras: você ouve até 20 mil/s; o grito vai até ~80 mil/s
    hb = ease((lt - to + 0.5) / 0.5)
    if hb > 0:
        ss = SS(W, H, s=2)
        ss.rrect(90, 480, 990, 740, 34, fill=(10, 14, 30, int(225 * hb)), ink=(*INK, int(255 * hb)), w=6)
        ss.text((130, 540), "VOCÊ OUVE", 40, "anton", fill=(255, 255, 255, int(255 * hb)), anchor="lm")
        ss.rrect(360, 515, 360 + 200 * hb, 565, 18, fill=(255, 255, 255, int(255 * hb)))
        ss.text((580, 540), "20 mil/s", 36, "mont-ExtraBold", fill=(255, 255, 255, int(255 * hb)), anchor="lm")
        ss.text((130, 660), "MEU GRITO", 40, "anton", fill=(*SON, int(255 * hb)), anchor="lm")
        ss.rrect(360, 635, 360 + 560 * hb, 685, 18, fill=(*SON, int(255 * hb)))
        ss.text((640, 660), "até 80 mil/s", 34, "mont-ExtraBold", fill=(*INK, int(255 * hb)), anchor="mm")
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * go, dx=4 * go * math.sin(lt * 40))


# ======================================================================= cena 5: o eco volta
def _ping(ss, lt, x0, y, x1, period, t_off=0.0, s=1.0):
    """um ping: arco ciano vai de x0 até x1, volta laranja. Devolve (fase, acerto)"""
    ph = ((lt - t_off) % period) / period
    if ph < 0.5:
        r = lerp(60, x1 - x0, ph / 0.5)
        ss.line(A.ell_pts(x0, y, r, r, 0, 20, -0.5, 0.5), (*SON, 240), 10 * s)
        hit = 0.0
    else:
        r = lerp(x1 - x0, 60, (ph - 0.5) / 0.5)
        ss.line(A.ell_pts(x1, y, x1 - x0 - r + 60, x1 - x0 - r + 60, 0, 20, math.pi - 0.5, math.pi + 0.5), (*ECO, 240), 10 * s)
        hit = math.exp(-(ph - 0.5) * 12)
    return ph, hit


def echo(ctx, lt):
    img = night_bg()
    trees(img, lt * 0.3, 0)
    img = ImageEnhance.Brightness(img).enhance(0.7)
    tb = ctx.wt("bate"); tv = ctx.wt("volta")
    ss = SS(W, H, s=2)
    x0, y, x1 = 300, 900, 860
    # um ping sincronizado com a fala: sai no início, bate em "bate", volta em "volta"
    span = max(0.6, tb)
    if lt < tb:
        r = lerp(60, x1 - x0, ease(lt / span))
        ss.line(A.ell_pts(x0, y, r, r, 0, 24, -0.5, 0.5), (*SON, 240), 12)
        hit = 0.0
    else:
        u = clamp01((lt - tb) / max(0.5, tv - tb + 0.4))
        rr = lerp(60, x1 - x0, u)
        ss.line(A.ell_pts(x1, y, rr, rr, 0, 24, math.pi - 0.5, math.pi + 0.5), (*ECO, 240), 12)
        hit = math.exp(-(lt - tb) * 3)
        if u >= 1:
            ss.circle(x0, y - 120, 60 + 20 * math.sin(lt * 10), fill=(*ECO, 90))
    mosquito(ss, x1 + 10 * math.sin(lt * 3), y + 12 * math.sin(lt * 4), 110, lt, glow=hit)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    bat(ss, x0 - 60, y + 40, 360, t=lt, rot=12, mouth=0.6 if lt < 0.4 else 0.2, eye=1.2)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.04 + 0.02 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 6: longe × perto
def near(ctx, lt):
    img = A.vgrad(W, H, [(0, (14, 22, 54)), (1, (30, 36, 84))])
    tr = ctx.wt("rápido"); tp = ctx.wt("perto")
    ss = SS(W, H, s=2)
    rows = ((770, 900, 1.6, "LONGE", "eco demora", (180, 200, 255)), (1590, 560, 0.7, "PERTO", "eco rápido", ECO))
    for k, (y, xm, per, t1, t2, col) in enumerate(rows):
        qa = ease((lt - (0 if k == 0 else tp - 0.6)) / 0.4)
        if qa <= 0: continue
        ss.rrect(60, y - 280, 1020, y + 250, 40, fill=(8, 12, 30, int(200 * qa)), ink=(*INK, int(255 * qa)), w=6)
        _ping(ss, lt, 230, y, xm, per)
        mosquito(ss, xm + 50, y, 80, lt)
        ss.text((100, y - 220), t1, 56, "anton", fill=(*col, int(255 * qa)), anchor="lm", stroke=6)
        ss.text((980, y - 220), t2, 40, "mont-ExtraBold", fill=(255, 255, 255, int(255 * qa)), anchor="rm", stroke=5)
        # relógio do eco
        ph = (lt % per) / per
        ss.rrect(100, y + 160, 980, y + 200, 18, fill=(40, 46, 80, int(255 * qa)))
        ss.rrect(100, y + 160, lerp(110, 980, ph), y + 200, 18, fill=(*col, int(255 * qa)))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    for y in (770, 1590):
        bat(ss, 170, y + 20, 220, t=lt + y, rot=12, mouth=0.4, eye=1.1)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.9))


# ======================================================================= cena 7: o bote final (190/s)
def buzz(ctx, lt):
    img = night_bg()
    trees(img, lt * 3, 0)
    t1 = ctx.wt("190"); tb = ctx.wt("bote")
    q = ease((lt - tb + 0.3) / max(0.8, t1 - tb + 0.6))
    rate = lerp(12, 190, q)
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(2)
    for k in range(24):
        a = rng.uniform(0, 2 * math.pi); r0 = rng.uniform(300, 500)
        u = (lt * 1.8 + rng.uniform(0, 1)) % 1
        r = r0 + u * 700
        ss.line([(540 + r * math.cos(a), 900 + r * math.sin(a)), (540 + (r + 160) * math.cos(a), 900 + (r + 160) * math.sin(a))],
                (255, 255, 255, int(120 * q)), 4)
    mx, my = 540 + 20 * math.sin(lt * 9), 920 + 15 * math.cos(lt * 11)
    mosquito(ss, mx, my, lerp(80, 150, q), lt, glow=q)
    gap = lerp(140, 26, q)
    arcs(ss, 540, 1420, lt, -math.pi / 2, speed=lerp(500, 1400, q), gap=gap, rmax=520, spread=0.6, w=lerp(10, 6, q), r0=80)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    bat(ss, 540, lerp(1680, 1620, q), lerp(700, 900, q), t=lt * 1.5, mouth=0.9, eye=1.3)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ss.rrect(300, 520, 780, 740, 40, fill=(8, 12, 30, 225), ink=INK, w=6)
    ss.text((540, 615), f"{int(rate)}", 130, "anton", fill=SON, stroke=8)
    ss.text((540, 708), "gritos por segundo", 34, "mont-ExtraBold", fill=(255, 255, 255))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.08 * q, dx=4 * q * math.sin(lt * 50), dy=4 * q * math.cos(lt * 43))


# ======================================================================= cena 8: sensor de ré
def car_side(ss, x, y, s):
    """carro de lado, traseira para a direita (x = para-choque traseiro)"""
    body = [(x, y - 0.3 * s), (x - 0.05 * s, y - 0.62 * s), (x - 0.3 * s, y - 0.66 * s), (x - 0.42 * s, y - 1.0 * s),
            (x - 1.05 * s, y - 1.0 * s), (x - 1.3 * s, y - 0.66 * s), (x - 1.75 * s, y - 0.6 * s), (x - 1.8 * s, y - 0.3 * s),
            (x - 1.75 * s, y - 0.1 * s), (x - 0.02 * s, y - 0.1 * s)]
    ss.poly(body, fill=(70, 150, 140), ink=INK, w=6)
    ss.poly([(x - 0.36 * s, y - 0.66 * s), (x - 0.46 * s, y - 0.92 * s), (x - 0.72 * s, y - 0.92 * s), (x - 0.72 * s, y - 0.66 * s)], fill=(190, 230, 250), ink=INK, w=4)
    ss.poly([(x - 0.8 * s, y - 0.66 * s), (x - 0.8 * s, y - 0.92 * s), (x - 1.02 * s, y - 0.92 * s), (x - 1.2 * s, y - 0.66 * s)], fill=(190, 230, 250), ink=INK, w=4)
    for wx in (x - 0.38 * s, x - 1.42 * s):
        ss.circle(wx, y - 0.1 * s, 0.2 * s, fill=(30, 30, 36), ink=INK, w=5)
        ss.circle(wx, y - 0.1 * s, 0.09 * s, fill=(170, 170, 180))
    ss.rrect(x - 0.06 * s, y - 0.4 * s, x + 0.02 * s, y - 0.3 * s, 6, fill=(255, 90, 70), ink=INK, w=3)
    ss.circle(x, y - 0.22 * s, 0.025 * s, fill=(30, 30, 36))


def car(ctx, lt):
    img = A.vgrad(W, H, [(0, (40, 46, 70)), (0.7, (70, 72, 96)), (1, (50, 50, 60))])
    ss = SS(W, H, s=2)
    ss.rect(0, 1360, W, H, (60, 60, 70))
    for k in range(8):
        ss.rect(k * 150, 1380, k * 150 + 80, 1395, (230, 210, 80))
    # muro à direita (tijolos)
    wx = 900
    ss.rect(wx, 700, W, 1360, (160, 80, 64))
    for r in range(14):
        off = 40 if r % 2 else 0
        for c in range(4):
            ss.rrect(wx + off + c * 90 - 40, 700 + r * 47 + 3, wx + off + c * 90 + 40, 700 + r * 47 + 44, 4, fill=(184, 98, 76))
    q = easeio(clamp01(lt / max(1.0, ctx.dur - 0.3)))
    cx = lerp(560, 860, q)
    car_side(ss, cx, 1360, 300)
    gap = wx - cx
    per = lerp(0.6, 0.12, q)
    arcs(ss, cx + 4, 1290, lt, 0.0, speed=gap / 0.2 + 80, gap=max(24, gap * 0.35), rmax=max(40, gap), spread=0.5, w=6, r0=10)
    img.alpha_composite(ss.get())
    # display do sensor: barras + bip
    ss = SS(W, H, s=2)
    ss.rrect(140, 480, 940, 750, 36, fill=(10, 12, 24, 230), ink=INK, w=6)
    ss.text((540, 540), "SENSOR DE RÉ", 50, "anton", fill=(255, 255, 255))
    nb = int(1 + 7 * q)
    for k in range(8):
        col = (80, 220, 120) if k < 3 else ((255, 210, 60) if k < 6 else (255, 80, 60))
        on = k < nb
        ss.rrect(190 + k * 90, 600, 260 + k * 90, 710, 10, fill=col if on else (40, 44, 60))
    beep = ((lt % per) / per) < 0.45
    if beep:
        ss.text((880, 430), "BIP", 46, "anton", fill=(255, 222, 40), stroke=6)
    # o morcego no canto fazendo igual
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    ss.rrect(60, 1450, 420, 1790, 30, fill=(12, 18, 46, 220), ink=INK, w=5)
    arcs(ss, 170, 1620, lt, 0.0, speed=500, gap=60, rmax=220, spread=0.5, w=5, r0=30)
    mosquito(ss, 370, 1620, 40, lt)
    bat(ss, 150, 1640, 160, t=lt, rot=14, mouth=0.5)
    ss.text((240, 1760), "= eu", 36, "mont-ExtraBold", fill=SON)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * q)


# ======================================================================= cena 9: o fio de 0,3 mm
def wire(ctx, lt):
    img = night_bg()
    trees(img, lt, 0)
    img = ImageEnhance.Brightness(img).enhance(0.8)
    td = ctx.wt("desvio")
    ss = SS(W, H, s=2)
    # fio fino vertical
    ss.line([(560, -20), (560, H + 20)], (220, 220, 230), 3)
    hl = ease((lt - ctx.wt("fio") + 0.2) / 0.4)
    if hl > 0:
        ss.line([(560, -20), (560, H + 20)], (255, 222, 40, int(160 * hl)), 12)
    # lupa
    if hl > 0:
        ss.circle(840, 640, 170, fill=(20, 26, 60, int(230 * hl)), ink=(255, 255, 255, int(255 * hl)), w=8)
        ss.rect(830, 480, 850, 800, (220, 220, 230, int(255 * hl)))
        ss.text((840, 860), "0,3 mm", 52, "anton", fill=(255, 222, 40, int(255 * hl)), stroke=6)
        ss.line([(560, 640), (670, 640)], (255, 255, 255, int(200 * hl)), 4)
    img.alpha_composite(ss.get())
    # morcego cruza da esquerda para a direita desviando
    u = clamp01((lt + 0.3) / max(1.0, ctx.dur + 0.2))
    bx = lerp(-200, 1300, u)
    by = 1250 - 260 * math.exp(-((bx - 560) / 220.0) ** 2)
    ss = SS(W, H, s=2)
    arcs(ss, bx + 120, by - 40, lt, -0.2, speed=700, gap=50, rmax=300, spread=0.5, w=6, r0=40)
    bat(ss, bx, by, 380, t=lt * 1.4, rot=lerp(10, -10, u) + 18 * math.sin((bx - 560) / 200.0), mouth=0.6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03, dx=-0.04 * (bx - 540))


# ======================================================================= cena 10: loop
def loop(ctx, lt):
    tc = ctx.wt("caçando")
    tr = lt - ctx.dur + 1 / 30.0
    if lt < tc - 0.2:
        # o bote: o morcego sobe até o mosquito e engole (o mosquito some)
        u = ease(lt / max(0.4, tc - 0.4))
        bx = lerp(BX, MX - 20, u); by = lerp(BY, MY + 120, u); bs = lerp(BS, 760, u)
        img = hook_frame(tr, bx=bx, by=by, bs=bs, mos=1 - u, mouth=0.9 - 0.8 * u, son=1 - u)
        return A.cam(img, zoom=1.03 + 0.05 * u)
    back = easeio(clamp01((lt - tc + 0.2) / max(0.3, ctx.dur - tc + 0.2)))
    bx = lerp(MX - 20, BX + 14 * math.sin(tr * 1.3), back)
    by = lerp(MY + 120, BY + 22 * math.sin(tr * 4.5), back)
    bs = lerp(760, BS, back)
    img = hook_frame(tr, bx=bx, by=by, bs=bs, mos=back, son=back)
    return A.cam(img, zoom=lerp(1.08, 1.03 + 0.01 * math.sin(tr * 1.2), back), rot=0.5 * math.sin(tr * 0.8) * back)


# ======================================================================= capa
def cover_bg(cv):
    img = night_bg()
    trees(img, 0.0, 0)
    ss = SS(W, H, s=2)
    mosquito(ss, 820, 700, 90, 0.0, glow=0.6)
    arcs(ss, 540, 1050, 0.3, math.atan2(700 - 1050, 820 - 540), speed=0, gap=120, rmax=560, spread=0.55, w=12, r0=120)
    img.alpha_composite(ss.get())
    trees(img, 0.0, 1)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 620)
    ss = SS(int(2.3 * s), int(1.3 * s), s=2)
    bat(ss, 1.15 * s, 0.68 * s, s, t=0.0, flap=0.75, mouth=0.75, eye=1.9)
    return ss.get()
