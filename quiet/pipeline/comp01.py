"""The Quiet Archive - COMP01 assembler: "2 Hours of Calm Ancient History for Sleep | Rome, a Monastery & the Nile".
Parts are re-rendered first with sleep.py (comp01_p01/p02 = EP01/EP02 with a 30 s rest that fades to black;
comp01_p03 = EP03 with the single long ambient tail, COMP_TAIL minutes):
  python3 -I sleep.py comp01_p01.py out/p01 ; ... p02 ; COMP_TAIL=34 python3 -I sleep.py comp01_p03.py out/p03
Then:  python3 -I comp01.py out            -> out/comp01/final.mp4, subtitles.srt, chapters.txt
New here: quiet text cards on a near-black "candle haze" ground that dissolve into the next part's first scene,
with a soft ambient bed that rises gently (no cuts, no level jumps; one loudness pass over the whole film).
"""
import os, sys, re, json, subprocess, importlib.util
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
def load(path, name):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
S = load(os.path.join(HERE, "sleep.py"), "sleep")
W, H, FPS, LOOP_S = S.W, S.H, S.FPS, S.LOOP_S
CARD_S = 15
SR = 24000

PARTS = [("p01", "comp01_p01.py", "The First Night", "Ancient Rome", "Rome"),
         ("p02", "comp01_p02.py", "The Second Night", "A Medieval Monastery", "Monastery"),
         ("p03", "comp01_p03.py", "The Third Night", "Beside the Nile", "Nile")]

def dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).decode())

def haze(pal, t):
    """near-black ground with a faint, slowly breathing candle glow low in the frame"""
    c = np.zeros((H, W, 3), np.float32) + np.array(pal["sky_top"], np.float32) * 0.6
    k = 0.10 + 0.02 * np.sin(S.TAU * t / 15.0)
    c += S.radial_glow(W * 0.5, H * 0.86, 520, pal["light"], k)
    return Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).convert("RGBA")

def card(path, pal, scene, seed, kicker, title, sub):
    sc = S.Scene(scene, pal, seed)
    def gen():
        for f in range(CARD_S * FPS):
            t = f / FPS
            im = haze(pal, t)
            fade_in = S.smooth((t - (CARD_S - 4.0)) / 4.0)          # last 4 s: dissolve into the next scene
            if fade_in > 0:
                nxt = sc.frame((LOOP_S - (CARD_S - t)) % LOOP_S); S.brand(nxt, p=pal)
                im = Image.blend(im, nxt, fade_in)
            a = S.smooth((t - 1.5) / 3.0) * (1 - S.smooth((t - (CARD_S - 5.5)) / 3.0))
            S.title_card(im, kicker, title, a, p=pal)
            if a > 0 and sub:
                d = ImageDraw.Draw(im)
                d.text((W / 2, H * 0.44 + 150), sub, font=S.F(34, 400, True), fill=pal["accent"] + (int(200 * a),), anchor="mm")
            yield im
    S.encode(gen(), CARD_S * FPS, path)

def bed(seconds, seed):
    """same ambient bed as sleep.mix_audio, rising from silence over 6 s (previous part has faded its bed out)"""
    from scipy.signal import lfilter
    n = int(round(seconds * SR)); tt = np.arange(n) / SR; rng = np.random.default_rng(seed)
    brown = lfilter([1.0], [1, -0.997], rng.standard_normal(n + SR * 5))
    brown = lfilter([0.06, 0.06], [1, -0.88], brown)[SR * 5:]
    y = brown * 0.0017 * (0.85 + 0.15 * np.sin(S.TAU * tt / 41))
    pad = np.zeros(n)
    for f, a in ((110.0, 0.5), (164.81, 0.32), (220.0, 0.22), (277.18, 0.12)):
        pad += a * np.sin(S.TAU * f * tt + f) * (0.6 + 0.4 * np.sin(S.TAU * tt / (23 + f % 7)))
    y = (y + pad * 0.010) * np.clip(tt / 6.0, 0, 1)
    return y.astype(np.float32)

def srt_items(path):
    out = []
    for blk in open(path).read().strip().split("\n\n"):
        ln = blk.strip().split("\n")
        if len(ln) < 3: continue
        a, b = ln[1].split(" --> ")
        out.append((tsec(a), tsec(b), " ".join(ln[2:])))
    return out

def tsec(x):
    h, m, s = x.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(s)

if __name__ == "__main__":
    root = sys.argv[1]; od = os.path.join(root, "comp01"); os.makedirs(od, exist_ok=True)
    vids, wavs, subs, chaps, t = [], [], [], [], 0.0
    for i, (pid, epf, kick, title, short) in enumerate(PARTS):
        ep = load(os.path.join(HERE, epf), "ep_" + pid)
        pal = dict(S.PAL); pal.update(getattr(ep, "PALETTE", {}))
        cpath = os.path.join(od, f"card_{i}.mp4")
        if i == 0:
            ck, ct, cs = "The Quiet Archive", "Three Quiet Nights in History", "Rome  ·  a Monastery  ·  the Nile"
        else:
            ck, ct, cs = kick, title, ""
        if not os.path.exists(cpath):
            card(cpath, pal, ep.CHAPTERS[0]["scene"], 100 + getattr(ep, "SEED", 0), ck, ct, cs)
        cd = dur(cpath); vids.append(cpath); wavs.append(bed(cd, 50 + i))
        if i == 0: chaps.append((0.0, "Welcome: Three Quiet Nights"))
        t += cd
        pdir = os.path.join(root, pid); sil = os.path.join(pdir, "silent.mp4"); pd = dur(sil)
        a, sr = sf.read(os.path.join(pdir, "mix.wav"), dtype="float32"); assert sr == SR
        n = int(round(pd * SR)); a = a[:n] if len(a) >= n else np.concatenate([a, np.zeros(n - len(a), np.float32)])
        vids.append(sil); wavs.append(a)
        tl = json.load(open(os.path.join(pdir, "timeline.json")))
        for c in tl["chapters"]:
            if c.get("tail") and i < len(PARTS) - 1: continue
            label = c["title"] if not c.get("tail") else "Rest: Gentle Ambience"
            if c is tl["chapters"][0]: label = f"{short}: {label}" if short.lower() not in label.lower() else label
            chaps.append((t + c["start"], label))
        subs += [(t + s0, t + s1, x) for s0, s1, x in srt_items(os.path.join(pdir, "subtitles.srt"))]
        t += pd
        print(f"part {pid}: starts {S.mmss(t - pd)} len {S.mmss(pd)}", flush=True)
    total = t
    listf = os.path.join(od, "list.txt"); open(listf, "w").write("".join(f"file '{os.path.abspath(v)}'\n" for v in vids))
    sil = os.path.join(od, "silent.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", listf, "-c", "copy", sil], check=True)
    mixp = os.path.join(od, "mix.wav"); sf.write(mixp, np.clip(np.concatenate(wavs), -1, 1), SR, subtype="PCM_16")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", sil, "-i", mixp, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-af", "loudnorm=I=-19:TP=-2:LRA=9", "-ar", "48000", "-c:a", "aac", "-b:a", "64k", "-ac", "1",
                    "-t", f"{total:.2f}", "-movflags", "+faststart", os.path.join(od, "final.mp4")], check=True)
    with open(os.path.join(od, "subtitles.srt"), "w") as fo:
        fo.write("\n".join(f"{k}\n{S.ts(a)} --> {S.ts(b)}\n{x}\n" for k, (a, b, x) in enumerate(subs, 1)))
    open(os.path.join(od, "chapters.txt"), "w").write("".join(f"{S.mmss(s)} {x}\n" for s, x in chaps))
    print("total", S.mmss(total), "| ok", os.path.getsize(os.path.join(od, "final.mp4")) // 1_000_000, "MB")
