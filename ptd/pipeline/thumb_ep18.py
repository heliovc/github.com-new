# Thumbnail EP18 (estilo do thumb_ep07/ep17): à esquerda, a casa da vistoria (cena "house") com os cômodos fechados em "?"
# e o cofre aceso com um cadeado; à direita, a frase em 3 linhas ("O BANCO / QUE NINGUÉM / CONHECE") e o selo "SALDO SEM FGC"
# (conta de pagamento não tem cobertura do FGC — FGC / imprensa, caso Will Bank, jan/2026).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM, RED = R.GREEN, R.BG1, R.WHITE, R.AMBER, R.RED
F = R.F
def logo(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    m = size * 0.14; s = size - 2 * m
    d.rounded_rectangle([m, m, m + s, m + s], int(s * 0.22), fill=G)
    d.text((size / 2, size / 2 + size * 0.02), "$", font=F(int(size * 0.62), "Black"), fill=BG1, anchor="mm")
    return img
old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
d = ImageDraw.Draw(t)
EDGE, OFF = (110, 125, 150), (26, 36, 56)
x0, y0, w, h = 70, 230, 470, 400
d.polygon([(x0 - 35, y0), (x0 + w / 2, y0 - 160), (x0 + w + 35, y0)], fill=(70, 50, 120), outline=EDGE)
rel = [(0, 0.66, 1, 1), (0, 0.33, 0.5, 0.66), (0.5, 0.33, 1, 0.66), (0, 0, 0.5, 0.33), (0.5, 0, 1, 0.33)]
for i, (a, b, c, e) in enumerate(rel):
    rx0, ry0, rx1, ry1 = x0 + a * w, y0 + b * h, x0 + c * w, y0 + e * h
    lit = i == 2
    d.rectangle([rx0, ry0, rx1, ry1], fill=AM if lit else OFF, outline=EDGE, width=5)
    cx, cy = (rx0 + rx1) / 2, (ry0 + ry1) / 2
    if lit:  # cadeado
        d.arc([cx - 30, cy - 62, cx + 30, cy - 2], 180, 360, fill=BG1, width=12)
        d.rounded_rectangle([cx - 44, cy - 32, cx + 44, cy + 40], 10, fill=BG1)
        d.ellipse([cx - 9, cy - 6, cx + 9, cy + 12], fill=AM)
    else:
        d.text((cx, cy), "?", font=F(70, "Black"), fill=(120, 135, 160), anchor="mm")
d.text((610, 130), "O BANCO", font=F(104, "Black"), fill=W_, anchor="lm")
d.text((610, 250), "QUE NINGUÉM", font=F(82, "Black"), fill=W_, anchor="lm")
d.text((610, 370), "CONHECE", font=F(104, "Black"), fill=AM, anchor="lm")
d.rounded_rectangle([610, 465, 1190, 565], 22, fill=(70, 30, 34))
d.text((900, 515), "SALDO SEM FGC", font=F(62, "Black"), fill=(255, 150, 130), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 645))
d.text((112, 675), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
