import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import render as R
OUT = os.path.join(R.HERE, "out/ep08"); os.makedirs(OUT, exist_ok=True)
F = R.F
t = R.make_starfield(1280, 720, 700, 88).convert("RGBA")
# huge cracked Moon coming down on the right, Earth horizon glowing at the bottom
glow = R.radial(900, [(0, (255, 120, 60, 150)), (0.5, (255, 80, 30, 50)), (1, (255, 60, 20, 0))]); R.paste_c(t, glow, 900, 720)
m = R.moon8(220, light=(-0.6, 0.4), cracked=1.0)
m = m.resize((int(m.width * 1.45), int(m.height * 1.45)), Image.BICUBIC)
R.paste_c(t, m, 930, 300)
e = R.earth_sprite(900, light=(-0.3, -1))
R.paste_c(t, e, 640, 720 + 860)
d = ImageDraw.Draw(t)
d.ellipse([640 - 905, 720 - 45, 640 + 905, 720 + 1765], outline=(255, 140, 80), width=6)
for txt, col, sz, y in [("4 DAYS", (255, 255, 255), 150, 150), ("LEFT", (255, 96, 44), 150, 300)]:
    d.text((50 + 6, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((50, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.text((56, 420), "if the Moon fell", font=F(44, "Bold"), fill=(222, 226, 236), anchor="lm")
t.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
