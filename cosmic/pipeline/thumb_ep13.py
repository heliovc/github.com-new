import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep13"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# highway into space toward a big Neptune, red car from behind + "4,912 YEARS" odometer badge
big = R.background(0.0)
vx, vy = 1300, 560
R.paste_c(big, R.radial(900, [(0, (80, 120, 240, 110)), (1, (80, 120, 240, 0))]), vx, vy - 200)
R.paste_c(big, R.planet_sprite(230, (80, 120, 240), light=(-0.6, -0.4)), vx, vy - 230)
lay = Image.new("RGBA", big.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
dl.polygon([(vx - 20, vy), (vx + 20, vy), (R.W + 900, R.H), (-200, R.H)], fill=(36, 32, 40, 255))
for side in (-1, 1): dl.line([(vx + side * 18, vy), (vx + side * 1100 + (350 if side < 0 else 900) * 0, R.H)], fill=(230, 220, 200, 255), width=8)
for k in range(9):
    z = k / 9; z2 = z + 0.045
    ya, yb = vy + (R.H - vy) * z ** 2.2, vy + (R.H - vy) * min(1, z2) ** 2.2
    xa, xb = vx + (R.W / 2 + 200 - vx) * z ** 2.2, vx + (R.W / 2 + 200 - vx) * min(1, z2) ** 2.2
    wa, wb = 3 + 20 * z ** 2.2, 3 + 20 * min(1, z2) ** 2.2
    dl.polygon([(xa - wa, ya), (xa + wa, ya), (xb + wb, yb), (xb - wb, yb)], fill=(255, 170, 60, 255))
big.alpha_composite(lay)
R._car13(ImageDraw.Draw(big), 1240, 900, 1.25, 0.0)
img = big.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("NEPTUNE", (255, 255, 255), 118, 110), ("BY CAR?", (255, 190, 80), 150, 245)]:
    d.text((356, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="mm")
    d.text((350, y), txt, font=F(sz, "Black"), fill=col, anchor="mm", stroke_width=5, stroke_fill=(10, 10, 25))
d.rounded_rectangle([60, 400, 600, 530], 24, fill=(14, 10, 18), outline=(255, 170, 60), width=6)
d.text((330, 465), "4,912 YEARS", font=F(68, "Black"), fill=(255, 170, 60), anchor="mm")
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=(230, 230, 240), anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
