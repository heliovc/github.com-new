import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep11"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# the ring arch over a city at dusk, computed in 3D (same as the ringsky scene), no info box
big = R.background(0.0)
R.sc_ringsky(big, {"lat": 22, "mode": "dusk", "elev": 22, "fov": 112}, 6.0, 8.0)
ImageDraw.Draw(big).rectangle([0, 840, 1920, 1080], fill=(8, 9, 16))
img = big.resize((1280, 720), Image.LANCZOS)
d = ImageDraw.Draw(img)
for txt, col, sz, y in [("EARTH", (255, 255, 255), 128, 90), ("WITH RINGS", (255, 150, 170), 112, 205)]:
    d.text((646, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="mm")
    d.text((640, y), txt, font=F(sz, "Black"), fill=col, anchor="mm", stroke_width=5, stroke_fill=(10, 10, 25))
d.rounded_rectangle([410, 280, 870, 350], 18, fill=(20, 22, 50))
d.text((640, 315), "FROM YOUR STREET", font=F(40, "Black"), fill=(255, 255, 255), anchor="mm")
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=(230, 230, 240), anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
