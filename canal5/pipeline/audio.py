"""Canal 5 — som 100% sintetizado (sem direitos de terceiros): trilha, efeitos e mixagem.

Regras do plano: trilha a -20 dB sob a voz; 1 SFX por troca de cena; mundo humano grave/lento, bicho agudo/rápido;
0,3 s de silêncio (trilha zerada) antes do payoff.
"""
import numpy as np

SR = 48000


def T(d):
    return np.arange(int(max(0.0, d) * SR)) / SR


def resample(a, sr0, sr1):
    if sr0 == sr1: return a.astype(np.float32)
    n1 = int(round(len(a) * sr1 / sr0))
    A = np.fft.rfft(a.astype(np.float64))
    m = n1 // 2 + 1
    B = np.zeros(m, dtype=complex); k = min(m, len(A)); B[:k] = A[:k]
    return (np.fft.irfft(B, n=n1) * (n1 / len(a))).astype(np.float32)


def filt(x, lo=None, hi=None):
    if len(x) == 0: return x
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.ones_like(f)
    if lo: g *= 1 / (1 + (lo / np.maximum(f, 1.0)) ** 4)
    if hi: g *= 1 / (1 + (f / hi) ** 4)
    return np.fft.irfft(X * g, n=len(x))


def noise(d, seed=0):
    return np.random.default_rng(seed).standard_normal(int(d * SR))


def norm(x, pk=1.0):
    m = np.abs(x).max() if len(x) else 0
    return x * (pk / m) if m > 0 else x


def fades(x, a=0.004, r=0.03):
    n = len(x); x = x.copy()
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na: x[:na] *= np.linspace(0, 1, na)
    if nr: x[-nr:] *= np.linspace(1, 0, nr)
    return x


def sweep(f0, f1, d, shape=1.0):
    t = T(d); u = (t / max(d, 1e-6)) ** shape
    f = f0 * (f1 / f0) ** u
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


# ------------------------------------------------------------------ efeitos
def whoosh(d=0.55, lo=300, hi=7000, seed=1, rev=False, **_):
    n = noise(d, seed); t = T(d); out = np.zeros_like(n)
    bands = [(lo, lo * 3), (lo * 3, lo * 9), (lo * 9, hi)]
    for k, (a, b) in enumerate(bands):
        c = (0.30 + 0.17 * k) if not rev else (0.70 - 0.17 * k)
        out += filt(n, a, b) * np.exp(-((t / d - c) / 0.2) ** 2)
    return fades(norm(out))


def wind(d=3.0, seed=2, muffled=False, **_):
    n = noise(d, seed); t = T(d)
    x = filt(n, 70, 500 if muffled else 1100)
    lfo = 0.55 + 0.45 * np.sin(2 * np.pi * 0.35 * t + 1.3) * np.sin(2 * np.pi * 0.11 * t + 0.2)
    wh = filt(noise(d, seed + 7), 900, 1600) * (0.12 if not muffled else 0.04) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.23 * t))
    return fades(norm(x * lfo + wh), 0.25, 0.4)


def tic(**_):
    t = T(0.07)
    x = np.sin(2 * np.pi * 4200 * t) * np.exp(-t / 0.007) + 0.5 * np.sin(2 * np.pi * 6900 * t) * np.exp(-t / 0.004)
    return fades(norm(x), 0.0005, 0.01)


def thud(**_):
    t = T(0.7); f = 48 + 70 * np.exp(-t / 0.05)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.2)
    x += filt(noise(0.7, 5), 30, 260) * np.exp(-t / 0.05) * 0.6
    return fades(norm(x), 0.001, 0.1)


def hum(d=3.0, f0=120, **_):
    t = T(d)
    x = sum(a * np.sin(2 * np.pi * f0 * k * t + k) for k, a in ((0.5, 0.7), (1, 1.0), (2, 0.45), (3, 0.25), (4, 0.12)))
    x *= 1 + 0.12 * np.sin(2 * np.pi * 2.7 * t)
    x += filt(noise(d, 9), 80, 400) * 0.15
    return fades(norm(x), 0.35, 0.35)


def rise(d=1.2, f0=260, f1=1100, **_):
    x = sweep(f0, f1, d, 0.8) + 0.3 * sweep(2 * f0, 2 * f1, d, 0.8)
    t = T(d); env = np.minimum(1, t / 0.05) * (0.6 + 0.4 * t / d)
    return fades(norm(x * env), 0.01, 0.08)


def steps(d=2.0, rate=10.0, seed=3, **_):
    out = np.zeros(int(d * SR)); rng = np.random.default_rng(seed)
    k = 0.0
    while k < d - 0.05:
        i = int(k * SR); t = T(0.03); f = rng.uniform(5000, 7500)
        c = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.004) * rng.uniform(0.4, 1.0)
        out[i:i + len(c)] += c[:len(out) - i]
        k += 1 / rate * rng.uniform(0.8, 1.2)
    return norm(out)


def kick(**_):
    t = T(0.4); f = 46 + 110 * np.exp(-t / 0.03)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13)
    x[:200] += np.linspace(0.6, 0, 200)
    return fades(norm(x), 0.0005, 0.05)


def metal(seed=4, **_):
    rng = np.random.default_rng(seed); out = np.zeros(int(0.9 * SR))
    for k in range(3):
        st = int(rng.uniform(0, 0.4) * SR); t = T(0.5)
        x = sum(a * np.sin(2 * np.pi * f * rng.uniform(0.97, 1.03) * t) * np.exp(-t / dcy)
                for f, a, dcy in ((1530, 1, 0.25), (2370, .6, .18), (3660, .4, .12), (5110, .25, .08)))
        out[st:st + len(x)] += x[:len(out) - st] * rng.uniform(0.4, 1)
    return fades(norm(out), 0.0005, 0.05)


def hiss(d=1.0, **_):
    t = T(d); x = filt(noise(d, 11), 2500, 11000) * np.sin(np.pi * t / d) ** 0.7
    return norm(x)


def door(**_):
    t = T(0.5)
    x = np.sin(2 * np.pi * np.cumsum(70 + 40 * np.exp(-t / 0.03)) / SR) * np.exp(-t / 0.09)
    x += filt(noise(0.5, 12), 200, 1500) * np.exp(-t / 0.02) * 0.5
    return fades(norm(x), 0.001, 0.05)


def glitch(d=0.4, seed=13, **_):
    rng = np.random.default_rng(seed); out = np.zeros(int(d * SR)); k = 0
    while k < len(out):
        n = int(rng.uniform(0.015, 0.05) * SR); t = np.arange(n) / SR; f = rng.uniform(200, 2400)
        sq = np.sign(np.sin(2 * np.pi * f * t)) * rng.uniform(0.3, 1)
        if rng.random() < 0.4: sq = filt(rng.standard_normal(n), 1000, 8000)
        out[k:k + n] += sq[:len(out) - k]; k += n
    return fades(norm(out), 0.002, 0.05)


def pop(f0=500, f1=1300, **_):
    t = T(0.09); x = sweep(f0, f1, 0.09, 0.5) * np.exp(-t / 0.035)
    return fades(norm(x), 0.001, 0.01)


def blip_up(**_):
    return rise(0.5, 500, 1600)


def drip(**_):
    t = T(0.18); x = sweep(900, 2200, 0.18, 0.4) * np.exp(-t / 0.05)
    return fades(norm(x), 0.001, 0.02)


def sizzle(d=1.5, **_):
    t = T(d); n = noise(d, 21); cr = (np.random.default_rng(22).random(len(n)) > 0.9985).astype(float)
    x = filt(n, 3000, 9000) * 0.3 + filt(cr, 1500, 9000) * 6
    return fades(norm(x * np.sin(np.pi * t / d) ** 0.5), 0.05, 0.2)


LIB = dict(whoosh=whoosh, wind=wind, tic=tic, thud=thud, hum=hum, rise=rise, steps=steps, kick=kick, metal=metal,
           hiss=hiss, door=door, glitch=glitch, pop=pop, blip_up=blip_up, drip=drip, sizzle=sizzle,
           whoosh_lo=lambda **k: whoosh(0.85, 110, 2200, seed=k.get("seed", 5)),
           whoosh_hi=lambda **k: whoosh(0.32, 900, 10000, seed=k.get("seed", 6)))


# ------------------------------------------------------------------ trilha
MAJOR = [0, 2, 4, 5, 7, 9, 11]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def marimba(f, d=0.8, vel=1.0):
    t = T(d)
    x = (np.sin(2 * np.pi * f * t) * np.exp(-t / 0.32) + 0.22 * np.sin(2 * np.pi * f * 3.93 * t) * np.exp(-t / 0.07)
         + 0.05 * np.sin(2 * np.pi * f * 9.2 * t) * np.exp(-t / 0.025))
    return fades(x * vel, 0.002, 0.05)


def pluck(f, d=0.6, vel=1.0):
    t = T(d)
    x = sum((0.6 ** k) * np.sin(2 * np.pi * f * (k + 1) * t) * np.exp(-t * (6 + 5 * k)) for k in range(5))
    return fades(x * vel, 0.001, 0.05)


def bassn(f, d=0.5, vel=1.0):
    t = T(d)
    x = (np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t)) * np.exp(-t / 0.35)
    return fades(x * vel, 0.01, 0.06)


def padc(fs, d):
    t = T(d); x = np.zeros_like(t)
    for f in fs:
        for det in (-0.6, 0.6):
            x += np.sin(2 * np.pi * (f + det) * t)
    env = np.minimum(1, t / 0.4) * np.minimum(1, (d - t) / 0.4)
    return x * env / max(1, len(fs) * 2)


def music(total, bpm=104, root=65, prog=(0, 5, 3, 4), seed=1, inst="marimba", density=0.8, perc=True, **_):
    rng = np.random.default_rng(seed)
    beat = 60.0 / bpm; bar = 4 * beat
    n = int((total + 2) * SR); out = np.zeros(n)
    voice = marimba if inst == "marimba" else pluck
    pats = [[0, 2, 1, 2, 3, 2, 1, 2], [0, 1, 2, 3, 2, 1, 2, 1], [0, 2, 3, 2, 1, 2, 0, 3], [3, 2, 1, 0, 1, 2, 3, 2]]

    def put(x, t0, g):
        i = int(t0 * SR)
        if i >= n: return
        out[i:i + len(x)] += x[:n - i] * g

    nb = int(total / bar) + 2
    for b in range(nb):
        deg = prog[b % len(prog)]; t0 = b * bar
        chord = [root + MAJOR[(deg + i) % 7] + 12 * ((deg + i) // 7) for i in (0, 2, 4)]
        tones = chord + [chord[0] + 12]
        pat = pats[(b // len(prog) + seed) % len(pats)]
        for k in range(8):
            if rng.random() > density and k not in (0, 4): continue
            m = tones[pat[k]] + (12 if (b % 4 == 3 and k > 5) else 0)
            put(voice(hz(m), 0.7, rng.uniform(0.55, 1.0)), t0 + k * beat / 2, 0.5)
        br = root - 24 + MAJOR[deg]
        put(bassn(hz(br), beat * 1.6), t0, 0.7)
        put(bassn(hz(br), beat * 1.2), t0 + 2 * beat, 0.6)
        if rng.random() < 0.5: put(bassn(hz(br + 7), beat * 0.6), t0 + 3.5 * beat, 0.4)
        put(padc([hz(m - 12) for m in chord], bar), t0, 0.12)
        if perc:
            for k in range(8):
                if k % 2 == 1:
                    sh = filt(noise(0.05, b * 8 + k), 5000, 14000) * np.exp(-T(0.05) / 0.012)
                    put(sh, t0 + k * beat / 2, 0.07)
            put(kick(), t0, 0.35); put(kick(), t0 + 2 * beat, 0.25)
    return out[:int(total * SR) + 1]


# ------------------------------------------------------------------ mixagem
def mix(voice, mus, events, total, payoff_t=None, music_db=-20.0):
    n = int(total * SR) + 1
    v = np.zeros(n); v[:min(n, len(voice))] = voice[:n]
    v = norm(v, 0.85)
    act = v[np.abs(v) > 0.03]
    vr = float(np.sqrt(np.mean(act ** 2))) if len(act) else 0.1
    m = np.zeros(n); m[:min(n, len(mus))] = mus[:n]
    mr = float(np.sqrt(np.mean(m ** 2))) or 1.0
    m *= vr * 10 ** (music_db / 20) / mr
    g = np.ones(n)
    if payoff_t is not None:
        tt = np.arange(n) / SR
        a, b = payoff_t - 0.42, payoff_t - 0.30
        g = np.where(tt < a, 1.0, np.where(tt < b, 1 - (tt - a) / (b - a), np.where(tt < payoff_t, 0.0,
                     np.minimum(1.0, (tt - payoff_t) / 0.5))))
    m *= g
    s = np.zeros(n)
    for ev in events:
        typ, t0, gdb, params = ev
        fn = LIB.get(typ)
        if fn is None: continue
        x = fn(**params)
        i = int(max(0.0, t0) * SR)
        if i >= n: continue
        s[i:i + len(x)] += x[:n - i] * 0.85 * 10 ** (gdb / 20)
    out = v + m + s
    # volume de Shorts: sobe o RMS até ~0,16 (≈ -16 dBFS) com saturação suave nos picos
    base = float(np.sqrt(np.mean(out ** 2))) or 1e-3
    g = 1.0
    for _ in range(8):
        y = np.tanh(out * g)
        r = float(np.sqrt(np.mean(y ** 2)))
        if r >= 0.16 or g > 4: break
        g *= min(1.6, 0.16 / max(r, 1e-4))
    return norm(np.tanh(out * g), 0.95).astype(np.float32)
