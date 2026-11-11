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
# cartão de crédito genérico, inclinado, com "fogo" de juros
card = Image.new("RGBA", (520, 330), (0, 0, 0, 0)); c = ImageDraw.Draw(card)
c.rounded_rectangle([0, 0, 520, 330], 34, fill=(150, 36, 40))
c.rounded_rectangle([0, 0, 520, 330], 34, outline=(255, 120, 100), width=6)
c.rounded_rectangle([50, 95, 140, 165], 12, fill=(230, 190, 100))
for k in range(4): c.text((60 + k * 112, 225), "••••", font=F(40, "Black"), fill=(255, 220, 210))
c.text((470, 60), "CRÉDITO", font=F(34, "Black"), fill=(255, 210, 200), anchor="rm")
card = card.rotate(-12, expand=True, resample=Image.BICUBIC)
t.alpha_composite(card, (40, 220))
d = ImageDraw.Draw(t)
# setas de juros subindo
for i, (x, y, s) in enumerate([(520, 190, 70), (585, 120, 85), (440, 140, 60)]):
    d.polygon([(x, y - s), (x - s * 0.6, y), (x + s * 0.6, y)], fill=(255, 90, 70))
    d.rectangle([x - s * 0.22, y, x + s * 0.22, y + s * 0.9], fill=(255, 90, 70))
d.text((960, 140), "JURO DE", font=F(84, "Black"), fill=W_, anchor="mm")
d.text((960, 290), "451%", font=F(210, "Black"), fill=AM, anchor="mm")
d.text((960, 430), "AO ANO", font=F(84, "Black"), fill=AM, anchor="mm")
d.rounded_rectangle([730, 500, 1190, 580], 20, fill=(70, 30, 34))
d.text((960, 540), "QUEM GANHA?", font=F(56, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 630))
d.text((112, 660), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
