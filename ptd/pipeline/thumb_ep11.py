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
# extrato de benefício genérico, inclinado, com a linha do desconto em vermelho e carimbo
rc = Image.new("RGBA", (500, 470), (0, 0, 0, 0)); c = ImageDraw.Draw(rc)
c.rounded_rectangle([0, 0, 500, 450], 24, fill=(238, 240, 246))
for zx in range(10, 490, 30): c.polygon([(zx, 450), (zx + 15, 468), (zx + 30, 450)], fill=(238, 240, 246))
c.text((250, 56), "BENEFÍCIO", font=F(44, "Black"), fill=(20, 30, 48), anchor="mm")
for i, (a, b, col) in enumerate([("Benefício", "1.518,00", (20, 30, 48)), ("DESCONTO", "- 45,00", (214, 50, 44)), ("DESCONTO", "- 45,00", (214, 50, 44))]):
    y = 150 + i * 92
    if col != (20, 30, 48): c.rectangle([20, y - 36, 480, y + 36], fill=(252, 222, 218))
    c.text((36, y), a, font=F(38, "Bold"), fill=col, anchor="lm")
    c.text((464, y), b, font=F(40, "Black"), fill=col, anchor="rm")
rc = rc.rotate(8, expand=True, resample=Image.BICUBIC)
t.alpha_composite(rc, (30, 60))
st = Image.new("RGBA", (420, 120), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
ds.rounded_rectangle([6, 6, 414, 114], 14, fill=(255, 236, 232, 250), outline=(214, 50, 44, 255), width=9)
ds.text((210, 62), "SEM AUTORIZAÇÃO", font=F(42, "Black"), fill=(214, 50, 44, 240), anchor="mm")
st = st.rotate(-14, expand=True, resample=Image.BICUBIC)
t.alpha_composite(st, (70, 395))
d = ImageDraw.Draw(t)
d.text((930, 120), "O GOLPE", font=F(80, "Black"), fill=W_, anchor="mm")
d.text((930, 210), "DO INSS", font=F(80, "Black"), fill=W_, anchor="mm")
d.text((930, 360), "R$ 6,3 BI", font=F(150, "Black"), fill=AM, anchor="mm")
d.rounded_rectangle([690, 470, 1170, 560], 20, fill=(70, 30, 34))
d.text((930, 515), "QUEM DEVOLVEU?", font=F(54, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 630))
d.text((112, 660), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
