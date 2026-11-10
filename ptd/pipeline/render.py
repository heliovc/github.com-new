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
                fsn = 84
                while F(fsn, "Black").getlength(f"{fmt_num(pct, 0)}%") > w - 30 and fsn > 40: fsn -= 4
                dr.text((cx + w / 2, y), f"{fmt_num(pct, 0)}%", font=F(fsn, "Black"), fill=BG1, anchor="mm")
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


def sc_journey(img, v, t, dur):
    """Criado no EP06: mapa de paradas ("siga o recebível"). stops = [rótulos curtos]; cur = índice da parada atual;
    title/sub = nome grande da parada. Paradas já vencidas ficam verdes com check; a moeda R$ viaja até a atual."""
    dr = ImageDraw.Draw(img); stops = v["stops"]; cur = v["cur"]; n = len(stops)
    alpha_text(img, (W / 2, 150), v.get("head", "SIGA O RECEBÍVEL"), F(40, "Black"), AMBER, ease(t / 0.4))
    x0, x1, y = 200, W - 200, 430
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    dr.line([(x0, y), (x1, y)], fill=(44, 60, 92), width=10)
    pm = ease((t - 0.2) / 1.2)
    xc = lerp(xs[max(cur - 1, 0)], xs[cur], pm)
    dr.line([(x0, y), (xc, y)], fill=GREEN, width=10)
    for i, (x, lab) in enumerate(zip(xs, stops)):
        if i < cur:
            dr.ellipse([x - 26, y - 26, x + 26, y + 26], fill=GREEN)
            dr.line([(x - 11, y + 1), (x - 3, y + 10), (x + 13, y - 9)], fill=BG1, width=6)
            col = (150, 200, 170)
        elif i == cur:
            r = 40 + 5 * math.sin(t * 4)
            dr.ellipse([x - r - 10, y - r - 10, x + r + 10, y + r + 10], outline=AMBER, width=4)
            dr.ellipse([x - r, y - r, x + r, y + r], fill=AMBER)
            dr.text((x, y + 2), str(i + 1), font=F(42, "Black"), fill=BG1, anchor="mm")
            col = WHITE
        else:
            dr.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(30, 42, 66), outline=(70, 86, 118), width=4)
            dr.text((x, y + 1), str(i + 1), font=F(26, "Bold"), fill=(110, 125, 150), anchor="mm")
            col = (110, 125, 150)
        fs = 26
        while F(fs, "Bold").getlength(lab) > (x1 - x0) / (n - 1) - 12 and fs > 18: fs -= 1
        dr.text((x, y + 78), lab, font=F(fs, "Bold"), fill=col, anchor="mm")
    # moeda viajando
    cy = y - 95 - 18 * math.sin(pm * math.pi)
    dr.ellipse([xc - 34, cy - 34, xc + 34, cy + 34], fill=AMBER, outline=(255, 215, 120), width=4)
    dr.text((xc, cy + 1), "R$", font=F(26, "Black"), fill=BG1, anchor="mm")
    a = ease((t - 0.5) / 0.6)
    alpha_text(img, (W / 2, 700), v["title"], F(100, "ExtraBold"), WHITE, a, dy=(1 - a) * 30)
    if v.get("sub"): alpha_text(img, (W / 2, 820), v["sub"], F(44, "SemiBold"), GREEN, ease((t - 0.9) / 0.6))
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_calendar(img, v, t, dur):
    """Criado no EP06: agenda de recebíveis. cells = [[rótulo, valor_txt]] (até 12, grade 6x2); caixa HOJE à esquerda.
    pull=True: as parcelas são "puxadas" para HOJE uma a uma e os contadores today_to / cost_to sobem (antecipação).
    Sem pull: as parcelas aparecem uma a uma no calendário (today_txt opcional na caixa HOJE)."""
    dr = ImageDraw.Draw(img); cells = v["cells"]; n = len(cells)
    alpha_text(img, (W / 2, 150), v["title"], F(60, "ExtraBold"), WHITE, ease(t / 0.5))
    hx0, hx1, hy0, hy1 = 110, 520, 290, 790
    a0 = ease((t - 0.1) / 0.5)
    dr.rounded_rectangle([hx0, hy0, hx1, hy1], 28, fill=mix(BG1, (24, 60, 48), a0), outline=mix(BG1, GREEN, a0), width=5)
    dr.text(((hx0 + hx1) / 2, hy0 + 60), v.get("today_label", "HOJE"), font=F(48, "Black"), fill=mix(BG1, GREEN, a0), anchor="mm")
    cols, cw, ch, gap = 6, 190, 210, 14
    gx0, gy0 = 590, 300
    pos = [(gx0 + (i % cols) * (cw + gap), gy0 + (i // cols) * (ch + gap + 46)) for i in range(n)]
    pull = v.get("pull", False)
    span = max(0.25, (dur * 0.6 - 1.0) / max(n, 1))
    done = 0.0
    for i, (lab, val) in enumerate(cells):
        x, y = pos[i]
        if pull:
            p = ease((t - 1.0 - i * span) / 0.6); done += p
            cx = lerp(x, (hx0 + hx1) / 2 - cw / 2, p); cy = lerp(y, (hy0 + hy1) / 2 - ch / 2, p)
            al = 1 - p
            if al <= 0.02: 
                dr.text((x + cw / 2, y + ch / 2), "—", font=F(40, "Bold"), fill=(60, 74, 100), anchor="mm"); continue
            ap = 1.0
        else:
            ap = ease((t - 0.5 - i * span) / 0.4)
            if ap <= 0: continue
            cx, cy, al = x, y, ap
        fill = mix(BG1, (34, 52, 84), al); out = mix(BG1, AMBER if (v.get("highlight", -1) == i) else BLUE, al)
        dr.rounded_rectangle([cx, cy, cx + cw, cy + ch], 20, fill=fill, outline=out, width=4)
        dr.text((cx + cw / 2, cy + 45), lab, font=F(30, "Bold"), fill=mix(BG1, DIM, al), anchor="mm")
        dr.text((cx + cw / 2, cy + 125), val, font=F(44, "Black"), fill=mix(BG1, WHITE, al), anchor="mm")
    hc = ((hx0 + hx1) / 2)
    if pull:
        frac = done / n
        dr.text((hc, hy0 + 200), v.get("prefix", "R$ ") + fmt_num(v["today_to"] * frac, 0), font=F(76, "Black"), fill=WHITE, anchor="mm")
        dr.text((hc, hy0 + 290), "na conta hoje", font=F(32, "SemiBold"), fill=DIM, anchor="mm")
        dr.text((hc, hy0 + 380), "- " + v.get("prefix", "R$ ") + fmt_num(v["cost_to"] * frac, 0), font=F(58, "Black"), fill=RED, anchor="mm")
        dr.text((hc, hy0 + 440), v.get("cost_label", "custo da antecipação"), font=F(28, "SemiBold"), fill=DIM, anchor="mm")
    elif v.get("today_txt"):
        dr.text((hc, (hy0 + hy1) / 2 + 30), v["today_txt"], font=F(80, "Black"), fill=mix(BG1, WHITE, a0), anchor="mm")
        if v.get("today_note"): dr.text((hc, (hy0 + hy1) / 2 + 120), v["today_note"], font=F(30, "SemiBold"), fill=mix(BG1, DIM, a0), anchor="mm")
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_obit(img, v, t, dur):
    """Criado no EP07: ficha de autópsia de uma receita. case, name, born, died, cause, note; stamp (texto) + stamp_col (hex).
    Papel claro entra; linhas são preenchidas uma a uma; carimbo bate inclinado no fim."""
    dr = ImageDraw.Draw(img)
    a = ease(t / 0.5)
    px0, px1, py0, py1 = 430, 1490, 110 + (1 - a) * 60, 980 + (1 - a) * 60
    paper = (232, 228, 214); ink, ink2 = (28, 30, 40), (110, 105, 95)
    dr.rounded_rectangle([px0, py0, px1, py1], 18, fill=mix(BG1, paper, a))
    if a < 0.4: return
    dr.rectangle([px0, py0, px1, py0 + 90], fill=(40, 44, 58))
    dr.text((px0 + 40, py0 + 45), "FICHA DE AUTÓPSIA", font=F(40, "Black"), fill=paper, anchor="lm")
    dr.text((px1 - 40, py0 + 45), v.get("case", ""), font=F(34, "Bold"), fill=AMBER, anchor="rm")
    rows = [("VÍTIMA", v["name"]), ("NASCIMENTO", v.get("born", "")), ("ÓBITO", v.get("died", "")), ("CAUSA", v.get("cause", ""))]
    span = max(0.5, dur * 0.4) / len(rows)
    for i, (lab, val) in enumerate(rows):
        p = ease((t - 0.5 - i * span) / 0.5)
        y = py0 + 160 + i * 110
        dr.text((px0 + 50, y), lab, font=F(28, "Bold"), fill=ink2, anchor="lm")
        for xx in range(int(px0 + 330), int(px1 - 50), 18): dr.line([(xx, y + 34), (xx + 9, y + 34)], fill=(190, 184, 170), width=2)
        if p > 0:
            fs = 56 if i == 0 else 44
            while F(fs, "ExtraBold").getlength(val) > px1 - px0 - 400 and fs > 26: fs -= 2
            dr.text((px0 + 330, y), val, font=F(fs, "ExtraBold"), fill=mix(paper, ink, p), anchor="lm")
    if v.get("note"):
        p = ease((t - 0.5 - len(rows) * span) / 0.5)
        dr.text(((px0 + px1) / 2, py1 - 50), v["note"], font=F(32, "SemiBold"), fill=mix(paper, ink2, p), anchor="mm")
    if v.get("stamp"):
        ts = 0.7 + len(rows) * span
        p = ease((t - ts) / 0.25)
        if p > 0:
            sc = 1.6 - 0.6 * p
            col = hexc(v.get("stamp_col", "#C0392B"))
            txt = v["stamp"]; f = F(int(66 * sc), "Black")
            tw = f.getlength(txt) + 60 * sc; th = 120 * sc
            lay = Image.new("RGBA", (int(tw) + 20, int(th) + 20), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            d2.rounded_rectangle([10, 10, 10 + tw, 10 + th], int(14 * sc), outline=col + (int(230 * p),), width=max(4, int(9 * sc)))
            d2.text((10 + tw / 2, 10 + th / 2), txt, font=f, fill=col + (int(230 * p),), anchor="mm")
            lay = lay.rotate(-12, expand=True, resample=Image.BICUBIC)
            img.alpha_composite(lay, (int(px1 - 30 - lay.width), int(py0 + 650 - lay.height / 2)))
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_race(img, v, t, dur):
    """Criado no EP07: corrida de transferências. lanes = [[nome, rótulo_tempo, fração_de_velocidade (1=mais rápido), cor_hex]].
    Cada raia avança uma moeda R$ até a chegada; a mais rápida chega primeiro e acende 'CHEGOU'."""
    dr = ImageDraw.Draw(img); lanes = v["lanes"]; n = len(lanes)
    alpha_text(img, (W / 2, 160), v["title"], F(64, "ExtraBold"), WHITE, ease(t / 0.5))
    x0, x1 = 470, W - 260
    for xx in range(x1, x1 + 30, 15):
        for yy in range(260, 260 + n * 190, 30):
            c = WHITE if ((xx - x1) // 15 + (yy - 260) // 30) % 2 == 0 else (40, 50, 70)
            dr.rectangle([xx, yy, xx + 15, yy + 30], fill=c)
    T = max(1.5, dur * 0.55)
    for i, (name, lab, spd, c) in enumerate(lanes):
        y = 340 + i * 190 + (3 - n) * 95
        col = hexc(c)
        dr.text((140, y), name, font=F(60, "Black"), fill=col, anchor="lm")
        dr.rounded_rectangle([x0, y - 14, x1, y + 14], 14, fill=(30, 42, 66))
        p = ease(max(0.0, t - 0.6) * spd / T) if spd > 0 else 0
        p = min(p, v.get("cap", [1] * n)[i]) if v.get("cap") else p
        xc = lerp(x0, x1, p)
        dr.rounded_rectangle([x0, y - 14, max(x0 + 28, xc), y + 14], 14, fill=col)
        dr.ellipse([xc - 36, y - 36, xc + 36, y + 36], fill=AMBER, outline=(255, 215, 120), width=4)
        dr.text((xc, y + 1), "R$", font=F(26, "Black"), fill=BG1, anchor="mm")
        dr.text((x0, y + 62), lab, font=F(32, "SemiBold"), fill=DIM if p < 0.999 else col, anchor="lm")
        if p >= 0.999:
            dr.text((x1 + 60, y), "✓", font=F(56, "Black"), fill=col, anchor="lm") if False else dr.text((x1 - 10, y - 60), "CHEGOU", font=F(30, "Black"), fill=col, anchor="rm")
    if v.get("caption"): alpha_text(img, (W / 2, H - 90), v["caption"], F(34, "SemiBold"), GREEN, ease((t - T) / 0.6))

def sc_act(img, v, t, dur):
    """Criado no EP08: abertura de ato num palco. n (número do ato), title, sub. Cortinas vermelhas abrem dos lados,
    um holofote acende no centro e o título sobe."""
    dr = ImageDraw.Draw(img)
    p = ease((t - 0.15) / 1.0)
    # holofote
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    a = int(70 * p)
    d2.polygon([(W / 2 - 90, 0), (W / 2 + 90, 0), (W / 2 + 520, H), (W / 2 - 520, H)], fill=(255, 236, 190, a))
    d2.ellipse([W / 2 - 560, H - 170, W / 2 + 560, H + 70], fill=(255, 236, 190, int(55 * p)))
    img.alpha_composite(lay)
    # cortinas
    cw = lerp(W / 2 + 10, 300, p)
    for side in (0, 1):
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d3 = ImageDraw.Draw(lay)
        x0, x1 = (0, cw) if side == 0 else (W - cw, W)
        d3.rectangle([x0, 0, x1, H], fill=(120, 18, 30, 255))
        k = 0; xx = x0
        while xx < x1:
            d3.rectangle([xx, 0, xx + 22, H], fill=(150, 28, 42, 255) if k % 2 == 0 else (96, 12, 22, 255)); xx += 46; k += 1
        img.alpha_composite(lay)
    dr = ImageDraw.Draw(img)
    dr.rectangle([0, 0, W, 70], fill=(90, 10, 20))
    for xx in range(0, W, 60): dr.pieslice([xx, 40, xx + 60, 100], 0, 180, fill=(90, 10, 20))
    a1 = ease((t - 0.7) / 0.5); a2 = ease((t - 1.0) / 0.5); a3 = ease((t - 1.3) / 0.5)
    alpha_text(img, (W / 2, 330), f"ATO {v['n']}", F(70, "Black"), AMBER, a1, dy=(1 - a1) * 30)
    lines = v["title"].split("\n")
    for i, l in enumerate(lines):
        alpha_text(img, (W / 2, 470 + i * 120 - (len(lines) - 1) * 60), l, F(108, "ExtraBold"), WHITE, a2, dy=(1 - a2) * 30)
    if v.get("sub"): alpha_text(img, (W / 2, 690), v["sub"], F(46, "SemiBold"), (255, 226, 170), a3)
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_ledger(img, v, t, dur):
    """Criado no EP08: folha de balanço com linhas [[rótulo, valor_txt]]. move = [de, para, rótulo_da_ficha]: uma ficha
    sai da linha 'de' e desliza até a linha 'para' (ex.: dívida com banco escondida em fornecedores). stamp opcional."""
    dr = ImageDraw.Draw(img)
    alpha_text(img, (W / 2, 150), v["title"], F(58, "ExtraBold"), WHITE, ease(t / 0.5))
    a = ease((t - 0.1) / 0.5)
    rows = v["rows"]; n = len(rows)
    px0, px1, py0 = 360, 1560, 240
    py1 = py0 + 110 + n * 120 + 30
    paper, ink, ink2 = (236, 240, 246), (20, 30, 48), (95, 105, 125)
    dr.rounded_rectangle([px0, py0, px1, py1], 22, fill=mix(BG1, paper, a))
    if a < 0.3: return
    dr.rectangle([px0, py0, px1, py0 + 80], fill=(34, 48, 74))
    dr.text((px0 + 40, py0 + 40), v.get("head", "BALANÇO PATRIMONIAL — PASSIVO"), font=F(34, "Black"), fill=paper, anchor="lm")
    ys = [py0 + 150 + i * 120 for i in range(n)]
    mv = v.get("move"); hl_to = mv[1] if mv else -1
    for i, (lab, val) in enumerate(rows):
        p = ease((t - 0.4 - i * 0.25) / 0.4)
        if p <= 0: continue
        y = ys[i]
        if i > 0: dr.line([(px0 + 40, y - 60), (px1 - 40, y - 60)], fill=(205, 210, 220), width=2)
        dr.text((px0 + 50, y), lab, font=F(44, "SemiBold"), fill=mix(paper, ink, p), anchor="lm")
        dr.text((px1 - 50, y), val, font=F(48, "Black"), fill=mix(paper, ink, p), anchor="rm")
    if mv:
        t0 = 0.6 + n * 0.25; T = max(1.2, dur * 0.35)
        p = ease((t - t0 - 0.6) / T)
        if t > t0:
            fy = lerp(ys[mv[0]], ys[mv[1]], p)
            f = F(40, "Black"); tw = f.getlength(mv[2]) + 60
            x0 = px0 + 680 - tw / 2
            col = RED if p < 0.999 else AMBER
            dr.rounded_rectangle([x0, fy - 38, x0 + tw, fy + 38], 38, fill=col)
            dr.text((x0 + tw / 2, fy), mv[2], font=f, fill=BG1 if p >= 0.999 else WHITE, anchor="mm")
            if p > 0.02 and p < 0.999:
                dr.line([(x0 - 30, ys[mv[0]]), (x0 - 30, fy)], fill=RED, width=5)
    if v.get("stamp"):
        ts = 0.6 + n * 0.25 + (max(1.2, dur * 0.35) + 0.8 if mv else 0.3)
        p = ease((t - ts) / 0.25)
        if p > 0:
            sc = 1.6 - 0.6 * p; col = hexc(v.get("stamp_col", "#C0392B"))
            txt = v["stamp"]; f = F(int(60 * sc), "Black")
            tw = f.getlength(txt) + 60 * sc; th = 110 * sc
            lay = Image.new("RGBA", (int(tw) + 20, int(th) + 20), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
            d2.rounded_rectangle([10, 10, 10 + tw, 10 + th], int(14 * sc), outline=col + (int(230 * p),), width=max(4, int(9 * sc)))
            d2.text((10 + tw / 2, 10 + th / 2), txt, font=f, fill=col + (int(230 * p),), anchor="mm")
            lay = lay.rotate(10, expand=True, resample=Image.BICUBIC)
            img.alpha_composite(lay, (int(px1 - 40 - lay.width), int(py1 - lay.height + 30)))
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_blackbox(img, v, t, dur):
    """Criado no EP09: abertura de trecho como caixa-preta de avião. n (trecho), title, sub, time (rótulo de época).
    A caixa laranja entra pela esquerda, o título surge à direita e uma onda de áudio 'tocando' corre embaixo."""
    dr = ImageDraw.Draw(img)
    p = ease((t - 0.1) / 0.8)
    bx, by, bw, bh = lerp(-600, 210, p), 300, 560, 420
    OR, ORD = (240, 128, 30), (180, 86, 14)
    lay = Image.new("RGBA", (bw + 40, bh + 40), (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
    d2.rounded_rectangle([20, 20, 20 + bw, 20 + bh], 34, fill=OR)
    for k in range(0, bw, 70):
        d2.polygon([(20 + k, 20 + bh - 60), (60 + k, 20 + bh - 60), (20 + k + 20, 20 + bh), (20 + k - 20, 20 + bh)], fill=(30, 30, 30))
    d2.rectangle([20, 20 + bh - 60, 20 + bw, 20 + bh - 56], fill=ORD)
    d2.text((20 + bw / 2, 110), "GRAVADOR DE VOO", font=F(44, "Black"), fill=(30, 22, 12), anchor="mm")
    d2.text((20 + bw / 2, 170), "NÃO ABRIR", font=F(34, "Bold"), fill=(70, 40, 10), anchor="mm")
    d2.rounded_rectangle([80, 225, bw - 40, 330], 16, fill=(30, 22, 12))
    d2.text((20 + bw / 2, 278), v.get("time", ""), font=F(48, "Black"), fill=OR, anchor="mm")
    lay = lay.rotate(-4, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(lay, (int(bx), int(by - 30)))
    a1 = ease((t - 0.7) / 0.5); a2 = ease((t - 1.0) / 0.5); a3 = ease((t - 1.3) / 0.5)
    x = 900
    alpha_text(img, (x, 330), f"TRECHO {v['n']}", F(64, "Black"), OR, a1, anchor="lm", dy=(1 - a1) * 30)
    lines = v["title"].split("\n")
    for i, l in enumerate(lines):
        alpha_text(img, (x, 450 + i * 110), l, F(100, "ExtraBold"), WHITE, a2, anchor="lm", dy=(1 - a2) * 30)
    if v.get("sub"): alpha_text(img, (x, 450 + len(lines) * 110 + 20), v["sub"], F(44, "SemiBold"), (255, 200, 150), a3, anchor="lm")
    # onda de áudio
    yb = 900
    for i in range(0, W - 200, 14):
        xx = 100 + i
        if xx > 100 + (W - 200) * ease(t / max(1.0, dur * 0.8)): break
        hgt = 10 + 34 * abs(math.sin(i * 0.07 + t * 5) * math.sin(i * 0.013))
        dr.line([(xx, yb - hgt), (xx, yb + hgt)], fill=OR if i % 28 == 0 else (150, 90, 40), width=6)
    if v.get("caption"): dr.text((W / 2, H - 50), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

def sc_flight(img, v, t, dur):
    """Criado no EP09: rota de voo. points = [[rótulo, altitude 0-100], ...]; alerts = [[posição (índice, pode ser
    fracionário), texto], ...] viram triângulos vermelhos quando o avião passa; crash=True pinta o fim de vermelho."""
    dr = ImageDraw.Draw(img); pts = v["points"]; n = len(pts)
    alpha_text(img, (160, 170), v["title"], F(60, "ExtraBold"), WHITE, ease(t / 0.5), anchor="lm")
    x0, x1, y0, y1 = 220, W - 220, 860, 330
    for k in range(5):
        yy = lerp(y0, y1, k / 4)
        for xx in range(x0, x1, 36): dr.line([(xx, yy), (xx + 16, yy)], fill=(36, 50, 76), width=2)
    dr.line([(x0, y0), (x1, y0)], fill=(70, 85, 110), width=4)
    def P(i):
        i = max(0.0, min(n - 1.0, i)); k = min(int(i), n - 2); f = i - k
        return (lerp(x0, x1, i / (n - 1)), y0 - (y0 - y1) * lerp(pts[k][1], pts[k + 1][1], f) / 100)
    for i, (lab, _) in enumerate(pts):
        dr.text((lerp(x0, x1, i / (n - 1)), y0 + 44), lab, font=F(30, "SemiBold"), fill=DIM, anchor="mm")
    prog = ease((t - 0.3) / max(1.2, dur * 0.7)) * (n - 1)
    steps = max(2, int(prog * 30) + 2)
    xy = [P(prog * j / (steps - 1)) for j in range(steps)]
    crash_from = v.get("crash_from", n - 2) if v.get("crash") else 99
    good = [q for j, q in enumerate(xy) if prog * j / (steps - 1) <= crash_from + 1e-6]
    bad = [q for j, q in enumerate(xy) if prog * j / (steps - 1) >= crash_from - 1e-6]
    if len(good) >= 2: dr.line(good, fill=hexc("#5B8DEF"), width=8, joint="curve")
    if len(bad) >= 2: dr.line(bad, fill=RED, width=8, joint="curve")
    for pos, txt in v.get("alerts", []):
        if prog + 1e-6 < pos: continue
        a = ease((prog - pos) / 0.3 + 0.2)
        x, y = P(pos)
        dr.polygon([(x, y - 70), (x - 26, y - 26), (x + 26, y - 26)], fill=mix(BG1, RED, a))
        dr.text((x, y - 42), "!", font=F(30, "Black"), fill=mix(BG1, WHITE, a), anchor="mm")
        for j, ln in enumerate(txt.split("\n")):
            dr.text((x, y - 110 - (len(txt.split("\n")) - 1 - j) * 38), ln, font=F(30, "Bold"), fill=mix(BG1, (255, 170, 150), a), anchor="mm")
    x, y = xy[-1]; xb, yb = xy[-2] if len(xy) > 1 else (x - 1, y)
    ang = math.atan2(y - yb, x - xb) if (x, y) != (xb, yb) else 0
    ca, sa = math.cos(ang), math.sin(ang)
    pl = [(34, 0), (-22, -20), (-12, 0), (-22, 20)]
    dr.polygon([(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pl], fill=WHITE)
    if v.get("caption"): dr.text((W / 2, H - 70), v["caption"], font=F(28, "Medium"), fill=DIM, anchor="mm")

SC = {"round": sc_round, "ticker": sc_ticker, "scoreboard": sc_scoreboard, "title": sc_title, "bignumber": sc_bignumber, "flow": sc_flow, "split": sc_split, "bullets": sc_bullets,
      "bars": sc_bars, "compare": sc_compare, "timeline": sc_timeline, "cards": sc_cards, "line": sc_line,
      "receipt": sc_receipt, "stack": sc_stack, "journey": sc_journey, "calendar": sc_calendar, "obit": sc_obit, "race": sc_race, "act": sc_act, "ledger": sc_ledger, "blackbox": sc_blackbox, "flight": sc_flight}

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
