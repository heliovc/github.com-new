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
# cortinas de palco nas bordas
for x0, x1 in ((0, 70), (1210, 1280)):
    k = 0; xx = x0
    while xx < x1:
        d.rectangle([xx, 0, xx + 18, 720], fill=(150, 28, 42) if k % 2 == 0 else (96, 12, 22)); xx += 35; k += 1
# folha de balanço inclinada à esquerda
card = Image.new("RGBA", (560, 470), (0, 0, 0, 0)); c = ImageDraw.Draw(card)
paper, ink, ink2 = (236, 240, 246), (20, 30, 48), (95, 105, 125)
c.rounded_rectangle([0, 0, 560, 470], 18, fill=paper)
c.rectangle([0, 0, 560, 70], fill=(34, 48, 74))
c.text((28, 35), "BALANÇO", font=F(36, "Black"), fill=paper, anchor="lm")
c.text((28, 140), "Lucro", font=F(44, "Bold"), fill=ink2, anchor="lm")
c.text((532, 140), "R$ ???", font=F(52, "Black"), fill=ink, anchor="rm")
c.text((28, 245), "Dívida", font=F(44, "Bold"), fill=ink2, anchor="lm")
c.text((532, 245), "R$ ???", font=F(52, "Black"), fill=ink, anchor="rm")
c.line([(28, 310), (532, 310)], fill=(200, 205, 215), width=3)
c.text((28, 390), "Fornecedores", font=F(44, "Bold"), fill=ink2, anchor="lm")
st = Image.new("RGBA", (440, 150), (0, 0, 0, 0)); s = ImageDraw.Draw(st)
s.rounded_rectangle([8, 8, 432, 142], 16, outline=(200, 40, 40, 240), width=11)
s.text((220, 77), "FRAUDE", font=F(96, "Black"), fill=(200, 40, 40, 240), anchor="mm")
st = st.rotate(-14, expand=True, resample=Image.BICUBIC)
card.alpha_composite(st, (70, 120))
card = card.rotate(5, expand=True, resample=Image.BICUBIC)
t.alpha_composite(card, (75, 110))
d = ImageDraw.Draw(t)
d.text((945, 170), "R$ 25", font=F(150, "Black"), fill=AM, anchor="mm")
d.text((945, 290), "BILHÕES", font=F(92, "Black"), fill=AM, anchor="mm")
d.text((945, 410), "ESCONDIDOS", font=F(78, "Black"), fill=W_, anchor="mm")
d.rounded_rectangle([735, 480, 1155, 560], 20, fill=(70, 30, 34))
d.text((945, 520), "AMERICANAS", font=F(52, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (760, 620))
d.text((832, 650), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1]); print("ok")
