"""Dia 8A — "E se você fosse um beija-flor?" (formato CURTO; paleta: jardim tropical ao meio-dia, céu turquesa,
folhas verde-folha, flores magenta e laranja, beija-flor verde-esmeralda com garganta rubi; noite azul-marinho com
lua fria; coração em raio-X vermelho, oxigênio em verde, frio em azul).

Cenas: hook (beija-flor parado no ar na flor, coração piscando no peito, eletrocardiograma correndo), human (dois corações
lado a lado: o humano grande e lento × o do beija-flor pequeno e disparado), vision (Visão do Bicho: movimento — o mundo vira
setas de fluxo em todas as direções, bico na borda), wings (asas em câmera lenta desenhando o "8", fantasmas das batidas),
oxygen (raio-X: ar verde entrando pelos pulmões, músculo do peito vermelho queimando), pump (close do coração bombeando com
cronômetro de 1 s e 20 batidas), night (noite: poleiro no galho, flores fechadas, chave do motor em OFF), torpor (monitor
caindo de 1.200 para 50), cold (termômetro descendo, o bicho azulado de frio), loop (amanhece e volta ao quadro inicial).
Fatos: Lasiewski et al. (1967, The Auk); Wolf et al. (2020, Biology Letters); Gaede et al. (2017, Current Biology).
"""
import math
import numpy as np
from PIL import Image, ImageEnhance
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

EMER = (40, 190, 120); EMER_D = (20, 120, 80); EMER_L = (120, 230, 170)
RUBY = (230, 40, 90); BELLY = (236, 240, 226)
BEAK = (40, 34, 40)
MAG = (230, 50, 150); ORG = (255, 140, 40); LEAF = (50, 150, 70); LEAF_D = (28, 96, 52)
SKY0 = (60, 200, 210); SKY1 = (180, 240, 230)
NAVY = (14, 22, 52)
RED = (240, 50, 60); BLUE = (80, 160, 255); GREEN = (80, 230, 120)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


def glow_at(img, x, y, r, col, a):
    A.paste_c(img, A.glow(int(r), col, int(a)), x, y)


# ======================================================================= beija-flor (de lado, olhando para a direita)
def hummer(ss, x, y, s, rot=0.0, t=0.0, flap=None, eye=1.0, alpha=255, heart=0.0, flip=1, wings=True, tint=None,
           xray=False, perched=False):
    """origem = centro do corpo; s = comprimento do corpo (bico à cauda ~ 2.2 s)."""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    a = alpha
    iw = max(1.5, s * 0.02)
    body = EMER if tint is None else A.mixc(EMER, tint, 0.55)
    bodyd = EMER_D if tint is None else A.mixc(EMER_D, tint, 0.55)
    belly = BELLY if tint is None else A.mixc(BELLY, tint, 0.4)
    f = (0.5 + 0.5 * math.sin(t * 30)) if flap is None else flap
    # asa de trás (borrão)
    def wing(phase, back):
        ang = lerp(-75, 35, phase)
        c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        L = 0.95
        tip = (0.05 + L * c * 0.55, -0.12 - L * sn * 0.9 - 0.25)
        pts = [(0.08, -0.12), (tip[0] - 0.12, tip[1] + 0.05), tip, (tip[0] + 0.1, tip[1] + 0.12), (-0.12, -0.02)]
        col = bodyd if back else body
        return P(A.spline(pts, n=6)), col
    if wings and not perched:
        for k, g in enumerate((0.0, 0.33, 0.66)):  # borrão das batidas
            ph = (f + g) % 1
            pts, col = wing(ph, True)
            ss.poly(pts, fill=(*col, int(a * 0.28)))
    # cauda
    ss.poly(P([(-0.45, 0.05), (-1.05, 0.28), (-1.08, 0.12), (-1.0, 0.0), (-0.5, -0.06)]), fill=(*bodyd, a), ink=(*INK, a), w=iw)
    # corpo
    ss.poly(P(A.spline([(0.45, -0.12), (0.25, 0.18), (-0.15, 0.22), (-0.55, 0.08), (-0.45, -0.12), (-0.05, -0.2), (0.3, -0.22)], n=8)),
            fill=(*body, a), ink=(*INK, a), w=iw)
    ss.poly(P(A.spline([(0.3, 0.05), (0.15, 0.2), (-0.2, 0.2), (-0.35, 0.08), (0.0, 0.04)], n=6)), fill=(*belly, a))
    # garganta rubi
    ss.poly(P(A.spline([(0.5, -0.02), (0.42, 0.14), (0.25, 0.14), (0.3, -0.02)], n=5)), fill=(*RUBY, a))
    # cabeça
    hx, hy = P([(0.52, -0.2)])[0]
    ss.circle(hx, hy, s * 0.2, fill=(*body, a), ink=(*INK, a), w=iw)
    # bico longo
    ss.poly(P([(0.68, -0.24), (1.45, -0.17), (1.46, -0.15), (0.68, -0.14)]), fill=(*BEAK, a), ink=(*INK, a), w=max(1, iw * 0.6))
    # olho grande
    ex, ey = P([(0.58, -0.24)])[0]; er = s * 0.065 * eye
    if perched and eye < 0.3:
        ss.line([(ex - er * 2, ey), (ex + er * 2, ey)], (*INK, a), max(2, s * 0.02))
    else:
        ss.circle(ex, ey, er, fill=(20, 16, 22, a))
        ss.circle(ex + er * 0.3 * flip, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, int(240 * a / 255)))
    # pés
    if perched:
        for k in (-0.05, 0.08):
            ss.line(P([(k, 0.2), (k + 0.02, 0.3)]), (*INK, a), max(2, s * 0.02))
    # coração no peito (raio-X)
    if heart > 0 or xray:
        cx, cy = P([(0.2, 0.02)])[0]
        r = s * 0.08 * (1 + 0.35 * heart)
        heart_shape(ss, cx, cy, r, (*RED, a))
    # asa da frente
    if wings and not perched:
        pts, col = wing(f, False)
        ss.poly(pts, fill=(*body, int(a * 0.9)), ink=(*INK, int(a * 0.6)), w=max(1, iw * 0.7))
    elif perched:
        ss.poly(P(A.spline([(0.25, -0.12), (-0.2, 0.0), (-0.75, 0.12), (-0.3, -0.12)], n=5)), fill=(*bodyd, a), ink=(*INK, a), w=iw)


def heart_shape(ss, cx, cy, r, col, ink=INK, w=0):
    pts = []
    for k in range(40):
        u = k / 40 * 2 * math.pi
        hx = 16 * math.sin(u) ** 3
        hy = -(13 * math.cos(u) - 5 * math.cos(2 * u) - 2 * math.cos(3 * u) - math.cos(4 * u))
        pts.append((cx + hx * r / 16, cy + hy * r / 16))
    ss.poly(pts, fill=col, ink=ink if w else None, w=w)


def pulse(t, rate):
    """0..1 batida (pico curto) com 'rate' batidas por segundo"""
    ph = (t * rate) % 1
    return math.exp(-ph * 9)


# ======================================================================= jardim tropical
def garden():
    def mk():
        im = A.vgrad(W, H, [(0, SKY0), (0.55, SKY1), (1, (150, 210, 150))])
        ss = SS(W, H, s=2)
        rng = np.random.default_rng(5)
        # folhas grandes (fundo)
        for k in range(14):
            x = rng.uniform(-100, W + 100); y = rng.uniform(900, H + 100); s = rng.uniform(220, 420)
            a = rng.uniform(-60, 60)
            ss.poly(A.xf(A.spline([(0, 0), (0.35, -0.5), (0, -1.2), (-0.35, -0.5)], n=8), x, y, s, a, 1),
                    fill=LEAF_D if k % 2 else LEAF, ink=(20, 60, 36), w=4)
        for k in range(5):
            x = rng.uniform(0, W); y = rng.uniform(1500, H)
            ss.circle(x, y, rng.uniform(30, 60), fill=ORG)
        im.alpha_composite(ss.get())
        return im
    return cached("bf_garden", mk).copy()


FX, FY = 760, 1000   # boca da flor


def flower(ss, x, y, s, open_=1.0, col=MAG):
    """flor tubular (tipo trombeta) pendurada; boca em (x, y) virada para a esquerda"""
    stem = (40, 110, 50)
    ss.line([(x + 1.3 * s, y - 2.8 * s), (x + 1.35 * s, y - 1.2 * s), (x + 1.15 * s, y - 0.05 * s)], stem, max(5, s * 0.07))
    for sg in (-1, 1):  # folhinha no talo
        ss.poly(A.xf(A.spline([(0, 0), (0.3, -0.12), (0.7, 0), (0.3, 0.12)], n=6), x + 1.33 * s, y - 1.6 * s, s, 90 + sg * 60, 1),
                fill=LEAF, ink=INK, w=max(2, s * 0.03))
    m = 0.35 + 0.65 * open_
    light = A.mixc(col, (255, 230, 245), 0.35)
    # tubo
    ss.poly(A.spline([(x + 1.15 * s, y - 0.07 * s), (x + 0.6 * s, y - 0.1 * s), (x + 0.2 * s, y - 0.2 * s * m),
                      (x + 0.2 * s, y + 0.2 * s * m), (x + 0.6 * s, y + 0.1 * s), (x + 1.15 * s, y + 0.07 * s)], n=6, closed=True),
            fill=col, ink=INK, w=max(2, s * 0.035))
    ss.line([(x + 1.0 * s, y), (x + 0.3 * s, y)], A.mixc(col, (120, 20, 70), 0.4), max(2, s * 0.025))
    # cálice
    ss.poly([(x + 1.25 * s, y - 0.12 * s), (x + 1.05 * s, y - 0.09 * s), (x + 1.05 * s, y + 0.09 * s), (x + 1.25 * s, y + 0.12 * s)],
            fill=LEAF, ink=INK, w=max(2, s * 0.03))
    # pétalas abertas em volta da boca
    for k in range(5):
        a = -math.pi / 2 + (k + 0.5) * math.pi / 5 * 2 - math.pi / 5
        py = y + 0.32 * s * m * math.sin(a); px = x + 0.12 * s + 0.08 * s * math.cos(a)
        ss.circle(px - 0.04 * s, py, 0.15 * s * m + 2, fill=light, ink=INK, w=max(2, s * 0.03))
    ss.oval(x + 0.1 * s, y, 0.06 * s, 0.16 * s * m, 0, fill=(120, 20, 70))
    ss.circle(x + 0.1 * s, y, 0.05 * s * m, fill=(255, 220, 90))


def ecg(ss, x0, x1, y, amp, t, rate, col, w=8, speed=900):
    """eletrocardiograma correndo para a esquerda"""
    pts = []
    n = 160
    for i in range(n + 1):
        x = lerp(x0, x1, i / n)
        tt = t - (x1 - x) / speed
        ph = (tt * rate) % 1
        v = 0.0
        if ph < 0.06: v = -math.sin(ph / 0.06 * math.pi) * 1.0
        elif ph < 0.1: v = math.sin((ph - 0.06) / 0.04 * math.pi) * 0.35
        pts.append((x, y + v * amp))
    ss.line(pts, col, w)


# ======================================================================= cena 1: gancho
def hook_frame(t, dark=0.0):
    img = garden()
    glow_at(img, 820, 300, 700, (255, 250, 210), 160)
    ss = SS(W, H, s=2)
    flower(ss, FX, FY, 240)
    bx = FX - 440 + 10 * math.sin(t * 2.3); by = FY + 10 + 14 * math.sin(t * 3.1)
    hummer(ss, bx, by, 300, rot=-6, t=t, eye=1.4, heart=pulse(t, 2.5))
    img.alpha_composite(ss.get())
    glow_at(img, bx + 60, by + 6, 120, (255, 60, 80), 160 * pulse(t, 2.5))
    # monitor: eletrocardiograma correndo
    ss = SS(W, H, s=2)
    ss.rrect(80, 1420, 1000, 1660, 30, fill=(10, 20, 26, 215), ink=INK, w=6)
    ecg(ss, 110, 970, 1560, 90, t, 6.0, (90, 255, 140), w=8, speed=1400)
    heart_shape(ss, 950, 1460, 18, RED)
    img.alpha_composite(ss.get())
    if dark > 0:
        img = ImageEnhance.Brightness(img).enhance(1 - 0.6 * dark)
    return A.vignette(img, 0.35)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.05 + 0.01 * math.sin(lt * 1.3), rot=0.5 * math.sin(lt * 0.8))


# ======================================================================= cena 2: o seu bate 70, o meu 17x
def human(ctx, lt):
    img = A.vgrad(W, H, [(0, (250, 236, 222)), (1, (236, 214, 200))])
    t7 = ctx.wt("70"); tr = ctx.wt("17")
    ss = SS(W, H, s=2)
    ss.line([(540, 520), (540, 1800)], (200, 180, 170), 6)
    # humano: coração grande e lento
    p1 = pulse(lt, 70 / 60)
    heart_shape(ss, 290, 860, 190 * (1 + 0.12 * p1), RED, w=8)
    ss.text((290, 1500), "70", 130, "anton", fill=INK)
    ss.text((290, 1610), "VOCÊ", 50, "anton", fill=(120, 90, 90))
    # beija-flor: coração pequeno e disparado
    q = ease((lt - t7 + 0.1) / 0.4)
    p2 = pulse(lt, 20)
    heart_shape(ss, 790, 860, 60 * (1 + 0.3 * p2), RED, w=5)
    hummer(ss, 790, 1060, 150, t=lt, eye=1.3)
    rq = ease((lt - tr + 0.2) / 0.4)
    n = int(lerp(70, 1200, rq))
    ss.text((790, 1500), f"{n:,}".replace(",", "."), 130, "anton", fill=RED)
    ss.text((790, 1610), "EU", 50, "anton", fill=(120, 90, 90))
    img.alpha_composite(ss.get())
    # ECGs
    ss = SS(W, H, s=2)
    ecg(ss, 80, 500, 1720, 50, lt, 70 / 60, (200, 60, 60), w=6, speed=300)
    ecg(ss, 580, 1000, 1720, 50, lt, 20 * max(0.06, rq), (200, 60, 60), w=6, speed=300)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * rq, dx=6 * rq * math.sin(lt * 40))


# ======================================================================= cena 3: Visão do Bicho (movimento)
def vision(ctx, lt):
    base = garden()
    ss = SS(W, H, s=2)
    flower(ss, 560, 820, 380)
    base.alpha_composite(ss.get())
    base = A.cam(base, zoom=1.15, dx=30 * math.sin(lt * 2.2), dy=20 * math.sin(lt * 3.0))
    q = ease(lt / 0.35)
    g = np.asarray(base.convert("L"), np.float32) / 255.0
    # mundo apagado em verde-azulado escuro; o movimento acende
    dim = Image.fromarray(np.clip(np.stack([10 + g * 50, 30 + g * 90, 40 + g * 90], 2), 0, 255).astype(np.uint8)).convert("RGBA")
    img = Image.blend(base, dim, 0.8 * q)
    ss = SS(W, H, s=2)
    # setas de fluxo em todas as direções (cada uma acende quando a cena balança)
    rng = np.random.default_rng(11)
    for k in range(70):
        x = rng.uniform(60, W - 60); y = rng.uniform(520, 1800)
        if 980 < y < 1260: continue
        ang = rng.uniform(0, 2 * math.pi) + 0.6 * math.sin(lt * 2 + k)
        L = 40 + 30 * math.sin(lt * 5 + k)
        c = A.mixc((120, 255, 230), (255, 255, 255), (k % 3) / 3)
        x1, y1 = x + L * math.cos(ang), y + L * math.sin(ang)
        A.arrow(ss, x, y, x1, y1, (*c, int(230 * q)), w=10, ink=None, iw=0)
    # mira na flor: ela fica parada
    ss.circle(560, 820, 140, ink=(255, 255, 120, int(255 * q)), w=8)
    ss.line([(560, 650), (560, 700)], (255, 255, 120, int(255 * q)), 8); ss.line([(560, 940), (560, 990)], (255, 255, 120, int(255 * q)), 8)
    ss.line([(390, 820), (440, 820)], (255, 255, 120, int(255 * q)), 8); ss.line([(680, 820), (730, 820)], (255, 255, 120, int(255 * q)), 8)
    # bico na borda (POV)
    ss.poly([(500, H + 20), (535, 1500), (548, 1500), (590, H + 20)], fill=BEAK, ink=INK, w=6)
    img.alpha_composite(ss.get())
    return img


# ======================================================================= cena 4: asas 80 por segundo
def wings(ctx, lt):
    img = garden()
    img = ImageEnhance.Brightness(img).enhance(0.75)
    t8 = ctx.wt("80")
    ss = SS(W, H, s=2)
    bx, by = 540, 900
    # o "8" que a ponta da asa desenha
    pts = [(bx + 40 + 260 * math.sin(u), by - 330 + 150 * math.sin(2 * u)) for u in np.linspace(0, 2 * math.pi, 80)]
    ss.line(pts, (255, 255, 255, 170), 8)
    hummer(ss, bx, by, 380, rot=-4, t=lt * 0.12, eye=1.4)
    img.alpha_composite(ss.get())
    # contador de batidas
    q = ease((lt - t8 + 0.3) / 0.4)
    ss = SS(W, H, s=2)
    ss.rrect(260, 1430, 820, 1640, 40, fill=(255, 255, 255, 230), ink=INK, w=6)
    n = int(80 * clamp01((lt - t8 + 0.5) / 1.2))
    ss.text((540, 1520), f"{n}", 120, "anton", fill=(20, 120, 80))
    ss.text((540, 1610), "POR SEGUNDO", 40, "anton", fill=INK)
    for k in range(6):  # tique-taque visual
        u = (lt * 4 + k / 6) % 1
        ss.circle(bx + 40 + 260 * math.sin(u * 2 * math.pi), by - 330 + 150 * math.sin(4 * math.pi * u), 14, fill=(255, 240, 120))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03 + 0.03 * q)


# ======================================================================= cena 5: raio-X — oxigênio
def xray_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (12, 20, 34)), (1, (24, 32, 56))])
        ss = SS(W, H, s=1)
        for k in range(0, W, 60): ss.line([(k, 0), (k, H)], (60, 80, 120, 60), 2)
        for k in range(0, H, 60): ss.line([(0, k), (W, k)], (60, 80, 120, 60), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("bf_xray", mk).copy()


def oxygen(ctx, lt):
    img = xray_bg()
    glow_at(img, 560, 960, 520, (120, 200, 255), 70)
    to = ctx.wt("oxigênio"); tq = ctx.wt("queima")
    bx, by, s = 600, 850, 420
    ss = SS(W, H, s=2)
    hummer(ss, bx, by, s, t=lt, eye=1.2, alpha=190, wings=True)
    P = lambda pts: A.xf(pts, bx, by, s, 0, 1)
    # músculo do peito (vermelho, queimando)
    hq = ease((lt - tq + 0.3) / 0.5)
    mx, my = P([(0.12, 0.06)])[0]
    ss.oval(mx, my, s * 0.22, s * 0.13, 0.2, fill=(*A.mixc((150, 60, 70), RED, hq), 230), ink=INK, w=5)
    # pulmões
    lx, ly = P([(-0.1, -0.08)])[0]
    ss.oval(lx, ly, s * 0.14, s * 0.07, 0, fill=(120, 200, 150, 200), ink=INK, w=4)
    # ar verde entrando pelo bico e indo pro músculo
    oq = ease((lt - to + 0.8) / 0.5)
    for k in range(14):
        u = (lt * 0.9 + k / 14) % 1
        if u < 0.5:
            x0, y0 = P([(1.4, -0.16)])[0]; x1, y1 = lx, ly
            v = u / 0.5
        else:
            x0, y0 = lx, ly; x1, y1 = mx, my
            v = (u - 0.5) / 0.5
        ss.circle(lerp(x0, x1, v), lerp(y0, y1, v) + 10 * math.sin(v * 8), 14, fill=(*GREEN, int(255 * (0.4 + 0.6 * oq))), ink=INK, w=2)
    # calor saindo do músculo
    for k in range(6):
        u = (lt * 1.2 + k / 6) % 1
        x = mx - 120 + k * 50
        pts = [(x + 14 * math.sin(v * 9 + lt * 7), my + 60 + v * 150 + u * 40) for v in np.linspace(0, 1, 10)]
        ss.line(pts, (*RED, int(200 * hq * math.sin(u * math.pi))), 8)
    img.alpha_composite(ss.get())
    glow_at(img, mx, my, 220, (255, 80, 60), 140 * hq)
    return A.cam(img, zoom=1.0 + 0.04 * oq)


# ======================================================================= cena 6: 20 por segundo
def pump(ctx, lt):
    img = xray_bg()
    t2 = ctx.wt("20"); ts = ctx.wt("segundo")
    p = pulse(lt, 20 / 3.0)   # a 30 fps, 20 por segundo não aparece: mostra em ritmo legível + cronômetro
    glow_at(img, 540, 880, 420, (255, 70, 70), 120 + 80 * p)
    ss = SS(W, H, s=2)
    # vasos
    for sg in (-1, 1):
        ss.line([(540 + sg * 60, 720), (540 + sg * 160, 560), (540 + sg * 300, 520)], (200, 40, 60), 40)
    heart_shape(ss, 540, 880, 260 * (1 + 0.18 * p), RED, w=10)
    # sangue correndo
    for k in range(10):
        u = (lt * 2.5 + k / 10) % 1
        for sg in (-1, 1):
            x = lerp(540 + sg * 60, 540 + sg * 300, u); y = lerp(720, 520, u ** 0.6)
            ss.circle(x, y, 12, fill=(255, 120, 120))
    # cronômetro de 1 s com 20 marcas acendendo
    cq = ease((lt - t2 + 0.4) / 0.4)
    cx, cy, r = 540, 1530, 170
    ss.circle(cx, cy, r + 20, fill=(240, 244, 250, int(240 * cq)), ink=(*INK, int(255 * cq)), w=8)
    lit = int(20 * clamp01((lt - t2 + 0.3) / max(0.6, ts - t2 + 0.4)))
    for k in range(20):
        a = -math.pi / 2 + k * 2 * math.pi / 20
        col = RED if k < lit else (190, 190, 200)
        ss.circle(cx + r * 0.82 * math.cos(a), cy + r * 0.82 * math.sin(a), 13, fill=(*col, int(255 * cq)))
    ss.text((cx, cy), "1 s", 70, "anton", fill=(*INK, int(255 * cq)))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * p)


# ======================================================================= cena 7: noite, motor desligado
def night_bg():
    def mk():
        im = A.vgrad(W, H, [(0, NAVY), (0.6, (26, 40, 80)), (1, (16, 30, 40))])
        ss = SS(W, H, s=2)
        rng = np.random.default_rng(3)
        for k in range(60):
            ss.circle(rng.uniform(0, W), rng.uniform(0, 1000), rng.uniform(1.5, 4), fill=(230, 240, 255, 200))
        ss.circle(820, 620, 70, fill=(230, 236, 250))
        for k in range(10):
            x = rng.uniform(-100, W + 100); y = rng.uniform(1300, H + 100); s = rng.uniform(220, 380)
            ss.poly(A.xf(A.spline([(0, 0), (0.35, -0.5), (0, -1.2), (-0.35, -0.5)], n=8), x, y, s, rng.uniform(-60, 60), 1),
                    fill=(18, 50, 44), ink=(8, 24, 22), w=4)
        im.alpha_composite(ss.get())
        return im
    return cached("bf_night", mk).copy()


def branch(ss):
    ss.line([(-40, 1120), (400, 1080), (760, 1110), (1120, 1060)], (70, 48, 36), 34)
    ss.line([(400, 1080), (330, 980)], (70, 48, 36), 14)


def night(ctx, lt):
    img = night_bg()
    tm = ctx.wt("motor")
    glow_at(img, 820, 620, 260, (200, 220, 255), 110)
    ss = SS(W, H, s=2)
    branch(ss)
    # o beija-flor pousa
    u = ease(lt / 1.2)
    bx = lerp(260, 520, u); by = lerp(820, 1010, u)
    per = u > 0.98
    hummer(ss, bx, by, 220, t=lt, eye=lerp(1.2, 0.2, ease((lt - tm + 0.2) / 0.6)) if per else 1.2, perched=per)
    # chave do motor
    q = ease((lt - tm + 0.3) / 0.4)
    ss.rrect(330, 1420, 750, 1620, 100, fill=(30, 36, 60), ink=INK, w=6)
    kx = lerp(650, 430, q)
    ss.circle(kx, 1520, 80, fill=A.mixc((90, 230, 140), (130, 130, 150), q), ink=INK, w=6)
    ss.text((kx, 1522), "ON" if q < 0.5 else "OFF", 46, "anton", fill=INK)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.03 + 0.02 * u)


# ======================================================================= cena 8: torpor — 1.200 -> 50
def torpor(ctx, lt):
    img = night_bg()
    img = ImageEnhance.Brightness(img).enhance(0.85)
    t5 = ctx.wt("50"); td = ctx.wt("despencar")
    u = ease((lt - td + 0.3) / max(0.6, t5 - td + 0.4))
    rate = lerp(6.0, 0.5, u)
    ss = SS(W, H, s=2)
    branch(ss)
    hummer(ss, 520, 1010, 220, t=lt, eye=0.1, perched=True, heart=pulse(lt, rate) * 0.6, xray=True)
    # monitor grande
    ss.rrect(80, 1360, 1000, 1760, 34, fill=(6, 16, 20, 230), ink=INK, w=6)
    ecg(ss, 110, 970, 1610, 110, lt, rate, (90, 255, 140), w=8, speed=700)
    n = int(lerp(1200, 50, u))
    ss.text((960, 1420), f"{n:,}".replace(",", ".") + " /min", 54, "anton", fill=(90, 255, 140), anchor="rm")
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * u)


# ======================================================================= cena 9: esfria até a temperatura do ar
def cold(ctx, lt):
    img = night_bg()
    te = ctx.wt("esfria"); ta = ctx.wt("ar")
    u = ease((lt - te + 0.2) / max(0.6, ta - te + 0.3))
    ss = SS(W, H, s=2)
    branch(ss)
    hummer(ss, 520, 1010, 220, t=lt, eye=0.1, perched=True, tint=A.mixc(EMER, (140, 190, 255), u) if u > 0 else None)
    # brilhinhos de frio
    rng = np.random.default_rng(7)
    for k in range(14):
        x = 520 + rng.uniform(-200, 200); y = 1000 + rng.uniform(-160, 60)
        ss.circle(x, y, 6 * u * (0.5 + 0.5 * math.sin(lt * 6 + k)), fill=(200, 230, 255))
    # termômetro
    ss.rrect(850, 420, 930, 1620, 40, fill=(240, 244, 250), ink=INK, w=6)
    ss.circle(890, 1660, 70, fill=A.mixc(RED, BLUE, u), ink=INK, w=6)
    ytop = lerp(560, 1400, u)
    ss.rrect(870, ytop, 910, 1660, 20, fill=A.mixc(RED, BLUE, u))
    ss.text((820, ytop), f"{int(lerp(40, 12, u))}°", 64, "anton", fill=(255, 255, 255), anchor="rm", stroke=6)
    img.alpha_composite(ss.get())
    glow_at(img, 520, 1000, 260, (120, 170, 255), 120 * u)
    return A.cam(img, zoom=1.04 + 0.03 * u)


# ======================================================================= cena 10: amanhece -> loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    u = easeio(clamp01(lt / max(0.6, ctx.dur * 0.55)))
    day = hook_frame(tr)
    if u < 1:
        nb = night_bg()
        ss = SS(W, H, s=2)
        branch(ss)
        hummer(ss, 520, 1010, 220, t=lt, eye=lerp(0.1, 1.2, u), perched=True)
        nb.alpha_composite(ss.get())
        day = Image.blend(nb, day, u)
    return A.cam(day, zoom=lerp(1.12, 1.05 + 0.01 * math.sin(tr * 1.3), u), rot=0.5 * math.sin(tr * 0.8) * u)


# ======================================================================= capa
def cover_bg(cv):
    img = garden()
    glow_at(img, 700, 500, 800, (255, 250, 210), 170)
    ss = SS(W, H, s=2)
    flower(ss, 900, 900, 260)
    img.alpha_composite(ss.get())
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 700) * 0.45
    ss = SS(int(2.8 * s), int(2.3 * s), s=2)
    hummer(ss, 1.2 * s, 1.5 * s, s, rot=-4, flap=0.9, eye=2.0, heart=0.6)
    return ss.get()
