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
# trajetória de voo que despenca, ao fundo
pts = [(30, 300), (170, 190), (320, 110), (440, 80), (530, 120), (650, 700)]
d.line(pts[:5], fill=(91, 141, 239), width=12, joint="curve")
d.line(pts[4:], fill=(224, 70, 60), width=12)
# caixa-preta laranja
OR = (240, 128, 30)
box = Image.new("RGBA", (460, 330), (0, 0, 0, 0)); b = ImageDraw.Draw(box)
b.rounded_rectangle([0, 0, 460, 330], 30, fill=OR)
for k in range(0, 460, 60):
    b.polygon([(k, 270), (k + 32, 270), (k + 14, 330), (k - 18, 330)], fill=(30, 30, 30))
b.text((230, 70), "CAIXA-PRETA", font=F(48, "Black"), fill=(30, 22, 12), anchor="mm")
b.rounded_rectangle([40, 120, 420, 240], 18, fill=(30, 22, 12))
b.text((230, 180), "MASTER", font=F(76, "Black"), fill=OR, anchor="mm")
box = box.rotate(7, expand=True, resample=Image.BICUBIC)
t.alpha_composite(box, (40, 330))
d = ImageDraw.Draw(t)
d = ImageDraw.Draw(t)
d.text((955, 150), "QUEM PAGOU", font=F(80, "Black"), fill=W_, anchor="mm")
d.text((955, 255), "R$ 40", font=F(150, "Black"), fill=AM, anchor="mm")
d.text((955, 375), "BILHÕES?", font=F(96, "Black"), fill=AM, anchor="mm")
d.rounded_rectangle([735, 455, 1175, 535], 20, fill=(70, 30, 34))
d.text((955, 495), "BANCO MASTER", font=F(52, "Black"), fill=(255, 140, 120), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (760, 620))
d.text((832, 650), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
