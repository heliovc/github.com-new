import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import render as R
OUT = os.path.join(R.HERE, "out/ep16"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# a glowing, mottled "fog wall" (our own noise, CMB-like) fills the right side; galaxies get smaller and redder toward it; tiny Earth at left
big = R.background(0.0)
Wb, Hb = big.size
rng = np.random.default_rng(16)
noise = rng.normal(0, 1, (Hb // 12, Wb // 12)).astype(np.float32)
nimg = Image.fromarray(((noise - noise.min()) / (noise.max() - noise.min()) * 255).astype(np.uint8)).resize((Wb, Hb), Image.BICUBIC).filter(ImageFilter.GaussianBlur(14))
n = np.asarray(nimg).astype(np.float32) / 255
xx = np.linspace(0, 1, Wb)[None, :]
wall = np.clip((xx - 0.52) / 0.12, 0, 1)
rgb = np.zeros((Hb, Wb, 4), np.float32)
rgb[..., 0] = 255; rgb[..., 1] = 90 + 120 * n; rgb[..., 2] = 30 + 60 * n
rgb[..., 3] = 255 * wall * (0.75 + 0.25 * n)
big.alpha_composite(Image.fromarray(rgb.astype(np.uint8), "RGBA"))
g = R.galaxy_sprite()
for x, s, col in [(330, 300, (255, 240, 220)), (560, 170, (255, 190, 160)), (730, 100, (255, 140, 110)), (850, 64, (255, 110, 80))]:
    sp = g.resize((s, s)); a = np.asarray(sp).astype(np.float32); a[..., 0] *= col[0] / 255; a[..., 1] *= col[1] / 255; a[..., 2] *= col[2] / 255
    R.paste_c(big, Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA"), x, 760)
R.paste_c(big, R.earth_sprite(24, glow=None), 90, 760)
img = big.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("THE LAST", (255, 255, 255), 112, 100), ("WALL", (255, 196, 90), 150, 225)]:
    d.text((44, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((40, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=5, stroke_fill=(10, 10, 25))
d.text((1060, 360), "?", font=F(260, "Black"), fill=(255, 255, 255), anchor="mm", stroke_width=8, stroke_fill=(90, 20, 10))
d.rounded_rectangle([40, 330, 560, 410], 20, fill=(30, 8, 8), outline=(255, 84, 84), width=5)
d.text((300, 370), "13.8 BILLION YEARS", font=F(44, "Black"), fill=(255, 120, 110), anchor="mm")
img.alpha_composite(R.logo_img(52), (40, 646))
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
