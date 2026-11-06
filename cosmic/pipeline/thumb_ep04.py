import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep04"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.W, R.H = 1280, 720
t = R.make_starfield(1280, 720, 900, 41).convert("RGBA")
R.draw_bh(t, 360, 380, 110, 0.0)
R.draw_astro(t, 410, 290, 0.42, sx=0.7, sy=1.8, rot=60)
d = ImageDraw.Draw(t)
for i, (txt, col, sz) in enumerate([("66", R.EMBER, 230), ("SECONDS", (255, 255, 255), 104), ("LEFT", R.PALE, 104)]):
    y = [190, 360, 470][i]
    d.text((1236 + 6, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="rm")
    d.text((1236, y), txt, font=F(sz, "Black"), fill=col, anchor="rm")
d.rounded_rectangle([760, 560, 1240, 630], 18, fill=R.EMBER)
d.text((1000, 595), "INSIDE A BLACK HOLE", font=F(40, "Black"), fill=(20, 8, 4), anchor="mm")
t.alpha_composite(R.logo_img(64), (36, 630))
d.text((110, 662), "COSMIC SCALE", font=F(26, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
