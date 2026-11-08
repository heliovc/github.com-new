import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM, DIM, RED = R.GREEN, R.BG1, R.WHITE, R.AMBER, R.DIM, R.RED
F = R.F
def logo(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    m = size * 0.14; s = size - 2 * m
    d.rounded_rectangle([m, m, m + s, m + s], int(s * 0.22), fill=G)
    d.text((size / 2, size / 2 + size * 0.02), "$", font=F(int(size * 0.62), "Black"), fill=BG1, anchor="mm")
    return img
old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
# ficha de autópsia inclinada à esquerda
card = Image.new("RGBA", (560, 600), (0, 0, 0, 0)); c = ImageDraw.Draw(card)
paper, ink, ink2 = (232, 228, 214), (28, 30, 40), (110, 105, 95)
c.rounded_rectangle([0, 0, 560, 600], 18, fill=paper)
c.rectangle([0, 0, 560, 80], fill=(40, 44, 58))
c.text((30, 40), "FICHA DE AUTÓPSIA", font=F(34, "Black"), fill=paper, anchor="lm")
c.text((30, 140), "VÍTIMA", font=F(24, "Bold"), fill=ink2, anchor="lm")
c.text((30, 215), "DOC", font=F(110, "Black"), fill=ink, anchor="lm")
c.text((30, 320), "1985 – 2024", font=F(46, "ExtraBold"), fill=ink, anchor="lm")
c.text((30, 400), "CAUSA", font=F(24, "Bold"), fill=ink2, anchor="lm")
c.text((30, 450), "o Pix", font=F(54, "ExtraBold"), fill=ink, anchor="lm")
st = Image.new("RGBA", (420, 150), (0, 0, 0, 0)); s = ImageDraw.Draw(st)
s.rounded_rectangle([8, 8, 412, 142], 16, outline=(200, 40, 40, 235), width=11)
s.text((210, 77), "MORTO", font=F(100, "Black"), fill=(200, 40, 40, 235), anchor="mm")
st = st.rotate(-14, expand=True, resample=Image.BICUBIC)
card.alpha_composite(st, (150, 330))
card = card.rotate(5, expand=True, resample=Image.BICUBIC)
t.alpha_composite(card, (20, 40))
d = ImageDraw.Draw(t)
# direita
d.text((960, 190), "PIX", font=F(200, "Black"), fill=G, anchor="mm")
d.text((960, 345), "QUEM ELE", font=F(84, "Black"), fill=W_, anchor="mm")
d.text((960, 440), "MATOU?", font=F(110, "Black"), fill=AM, anchor="mm")
d.rounded_rectangle([745, 530, 1175, 610], 20, fill=(70, 30, 34))
d.text((960, 570), "bancos: −R$ 1,5 bi", font=F(44, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(64); t.alpha_composite(lg, (700, 640))
d.text((776, 672), "POR TRÁS DO DINHEIRO", font=F(28, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1]); print("ok")
