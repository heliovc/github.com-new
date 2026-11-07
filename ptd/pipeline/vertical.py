"""Corte vertical 9:16 (TikTok / Reels / Shorts) a partir de um episódio já renderizado.
Uso: python3 vertical.py epXX_script.py out/epXX "0,6,7,9" "TÍTULO NO TOPO" [saida.mp4]
- usa out/epXX/video.mp4 + durs.json
- legenda grande queimada (palavras em blocos), título fixo no topo, @ do canal embaixo
"""
import sys, os, json, re, subprocess, importlib.util
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FD = "/usr/share/fonts/opentype/inter/"
HANDLE = "@portrazdodinheiro"
BG1, GREEN, AMBER, WHITE = (11, 18, 32), (58, 196, 125), (242, 169, 59), (240, 244, 250)

def F(s, w="Black"): return ImageFont.truetype(FD + f"Inter-{w}.otf", s)

def wrap(text, font, maxw):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def background(title, path):
    img = Image.new("RGB", (W, H), BG1); d = ImageDraw.Draw(img)
    for y in range(H):
        c = int(12 + 14 * (1 - abs(y - 700) / 1200)); d.line([(0, y), (W, y)], fill=(c - 2, c + 4, c + 22))
    f = F(84); lines = [l.replace(" ", " ") for l in wrap(title.upper().replace("R$ ", "R$ ").replace("US$ ", "US$ "), f, W - 120)]
    y = 330 - (len(lines) - 1) * 50
    for i, l in enumerate(lines):
        d.text((W / 2, y + i * 100), l, font=f, fill=AMBER if i == len(lines) - 1 else WHITE, anchor="mm")
    d.rounded_rectangle([W / 2 - 250, 1780, W / 2 - 200, 1830], 12, fill=GREEN)
    d.text((W / 2 - 225, 1806), "$", font=F(40), fill=BG1, anchor="mm")
    d.text((W / 2 - 180, 1805), HANDLE, font=F(40, "Bold"), fill=GREEN, anchor="lm")
    img.save(path)

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
Style: Cap,Inter Black,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,2,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    for t0, t1, txt in chunks:
        ev.append(f"Dialogue: 0,{ass_time(t0)},{ass_time(t1)},Cap,,0,0,0,,{{\\pos({W//2},1420)}}{txt}")
    open(path, "w").write(head + "\n".join(ev) + "\n")

def main():
    script, outdir, idx, title = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(",")], sys.argv[4]
    out = sys.argv[5] if len(sys.argv) > 5 else os.path.join(outdir, "vertical.mp4")
    spec = importlib.util.spec_from_file_location("ep", script); ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
    durs = json.load(open(os.path.join(outdir, "durs.json")))
    starts = [sum(durs[:i]) for i in range(len(durs))]
    chunks, tl = [], 0.0
    for i in idx:
        d = durs[i]; words = ep.SCENES[i]["say"].replace("M D R", "MDR").split()
        groups, g = [], []
        for w in words:
            g.append(w)
            if len(g) >= 4 or re.search(r"[.?!,:]$", w): groups.append(" ".join(g)); g = []
        if g: groups.append(" ".join(g))
        total = sum(len(x) for x in groups); t = tl + 0.15; usable = d - 0.6
        for x in groups:
            dd = usable * len(x) / total; chunks.append((t, t + dd, x.upper())); t += dd
        tl += d
    tmp = os.path.join(outdir, "_v"); os.makedirs(tmp, exist_ok=True)
    background(title, os.path.join(tmp, "bg.png")); captions(chunks, os.path.join(tmp, "cap.ass"))
    lst = []
    for k, i in enumerate(idx):
        seg = os.path.join(tmp, f"seg{k:02d}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{starts[i]:.3f}", "-i", os.path.join(outdir, "video.mp4"),
                        "-t", f"{durs[i]:.3f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-b:a", "192k", seg], check=True)
        lst.append(f"file '{os.path.abspath(seg)}'")
    open(os.path.join(tmp, "list.txt"), "w").write("\n".join(lst))
    cut = os.path.join(tmp, "cut.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "list.txt"), "-c", "copy", cut], check=True)
    comp = (f"[0:v]scale=1080:-2[sv];[1:v][sv]overlay=0:620[o];"
            f"[o]ass={os.path.join(tmp, 'cap.ass')}:fontsdir={FD}[outv]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", cut, "-loop", "1", "-i", os.path.join(tmp, "bg.png"),
           "-filter_complex", comp, "-map", "[outv]", "-map", "0:a", "-shortest",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-r", "30",
           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    print("ok", out, round(tl, 1), "s")

if __name__ == "__main__":
    main()
