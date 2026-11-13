import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM = R.GREEN, R.BG1, R.WHITE, R.AMBER
F = R.F
def logo(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    m = size * 0.14; s = size - 2 * m
    d.rounded_rectangle([m, m, m + s, m + s], int(s * 0.22), fill=G)
    d.text((size / 2, size / 2 + size * 0.02), "$", font=F(int(size * 0.62), "Black"), fill=BG1, anchor="mm")
    return img
old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
# contracheque genérico, inclinado, com a linha do consignado marcada em amarelo e carimbo
rc = Image.new("RGBA", (520, 500), (0, 0, 0, 0)); c = ImageDraw.Draw(rc)
c.rounded_rectangle([0, 0, 520, 480], 24, fill=(244, 242, 236))
for zx in range(10, 510, 30): c.polygon([(zx, 480), (zx + 15, 498), (zx + 30, 480)], fill=(244, 242, 236))
c.text((260, 58), "CONTRACHEQUE", font=F(44, "Black"), fill=(20, 30, 48), anchor="mm")
rows = [("Salário", "2.500,00", (20, 30, 48), None), ("CONSIGNADO", "- 235,50", (20, 30, 48), (255, 222, 70)),
        ("CONSIGNADO", "- 235,50", (20, 30, 48), (255, 222, 70)), ("Cai na conta", "2.029,00", (30, 150, 90), None)]
for i, (a, b, col, hl) in enumerate(rows):
    y = 150 + i * 88
    if hl: c.rectangle([18, y - 34, 502, y + 34], fill=hl)
    c.text((36, y), a, font=F(38, "Bold"), fill=col, anchor="lm")
    c.text((484, y), b, font=F(40, "Black"), fill=col, anchor="rm")
rc = rc.rotate(7, expand=True, resample=Image.BICUBIC)
t.alpha_composite(rc, (25, 55))
st = Image.new("RGBA", (440, 120), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
ds.rounded_rectangle([6, 6, 434, 114], 14, fill=(232, 244, 236, 250), outline=(30, 150, 90, 255), width=9)
ds.text((220, 62), "O BANCO RECEBE", font=F(44, "Black"), fill=(30, 150, 90, 240), anchor="mm")
st = st.rotate(-12, expand=True, resample=Image.BICUBIC)
t.alpha_composite(st, (70, 450))
d = ImageDraw.Draw(t)
d.text((945, 120), "CONSIGNADO", font=F(84, "Black"), fill=W_, anchor="mm")
d.text((945, 300), "R$ 770 BI", font=F(132, "Black"), fill=AM, anchor="mm")
d.rounded_rectangle([700, 420, 1190, 510], 20, fill=(30, 70, 50))
d.text((945, 465), "QUEM GANHA?", font=F(58, "Black"), fill=(120, 230, 160), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 630))
d.text((112, 660), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
