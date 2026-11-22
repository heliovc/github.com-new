"""Canal 5 — "E se você fosse…" — motor dos Shorts POV animal (1080x1920, 30 fps, PT-BR).

Fluxo: <episódio>/script.json -> voz Kokoro (pf_dora) frase a frase + tempo por palavra -> cenas desenhadas por
código (pipeline/scenes/<modulo>.py) -> legendas queimadas 1–3 palavras (62% da altura), HUD de escala, etiquetas
-> trilha e SFX sintetizados (audio.py) -> video.mp4 + capa.jpg + legendas.srt + timeline.json + publish.draft.json

Uso (de qualquer pasta):
  python3 -I canal5/pipeline/engine.py canal5/d01a-formiga             render completo
  python3 -I canal5/pipeline/engine.py canal5/d01a-formiga --sheet     folha de contato (revisão sem vídeo)
  python3 -I canal5/pipeline/engine.py canal5/d01a-formiga --stills 0,4.2,12.5
  opções: --workers N (padrão: núcleos-1)  --draft (renderiza em 540x960 para conferir rápido)

script.json (ver d01a-formiga/script.json):
  voice, speed, scene_module, say_map {"30º": "trigésimo"}, music {bpm, root, prog, seed, inst},
  hud_series, beats [{scene, text ("*palavra*" = destaque amarelo), pause_before?, payoff?}],
  scenes {id: {hud, labels [{text, at, emoji?, style?}], sfx_cut, sfx [{type, at, gain, ...}], vision?, ...}},
  cover {t, title}, publish {...}, sources [...]
"""
import sys, os, re, json, math, hashlib, subprocess, importlib, time, shutil, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFilter

import art as A
import audio as AU

W, H, FPS = A.W, A.H, 30
SR = AU.SR
CAP_Y = 1195           # linha de base das legendas (~62% da altura)
LABEL_Y = 395          # etiqueta da cena (abaixo do HUD)
YELLOW = A.YELLOW
PUNCT_END = re.compile(r"[,.;:!?…—]+$")


# ------------------------------------------------------------------ ffmpeg
def ffmpeg_bin():
    p = shutil.which("ffmpeg")
    if p: return p
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


# ------------------------------------------------------------------ texto
def parse_text(text):
    toks = []
    for i, seg in enumerate(text.split("*")):
        for j, w in enumerate(seg.split()):
            if toks and re.fullmatch(r"[,.;:!?…—]+", w) and (j > 0 or not seg.startswith(" ")):
                toks[-1]["w"] += w  # pontuação colada na palavra anterior (ex.: "*andar*.")
                continue
            toks.append({"w": w, "key": i % 2 == 1, "num": bool(re.search(r"\d", w))})
    return toks


def core(w):
    return PUNCT_END.sub("", w).strip("\"“”()")


def norm(w):
    return core(w).lower()


def spoken(w, say_map):
    c = core(w)
    tail = w[w.find(c) + len(c):] if c and c in w else ""
    return say_map.get(c, c) + tail


VOW = re.compile(r"[aeiouáéíóúâêôãõàüy]+", re.I)


def syl(s):
    return max(1, len(VOW.findall(s)))


def cap_text(w):
    c = re.sub(r"[,.;:—]+$", "", w).strip("\"“”()")
    return c.upper()


# ------------------------------------------------------------------ voz
def kokoro_paths():
    for d in (os.environ.get("KOKORO_DIR", ""), os.path.join(HERE, "models"), os.path.expanduser("~/.cache/kokoro")):
        if not d: continue
        for m, v in (("kokoro-v1.0.onnx", "voices-v1.0.bin"), ("kokoro.onnx", "voices.bin"),
                     ("kokoro-v1.0.int8.onnx", "voices-v1.0.bin")):
            if os.path.exists(os.path.join(d, m)) and os.path.exists(os.path.join(d, v)):
                return os.path.join(d, m), os.path.join(d, v)
    raise FileNotFoundError("modelos Kokoro não encontrados: rode canal5/setup.sh")


_K = None


def synth_kokoro(text, voice, speed, cache):
    global _K
    h = hashlib.sha1(f"{voice}|{speed}|{text}".encode()).hexdigest()[:14]
    p = os.path.join(cache, f"tts_{h}.wav")
    if not os.path.exists(p):
        if _K is None:
            from kokoro_onnx import Kokoro
            _K = Kokoro(*kokoro_paths())
        a, sr = _K.create(text, voice=voice, speed=speed, lang="pt-br")
        sf.write(p, AU.resample(np.asarray(a, dtype=np.float32), sr, SR), SR)
    a, _ = sf.read(p, dtype="float32")
    return a, None


def synth_edge(text, voice, rate, cache):
    """voz neural PT-BR (Microsoft, via edge-tts) + limites de palavra [(início s, duração s, texto)]"""
    h = hashlib.sha1(f"edge|{voice}|{rate}|{text}".encode()).hexdigest()[:14]
    p = os.path.join(cache, f"tts_{h}.wav"); pj = p[:-4] + ".json"
    if not (os.path.exists(p) and os.path.exists(pj)):
        import asyncio, io, ssl, edge_tts
        if os.environ.get("SSL_CERT_FILE"):  # nuvem com proxy: confia no certificado do proxy (edge-tts usa certifi fixo)
            import edge_tts.communicate as _etc
            _etc._SSL_CTX = ssl.create_default_context(cafile=os.environ["SSL_CERT_FILE"])

        async def go():
            c = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
            audio, wb = bytearray(), []
            async for ch in c.stream():
                if ch["type"] == "audio": audio += ch["data"]
                elif ch["type"] == "WordBoundary": wb.append((ch["offset"] / 1e7, ch["duration"] / 1e7, ch["text"]))
            return bytes(audio), wb

        err = None
        for attempt in range(4):
            try:
                audio, wb = asyncio.run(go())
                if audio: break
            except Exception as e:  # rede instável: tenta de novo
                err = e
            time.sleep(2 + 3 * attempt)
        else:
            raise RuntimeError(f"edge-tts falhou: {err}")
        a, sr = sf.read(io.BytesIO(audio), dtype="float32")
        if a.ndim > 1: a = a.mean(axis=1)
        sf.write(p, AU.resample(a, sr, SR), SR)
        json.dump(wb, open(pj, "w", encoding="utf-8"), ensure_ascii=False)
    a, _ = sf.read(p, dtype="float32")
    return a, json.load(open(pj, encoding="utf-8"))


def synth(text, S, b, cache):
    tts = S.get("tts", {"engine": "kokoro", "voice": S.get("voice", "pf_dora")})
    if tts.get("engine") == "edge":
        return synth_edge(text, tts.get("voice", "pt-BR-ThalitaMultilingualNeural"), b.get("rate", tts.get("rate", "+0%")), cache)
    return synth_kokoro(text, tts.get("voice", "pf_dora"), b.get("speed", S.get("speed", 0.92)), cache)


def trim_idx(a, rel=0.02, pad=0.025):
    env = np.abs(a); idx = np.where(env > rel * env.max())[0]
    if len(idx) == 0: return 0, len(a)
    return max(0, idx[0] - int(pad * SR)), min(len(a), idx[-1] + int(pad * SR))


def times_from_boundaries(toks, wb, lead, dur, say_map):
    """casa os limites de palavra do TTS com as palavras da legenda (um limite pode cobrir 2+ palavras, ex. '6 km/h')"""
    out, k = [], 0
    for (o, d, txt) in wb:
        n = max(1, len(txt.split()))
        group = toks[k:k + n]
        if len(group) < n: return None
        ws = [syl(spoken(t["w"], say_map)) + 0.35 for t in group]; tot = sum(ws); acc = o - lead
        for t, wgt in zip(group, ws):
            dd = d * wgt / tot; out.append((acc, acc + dd)); acc += dd
        k += n
    if k != len(toks): return None
    res = []
    for i, (a0, a1) in enumerate(out):
        nxt = out[i + 1][0] if i + 1 < len(out) else dur
        res.append((max(0.0, a0), max(a0 + 0.05, min(max(a1, a0 + 0.05), nxt))))
    return res


def trim(a, rel=0.02, pad=0.025):
    env = np.abs(a); idx = np.where(env > rel * env.max())[0]
    if len(idx) == 0: return a
    return a[max(0, idx[0] - int(pad * SR)): min(len(a), idx[-1] + int(pad * SR))]


def word_times(a, toks, say_map):
    """tempo de cada palavra dentro da frase: pausas reais do áudio nas vírgulas + peso por sílaba"""
    n = len(toks); dur = len(a) / SR
    hop = int(SR * 0.01); m = len(a) // hop
    env = np.sqrt(np.mean(a[:m * hop].reshape(m, hop) ** 2, axis=1)) + 1e-9
    sil = env < 0.08 * np.percentile(env, 95)
    gaps = []; i = 0
    while i < m:
        if sil[i]:
            j = i
            while j < m and sil[j]: j += 1
            if i > 6 and j < m - 6 and j - i >= 6: gaps.append((i * 0.01, j * 0.01))
            i = j
        else:
            i += 1
    P = [k for k in range(n - 1) if PUNCT_END.search(toks[k]["w"])]
    cuts = {}
    if P and len(gaps) >= len(P):
        chosen = sorted(sorted(gaps, key=lambda g: g[0] - g[1])[:len(P)])
        cuts = dict(zip(P, chosen))
    times = [None] * n; st = 0; t0 = 0.0
    for k in range(n):
        if k in cuts or k == n - 1:
            t1 = cuts[k][0] if k in cuts else dur
            ws = []
            for j in range(st, k + 1):
                wgt = syl(spoken(toks[j]["w"], say_map)) + 0.35
                if not cuts and j < k and PUNCT_END.search(toks[j]["w"]): wgt += 1.1
                ws.append(wgt)
            tot = sum(ws); acc = t0
            for j, wgt in zip(range(st, k + 1), ws):
                d = (t1 - t0) * wgt / tot; times[j] = (acc, acc + d); acc += d
            st = k + 1; t0 = cuts[k][1] if k in cuts else dur
    return times


# ------------------------------------------------------------------ linha do tempo
def build_timeline(ep):
    S = json.load(open(os.path.join(ep, "script.json"), encoding="utf-8"))
    say_map = S.get("say_map", {})
    cache = os.path.join(ep, ".cache"); os.makedirs(cache, exist_ok=True)
    words, beats, pieces = [], [], []
    t = 0.03
    for bi, b in enumerate(S["beats"]):
        toks = parse_text(b["text"])
        edge = S.get("tts", {}).get("engine") == "edge"
        if b.get("say"): say = b["say"]
        elif edge: say = " ".join(tk["w"] for tk in toks)   # a voz neural lê números e unidades sozinha
        else: say = " ".join(spoken(tk["w"], say_map) for tk in toks)
        raw, wb = synth(say, S, b, cache)
        i0, i1 = trim_idx(raw); a = raw[i0:i1]
        if bi > 0:
            prev = S["beats"][bi - 1]["text"].rstrip()
            t += b.get("pause_before", 0.07 if prev.endswith((",", ":", "…")) and not b.get("payoff") else 0.15)
        start = t
        wt = times_from_boundaries(toks, wb, i0 / SR, len(a) / SR, say_map) if (wb and not b.get("say")) else None
        if wt is None: wt = word_times(a, toks, say_map)
        for tk, (w0, w1) in zip(toks, wt):
            words.append(dict(w=tk["w"], key=tk["key"], num=tk["num"], t0=round(start + w0, 3),
                              t1=round(start + w1, 3), beat=bi))
        beats.append(dict(scene=b["scene"], t0=round(start, 3), t1=round(start + len(a) / SR, 3),
                          payoff=bool(b.get("payoff"))))
        pieces.append((start, a))
        t = start + len(a) / SR
    total = round(t + S.get("tail", 0.55), 3)
    voice = np.zeros(int(total * SR) + 1, dtype=np.float32)
    for st, a in pieces:
        i = int(st * SR); voice[i:i + len(a)] += a[:len(voice) - i]
    scenes = []
    for bi, b in enumerate(beats):
        if not scenes or scenes[-1]["id"] != b["scene"]:
            scenes.append(dict(id=b["scene"], t0=0.0 if not scenes else round(b["t0"] - 0.05, 3), beats=[bi]))
        else:
            scenes[-1]["beats"].append(bi)
    for i, s in enumerate(scenes):
        s["t1"] = scenes[i + 1]["t0"] if i + 1 < len(scenes) else total
    T = dict(total=total, words=words, beats=beats, scenes=scenes, chunks=make_chunks(words))
    json.dump(T, open(os.path.join(ep, "timeline.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return S, T, voice


def make_chunks(words):
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        L = sum(len(core(words[j]["w"])) for j in cur)
        nxt = words[i + 1] if i + 1 < len(words) else None
        end = (PUNCT_END.search(w["w"]) is not None) or len(cur) == 3 or L >= 13 or nxt is None
        if nxt is not None and not end:
            if nxt["beat"] != w["beat"] or L + len(core(nxt["w"])) > 15: end = True
            elif (nxt["num"] or nxt["key"]) and not (w["key"] or w["num"]) and len(cur) >= 2: end = True
        if end: groups.append(cur); cur = []
    out = []
    for k, g in enumerate(groups):
        t0 = words[g[0]]["t0"]
        t1 = words[groups[k + 1][0]]["t0"] if k + 1 < len(groups) else words[g[-1]]["t1"] + 0.5
        t1 = min(t1, words[g[-1]]["t1"] + 0.4)
        out.append(dict(ix=g, t0=t0, t1=t1))
    return out


# ------------------------------------------------------------------ contexto das cenas
class Ctx:
    def __init__(self, S, T, sc, idx):
        self.S, self.T, self.sc, self.idx = S, T, sc, idx
        self.t0, self.t1 = sc["t0"], sc["t1"]; self.dur = self.t1 - self.t0
        self.p = S["scenes"].get(sc["id"], {})
        self.words = [w for w in T["words"] if w["beat"] in sc["beats"]]
        self.gt = 0.0

    def wt(self, sub, n=0, end=False, default=None):
        """tempo LOCAL (s desde o início da cena) da n-ésima palavra que contém 'sub'"""
        sub = sub.lower(); k = 0
        exact = sub.startswith("=")
        if exact: sub = sub[1:]
        for w in self.words:
            if (norm(w["w"]) == sub) if exact else (sub in norm(w["w"])):
                if k == n: return (w["t1"] if end else w["t0"]) - self.t0
                k += 1
        return default if default is not None else self.dur * 0.5

    def beat_t(self, j, end=False):
        b = self.T["beats"][self.sc["beats"][min(j, len(self.sc["beats"]) - 1)]]
        return (b["t1"] if end else b["t0"]) - self.t0


# ------------------------------------------------------------------ sobreposições
_WC, _HC, _LC = {}, {}, {}


def word_img(txt, size, col):
    key = (txt, size, col)
    if key not in _WC:
        f = A.F(size, "anton"); st = max(7, size // 10)
        x0, y0, x1, y1 = f.getbbox(txt, anchor="ls", stroke_width=st)
        asc, desc = f.getmetrics()
        im = Image.new("RGBA", (x1 - x0 + 30, asc + desc + 2 * st + 30))
        d = ImageDraw.Draw(im)
        bx, by = 12 - x0, 12 + st + asc
        d.text((bx + 6, by + 8), txt, font=f, fill=(0, 0, 0, 120), anchor="ls", stroke_width=st, stroke_fill=(0, 0, 0, 120))
        d.text((bx, by), txt, font=f, fill=col, anchor="ls", stroke_width=st, stroke_fill=(0, 0, 0))
        _WC[key] = (im, by, x1 - x0 + 24)
    return _WC[key]


def draw_caption(img, T, gt, base=112):
    ch = next((c for c in T["chunks"] if c["t0"] - 0.03 <= gt < c["t1"]), None)
    if ch is None: return
    parts = []
    for i in ch["ix"]:
        w = T["words"][i]
        if not (w["t0"] <= gt + 0.03 or i == ch["ix"][0]): continue
        size = int(base * 1.3) if w["num"] else base
        col = YELLOW if (w["key"] or w["num"]) else (255, 255, 255)
        parts.append((i, *word_img(cap_text(w["w"]), size, col)))
    sp = 24
    # largura do bloco inteiro define a escala (evita "pulo" de tamanho quando entra palavra nova)
    full = 0
    for i in ch["ix"]:
        w = T["words"][i]
        full += word_img(cap_text(w["w"]), int(base * 1.3) if w["num"] else base,
                         YELLOW if (w["key"] or w["num"]) else (255, 255, 255))[2] + sp
    sc = min(1.0, 880 / max(1, full - sp))
    tot = sum(p[3] for p in parts) + sp * (len(parts) - 1)
    x = W / 2 - tot * sc / 2
    for (i, im, by, wd) in parts:
        w = T["words"][i]
        age = gt - w["t0"]; pop = 1 + 0.2 * max(0.0, 1 - age / 0.11)
        s = sc * pop
        im2 = im if abs(s - 1) < 1e-3 else im.resize((int(im.width * s), int(im.height * s)), Image.BICUBIC)
        cx = x + wd * sc / 2
        A.paste(img, im2, cx - (12 + (wd - 24) / 2) * s, CAP_Y - by * s)
        x += (wd + sp) * sc


def hud_img(series, line, accent):
    key = (series, line, accent)
    if key not in _HC:
        f1, f2 = A.F(28, "mont-ExtraBold"), A.F(40, "mont-Bold")
        wd = int(max(f1.getlength(series), f2.getlength(line)) + 70)
        ss = A.SS(wd + 12, 136, s=2)
        ss.rrect(6, 6, 6 + wd, 130, 26, fill=(14, 10, 24, 175), ink=(255, 255, 255, 60), w=2)
        ss.text((40, 44), series, 28, "mont-ExtraBold", fill=accent, anchor="lm")
        ss.text((40, 94), line, 40, "mont-Bold", fill=(255, 255, 255), anchor="lm")
        # régua
        ss.line([(20, 30), (20, 112)], (255, 255, 255, 170), 3)
        for k in range(5): ss.line([(20, 30 + k * 20.5), (28 if k % 2 else 32, 30 + k * 20.5)], (255, 255, 255, 170), 3)
        _HC[key] = ss.get()
    return _HC[key]


def label_img(lab, accent):
    key = (lab.get("text"), lab.get("emoji"), lab.get("style"), accent)
    if key not in _LC:
        if lab.get("style") == "vision":
            _LC[key] = A.sticker(lab["text"], size=50, fg=(255, 255, 255), bg=(150, 40, 200),
                                 hi=(255, 236, 90), ink=(255, 255, 255), iw=4)
        else:
            _LC[key] = A.sticker(lab["text"], size=54, fg=A.INK, bg=(255, 255, 255), hi=accent,
                                 emoji_code=lab.get("emoji"))
    return _LC[key]


def draw_overlays(img, S, T, ctx, gt, lt, captions=True):
    p = ctx.p; accent = tuple(S.get("accent", (230, 60, 80)))
    hud = p.get("hud", S.get("hud"))
    if hud:
        h = hud_img(S.get("hud_series", "E SE VOCÊ FOSSE…"), hud, accent)
        A.paste(img, h, 56, 150)
    labs = p.get("labels", [])
    cur = None
    for lab in labs:
        at = lab.get("at", 0)
        t_at = ctx.wt(at) if isinstance(at, str) else float(at)
        if lt >= t_at - 0.05: cur = (lab, t_at)
    if cur:
        lab, t_at = cur
        im = label_img(lab, accent)
        u = A.back((lt - t_at) / 0.28)
        A.paste_t(img, im, W / 2, LABEL_Y, scale=max(0.05, 0.55 + 0.45 * u), rot=-2.2, alpha=A.clamp01((lt - t_at) / 0.1 + 0.3))
    if captions: draw_caption(img, T, gt)


# ------------------------------------------------------------------ quadro
class Renderer:
    def __init__(self, ep, S=None, T=None):
        self.ep = ep
        if S is None:
            S = json.load(open(os.path.join(ep, "script.json"), encoding="utf-8"))
            T = json.load(open(os.path.join(ep, "timeline.json"), encoding="utf-8"))
        self.S, self.T = S, T
        self.mod = importlib.import_module("scenes." + S["scene_module"])
        self.ctxs = [Ctx(S, T, sc, i) for i, sc in enumerate(T["scenes"])]
        if hasattr(self.mod, "setup"): self.mod.setup(self.S, self.T, self.ctxs)

    def scene_at(self, gt):
        for c in self.ctxs:
            if c.t0 <= gt < c.t1: return c
        return self.ctxs[-1]

    def frame(self, i, captions=True, overlays=True):
        gt = i / FPS
        ctx = self.scene_at(gt); lt = gt - ctx.t0; ctx.gt = gt
        fn = getattr(self.mod, ctx.p.get("fn", ctx.sc["id"]))
        img = fn(ctx, lt).convert("RGBA")
        vis = ctx.p.get("vision")
        if vis and vis.get("type") == "compound":
            a0 = ctx.wt(vis["from"]) if isinstance(vis.get("from"), str) else vis.get("from", 0.0)
            a1 = ctx.wt(vis["to"]) if isinstance(vis.get("to"), str) else vis.get("to", ctx.dur + 1)
            amt = A.clamp01((lt - a0) / 0.18) * (1 - A.clamp01((lt - a1) / 0.18))
            img = A.compound_eye(img, cell=vis.get("cell", 34), amount=amt)
        if ctx.idx > 0 and lt < 0.22 and not ctx.p.get("no_punch"):
            u = lt / 0.22
            img = A.cam(img, zoom=1 + 0.07 * (1 - A.ease(u)))
            if lt < 0.1:
                fl = Image.new("RGBA", img.size, (255, 255, 255, int(110 * (1 - lt / 0.1))))
                img.alpha_composite(fl)
        if overlays: draw_overlays(img, self.S, self.T, ctx, gt, lt, captions)
        return img.convert("RGB")


# ------------------------------------------------------------------ render paralelo
_R = None


def _init(ep):
    global _R
    _R = Renderer(ep)


def _segment(args):
    k, a, b, out, draft = args
    sz = (W // 2, H // 2) if draft else (W, H)
    cmd = [ffmpeg_bin(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{sz[0]}x{sz[1]}",
           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-g", "60", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(a, b):
        im = _R.frame(i)
        if draft: im = im.resize(sz, Image.BILINEAR)
        p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
    return k


def render_audio(S, T, voice, ep):
    total = T["total"]
    mus = AU.music(total, **S.get("music", {}))
    events = []
    ctxs = [Ctx(S, T, sc, i) for i, sc in enumerate(T["scenes"])]
    for c in ctxs:
        p = c.p
        cut = p.get("sfx_cut", "whoosh" if c.idx > 0 else None)
        if cut: events.append((cut, c.t0 - 0.12, p.get("sfx_cut_gain", -13.0), {"seed": c.idx}))
        for ev in p.get("sfx", []):
            at = ev.get("at", 0)
            t = c.wt(at) if isinstance(at, str) else float(at)
            prm = {k: v for k, v in ev.items() if k not in ("type", "at", "gain")}
            if prm.get("d") == "scene": prm["d"] = c.dur - t + 0.2
            events.append((ev["type"], c.t0 + t, ev.get("gain", -14.0), prm))
    pay = next((b["t0"] for b in T["beats"] if b["payoff"]), None)
    out = AU.mix(voice, mus, events, total, pay, S.get("music_db", -20.0))
    path = os.path.join(ep, ".cache", "audio.wav")
    sf.write(path, out, SR)
    return path


def write_srt(T, path):
    def ts(t):
        ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    lines = []
    for k, c in enumerate(T["chunks"], 1):
        txt = " ".join(core(T["words"][i]["w"]) for i in c["ix"])
        lines += [str(k), f"{ts(c['t0'])} --> {ts(c['t1'])}", txt, ""]
    open(path, "w", encoding="utf-8").write("\n".join(lines))


def _title_line(d, cx, y, ln, size):
    """linha de título em Anton; o "º" sai pequeno e alto (a fonte não tem o ordinal bem desenhado)"""
    f, fo = A.F(size, "anton"), A.F(int(size * 0.5), "anton")
    parts = ln.split("º")
    wid = sum(f.getlength(p) for p in parts) + fo.getlength("o") * (len(parts) - 1)
    x = cx - wid / 2; top = y - size * 0.5
    for k, p in enumerate(parts):
        d.text((x, y), p, font=f, fill=(255, 255, 255), anchor="lm", stroke_width=12, stroke_fill=(0, 0, 0))
        x += f.getlength(p)
        if k < len(parts) - 1:
            d.text((x + 4, top + size * 0.08), "o", font=fo, fill=(255, 255, 255), anchor="lt", stroke_width=8,
                   stroke_fill=(0, 0, 0))
            x += fo.getlength("o") + 8


def _cover_v1(R, path):
    """capa: cena aproximada no bicho + faixa "E SE VOCÊ FOSSE…" + título + selo "VOCÊ" apontando para o bicho.
    script.json -> cover: {t, title[], focus:[x,y] (onde o bicho está no quadro t), zoom, r (raio do anel),
    at:[x,y] (onde o bicho fica na capa; padrão 540,1240)}"""
    S = R.S; cv = S.get("cover", {})
    img = R.frame(int(cv.get("t", 1.0) * FPS), captions=False, overlays=False).convert("RGBA")
    fx, fy = cv.get("focus", [W / 2, H * 0.62]); px, py = cv.get("at", [W / 2, 1240]); z = cv.get("zoom", 1.0)
    img = A.cam(img, zoom=z, dx=px - fx, dy=py - fy, cx=fx, cy=fy)
    shade = A.vgrad(W, H, [(0, (0, 0, 0, 200)), (0.36, (0, 0, 0, 40)), (0.52, (0, 0, 0, 0)), (0.85, (0, 0, 0, 0)),
                           (1, (0, 0, 0, 170))])
    img.alpha_composite(shade)
    acc = tuple(S.get("accent", (230, 60, 80)))
    # anel de destaque em volta do bicho
    r = cv.get("r", 260)
    ring = A.SS(W, H, s=2)
    ring.ellipse(px, py, r, r * 0.8, ink=YELLOW, w=14)
    img.alpha_composite(ring.get())
    # selo "VOCÊ" com seta: você = o bicho
    tag = A.sticker("VOCÊ", size=78, fg=(0, 0, 0), bg=YELLOW, pad=(34, 14), radius=26, iw=7).rotate(6, expand=True,
                                                                                                     resample=Image.BICUBIC)
    sx = int(px + r * 0.55); sy = int(py - r * 0.8 - 210)
    lines = cv.get("title", ["?"]); size = 158 if max(len(l) for l in lines) <= 12 else 140
    y_title_end = 420 + int(size * 1.06) * (len(lines) - 1) + size // 2
    sx = min(sx, W - tag.width // 2 - 30); sy = max(sy, y_title_end + tag.height // 2 + 40)
    ar = A.SS(W, H, s=2)
    A.arrow(ar, sx - 30, sy + tag.height // 2 - 10, px + r * 0.35, py - r * 0.6, YELLOW, w=26, iw=6)
    img.alpha_composite(ar.get())
    A.paste_c(img, tag, sx, sy)
    # faixa da série
    band = A.sticker("E SE VOCÊ FOSSE…", size=86, fg=(0, 0, 0), bg=YELLOW, pad=(40, 18), radius=18, iw=8)
    band = band.rotate(-2.5, expand=True, resample=Image.BICUBIC)
    A.paste_c(img, band, W // 2, 235)
    d = ImageDraw.Draw(img)
    y = 420
    for ln in lines:
        _title_line(d, W / 2, y, ln, size); y += int(size * 1.06)
    d.text((W / 2, H - 120), "NA PELE DE", font=A.F(54, "mont-Black"), fill=(255, 255, 255), anchor="mm",
           stroke_width=6, stroke_fill=(0, 0, 0))
    img.convert("RGB").save(path, quality=92)


def _title_rich(d, cx, y, ln, size, base=(255, 255, 255), hi=YELLOW):
    """linha de título em Anton com *destaque* (amarelo) e "º" pequeno e alto"""
    f, fo = A.F(size, "anton"), A.F(int(size * 0.5), "anton")
    segs = [(seg, k % 2 == 1) for k, seg in enumerate(ln.split("*")) if seg]
    def seg_w(t):
        parts = t.split("º")
        return sum(f.getlength(p) for p in parts) + (fo.getlength("o") + 8) * (len(parts) - 1)
    x = cx - sum(seg_w(t) for t, _ in segs) / 2; top = y - size * 0.5
    for t, h in segs:
        col = hi if h else base
        parts = t.split("º")
        for k, p in enumerate(parts):
            d.text((x, y), p, font=f, fill=col, anchor="lm", stroke_width=max(8, size // 13), stroke_fill=(0, 0, 0))
            x += f.getlength(p)
            if k < len(parts) - 1:
                d.text((x + 4, top + size * 0.08), "o", font=fo, fill=col, anchor="lt", stroke_width=8, stroke_fill=(0, 0, 0))
                x += fo.getlength("o") + 8


def _outlined(sp, px=16, col=(255, 255, 255)):
    """recorte "adesivo": contorno grosso (borda arredondada) em volta do sprite"""
    pad = px * 2
    big = Image.new("RGBA", (sp.width + 2 * pad, sp.height + 2 * pad))
    big.paste(sp, (pad, pad))
    a = big.split()[3].filter(ImageFilter.GaussianBlur(px * 0.55)).point(lambda v: 255 if v > 10 else 0)
    a = a.filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new("RGBA", big.size, (*col, 0)); out.putalpha(a)
    out.alpha_composite(big)
    return out


def _burst(cx, cy, col, n=16, r=1500, a=70, spin=0.0):
    """raios de "explosão" atrás do bicho, somem para fora"""
    ss = A.SS(W, H, s=1)
    for k in range(n):
        a0 = spin + 2 * math.pi * k / n; a1 = a0 + math.pi / n
        ss.poly([(cx, cy), (cx + r * math.cos(a0), cy + r * math.sin(a0)), (cx + r * math.cos(a1), cy + r * math.sin(a1))],
                fill=(*col, 255))
    rays = ss.get()
    fall = A.rgrad(900, [(0, (255, 255, 255, a)), (0.45, (255, 255, 255, int(a * 0.8))), (1.0, (255, 255, 255, 0))],
                   w=W, h=H, cx=cx, cy=cy).split()[3]
    m = Image.composite(fall, Image.new("L", (W, H), 0), rays.split()[3])
    rays.putalpha(m)
    return rays


def write_cover(R, path):
    """capa v2 (21/11): bicho GRANDE recortado (contorno branco) sobre o cenário desfocado + raios + faixa
    "E SE VOCÊ FOSSE…" + título curto (*destaque* em amarelo) + selo "VOCÊ" + chip do gancho.
    Precisa de cover_sprite(cv) no módulo da cena (senão cai na capa antiga).
    script.json -> cover: {t, focus, zoom, at:[x,y] centro do bicho na capa, title:[1-2 linhas], hook:"texto curto",
    sprite_rot, you:[x,y] para onde a seta do VOCÊ aponta (cabeça), you_side: "left"|"right"}"""
    from PIL import ImageEnhance
    S = R.S; cv = S.get("cover", {})
    if not hasattr(R.mod, "cover_sprite"):
        return _cover_v1(R, path)
    acc = tuple(S.get("accent", (230, 60, 80)))
    fx, fy = cv.get("focus", [W / 2, H * 0.62]); px, py = cv.get("at", [W / 2, 1150]); z = cv.get("zoom", 1.0)
    if hasattr(R.mod, "cover_bg"):
        bg = R.mod.cover_bg(cv).convert("RGBA")
    else:
        bg = R.frame(int(cv.get("t", 1.0) * FPS), captions=False, overlays=False).convert("RGBA")
    bg = A.cam(bg, zoom=z, dx=px - fx, dy=py - fy, cx=fx, cy=fy)
    bg = bg.filter(ImageFilter.GaussianBlur(cv.get("blur", 7)))
    bg = ImageEnhance.Color(bg.convert("RGB")).enhance(1.35).convert("RGBA")
    img = bg
    img.alpha_composite(A.rgrad(700, [(0, (*acc, 120)), (0.6, (*acc, 40)), (1, (*acc, 0))], w=W, h=H, cx=px, cy=py))
    img.alpha_composite(_burst(px, py, (255, 246, 210), a=cv.get("burst", 80), spin=0.1))
    img.alpha_composite(A.vgrad(W, H, [(0, (0, 0, 0, 190)), (0.30, (0, 0, 0, 60)), (0.42, (0, 0, 0, 0)),
                                       (0.86, (0, 0, 0, 0)), (1, (0, 0, 0, 150))]))
    # o bicho, grande, com contorno branco e sombra
    sp = R.mod.cover_sprite(cv).convert("RGBA")
    rot = cv.get("sprite_rot", 0)
    if rot: sp = sp.rotate(rot, resample=Image.BICUBIC, expand=True)
    sp = _outlined(sp, cv.get("outline", 16))
    sh, pad = A.shadow_of(sp, 22, 0.55)
    A.paste_c(img, sh, px + 16, py + 30)
    A.paste_c(img, sp, px, py)
    # selo VOCÊ com seta curta apontando para a cabeça
    hx, hy = cv.get("you", [px, py - 150]); side = cv.get("you_side", "right")
    tag = A.sticker("VOCÊ", size=84, fg=(0, 0, 0), bg=YELLOW, pad=(36, 14), radius=26, iw=8)
    tag = tag.rotate(7 if side == "right" else -7, expand=True, resample=Image.BICUBIC)
    sgn = 1 if side == "right" else -1
    tx = int(min(max(hx + sgn * 230, tag.width // 2 + 30), W - tag.width // 2 - 30)); ty = int(hy - 250)
    ar = A.SS(W, H, s=2)
    A.arrow(ar, tx - sgn * tag.width * 0.25, ty + tag.height * 0.42, hx + sgn * 30, hy - 40, YELLOW, w=24, iw=6)
    img.alpha_composite(ar.get())
    A.paste_c(img, tag, tx, ty)
    # faixa da série + título
    band = A.sticker("E SE VOCÊ FOSSE…", size=88, fg=(0, 0, 0), bg=YELLOW, pad=(40, 18), radius=18, iw=8)
    A.paste_c(img, band.rotate(-2.5, expand=True, resample=Image.BICUBIC), W // 2, 200)
    d = ImageDraw.Draw(img)
    lines = cv.get("title", ["?"]); n = max(len(l.replace("*", "")) for l in lines)
    size = 190 if n <= 10 else 168 if n <= 12 else 148
    y = 385
    for ln in lines:
        _title_rich(d, W / 2, y, ln, size); y += int(size * 1.04)
    if cv.get("hook"):
        chip = A.sticker(cv["hook"], size=66, fg=(255, 255, 255), bg=acc, pad=(34, 14), radius=22, iw=8)
        if chip.width > W - 90:
            k = (W - 90) / chip.width
            chip = chip.resize((int(chip.width * k), int(chip.height * k)), Image.LANCZOS)
        A.paste_c(img, chip.rotate(2.5, expand=True, resample=Image.BICUBIC), W // 2, cv.get("hook_y", 1640))
    d.text((W / 2, H - 105), "NA PELE DE", font=A.F(50, "mont-Black"), fill=(255, 255, 255), anchor="mm",
           stroke_width=6, stroke_fill=(0, 0, 0))
    img.convert("RGB").save(path, quality=92)


def write_publish(S, T, ep):
    pub = dict(S.get("publish", {}))
    if not pub: return
    item = dict(key=S["key"], kind="short", video="video.mp4", title=pub["title"], description=pub["description"],
                tags=pub.get("tags", []), publish_at=pub.get("publish_at"), if_late="public_now", made_for_kids=False,
                altered_content=True, pinned_comment=pub.get("pinned_comment"), thumbnail="capa.jpg")
    doc = dict(version=1, channel_id=pub.get("channel_id", "UC_CANAL5_PENDENTE"),
               created_at=time.strftime("%Y-%m-%dT%H:%M:%S-03:00", time.gmtime(time.time() - 3 * 3600)), items=[item])  # sempre horário de Brasília (a nuvem roda em UTC)
    json.dump(doc, open(os.path.join(ep, "publish.draft.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def sheet(R, path, extra=()):
    T = R.T; ts = [0.0]
    for sc in T["scenes"]:
        ts += [sc["t0"] + 0.35, (sc["t0"] + sc["t1"]) / 2, sc["t1"] - 0.15]
    ts += list(extra) + [T["total"] - 1 / FPS]
    ts = sorted(set(round(t, 2) for t in ts))
    cw, chh = 270, 480; cols = 6; rows = math.ceil(len(ts) / cols)
    out = Image.new("RGB", (cols * cw, rows * (chh + 30)), (20, 20, 20))
    d = ImageDraw.Draw(out)
    for k, t in enumerate(ts):
        im = R.frame(int(t * FPS)).resize((cw, chh), Image.BILINEAR)
        x, y = (k % cols) * cw, (k // cols) * (chh + 30)
        out.paste(im, (x, y)); d.text((x + 6, y + chh + 4), f"{t:.2f}s {R.scene_at(t).sc['id']}",
                                      font=A.F(18, "mont-Bold"), fill=(255, 255, 255))
    out.save(path)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep"); ap.add_argument("--sheet", action="store_true"); ap.add_argument("--stills", default="")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--draft", action="store_true"); ap.add_argument("--audio", action="store_true")
    ap.add_argument("--cover", action="store_true", help="só refaz capa.jpg usando o timeline.json (sem voz)")
    a = ap.parse_args()
    ep = os.path.abspath(a.ep)
    if a.cover:
        write_cover(Renderer(ep), os.path.join(ep, "capa.jpg")); print(os.path.join(ep, "capa.jpg")); return
    t_start = time.time()
    S, T, voice = build_timeline(ep)
    nw = len(T["words"])
    print(f"[canal5] {S['key']}: {T['total']:.1f} s, {nw} palavras, {len(T['scenes'])} cenas")
    if a.audio:
        print(render_audio(S, T, voice, ep)); return
    if a.sheet or a.stills:
        R = Renderer(ep, S, T)
        if a.sheet: print(sheet(R, os.path.join(ep, ".cache", "sheet.png")))
        for s in [x for x in a.stills.split(",") if x]:
            p = os.path.join(ep, ".cache", f"still_{float(s):06.2f}.png")
            R.frame(int(float(s) * FPS)).save(p); print(p)
        return
    apath = render_audio(S, T, voice, ep)
    N = int(math.ceil(T["total"] * FPS))
    tmp = os.path.join(ep, ".cache", "seg"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    k = a.workers; bounds = [round(N * j / k) for j in range(k + 1)]
    jobs = [(j, bounds[j], bounds[j + 1], os.path.join(tmp, f"s{j:02d}.mp4"), a.draft) for j in range(k)
            if bounds[j + 1] > bounds[j]]
    import multiprocessing as mp
    with mp.get_context("spawn").Pool(len(jobs), initializer=_init, initargs=(ep,)) as pool:
        for j in pool.imap_unordered(_segment, jobs): print(f"  segmento {j} ok ({time.time() - t_start:.0f} s)")
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{j[3]}'\n" for j in jobs))
    out = os.path.join(ep, "video_draft.mp4" if a.draft else "video.mp4")
    subprocess.run([ffmpeg_bin(), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", apath,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)
    R = Renderer(ep, S, T)
    write_srt(T, os.path.join(ep, "legendas.srt"))
    write_cover(R, os.path.join(ep, "capa.jpg"))
    write_publish(S, T, ep)
    print(f"[canal5] pronto: {out} ({time.time() - t_start:.0f} s)")


if __name__ == "__main__":
    main()
