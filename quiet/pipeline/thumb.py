"""Thumbnail 1280x720: python3 -I thumb.py <scene> "<BIG LINE>" "<small line>" out.jpg [seed]"""
import sys
sys.path.insert(0, ".")
import sleep as S
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
scene, big, small, out = sys.argv[1:5]; seed = int(sys.argv[5]) if len(sys.argv) > 5 else 7
P = dict(S.PAL); P.update(sky_mid=(48, 32, 52), horizon=(176, 104, 66), moon=(255, 238, 205))
sc = S.Scene(scene, P, seed)
im = sc.frame(6.0).convert("RGB")
im = ImageEnhance.Brightness(im).enhance(1.35); im = ImageEnhance.Contrast(im).enhance(1.12)
im = im.resize((1280, 720), Image.LANCZOS).convert("RGBA")
sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
d.rectangle([0, 470, 1280, 720], fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(40)); im.alpha_composite(sh)
d = ImageDraw.Draw(im)
f = S.F(112, 600); 
while f.getlength(big) > 1180: f = S.F(f.size - 6, 600)
d.text((643, 590), big, font=f, fill=(0, 0, 0, 200), anchor="mm")
d.text((640, 585), big, font=f, fill=(250, 236, 208, 255), anchor="mm")
d.text((640, 672), small, font=S.F(40, 400, True), fill=P["accent"] + (255,), anchor="mm")
im.convert("RGB").save(out, quality=92); print("ok", out)
