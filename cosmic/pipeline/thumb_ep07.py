import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import render as R
OUT = os.path.join(R.HERE, "out/ep07"); os.makedirs(OUT, exist_ok=True)
F = R.F
t = R.make_starfield(1280, 720, 900, 77).convert("RGBA")
d = ImageDraw.Draw(t)
# balance: pivot at (760, 300); beam tilted down to the LEFT (spoon side heavy)
px, py, L, ang = 690, 340, 340, math.radians(-16)
lx, ly = px - L * math.cos(ang), py - L * math.sin(ang) * -1
lx, ly = px - L * math.cos(ang), py + L * math.sin(-ang)
rx, ry = px + L * math.cos(ang), py - L * math.sin(-ang)
d.polygon([(px - 60, 690), (px + 60, 690), (px + 12, py), (px - 12, py)], fill=(120, 130, 160))
d.line([(lx, ly), (rx, ry)], fill=(210, 215, 230), width=14)
d.ellipse([px - 22, py - 22, px + 22, py + 22], fill=(255, 111, 145))
for (x, y) in ((lx, ly), (rx, ry)):
    d.line([(x, y), (x - 110, y + 150)], fill=(180, 185, 200), width=4); d.line([(x, y), (x + 110, y + 150)], fill=(180, 185, 200), width=4)
    d.chord([x - 150, y + 100, x + 150, y + 210], 0, 180, fill=(170, 176, 196))
# left pan: spoon with glowing matter
R.draw_spoon(d, lx - 30, ly + 125, 0.45)
R.paste_c(t, R.ns(34), lx - 30, ly + 122)
d = ImageDraw.Draw(t)
# right pan: crowd of tiny people
rng = random.Random(3)
for i in range(40):
    x = rx - 105 + (i % 10) * 23 + rng.uniform(-3, 3); y = ry + 150 - (i // 10) * 30
    c = (255, 111, 145) if i % 3 else (255, 200, 210)
    d.ellipse([x - 5, y - 26, x + 5, y - 16], fill=c); d.rounded_rectangle([x - 6, y - 15, x + 6, y + 2], 4, fill=c)
d.text((rx, ry - 30), "8 BILLION PEOPLE", font=F(30, "Black"), fill=(255, 200, 210), anchor="mm")
# text, left top
for txt, col, sz, y in [("1 TEASPOON", (255, 255, 255), 104, 90)]:
    d.text((44 + 5, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((44, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.rounded_rectangle([44, 160, 520, 250], 20, fill=(91, 140, 255))
d.text((282, 205), "WINS.", font=F(70, "Black"), fill=(255, 255, 255), anchor="mm")
d.text((48, 300), "of a neutron star", font=F(40, "Bold"), fill=(200, 220, 255), anchor="lm")
t.alpha_composite(R.logo_img(56), (40, 640))
d.text((106, 668), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
