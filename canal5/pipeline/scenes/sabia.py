"""Dia 6B — "E se você fosse um sabiá no fio de alta tensão?" (formato CURTO; paleta: céu verde-água de fim de tarde
com horizonte creme, morros verde-escuros, poste de concreto, sabiá oliva com barriga laranja-ferrugem; eletricidade
em amarelo, Visão do Bicho em violeta ultravioleta).

Cenas: hook (o sabiá pousa no fio, pulsos amarelos correndo pelo cabo), danger (placa de PERIGO ALTA TENSÃO tremendo),
vision (Visão do Bicho: ultravioleta — descargas violeta nos isoladores e no cabo, bico na borda), path (raio-X: o
choque precisa de um caminho entre 13.800 V e 0 V), feet (os dois pés no mesmo fio: 13.800 V e 13.800 V),
flow (a corrente passa por baixo dos pés, pelo fio), you (você, no chão, viraria o caminho até a terra: esquema),
hawk (asa aberta de gavião encostando em dois fios: faísca de curto), loop (o sabiá sai e pousa de novo: quadro inicial).
Fatos: Harvard Lecture Demonstrations; Physics Van (Illinois); Ödeen & Håstad (2013); Tyler et al. (2014).
"""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

OLIVE = (128, 112, 76); OLIVE_D = (86, 74, 50); OLIVE_L = (170, 154, 112)
RUST = (226, 120, 52); RUST_L = (246, 168, 96)
BEAK = (214, 176, 70); RING = (255, 206, 60)
ELE = (255, 222, 40)       # eletricidade (amarelo)
UV = (190, 110, 255)       # ultravioleta (violeta)
CABLE = (40, 40, 48)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= sabiá (perfil, cabeça para a direita)
def bird(ss, x, y, s, t=0.0, wing=0.0, eye=1.0, rot=0.0, flip=1, alpha=255, xray=0.0):
    """origem = ponto dos pés no fio. wing: 0 = asa fechada, 1 = asa aberta batendo."""
    P = lambda pts: A.xf(pts, x, y, s, rot, flip)
    iw = max(1.5, s * 0.008)
    ba = int(alpha * (1 - 0.65 * xray))
    # cauda
    ss.poly(P([(-0.3, -0.42), (-0.85, -0.3), (-0.88, -0.2), (-0.3, -0.3)]), fill=(*OLIVE_D, ba), ink=(*INK, alpha), w=iw)
    # pernas e dedos agarrando o fio
    for dx in (-0.05, 0.08):
        ss.line(P([(dx, -0.24), (dx + 0.02, 0.0)]), (*BEAK, alpha), max(2, s * 0.018))
        ss.line(P([(dx - 0.07, 0.0), (dx + 0.1, 0.0)]), (*BEAK, alpha), max(2, s * 0.016))
        ss.line(P([(dx + 0.1, 0.0), (dx + 0.12, 0.04)]), (*BEAK, alpha), max(2, s * 0.014))
    # corpo
    body = A.spline([(0.36, -0.62), (0.2, -0.66), (-0.1, -0.6), (-0.34, -0.42), (-0.3, -0.28), (-0.05, -0.2),
                     (0.22, -0.26), (0.36, -0.42)], 6)
    ss.poly(P(body), fill=(*OLIVE, ba), ink=(*INK, alpha), w=iw)
    belly = A.spline([(0.34, -0.5), (0.3, -0.36), (0.12, -0.24), (-0.1, -0.24), (-0.05, -0.36), (0.15, -0.46)], 6)
    ss.poly(P(belly), fill=(*RUST, ba))
    ss.poly(P(A.spline([(0.3, -0.44), (0.18, -0.32), (0.04, -0.3), (0.14, -0.4)], 4)), fill=(*RUST_L, int(ba * 0.8)))
    # asa
    if wing > 0.05:
        f = math.sin(t * 14) * wing
        tip = (-0.55 + 0.1 * f, -1.15 + 0.35 * (1 - f))
        wpts = [(0.12, -0.6), (-0.05, -0.95 + 0.2 * (1 - wing)), tip, (-0.45, -0.72), (-0.2, -0.56)]
        ss.poly(P(A.spline(wpts, 5)), fill=(*OLIVE_D, ba), ink=(*INK, alpha), w=iw)
        for k in range(3):
            ss.line(P([(-0.05 - 0.12 * k, -0.62), (lerp(-0.05, tip[0], 0.8) - 0.1 * k, lerp(-0.8, tip[1], 0.8) + 0.06 * k)]),
                    (*OLIVE_L, int(ba * 0.6)), max(1, s * 0.006))
    else:
        ss.poly(P(A.spline([(0.16, -0.58), (-0.1, -0.6), (-0.4, -0.4), (-0.15, -0.38), (0.1, -0.46)], 5)),
                fill=(*OLIVE_D, ba), ink=(*INK, alpha), w=iw)
        for k in range(3):
            ss.line(P([(-0.05 - 0.08 * k, -0.55 + 0.03 * k), (-0.3 - 0.04 * k, -0.42 + 0.01 * k)]), (*OLIVE_L, int(ba * 0.6)), max(1, s * 0.006))
    # cabeça
    hx, hy = P([(0.4, -0.72)])[0]
    ss.circle(hx, hy, s * 0.15, fill=(*OLIVE, ba), ink=(*INK, alpha), w=iw)
    ss.ellipse(*P([(0.46, -0.64)])[0], s * 0.06, s * 0.04, fill=(*OLIVE_L, int(ba * 0.6)))
    # bico
    ss.poly(P([(0.52, -0.76), (0.72, -0.7), (0.52, -0.67)]), fill=(*BEAK, alpha), ink=(*INK, alpha), w=iw)
    ss.line(P([(0.53, -0.715), (0.68, -0.703)]), (*INK, alpha), max(1, s * 0.005))
    # olho com anel amarelo
    ex, ey = P([(0.44, -0.76)])[0]; er = s * 0.035 * eye
    ss.circle(ex, ey, er * 1.35, fill=(*RING, alpha))
    ss.circle(ex, ey, er, fill=(20, 14, 12, alpha), ink=(*INK, alpha), w=max(1, iw * 0.5))
    ss.circle(ex - er * 0.3, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, int(240 * alpha / 255)))
    if xray > 0.01:
        ss.text(P([(0.0, -0.42)])[0], "0 V", max(20, s * 0.12), "anton", fill=(255, 255, 255, int(255 * xray)), stroke=max(2, s * 0.012))


# ======================================================================= cenário
WY = lambda x: 1600 + 0.00008 * (x - 540) ** 2 - 0.05 * (x - 540)      # fio principal (o do sabiá)
WY2 = lambda x: 880 + 0.00008 * (x - 540) ** 2 - 0.05 * (x - 540)      # fio de cima


def sky_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (120, 206, 200)), (0.55, (196, 232, 214)), (0.78, (252, 236, 200)), (1, (246, 214, 170))])
        ss = SS(W, H, s=1)
        rng = np.random.default_rng(8)
        for k in range(5):
            cx, cy = rng.uniform(0, W), rng.uniform(150, 700)
            for j in range(5):
                ss.ellipse(cx + j * 60 - 120, cy + rng.uniform(-20, 20), rng.uniform(80, 130), rng.uniform(40, 60), fill=(255, 255, 250, 150))
        # morros
        pts = [(0, 1500)] + [(x, 1380 - 90 * math.sin(x / 210.0) - 50 * math.sin(x / 90.0 + 1)) for x in range(0, W + 41, 40)] + [(W, 1500), (W, H), (0, H)]
        ss.poly(pts, fill=(64, 122, 92))
        pts = [(0, 1640)] + [(x, 1560 - 60 * math.sin(x / 160.0 + 2)) for x in range(0, W + 41, 40)] + [(W, H), (0, H)]
        ss.poly(pts, fill=(40, 92, 70))
        im.alpha_composite(ss.get().filter(ImageFilter.GaussianBlur(4)))
        return im
    return cached("sky", mk).copy()


def pole(ss, x, top, bot, s=1.0):
    ss.poly([(x - 34 * s, bot), (x - 22 * s, top), (x + 22 * s, top), (x + 34 * s, bot)], fill=(176, 176, 172), ink=INK, w=5)
    ss.rrect(x - 260 * s, top + 40 * s, x + 260 * s, top + 80 * s, 6, fill=(150, 150, 148), ink=INK, w=5)
    ins = []
    for dx in (-210, 0, 210):
        ix, iy = x + dx * s, top + 40 * s
        for k in range(3):
            ss.ellipse(ix, iy - 14 * s - k * 22 * s, 24 * s, 10 * s, fill=(130, 170, 150), ink=INK, w=3)
        ins.append((ix, iy - 70 * s))
    return ins


def wire(ss, f, col=CABLE, w=10, x0=-40, x1=W + 40):
    pts = [(x, f(x)) for x in range(x0, x1 + 1, 30)]
    ss.line(pts, col, w)
    return pts


def pulses(ss, f, t, speed=900.0, gap=170.0, a=255, w=8, ln=60, col=ELE, x0=-40, x1=W + 40):
    """pulsos amarelos correndo pelo fio (da esquerda para a direita)"""
    off = (t * speed) % gap
    x = x0 + off - gap
    while x < x1:
        xa, xb = x, x + ln
        if xb > x0:
            ss.line([(xa, f(xa)), ((xa + xb) / 2, f((xa + xb) / 2)), (xb, f(xb))], (*col, a), w)
        x += gap


# ======================================================================= cena 1: gancho (pousando)
BX = 540
START = (180, 1160)


def hook_frame(t, land=None, tw=None, wire_a=255, uv=0.0):
    img = sky_bg()
    ss = SS(W, H, s=2)
    ins = pole(ss, 900, 820, H + 20, 1.0)
    wire(ss, WY2, w=8)
    wire(ss, WY, w=12)
    pulses(ss, WY, t, a=wire_a)
    pulses(ss, WY2, t + 0.3, a=int(wire_a * 0.8), w=6)
    img.alpha_composite(ss.get())
    u = ease(t / 0.9) if land is None else land
    bx = lerp(START[0], BX, u); by = lerp(START[1], WY(BX), u) - 60 * math.sin(math.pi * u) * (1 - u)
    wg = 1.0 - ease(clamp01((u - 0.85) / 0.15))
    ss = SS(W, H, s=2)
    # balanço do fio depois do pouso
    bob = 10 * math.exp(-max(0, t - 0.9) * 4) * math.sin(t * 14) if land is None else 0.0
    bird(ss, bx, by + bob, 560, t=t if tw is None else tw, wing=wg, eye=1.2, rot=lerp(-12, 0, u) + 2 * math.sin(t * 1.4))
    sp = ss.get()
    sh, pad = A.shadow_of(sp, 18, 0.3)
    A.paste(img, sh, -pad + 10, -pad + 24)
    img.alpha_composite(sp)
    return A.vignette(img, 0.3)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.03 + 0.01 * math.sin(lt * 1.2), rot=0.4 * math.sin(lt * 0.7))


# ======================================================================= cena 2: perigo
def danger(ctx, lt):
    img = sky_bg()
    tf = ctx.wt("fatal")
    ss = SS(W, H, s=2)
    pole(ss, 540, 260, H + 20, 1.6)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    q = A.back(clamp01(lt / 0.35))
    cx, cy = 540, 760
    r = 300 * q + 1
    tri = [(cx, cy - r), (cx + r * 0.95, cy + r * 0.7), (cx - r * 0.95, cy + r * 0.7)]
    ss.poly(tri, fill=(255, 210, 30), ink=INK, w=14)
    bolt = [(0.08, -0.62), (-0.2, 0.05), (0.0, 0.05), (-0.1, 0.55), (0.24, -0.15), (0.03, -0.15), (0.16, -0.62)]
    ss.poly([(cx + px * r, cy + py * r) for px, py in bolt], fill=INK)
    ss.rrect(170, 1440, 910, 1600, 24, fill=(230, 40, 40), ink=INK, w=8)
    ss.text((540, 1520), "ALTA TENSÃO", 84, "anton", fill=(255, 255, 255))
    # faíscas
    rng = np.random.default_rng(int(lt * 12))
    for _ in range(8):
        a = rng.uniform(0, 2 * math.pi); r0 = rng.uniform(320, 420)
        p0 = (cx + r0 * math.cos(a), cy + r0 * math.sin(a))
        pts = [p0]
        for k in range(3):
            pts.append((pts[-1][0] + rng.uniform(-50, 50) + 40 * math.cos(a), pts[-1][1] + rng.uniform(-50, 50) + 40 * math.sin(a)))
        ss.line(pts, (*ELE, 220), 6)
    img.alpha_composite(ss.get())
    sh = 1.0 if lt > tf - 0.1 else 0.3
    return A.cam(img, zoom=1.02 + 0.03 * ease((lt - tf) / 0.3), dx=6 * sh * math.sin(lt * 47), dy=5 * sh * math.cos(lt * 39))


# ======================================================================= cena 3: Visão do Bicho (ultravioleta)
def _uv(img):
    arr = np.asarray(img.convert("RGB"), np.float32)
    g = arr.mean(axis=2, keepdims=True)
    b = arr[:, :, 2:3]
    out = np.concatenate([g * 0.55 + b * 0.25, g * 0.35, g * 0.75 + b * 0.45], axis=2)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).convert("RGBA")


def vision(ctx, lt):
    t = lt + CTX["hook"].dur + CTX["danger"].dur
    img = sky_bg()
    ss = SS(W, H, s=2)
    ins = pole(ss, 620, 700, H + 20, 1.5)
    wire(ss, lambda x: 640 + 0.00005 * (x - 600) ** 2, w=10)
    for dx in (-315, 315):
        wire(ss, lambda x, dx=dx: 640 + 0.00005 * (x - 600 - dx) ** 2, w=10)
    img.alpha_composite(ss.get())
    img = _uv(img)
    # descargas (corona) nos isoladores e ao longo do cabo
    tf = ctx.wt("faíscas")
    on = 0.35 + 0.65 * ease((lt - tf + 0.2) / 0.4)
    ss = SS(W, H, s=2)
    rng = np.random.default_rng(int(lt * 15))
    for (ix, iy) in ins:
        fl = rng.uniform(0.5, 1.0) * on
        A.paste_c(img, A.glow(150, (230, 180, 255), int(220 * fl)), ix, iy + 40)
        for _ in range(6):
            a = rng.uniform(0, 2 * math.pi); r = rng.uniform(40, 120)
            ss.line([(ix, iy + 40), (ix + r * math.cos(a), iy + 40 + r * math.sin(a))], (255, 235, 255, int(220 * fl)), 4)
    for _ in range(int(14 * on)):
        x = rng.uniform(0, W); y = 640 + 0.00005 * (x - 600) ** 2
        ss.circle(x, y, rng.uniform(6, 16), fill=(245, 220, 255, int(rng.uniform(120, 230))))
    img.alpha_composite(ss.get())
    # bico do sabiá na borda (POV)
    ss = SS(W, H, s=2)
    by = 1880 + 10 * math.sin(lt * 2)
    ss.poly([(380, H + 40), (560, by - 160), (740, H + 40)], fill=BEAK, ink=INK, w=8)
    ss.line([(560, by - 150), (560, H + 40)], INK, 5)
    for sg in (-1, 1):
        ss.circle(540 + sg * 820, 1700, 380, fill=(*OLIVE_D, 255), ink=INK, w=8)
    img.alpha_composite(ss.get())
    return A.cam(A.vignette(img, 0.5), zoom=1.02 + 0.02 * math.sin(lt * 1.5), rot=0.6 * math.sin(lt * 0.9))


# ======================================================================= cena 4: o choque precisa de um caminho
def xbg():
    def mk():
        im = A.vgrad(W, H, [(0, (24, 30, 46)), (1, (12, 14, 24))])
        ss = SS(W, H, s=1)
        for k in range(0, H, 60):
            ss.line([(0, k), (W, k)], (255, 222, 40, 18), 2)
        for k in range(0, W, 60):
            ss.line([(k, 0), (k, H)], (255, 222, 40, 18), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("xbg", mk).copy()


def bolt_path(ss, p0, p1, t, col=ELE, a=255, w=10, seed=0, n=9, amp=40):
    rng = np.random.default_rng(seed + int(t * 20))
    pts = [p0]
    for k in range(1, n):
        u = k / n
        pts.append((lerp(p0[0], p1[0], u) + rng.uniform(-amp, amp), lerp(p0[1], p1[1], u) + rng.uniform(-amp * 0.3, amp * 0.3)))
    pts.append(p1)
    ss.line(pts, (*col, int(a * 0.35)), w * 3)
    ss.line(pts, (*col, a), w)
    ss.line(pts, (255, 255, 255, a), max(2, w * 0.3))


def path(ctx, lt):
    img = xbg()
    tc = ctx.wt("caminho"); td = ctx.wt("diferentes")
    ss = SS(W, H, s=2)
    # dois pontos: alto (13.800 V) e baixo (0 V)
    ss.rrect(140, 470, 940, 590, 30, fill=(255, 222, 40), ink=INK, w=8)
    ss.text((540, 530), "13.800 V", 80, "anton", fill=INK)
    ss.rrect(140, 1560, 940, 1680, 30, fill=(120, 130, 150), ink=INK, w=8)
    ss.text((540, 1620), "0 V  (terra)", 70, "anton", fill=(255, 255, 255), stroke=6)
    q = ease((lt - tc + 0.1) / 0.5)
    if q > 0:
        y1 = lerp(600, 1550, q)
        bolt_path(ss, (540, 600), (540, y1), lt, seed=3)
    else:
        ss.text((540, 860), "?", 220, "anton", fill=(255, 255, 255, 200), stroke=10)
    qd = ease((lt - td + 0.2) / 0.4)
    if qd > 0:
        A.arrow(ss, 960, 640, 960, 1500, (255, 255, 255, int(255 * qd)), w=26)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * q, dx=4 * q * math.sin(lt * 50) * math.exp(-max(0, lt - tc) * 3))


# ======================================================================= cena 5: os dois pés no mesmo fio
def feet(ctx, lt):
    img = sky_bg().filter(ImageFilter.GaussianBlur(14))
    td = ctx.wt("dois"); tm = ctx.wt("mesma")
    ss = SS(W, H, s=2)
    f = lambda x: 1450 + 0.00003 * (x - 540) ** 2
    wire(ss, f, w=60)
    pulses(ss, f, lt, speed=1400, gap=260, w=22, ln=90)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    bird(ss, 560, 1420, 1500, t=lt, wing=0.0, eye=1.0)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    for k, (fx, tt) in enumerate(((440, td), (720, tm))):
        qa = A.back(clamp01((lt - tt + 0.2) / 0.35))
        if qa <= 0: continue
        ss.rrect(fx - 150 * qa, 1580, fx + 150 * qa, 1700, 26, fill=(255, 222, 40), ink=INK, w=6)
        if qa > 0.6:
            ss.text((fx, 1640), "13.800 V", 52, "anton", fill=INK)
        A.arrow(ss, fx, 1580, fx, 1500, (255, 255, 255, int(255 * clamp01(qa))), w=16)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * easeio(lt / max(1, ctx.dur)), dy=-10 * easeio(lt / max(1, ctx.dur)))


# ======================================================================= cena 6: a corrente segue pelo fio
def flow(ctx, lt):
    t = lt + 3.0
    img = sky_bg()
    ts = ctx.wt("segue")
    ss = SS(W, H, s=2)
    pole(ss, 900, 820, H + 20, 1.0)
    wire(ss, WY2, w=8)
    wire(ss, WY, w=14)
    hi = ease((lt - ts + 0.3) / 0.4)
    pulses(ss, WY, t, speed=lerp(900, 1500, hi), gap=150, w=lerp(8, 14, hi), ln=80)
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    bird(ss, BX, WY(BX), 560, t=t, wing=0.0, eye=1.2, xray=0.7, rot=2 * math.sin(t * 1.4))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    # setas ao longo do fio, passando por baixo dos pés
    for k in range(3):
        x = ((lt * 300 + k * 360) % (W + 200)) - 100
        A.arrow(ss, x, WY(x) + 70, x + 140, WY(x + 140) + 70, (*ELE, 230), w=26)
    ss.rrect(380, 700, 700, 830, 30, fill=(255, 255, 255, 230), ink=INK, w=6)
    ss.text((540, 765), "por mim: 0", 56, "anton", fill=INK)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.04 + 0.02 * math.sin(lt))


# ======================================================================= cena 7: você no chão (esquema)
def you(ctx, lt):
    img = xbg()
    tc = ctx.wt("chão"); tt = ctx.wt("terra")
    ss = SS(W, H, s=2)
    wy = 560
    ss.line([(-20, wy), (W + 20, wy)], (90, 90, 100), 16)
    pulses(ss, lambda x: wy, lt, gap=150, w=10)
    ss.rect(0, 1700, W, H, (70, 62, 52))
    ss.text((540, 1810), "TERRA  0 V", 60, "anton", fill=(220, 210, 190))
    # silhueta translúcida, braço para cima, mão perto do fio (esquema, sem encostar)
    px, top, base = 540, 760, 1700
    hh = base - top
    a = 150
    ss.circle(px, top + hh * 0.08, hh * 0.075, fill=(180, 200, 230, a), ink=(220, 230, 255), w=4)
    ss.rrect(px - hh * 0.1, top + hh * 0.17, px + hh * 0.1, top + hh * 0.56, 30, fill=(180, 200, 230, a), ink=(220, 230, 255), w=4)
    for sg in (-1, 1):
        ss.line([(px + sg * hh * 0.05, top + hh * 0.55), (px + sg * hh * 0.08, base)], (180, 200, 230, a + 60), 34)
    ss.line([(px + hh * 0.09, top + hh * 0.2), (px + hh * 0.16, wy + 70)], (180, 200, 230, a + 60), 30)
    ss.line([(px - hh * 0.09, top + hh * 0.2), (px - hh * 0.2, top + hh * 0.45)], (180, 200, 230, a + 60), 30)
    # caminho (tracejado) do fio até a terra
    q = ease((lt - 0.2) / max(0.6, tt - 0.2))
    route = [(px + hh * 0.16, wy + 20), (px + hh * 0.16, wy + 70), (px + hh * 0.09, top + hh * 0.2), (px, top + hh * 0.4),
             (px + hh * 0.05, top + hh * 0.55), (px + hh * 0.08, base), (px + hh * 0.08, base + 40)]
    L = [0.0]
    for i in range(1, len(route)):
        L.append(L[-1] + math.dist(route[i - 1], route[i]))
    upto = L[-1] * q
    for i in range(1, len(route)):
        if L[i - 1] >= upto: break
        p0 = route[i - 1]; u = min(1.0, (upto - L[i - 1]) / max(1e-6, L[i] - L[i - 1]))
        p1 = (lerp(p0[0], route[i][0], u), lerp(p0[1], route[i][1], u))
        bolt_path(ss, p0, p1, lt, seed=i, n=4, amp=12, w=8)
    if lt > tt - 0.2:
        ss.circle(px + hh * 0.08, base, 60 + 30 * math.sin(lt * 12), fill=(*ELE, 90))
        # aviso
        ss.circle(860, 1000, 110, fill=(230, 40, 40), ink=INK, w=8)
        ss.text((860, 1000), "!", 150, "anton", fill=(255, 255, 255))
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * q)


# ======================================================================= cena 8: gavião de asa aberta em dois fios
def hawk_shape(ss, x, y, s, flap=0.0, a=255, col=(120, 84, 56)):
    P = lambda pts: A.xf(pts, x, y, s, 0, 1)
    for sg in (-1, 1):
        wing = [(sg * 0.1, -0.05), (sg * 0.55, -0.22 - 0.1 * flap), (sg * 1.0, -0.15 - 0.15 * flap), (sg * 1.12, 0.0 - 0.1 * flap),
                (sg * 1.0, 0.08), (sg * 0.86, 0.06), (sg * 0.9, 0.16), (sg * 0.7, 0.12), (sg * 0.7, 0.22), (sg * 0.45, 0.16), (sg * 0.12, 0.14)]
        ss.poly(P(wing), fill=(*col, a), ink=(*INK, a), w=5)
    ss.poly(P([(-0.12, 0.1), (0.0, 0.6), (0.12, 0.1)]), fill=(*col, a), ink=(*INK, a), w=5)
    ss.oval(*P([(0, 0.05)])[0], s * 0.13, s * 0.28, 0, fill=(*col, a), ink=(*INK, a), w=5)
    ss.circle(*P([(0, -0.26)])[0], s * 0.11, fill=(240, 230, 210, a), ink=(*INK, a), w=5)
    ss.poly(P([(-0.04, -0.2), (0.0, -0.12), (0.04, -0.2)]), fill=(250, 200, 60, a), ink=(*INK, a), w=3)


def hawk(ctx, lt):
    img = sky_bg()
    tcu = ctx.wt("curto"); tg = ctx.wt("gavião")
    ss = SS(W, H, s=2)
    # dois fios paralelos (vista de frente)
    y1, y2 = 1300, 1600
    for yy in (y1, y2):
        ss.line([(-20, yy), (W + 20, yy)], CABLE, 12)
        pulses(ss, lambda x, yy=yy: yy, lt, gap=160, w=8)
    img.alpha_composite(ss.get())
    q = ease((lt - tg + 0.3) / max(0.8, tcu - tg))
    ss = SS(W, H, s=2)
    hy = lerp(700, 1450, q)
    hawk_shape(ss, 540, hy, 440, flap=math.sin(lt * 6) * (1 - q))
    img.alpha_composite(ss.get())
    sp = ease((lt - tcu + 0.05) / 0.15) * math.exp(-max(0, lt - tcu) * 1.5)
    if sp > 0.02:
        ss = SS(W, H, s=2)
        # o caminho: de um fio para o outro pelas pontas das asas
        for sg in (-1, 1):
            xw = 540 + sg * 440
            bolt_path(ss, (xw, y1), (xw, y2), lt, seed=7 + sg, n=6, amp=24, w=10, a=int(255 * sp))
            A.paste_c(img, A.glow(180, (255, 240, 160), int(240 * sp)), xw, (y1 + y2) / 2)
        ss.circle(540, 1450, 500, ink=(230, 40, 40, int(255 * sp)), w=14)
        img.alpha_composite(ss.get())
        img.alpha_composite(Image.new("RGBA", (W, H), (255, 250, 220, int(110 * sp))))
    return A.cam(img, zoom=1.02 + 0.03 * sp, dx=8 * sp * math.sin(lt * 60))


# ======================================================================= cena 9: loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    t_out = ctx.dur - 1.0
    if lt < t_out:
        # sentado, tranquilo, no fio só
        img = hook_frame(tr + 10.0, land=1.0, tw=lt)
        return A.cam(img, zoom=1.06 - 0.02 * easeio(lt / max(0.5, t_out)))
    u = easeio(clamp01((lt - t_out) / 1.0))
    img = hook_frame(tr, land=1.0 - u)
    return A.cam(img, zoom=lerp(1.04, 1.03 + 0.01 * math.sin(tr * 1.2), u), rot=0.4 * math.sin(tr * 0.7) * u)


# ======================================================================= capa
def cover_bg(cv):
    img = sky_bg()
    ss = SS(W, H, s=2)
    pole(ss, 900, 820, H + 20, 1.0)
    wire(ss, WY2, w=8)
    wire(ss, lambda x: WY(x) - 300, w=12)
    pulses(ss, lambda x: WY(x) - 300, 0.0, speed=0, w=10)
    img.alpha_composite(ss.get())
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 600)
    ss = SS(int(1.7 * s), int(1.25 * s), s=2)
    bird(ss, 0.75 * s, 1.0 * s, s, t=0.0, wing=0.0, eye=1.8)
    ss.line([(0.0, 1.0 * s), (1.7 * s, 1.0 * s)], CABLE, max(6, s * 0.02))
    return ss.get()
