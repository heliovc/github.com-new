# Thumbnail EP15 (estilo do thumb_ep07/ep14): à esquerda, o velocímetro do score com o ponteiro na faixa baixa;
# à direita, a tese em 3 linhas e o selo "R$ 5.184 A MAIS" (exemplo ilustrativo do episódio).
import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
cx, cy, r = 320, 470, 270
bands = [(0, 300, RED), (300, 500, AM), (500, 700, R.BLUE), (700, 1000, G)]
for lo, hi, col in bands:
    d.arc([cx - r, cy - r, cx + r, cy + r], 180 + 180 * lo / 1000 + 0.8, 180 + 180 * hi / 1000 - 0.8, fill=col, width=60)
ang = math.radians(180 + 180 * 230 / 1000)
d.line([(cx, cy), (cx + 225 * math.cos(ang), cy + 225 * math.sin(ang))], fill=W_, width=16)
d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill=W_)
d.text((cx, cy - 110), "SCORE", font=F(46, "Black"), fill=(200, 210, 230), anchor="mm")
d.text((cx, cy + 90), "?", font=F(120, "Black"), fill=RED, anchor="mm")
d.text((660, 120), "QUEM DÁ", font=F(96, "Black"), fill=W_, anchor="lm")
d.text((660, 235), "A SUA NOTA", font=F(96, "Black"), fill=W_, anchor="lm")
d.text((660, 350), "DECIDE O", font=F(96, "Black"), fill=W_, anchor="lm")
d.text((660, 465), "SEU JURO", font=F(110, "Black"), fill=AM, anchor="lm")
d.rounded_rectangle([660, 545, 1230, 635], 22, fill=(70, 30, 34))
d.text((945, 590), "R$ 5.184 A MAIS", font=F(58, "Black"), fill=(255, 150, 130), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 645))
d.text((112, 675), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
