"""Logo (800x800) and banner (2560x1440) for The Quiet Archive."""
import sys, math
sys.path.insert(0, ".")
import sleep as S
from PIL import Image, ImageDraw, ImageFilter
P = S.PAL

def lamp(d, cx, cy, s, col, flame=True):
    d.ellipse([cx - 120*s, cy - 44*s, cx + 110*s, cy + 30*s], fill=col)
    d.polygon([(cx + 90*s, cy - 26*s), (cx + 170*s, cy - 42*s), (cx + 178*s, cy - 18*s), (cx + 96*s, cy + 6*s)], fill=col)
    d.ellipse([cx - 40*s, cy - 58*s, cx + 30*s, cy - 30*s], fill=col)
    d.arc([cx - 190*s, cy - 50*s, cx - 90*s, cy + 20*s], 100, 260, fill=col, width=int(16*s))
    d.rectangle([cx - 60*s, cy + 26*s, cx + 50*s, cy + 44*s], fill=col)
    return (cx + 176*s, cy - 46*s)

# logo
L = 800
img = Image.new("RGBA", (L, L), S.PAL["sky_top"] + (255,))
glow = S.Scene.__new__(S.Scene); g = S.Scene._glow(glow, 300).resize((900, 900))
gl = Image.new("RGBA", g.size, P["light"] + (0,)); gl.putalpha(g.getchannel("A").point(lambda v: int(v * 0.45)))
d = ImageDraw.Draw(img)
img.alpha_composite(gl, (int(L/2 + 120 - 450), int(L/2 - 40 - 450)))
d = ImageDraw.Draw(img)
d.ellipse([60, 60, L - 60, L - 60], outline=P["accent"] + (255,), width=6)
d.ellipse([84, 84, L - 84, L - 84], outline=P["accent"] + (110,), width=2)
fx, fy = lamp(d, L/2 - 30, L/2 + 90, 1.25, mix := (36, 26, 24, 255))
d.polygon([(fx - 16, fy + 4), (fx, fy - 70), (fx + 16, fy + 4), (fx, fy + 16)], fill=(255, 206, 128, 255))
d.polygon([(fx - 7, fy + 2), (fx, fy - 38), (fx + 7, fy + 2)], fill=(255, 246, 220, 255))
img.convert("RGB").save("out/logo.png")

# banner
BW, BH = 2560, 1440
sc = S.Scene("hills", P, 404)
fr = sc.frame(5.0).convert("RGB").resize((2560, 1440), Image.LANCZOS)
ban = fr.convert("RGBA")
shade = Image.new("RGBA", (BW, BH), (0, 0, 0, 0)); ds = ImageDraw.Draw(shade)
ds.rectangle([0, 520, BW, 920], fill=(0, 0, 0, 120)); shade = shade.filter(ImageFilter.GaussianBlur(60)); ban.alpha_composite(shade)
d = ImageDraw.Draw(ban)
d.text((BW/2, 640), "T H E   Q U I E T   A R C H I V E", font=S.F(44, 500), fill=P["accent"] + (255,), anchor="mm")
d.text((BW/2, 735), "Calm history to fall asleep to", font=S.F(104, 400, True), fill=P["text"] + (255,), anchor="mm")
d.line([(BW/2 - 160, 820), (BW/2 - 24, 820)], fill=P["accent"] + (220,), width=3); d.line([(BW/2 + 24, 820), (BW/2 + 160, 820)], fill=P["accent"] + (220,), width=3)
d.regular_polygon((BW/2, 820, 9), 4, fill=P["accent"] + (230,))
ban.convert("RGB").save("out/banner.jpg", quality=90)
print("ok")
