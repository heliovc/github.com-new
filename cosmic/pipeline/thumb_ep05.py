import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep05"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.W, R.H = 1280, 720
t = R.make_starfield(1280, 720, 900, 51).convert("RGBA")
R.draw_star(t, 250, 380, 470, R.CRIM)
d = ImageDraw.Draw(t)
# Earth orbit inside the star (dashed) + tiny Earth
for k in range(0, 360, 6): d.arc([250 - 150, 380 - 150, 250 + 150, 380 + 150], k, k + 3, fill=(255, 255, 255), width=3)
R.paste_c(t, R.earth_sprite(14, glow=None), 250 + 106, 380 - 106)
d = ImageDraw.Draw(t)
d.text((250 + 128, 380 - 138), "EARTH", font=F(30, "Black"), fill=(255, 255, 255), anchor="lb")
# the Sun, to scale-ish, in the dark area
R.paste_c(t, R.sun_sprite(5), 1170, 640)
d.line([(1170, 625), (1170, 585)], fill=(255, 225, 160), width=3)
d.text((1170, 570), "our Sun", font=F(28, "Bold"), fill=(255, 225, 160), anchor="mb")
for i, (txt, col, sz) in enumerate([("1,500×", R.CREAM, 190), ("THE SUN", (255, 255, 255), 112)]):
    y = [200, 350][i]
    d.text((1236 + 6, y + 7), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="rm")
    d.text((1236, y), txt, font=F(sz, "Black"), fill=col, anchor="rm")
d.rounded_rectangle([760, 440, 1240, 510], 18, fill=R.CRIM)
d.text((1000, 475), "EARTH IS INSIDE IT", font=F(40, "Black"), fill=(25, 5, 10), anchor="mm")
t.alpha_composite(R.logo_img(64), (36, 630))
d.text((110, 662), "COSMIC SCALE", font=F(26, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
