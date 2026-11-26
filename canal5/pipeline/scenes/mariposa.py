"""Dia 7B — "E se você fosse uma mariposa na lâmpada?" (formato CURTO; paleta: varanda à noite, parede verde-oliva escura,
céu ameixa, lâmpada âmbar quente × LED branco-gelo, mariposa bege e caramelo, ultravioleta em violeta).

Cenas: hook (close: a mariposa girando em volta da lâmpada acesa, rastro em espiral), vision (Visão do Bicho: ultravioleta —
o mundo em violeta, as flores/lâmpada brilham, antenas na borda), hot (raio-X da lâmpada antiga: corrente amarela, fio
fininho ficando vermelho, termômetro até 2.500 °C), heat (barra: 90% calor × 10% luz), heat2 (ondas de calor vermelhas
saindo do vidro, a mariposa recua), led (raio-X do LED: chip, corrente amarela, luz saindo direto), cool (as duas lado a
lado: medidor de energia, -75%, LED azul = frio), confuse (a mariposa rodando com pontos de interrogação), back (lá fora:
costas viradas pro céu/lua; aqui: pra lâmpada → órbita), loop (volta ao quadro inicial).
Fatos: Fabian et al. (2024, Nature Communications); U.S. Department of Energy.
"""
import math
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import art as A
from art import W, H, SS, lerp, ease, easeio, clamp01, INK
from scenes.common import cached

WING = (206, 176, 132); WING_D = (150, 112, 74); WING_L = (232, 212, 172)
BODY = (168, 128, 86); FUZZ = (226, 204, 164)
AMBER = (255, 190, 90); WARM = (255, 230, 160)
ICE = (220, 240, 255)
UV = (190, 110, 255)
RED = (255, 70, 50); BLUE = (80, 160, 255); YEL = (255, 222, 40)
OLIVE = (52, 60, 40); OLIVE_D = (34, 40, 28); PLUM = (40, 22, 50)
CTX = {}


def setup(S, T, ctxs):
    for c in ctxs: CTX[c.sc["id"]] = c


# ======================================================================= mariposa (vista de cima/de frente, asas abertas)
def moth(ss, x, y, s, rot=0.0, flap=None, t=0.0, eye=1.0, alpha=255, uv=0.0):
    """origem = centro do tórax; s = envergadura/2. rot em graus (0 = cabeça para cima)."""
    P = lambda pts: A.xf(pts, x, y, s, rot, 1)
    iw = max(1.5, s * 0.012)
    f = (0.5 + 0.5 * math.sin(t * 34)) if flap is None else flap
    k = 1 - 0.45 * f
    for sg in (-1, 1):
        # asa de trás
        hw = [(sg * 0.05, 0.05), (sg * 0.62 * k, 0.22), (sg * 0.55 * k, 0.55), (sg * 0.22 * k, 0.62), (sg * 0.05, 0.3)]
        ss.poly(P(A.spline(hw, n=6)), fill=(*WING_L, alpha), ink=(*INK, alpha), w=iw)
        # asa da frente (triangular)
        fw = [(sg * 0.06, -0.12), (sg * 0.5 * k, -0.42), (sg * 1.0 * k, -0.34), (sg * 0.95 * k, -0.05), (sg * 0.55 * k, 0.18),
              (sg * 0.08, 0.12)]
        ss.poly(P(A.spline(fw, n=6)), fill=(*WING, alpha), ink=(*INK, alpha), w=iw)
        # desenhos da asa
        ss.line(P([(sg * 0.12, -0.05), (sg * 0.85 * k, -0.25)]), (*WING_D, alpha), max(1, s * 0.02))
        ss.line(P([(sg * 0.15, 0.06), (sg * 0.8 * k, -0.04)]), (*WING_D, alpha), max(1, s * 0.02))
        ex, ey = P([(sg * 0.55 * k, -0.12)])[0]
        ss.circle(ex, ey, s * 0.07 * (0.6 + 0.4 * k), fill=(*WING_D, alpha))
        if uv > 0:  # padrões que só aparecem no ultravioleta
            ss.circle(ex, ey, s * 0.16 * (0.6 + 0.4 * k), fill=(*UV, int(160 * uv * alpha / 255)))
            ss.poly(P([(sg * 0.6 * k, -0.38), (sg * 0.98 * k, -0.32), (sg * 0.93 * k, -0.1)]), fill=(255, 220, 255, int(170 * uv * alpha / 255)))
    # corpo peludo
    ss.oval(*P([(0, 0.18)])[0], s * 0.09, s * 0.3, math.radians(rot), fill=(*BODY, alpha), ink=(*INK, alpha), w=iw)
    for j in range(4):
        ss.line(P([(-0.08, 0.1 + j * 0.09), (0.08, 0.1 + j * 0.09)]), (*WING_D, alpha), max(1, s * 0.012))
    ss.circle(*P([(0, -0.1)])[0], s * 0.12, fill=(*FUZZ, alpha), ink=(*INK, alpha), w=iw)
    hx, hy = P([(0, -0.24)])[0]
    ss.circle(hx, hy, s * 0.09, fill=(*FUZZ, alpha), ink=(*INK, alpha), w=iw)
    # antenas plumosas
    for sg in (-1, 1):
        a0 = (sg * 0.03, -0.3); a1 = (sg * 0.2, -0.52); a2 = (sg * 0.32, -0.62)
        ss.line(P([a0, a1, a2]), (*WING_D, alpha), max(1.5, s * 0.016))
        for j in range(6):
            u = 0.2 + j * 0.14
            px, py = lerp(a0[0], a2[0], u), lerp(a0[1], a2[1], u)
            ss.line(P([(px, py), (px + sg * 0.06, py + 0.02)]), (*WING_D, alpha), max(1, s * 0.01))
            ss.line(P([(px, py), (px - sg * 0.02, py - 0.06)]), (*WING_D, alpha), max(1, s * 0.01))
    # olhos grandes
    for sg in (-1, 1):
        ex, ey = P([(sg * 0.075, -0.27)])[0]; er = s * 0.05 * eye
        ss.circle(ex, ey, er, fill=(30, 22, 20, alpha), ink=(*INK, alpha), w=max(1, iw * 0.6))
        ss.circle(ex - er * 0.3, ey - er * 0.35, er * 0.38, fill=(255, 255, 255, int(240 * alpha / 255)))


# ======================================================================= varanda à noite
def porch():
    def mk():
        im = A.vgrad(W, H, [(0, PLUM), (0.4, (60, 34, 66)), (1, (70, 44, 60))])
        ss = SS(W, H, s=2)
        # parede verde-oliva com tábuas
        ss.rect(0, 0, W, H, OLIVE)
        for k in range(0, W, 120):
            ss.line([(k, 0), (k, H)], OLIVE_D, 6)
        # janela com céu ameixa e lua
        ss.rrect(620, 1150, 1000, 1650, 14, fill=(46, 28, 64), ink=(30, 24, 20), w=12)
        ss.circle(880, 1260, 36, fill=(240, 230, 210))
        ss.line([(810, 1150), (810, 1650)], (30, 24, 20), 10); ss.line([(620, 1400), (1000, 1400)], (30, 24, 20), 10)
        im.alpha_composite(ss.get())
        return im
    return cached("porch", mk).copy()


def bulb(ss, x, y, s, on=1.0, kind="inc", hot=0.0):
    """lâmpada pendurada; (x, y) = centro do bulbo; s = raio"""
    ss.line([(x, -40), (x, y - 1.35 * s)], (30, 26, 24), max(3, s * 0.05))
    ss.rrect(x - 0.42 * s, y - 1.45 * s, x + 0.42 * s, y - 0.8 * s, 0.08 * s, fill=(170, 160, 150), ink=INK, w=5)
    for j in range(3):
        ss.line([(x - 0.42 * s, y - 1.3 * s + j * 0.17 * s), (x + 0.42 * s, y - 1.25 * s + j * 0.17 * s)], (120, 110, 100), 4)
    if kind == "inc":
        glass = (lerp(240, 255, on), lerp(230, 236, on), lerp(210, 170, on))
    else:
        glass = (lerp(225, 245, on), lerp(230, 250, on), lerp(235, 255, on))
    ss.poly(A.spline([(x - 0.4 * s, y - 0.82 * s), (x - 1.0 * s, y - 0.1 * s), (x - 0.75 * s, y + 0.75 * s), (x, y + 1.0 * s),
                      (x + 0.75 * s, y + 0.75 * s), (x + 1.0 * s, y - 0.1 * s), (x + 0.4 * s, y - 0.82 * s)], n=8),
            fill=(*[int(c) for c in glass], 235), ink=INK, w=5)
    if kind == "inc":
        # fio de tungstênio
        hcol = A.mixc((120, 90, 70), (255, 250, 220), on) if hot <= 0 else A.mixc((255, 120, 60), (255, 250, 220), on)
        ss.line([(x - 0.15 * s, y - 0.8 * s), (x - 0.25 * s, y + 0.1 * s)], (90, 80, 70), 4)
        ss.line([(x + 0.15 * s, y - 0.8 * s), (x + 0.25 * s, y + 0.1 * s)], (90, 80, 70), 4)
        pts = [(x - 0.25 * s + 0.5 * s * i / 24, y + 0.1 * s + 0.05 * s * math.sin(i * 1.6)) for i in range(25)]
        ss.line(pts, hcol, max(3, s * 0.035))
    else:
        ss.rrect(x - 0.3 * s, y - 0.2 * s, x + 0.3 * s, y + 0.1 * s, 0.05 * s, fill=(250, 250, 255), ink=(120, 140, 170), w=4)
        for j in range(4):
            ss.rect(x - 0.24 * s + j * 0.14 * s, y - 0.14 * s, x - 0.16 * s + j * 0.14 * s, y + 0.04 * s, (255, 236, 120))


def glow_at(img, x, y, r, col, a):
    A.paste_c(img, A.glow(int(r), col, int(a)), x, y)


# ======================================================================= cena 1: gancho
BX, BY, BR = 540, 860, 210
ORX, ORY = 400, 230


def orbit_pos(t):
    a = t * 3.4
    return BX + ORX * math.cos(a), BY + 60 + ORY * math.sin(a), a


def hook_frame(t, bright=1.0, extra=None, moth_a=255):
    img = porch()
    glow_at(img, BX, BY, 900, (255, 200, 110), 150 * bright)
    glow_at(img, BX, BY, 420, (255, 236, 180), 200 * bright)
    ss = SS(W, H, s=2)
    # poeirinha brilhando
    rng = np.random.default_rng(2)
    for k in range(30):
        u = (t * 0.07 + rng.uniform(0, 1)) % 1
        ss.circle(BX + rng.uniform(-450, 450), BY + 500 - u * 900, rng.uniform(2, 5), fill=(255, 240, 200, int(150 * math.sin(u * math.pi))))
    img.alpha_composite(ss.get())
    mx, my, a = orbit_pos(t)
    front = math.sin(a) > 0
    # rastro da órbita
    ss = SS(W, H, s=2)
    for k in range(26):
        tt = t - k * 0.025
        px, py, _ = orbit_pos(tt)
        ss.circle(px, py, 18 - k * 0.5, fill=(255, 250, 230, int(130 * (1 - k / 26))))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    sc = 200 + 60 * math.sin(a)
    rot = math.degrees(a) + 180
    if not front:
        moth(ss, mx, my, sc, rot=rot, t=t, eye=1.3, alpha=moth_a)
    bulb(ss, BX, BY, BR, on=bright)
    if front:
        moth(ss, mx, my, sc, rot=rot, t=t, eye=1.3, alpha=moth_a)
    if extra: extra(ss)
    img.alpha_composite(ss.get())
    glow_at(img, BX, BY + 20, 260, (255, 250, 220), 120 * bright)
    return A.vignette(img, 0.4)


def hook(ctx, lt):
    return A.cam(hook_frame(lt), zoom=1.04 + 0.01 * math.sin(lt * 1.1), rot=0.6 * math.sin(lt * 0.9))


# ======================================================================= cena 2: Visão do Bicho (ultravioleta)
def vision(ctx, lt):
    base = hook_frame(lt + CTX["hook"].dur)
    g = np.asarray(base.convert("L"), np.float32) / 255.0
    q = ease(lt / 0.35)
    # mundo em violeta: escuro onde não há UV, lâmpada e padrões das asas acesos
    r = 30 + g * 150; gg = 10 + g * 60; b = 60 + g * 195
    uvimg = Image.fromarray(np.clip(np.stack([r, gg, b], 2), 0, 255).astype(np.uint8)).convert("RGBA")
    img = Image.blend(base, uvimg, q)
    glow_at(img, BX, BY, 700, UV, 170 * q)
    ss = SS(W, H, s=2)
    # flores do jardim (lá fora, na janela) com "alvo" UV
    for fx, fy in ((700, 1560), (860, 1600), (940, 1520)):
        for k in range(6):
            a = k * math.pi / 3 + lt
            ss.circle(fx + 28 * math.cos(a), fy + 28 * math.sin(a), 20, fill=(230, 200, 255, int(220 * q)))
        ss.circle(fx, fy, 18, fill=(60, 0, 90, int(255 * q)))
    # mariposa vizinha com as asas acesas no UV
    moth(ss, 300, 1500, 160, rot=-20, t=lt, uv=q)
    # antenas na borda (POV)
    for sg in (-1, 1):
        sw = 20 * math.sin(lt * 2 + sg)
        a0 = (540 + sg * 60, H + 40); a1 = (540 + sg * 260 + sw, 1500); a2 = (540 + sg * 420 + sw, 1300)
        ss.line([a0, a1, a2], (*WING_D, 255), 14)
        for j in range(10):
            u = 0.15 + j * 0.08
            px, py = lerp(a0[0], a2[0], u), lerp(a0[1], a2[1], u)
            ss.line([(px, py), (px + sg * 50, py + 30)], WING_D, 6)
            ss.line([(px, py), (px - sg * 20, py - 50)], WING_D, 6)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.06, dx=10 * math.sin(lt * 2))


# ======================================================================= cena 3: raio-X da lâmpada antiga
def xray_bg():
    def mk():
        im = A.vgrad(W, H, [(0, (14, 18, 34)), (1, (30, 30, 56))])
        ss = SS(W, H, s=1)
        for k in range(0, W, 60): ss.line([(k, 0), (k, H)], (60, 70, 120, 60), 2)
        for k in range(0, H, 60): ss.line([(0, k), (W, k)], (60, 70, 120, 60), 2)
        im.alpha_composite(ss.get())
        return im
    return cached("xray", mk).copy()


def hot(ctx, lt):
    img = xray_bg()
    tf = ctx.wt("fio"); tg = ctx.wt("graus")
    heat = ease((lt - tf + 0.2) / max(0.6, tg - tf + 0.2))
    glow_at(img, 540, 780, 600 * (0.4 + 0.6 * heat), (255, 120, 60), 170 * heat)
    ss = SS(W, H, s=2)
    bulb(ss, 540, 760, 300, on=heat, kind="inc", hot=heat)
    # corrente (amarelo) subindo pelos fios
    for sg in (-1, 1):
        for k in range(4):
            u = (lt * 1.4 + k / 4) % 1
            px = 540 + sg * lerp(0.15, 0.25, u) * 300; py = lerp(760 - 0.8 * 300, 760 + 0.1 * 300, u)
            ss.circle(px, py, 14, fill=YEL, ink=INK, w=3)
    # termômetro
    ss.rrect(860, 520, 940, 1360, 40, fill=(240, 240, 250), ink=INK, w=6)
    ss.circle(900, 1400, 70, fill=RED, ink=INK, w=6)
    ss.rrect(880, lerp(1340, 560, heat), 920, 1400, 20, fill=RED)
    ss.text((780, lerp(1340, 560, heat)), f"{int(lerp(25, 2500, heat)):,}°".replace(",", "."), 60, "anton", fill=(255, 255, 255), anchor="rm", stroke=6)
    img.alpha_composite(ss.get())
    # mariposa pequena ao lado, para escala
    ss = SS(W, H, s=2)
    moth(ss, 180, 1500, 90, rot=10, t=lt, eye=1.2)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.05 * heat, dx=3 * heat * math.sin(lt * 37))


# ======================================================================= cena 4: 90% vira calor
def heat(ctx, lt):
    img = xray_bg()
    tc = ctx.wt("calor"); tb = ctx.wt("brilha")
    ss = SS(W, H, s=2)
    glow_at(img, 540, 1440, 520, (255, 140, 60), 160)
    bulb(ss, 540, 1450, 220, on=1.0, kind="inc", hot=1.0)
    # setas: um pouco de luz (amarelo) e muito calor (vermelho)
    q1 = ease((lt - tb + 0.1) / 0.4); q2 = ease((lt - tc + 0.8) / 0.5)
    for k in range(2):
        a = -math.pi / 2 + (k - 0.5) * 0.9
        A.arrow(ss, 540 + 280 * math.cos(a), 1450 + 280 * math.sin(a), 540 + (280 + 140 * q1) * math.cos(a),
                1450 + (280 + 140 * q1) * math.sin(a), YEL, w=22)
    for k in range(8):
        a = math.pi * 0.1 + k * math.pi * 0.8 / 7 + (0 if k < 4 else math.pi)
        a = -math.pi / 2 + (k - 3.5) * 0.42 + math.pi
        r0 = 280; r1 = 280 + 220 * q2
        if q2 > 0.02:
            pts = [(540 + lerp(r0, r1, u) * math.cos(a) + 16 * math.sin(u * 12 + lt * 8) * math.sin(a),
                    1450 + lerp(r0, r1, u) * math.sin(a) - 16 * math.sin(u * 12 + lt * 8) * math.cos(a)) for u in np.linspace(0, 1, 14)]
            ss.line(pts, (*RED, 230), 14)
    # barra 90 / 10
    bq = ease((lt - tc + 0.6) / 0.4)
    if bq > 0:
        ss.rrect(90, 520, 990, 700, 30, fill=(10, 10, 20, int(225 * bq)), ink=(*INK, int(255 * bq)), w=6)
        x0, x1 = 130, 950
        xm = lerp(x0, x1, 0.9 * bq)
        ss.rrect(x0, 560, xm, 660, 20, fill=RED)
        ss.rrect(xm, 560, x1, 660, 20, fill=YEL)
        ss.text(((x0 + xm) / 2, 610), "90% CALOR", 50, "anton", fill=(255, 255, 255), stroke=5)
        ss.text(((xm + x1) / 2, 610), "luz", 30, "mont-ExtraBold", fill=INK)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.03 * q2)


# ======================================================================= cena 5: quente demais pra encostar
def heat2(ctx, lt):
    img = porch()
    glow_at(img, 540, 900, 800, (255, 170, 90), 150)
    ss = SS(W, H, s=2)
    bulb(ss, 540, 900, 240, on=1.0)
    for k in range(6):  # ondas de calor (vermelho) subindo
        u = (lt * 0.7 + k / 6) % 1
        x = 340 + k * 80
        pts = [(x + 20 * math.sin(v * 9 + lt * 6), 1160 - v * 400 - u * 200) for v in np.linspace(0, 1, 14)]
        ss.line(pts, (*RED, int(200 * math.sin(u * math.pi))), 10)
    img.alpha_composite(ss.get())
    # a mariposa chega perto e recua
    u = (lt % 1.6) / 1.6
    d = 240 + 280 + 120 * (1 - math.sin(u * math.pi))
    ss = SS(W, H, s=2)
    mx, my = 540 + d * 0.75, 900 + d * 0.4
    moth(ss, mx, my, 150, rot=-120 + 10 * math.sin(lt * 5), t=lt, eye=1.3)
    te = ctx.wt("encostar")
    q = ease((lt - te + 0.2) / 0.3)
    if q > 0:
        ss.circle(860, 1420, 90 * q, fill=(255, 255, 255), ink=RED, w=14)
        ss.text((860, 1425), "!", 120 * q + 1, "anton", fill=RED)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.08 - 0.03 * easeio(lt / max(1, ctx.dur)), dx=-30)


# ======================================================================= cena 6: raio-X do LED
def led(ctx, lt):
    img = xray_bg()
    tc = ctx.wt("chip"); tl = ctx.wt("luz"); td = ctx.wt("direto")
    q = ease((lt - tl + 0.3) / 0.4)
    glow_at(img, 540, 1390, 600, (200, 230, 255), 150 * q)
    ss = SS(W, H, s=2)
    # chip grande em corte
    cq = ease((lt - tc + 0.4) / 0.4)
    ss.rrect(240, 1370, 840, 1590, 30, fill=(70, 80, 110), ink=INK, w=6)
    ss.rrect(300, 1410, 780, 1480, 14, fill=(120, 140, 200), ink=INK, w=4)   # camada n
    ss.rrect(300, 1480, 780, 1550, 14, fill=(200, 120, 160), ink=INK, w=4)   # camada p
    ss.text((540, 1630), "CHIP DE LED", 46, "anton", fill=(255, 255, 255), stroke=5)
    # corrente amarela entrando pelos dois lados e encontrando no meio
    for k in range(6):
        u = (lt * 1.2 + k / 6) % 1
        ss.circle(lerp(160, 520, u), 1480, 13 * cq + 1, fill=YEL, ink=INK, w=2)
        ss.circle(lerp(920, 560, u), 1480, 13 * cq + 1, fill=YEL, ink=INK, w=2)
    ss.line([(60, 1480), (240, 1480)], (160, 160, 170), 16); ss.line([(840, 1480), (1020, 1480)], (160, 160, 170), 16)
    # luz saindo direto (fótons brancos)
    for k in range(10):
        u = (lt * 1.5 + k / 10) % 1
        a = -math.pi / 2 + (k - 4.5) * 0.17
        r = 80 + u * 700
        ss.circle(540 + r * math.cos(a), 1430 + r * math.sin(a), 16 * q + 1, fill=(*ICE, int(255 * q * (1 - u * 0.7))))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    moth(ss, 860, 760, 110, rot=-25, t=lt, eye=1.2)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.0 + 0.04 * ease((lt - td + 0.3) / 0.4))


# ======================================================================= cena 7: gasta 75% menos e quase não esquenta
def cool(ctx, lt):
    img = porch()
    img = ImageEnhance.Brightness(img).enhance(0.7)
    t7 = ctx.wt("75"); te = ctx.wt("esquenta")
    glow_at(img, 290, 800, 380, (255, 160, 70), 160)
    glow_at(img, 790, 800, 380, (200, 230, 255), 150)
    ss = SS(W, H, s=2)
    bulb(ss, 290, 800, 150, on=1.0, kind="inc", hot=1.0)
    bulb(ss, 790, 800, 150, on=1.0, kind="led")
    # medidores de energia
    q = ease((lt - t7 + 0.4) / 0.5)
    for x, frac, col in ((290, 1.0, RED), (790, lerp(1.0, 0.25, q), BLUE)):
        ss.rrect(x - 70, 1300, x + 70, 1660, 20, fill=(20, 20, 30), ink=INK, w=5)
        ss.rrect(x - 50, lerp(1640, 1320, frac), x + 50, 1640, 14, fill=col)
    ss.text((290, 1720), "ANTIGA", 44, "anton", fill=(255, 255, 255), stroke=5)
    ss.text((790, 1720), "LED", 44, "anton", fill=(255, 255, 255), stroke=5)
    # termômetros: vermelho × azul
    hq = ease((lt - te + 0.4) / 0.4)
    if hq > 0:
        for x, col, txt in ((290, RED, "QUENTE"), (790, BLUE, "MORNA")):
            ss.rrect(x - 130, 520, x + 130, 620, 30, fill=(255, 255, 255, int(235 * hq)), ink=(*INK, int(255 * hq)), w=5)
            ss.text((x, 570), txt, 46, "anton", fill=(*col, int(255 * hq)))
    img.alpha_composite(ss.get())
    ss = SS(W, H, s=2)
    moth(ss, 540, 1500 + 20 * math.sin(lt * 3), 100, rot=0, t=lt, eye=1.3)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.02 + 0.02 * math.sin(lt * 0.8))


# ======================================================================= cena 8: eu me confundo
def confuse(ctx, lt):
    def extra(ss):
        tq = ctx.wt("confundo")
        q = ease((lt - tq + 0.4) / 0.4)
        mx, my, a = orbit_pos(lt * 1.6 + CTX["hook"].dur)
        for k in range(3):
            ang = lt * 2 + k * 2.1
            ss.text((mx + 130 * math.cos(ang), my - 120 + 50 * math.sin(ang)), "?", 90, "anton",
                    fill=(255, 240, 120, int(255 * q)), stroke=6)

    img = hook_frame(lt * 1.6 + CTX["hook"].dur, extra=extra)
    return A.cam(img, zoom=1.12, rot=4 * math.sin(lt * 2.5))


# ======================================================================= cena 9: costas para o claro
def back(ctx, lt):
    img = A.vgrad(W, H, [(0, (30, 20, 60)), (0.6, (60, 40, 90)), (1, (24, 30, 30))])
    tc = ctx.wt("costas"); tcl = ctx.wt("claro")
    ss = SS(W, H, s=2)
    # céu com lua (lá fora): a mariposa voa reta, costas para cima
    ss.rrect(60, 470, 1020, 1120, 40, fill=(54, 40, 100), ink=INK, w=6)
    ss.circle(820, 600, 60, fill=(250, 240, 210))
    for k in range(20):
        rng = np.random.default_rng(k)
        ss.circle(rng.uniform(90, 990), rng.uniform(500, 800), 3, fill=(255, 255, 240, 200))
    ss.rect(60, 1000, 1020, 1120, (30, 46, 30))
    ss.text((160, 530), "LÁ FORA", 40, "anton", fill=(255, 255, 255), anchor="lm", stroke=5)
    mx = lerp(150, 930, (lt * 0.35) % 1)
    q = ease((lt - tc + 0.3) / 0.4)
    # mariposa de lado: costas (seta) para cima
    moth(ss, mx, 880, 90, rot=90, t=lt, eye=1.1)
    if q > 0:
        A.arrow(ss, mx, 830, mx, 700, (255, 240, 120, int(255 * q)), w=20)
    # aqui: lâmpada do lado -> órbita
    ss.rrect(60, 1180, 1020, 1840, 40, fill=(40, 46, 32), ink=INK, w=6)
    ss.text((160, 1240), "AQUI", 40, "anton", fill=(255, 255, 255), anchor="lm", stroke=5)
    img.alpha_composite(ss.get())
    glow_at(img, 540, 1520, 300, (255, 200, 110), 200)
    ss = SS(W, H, s=2)
    ss.circle(540, 1520, 60, fill=WARM, ink=INK, w=5)
    lq = ease((lt - tcl + 0.4) / 0.4)
    a = lt * 3.0
    ox, oy = 540 + 220 * math.cos(a), 1520 + 160 * math.sin(a)
    for k in range(20):
        aa = a - k * 0.08
        ss.circle(540 + 220 * math.cos(aa), 1520 + 160 * math.sin(aa), 10 - k * 0.4, fill=(255, 250, 220, int(160 * (1 - k / 20))))
    moth(ss, ox, oy, 80, rot=math.degrees(a) + 180, t=lt, eye=1.1)
    if lq > 0:
        A.arrow(ss, ox, oy, lerp(ox, 540, 0.55), lerp(oy, 1520, 0.55), (255, 240, 120, int(255 * lq)), w=16)
    img.alpha_composite(ss.get())
    return A.cam(img, zoom=1.01 + 0.02 * math.sin(lt * 0.7))


# ======================================================================= cena 10: loop
def loop(ctx, lt):
    tr = lt - ctx.dur + 1 / 30.0
    u = easeio(clamp01(lt / max(0.6, ctx.dur * 0.6)))
    img = hook_frame(tr)
    return A.cam(img, zoom=lerp(1.14, 1.04 + 0.01 * math.sin(tr * 1.1), u), rot=0.6 * math.sin(tr * 0.9) * u)


# ======================================================================= capa
def cover_bg(cv):
    img = porch()
    glow_at(img, 540, 760, 900, (255, 200, 110), 170)
    ss = SS(W, H, s=2)
    bulb(ss, 540, 760, 170, on=1.0)
    for k in range(3):
        ss.circle(540, 820, 260 + k * 120, ink=(255, 250, 220, 120 - k * 30), w=8)
    img.alpha_composite(ss.get())
    glow_at(img, 540, 780, 300, (255, 250, 220), 140)
    return img


def cover_sprite(cv):
    s = cv.get("sprite_s", 600) * 0.5
    ss = SS(int(2.3 * s), int(1.9 * s), s=2)
    moth(ss, 1.15 * s, 1.05 * s, s, rot=0, flap=0.0, eye=2.0)
    return ss.get()
