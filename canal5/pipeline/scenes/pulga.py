"""Dia 5A — "E se você fosse uma pulga pulando 80 vezes o seu tamanho?" (formato CURTO; paleta: tapete verde-musgo,
sol amarelo de manhã entrando pela janela, pulga castanho-avermelhada; raio-X violeta para a mola de resilina).

Cenas: hook (a pulga agachada no topo dos fios do tapete, arco pontilhado do pulo saindo da tela), vision/vision2
(Visão do Bicho: olhos simples, só luz e sombra; a sombra do cachorro passa, o calor chega, as patas na borda
pulam), human (você pulando um prédio de 40 andares), spring (raio-X: ela espreme a mola de borracha devagar),
lock (a trava engata), release (solta: a mola chuta a perna e ela dispara), gforce (medidor: 150 G),
astro (barras: astronauta 3 G × pulga 150 G), loop (cai de volta no tapete e carrega a mola: quadro inicial).
Fatos: Sutton & Burrows (2011, J. Exp. Biol.); Bennet-Clark & Lucey (1967); Rust & Dryden (1997).
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

FL = (156, 74, 42); FL_D = (98, 42, 26); FL_L = (214, 134, 84)
MOSS = (92, 136, 58); MOSS_D = (52, 86, 36); MOSS_L = (150, 190, 86)
SUN = (255, 214, 90)
RES = (190, 110, 255)        # resilina (raio-X violeta)
HEAT = (255, 70, 50)
GOLD = (236, 168, 70)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= pulga (perfil, cabeça para a direita)
def _leg(ss, P, pts, col, w, ink_w):
    q = P(pts)
    ss.line(q, (*INK, 255), w + ink_w * 2)
    ss.line(q, col, w)


def flea(ss, x, y, s, t=0.0, rot=0.0, flip=1, crouch=1.0, eye=1.0, xray=0.0, pad=0.0, alpha=255):
    """crouch: 1 = agachada (perna de trás dobrada), 0 = perna esticada (pulo). xray: corpo translúcido + mola.
    pad: 0..1 compressão da mola. Origem = centro do corpo; chão em y ≈ +0.46 quando agachada."""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.5, s * 0.008)
    lw = max(2, s * 0.022)
    ba = int(alpha * (1 - 0.6 * xray))
    # pernas da frente e do meio (finas)
    for k, (cx0, ph) in enumerate(((0.28, 0.0), (0.12, 1.4))):
        sw = 0.02 * math.sin(t * 7 + ph)
        _leg(ss, P, [(cx0, 0.16), (cx0 + 0.12, 0.3), (cx0 + 0.06 + sw, 0.42), (cx0 + 0.14 + sw, 0.46)], FL_D, lw * 0.8, iw * 0.6)
    # perna de trás (enorme): coxa -> joelho -> tornozelo -> pé
    c = clamp01(crouch)
    knee = (lerp(-0.34, 0.14, c), lerp(0.52, 0.3, c))
    ank = (lerp(-0.5, -0.2, c), lerp(0.86, 0.42, c))
    foot = (lerp(-0.66, -0.02, c), lerp(0.98, 0.47, c))
    hip = (-0.14, 0.14)
    ss.poly(P(A.spline([(hip[0] - 0.08, hip[1] - 0.04), (hip[0] + 0.1, hip[1] - 0.02), (knee[0] + 0.03, knee[1]),
                        (knee[0] - 0.02, knee[1] + 0.05), (hip[0] - 0.08, hip[1] + 0.1)], 5)), fill=(*FL, ba), ink=(*INK, alpha), w=iw)
    _leg(ss, P, [knee, ank], FL, lw * 1.3, iw * 0.7)
    _leg(ss, P, [ank, foot], FL_D, lw * 0.9, iw * 0.6)
    for k in range(4):  # espinhos da tíbia
        u = (k + 1) / 5; px = lerp(knee[0], ank[0], u); py = lerp(knee[1], ank[1], u)
        ss.line(P([(px, py), (px - 0.05, py - 0.02)]), (*INK, alpha), max(1, s * 0.005), cap=False)
    # corpo (achatado dos lados, placas)
    body = A.spline([(0.48, 0.02), (0.44, -0.14), (0.3, -0.25), (0.05, -0.31), (-0.22, -0.3), (-0.42, -0.2),
                     (-0.53, -0.02), (-0.47, 0.13), (-0.26, 0.22), (0.05, 0.24), (0.3, 0.19), (0.44, 0.12)], 6)
    ss.poly(P(body), fill=(*FL, ba), ink=(*INK, alpha), w=iw)
    ss.poly(P(A.spline([(0.36, -0.15), (0.1, -0.26), (-0.25, -0.25), (-0.4, -0.14), (-0.1, -0.17), (0.2, -0.14)], 5)),
            fill=(*FL_L, int(ba * 0.7)))
    for xx in (0.28, 0.14, 0.0, -0.14, -0.28, -0.4):
        top = -0.3 + 0.12 * (abs(xx) / 0.45) ** 2; bot = 0.23 - 0.08 * (abs(xx) / 0.45) ** 2
        ss.line(P(A.bez((xx, top), (xx - 0.03, top * 0.4), (xx - 0.03, bot * 0.4), (xx, bot), 8)),
                (*FL_D, int(alpha * 0.8)), max(1, s * 0.006), cap=False)
        for k in range(2):  # cerdas para trás
            yy = lerp(top, bot, 0.25 + 0.4 * k)
            ss.line(P([(xx - 0.02, yy), (xx - 0.08, yy - 0.015)]), (*INK, int(alpha * 0.7)), max(1, s * 0.004), cap=False)
    # cabeça: antena, boca (estilete), olho
    ss.line(P(A.bez((0.4, -0.12), (0.36, -0.2), (0.3, -0.22), (0.26, -0.2), 6)), (*INK, alpha), max(1.5, s * 0.01))
    ss.line(P([(0.45, 0.1), (0.43, 0.22), (0.4, 0.3)]), (*FL_D, alpha), max(1.5, s * 0.012))
    ex, ey = P([(0.37, -0.05)])[0]; er = s * 0.032 * eye
    ss.circle(ex, ey, er * 1.2, fill=(*FL_D, alpha))
    ss.circle(ex, ey, er, fill=(18, 10, 12, alpha), ink=(*INK, alpha), w=max(1, iw * 0.6))
    ss.circle(ex - er * 0.32, ey - er * 0.34, er * 0.38, fill=(255, 255, 255, int(240 * alpha / 255)))
    ss.circle(ex + er * 0.3, ey + er * 0.3, er * 0.14, fill=(255, 255, 255, int(170 * alpha / 255)))
    # raio-X: a mola de resilina acima da perna de trás
    if xray > 0.01:
        coil(ss, P, (-0.3, -0.08), (lerp(0.12, -0.08, pad), -0.08), 0.085, 7, int(255 * xray), glow=pad)


def coil(ss, P, p0, p1, r, n, a=255, glow=0.0, w=None):
    """mola em zigue-zague de p0 a p1 (unidades do corpo)"""
    pts = []
    m = n * 2
    for k in range(m + 1):
        u = k / m
        x = lerp(p0[0], p1[0], u); yy = lerp(p0[1], p1[1], u) + (r if k % 2 else -r) * (0 if k in (0, m) else 1)
        pts.append((x, yy))
    q = P(pts)
    ww = w or max(3, abs(q[0][0] - q[-1][0]) * 0.04 + 6)
    if glow > 0:
        ss.line(q, (*RES, int(a * 0.35 * glow)), ww * 4)
    ss.line(q, (*INK, a), ww + 6)
    ss.line(q, (*RES, a), ww)
    ss.line(q, (240, 220, 255, int(a * 0.7)), max(1, ww * 0.3))


# ======================================================================= tapete e sala
def room_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (232, 214, 160)), (0.45, (196, 170, 110)), (0.7, (120, 130, 70)), (1, (60, 84, 40))])
        ss = SS(W, H, s=1)
        # janela e faixa de sol
        ss.poly([(640, -40), (1120, -40), (1120, 900), (300, 1700)], fill=(255, 240, 170, 70))
        ss.rect(700, 120, 1020, 560, (255, 248, 210, 160))
        # sofá e cachorro desfocados ao fundo
        ss.rrect(-80, 520, 520, 980, 70, fill=(176, 92, 64, 255))
        ss.ellipse(260, 860, 260, 120, fill=(GOLD[0], GOLD[1], GOLD[2], 255))
        ss.circle(470, 760, 110, fill=(GOLD[0], GOLD[1], GOLD[2], 255))
        ss.ellipse(420, 720, 40, 90, fill=(170, 110, 50, 255))
        im.alpha_composite(ss.get())
        return im.filter(ImageFilter.GaussianBlur(26))
    return cached("room", mk).copy()


def fibers(img, t, y0, n=120, seed=1, s=1.0, col=MOSS, dark=MOSS_D, light=MOSS_L, sway=1.0, blur=0):
    rng = np.random.default_rng(seed)
    ss = SS(W, H, s=2)
    for _ in range(n):
        x = rng.uniform(-40, W + 40); hgt = rng.uniform(260, 520) * s; ph = rng.uniform(0, 6.28)
        lean = rng.uniform(-0.25, 0.25) + 0.05 * sway * math.sin(t * 1.3 + ph)
        base = y0 + rng.uniform(0, 260) * s
        top = (x + lean * hgt, base - hgt)
        pts = A.bez((x, H + 40), (x, base - hgt * 0.3), (top[0] - lean * 60, base - hgt * 0.8), top, 10)
        cc = A.mixc(dark, col, rng.uniform(0.2, 1))
        ww = rng.uniform(14, 26) * s
        ss.line(pts, (*INK, 255), ww + 5)
        ss.line(pts, cc, ww)
        ss.line(pts[4:], (*light, 150), ww * 0.3)
    im = ss.get()
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(im)


def dotted_arc(ss, x0, y0, x1, y1, peak, t, col=(255, 255, 255), a=255, n=26, r=10, speed=1.0, upto=1.0):
    for k in range(n):
        u = ((k + t * speed) % n) / n
        if u > upto: continue
        x = lerp(x0, x1, u); y = lerp(y0, y1, u) - peak * 4 * u * (1 - u)
        ss.circle(x, y, r * (0.7 + 0.3 * math.sin(u * math.pi)), fill=(*col, a), ink=(*INK, a), w=3)


# ======================================================================= cena 1: gancho
FX, FY, FS = 480, 1440, 580


def hook_frame(t, fx=None, fy=None, fs=None, crouch=None, xray=0.0, pad=0.0, arc=1.0, rot=None):
    img = room_bg()
    fibers(img, t, 1380, 60, seed=7, s=0.75, col=(110, 150, 70), blur=5)
    fibers(img, t, 1640, 50, seed=11, s=0.55)
    fx = FX + 6 * math.sin(t * 1.1) if fx is None else fx
    fy = FY + 5 * math.sin(t * 2.3) if fy is None else fy
    fs = FS if fs is None else fs
    c = 1.0 - 0.04 * (0.5 + 0.5 * math.sin(t * 5)) if crouch is None else crouch
    if arc > 0:
        ss = SS(W, H, s=2)
        dotted_arc(ss, fx + 60, fy - 80, 1300, 200, 900, t, col=(255, 236, 120), a=int(255 * arc), speed=6.0, r=15)
        img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    flea(ss, fx, fy, fs, t=t, rot=-6 if rot is None else rot, crouch=c, eye=1.2, xray=xray, pad=pad)
    sp = ss.get()
    sh, padd = A.shadow_of(sp, 18, 0.45)
    A.paste(img, sh, -padd + 8, -padd + 26)
    img.alpha_composite(sp)
    fibers(img, t, 1760, 60, seed=3, s=0.5)
    return A.vignette(img, 0.4)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.03 + 0.01 * math.sin(lt * 1.2), rot=0.4 * math.sin(lt * 0.7))


# ======================================================================= cenas 2-3: Visão do Bicho (luz e sombra)
def _pixelate(im, k):
    sm = im.resize((max(1, W // k), max(1, H // k)), Image.BILINEAR)
    return sm.resize((W, H), Image.NEAREST)


def pov_legs(img, t, crouch=1.0, jump=0.0):
    ss = SS(W, H, s=2)
    for sg in (-1, 1):
        bx = 540 + sg * 260; by = H + 40 - 0 * jump
        kx = bx + sg * lerp(170, 60, jump); ky = lerp(1560, 1700, jump) + 10 * math.sin(t * 6 + sg)
        fx = bx + sg * lerp(250, 120, jump); fy = H + 30
        for pts, w in (([(bx, by), (kx, ky)], 46), ([(kx, ky), (fx, fy)], 34)):
            ss.line(pts, (*INK, 255), w + 10); ss.line(pts, FL, w)
        for k in range(3):
            u = (k + 1) / 4
            px, py = lerp(kx, fx, u), lerp(ky, fy, u)
            ss.line([(px, py), (px + sg * 30, py - 14)], INK, 5)
    # antenas curtinhas no alto
    for sg in (-1, 1):
        pts = A.bez((540 + sg * 120, -30), (540 + sg * 160, 120), (540 + sg * 230, 160), (540 + sg * 300, 140 + 10 * math.sin(t * 4)), 10)
        ss.line(pts, (*INK, 255), 22); ss.line(pts, FL_D, 14)
    img.alpha_composite(ss.get())


def vision(ctx, lt):
    second = ctx.sc["id"] == "vision2"
    c1 = CTX.get("vision", ctx)
    t = lt + (c1.dur if second else 0.0)
    ts = c1.wt("sombra")
    # mundo da pulga: claro × escuro, quase sem forma
    base = room_bg()
    fibers(base, t, 1500, 50, seed=3, s=1.0)
    arr = np.asarray(base.convert("RGB"), np.float32)
    g = arr.mean(axis=2, keepdims=True)
    arr = np.clip((g - 90) * 1.6 + 110, 0, 255) * np.array([0.92, 1.0, 0.8], np.float32)
    img = Image.fromarray(arr.astype(np.uint8)).convert("RGBA").filter(ImageFilter.GaussianBlur(18))
    # a sombra do cachorro atravessando (da esquerda para a direita)
    u = ease((t - ts + 0.6) / 1.6)
    sx = lerp(-700, 520, u)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ss = SS(W, H, s=1)
    ss.ellipse(sx, 900, 640, 900, fill=(10, 14, 8, 225))
    sh.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(60)))
    img.alpha_composite(sh)
    if second:
        tq = ctx.wt("quente"); tp = ctx.wt("pular")
        hq = ease((lt - tq + 0.3) / 0.8)
        if hq > 0:
            gl = A.glow(560, HEAT, int(200 * hq))
            A.paste_c(img, gl, 560 + 20 * math.sin(lt * 3), 820)
            gl2 = A.glow(300, (255, 200, 80), int(150 * hq))
            A.paste_c(img, gl2, 560, 820)
        img = _pixelate(img, 36)
        jump = ease((lt - tp) / 0.25)
        pov_legs(img, t, jump=jump)
        if jump > 0:
            img.alpha_composite(Image.new("RGBA", (W, H), (255, 250, 230, int(200 * jump))))
        return A.cam(img, zoom=1.0 + 0.5 * jump, rot=2 * math.sin(lt * 1.3))
    img = _pixelate(img, 36)
    pov_legs(img, t)
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt), dx=5 * math.sin(lt * 1.5))


# ======================================================================= cena 4: você pulando um prédio de 40 andares
def person(ss, x, y, h, col=(60, 110, 200), a=255, run=0.0):
    hr = h * 0.13
    ss.circle(x, y - h + hr, hr, fill=(240, 196, 160, a), ink=(*INK, a), w=3)
    ss.rrect(x - h * 0.13, y - h + 2 * hr, x + h * 0.13, y - h * 0.42, h * 0.06, fill=(*col, a), ink=(*INK, a), w=3)
    for sg in (-1, 1):
        ss.line([(x, y - h * 0.45), (x + sg * h * 0.1 + run * sg * h * 0.1, y)], (*INK, a), max(3, h * 0.07))
        ss.line([(x, y - h * 0.75), (x + sg * h * 0.2, y - h * 0.55 - run * h * 0.2)], (*INK, a), max(3, h * 0.06))


def human(ctx, lt):
    img = A.vgrad(W, H, [(0, (160, 210, 250)), (0.7, (230, 240, 250)), (1, (200, 220, 200))])
    tp = ctx.wt("pular"); ta = ctx.wt("andares")
    ss = SS(W, H, s=2)
    # prédio de 40 andares
    bx0, bx1, top, base = 520, 820, 560, 1780
    grow = ease((lt - 0.0) / 0.9)
    tt = lerp(base, top, grow)
    ss.rect(bx0, tt, bx1, base, (120, 128, 150))
    fh = (base - top) / 40
    for k in range(40):
        yy = base - (k + 1) * fh
        if yy < tt: break
        for j in range(5):
            ss.rect(bx0 + 18 + j * 57, yy + fh * 0.22, bx0 + 52 + j * 57, yy + fh * 0.78, (210, 230, 250) if (k + j) % 3 else (255, 230, 150))
    ss.rrect(bx0, tt, bx1, base, 4, ink=INK, w=5)
    ss.rect(0, base, W, H, (110, 150, 90))
    if grow > 0.9:
        ss.text((bx1 + 20, top + 10), "40", 64, "anton", fill=(255, 255, 255), anchor="lm", stroke=7)
        ss.text((bx1 + 20, top + 70), "andares", 38, "mont-ExtraBold", fill=(255, 255, 255), anchor="lm", stroke=5)
    # você pula por cima
    q = ease((lt - tp + 0.1) / max(0.6, ta - tp + 0.8))
    x0, y0, x1, y1, pk = 300, base, 1000, base, 1400
    dotted_arc(ss, x0, y0 - 40, x1, y1 - 40, pk, lt, col=(255, 222, 40), n=30, r=9, speed=0, upto=q)
    px = lerp(x0, x1, q); py = lerp(y0, y1, q) - pk * 4 * q * (1 - q)
    person(ss, px, py, 90, run=1.0 if 0.02 < q < 0.98 else 0.0)
    img.alpha_composite(ss.get())
    # quadrinho: a pulga e os 17 cm
    ss = SS(W, H, s=2)
    ss.rrect(40, 1400, 400, 1760, 30, fill=(255, 250, 235, 235), ink=INK, w=5)
    ss.rect(60, 1700, 380, 1740, MOSS)
    flea(ss, 110, 1688, 70, t=lt, crouch=0.6)
    dotted_arc(ss, 125, 1680, 340, 1700, 230, lt, col=FL, n=14, r=6, speed=4)
    ss.text((220, 1440), "você = pulga", 30, "mont-ExtraBold", fill=INK)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 5: espremendo a mola (raio-X)
def xray_bg(seed=0):
    def mk():
        im = A.vgrad(W, H, [(0, (40, 20, 70)), (1, (16, 8, 34))])
        ss = SS(W, H, s=1)
        for k in range(0, H, 60):
            ss.line([(0, k), (W, k)], (120, 80, 200, 40), 2)
        for k in range(0, W, 60):
            ss.line([(k, 0), (k, H)], (120, 80, 200, 40), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("xbg", mk).copy()


def spring(ctx, lt):
    img = xray_bg()
    tm = ctx.wt("mola")
    q = easeio(clamp01((lt - 0.4) / max(1.0, ctx.dur - 0.6)))
    ss = SS(W, H, s=2)
    flea(ss, 520, 1540, 860, t=lt * 0.3, rot=-4, crouch=1.0, xray=1.0, pad=q, eye=1.1)
    # músculos puxando (setas para dentro)
    for sg in (-1, 1):
        cx = 520 + sg * 300
        A.arrow(ss, cx + sg * 120, 1400, cx - sg * 40, 1400, (255, 150, 200, int(255 * clamp01(lt / 0.5))), w=34, iw=4)
    img.alpha_composite(ss.get())
    # barra de energia guardada
    ss = SS(W, H, s=2)
    ss.rrect(190, 600, 890, 700, 40, fill=(20, 10, 30, 220), ink=INK, w=6)
    ss.rrect(206, 616, lerp(220, 874, q), 684, 30, fill=(255, 170, 60))
    ss.text((540, 560), "ENERGIA GUARDADA", 44, "anton", fill=(255, 220, 160), stroke=6)
    hq = ease((lt - tm + 0.2) / 0.5)
    if hq > 0:
        ss.text((540, 880), "devagar…", 60, "anton", fill=(*RES, int(255 * hq)), stroke=7)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.05 * q, dx=2 * q * math.sin(lt * 25))


# ======================================================================= cena 6: a trava
def lock(ctx, lt):
    img = xray_bg()
    tb = ctx.wt("borracha"); tt = ctx.wt("travo"); tc = ctx.wt("carregada")
    lk = ease((lt - tt) / 0.18)
    ss = SS(W, H, s=2)
    P = lambda pts: [(px, py) for px, py in pts]
    y = 1500
    # parede (corpo) à esquerda, placa da perna à direita
    ss.rrect(80, y - 260, 170, y + 260, 20, fill=FL_D, ink=INK, w=6)
    xr = 640
    coil(ss, P, (170, y), (xr, y), 120, 7, 255, glow=0.6 + 0.4 * math.sin(lt * 6) * 0.5, w=22)
    ss.rrect(xr, y - 200, xr + 70, y + 200, 16, fill=(200, 200, 215), ink=INK, w=6)
    ss.rrect(xr + 70, y - 30, 1000, y + 30, 14, fill=FL, ink=INK, w=6)
    ss.text((870, y + 90), "perna", 44, "mont-ExtraBold", fill=FL_L, stroke=5)
    # gancho da trava descendo e engatando
    hy = lerp(y - 520, y - 250, lk)
    hook_pts = [(xr + 110, hy - 300), (xr + 110, hy + 120), (xr + 60, hy + 170), (xr + 20, hy + 150), (xr + 40, hy + 110), (xr + 80, hy + 110), (xr + 80, hy - 300)]
    ss.poly(hook_pts, fill=(255, 210, 60), ink=INK, w=6)
    if lk >= 1:
        sp = math.exp(-(lt - tt - 0.18) * 4)
        for k in range(8):
            a = k / 8 * 2 * math.pi
            ss.line([(xr + 40 + 40 * math.cos(a), hy + 160 + 40 * math.sin(a)), (xr + 40 + (60 + 60 * sp) * math.cos(a), hy + 160 + (60 + 60 * sp) * math.sin(a))],
                    (255, 255, 200, int(255 * sp)), 8)
    ss.text((330, 900), "resilina", 80, "anton", fill=RES, stroke=8)
    ss.text((330, 985), "(tipo borracha)", 34, "mont-ExtraBold", fill=(220, 200, 255, int(255 * ease((lt - tb) / 0.5))), stroke=4)
    img.alpha_composite(ss.get())
    hq = ease((lt - tc + 0.1) / 0.4)
    if hq > 0:
        ss = SS(W, H, s=2)
        ss.rrect(190, 1800, 890, 1850, 25, fill=(255, 170, 60, int(255 * hq)), ink=INK, w=5)
        img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * lk, dy=-6 * lk * math.exp(-max(0, lt - tt) * 5) * math.sin(lt * 50))


# ======================================================================= cena 7: solta a trava, a mola chuta a perna
def release(ctx, lt):
    tch = ctx.wt("chuta"); td = ctx.wt("disparo")
    kick = ease((lt - tch) / 0.12)
    fly = clamp01((lt - tch - 0.12) / 1.2)
    img = room_bg()
    fibers(img, lt, 1380, 60, seed=7, s=0.75, col=(110, 150, 70), blur=5)
    fibers(img, lt, 1640, 50, seed=11, s=0.55)
    fy = FY - 2600 * fly ** 1.6
    ss = SS(W, H, s=2)
    if fly > 0:
        for k in range(10):
            yy = fy + 200 + k * 90
            ss.line([(470 - 120 + k * 25, yy), (470 - 120 + k * 25, yy + 160)], (255, 250, 220, int(200 * (1 - fly))), 8)
        r = 80 + 500 * fly
        ss.ellipse(470, 1740, r, r * 0.25, ink=(255, 250, 220, int(220 * (1 - fly))), w=10)
    flea(ss, FX, fy, FS, t=lt, rot=lerp(-6, -24, kick), crouch=1 - kick, eye=1.2, xray=1.0 - kick, pad=1.0 - kick)
    img.alpha_composite(ss.get())
    fibers(img, lt, 1760, 60, seed=3, s=0.5)
    sh = math.exp(-max(0, lt - tch) * 6) if lt > tch else 0
    return A.cam(A.vignette(img, 0.4), zoom=1.03 + 0.04 * kick, dx=14 * sh * math.sin(lt * 60), dy=10 * sh * math.cos(lt * 47))


# ======================================================================= cena 8: 150 G
def gdial(ss, cx, cy, r, v, vmax=160):
    ss.circle(cx, cy, r + 20, fill=(20, 24, 30, 235), ink=INK, w=8)
    for k in range(0, vmax + 1, 10):
        a = math.radians(lerp(140, 400, k / vmax))
        r0 = r - (34 if k % 50 == 0 else 18)
        col = (255, 90, 70) if k >= 100 else (230, 230, 230)
        ss.line([(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + r * math.cos(a), cy + r * math.sin(a))], col, 6 if k % 50 == 0 else 3)
        if k % 50 == 0:
            ss.text((cx + (r - 80) * math.cos(a), cy + (r - 80) * math.sin(a)), str(k), 40, "anton", fill=(240, 240, 240))
    a = math.radians(lerp(140, 400, clamp01(v / vmax)))
    ss.line([(cx, cy), (cx + (r - 30) * math.cos(a), cy + (r - 30) * math.sin(a))], (255, 222, 40), 14)
    ss.circle(cx, cy, 26, fill=(255, 222, 40), ink=INK, w=5)
    ss.text((cx, cy + r * 0.55), f"{int(v)} G", 84, "anton", fill=(255, 255, 255), stroke=8)


def gforce(ctx, lt):
    img = A.vgrad(W, H, [(0, (250, 226, 150)), (1, (200, 150, 70))])
    t1 = ctx.wt("150")
    v = 150 * ease((lt - 0.2) / max(0.6, t1 - 0.1)) + 3 * math.sin(lt * 30) * (lt > t1)
    ss = SS(W, H, s=2)
    # céu passando para baixo (riscos)
    rng = np.random.default_rng(4)
    for k in range(26):
        x = rng.uniform(0, W); ph = rng.uniform(0, 1)
        y = ((ph + lt * 2.5) % 1.0) * (H + 400) - 200
        ss.line([(x, y), (x, y + 220)], (255, 255, 255, 150), 6)
    gdial(ss, 540, 760, 300, v)
    flea(ss, 560, 1560, 430, t=lt, rot=-70, crouch=0.0, eye=1.2)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02, dx=5 * math.sin(lt * 37), dy=5 * math.cos(lt * 41))


# ======================================================================= cena 9: astronauta 3 G × pulga 150 G
def rocket(ss, x, y, s):
    ss.poly([(x, y - s), (x + s * 0.22, y - s * 0.6), (x + s * 0.22, y), (x - s * 0.22, y), (x - s * 0.22, y - s * 0.6)],
            fill=(235, 235, 240), ink=INK, w=5)
    ss.circle(x, y - s * 0.6, s * 0.09, fill=(120, 190, 255), ink=INK, w=4)
    for sg in (-1, 1):
        ss.poly([(x + sg * s * 0.22, y - s * 0.3), (x + sg * s * 0.4, y), (x + sg * s * 0.22, y)], fill=(230, 60, 60), ink=INK, w=4)
    ss.poly([(x - s * 0.15, y), (x, y + s * 0.4), (x + s * 0.15, y)], fill=(255, 170, 40), ink=INK, w=4)


def astro(ctx, lt):
    img = A.vgrad(W, H, [(0, (20, 30, 70)), (1, (60, 50, 110))])
    ta = ctx.wt("astronauta"); t3 = ctx.wt("3")
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(9)
    for _ in range(60):
        ss.circle(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(1.5, 4), fill=(255, 255, 255, int(rng.uniform(80, 220))))
    base = 1700
    qf = 1.0
    hf = 1100 * qf
    ss.rrect(600, base - hf, 900, base, 24, fill=(255, 170, 60), ink=INK, w=6)
    ss.text((750, base - hf - 60), "150 G", 80, "anton", fill=(255, 222, 40), stroke=8)
    flea(ss, 750, base + 110, 160, t=lt, crouch=1.0)
    qa = ease((lt - ta + 0.2) / 0.6)
    ha = 22 * ease((lt - t3 + 0.3) / 0.5)
    ss.rrect(180, base - max(10, ha), 480, base, 10, fill=(120, 190, 255), ink=INK, w=6)
    ss.text((330, base + 70), "3 G", 80, "anton", fill=(170, 220, 255, int(255 * qa)), stroke=8)
    rocket(ss, 330, base - 220, 300 * qa + 1)
    ss.line([(120, base), (960, base)], (255, 255, 255), 6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.03 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 10: loop
def loop(ctx, lt):
    ttu = ctx.wt("tudo"); tc = ctx.wt("carrego")
    tr = lt - ctx.dur + 1 / 30.0
    if lt < ttu:
        # caindo de volta (errou o cachorro)
        u = clamp01(lt / max(0.3, ttu))
        fy = lerp(-300, FY, u * u)
        img = hook_frame(tr, fy=fy, crouch=0.2 + 0.8 * u, arc=0.0, rot=lerp(30, -6, u))
        return A.cam(img, zoom=1.06)
    land = math.exp(-(lt - ttu) * 6)
    back = easeio(clamp01((lt - ttu) / max(0.3, ctx.dur - ttu)))
    pad = ease((lt - tc + 0.2) / 0.8) * (1 - back)
    img = hook_frame(tr, xray=pad, pad=pad, arc=back)
    return A.cam(img, zoom=lerp(1.06, 1.03 + 0.01 * math.sin(tr * 1.2), back), dy=8 * land * math.sin(lt * 40),
                 rot=0.4 * math.sin(tr * 0.7) * back)


# ======================================================================= capa
def cover_bg(cv):
    img = room_bg()
    fibers(img, 0.0, 1380, 60, seed=7, s=0.75, col=(110, 150, 70), blur=5)
    ss = SS(W, H, s=2)
    dotted_arc(ss, 560, 1300, 1300, 300, 900, 0.0, col=(255, 236, 120), speed=0)
    img.alpha_composite(ss.get())
    fibers(img, 0.0, 1640, 50, seed=11, s=0.55)
    fibers(img, 0.0, 1760, 60, seed=3, s=0.5)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 560)
    ss = SS(int(1.3 * s), int(1.1 * s), s=2)
    flea(ss, 0.62 * s, 0.42 * s, s, t=0.3, crouch=1.0, eye=1.9)
    return ss.get()
