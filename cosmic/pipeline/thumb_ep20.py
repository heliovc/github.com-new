import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
OUT = os.path.join(R.HERE, "out/ep20"); os.makedirs(OUT, exist_ok=True)
F = R.F
R.init()
# EP20: the violet "shrunken universe" sphere sitting inside the Sun's comet cloud, a glowing 1 mm grain on the left;
# bold "THE UNIVERSE" / "FITS HERE" + "SUN = 1 GRAIN OF SAND"
img = R.background(0.0); W, H = img.size
R.sc_fitinside(img, {"mode": "reveal"}, 3.0, 6.0)
# cover the scene's own left text with a dark panel, then our big words
lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([0, 0, 760, H], fill=(5, 7, 15, 255)); img.alpha_composite(lay)
R._grain20(img, 560, 840, 26)
img = img.resize((1280, 720), Image.LANCZOS); d = ImageDraw.Draw(img)
for txt, col, sz, y in [("THE UNIVERSE", (255, 255, 255), 96, 150), ("FITS HERE", (185, 155, 255), 118, 275)]:
    d.text((44, y + 6), txt, font=F(sz, "Black"), fill=(0, 0, 0), anchor="lm")
    d.text((38, y), txt, font=F(sz, "Black"), fill=col, anchor="lm", stroke_width=6, stroke_fill=(10, 10, 25))
d.text((40, 430), "IF THE SUN WERE", font=F(50, "Black"), fill=(240, 210, 150), anchor="lm", stroke_width=5, stroke_fill=(0, 0, 0))
d.text((40, 495), "A GRAIN OF SAND", font=F(50, "Black"), fill=(240, 210, 150), anchor="lm", stroke_width=5, stroke_fill=(0, 0, 0))
d.line([(400, 560), (365, 555)], fill=(240, 210, 150), width=0)
img.convert("RGB").save(os.path.join(OUT, "thumbnail.jpg"), quality=92)
print("ok")
