import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import render as R
OUT = os.path.join(R.HERE, "out/ep09"); os.makedirs(OUT, exist_ok=True)
F = R.F; Wt, Ht = 1280, 720
t = R.make_starfield(Wt, Ht, 500, 909).convert("RGBA")
# right side: a sky packed with stars turning into a white wall (the paradox)
lay = Image.new("RGBA", (Wt, Ht), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); rng = random.Random(3)
for i in range(1400):
    x = rng.uniform(640, Wt); y = rng.uniform(0, Ht); p = (x - 640) / 640
    r = 2 + 26 * p ** 2 * rng.random(); c = R.mix((255, 220, 160), (255, 252, 240), rng.random())
    d.ellipse([x - r, y - r, x + r, y + r], fill=c + (int(90 + 165 * p),))
img = t; img.alpha_composite(lay)
g = np.zeros((Ht, Wt, 4), np.uint8); xs = np.clip((np.arange(Wt) - 760) / 420, 0, 1)
g[..., :3] = (255, 248, 232); g[..., 3] = (xs ** 1.4 * 245).astype(np.uint8)[None, :]
img.alpha_composite(Image.fromarray(g, "RGBA"))
d = ImageDraw.Draw(img)
# hard edge line between the two skies
for txt, col, sz, y in [("SPACE", (255, 255, 255), 128, 150), ("SHOULD BE", (255, 255, 255), 96, 285), ("BLINDING", (255, 170, 60), 136, 425)]:
    d.text((56 + 6, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((56, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.text((60, 545), "so why is it black?", font=F(46, "Bold"), fill=(200, 210, 240), anchor="lm")
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
