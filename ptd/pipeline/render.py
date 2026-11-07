"""Pipeline Por Trás do Dinheiro: roteiro -> voz (Kokoro offline) -> visuais por código -> MP4 1080p + SRT.
Uso: python3 -I render.py ep01_script.py out/ep01
"""
import sys, os, re, math, subprocess, importlib.util, json
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1920, 1080, 30
FONT_DIR = "/usr/share/fonts/opentype/inter/"
def F(size, w="Bold"):
    return ImageFont.truetype(FONT_DIR + f"Inter-{w}.otf", size)

BG1, BG2 = (11, 18, 32), (20, 32, 54)
WHITE, DIM, GREEN, AMBER, RED, BLUE = (240, 244, 250), (120, 135, 160), (58, 196, 125), (242, 169, 59), (224, 108, 90), (91, 141, 239)
BRAND = "POR TRÁS DO DINHEIRO"

def hexc(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def lerp(a, b, t): return a + (b - a) * t
def mix(c1, c2, t): return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))

def make_bg():
    g = np.zeros((H, W, 3), np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - W * 0.7) / W) ** 2 + ((yy - H * 0.3) / H) ** 2)
    t = np.clip(1 - d * 1.3, 0, 1)[..., None]
    g[:] = np.array(BG1) * (1 - t) + np.array(BG2) * t
    img = Image.fromarray(g.astype(np.uint8))
    dr = ImageDraw.Draw(img)
    for x in range(0, W, 80):
        dr.line([(x, 0), (x, H)], fill=(255, 255, 255, 0), width=1)
    img = Image.blend(Image.fromarray(g.astype(np.uint8)), img, 0.04)
    return img
BG = None

def text_c(dr, xy, txt, font, fill, anchor="mm"):
    dr.text(xy, txt, font=font, fill=fill, anchor=anchor)

def alpha_text(base, xy, txt, font, fill, a, anchor="mm", dy=0):
    if a <= 0: return
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((xy[0], xy[1] + dy), txt, font=font, fill=fill + (int(255 * a),), anchor=anchor)
    base.alpha_composite(layer)

def chrome(img, prog):
    dr = ImageDraw.Draw(img)
    dr.rounded_rectangle([60, 48, 86, 74], 6, fill=GREEN)
    dr.text((73, 62), "$", font=F(22, "Black"), fill=BG1, anchor="mm")
    dr.text((100, 61), BRAND, font=F(22, "SemiBold"), fill=DIM, anchor="lm")
    dr.rectangle([0, H - 6, int(W * prog), H], fill=GREEN)

# ---------- cenas ----------
def sc_title(img, v, t, dur):
    a1, a2 = ease(t / 0.6), ease((t - 0.35) / 0.6)
    lines = v["title"].split("\n")
    size = 112 if max(len(l) for l in lines) < 22 else 92
    f = F(size, "ExtraBold"); lh = size * 1.15
    y0 = H / 2 - (len(lines) - 1) * lh / 2 - (40 if v.get("sub") else 0)
    if v.get("brand"):
        y0 += 40
        s = 120; cx, cy = W / 2, y0 - lh / 2 - 110
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
        d2.rounded_rectangle([cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2], 26, fill=GREEN + (int(255 * a1),))
        d2.text((cx, cy + 4), "$", font=F(96, "Black"), fill=BG1 + (int(255 * a1),), anchor="mm")
        img.alpha_composite(lay)
    for i, l in enumerate(lines):
        alpha_text(img, (W / 2, y0 + i * lh), l, f, WHITE, a1, dy=(1 - a1) * 40)
    if v.get("sub"):
        alpha_text(img, (W / 2, y0 + len(lines) * lh + 10), v["sub"], F(46, "SemiBold"), GREEN, a2, dy=(1 - a2) * 30)

def fmt_num(x, dec):
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s

def sc_bignumber(img, v, t, dur):
    p = ease((t - 0.3) / 1.6)
    val = lerp(v["from"], v["to"], p)
    dec = v.get("decimals", 0)
    txt = v.get("prefix", "") + fmt_num(val, dec) + v.get("suffix", "")
    col = mix(WHITE, AMBER if v["to"] < v["from"] or v.get("warn") else GREEN, p)
    a = ease(t / 0.4)
    fs = 260
    while F(fs, "Black").getlength(txt) > W - 160 and fs > 120: fs -= 10
    alpha_text(img, (W / 2, H / 2 - 40), txt, F(fs, "Black"), col, a)
    alpha_text(img, (W / 2, H / 2 + 150), v.get("caption", ""), F(42, "Medium"), DIM, ease((t - 0.6) / 0.6))
    if v.get("source"):
        alpha_text(img, (W / 2, H - 70), v["source"], F(28, "Medium"), DIM, ease((t - 0.9) / 0.6))

def node_box(dr, cx, cy, w, h, label, note, a, active=False):
    fill = mix(BG1, (34, 52, 84) if not active else (30, 92, 64), a)
    outline = mix(BG1, GREEN if active else BLUE, a)
    dr.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], 22, fill=fill, outline=outline, width=4)
    fs = 36
    while F(fs, "Bold").getlength(label) > w - 30 and fs > 20: fs -= 2
    dr.text((cx, cy), label, font=F(fs, "Bold"), fill=mix(BG1, WHITE, a), anchor="mm")
    if note: dr.text((cx, cy + h / 2 + 40), note, font=F(26, "Medium"), fill=mix(BG1, DIM, a), anchor="mm")

def sc_flow(img, v, t, dur):
    n = len(v["nodes"]); dr = ImageDraw.Draw(img)
    gap = W * 0.86 / n; x0 = W * 0.07 + gap / 2; cy = H / 2 - 20
    bw, bh = min(320, gap - 40), 150
    span = max(1.0, dur * 0.65) / n
    act = [ease((t - i * span) / 0.5) for i in range(n)]
    for i in range(n - 1):
        a = min(act[i], act[i + 1])
        if a > 0:
            xa, xb = x0 + i * gap + bw / 2 + 8, x0 + (i + 1) * gap - bw / 2 - 8
            dr.line([(xa, cy), (lerp(xa, xb, a), cy)], fill=DIM, width=5)
            if a > 0.95: dr.polygon([(xb, cy), (xb - 18, cy - 11), (xb - 18, cy + 11)], fill=DIM)
    for i, lab in enumerate(v["nodes"]):
        note = v.get("notes", [""] * n)[i]
        node_box(dr, x0 + i * gap, cy, bw, bh, lab, note, act[i])
    if v.get("pulse") and t > span * n:
        tt = ((t - span * n) / 2.2) % 1.0
        pos = tt * (n - 1); i = int(pos); f = pos - i
        px = lerp(x0 + i * gap, x0 + (i + 1) * gap, f)
        dr.ellipse([px - 16, cy - 16, px + 16, cy + 16], fill=GREEN)
    if v.get("caption"):
        alpha_text(img, (W / 2, H - 170), v["caption"], F(40, "SemiBold"), GREEN, ease((t - span * n) / 0.5))

def sc_split(img, v, t, dur):
    dr = ImageDraw.Draw(img); parts = v["parts"]
    x0, x1, y = 160, W - 160, 300
    a = ease(t / 0.8)
    tot = v["total"]; cx = x0
    for i, (lab, val, c) in enumerate(parts):
        w = (x1 - x0) * val / tot * a
        dr.rectangle([cx, y - 40, cx + w, y + 40], fill=hexc(c)); cx += w
    dr.text((x0, y - 80), v.get("left_label", "R$ 100 vendidos"), font=F(36, "SemiBold"), fill=DIM, anchor="lm")
    dr.text((x1, y - 80), v.get("right_label", "R$ 3 de taxa  →"), font=F(36, "SemiBold"), fill=AMBER, anchor="rm")
    fees = parts[1:]; mx = max(p[1] for p in fees)
    span = max(1.0, dur * 0.7) / len(fees)
    for i, (lab, val, c) in enumerate(fees):
        p = ease((t - 1.0 - i * span) / 0.7)
        yy = 520 + i * 150
        bw = 680 * val / mx * p
        dr.text((160, yy), lab, font=F(40, "SemiBold"), fill=mix(BG1, WHITE, p), anchor="lm")
        dr.rounded_rectangle([860, yy - 34, 860 + max(bw, 1), yy + 34], 12, fill=hexc(c))
        if p > 0.05: dr.text((860 + bw + 24, yy), "R$ " + fmt_num(val * p, 2), font=F(44, "Bold"), fill=WHITE, anchor="lm")
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_bullets(img, v, t, dur):
    dr = ImageDraw.Draw(img)
    alpha_text(img, (160, 210), v["title"], F(76, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    items = v["items"]; hl = v.get("highlight", -1)
    span = max(0.8, dur * 0.6) / len(items)
    for i, it in enumerate(items):
        if v.get("instant_until") is not None and i < v["instant_until"]:
            a = 1.0
        else:
            k = i - (v.get("instant_until") or 0)
            a = ease((t - 0.3 - k * span) / 0.5)
        col = GREEN if i == hl else (WHITE if hl < 0 else (170, 180, 200))
        y = 380 + i * 130
        if a > 0:
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            d2.rounded_rectangle([160, y - 8, 172, y + 52], 4, fill=col + (int(255 * a),))
            d2.text((200 + (1 - a) * 30, y + 22), it, font=F(52, "SemiBold"), fill=col + (int(255 * a),), anchor="lm")
            img.alpha_composite(lay)
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_bars(img, v, t, dur):
    dr = ImageDraw.Draw(img)
    alpha_text(img, (160, 200), v["title"], F(64, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    mx = max(i[1] for i in v["items"])
    lw = max(F(52, "Bold").getlength(v.get("prefix", "") + fmt_num(i[1], v.get("decimals", 2)) + v.get("suffix", "")) for i in v["items"])
    full = min(1000, W - 640 - 24 - lw - 70)
    for i, (lab, val, c) in enumerate(v["items"]):
        p = ease((t - 0.5 - i * 0.6) / 0.9); y = 400 + i * 170
        dr.text((160, y), lab, font=F(42, "SemiBold"), fill=mix(BG1, WHITE, p), anchor="lm")
        bw = full * val / mx * p
        dr.rounded_rectangle([640, y - 42, 640 + max(1, bw), y + 42], 14, fill=hexc(c))
        if p > 0.05: dr.text((640 + bw + 24, y), v.get("prefix", "") + fmt_num(val * p, v.get("decimals", 2)) + v.get("suffix", ""), font=F(52, "Bold"), fill=WHITE, anchor="lm")
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_compare(img, v, t, dur):
    dr = ImageDraw.Draw(img)
    for k, (col, side, x) in enumerate([(GREEN, v["left"], W * 0.27), (AMBER, v["right"], W * 0.73)]):
        a = ease((t - k * 0.8) / 0.6)
        if a <= 0: continue
        dr.rounded_rectangle([x - 380, 200, x + 380, 880], 30, fill=mix(BG1, (24, 38, 62), a), outline=mix(BG1, col, a), width=4)
        dr.text((x, 290), side[0], font=F(80 if len(side[0]) < 14 else 60, "ExtraBold"), fill=mix(BG1, col, a), anchor="mm")
        for i, s in enumerate(side[1:]):
            fs = 42
            while F(fs, "SemiBold").getlength(s) > 700 and fs > 26: fs -= 2
            dr.text((x, 450 + i * 120), s, font=F(fs, "SemiBold"), fill=mix(BG1, WHITE, a), anchor="mm")
    if v.get("caption"): dr.text((W / 2, H - 90), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_timeline(img, v, t, dur):
    dr = ImageDraw.Draw(img); pts = v["points"]; y = H / 2 - 40
    x0, x1 = 220, W - 220
    p = ease(t / (dur * 0.5)); dr.line([(x0, y), (lerp(x0, x1, p), y)], fill=DIM, width=6)
    pos = [x0, x0 + (x1 - x0) * 0.3, x1] if len(pts) == 3 and not v.get("even") else [lerp(x0, x1, i / (len(pts) - 1)) for i in range(len(pts))]
    for i, (lab, note) in enumerate(pts):
        a = ease((t - (pos[i] - x0) / (x1 - x0) * dur * 0.5) / 0.4)
        if a <= 0: continue
        c = GREEN if i == len(pts) - 1 else WHITE
        dr.ellipse([pos[i] - 18, y - 18, pos[i] + 18, y + 18], fill=mix(BG1, c, a))
        dr.text((pos[i], y - 70), lab, font=F(48, "Bold"), fill=mix(BG1, c, a), anchor="mm")
        dr.text((pos[i], y + 70), note, font=F(32, "Medium"), fill=mix(BG1, DIM, a), anchor="mm")
    if v.get("caption"): alpha_text(img, (W / 2, H - 200), v["caption"], F(48, "SemiBold"), AMBER, ease((t - dur * 0.6) / 0.6))

def sc_cards(img, v, t, dur):
    """Cartões lado a lado; highlight = índice em destaque, os outros ficam apagados."""
    dr = ImageDraw.Draw(img); cards = v["cards"]; n = len(cards); hl = v.get("highlight", -1)
    if v.get("title"): alpha_text(img, (W / 2, 190), v["title"], F(68, "ExtraBold"), WHITE, ease(t / 0.5))
    cw, ch, gap = (480, 520, 60) if n <= 3 else (380, 500, 40)
    x0 = W / 2 - (n * cw + (n - 1) * gap) / 2; y0 = 300
    for i, (num, name, note) in enumerate(cards):
        a = ease((t - 0.2 - i * 0.35) / 0.5)
        if a <= 0: continue
        on = hl < 0 or i == hl
        col = AMBER if (i == hl) else (BLUE if on else (60, 72, 96))
        x = x0 + i * (cw + gap)
        dr.rounded_rectangle([x, y0, x + cw, y0 + ch], 30, fill=mix(BG1, (24, 38, 62) if on else (16, 26, 44), a), outline=mix(BG1, col, a), width=5 if i == hl else 3)
        tc = WHITE if on else (90, 100, 125)
        dr.ellipse([x + cw / 2 - 70, y0 + 60, x + cw / 2 + 70, y0 + 200], fill=mix(BG1, col, a))
        dr.text((x + cw / 2, y0 + 132), num, font=F(80, "Black"), fill=mix(BG1, BG1, a), anchor="mm")
        fs = 56
        while F(fs, "ExtraBold").getlength(name) > cw - 40 and fs > 30: fs -= 2
        dr.text((x + cw / 2, y0 + 290), name, font=F(fs, "ExtraBold"), fill=mix(BG1, tc, a), anchor="mm")
        for j, ln in enumerate(note.split("\n")):
            dr.text((x + cw / 2, y0 + 380 + j * 50), ln, font=F(34, "Medium"), fill=mix(BG1, DIM if on else (70, 80, 100), a), anchor="mm")
    if v.get("caption"): alpha_text(img, (W / 2, H - 120), v["caption"], F(40, "SemiBold"), GREEN, ease((t - 1.5) / 0.6))

def sc_line(img, v, t, dur):
    """Curva que cresce ponto a ponto. points = [[rótulo_x, valor], ...]; cap = linha horizontal opcional (teto)."""
    dr = ImageDraw.Draw(img); pts = v["points"]; n = len(pts)
    alpha_text(img, (160, 170), v["title"], F(60, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    x0, x1, y0, y1 = 260, W - 300, 860, 290
    mx = v.get("max", max(p[1] for p in pts) * 1.05)
    def Y(val): return y0 - (y0 - y1) * val / mx
    dr.line([(x0, y0), (x1, y0)], fill=(60, 75, 100), width=3)
    for i, (lab, val) in enumerate(pts):
        x = lerp(x0, x1, i / (n - 1))
        dr.text((x, y0 + 40), lab, font=F(30, "Medium"), fill=DIM, anchor="mm")
    prog = ease((t - 0.4) / max(1.0, dur * 0.6)) * (n - 1)
    col = hexc(v.get("color", "#E06C5A"))
    xy = []
    for i in range(n):
        if i > prog + 1e-6: break
        xy.append((lerp(x0, x1, i / (n - 1)), Y(pts[i][1])))
    k = int(prog)
    if k < n - 1 and prog > k:
        f = prog - k
        xy.append((lerp(x0, x1, (k + f) / (n - 1)), Y(lerp(pts[k][1], pts[k + 1][1], f))))
    if len(xy) >= 2: dr.line(xy, fill=col, width=8, joint="curve")
    if xy:
        x, y = xy[-1]; dr.ellipse([x - 14, y - 14, x + 14, y + 14], fill=col)
        cur = lerp(pts[min(k, n - 1)][1], pts[min(k + 1, n - 1)][1], prog - k) if k < n - 1 else pts[-1][1]
        dr.text((x + 26, y - 30), v.get("prefix", "R$ ") + fmt_num(cur, v.get("decimals", 0)) + v.get("suffix", ""), font=F(48, "Black"), fill=WHITE, anchor="lm")
    if v.get("cap") is not None:
        a = ease((t - dur * 0.55) / 0.6)
        if a > 0:
            yc = Y(v["cap"])
            for xx in range(x0, x1, 40): dr.line([(xx, yc), (xx + 22, yc)], fill=mix(BG1, GREEN, a), width=5)
            dr.text((x0 + 10, yc - 34), v.get("cap_label", "teto"), font=F(34, "Bold"), fill=mix(BG1, GREEN, a), anchor="lm")
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_receipt(img, v, t, dur):
    """Criado no EP04: 'extrato' de um cliente. lines = [[rótulo, valor_txt, cor_hex]]; total = [rótulo, valor_txt]."""
    dr = ImageDraw.Draw(img)
    alpha_text(img, (160, 170), v["title"], F(60, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    px0, px1, py0 = 520, 1400, 260
    lines = v["lines"]; n = len(lines)
    py1 = py0 + 120 + n * 105 + (150 if v.get("total") else 40)
    a = ease((t - 0.1) / 0.5)
    dr.rounded_rectangle([px0, py0, px1, py1], 26, fill=mix(BG1, (236, 240, 246), a))
    for zx in range(px0 + 10, px1 - 10, 40):  # serrilhado do papel
        dr.polygon([(zx, py1), (zx + 20, py1 + 18), (zx + 40, py1)], fill=mix(BG1, (236, 240, 246), a))
    if a < 0.3: return
    ink, ink2 = (20, 30, 48), (95, 105, 125)
    dr.text(((px0 + px1) / 2, py0 + 60), v.get("head", "EXTRATO MENSAL"), font=F(40, "Black"), fill=ink, anchor="mm")
    for xx in range(px0 + 40, px1 - 40, 24): dr.line([(xx, py0 + 105), (xx + 12, py0 + 105)], fill=ink2, width=3)
    span = max(0.8, dur * 0.55) / n
    for i, (lab, val, c) in enumerate(lines):
        p = ease((t - 0.6 - i * span) / 0.5)
        if p <= 0: continue
        y = py0 + 170 + i * 105
        dr.text((px0 + 50, y), lab, font=F(40, "SemiBold"), fill=mix((236, 240, 246), ink, p), anchor="lm")
        dr.text((px1 - 50, y), val, font=F(46, "Black"), fill=mix((236, 240, 246), hexc(c), p), anchor="rm")
    if v.get("total"):
        p = ease((t - 0.6 - n * span) / 0.6)
        if p > 0:
            y = py1 - 75
            dr.line([(px0 + 40, y - 60), (px1 - 40, y - 60)], fill=mix((236, 240, 246), ink, p), width=4)
            dr.text((px0 + 50, y), v["total"][0], font=F(46, "Black"), fill=mix((236, 240, 246), ink, p), anchor="lm")
            dr.text((px1 - 50, y), v["total"][1], font=F(56, "Black"), fill=mix((236, 240, 246), (30, 150, 90), p), anchor="rm")
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_stack(img, v, t, dur):
    """Criado no EP04: barra 100% empilhada (fatias de um total). parts = [[rótulo, pct, cor_hex, nota]]; highlight opcional."""
    dr = ImageDraw.Draw(img); parts = v["parts"]; hl = v.get("highlight", -1)
    alpha_text(img, (W / 2, 200), v["title"], F(66, "ExtraBold"), WHITE, ease(t / 0.5))
    x0, x1, y = 160, W - 160, 470
    tot = sum(p[1] for p in parts); cx = x0
    span = max(0.9, dur * 0.5) / len(parts)
    for i, (lab, pct, c, note) in enumerate(parts):
        p = ease((t - 0.5 - i * span) / 0.7)
        w = (x1 - x0) * pct / tot
        col = hexc(c) if (hl < 0 or i == hl) else mix(hexc(c), BG1, 0.6)
        if p > 0:
            dr.rounded_rectangle([cx + 4, y - 90, cx + 4 + max(8, (w - 8) * p), y + 90], 18, fill=col)
            if p > 0.6:
                dr.text((cx + w / 2, y), f"{fmt_num(pct, 0)}%", font=F(84, "Black"), fill=BG1, anchor="mm")
                tc = WHITE if (hl < 0 or i == hl) else (110, 120, 145)
                dr.text((cx + w / 2, y + 160), lab, font=F(48, "ExtraBold"), fill=tc, anchor="mm")
                for j, ln in enumerate(note.split("\n")):
                    dr.text((cx + w / 2, y + 225 + j * 46), ln, font=F(32, "Medium"), fill=DIM, anchor="mm")
        cx += w
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_round(img, v, t, dur):
    """Criado no EP05: cartão de luta. n, year, left, right, sub. 'ROUND N' entra de cima; nomes deslizam das laterais."""
    dr = ImageDraw.Draw(img)
    a = ease(t / 0.5); a2 = ease((t - 0.5) / 0.6); a3 = ease((t - 1.1) / 0.6)
    # faixas diagonais de fundo
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.polygon([(0, 330), (W, 250), (W, 330), (0, 410)], fill=AMBER + (int(40 * a),))
    d2.polygon([(0, 760), (W, 680), (W, 720), (0, 800)], fill=GREEN + (int(30 * a),))
    img.alpha_composite(lay)
    alpha_text(img, (W / 2, 250 - (1 - a) * 60), f"ROUND {v['n']}", F(150, "Black"), AMBER, a)
    if v.get("year"):
        w = F(40, "Black").getlength(v["year"]) + 60
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d3 = ImageDraw.Draw(lay)
        d3.rounded_rectangle([W / 2 - w / 2, 365, W / 2 + w / 2, 425], 30, fill=WHITE + (int(235 * a),))
        img.alpha_composite(lay)
        alpha_text(img, (W / 2, 395), v["year"], F(40, "Black"), BG1, a)
    sz = 84
    while max(F(sz, "ExtraBold").getlength(v["left"]), F(sz, "ExtraBold").getlength(v["right"])) > 700 and sz > 44: sz -= 4
    alpha_text(img, (W / 2 - 110 - (1 - a2) * 300, 560), v["left"], F(sz, "ExtraBold"), GREEN, a2, anchor="rm")
    alpha_text(img, (W / 2 + 110 + (1 - a2) * 300, 560), v["right"], F(sz, "ExtraBold"), RED, a2, anchor="lm")
    alpha_text(img, (W / 2, 560), "×", F(110, "Black"), WHITE, a2)
    if v.get("sub"):
        alpha_text(img, (W / 2, 880), v["sub"], F(52, "SemiBold"), WHITE, a3, dy=(1 - a3) * 20)
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_ticker(img, v, t, dur):
    """Criado no EP05: painel de cotações em queda/alta num dia. rows = [[nome, pct, nota]]. Barra vermelha p/ queda."""
    dr = ImageDraw.Draw(img)
    alpha_text(img, (160, 170), v["title"], F(60, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    if v.get("date"):
        alpha_text(img, (W - 160, 170), v["date"], F(40, "Bold"), AMBER, ease(t / 0.5), anchor="rm")
    rows = v["rows"]; mx = max(abs(r[1]) for r in rows)
    span = max(0.8, dur * 0.5) / len(rows)
    for i, (name, pct, note) in enumerate(rows):
        p = ease((t - 0.4 - i * span) / 0.8); y = 330 + i * 160 + (4 - len(rows)) * 80
        dr.rounded_rectangle([140, y - 62, W - 140, y + 62], 20, fill=(18, 28, 46), outline=(40, 56, 84), width=2)
        if p <= 0: continue
        col = RED if pct < 0 else GREEN
        dr.text((190, y - 12), name, font=F(50, "ExtraBold"), fill=mix(BG1, WHITE, p), anchor="lm")
        if note: dr.text((190, y + 36), note, font=F(26, "Medium"), fill=mix(BG1, DIM, p), anchor="lm")
        bx0 = 820; bw = 560 * abs(pct) / mx * p
        dr.rounded_rectangle([bx0, y - 26, bx0 + max(8, bw), y + 26], 10, fill=col)
        tx = W - 180
        s = ("−" if pct < 0 else "+") + fmt_num(abs(pct) * p, v.get("decimals", 1)) + "%"
        dr.text((tx, y), s, font=F(56, "Black"), fill=col, anchor="rm")
        cx = bx0 - 40
        if pct < 0: dr.polygon([(cx - 18, y - 12), (cx + 18, y - 12), (cx, y + 16)], fill=col)
        else: dr.polygon([(cx - 18, y + 12), (cx + 18, y + 12), (cx, y - 16)], fill=col)
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_scoreboard(img, v, t, dur):
    """Criado no EP05: placar em colunas verticais. cols = [[nome, valor, cor_hex]]; highlight = índice (opcional)."""
    dr = ImageDraw.Draw(img); cols = v["cols"]; n = len(cols); hl = v.get("highlight", -1)
    alpha_text(img, (W / 2, 170), v["title"], F(62, "ExtraBold"), WHITE, ease(t / 0.5))
    base, hmax = 830, 470; cw = min(220, (W - 320) / n - 40); gap = (W - 320 - n * cw) / max(1, n - 1)
    mx = max(c[1] for c in cols)
    dr.line([(140, base + 4), (W - 140, base + 4)], fill=(60, 72, 100), width=4)
    for i, (name, val, c) in enumerate(cols):
        p = ease((t - 0.4 - i * 0.3) / 0.9); x = 160 + i * (cw + gap); cx = x + cw / 2
        col = hexc(c) if (hl < 0 or i == hl) else mix(hexc(c), BG1, 0.55)
        hh = hmax * val / mx * p
        dr.rounded_rectangle([x, base - max(hh, 10), x + cw, base], 18, fill=col)
        if p > 0.05:
            dr.text((cx, base - hh - 40), fmt_num(val * p, v.get("decimals", 0)) + v.get("suffix", "%"), font=F(56, "Black"), fill=WHITE, anchor="mm")
        fs = 38
        while F(fs, "ExtraBold").getlength(name) > cw + 30 and fs > 24: fs -= 2
        dr.text((cx, base + 50), name, font=F(fs, "ExtraBold"), fill=mix(BG1, WHITE if (hl < 0 or i == hl) else (130, 140, 165), max(p, 0.3)), anchor="mm")
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

SC = {"round": sc_round, "ticker": sc_ticker, "scoreboard": sc_scoreboard, "title": sc_title, "bignumber": sc_bignumber, "flow": sc_flow, "split": sc_split, "bullets": sc_bullets,
      "bars": sc_bars, "compare": sc_compare, "timeline": sc_timeline, "cards": sc_cards, "line": sc_line,
      "receipt": sc_receipt, "stack": sc_stack}

# ---------- voz ----------
def tts(scenes, outdir, voice="pm_alex", speed=1.05):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(HERE, "models/kokoro.onnx"), os.path.join(HERE, "models/voices.bin"))
    durs = []; chunks = []; sr = 24000
    for i, s in enumerate(scenes):
        cache = os.path.join(outdir, f"cena_{i:02d}.wav")
        if os.path.exists(cache) and open(cache + ".txt").read() == s["say"]:
            a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(s["say"], voice=voice, speed=speed, lang="pt-br")
            sf.write(cache, a, sr); open(cache + ".txt", "w").write(s["say"])
        a = np.concatenate([np.zeros(int(sr * 0.15)), a, np.zeros(int(sr * 0.45))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
        print(f"tts {i+1}/{len(scenes)} {durs[-1]:.1f}s", flush=True)
    audio = np.concatenate(chunks)
    audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    sf.write(os.path.join(outdir, "voz.wav"), audio, sr)
    return durs

def srt_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int((s % 1) * 1000):03d}"

def write_srt(scenes, durs, path):
    out = []; t0 = 0.0; n = 1
    for s, d in zip(scenes, durs):
        sents = [x.strip() for x in re.split(r"(?<=[.?!])\s+", s["say"]) if x.strip()]
        total = sum(len(x) for x in sents); t = t0 + 0.15; usable = d - 0.6
        for x in sents:
            dd = usable * len(x) / total
            out.append(f"{n}\n{srt_time(t)} --> {srt_time(t + dd)}\n{x}\n"); n += 1; t += dd
        t0 += d
    open(path, "w").write("\n".join(out))

def render(scenes, durs, outdir):
    global BG
    BG = make_bg().convert("RGBA")
    total = sum(durs)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voz.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", os.path.join(outdir, "video.mp4")]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    elapsed = 0.0
    for i, (s, d) in enumerate(zip(scenes, durs)):
        nf = int(round(d * FPS)); v = s["vis"]
        for f in range(nf):
            t = f / FPS
            img = BG.copy()
            SC[v["type"]](img, v, t, d)
            chrome(img, (elapsed + t) / total)
            if t < 0.25:
                img = Image.blend(BG, img, ease(t / 0.25))
            p.stdin.write(img.convert("RGB").tobytes())
        elapsed += d
        print(f"render cena {i+1}/{len(scenes)}", flush=True)
    p.stdin.close(); p.wait()

def preview(scenes, outdir, at=0.8):
    """Gera um PNG por cena (no instante 'at' da duração) para conferir layout."""
    global BG
    BG = make_bg().convert("RGBA")
    durs = json.load(open(os.path.join(outdir, "durs.json"))) if os.path.exists(os.path.join(outdir, "durs.json")) else [10] * len(scenes)
    os.makedirs(os.path.join(outdir, "prev"), exist_ok=True)
    for i, (s, d) in enumerate(zip(scenes, durs)):
        img = BG.copy(); SC[s["vis"]["type"]](img, s["vis"], d * at, d); chrome(img, 0.5)
        img.convert("RGB").resize((960, 540)).save(os.path.join(outdir, "prev", f"{i:02d}.png"))

HERE = os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ep", sys.argv[1]); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    only = sys.argv[3] if len(sys.argv) > 3 else None
    scenes = ep.SCENES
    if only == "preview":
        preview(scenes, outdir); print("preview ok"); sys.exit()
    durs = tts(scenes, outdir)
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
    write_srt(scenes, durs, os.path.join(outdir, "legendas.srt"))
    print("duração total:", round(sum(durs), 1), "s")
    if only == "tts": sys.exit()
    render(scenes, durs, outdir)
    print("ok")
