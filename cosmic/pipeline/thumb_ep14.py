import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep14"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# cross-section to scale: a 10 km rock resting on the seafloor, still towering out of a 3.7 km ocean; big words at left
big = R.background(0.0)
R.sc_oceancut(big, {"d_m": 10000, "view_km": 14, "mode": "drop", "x": 1380, "bare": True, "hot": 0.0}, 3.0, 2.0)
img = big.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
d.rectangle([0, 0, 1280, 60], fill=(5, 7, 15))
for txt, col, sz, y in [("THE OCEAN IS", (255, 255, 255), 84, 120), ("TOO SHALLOW", (255, 140, 50), 112, 225)]:
    d.text((44, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((40, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=5, stroke_fill=(10, 10, 25))
d.rounded_rectangle([40, 320, 470, 420], 20, fill=(8, 16, 34), outline=(40, 205, 195), width=5)
d.text((255, 370), "10 km rock", font=F(54, "Black"), fill=(255, 255, 255), anchor="mm")
d.text((60, 575), "ocean: 3.7 km deep", font=F(44, "Black"), fill=(255, 255, 255), anchor="lm", stroke_width=4, stroke_fill=(6, 24, 52))
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=(230, 230, 240), anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
