"""Compilation thumbnail 1280x720: three episode scenes side by side, melted into each other with soft vertical blends.
python3 -I thumb_comp.py "<BIG LINE>" "<small line>" out.jpg ep01_rome.py:city ep02_monastery.py:cloister ep03_nile.py:nile:mirror"""
import sys, os, importlib.util as U
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(p, n):
    sp = U.spec_from_file_location(n, p); m = U.module_from_spec(sp); sp.loader.exec_module(m); return m
S = load(os.path.join(HERE, "sleep.py"), "sleep")
big, small, out = sys.argv[1:4]; specs = sys.argv[4:]
TW, TH = 1280, 720
panels = []
for i, sp in enumerate(specs):
    f, scene, *opt = sp.split(":")
    ep = load(os.path.join(HERE, f), f"ep{i}")
    P = dict(S.PAL); P.update(getattr(ep, "PALETTE", {}))
    P["sky_mid"] = S.mix(P["sky_mid"], (255, 255, 255), 0.08); P["horizon"] = S.mix(P["horizon"], (255, 255, 255), 0.18)
    im = S.Scene(scene, P, 300 + 11 * i).frame(6.0).convert("RGB")
    im = ImageEnhance.Brightness(im).enhance(1.45); im = ImageEnhance.Contrast(im).enhance(1.12)
    if "mirror" in opt: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    panels.append((np.asarray(im.resize((TW, TH), Image.LANCZOS), np.float32), P))
n = len(panels); xs = np.arange(TW, dtype=np.float32)
acc = np.zeros((TH, TW, 3), np.float32); wsum = np.zeros((1, TW, 1), np.float32)
for i, (a, _) in enumerate(panels):
    c = (i + 0.5) * TW / n
    w = np.exp(-((xs - c) / (TW / n * 0.56)) ** 8)[None, :, None]
    acc += a * w; wsum += w
img = Image.fromarray(np.clip(acc / wsum, 0, 255).astype(np.uint8)).convert("RGBA")
sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
d.rectangle([0, 455, TW, TH], fill=(0, 0, 0, 175)); sh = sh.filter(ImageFilter.GaussianBlur(40)); img.alpha_composite(sh)
d = ImageDraw.Draw(img)
for i, sp in enumerate(specs):  # small place labels near the top of each panel
    lab = os.path.basename(sp.split(":")[0]).split("_", 1)[1][:-3].upper()
    lab = {"ROME": "ROME", "MONASTERY": "MONASTERY", "NILE": "THE NILE"}.get(lab, lab)
    d.text(((i + 0.5) * TW / n, 52), " ".join(lab), font=S.F(30, 500), fill=panels[i][1]["accent"] + (235,), anchor="mm")
f = S.F(116, 600)
while f.getlength(big) > 1180: f = S.F(f.size - 6, 600)
d.text((643, 585), big, font=f, fill=(0, 0, 0, 200), anchor="mm")
d.text((640, 580), big, font=f, fill=(250, 236, 208, 255), anchor="mm")
d.text((640, 670), small, font=S.F(40, 400, True), fill=(226, 196, 140, 255), anchor="mm")
img.convert("RGB").save(out, quality=92); print("ok", out)
