import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep15"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# Voyager big on the right, a green radio line running back to a tiny Earth at far left; big words top-left
big = R.background(0.0); d = ImageDraw.Draw(big)
for j in range(60):
    u = j / 60; d.line([(150 + 1300 * u, 820 - 260 * u), (150 + 1300 * (u + 0.012), 820 - 260 * (u + 0.012))], fill=(90, 230, 150), width=10)
R.paste_c(big, R.earth_sprite(26, glow=None), 120, 828)
R.voyager15(big, 1560, 520, 3.4, ang=-0.25)
img = big.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("1 LIGHT-DAY", (255, 255, 255), 118, 105), ("AWAY", (240, 190, 80), 118, 225)]:
    d.text((44, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((40, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=5, stroke_fill=(10, 10, 25))
d.rounded_rectangle([40, 310, 470, 400], 20, fill=(8, 22, 18), outline=(90, 230, 150), width=5)
d.text((255, 355), "24 HOURS", font=F(56, "Black"), fill=(90, 230, 150), anchor="mm")
d.text((70, 610), "Earth", font=F(34, "Black"), fill=(255, 255, 255), anchor="lm", stroke_width=4, stroke_fill=(6, 12, 30))
img.alpha_composite(R.logo_img(52), (1160, 646))
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
