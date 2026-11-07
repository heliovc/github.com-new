import sys; sys.path.insert(0, "/home/claude/canal")
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

def pos(d, x, y, w, h, body, scr, txt, tcol, rot=0):
    d.rounded_rectangle([x, y, x + w, y + h], 34, fill=body, outline=tuple(min(255, c + 40) for c in body), width=5)
    d.rounded_rectangle([x + 22, y + 26, x + w - 22, y + h * 0.42], 16, fill=scr)
    d.text((x + w / 2, y + h * 0.24), txt, font=F(int(w * 0.24), "Black"), fill=tcol, anchor="mm")
    for r in range(3):
        for c in range(3):
            cx, cy = x + w * (0.25 + c * 0.25), y + h * (0.55 + r * 0.13)
            d.rounded_rectangle([cx - w * 0.09, cy - h * 0.04, cx + w * 0.09, cy + h * 0.04], 8, fill=tuple(min(255, k + 25) for k in body))

old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
d = ImageDraw.Draw(t)
# ringue: cordas
for i, yy in enumerate((150, 215, 280)):
    d.line([(640, yy), (1280, yy - 40)], fill=(150, 60, 60) if i != 1 else (220, 220, 230), width=8)
# três maquininhas, a do meio caída (desenhada em camada rotacionada)
d.rectangle([600, 640, 1280, 720], fill=(16, 26, 44))
pos(d, 760, 300, 170, 320, (36, 96, 70), (12, 30, 24), "2,11%", G)
pos(d, 1070, 280, 180, 350, (40, 60, 110), (12, 20, 40), "Pix", (120, 200, 255))
lay = Image.new("RGBA", (360, 220), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
dl.rounded_rectangle([10, 10, 350, 200], 30, fill=(110, 70, 30), outline=(150, 100, 50), width=5)
dl.rounded_rectangle([30, 30, 200, 190], 14, fill=(40, 20, 10))
dl.text((115, 110), "2,99%", font=F(44, "Black"), fill=RED, anchor="mm")
lay = lay.rotate(-12, expand=True, resample=Image.BICUBIC)
t.alpha_composite(lay, (880, 475))
d = ImageDraw.Draw(t)
# d.text((960, 690), "K.O.", font=F(46, "Black"), fill=RED, anchor="mm")

d.text((50, 105), "GUERRA DAS", font=F(64, "Black"), fill=W_, anchor="lm")
d.text((50, 180), "MAQUININHAS", font=F(64, "Black"), fill=W_, anchor="lm")
d.text((44, 340), "QUEM", font=F(150, "Black"), fill=AM, anchor="lm")
d.text((44, 480), "GANHOU?", font=F(124, "Black"), fill=AM, anchor="lm")
lg = logo(84); t.alpha_composite(lg, (50, 600))
d.text((150, 642), "POR TRÁS DO DINHEIRO", font=F(30, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1])
print("ok")
