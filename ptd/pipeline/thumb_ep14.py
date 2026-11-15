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
# a cebola do juro: corte com 5 camadas, a do calote acesa, e um "%" no miolo
on = Image.new("RGBA", (560, 560), (0, 0, 0, 0)); c = ImageDraw.Draw(on)
cols = [(52, 70, 104), (242, 169, 59), (74, 52, 88), (86, 48, 76), (58, 196, 125)]
for i, r in enumerate([270, 222, 174, 126, 78]):
    c.ellipse([280 - r, 280 - r, 280 + r, 280 + r], fill=cols[i], outline=BG1, width=6)
c.text((280, 286), "%", font=F(96, "Black"), fill=BG1, anchor="mm")
c.text((280, 34), "CUSTO", font=F(26, "Black"), fill=(200, 210, 230), anchor="mm")
c.text((280, 82), "CALOTE", font=F(30, "Black"), fill=BG1, anchor="mm")
t.alpha_composite(on, (30, 90))
d = ImageDraw.Draw(t)
# direita: o paradoxo
d.text((640, 120), "SELIC", font=F(92, "Black"), fill=W_, anchor="lm")
d.text((930, 120), "CAIU", font=F(92, "Black"), fill=G, anchor="lm")
d.polygon([(1205, 85), (1255, 85), (1230, 150)], fill=G)
d.text((640, 250), "SEU JURO", font=F(92, "Black"), fill=W_, anchor="lm")
d.text((640, 360), "SUBIU", font=F(120, "Black"), fill=RED, anchor="lm")
d.polygon([(1040, 395), (1100, 395), (1070, 320)], fill=RED)
d.rounded_rectangle([640, 460, 1220, 560], 22, fill=(70, 30, 34))
d.text((930, 510), "49% AO ANO", font=F(64, "Black"), fill=(255, 150, 130), anchor="mm")
d.text((930, 610), "o spread, explicado", font=F(40, "Bold"), fill=AM, anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 645))
d.text((112, 675), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
