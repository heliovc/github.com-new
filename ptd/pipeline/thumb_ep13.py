import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM = R.GREEN, R.BG1, R.WHITE, R.AMBER
F = R.F
PURP = (130, 10, 209)
def logo(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    m = size * 0.14; s = size - 2 * m
    d.rounded_rectangle([m, m, m + s, m + s], int(s * 0.22), fill=G)
    d.text((size / 2, size / 2 + size * 0.02), "$", font=F(int(size * 0.62), "Black"), fill=BG1, anchor="mm")
    return img
old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
# prédio roxo genérico de 5 andares (sem marca), com o 4º andar aceso e uma rachadura na base
b = Image.new("RGBA", (470, 600), (0, 0, 0, 0)); c = ImageDraw.Draw(b)
c.polygon([(10, 110), (235, 20), (460, 110)], fill=PURP)
c.text((235, 80), "BANCO", font=F(46, "Black"), fill=(255, 255, 255), anchor="mm")
for i in range(5):
    y1 = 120 + i * 90
    col = AM if i == 1 else (54, 30, 90)
    c.rectangle([30, y1, 440, y1 + 82], fill=col, outline=(120, 90, 170), width=3)
    for k in range(5):
        wx = 60 + k * 76
        c.rectangle([wx, y1 + 22, wx + 44, y1 + 60], fill=(255, 236, 170) if i == 1 else (90, 70, 130))
c.line([(120, 572), (160, 530), (140, 500), (190, 460), (175, 430)], fill=(240, 70, 60), width=9)
c.rectangle([0, 570, 470, 590], fill=(90, 100, 130))
t.alpha_composite(b, (40, 70))
d = ImageDraw.Draw(t)
d.text((905, 110), "NUBANK", font=F(96, "Black"), fill=W_, anchor="mm")
d.text((905, 215), "VIROU BANCO", font=F(82, "Black"), fill=(190, 140, 255), anchor="mm")
d.text((905, 360), "US$ 1,1 BI", font=F(124, "Black"), fill=AM, anchor="mm")
d.text((905, 445), "de lucro em 3 meses", font=F(40, "Bold"), fill=W_, anchor="mm")
d.rounded_rectangle([630, 500, 1180, 590], 20, fill=(110, 30, 30))
d.text((905, 545), "E A RACHADURA?", font=F(56, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 640))
d.text((112, 670), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
