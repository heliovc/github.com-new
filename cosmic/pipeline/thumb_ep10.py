import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import numpy as np
import render as R
OUT = os.path.join(R.HERE, "out/ep10"); os.makedirs(OUT, exist_ok=True)
F = R.F; Wt, Ht = 1280, 720
img = R.make_starfield(Wt, Ht, 500, 1010).convert("RGBA")
# one body split down the middle: left half banded Jupiter, right half the red star it would become
cx, cy, r = 930, 380, 300
pl = R.jup10(r, 0.0); st = R.jup10(r, 1.0)
lay = Image.new("RGBA", (Wt, Ht), (0, 0, 0, 0)); R.paste_c(lay, st, cx, cy)
lay2 = Image.new("RGBA", (Wt, Ht), (0, 0, 0, 0)); R.paste_c(lay2, pl, cx, cy)
m = np.zeros((Ht, Wt), np.uint8); m[:, :cx] = 255
a2 = np.minimum(np.asarray(lay2.getchannel("A")), m); lay2.putalpha(Image.fromarray(a2))
img.alpha_composite(lay); img.alpha_composite(lay2)
d = ImageDraw.Draw(img)
d.line([(cx, cy - r - 30), (cx, cy + r + 30)], fill=(255, 255, 255), width=5)
for txt, col, sz, y in [("JUPITER", (255, 255, 255), 120, 170), ("AS A STAR?", (255, 110, 70), 112, 300)]:
    d.text((50 + 6, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((50, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.rounded_rectangle([50, 410, 470, 520], 20, fill=(190, 240, 110))
d.text((260, 465), "NEEDS 80×", font=F(64, "Black"), fill=(20, 24, 10), anchor="mm")
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=R.DIM, anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
