"""Shortcut Lab logo, banner and thumbnail.
python3 -I lab_brand.py brand
python3 -I lab_brand.py thumb "LINE ONE" "LINE TWO" "code snippet line" out.jpg [accent: lime|coral|sky]"""
import sys; sys.path.insert(0, ".")
import tutor as T
from PIL import Image, ImageDraw, ImageFilter
if sys.argv[1] == "brand":
    L = 800; img = Image.new("RGB", (L, L), T.BG); d = ImageDraw.Draw(img)
    d.rounded_rectangle([110, 110, 690, 690], 130, fill=T.LIME)
    d.text((400, 392), "</>", font=T.F(250, "monob"), fill=T.BG, anchor="mm")
    d.rectangle([250, 540, 550, 572], fill=T.BG)
    img.save("out/logo.png")
    bw, bh = 2560, 1440; b = T.make_bg(bw, bh); d = ImageDraw.Draw(b)
    d.rounded_rectangle([bw/2 - 470, 560, bw/2 - 370, 660], 22, fill=T.LIME); d.text((bw/2 - 420, 610), "</>", font=T.F(44, "monob"), fill=T.BG, anchor="mm")
    d.text((bw/2 - 340, 610), "SHORTCUT LAB", font=T.F(110, "Bold"), fill=T.TXT, anchor="lm")
    d.text((bw/2, 760), "Software & AI tutorials that save you hours", font=T.F(54, "Regular"), fill=T.DIM, anchor="mm")
    d.text((bw/2, 840), "$ new tutorial every day", font=T.F(40, "mono"), fill=T.LIME, anchor="mm")
    b.convert("RGB").save("out/banner.jpg", quality=90); print("brand ok")
else:
    l1, l2, code, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY}[sys.argv[6] if len(sys.argv) > 6 else "lime"]
    img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    # code card on the right, tilted look via offset shadow
    T.W, T.H = 1280, 720
    box = [700, 150, 1240, 560]; T.window(img, box, "script.py")
    d = ImageDraw.Draw(img); f = T.F(26, "mono"); y = 230
    for ln in code.split("|"):
        cx = 730
        for s, c in T.colorize(ln): d.text((cx, y), s, font=f, fill=c); cx += f.getlength(s)
        y += 46
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 112
        while T.F(fs, "Bold").getlength(txt) > 640: fs -= 4
        d.text((50, 230 + i * 150), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
