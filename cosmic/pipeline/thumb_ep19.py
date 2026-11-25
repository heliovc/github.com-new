import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep19"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# EP19: a huge twin Moon rising over the mesas next to our small Moon; bold "2 MOONS" + "SAME TIDES?"
img = R.background(0.0); W, H = img.size
R._land19(img, 0.75)
R.paste_c(img, R.radial(1400, [(0, (230, 225, 255, 120)), (0.3, (190, 180, 255, 40)), (1, (120, 110, 200, 0))]), 1430, 430)
R.paste_c(img, R._sized19(330, -1), 1430, 430)
R.paste_c(img, R.radial(300, [(0, (230, 225, 255, 120)), (1, (120, 110, 200, 0))]), 1020, 170)
R.paste_c(img, R.moon19(48), 1020, 170)
d = ImageDraw.Draw(img)
img = img.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("2 MOONS", (255, 255, 255), 150, 250), ("SAME TIDES?", (255, 190, 100), 104, 420)]:
    d.text((56, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((48, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=7, stroke_fill=(10, 10, 25))
d.text((52, 560), "5 ORBITS TESTED", font=F(54, "Black"), fill=(140, 230, 220), anchor="lm", stroke_width=6, stroke_fill=(0, 0, 0))
img.convert("RGB").save(os.path.join(OUT, "thumbnail.jpg"), quality=92)
print("ok")
