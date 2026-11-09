"""Cosmic Scale — "Scale Shorts" (vertical nativo 1080x1920 30fps): UMA comparação de escala ("X inside Y", "small vs giant"), 30–50 s.
Uso: python3 -I scale_short.py scaleNN_algo.py out/scaleNN [--preview]
Roteiro: TITLE, THEME {accent, accent2, tint}, BIG {num, top, sub} (número grande já no frame 0), BEATS [{say, vis{...}}], SOURCES.
- O 1º beat é o gancho (≤ 2 s falado); o último termina com uma pergunta e emenda no 1º (loop): o frame final repete a composição do frame 0.
- Sem fade no início; legenda grande queimada (3 palavras por bloco); narração Kokoro af_heart.
Visuais (vis.type):
  "gap"    : Terra no topo e Lua embaixo EM ESCALA; os planetas caem e empilham no vão (vis.add = nomes que entram neste beat,
             vis.moon = "apogee" | "mean"; vis.show_total = mostra a soma) (scale01).
  "inside" : corpo grande Y (vis.big_r_km, vis.big_col) e o pequeno X (vis.small_r_km) com contador de quantos X cabem em Y (vis.count).
Reaproveita render.py (sprites, fontes) e ranking.py (fundo, texto, legendas).
"""
import sys, os, math, json, subprocess, importlib.util, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw
import render as R
import ranking as K

W, H, FPS = 1080, 1920, 30
F, ease, easeio, mix, lerp, text = R.F, R.ease, R.easeio, R.mix, R.lerp, K.text
HANDLE = "@universeinscale"

PL_KM = {"Mercury": 4879, "Venus": 12104, "Mars": 6792, "Jupiter": 142984, "Saturn": 120536, "Uranus": 51118, "Neptune": 49528}
PL_ORDER = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
EARTH_KM, MOON_KM = 12742, 3474.8
GAP = {"apogee": 405500 - 6371 - 1737, "mean": 384400 - 6371 - 1737}
GX, GY0, GY1 = 690, 330, 1480  # gap column: Earth surface at GY0, Moon surface (apogee) at GY1

def load(path):
    spec = importlib.util.spec_from_file_location("sc", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def schedule(beats, durs):
    """global arrival time of each planet: spread evenly over the beat that adds it"""
    arr, acc = {}, 0.0
    for b, d in zip(beats, durs):
        add = b["vis"].get("add", [])
        for i, n in enumerate(add): arr[n] = acc + 0.3 + (d - 0.8) * i / max(1, len(add))
        acc += d
    return arr

def gap_vis(img, v, th, gt, t, dur, arr):
    acc, acc2 = tuple(th["accent"]), tuple(th["accent2"])
    s = (GY1 - GY0) / GAP["apogee"]
    moon_mode = v.get("moon", "apogee")
    mp = easeio((t - 1.0) / 1.5) if moon_mode == "mean" else 0.0
    gap_px = lerp(GAP["apogee"], GAP["mean"], mp) * s
    d = ImageDraw.Draw(img)
    # Earth (to scale) at top, Moon at bottom
    er = EARTH_KM / 2 * s; mr = MOON_KM / 2 * s
    R.paste_c(img, R.radial(140, [(0, (120, 180, 255, 160)), (1, (60, 120, 255, 0))]), GX, GY0 - er)
    R.paste_c(img, R.earth_sprite(max(6, int(er)), glow=None), GX, GY0 - er)
    my = GY0 + gap_px + mr
    R.paste_c(img, R.radial(110, [(0, (230, 230, 240, 150)), (1, (200, 200, 220, 0))]), GX, my)
    R.paste_c(img, R.planet_sprite(max(4, int(mr)), (185, 185, 190)), GX, my)
    d = ImageDraw.Draw(img)
    d.line([(GX - 260, GY0), (GX + 260, GY0)], fill=(90, 140, 255), width=2)
    d.line([(GX - 260, GY0 + gap_px), (GX + 260, GY0 + gap_px)], fill=(200, 200, 215), width=2)
    d.text((GX + 270, GY0 - er), "EARTH", font=F(34, "Black"), fill=(130, 180, 255), anchor="lm")
    d.text((GX + 270, my), "MOON", font=F(34, "Black"), fill=(220, 220, 230), anchor="lm")
    # ghost outlines: where the planets will go (hook teases the answer)
    if v.get("ghost"):
        yg = GY0; dg = ImageDraw.Draw(img)
        for n in PL_ORDER:
            h = PL_KM[n] * s
            if not (n in arr and gt >= arr[n]): K.dashed_circle(dg, GX, yg + h / 2, max(3, h / 2), (150, 170, 200), 3)
            yg += h
        dg.text((GX, GY0 + 0.4 * (GY1 - GY0)), "?", font=F(160, "Black"), fill=acc, anchor="mm") if not arr or gt < min(arr.values()) else None
    # stacked planets
    y = GY0; total = 0
    for n in PL_ORDER:
        if n not in arr or gt < arr[n]: continue
        u = ease((gt - arr[n]) / 0.45)
        h = PL_KM[n] * s; cy = lerp(-200, y + h / 2, u)
        col = R.PCOL[n]
        if n == "Saturn":
            d = ImageDraw.Draw(img); d.ellipse([GX - h * 1.1, cy - h * 0.18, GX + h * 1.1, cy + h * 0.18], outline=(225, 205, 150), width=max(2, int(h * 0.05)))
        R.paste_c(img, R.planet_sprite(max(2, int(h / 2)), col, light=(-0.8, -0.4)), GX, cy)
        d = ImageDraw.Draw(img)
        lx = GX - max(h / 2, 20) - 30
        if n == "Saturn": lx = GX - h * 1.1 - 20
        d.text((lx, cy), n, font=F(36 if h > 40 else 28, "ExtraBold"), fill=col, anchor="rm")
        y += h; total += PL_KM[n]
    # overflow marker
    over = y - (GY0 + gap_px)
    if over > 1:
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rectangle([GX - 200, GY0 + gap_px, GX + 200, y], fill=(255, 70, 70, 110)); img.alpha_composite(lay)
    return total, gap_px / s

def inside_vis(img, v, th, gt, t, dur):
    acc = tuple(th["accent"]); cx, cy = W / 2, 900; Rb = 380
    R.paste_c(img, R.planet_sprite(Rb, tuple(v.get("big_col", (255, 190, 90))), light=(-0.7, -0.4)), cx, cy)
    rs = max(2, Rb * v["small_r_km"] / v["big_r_km"])
    n = int(v.get("count", 1) * easeio((t - 0.4) / max(1.0, dur * 0.7)))
    rng = random.Random(3); d = ImageDraw.Draw(img)
    for i in range(min(n, 900)):
        a = rng.uniform(0, 2 * math.pi); r = Rb * math.sqrt(rng.random()) * 0.95
        x, y = cx + r * math.cos(a), cy + r * math.sin(a); d.ellipse([x - rs, y - rs, x + rs, y + rs], fill=tuple(v.get("small_col", (90, 140, 255))))
    text(img, (W / 2, 330), f"{n:,}", 140, acc)

def chrome(img, th, gt, total):
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, int(W * gt / total), 10], fill=tuple(th["accent"]))
    d.text((W / 2, 1720), HANDLE, font=F(34, "Bold"), fill=R.CYAN, anchor="mm")

def frame(m, durs, gt, chunks, arr):
    th = m.THEME; beats = m.BEATS; total = sum(durs); acc = 0
    for i, (b, d) in enumerate(zip(beats, durs)):
        if gt < acc + d: break
        acc += d
    t = gt - acc; v = b["vis"]
    img = K.bg(gt, th)
    if v["type"] == "gap":
        tot_km, gap_km = gap_vis(img, v, th, gt, t, d, arr)
        # headline (always on: the number is on screen from frame 0)
        hl = v.get("head") or m.BIG
        text(img, (W / 2, 120), hl["num"], 118 if len(hl["num"]) < 12 else 96, tuple(th["accent"]))
        text(img, (W / 2, 215), hl["top"], 50, (255, 255, 255))
        if v.get("show_total"):
            p = 1.0 if v.get("moon") == "mean" else easeio((t - 0.3) / 1.2)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle([20, 1090, 420, 1450], 26, fill=(8, 10, 24, 225), outline=tuple(th["accent"]) + (160,), width=3); img.alpha_composite(lay)
            dd = ImageDraw.Draw(img)
            dd.text((220, 1135), "7 planets, side by side", font=F(28, "Bold"), fill=(200, 205, 220), anchor="mm")
            dd.text((220, 1195), f"{tot_km * p:,.0f} km", font=F(58, "Black"), fill=tuple(th["accent"]), anchor="mm")
            dd.text((220, 1265), "gap tonight" if v.get("moon") == "mean" else "gap, Moon at its farthest", font=F(28, "Bold"), fill=(200, 205, 220), anchor="mm")
            dd.text((220, 1325), f"{gap_km:,.0f} km", font=F(58, "Black"), fill=tuple(th["accent2"]), anchor="mm")
            diff = gap_km - tot_km
            dd.text((220, 1400), (f"{diff:,.0f} km to spare" if diff >= 0 else f"{-diff:,.0f} km too long"), font=F(34, "ExtraBold"), fill=(140, 255, 160) if diff >= 0 else (255, 110, 110), anchor="mm")
        if v.get("sub"): text(img, (W / 2, 290), v["sub"], 40, tuple(th["accent2"]), w="ExtraBold")
    elif v["type"] == "inside":
        inside_vis(img, v, th, gt, t, d)
    chrome(img, th, gt, total)
    K.draw_caption(img, chunks, gt, y=1590)
    return img

def tts(beats, outdir, voice):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(R.HERE, "models/kokoro.onnx"), os.path.join(R.HERE, "models/voices.bin"))
    speed = float(os.environ.get("SPEED", "1.05")); durs, chunks = [], []
    for i, b in enumerate(beats):
        cache = os.path.join(outdir, f"beat_{i:02d}.wav"); key = f"{voice}|{speed}|{b['say']}"
        if os.path.exists(cache) and open(cache + ".txt").read() == key: a, sr = sf.read(cache, dtype="float32")
        else:
            a, sr = k.create(b["say"], voice=voice, speed=speed, lang="en-us"); sf.write(cache, a, sr); open(cache + ".txt", "w").write(key)
        lead = 0.0 if i == 0 else 0.08  # hook starts on frame 0
        a = np.concatenate([np.zeros(int(sr * lead)), a, np.zeros(int(sr * (0.15 if i == len(beats) - 1 else 0.3)))]).astype(np.float32)
        chunks.append(a); durs.append(len(a) / sr)
    audio = np.concatenate(chunks); audio = audio / max(1e-6, np.abs(audio).max()) * 0.89
    tt = np.arange(len(audio)) / sr
    drone = (np.sin(2 * np.pi * 41 * tt) * 0.5 + np.sin(2 * np.pi * 61.5 * tt) * 0.3 + np.sin(2 * np.pi * 82.3 * tt) * 0.2) * 0.035
    audio = (audio + drone).astype(np.float32); audio /= max(1.0, np.abs(audio).max() / 0.95)
    sf.write(os.path.join(outdir, "voice.wav"), audio, sr)
    return durs

def main():
    m = load(sys.argv[1]); outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    if "--preview" in sys.argv:
        durs = [6.0] * len(m.BEATS); arr = schedule(m.BEATS, durs)
        for i in range(len(m.BEATS)):
            for k2, tt in enumerate((0.0, 5.5)):
                frame(m, durs, i * 6 + tt, [], arr).convert("RGB").save(os.path.join(outdir, f"prev_{i:02d}_{k2}.jpg"), quality=80)
        print("preview ok"); return
    durs = tts(m.BEATS, outdir, os.environ.get("VOICE", "af_heart"))
    json.dump(durs, open(os.path.join(outdir, "durs.json"), "w")); total = sum(durs); print("total", round(total, 1), "s")
    arr = schedule(m.BEATS, durs); chunks = []; acc = 0
    for b, d in zip(m.BEATS, durs): chunks += K.caption_chunks(b["say"], acc - (0.2 if acc == 0 else 0), d); acc += d
    out = os.path.join(outdir, "scale.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", os.path.join(outdir, "voice.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(int(total * FPS)):
        p.stdin.write(frame(m, durs, f / FPS, chunks, arr).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("ok", out)

if __name__ == "__main__":
    main()
