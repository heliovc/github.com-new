import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import render as R

OUT = os.path.join(R.HERE, "out/ep02"); os.makedirs(OUT, exist_ok=True)
F = R.F
t = R.make_starfield(1280, 720, 900, 12).convert("RGBA")
# frozen Earth bottom-right, drifting into the dark
e = R.planet_sprite(250, (70, 130, 230), light=(0.2, -1), earth=True, glow=(170, 225, 255))
a = np.asarray(e, np.float32); a[..., :3] = a[..., :3] * 0.35 + np.array([180, 220, 245], np.float32) * 0.45
e = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA")
R.paste_c(t, e, 1020, 470)
# empty Sun outline top-right
d = ImageDraw.Draw(t)
for k in range(0, 360, 14):
    d.arc([980, 20, 1200, 240], k, k + 7, fill=(255, 194, 75), width=6)
d.text((1090, 130), "?", font=F(110, "Black"), fill=(255, 194, 75), anchor="mm")
# words
d.rounded_rectangle([40, 60, 560, 170], 22, fill=(170, 225, 255))
d.text((300, 115), "NO MORE SUN", font=F(66, "Black"), fill=(8, 12, 24), anchor="mm")
for i, (txt, col) in enumerate([("GONE", (255, 255, 255)), ("FOREVER", (170, 225, 255))]):
    d.text((46, 290 + i * 150), txt, font=F(150, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((40, 284 + i * 150), txt, font=F(150, "Black"), fill=col, anchor="lm")
d.text((44, 560), "how long would we last?", font=F(52, "ExtraBold"), fill=(255, 194, 75), anchor="lm")
t.alpha_composite(R.logo_img(70), (40, 625))
d.text((120, 660), "COSMIC SCALE", font=F(28, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
