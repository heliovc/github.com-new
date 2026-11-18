# Thumbnail EP16 (estilo do thumb_ep07/ep15): à esquerda, a etiqueta de preço da dívida com R$ 1.000 riscado e
# R$ 100 em vermelho (deságio de 90%, o piso do Desenrola 3.0); à direita, a pergunta em 3 linhas e o selo "90% OFF".
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
lay = Image.new("RGBA", t.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(lay)
x0, y0, x1, y1 = 170, 150, 630, 590
R._tag_shape(d2, x0 + 12, y0 + 14, x1 + 12, y1 + 14, (0, 0, 0), 0.5)
hx, hy = R._tag_shape(d2, x0, y0, x1, y1, (238, 226, 196), 1.0)
d2.line([(hx, hy), (hx - 20, 20)], fill=(220, 220, 230, 255), width=5)
t.alpha_composite(lay)
d = ImageDraw.Draw(t)
cx = (x0 + x1) / 2 + 25
d.text((cx, 215), "SUA DÍVIDA", font=F(40, "Black"), fill=(140, 110, 70), anchor="mm")
d.text((cx, 330), "R$ 1.000", font=F(80, "Black"), fill=(125, 125, 140), anchor="mm")
lw = F(80, "Black").getlength("R$ 1.000")
d.line([(cx - lw / 2 - 10, 334), (cx + lw / 2 + 10, 334)], fill=(205, 60, 60), width=12)
d.text((cx, 470), "R$ 100", font=F(112, "Black"), fill=(200, 50, 45), anchor="mm")
d.text((670, 120), "QUEM", font=F(100, "Black"), fill=W_, anchor="lm")
d.text((670, 235), "COMPROU", font=F(100, "Black"), fill=W_, anchor="lm")
d.text((670, 350), "A SUA", font=F(100, "Black"), fill=W_, anchor="lm")
d.text((670, 465), "DÍVIDA?", font=F(112, "Black"), fill=AM, anchor="lm")
d.rounded_rectangle([670, 545, 1100, 635], 22, fill=(70, 30, 34))
d.text((885, 590), "90% OFF", font=F(62, "Black"), fill=(255, 150, 130), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 645))
d.text((112, 675), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
