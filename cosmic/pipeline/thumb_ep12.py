import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep12"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# Earth -> Mars light beam that has only crawled part of the way + a stopwatch badge
big = R.background(0.0)
R.paste_c(big, R.earth_sprite(150), 230, 760)
R.paste_c(big, R.planet_sprite(95, (210, 100, 70), light=(-1, -0.2)), 1700, 760)
lay = Image.new("RGBA", big.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
for k in range(40):
    dl.line([(390, 760), (1000, 760)], fill=(255, 232, 150, 6), width=90 - 2 * k)
dl.line([(390, 760), (1000, 760)], fill=(255, 245, 200, 255), width=10)
big.alpha_composite(lay)
R.paste_c(big, R.radial(200, [(0, (255, 255, 240, 255)), (0.3, (255, 232, 150, 200)), (1, (255, 200, 80, 0))]), 1000, 760)
d = ImageDraw.Draw(big)
for x in range(1040, 1580, 36): d.line([(x, 760), (x + 16, 760)], fill=(120, 130, 160), width=5)
img = big.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("LIGHT IS", (255, 255, 255), 120, 95), ("SLOW", (255, 220, 110), 190, 245)]:
    d.text((646, y + 8), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="mm")
    d.text((640, y), txt, font=F(sz, "Black"), fill=col, anchor="mm", stroke_width=5, stroke_fill=(10, 10, 25))
d.rounded_rectangle([880, 560, 1240, 660], 22, fill=(16, 60, 40), outline=(110, 255, 170), width=5)
d.text((1060, 610), "22 MIN", font=F(64, "Black"), fill=(110, 255, 170), anchor="mm")
d.text((1133, 455), "MARS", font=F(34, "Black"), fill=(240, 150, 120), anchor="mm")
img.alpha_composite(R.logo_img(52), (40, 646))
d.text((102, 672), "COSMIC SCALE", font=F(24, "Bold"), fill=(230, 230, 240), anchor="lm")
img.convert("RGB").save(f"{OUT}/thumbnail.jpg", quality=92)
print("ok")
