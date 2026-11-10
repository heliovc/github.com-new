"""Por Trás do Dinheiro — Shorts de ranking "5 ..." (vertical nativo 1080x1920 30fps).
Uso: python3 -I ranking.py rankXX_algo.py out/rankXX [--preview]
Roteiro: TITLE, THEME {accent, accent2, bar_col, hl_col, glow, bar, chart}, HOOK {say, top, sub}, ITEMS [{rank, name, short, tag, num, prefix, suffix, dec, unit, source, say}], OUTRO {say, note}
Visual: número grande do item + gráfico que vai sendo preenchido (5 -> 1), item atual em destaque.
THEME["chart"]: "hbars" (padrão, barras horizontais), "vbars" (colunas verticais, criado no rank #2)
ou "gauge" (termômetro horizontal com escala, criado no rank #3 — bom para taxas/percentuais)
ou "bubbles" (bolhas com área proporcional ao valor, criado no rank #4 — bom para tamanhos/bases de clientes)
ou "pits" (buracos, rank #5) ou "piles" (pilhas de notas, criado no rank #6 — bom para dívidas/valores em R$)
ou "towers" (arranha-céus com janelas, criado no rank #7 — bom para tamanho de empresas/bancos).
Tudo desenhado por código; narração Kokoro (pm_alex, pt-br); legenda grande queimada. Layout seguro p/ UI do Shorts:
legenda y=1585, @ y=1690, fonte y=1745.
"""
import sys, os, re, json, subprocess, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw
import render as R

W, H, FPS = 1080, 1920, 30
HANDLE = "@portrazdodinheiro"
F, ease, mix, lerp, fmt = R.F, R.ease, R.mix, R.lerp, R.fmt_num
BG1, WHITE, DIM, GREEN = R.BG1, R.WHITE, R.DIM, R.GREEN

def load(path):
    spec = importlib.util.spec_from_file_location("rk", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

_bg = None
def bg(th):
    global _bg
    if _bg is None:
        g = np.zeros((H, W, 3), np.float32); yy, xx = np.mgrid[0:H, 0:W]
        d = np.sqrt(((xx - W * 0.5) / W) ** 2 + ((yy - H * 0.35) / H) ** 2)
        t = np.clip(1 - d * 1.6, 0, 1)[..., None]
        g[:] = np.array(BG1) * (1 - t) + np.array(th.get("glow", (24, 40, 70))) * t
        _bg = Image.fromarray(g.astype(np.uint8)).convert("RGBA")
    return _bg.copy()

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def text(img, xy, s, size, col, w="Black", a=1.0, anchor="mm"):
    if a <= 0: return
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text((xy[0] + 3, xy[1] + 5), s, font=F(size, w), fill=(0, 0, 0, int(150 * a)), anchor=anchor)
    d.text(xy, s, font=F(size, w), fill=tuple(col) + (int(255 * a),), anchor=anchor)
    img.alpha_composite(lay)

def val_str(it, v):
    return it.get("prefix", "") + fmt(v, it.get("dec", 1)) + it.get("suffix", "")

def chart_h(img, items, th, upto, t, cur_rank):
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items)
    order = sorted(items, key=lambda x: x["rank"])
    y0, step = 780, 128; x0, x1 = 370, 880
    for k, it in enumerate(order):
        y = y0 + k * step
        d.text((70, y), f"{it['rank']}º", font=F(44, "Black"), fill=(70, 85, 115), anchor="lm")
        d.rounded_rectangle([x0, y - 34, x1, y + 34], 14, fill=(22, 34, 56))
        if it["rank"] < upto: continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.2) if on else 1.0
        col = tuple(th["hl_col"]) if on else tuple(th["bar_col"])
        bw = (x1 - x0) * it["num"] / mx * p
        d.rounded_rectangle([x0, y - 34, x0 + max(bw, 28), y + 34], 14, fill=col)
        d.text((130, y), it["short"], font=F(36, "ExtraBold"), fill=WHITE if on else (170, 180, 200), anchor="lm")
        d.text((x0 + bw + 16 if bw < (x1 - x0) - 190 else x0 + bw - 16, y), val_str(it, it["num"] * p), font=F(36, "Black"),
               fill=WHITE if bw < (x1 - x0) - 190 else BG1, anchor="lm" if bw < (x1 - x0) - 190 else "rm")

def chart_v(img, items, th, upto, t, cur_rank):
    """Colunas verticais: 5º à esquerda, 1º à direita; base em y=1480, altura máx 560."""
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items)
    order = sorted(items, key=lambda x: -x["rank"])
    base, hmax, cw, gap = 1480, 560, 150, 46
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    d.line([(60, base + 4), (W - 60, base + 4)], fill=(60, 72, 100), width=4)
    for k, it in enumerate(order):
        x = x0 + k * (cw + gap); cx = x + cw / 2
        d.rounded_rectangle([x, base - hmax, x + cw, base], 18, fill=(22, 30, 48))
        d.text((cx, base + 42), f"{it['rank']}º", font=F(40, "Black"), fill=(80, 92, 120), anchor="mm")
        if it["rank"] < upto: continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.2) if on else 1.0
        col = tuple(th["hl_col"]) if on else tuple(th["bar_col"])
        hh = hmax * it["num"] / mx * p
        d.rounded_rectangle([x, base - max(hh, 24), x + cw, base], 18, fill=col)
        fs = 34
        while F(fs, "Black").getlength(val_str(it, it["num"])) > cw + 36 and fs > 22: fs -= 2
        d.text((cx, base - hh - 30), val_str(it, it["num"] * p), font=F(fs, "Black"), fill=WHITE if on else (190, 198, 215), anchor="mm")
        fs2 = 30
        while F(fs2, "ExtraBold").getlength(it["short"]) > cw - 14 and fs2 > 18: fs2 -= 2
        d.text((cx, base - 34), it["short"], font=F(fs2, "ExtraBold"), fill=BG1, anchor="mm")

def chart_g(img, items, th, upto, t, cur_rank):
    """Termômetro (rank #3): tubo horizontal com gradiente frio->quente e escala; cada item vira um marcador
    (pino) na posição do seu valor. Item atual: pino grande que desliza desde o zero; anteriores: pinos menores."""
    d = ImageDraw.Draw(img); mx = th.get("gauge_max", max(i["num"] for i in items) * 1.1)
    x0, x1, y = 110, W - 110, 960
    cold, hot = th.get("cold", (58, 196, 125)), th.get("hot", (224, 70, 70)); midc = th.get("mid", (242, 169, 59))
    def mix(c1, c2, k):  # gradiente de 3 paradas: frio -> âmbar -> quente
        return R.mix(c1, midc, k * 2) if k < 0.5 else R.mix(midc, c2, (k - 0.5) * 2)
    # tubo
    d.rounded_rectangle([x0 - 20, y - 46, x1 + 20, y + 46], 46, fill=(22, 30, 48))
    for k in range(int(x1 - x0)):
        c = mix(cold, hot, k / (x1 - x0))
        d.line([(x0 + k, y - 26), (x0 + k, y + 26)], fill=tuple(int(cc * 0.55 + 10) for cc in c))
    # escala
    step = th.get("gauge_step", 50)
    v = 0
    while v <= mx + 1e-6:
        x = x0 + (x1 - x0) * v / mx
        d.line([(x, y + 56), (x, y + 76)], fill=(90, 102, 130), width=3)
        d.text((x, y + 104), fmt(v, 0) + th.get("gauge_unit", ""), font=F(28, "Bold"), fill=(110, 122, 150), anchor="mm")
        v += step
    order = sorted(items, key=lambda x: -x["rank"])
    for it in order:
        if it["rank"] < upto: continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.4) if on else 1.0
        val = it["num"] * p
        x = x0 + (x1 - x0) * min(val, mx) / mx
        col = mix(cold, hot, min(val, mx) / mx)
        if on:
            d.line([(x0, y), (x, y)], fill=col, width=40)
            d.ellipse([x - 40, y - 40, x + 40, y + 40], fill=col, outline=WHITE, width=6)
            d.polygon([(x - 22, y - 120), (x + 22, y - 120), (x, y - 70)], fill=col)
            d.text((x, y - 160), it["short"], font=F(40, "Black"), fill=WHITE, anchor="mm")
        else:
            d.ellipse([x - 18, y - 18, x + 18, y + 18], fill=col, outline=(20, 26, 40), width=4)
            d.text((x, y - 50 - (it["rank"] % 2) * 40), f"{it['rank']}º", font=F(30, "Black"), fill=(170, 180, 200), anchor="mm")
    # placar dos itens já revelados (5 -> 1, de cima para baixo)
    y2 = 1150
    for it in order:
        if it["rank"] < upto: continue
        on = it["rank"] == cur_rank
        yy = y2 + (5 - it["rank"]) * 78
        col = tuple(th["accent"]) if on else (150, 160, 185)
        d.rounded_rectangle([120, yy - 32, W - 120, yy + 32], 16, fill=(30, 26, 52) if on else (20, 22, 38))
        d.text((150, yy), f"{it['rank']}º  {it['name']}", font=F(36, "ExtraBold"), fill=WHITE if on else col, anchor="lm")
        d.text((W - 150, yy), val_str(it, it["num"]), font=F(38, "Black"), fill=col, anchor="rm")
    return

def chart_b(img, items, th, upto, t, cur_rank):
    """Bolhas (rank #4): cada item = círculo com ÁREA proporcional ao valor. 2 em cima (2º e 3º), 3 embaixo (4º, 1º, 5º).
    Não revelado: contorno tracejado com "?"; atual: cresce do zero com brilho; revelados: preenchidos."""
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items); rmax = th.get("bubble_rmax", 220)
    pos = {1: (540, 1290), 2: (290, 910), 3: (790, 910), 4: (170, 1300), 5: (920, 1300)}
    for it in sorted(items, key=lambda x: x["rank"]):
        cx, cy = pos[it["rank"]]; r = rmax * (it["num"] / mx) ** 0.5
        if it["rank"] < upto:   # ainda escondido
            n = 40
            for k in range(n):
                if k % 2: continue
                a0, a1 = 360 * k / n, 360 * (k + 1) / n
                d.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=(80, 96, 120), width=4)
            d.text((cx, cy), "?", font=F(int(r * 0.7), "Black"), fill=(90, 106, 130), anchor="mm")
            continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.2) if on else 1.0; rr = max(r * p, 2)
        col = tuple(th["accent"]) if on else tuple(th.get("bar_col", (60, 90, 110)))
        if on:
            for g in range(6, 0, -1):
                gg = rr + g * 7
                d.ellipse([cx - gg, cy - gg, cx + gg, cy + gg], fill=tuple(int(c * (0.10 + 0.04 * (6 - g))) for c in col))
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col, outline=WHITE if on else (20, 30, 40), width=5)
        if p > 0.6:
            tc = BG1 if on else WHITE
            fs = int(min(r * 0.30, 54)); d.text((cx, cy - r * 0.18), it["short"], font=F(fs, "Black"), fill=tc, anchor="mm")
            d.text((cx, cy + r * 0.22), val_str(it, it["num"]), font=F(int(min(r * 0.26, 48)), "ExtraBold"), fill=tc, anchor="mm")
        d.text((cx, cy - r - 26), f"{it['rank']}º", font=F(34, "Black"), fill=tuple(th["accent2"]), anchor="mm")
    return

def chart_p(img, items, th, upto, t, cur_rank):
    """Buracos (rank #5, rombos): chão em y=830; cada item = um buraco cavado para baixo com PROFUNDIDADE proporcional
    ao valor (5º à esquerda, 1º à direita). Não revelado: contorno tracejado com "?"; atual: cava do zero com borda brilhante."""
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items)
    ground, hmax, cw, gap = 830, 600, 160, 34
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    soil = tuple(th.get("soil", (70, 40, 52)))
    d.rectangle([40, ground - 14, W - 40, ground + 10], fill=soil)
    for k in range(40, W - 40, 26): d.line([(k, ground - 14), (k + 12, ground - 24)], fill=tuple(int(c * 1.3) for c in soil), width=4)
    order = sorted(items, key=lambda x: -x["rank"])
    for k, it in enumerate(order):
        x = x0 + k * (cw + gap); cx = x + cw / 2
        hh_full = hmax * it["num"] / mx
        d.text((cx, ground - 60), f"{it['rank']}º", font=F(38, "Black"), fill=tuple(th["accent2"]), anchor="mm")
        if it["rank"] < upto:
            yy = ground + 10
            while yy < ground + hh_full:
                d.line([(x, yy), (x, min(yy + 16, ground + hh_full))], fill=(90, 70, 85), width=4)
                d.line([(x + cw, yy), (x + cw, min(yy + 16, ground + hh_full))], fill=(90, 70, 85), width=4); yy += 30
            d.text((cx, ground + min(hh_full, 300) / 2 + 20), "?", font=F(64, "Black"), fill=(110, 90, 105), anchor="mm")
            continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.3) if on else 1.0; hh = max(hh_full * p, 20)
        rim = tuple(th["accent"]) if on else tuple(th.get("bar_col", (120, 60, 80)))
        pts = [(x, ground + 10)]
        n = 7
        for j in range(1, n + 1):
            yy = ground + 10 + hh * j / n; pts.append((x + (6 if j % 2 else -6), yy))
        pts += [(cx, ground + 10 + hh + 18)]
        for j in range(n, 0, -1):
            yy = ground + 10 + hh * j / n; pts.append((x + cw + (-6 if j % 2 else 6), yy))
        pts.append((x + cw, ground + 10))
        d.polygon(pts, fill=(6, 4, 8), outline=rim, width=6 if on else 4)
        fs = 34
        while F(fs, "Black").getlength(val_str(it, it["num"])) > cw - 10 and fs > 20: fs -= 2
        d.text((cx, ground + 10 + hh + 58), val_str(it, it["num"] * p), font=F(fs, "Black"), fill=WHITE if on else (220, 200, 210), anchor="mm")
        fs2 = 30
        while F(fs2, "ExtraBold").getlength(it["short"]) > cw + 20 and fs2 > 18: fs2 -= 2
        d.text((cx, ground - 105), it["short"], font=F(fs2, "ExtraBold"), fill=WHITE if on else (190, 180, 195), anchor="mm")

def chart_n(img, items, th, upto, t, cur_rank):
    """Pilhas de notas (rank #6, recuperações judiciais): 5º à esquerda, 1º à direita, base y=1400; cada pilha = notas
    empilhadas, altura proporcional à dívida. Não revelado: silhueta tracejada com "?"; atual: notas caem uma a uma."""
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items)
    order = sorted(items, key=lambda x: -x["rank"])
    base, hmax, cw, gap, bh = 1400, 560, 160, 32, 20
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    d.rectangle([50, base + 4, W - 50, base + 16], fill=(60, 72, 100))
    paper = tuple(th.get("bill", (96, 160, 110))); dark = tuple(int(c * 0.62) for c in paper)
    for k, it in enumerate(order):
        x = x0 + k * (cw + gap); cx = x + cw / 2
        full = hmax * it["num"] / mx; nb = max(1, int(full / bh))
        d.text((cx, base + 52), f"{it['rank']}º", font=F(40, "Black"), fill=tuple(th["accent2"]), anchor="mm")
        if it["rank"] < upto:
            yy = base
            while yy > base - full:
                d.line([(x, yy), (x, max(yy - 14, base - full))], fill=(70, 82, 110), width=3)
                d.line([(x + cw, yy), (x + cw, max(yy - 14, base - full))], fill=(70, 82, 110), width=3); yy -= 28
            d.line([(x, base - full), (x + cw, base - full)], fill=(70, 82, 110), width=3)
            d.text((cx, base - min(full, 300) / 2), "?", font=F(64, "Black"), fill=(100, 112, 140), anchor="mm")
            continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.4) if on else 1.0; shown = max(1, int(round(nb * p)))
        for j in range(shown):
            y1 = base - j * bh; y0 = y1 - bh + 3; jit = (6 if j % 3 == 0 else -4 if j % 3 == 1 else 2)
            col = paper if on else tuple(int(c * 0.7) for c in paper)
            d.rounded_rectangle([x + jit, y0, x + cw + jit, y1], 5, fill=col, outline=dark, width=2)
            d.ellipse([cx + jit - 7, (y0 + y1) / 2 - 6, cx + jit + 7, (y0 + y1) / 2 + 6], outline=dark, width=2)
        top = base - shown * bh
        if on:
            d.rounded_rectangle([x - 6, top - 6, x + cw + 12, base + 4], 10, outline=tuple(th["accent"]), width=5)
        fs = 34
        while F(fs, "Black").getlength(val_str(it, it["num"])) > cw + 30 and fs > 20: fs -= 2
        d.text((cx, top - 34), val_str(it, it["num"] * p), font=F(fs, "Black"), fill=WHITE if on else (200, 205, 220), anchor="mm")
        fs2 = 30
        while F(fs2, "ExtraBold").getlength(it["short"]) > cw + 24 and fs2 > 18: fs2 -= 2
        d.text((cx, top - 80), it["short"], font=F(fs2, "ExtraBold"), fill=WHITE if on else (180, 186, 205), anchor="mm")

def chart_t(img, items, th, upto, t, cur_rank):
    """Prédios (rank #7, maiores bancos): 5º à esquerda, 1º à direita, base y=1400; cada item = um arranha-céu com
    janelas, altura proporcional ao valor. Não revelado: silhueta tracejada com "?"; atual: o prédio sobe e as janelas acendem."""
    d = ImageDraw.Draw(img); mx = max(i["num"] for i in items)
    order = sorted(items, key=lambda x: -x["rank"])
    base, hmax, cw, gap = 1400, 600, 160, 32
    x0 = W / 2 - (5 * cw + 4 * gap) / 2
    d.rectangle([50, base + 4, W - 50, base + 16], fill=(60, 72, 100))
    body = tuple(th.get("tower", (40, 58, 92))); lit = tuple(th["accent"])
    for k, it in enumerate(order):
        x = x0 + k * (cw + gap); cx = x + cw / 2
        full = hmax * it["num"] / mx
        d.text((cx, base + 52), f"{it['rank']}º", font=F(40, "Black"), fill=tuple(th["accent2"]), anchor="mm")
        if it["rank"] < upto:
            yy = base
            while yy > base - full:
                d.line([(x, yy), (x, max(yy - 14, base - full))], fill=(70, 82, 110), width=3)
                d.line([(x + cw, yy), (x + cw, max(yy - 14, base - full))], fill=(70, 82, 110), width=3); yy -= 28
            d.line([(x, base - full), (x + cw, base - full)], fill=(70, 82, 110), width=3)
            d.text((cx, base - min(full, 300) / 2), "?", font=F(64, "Black"), fill=(100, 112, 140), anchor="mm")
            continue
        on = it["rank"] == cur_rank
        p = ease(t / 1.4) if on else 1.0; hh = max(30, full * p); top = base - hh
        d.rectangle([x, top, x + cw, base], fill=body if on else tuple(int(c * 0.8) for c in body),
                    outline=lit if on else (70, 85, 120), width=5 if on else 2)
        d.rectangle([cx - 6, top - 40, cx + 6, top], fill=(120, 130, 160))
        wy = base - 30; j = 0
        while wy > top + 20:
            for c in range(3):
                wx = x + 22 + c * 46
                on_w = (j * 3 + c) % 4 != 1
                d.rectangle([wx, wy - 18, wx + 26, wy], fill=(lit if on else (150, 140, 100)) if on_w else (24, 32, 50))
            wy -= 40; j += 1
        fs = 34
        while F(fs, "Black").getlength(val_str(it, it["num"])) > cw + 30 and fs > 20: fs -= 2
        d.text((cx, top - 74), val_str(it, it["num"] * p), font=F(fs, "Black"), fill=WHITE if on else (200, 205, 220), anchor="mm")
        fs2 = 30
        while F(fs2, "ExtraBold").getlength(it["short"]) > cw + 24 and fs2 > 18: fs2 -= 2
        d.text((cx, top - 120), it["short"], font=F(fs2, "ExtraBold"), fill=WHITE if on else (180, 186, 205), anchor="mm")

def chart(img, items, th, upto, t, cur_rank):
    {"vbars": chart_v, "gauge": chart_g, "bubbles": chart_b, "pits": chart_p, "piles": chart_n, "towers": chart_t}.get(th.get("chart"), chart_h)(img, items, th, upto, t, cur_rank)

def seg_hook(img, sc, th, t, dur, items):
    ease = lambda x: 1.0  # frame 1 = thumbnail: gancho inteiro visível desde o frame 0 (rank #3)
    a = 1.0
    text(img, (W / 2, 250), "TOP 5", 150, th["accent"], a=a)
    tl = wrap(sc["top"].upper(), F(76, "Black"), W - 120)
    for i, l in enumerate(tl):
        text(img, (W / 2, 390 + i * 86), l, 76, WHITE, a=ease((t - 0.2) / 0.4))
    text(img, (W / 2, 390 + len(tl) * 86 + 10), sc["sub"], 46, th["accent2"], w="ExtraBold", a=ease((t - 0.8) / 0.4))
    chart(img, items, th, 99, t, -1)
    if th.get("chart") == "vbars":
        base, cw, gap = 1480, 150, 46; x0 = W / 2 - (5 * cw + 4 * gap) / 2
        for k in range(5):
            text(img, (x0 + k * (cw + gap) + cw / 2, base - 280), "?", 64, (90, 100, 130), a=ease((t - 0.4 - k * 0.15) / 0.3))
    elif th.get("chart") == "bubbles":
        if sc.get("tease"): text(img, (W / 2, 690), sc["tease"], 64, th["accent"], a=1.0)
    elif th.get("chart") in ("piles", "towers"):
        if sc.get("tease"): text(img, (W / 2, 780), sc["tease"], 64, th["accent"], a=1.0)
    elif th.get("chart") == "pits":
        if sc.get("tease"): text(img, (W / 2, 650), sc["tease"], 64, th["accent"], a=1.0)
    elif th.get("chart") == "gauge":
        if sc.get("tease"): text(img, (W / 2, 790), sc["tease"], 72, th["accent"], a=1.0)
        else: text(img, (W / 2, 800), "?", 120, (110, 120, 150), a=1.0)
    else:
        for k in range(5):
            text(img, (625, 780 + k * 128), "?", 52, (90, 105, 140), a=ease((t - 0.4 - k * 0.15) / 0.3))

def seg_item(img, it, th, t, dur, items):
    a = ease(t / 0.35); acc = tuple(th["accent"])
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle([60, 170, 250, 360], 34, fill=acc + (int(240 * a),)); img.alpha_composite(lay)
    text(img, (155, 268), f"{it['rank']}º", 108, BG1, a=a)
    nm = it["name"]; size = 76
    while F(size, "Black").getlength(nm) > 760 and size > 44: size -= 4
    text(img, (285, 235), nm, size, WHITE, a=a, anchor="lm")
    text(img, (287, 318), it.get("tag", ""), 36, th["accent2"], w="Bold", a=ease((t - 0.3) / 0.4), anchor="lm")
    p = ease((t - 0.4) / 1.4)
    text(img, (W / 2, 500), val_str(it, it["num"] * p), 140, acc, a=ease((t - 0.3) / 0.4))
    text(img, (W / 2, 600), it["unit"], 40, (230, 235, 245), w="Bold", a=ease((t - 0.6) / 0.4))
    chart(img, items, th, it["rank"], t, it["rank"])
    text(img, (W / 2, 1745), "Fonte: " + it["source"], 28, (140, 155, 185), w="SemiBold", a=ease((t - 0.8) / 0.4))

def seg_outro(img, sc, th, t, dur, items):
    chart(img, items, th, 1, 99, -1)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    a = ease(t / 0.5); s = 190; cx, cy = W / 2, 330
    d.rounded_rectangle([cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2], 40, fill=GREEN + (int(255 * a),))
    d.text((cx, cy + 6), "$", font=F(150, "Black"), fill=BG1 + (int(255 * a),), anchor="mm"); img.alpha_composite(lay)
    text(img, (W / 2, 520), "SIGA O CANAL", 90, th["accent"], a=ease((t - 0.4) / 0.5))
    text(img, (W / 2, 610), "Por Trás do Dinheiro", 54, WHITE, w="ExtraBold", a=ease((t - 0.6) / 0.5))
    if sc.get("note"): text(img, (W / 2, 1745), sc["note"], 28, (140, 155, 185), w="SemiBold", a=ease((t - 0.8) / 0.4))

def caption_chunks(say, t0, dur):
    words = say.split(); groups, g = [], []
    for w in words:
        g.append(w)
        if len(g) >= 3 or re.search(r"[.?!,:]$", w): groups.append(" ".join(g)); g = []
    if g: groups.append(" ".join(g))
    total = sum(len(x) for x in groups); t = t0 + 0.15; usable = dur - 0.5; out = []
    for x in groups:
        dd = usable * len(x) / total; out.append((t, t + dd, x.upper().rstrip(".,"))); t += dd
    return out

def draw_caption(img, chunks, gt, y=1585):
    for a, b, s in chunks:
        if a <= gt < b:
            f = F(70, "Black"); lines = wrap(s, f, W - 140); d = ImageDraw.Draw(img)
            for i, l in enumerate(lines):
                d.text((W / 2, y + i * 82 - (len(lines) - 1) * 41), l, font=f, fill=(255, 255, 255), anchor="mm", stroke_width=8, stroke_fill=(0, 0, 0))
            return

def chrome(img, th, gt, total):
    d = ImageDraw.Draw(img)
    d.text((W / 2, 92), th.get("bar", "TOP 5"), font=F(32, "ExtraBold"), fill=(200, 210, 230), anchor="mm")
    d.rectangle([0, 0, int(W * gt / total), 10], fill=tuple(th["accent"]))
    d.text((W / 2, 1690), HANDLE, font=F(34, "Bold"), fill=GREEN, anchor="mm")

def build(m):
    return [("hook", m.HOOK)] + [("item", it) for it in sorted(m.ITEMS, key=lambda x: -x["rank"])] + [("outro", m.OUTRO)]

def tts(segs, outdir, voice):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(R.HERE, "models/kokoro.onnx"), os.path.join(R.HERE, "models/voices.bin"))
    durs, chunks = [], []; speed = float(os.environ.get("SPEED", "1.05"))
    for i, (_, s) in enumerate(segs):
        cache = os.path.join(outdir, f"seg_{i:02d}.wav"); key = f"{voice}|{speed}|{s['say']}"
        if os.path.exists(cache) and open(cache + ".txt").read() == key: a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(s["say"], voice=voice, speed=speed, lang="pt-br"); sf.write(cache, a, sr); open(cache + ".txt", "w").write(key)
        a = np.concatenate([np.zeros(int(sr * 0.1)), a, np.zeros(int(sr * 0.3))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    sf.write(os.path.join(outdir, "voice.wav"), audio, sr)
    return durs

def frame(segs, durs, th, gt, chunks, items):
    total = sum(durs); acc = 0
    for (kind, s), d in zip(segs, durs):
        if gt < acc + d: break
        acc += d
    t = gt - acc; img = bg(th)
    {"hook": seg_hook, "item": seg_item, "outro": seg_outro}[kind](img, s, th, t, d, items)
    chrome(img, th, gt, total); draw_caption(img, chunks, gt)
    if t < 0.2 and gt > 0.5: img = Image.blend(bg(th), img, ease(t / 0.2))
    return img

def main():
    m = load(sys.argv[1]); outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    th = m.THEME; segs = build(m); items = m.ITEMS
    if "--preview" in sys.argv:
        durs = [10.0] * len(segs)
        for i in range(len(segs)):
            frame(segs, durs, th, i * 10 + 6, [], items).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}.jpg"), quality=80)
        print("preview ok"); return
    durs = tts(segs, outdir, os.environ.get("VOICE", "pm_alex"))
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w"))
    total = sum(durs); print("total", round(total, 1), "s", flush=True)
    if "--tts" in sys.argv: return
    chunks = []; acc = 0
    for (_, s), d in zip(segs, durs): chunks += caption_chunks(s["say"], acc, d); acc += d
    out = os.path.join(outdir, "ranking.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voice.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        p.stdin.write(frame(segs, durs, th, f / FPS, chunks, items).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    main()
