import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep18"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# Jupiter fills the right side; a tiny glowing capsule falls toward it; a dashed depth line runs down into the planet
img = R.background(0.0); W, H = img.size
R.paste_c(img, R.jup18(900), W * 0.80, H * 0.62)
d = ImageDraw.Draw(img)
x0, y0 = W * 0.80 - 900 * math.cos(math.radians(55)) * 0.35, 130
for k in range(16):
    y = 300 + k * 48; d.line([(1330, y), (1330, y + 26)], fill=(255, 255, 255), width=8)
R.paste_c(img, R.radial(140, [(0, (255, 240, 200, 255)), (0.25, (255, 150, 60, 220)), (1, (255, 80, 20, 0))]), 1330, 220)
R._capsule18(img, 1330, 220, 2.2, glow=0.0, ang=0.0)
img = img.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("NO", (255, 255, 255), 170, 300), ("GROUND", (255, 190, 100), 150, 470)]:
    d.text((58, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((50, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=7, stroke_fill=(10, 10, 25))
d.text((54, 610), "70,000 KM DOWN", font=F(60, "Black"), fill=(255, 255, 255), anchor="lm", stroke_width=6, stroke_fill=(0, 0, 0))
img.convert("RGB").save(os.path.join(OUT, "thumbnail.jpg"), quality=92)
print("ok")
