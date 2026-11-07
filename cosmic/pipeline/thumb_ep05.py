import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep05"); os.makedirs(OUT, exist_ok=True)
F = R.F
t = R.make_starfield(1280, 720, 900, 55).convert("RGBA")
R.draw_giant(t, 1090, 380, 470, "rsg")
d = ImageDraw.Draw(t)
sx, sy = 560, 600
R.paste_c(t, R.sun_sprite(4), sx, sy)
d = ImageDraw.Draw(t)
d.ellipse([sx - 16, sy - 16, sx + 16, sy + 16], outline=R.GOLD, width=3)
d.line([(sx, sy + 20), (sx, sy + 52)], fill=R.GOLD, width=3)
d.text((sx, sy + 78), "OUR SUN", font=F(30, "Black"), fill=R.GOLD, anchor="mm")
for i, (txt, col, sz) in enumerate([("2,000×", R.RSGC, 190), ("BIGGER THAN", (255, 255, 255), 78), ("THE SUN", R.MINT, 104)]):
    y = [150, 290, 385][i]
    d.text((48 + 6, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((48, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.rounded_rectangle([48, 470, 470, 532], 16, fill=R.RSGC)
d.text((259, 501), "THE LARGEST STAR", font=F(36, "Black"), fill=(255, 255, 255), anchor="mm")
t.alpha_composite(R.logo_img(56), (40, 640))
d.text((106, 668), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
