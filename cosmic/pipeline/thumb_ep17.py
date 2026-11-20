import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep17"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# split sky: left = today's blue noon sky with our small Sun; right = a giant red star filling the sky over the same beach
img = R.background(0.0); W, H = img.size; d = ImageDraw.Draw(img)
for y in range(0, H, 4):
    u = y / H
    d.rectangle([0, y, W // 2, y + 4], fill=R.mix((70, 130, 220), (190, 220, 250), u))
right = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(right)
for y in range(0, H, 4):
    u = y / H; dr.rectangle([W // 2, y, W, y + 4], fill=R.mix((60, 8, 10), (150, 40, 20), u) + (255,))
img.alpha_composite(right)
R.paste_c(img, R.star17(520, 2100, halo=1.3), W * 0.80, H * 0.42)
R.paste_c(img, R.sun_sprite(42), W * 0.27, H * 0.33)
d = ImageDraw.Draw(img)
hill = [(0, H)] + [(x, 860 - 60 * __import__("math").sin(x / 230) - 30 * __import__("math").sin(x / 77)) for x in range(0, W + 1, 40)] + [(W, H)]
d.polygon(hill, fill=(12, 14, 22))
d.line([(W // 2, 0), (W // 2, H)], fill=(255, 255, 255), width=10)
img = img.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("SWAP", (255, 255, 255), 150, 470), ("THE SUN?", (255, 205, 90), 132, 610)]:
    d.text((54, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((48, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=6, stroke_fill=(10, 10, 25))
d.text((1240, 680), "2,150× WIDER", font=F(46, "Black"), fill=(255, 255, 255), anchor="rm", stroke_width=5, stroke_fill=(0, 0, 0))
d.text((330, 160), "TODAY", font=F(44, "Black"), fill=(255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(0, 0, 0))
img.convert("RGB").save(os.path.join(OUT, "thumbnail.jpg"), quality=92)
print("ok")
