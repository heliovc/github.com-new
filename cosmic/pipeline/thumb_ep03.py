import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep03"); os.makedirs(OUT, exist_ok=True)
F = R.F
t = R.make_starfield(1280, 720, 900, 23).convert("RGBA")
sp = R.web_layer("universe").resize((620, 620), Image.LANCZOS)
R.paste_c(t, sp, 1010, 380)
d = ImageDraw.Draw(t)
d.ellipse([1004, 374, 1016, 386], fill=(255, 255, 255)); d.text((1010, 410), "YOU", font=F(30, "Black"), fill=(255, 255, 255), anchor="mm")
d.rounded_rectangle([40, 50, 520, 150], 22, fill=R.MAG)
d.text((280, 100), "VISIBLE UNIVERSE", font=F(46, "Black"), fill=(14, 8, 30), anchor="mm")
for i, (txt, col, sz) in enumerate([("93 BILLION", (255, 255, 255), 128), ("LIGHT-YEARS", R.VIO, 96)]):
    y = 280 + i * 140
    d.text((48, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((42, y), txt, font=F(sz, "Black"), fill=col, anchor="lm")
d.text((46, 530), "...in a 13.8-billion-year-old universe?", font=F(40, "ExtraBold"), fill=(255, 194, 75), anchor="lm")
t.alpha_composite(R.logo_img(70), (40, 625))
d.text((120, 660), "COSMIC SCALE", font=F(28, "Bold"), fill=R.DIM, anchor="lm")
t.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
