"""Shortcut Lab logo, banner and thumbnail.
python3 -I lab_brand.py brand
python3 -I lab_brand.py thumbfolders "LINE ONE" "LINE TWO" "Images|Docs|Audio|Video|Zips|Other" out.jpg sky
python3 -I lab_brand.py thumbsheet "LINE ONE" "LINE TWO" "=FORMULA" out.jpg coral   (EP03: mini spreadsheet card)
python3 -I lab_brand.py thumbprompt "LINE ONE" "LINE TWO" "vague prompt" out.jpg violet   (EP04: before/after prompt card)
python3 -I lab_brand.py thumbgit "LINE ONE" "LINE TWO" "hash msg|hash msg|hash msg" out.jpg yellow   (EP05: commit history + "go back" arc)
python3 -I lab_brand.py thumbchart "LINE ONE" "LINE TWO" "df.plot(kind=\"bar\")" out.jpg mint   (EP06: dark chart card, bars + trend line)
python3 -I lab_brand.py thumbterm "LINE ONE" "LINE TWO" "$ cmd|output|$ cmd" out.jpg pink   (EP07: big terminal card, typed commands + outputs)
python3 -I lab_brand.py thumbquery "LINE ONE" "LINE TWO" "=QUERY()" "Lena=1670|Omar=1530" out.jpg orange   (EP08: ranked report card with bars over a faded raw table)
python3 -I lab_brand.py thumbweb "LINE ONE" "LINE TWO" "<html line>|<html line>" screenshot.png out.jpg periwinkle   (EP09: code card behind, browser with the REAL page screenshot in front)
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
elif sys.argv[1] == "thumbfolders":  # EP02 layout: big text left, grid of colored folders right
    l1, l2, labels, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL}[sys.argv[6] if len(sys.argv) > 6 else "sky"]
    T.ACC = acc; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    cols = [T.SKY, T.YEL, T.VIO, T.CORAL, T.LIME, T.DIM]
    for i, lab in enumerate(labels.split("|")):
        cx, cy = 790 + (i % 2) * 235, 150 + (i // 2) * 175; c = cols[i % len(cols)]
        d.rounded_rectangle([cx, cy, cx + 70, cy + 26], 8, fill=c); d.rounded_rectangle([cx, cy + 16, cx + 200, cy + 136], 14, fill=c)
        d.text((cx + 100, cy + 80), lab, font=T.F(30, "Bold"), fill=T.BG, anchor="mm")
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 120
        while T.F(fs, "Bold").getlength(txt) > 660: fs -= 4
        d.text((50, 250 + i * 170), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "$ python sort_downloads.py", font=T.F(30, "mono"), fill=T.LIME)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbsheet":  # EP03 layout: text left, tilted mini spreadsheet with a spilled result right
    l1, l2, form, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL}[sys.argv[6] if len(sys.argv) > 6 else "coral"]
    T.ACC = acc; img = T.make_bg(1280, 720)
    card = Image.new("RGBA", (600, 560), (0, 0, 0, 0)); c = ImageDraw.Draw(card)
    c.rounded_rectangle([0, 0, 599, 559], 22, fill=T.PANEL, outline=T.LINE, width=3)
    c.rounded_rectangle([20, 20, 580, 76], 10, fill=T.PANEL2); c.text((40, 48), "fx", font=T.F(26, "Medium"), fill=T.DIM, anchor="lm")
    c.text((90, 48), form, font=T.F(28, "monob"), fill=T.TXT, anchor="lm")
    xs = [20, 70, 220, 400, 580]; ys = [100 + i * 54 for i in range(9)]
    for y in ys: c.line([20, y, 580, y], fill=T.LINE, width=2)
    for x in xs: c.line([x, 100, x, ys[-1]], fill=T.LINE, width=2)
    names, vals = ["Ana", "Ben", "Cara", "Dev", "Eli"], ["1590", "435", "1550", "1225", "1130"]
    c.text((145, 127), "Rep", font=T.F(26, "Bold"), fill=T.DIM, anchor="mm"); c.text((310, 127), "Total", font=T.F(26, "Bold"), fill=T.DIM, anchor="mm")
    for i, (n, v) in enumerate(zip(names, vals)):
        y = (ys[i + 1] + ys[i + 2]) / 2; c.text((45, y), str(i + 2), font=T.F(22, "Bold"), fill=T.DIM, anchor="mm")
        c.text((90, y), n, font=T.F(30, "Medium"), fill=T.TXT, anchor="lm"); c.text((385, y), v, font=T.F(30, "Bold"), fill=acc, anchor="rm")
    c.rectangle([220, ys[1], 400, ys[6]], outline=T.SKY, width=4); c.rectangle([220, ys[1], 400, ys[2]], outline=acc, width=6)
    card = card.rotate(-4, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); sh.paste((0, 0, 0, 150), (660, 110), card); sh = sh.filter(ImageFilter.GaussianBlur(20)); img.alpha_composite(sh)
    img.alpha_composite(card, (650, 90)); d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 124
        while T.F(fs, "Bold").getlength(txt) > 600: fs -= 4
        d.text((50, 260 + i * 160), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "Excel 365 · 2021 · 2024", font=T.F(30, "Medium"), fill=T.DIM)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbprompt":  # EP04 layout: text left, before (struck) / after (colored parts) prompt cards right
    l1, l2, vague, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL}[sys.argv[6] if len(sys.argv) > 6 else "violet"]
    T.ACC = acc; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    x0, x1 = 690, 1240
    d.rounded_rectangle([x0, 70, x1, 170], 18, fill=T.PANEL, outline=T.CORAL, width=3)
    d.rounded_rectangle([x0 + 20, 86, x0 + 130, 118], 16, fill=T.CORAL); d.text((x0 + 75, 102), "BEFORE", font=T.F(20, "Bold"), fill=T.BG, anchor="mm")
    fv = T.F(30, "Medium"); d.text((x0 + 22, 145), vague, font=fv, fill=T.DIM, anchor="lm"); d.line([x0 + 22, 147, x0 + 22 + fv.getlength(vague), 147], fill=T.CORAL, width=4)
    d.rounded_rectangle([x0, 200, x1, 650], 18, fill=T.PANEL, outline=acc, width=4)
    d.rounded_rectangle([x0 + 20, 218, x0 + 120, 250], 16, fill=acc); d.text((x0 + 70, 234), "AFTER", font=T.F(20, "Bold"), fill=T.BG, anchor="mm")
    parts = [("Who you are", T.SKY), ("The task", T.VIO), ("The details", T.YEL), ("Who it's for", T.LIME), ("The format", (255, 160, 200))]
    for i, (lab, col) in enumerate(parts):
        y = 275 + i * 74; d.rounded_rectangle([x0 + 22, y, x1 - 22, y + 58], 14, fill=T.mix(T.PANEL, col, 0.22), outline=col, width=3)
        d.ellipse([x0 + 42, y + 19, x0 + 62, y + 39], fill=col); d.text((x0 + 80, y + 29), lab, font=T.F(32, "Bold"), fill=T.TXT, anchor="lm")
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 124
        while T.F(fs, "Bold").getlength(txt) > 600: fs -= 4
        d.text((50, 270 + i * 160), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "ChatGPT · Claude · Gemini · Copilot", font=T.F(28, "Medium"), fill=T.DIM)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbgit":  # EP05 layout: text left, vertical commit history right, newest on top, dashed arc back to the oldest
    l1, l2, commits, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL}[sys.argv[6] if len(sys.argv) > 6 else "yellow"]
    T.ACC = acc; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    cs = commits.split("|"); x = 800; ys = [170 + i * 170 for i in range(len(cs))]
    d.rounded_rectangle([700, 90, 1240, 640], 24, fill=T.PANEL, outline=T.LINE, width=2)
    for i, c in enumerate(cs):
        h, msg = c.split(" ", 1); y = ys[i]; bad = i == 0; col = T.CORAL if bad else acc
        if i: d.line([x, ys[i - 1] + 34, x, y - 34], fill=T.LINE, width=8)
        d.ellipse([x - 32, y - 32, x + 32, y + 32], fill=col, outline=T.BG, width=5)
        d.text((x + 60, y - 22), h, font=T.F(28, "monob"), fill=col, anchor="lm"); d.text((x + 60, y + 20), msg, font=T.F(30, "SemiBold"), fill=T.TXT, anchor="lm")
    import math
    ya, yb = ys[0], ys[-1]; cx = x - 40
    for k in range(0, 40, 2):
        a0, a1 = math.pi / 2 + math.pi * k / 40, math.pi / 2 + math.pi * (k + 1) / 40
        r = (yb - ya) / 2; my = (ya + yb) / 2
        d.line([cx + 70 * math.cos(a0) - 0, my - r * math.sin(a0), cx + 70 * math.cos(a1), my - r * math.sin(a1)], fill=T.YEL if acc != T.YEL else T.SKY, width=6)
    d.text((cx - 4, yb + 4), "▶", font=T.F(34, "monob"), fill=T.YEL if acc != T.YEL else T.SKY, anchor="mm")
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 124
        while T.F(fs, "Bold").getlength(txt) > 600: fs -= 4
        d.text((50, 270 + i * 160), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "Windows · Mac · Linux", font=T.F(30, "Medium"), fill=T.DIM)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbchart":  # EP06 layout: text left, dark chart card right (rising bars + trend line with dots), code chip under it
    l1, l2, code, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL, "mint": (80, 220, 190)}[sys.argv[6] if len(sys.argv) > 6 else "mint"]
    T.ACC = acc; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    d.rounded_rectangle([690, 100, 1240, 560], 24, fill=T.PANEL, outline=T.LINE, width=2)
    for k in range(4): d.line([740, 180 + k * 85, 1200, 180 + k * 85], fill=T.LINE, width=2)
    vals = [0.35, 0.5, 0.42, 0.68, 0.9]; cols = [T.SKY, T.VIO, T.CORAL, T.YEL, acc]; bx = 750; bw = 70; base = 510
    pts = []
    for i, v in enumerate(vals):
        x = bx + i * 90; top = base - v * 320
        d.rounded_rectangle([x, top, x + bw, base], 10, fill=cols[i]); pts.append((x + bw / 2, top - 40))
    d.line(pts, fill=T.TXT, width=6)
    for (x, y) in pts: d.ellipse([x - 11, y - 11, x + 11, y + 11], fill=T.TXT, outline=T.BG, width=3)
    d.line([740, base, 1200, base], fill=T.DIM, width=3)
    fc = T.F(30, "mono"); cw = fc.getlength(code) + 50
    d.rounded_rectangle([965 - cw / 2, 590, 965 + cw / 2, 650], 30, fill=T.BG, outline=acc, width=3); d.text((965, 620), code, font=fc, fill=acc, anchor="mm")
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 124
        while T.F(fs, "Bold").getlength(txt) > 600: fs -= 4
        d.text((50, 270 + i * 160), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "pandas + matplotlib · free", font=T.F(30, "Medium"), fill=T.DIM)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbterm":
    l1, l2, lines, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL, "pink": (255, 160, 200)}[sys.argv[6] if len(sys.argv) > 6 else "pink"]
    T.ACC = acc; T.W, T.H = 1280, 720; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    box = [640, 140, 1250, 580]; T.window(img, box, "Terminal", kind="term")
    d = ImageDraw.Draw(img); f = T.F(25, "mono"); y = 225
    for ln in lines.split("|"):
        cx = 675
        for s2, c in T.colorize(ln, "sh"): d.text((cx, y), s2, font=f, fill=(acc if s2 == "$ " else c)); cx += f.getlength(s2)
        y += 52
    d.rectangle([cx + 4, y - 52, cx + 22, y - 18], fill=acc)
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 120
        while T.F(fs, "Bold").getlength(txt) > 560: fs -= 4
        d.text((50, 260 + i * 160), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbquery":  # EP08 layout: text left; right a faded raw table behind, a clean ranked report card with bars in front, QUERY chip on top
    l1, l2, form, rows, out = sys.argv[2:7]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL, "orange": (255, 155, 50)}[sys.argv[7] if len(sys.argv) > 7 else "orange"]
    T.ACC = acc; img = T.make_bg(1280, 720); d = ImageDraw.Draw(img)
    for i in range(9):  # raw data, faded
        y = 150 + i * 46; d.rounded_rectangle([800, y, 1240, y + 36], 6, fill=T.mix(T.BG, T.PANEL, 0.6))
        for j, w in enumerate([90, 60, 80, 70]): d.rounded_rectangle([815 + j * 105, y + 13, 815 + j * 105 + w, y + 23], 4, fill=T.mix(T.BG, T.LINE, 0.8))
    data = [r.split("=") for r in rows.split("|")]; mx = max(float(v) for _, v in data)
    cx0, cy0, cw, ch = 650, 220, 520, 90 + len(data) * 74
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([cx0 + 12, cy0 + 20, cx0 + cw + 12, cy0 + ch + 20], 22, fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(20)); img.alpha_composite(sh)
    d = ImageDraw.Draw(img); d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + ch], 22, fill=T.PANEL, outline=acc, width=4)
    d.text((cx0 + 30, cy0 + 45), "Rep", font=T.F(28, "Bold"), fill=T.DIM, anchor="lm"); d.text((cx0 + cw - 30, cy0 + 45), "Total", font=T.F(28, "Bold"), fill=T.DIM, anchor="rm")
    for i, (n, v) in enumerate(data):
        y = cy0 + 100 + i * 74; bw = (cw - 290) * float(v) / mx
        d.rounded_rectangle([cx0 + 150, y - 20, cx0 + 150 + bw, y + 20], 10, fill=T.mix(T.PANEL, acc, 0.35 + 0.65 * (i == 0)))
        d.text((cx0 + 30, y), n, font=T.F(32, "SemiBold"), fill=T.TXT, anchor="lm"); d.text((cx0 + cw - 30, y), v, font=T.F(32, "monob"), fill=acc if i == 0 else T.TXT, anchor="rm")
    fw = T.F(34, "monob").getlength(form) + 60
    d.rounded_rectangle([cx0 + cw / 2 - fw / 2, cy0 - 90, cx0 + cw / 2 + fw / 2, cy0 - 26], 32, fill=acc); d.text((cx0 + cw / 2, cy0 - 58), form, font=T.F(34, "monob"), fill=T.BG, anchor="mm")
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 120
        while T.F(fs, "Bold").getlength(txt) > 560: fs -= 4
        d.text((50, 300 + i * 150), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm")
    img.convert("RGB").save(out, quality=92); print("thumb ok")
elif sys.argv[1] == "thumbweb":  # EP09 layout: text left; right an index.html code card (behind) + browser window showing the real rendered page (front)
    l1, l2, code, shot, out = sys.argv[2:7]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL, "periwinkle": (125, 140, 255)}[sys.argv[7] if len(sys.argv) > 7 else "periwinkle"]
    T.ACC = acc; T.W, T.H = 1280, 720; img = T.make_bg(1280, 720)
    T.window(img, [590, 80, 1100, 400], "index.html")
    d = ImageDraw.Draw(img); f = T.F(24, "mono"); y = 158
    for ln in code.split("|"):
        cx = 625
        for s2, c in T.colorize(ln, "html"): d.text((cx, y), s2, font=f, fill=c); cx += f.getlength(s2)
        y += 44
    bx0, by0, bw = 760, 262, 490; pic = Image.open(shot).convert("RGBA"); pic = pic.resize((bw - 24, int(pic.height * (bw - 24) / pic.width)), Image.LANCZOS).crop((0, 0, bw - 24, 330))
    T.window(img, [bx0, by0, bx0 + bw, by0 + 52 + 12 + pic.height + 12], "my first page", kind="term")
    img.alpha_composite(pic, (bx0 + 12, by0 + 64)); d = ImageDraw.Draw(img)
    d.rounded_rectangle([bx0 - 4, by0 - 4, bx0 + bw + 4, by0 + 52 + 12 + pic.height + 16], 18, outline=acc, width=4)
    d.rounded_rectangle([40, 40, 300, 92], 26, fill=acc); d.text((170, 66), "SHORTCUT LAB", font=T.F(26, "Bold"), fill=T.BG, anchor="mm")
    for i, (txt, col) in enumerate([(l1, T.TXT), (l2, acc)]):
        fs = 120
        while T.F(fs, "Bold").getlength(txt) > 540: fs -= 4
        d.text((50, 280 + i * 150), txt, font=T.F(fs, "Bold"), fill=col, anchor="lm", stroke_width=4, stroke_fill=T.BG)
    d.text((54, 600), "HTML + CSS · 15 minutes · free", font=T.F(30, "Medium"), fill=T.DIM)
    img.convert("RGB").save(out, quality=92); print("thumb ok")
else:
    l1, l2, code, out = sys.argv[2:6]; acc = {"lime": T.LIME, "coral": T.CORAL, "sky": T.SKY, "violet": T.VIO, "yellow": T.YEL}[sys.argv[6] if len(sys.argv) > 6 else "lime"]
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
