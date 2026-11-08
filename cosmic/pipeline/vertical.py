"""Cosmic Scale — corte vertical 9:16 (YouTube Shorts / TikTok / Reels) a partir de um episódio renderizado.
Uso: python3 -I vertical.py epXX.py out/epXX "0,3,9,10,15" "TITLE ON TOP" [saida.mp4]
- usa out/epXX/final.mp4 (ou video.mp4) + durs.json
- fundo estrelado, título no topo, vídeo 16:9 no meio, legenda grande queimada, @ do canal embaixo
- precisa somar > 60 s para contar no TikTok Creator Rewards; Shorts aceita até 3 min
"""
import sys, os, json, re, subprocess, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R

W, H = 1080, 1920
FD = R.FONT_DIR
HANDLE = "@universeinscale"
HEAD_CUT = 0.32  # 08/11: corta o fade/silêncio inicial para o 1º frame já ter imagem e movimento

def wrap(text, font, maxw):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def background(title, path):
    img = R.make_starfield(W, H, 2200, 21).convert("RGBA"); d = ImageDraw.Draw(img)
    f = R.F(88, "Black"); lines = wrap(title.upper(), f, W - 110)
    y = 330 - (len(lines) - 1) * 52
    for i, l in enumerate(lines):
        d.text((W / 2 + 4, y + i * 104 + 5), l, font=f, fill=(0, 0, 0), anchor="mm")
        d.text((W / 2, y + i * 104), l, font=f, fill=R.GOLD if i == len(lines) - 1 else R.WHITE, anchor="mm")
    lg = R.logo_img(70); img.alpha_composite(lg, (int(W / 2 - 230), 1770))
    d.text((W / 2 - 150, 1805), HANDLE, font=R.F(40, "Bold"), fill=R.CYAN, anchor="lm")
    d.text((W / 2, 1700), "Full video on the channel", font=R.F(34, "SemiBold"), fill=R.DIM, anchor="mm")
    img.convert("RGB").save(path)

def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def captions(chunks, path):
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter Black,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,2,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = [f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Cap,,0,0,0,,{{\\pos({W//2},1430)}}{t}" for a, b, t in chunks]
    open(path, "w").write(head + "\n".join(ev) + "\n")

def main():
    script, outdir, idx, title = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")], sys.argv[4]
    out = sys.argv[5] if len(sys.argv) > 5 else os.path.join(outdir, "vertical.mp4")
    src = os.path.join(outdir, "final.mp4") if os.path.exists(os.path.join(outdir, "final.mp4")) else os.path.join(outdir, "video.mp4")
    spec = importlib.util.spec_from_file_location("ep", script); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    durs = json.load(open(os.path.join(outdir, "durs.json")))
    starts = [sum(durs[:i]) for i in range(len(durs))]
    chunks, tl = [], 0.0
    for k0, i in enumerate(idx):
        d = durs[i] - (HEAD_CUT if k0 == 0 else 0); words = ep.SCENES[i]["say"].split()
        groups, g = [], []
        for w in words:
            g.append(w)
            if len(g) >= 4 or re.search(r"[.?!,:]$", w): groups.append(" ".join(g)); g = []
        if g: groups.append(" ".join(g))
        total = sum(len(x) for x in groups); t = tl + (0.0 if k0 == 0 else 0.2); usable = d - (0.5 if k0 == 0 else 0.7)
        for x in groups:
            dd = usable * len(x) / total; chunks.append((t, t + dd, x.upper())); t += dd
        tl += d
    tmp = os.path.join(outdir, "_v"); os.makedirs(tmp, exist_ok=True)
    background(title, os.path.join(tmp, "bg.png")); captions(chunks, os.path.join(tmp, "cap.ass"))
    lst = []
    for k, i in enumerate(idx):
        seg = os.path.join(tmp, f"seg{k:02d}.mp4")
        off = HEAD_CUT if k == 0 else 0.0  # 1st frame = full picture (no fade, no silent lead-in)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{starts[i] + off:.3f}", "-i", src, "-t", f"{durs[i] - off:.3f}",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", seg], check=True)
        lst.append(f"file '{os.path.abspath(seg)}'")
    open(os.path.join(tmp, "list.txt"), "w").write("\n".join(lst))
    cut = os.path.join(tmp, "cut.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"), "-c", "copy", cut], check=True)
    comp = f"[0:v]setpts=PTS-STARTPTS,scale=1080:-2[sv];[1:v][sv]overlay=0:620[o];[o]ass={os.path.join(tmp, 'cap.ass')}:fontsdir={FD}[outv]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", cut, "-loop", "1", "-i", os.path.join(tmp, "bg.png"),
                    "-filter_complex", comp, "-map", "[outv]", "-map", "0:a", "-shortest",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-r", "30",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
    print("ok", out, round(tl, 1), "s")

if __name__ == "__main__":
    main()
