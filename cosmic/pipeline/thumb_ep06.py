import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep06"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.W, R.H = 1280, 720
t = R.make_starfield(1280, 720, 900, 66).convert("RGBA")
cx, cy, Rg = 930, 400, 300
# globe with grid (no rotation) + speed streaks flying off to the east
R.paste_c(t, R.planet_sprite(Rg, (32, 86, 160), light=(-0.9, -0.4), glow=(110, 190, 255)), cx, cy)
lay = Image.new("RGBA", t.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
for blob in R.land_blobs():
    pp = [R.proj6(la, lo, 40, Rg, cx, cy) for la, lo in blob]
    if all(p[2] > 0.05 for p in pp): dl.polygon([(p[0], p[1]) for p in pp], fill=(70, 140, 85, 210))
for lat in range(-60, 90, 30):
    seg = [(p[0], p[1]) for p in (R.proj6(lat, lo, 0, Rg, cx, cy) for lo in range(-180, 181, 6)) if p[2] > 0]
    dl.line(seg, fill=(150, 220, 255, 120 if lat else 230), width=2 if lat else 4)
t.alpha_composite(lay)
d = ImageDraw.Draw(t)
# a red STOP disc on the globe
d.ellipse([cx - 95, cy - 95, cx + 95, cy + 95], fill=(220, 40, 50), outline=(255, 255, 255), width=8)
d.text((cx, cy + 4), "STOP", font=F(58, "Black"), fill=(255, 255, 255), anchor="mm")
# little houses / person flung east with streaks
for i, (x, y, s) in enumerate([(1180, 230, 1.0), (1215, 470, 0.8), (1150, 600, 0.7)]):
    for k in range(6): d.line([(x - 40 - k * 26, y + k * 3), (x - 90 - k * 26, y + k * 3)], fill=(220, 235, 245), width=3)
    R.house6(d, x, y, s, (220, 160, 110))
# text block, left
for txt, col, sz, y in [("EARTH", (255, 255, 255), 150, 190), ("STOPS.", tuple(R.TEAL6), 150, 340)]:
    d.text((50 + 6, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((50, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.rounded_rectangle([50, 450, 560, 535], 20, fill=R.AMB6)
d.text((305, 492), "YOU DON'T.", font=F(56, "Black"), fill=(25, 15, 5), anchor="mm")
d.text((52, 590), "1,670 km/h", font=F(46, "Black"), fill=(255, 255, 255), anchor="lm")
t.alpha_composite(R.logo_img(56), (40, 640))
d.text((106, 668), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
