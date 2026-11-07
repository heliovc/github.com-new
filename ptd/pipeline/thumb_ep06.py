import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM, DIM, RED, BLUE = R.GREEN, R.BG1, R.WHITE, R.AMBER, R.DIM, R.RED, R.BLUE
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
# agenda de 12 parcelas à esquerda (3 col x 4 lin), as da direita "voando" para fora
cw, ch, gx, gy = 150, 104, 40, 150
for i in range(12):
    c, r = i % 3, i // 3
    x, y = gx + c * (cw + 14), gy + r * (ch + 14)
    k = i / 11
    fill = R.mix((36, 56, 92), (18, 26, 44), k * 0.6)
    d.rounded_rectangle([x, y, x + cw, y + ch], 16, fill=fill, outline=R.mix(BLUE, (60, 70, 90), k), width=4)
    d.text((x + cw / 2, y + 30), f"mês {i+1}", font=F(22, "Bold"), fill=DIM, anchor="mm")
    d.text((x + cw / 2, y + 70), "R$ 97", font=F(38, "Black"), fill=W_, anchor="mm")
# seta das parcelas para o "hoje"
d.polygon([(560, 330), (640, 390), (560, 450)], fill=AM)
d.rectangle([520, 370, 562, 410], fill=AM)
d.text((40, 85), "12x SEM JUROS", font=F(46, "Black"), fill=G, anchor="lm")
# números à direita
d.text((960, 175), "R$ 1.200", font=F(110, "Black"), fill=(150, 160, 185), anchor="mm")
d.line([(735, 180), (1185, 165)], fill=RED, width=12)
d.text((960, 345), "R$ 1.013", font=F(150, "Black"), fill=AM, anchor="mm")
d.text((960, 470), "QUEM FICA", font=F(76, "Black"), fill=W_, anchor="mm")
d.text((960, 555), "COM O RESTO?", font=F(76, "Black"), fill=W_, anchor="mm")
lg = logo(70); t.alpha_composite(lg, (40, 630))
d.text((122, 665), "POR TRÁS DO DINHEIRO", font=F(28, "Bold"), fill=G, anchor="lm")
d.text((1240, 690), "exemplo ilustrativo", font=F(22, "SemiBold"), fill=DIM, anchor="rm")
t.convert("RGB").save(sys.argv[1]); print("ok")
