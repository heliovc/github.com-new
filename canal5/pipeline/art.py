"""Canal 5 — kit de desenho vetorial 2D (PIL com superamostragem) + filtros "Visão do Bicho".

Estilo: formas chapadas, contorno fino, sombras suaves, cores saturadas. Tudo desenhado por código.
- SS: superfície superamostrada (desenha em s×, reduz no fim = bordas suaves).
- paste/paste_t: cola sprites com recorte, escala, rotação e opacidade.
- vgrad/rgrad/glow: gradientes. shadow_of: sombra suave de um sprite.
- compound_eye: mosaico hexagonal (olho composto). night_reveal: cinza escuro (humano) -> cor (bicho noturno).
"""
import math, os, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
HERE = os.path.dirname(os.path.abspath(__file__))
INK = (34, 24, 40)
WHITE = (255, 255, 255)
YELLOW = (255, 222, 40)


# ------------------------------------------------------------------ matemática
def clamp01(x):
    return 0.0 if x < 0 else 1.0 if x > 1 else x


def ease(x):
    x = clamp01(x); return 1 - (1 - x) ** 3


def easeio(x):
    x = clamp01(x); return x * x * (3 - 2 * x)


def back(x, c=1.7):
    x = clamp01(x); return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2


def lerp(a, b, u):
    return a + (b - a) * u


def mixc(c1, c2, u):
    u = clamp01(u)
    return tuple(int(round(a + (b - a) * u)) for a, b in zip(c1, c2))


def win(t, a, b, fade=0.25):
    """1 dentro de [a, b], com rampas de 'fade' s nas bordas"""
    if t < a - fade or t > b + fade: return 0.0
    if t < a: return easeio((t - (a - fade)) / fade)
    if t > b: return 1 - easeio((t - b) / fade)
    return 1.0


def noise1(x, seed=0):
    """ruído suave 1D barato (soma de senos)"""
    s = seed * 1.618
    return (math.sin(x * 1.7 + s) * 0.5 + math.sin(x * 3.1 + s * 2.3) * 0.3 + math.sin(x * 5.3 + s * 0.7) * 0.2)


# ------------------------------------------------------------------ fontes
def font_path(name):
    for d in (os.environ.get("CANAL5_FONTS", ""), os.path.join(HERE, "..", "fonts"),
              os.path.expanduser("~/.cache/canal5/fonts"), "/usr/share/fonts/truetype/google-fonts"):
        if d and os.path.exists(os.path.join(d, name)):
            return os.path.join(d, name)
    raise FileNotFoundError(f"fonte {name}: rode canal5/setup.sh")


_FC = {}


def F(size, kind="anton"):
    """kind: 'anton' | 'mont-<Peso>' (Thin..Black)"""
    size = max(4, int(size))
    key = (size, kind)
    if key not in _FC:
        if kind == "anton":
            f = ImageFont.truetype(font_path("Anton-Regular.ttf"), size)
        else:
            f = ImageFont.truetype(font_path("Montserrat-Variable.ttf"), size)
            f.set_variation_by_name(kind.split("-", 1)[1])
        _FC[key] = f
    return _FC[key]


_EMO = {}


def emoji(code, size):
    key = (code, size)
    if key not in _EMO:
        p = os.path.join(HERE, "..", "assets", "emoji", f"emoji_u{code}.png")
        _EMO[key] = Image.open(p).convert("RGBA").resize((size, size), Image.LANCZOS) if os.path.exists(p) else None
    return _EMO[key]


# ------------------------------------------------------------------ superfície superamostrada
class SS:
    """Superfície RGBA superamostrada. Cores com alfa < 255 são MISTURADAS (desenha numa camada temporária e compõe),
    porque o ImageDraw do PIL substitui os pixels em imagens RGBA em vez de misturar."""

    def __init__(self, w=W, h=H, s=2, bg=(0, 0, 0, 0)):
        self.w, self.h, self.s = int(w), int(h), s
        self.im = Image.new("RGBA", (self.w * s, self.h * s), bg)
        self.d = ImageDraw.Draw(self.im)

    def _p(self, pts):
        s = self.s
        return [(x * s, y * s) for x, y in pts]

    @staticmethod
    def _tr(*cols):
        return any(c is not None and len(c) == 4 and c[3] < 255 for c in cols)

    def _ctx(self, P, pad, *cols):
        """(draw, ox, oy, tmp): camada temporária só quando há translucidez"""
        if not self._tr(*cols): return self.d, 0, 0, None
        xs = [p[0] for p in P]; ys = [p[1] for p in P]
        x0 = int(max(0, min(xs) - pad)); y0 = int(max(0, min(ys) - pad))
        x1 = int(min(self.im.width, max(xs) + pad + 1)); y1 = int(min(self.im.height, max(ys) + pad + 1))
        if x1 <= x0 or y1 <= y0: return None, 0, 0, None
        tmp = Image.new("RGBA", (x1 - x0, y1 - y0))
        return ImageDraw.Draw(tmp), x0, y0, tmp

    def _commit(self, tmp, ox, oy):
        if tmp is not None: self.im.alpha_composite(tmp, (ox, oy))

    def poly(self, pts, fill=None, ink=None, w=0):
        if len(pts) < 3: return
        P = self._p(pts); ww = max(1, int(w * self.s))
        if fill is not None and ink is not None and w > 0 and self._tr(fill, ink):
            self.poly(pts, fill=fill); self.poly(pts, ink=ink, w=w); return
        d, ox, oy, tmp = self._ctx(P, ww + 2, fill, ink if w else None)
        if d is None: return
        Q = [(x - ox, y - oy) for x, y in P]
        if fill is not None: d.polygon(Q, fill=fill)
        if ink is not None and w > 0: d.line(Q + [Q[0], Q[1]], fill=ink, width=ww, joint="curve")
        self._commit(tmp, ox, oy)

    def line(self, pts, col, w, cap=True):
        if len(pts) < 2: return
        P = self._p(pts); ww = max(1, int(w * self.s))
        d, ox, oy, tmp = self._ctx(P, ww + 2, col)
        if d is None: return
        Q = [(x - ox, y - oy) for x, y in P]
        d.line(Q, fill=col, width=ww, joint="curve")
        if cap and ww > 2:
            r = ww / 2
            for (x, y) in (Q[0], Q[-1]):
                d.ellipse([x - r, y - r, x + r, y + r], fill=col)
        self._commit(tmp, ox, oy)

    def ellipse(self, cx, cy, rx, ry, fill=None, ink=None, w=0):
        s = self.s
        box = [(cx - rx) * s, (cy - ry) * s, (cx + rx) * s, (cy + ry) * s]
        if box[2] <= box[0] or box[3] <= box[1]: return
        ww = max(1, int(w * s)) if w else 0
        if fill is not None and ink is not None and w > 0 and self._tr(fill, ink):
            self.ellipse(cx, cy, rx, ry, fill=fill); self.ellipse(cx, cy, rx, ry, ink=ink, w=w); return
        d, ox, oy, tmp = self._ctx([(box[0], box[1]), (box[2], box[3])], ww + 2, fill, ink if w else None)
        if d is None: return
        d.ellipse([box[0] - ox, box[1] - oy, box[2] - ox, box[3] - oy], fill=fill, outline=ink if w else None, width=ww)
        self._commit(tmp, ox, oy)

    def circle(self, cx, cy, r, **k):
        self.ellipse(cx, cy, r, r, **k)

    def oval(self, cx, cy, rx, ry, rot, fill=None, ink=None, w=0, n=40):
        self.poly(ell_pts(cx, cy, rx, ry, rot, n), fill=fill, ink=ink, w=w)

    def rrect(self, x0, y0, x1, y1, r, fill=None, ink=None, w=0):
        s = self.s
        if x1 <= x0 or y1 <= y0: return
        if fill is not None and ink is not None and w > 0 and self._tr(fill, ink):
            self.rrect(x0, y0, x1, y1, r, fill=fill); self.rrect(x0, y0, x1, y1, r, ink=ink, w=w); return
        ww = max(1, int(w * s)) if w else 0
        d, ox, oy, tmp = self._ctx([(x0 * s, y0 * s), (x1 * s, y1 * s)], ww + 2, fill, ink if w else None)
        if d is None: return
        d.rounded_rectangle([x0 * s - ox, y0 * s - oy, x1 * s - ox, y1 * s - oy], radius=max(0, r * s), fill=fill,
                            outline=ink if w else None, width=ww)
        self._commit(tmp, ox, oy)

    def rect(self, x0, y0, x1, y1, fill):
        s = self.s
        d, ox, oy, tmp = self._ctx([(x0 * s, y0 * s), (x1 * s, y1 * s)], 2, fill)
        if d is None: return
        d.rectangle([x0 * s - ox, y0 * s - oy, x1 * s - ox, y1 * s - oy], fill=fill)
        self._commit(tmp, ox, oy)

    def text(self, xy, txt, size, kind="mont-ExtraBold", fill=WHITE, anchor="mm", stroke=0, stroke_fill=INK):
        s = self.s
        f = F(size * s, kind); X, Y = xy[0] * s, xy[1] * s; sw = int(stroke * s)
        if not self._tr(fill, stroke_fill if stroke else None):
            self.d.text((X, Y), txt, font=f, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=stroke_fill); return
        bb = f.getbbox(txt, anchor=anchor, stroke_width=sw)
        d, ox, oy, tmp = self._ctx([(X + bb[0], Y + bb[1]), (X + bb[2], Y + bb[3])], 4, (0, 0, 0, 0))
        if d is None: return
        a = min(c[3] for c in (fill, stroke_fill if stroke else fill) if len(c) == 4)
        d.text((X - ox, Y - oy), txt, font=f, fill=tuple(fill[:3]) + (255,), anchor=anchor, stroke_width=sw,
               stroke_fill=tuple(stroke_fill[:3]) + (255,) if stroke else None)
        if a < 255: tmp.putalpha(tmp.split()[3].point(lambda v: v * a // 255))
        self._commit(tmp, ox, oy)

    def paste(self, sprite, x, y):
        """cola sprite (já em escala s) no canto x,y (coordenadas 1×)"""
        paste(self.im, sprite, int(x * self.s), int(y * self.s))

    def get(self):
        return self.im.reduce(self.s) if self.s > 1 else self.im


def blend_rect(img, box, col):
    """retângulo translúcido misturado (ImageDraw em RGBA substitui pixels)"""
    ov = Image.new("RGBA", img.size); ImageDraw.Draw(ov).rectangle(box, fill=col); img.alpha_composite(ov)


# ------------------------------------------------------------------ geometria
def ell_pts(cx, cy, rx, ry, rot=0.0, n=40, a0=0.0, a1=2 * math.pi):
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    out = []
    for i in range(n):
        a = a0 + (a1 - a0) * i / (n - (0 if a1 - a0 < 2 * math.pi - 1e-6 else 0))
        x, y = rx * math.cos(a), ry * math.sin(a)
        out.append((cx + x * c - y * s, cy + x * s + y * c))
    return out


def bez(p0, p1, p2, p3, n=20):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return out


def spline(pts, n=8, closed=True):
    """Catmull-Rom pelos pontos (contorno orgânico)"""
    P = list(pts); m = len(P); out = []
    rng = range(m) if closed else range(m - 1)
    for i in rng:
        p0 = P[(i - 1) % m] if closed else P[max(i - 1, 0)]
        p1 = P[i]; p2 = P[(i + 1) % m] if closed else P[i + 1]
        p3 = P[(i + 2) % m] if closed else P[min(i + 2, m - 1)]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    if not closed: out.append(P[-1])
    return out


def xf(pts, x, y, s, rot=0.0, flip=1):
    """transforma pontos de unidades do corpo para a tela"""
    c, sn = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    out = []
    for px, py in pts:
        px *= flip
        out.append((x + (px * c - py * sn) * s, y + (px * sn + py * c) * s))
    return out


# ------------------------------------------------------------------ cores / gradientes
def vgrad(w, h, stops):
    """stops: [(pos 0..1, (r,g,b[,a]))] de cima para baixo"""
    ys = np.linspace(0, 1, h)
    chans = []
    n = len(stops[0][1])
    pos = [p for p, _ in stops]
    for k in range(max(n, 3)):
        vals = [c[k] if k < len(c) else 255 for _, c in stops]
        chans.append(np.interp(ys, pos, vals))
    arr = np.stack(chans, axis=1)  # h x C
    if arr.shape[1] == 3: arr = np.concatenate([arr, np.full((h, 1), 255.0)], axis=1)
    arr = np.repeat(arr[:, None, :], w, axis=1)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def rgrad(r, stops, w=None, h=None, cx=None, cy=None):
    """sprite radial (2r x 2r por padrão); stops [(pos, rgba)] do centro para fora"""
    w = w or 2 * r; h = h or 2 * r
    cx = w / 2 if cx is None else cx; cy = h / 2 if cy is None else cy
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / max(1, r)
    pos = [p for p, _ in stops]
    chans = [np.interp(d, pos, [c[k] for _, c in stops]) for k in range(4)]
    return Image.fromarray(np.stack(chans, axis=2).astype(np.uint8), "RGBA")


_GLOW = {}


def glow(r, col, a=180):
    key = (int(r), tuple(col), a)
    if key not in _GLOW:
        _GLOW[key] = rgrad(int(r), [(0, (*col, a)), (0.35, (*col, int(a * 0.55))), (1, (*col, 0))])
    return _GLOW[key]


def shadow_of(sprite, blur=14, alpha=0.35, col=(10, 6, 20)):
    a = sprite.split()[3].point(lambda v: int(v * alpha))
    pad = blur * 3
    sh = Image.new("RGBA", (sprite.width + 2 * pad, sprite.height + 2 * pad), (*col, 0))
    m = Image.new("L", sh.size, 0); m.paste(a, (pad, pad))
    sh.putalpha(m.filter(ImageFilter.GaussianBlur(blur)))
    return sh, pad


# ------------------------------------------------------------------ colar sprites
def paste(dst, src, x, y, alpha=1.0):
    """alpha_composite com recorte (x,y = canto superior esquerdo, pode ser negativo)"""
    if src is None: return
    x, y = int(round(x)), int(round(y))
    sx0, sy0 = max(0, -x), max(0, -y)
    sx1, sy1 = min(src.width, dst.width - x), min(src.height, dst.height - y)
    if sx1 <= sx0 or sy1 <= sy0: return
    s = src.crop((sx0, sy0, sx1, sy1)) if (sx0 or sy0 or sx1 < src.width or sy1 < src.height) else src
    if alpha < 0.999:
        s = s.copy(); s.putalpha(s.split()[3].point(lambda v: int(v * alpha)))
    dst.alpha_composite(s, (x + sx0, y + sy0))


def paste_c(dst, src, cx, cy, alpha=1.0):
    if src is None: return
    paste(dst, src, cx - src.width / 2, cy - src.height / 2, alpha)


def paste_t(dst, src, cx, cy, scale=1.0, rot=0.0, alpha=1.0):
    if src is None or scale <= 0.01: return
    s = src
    if abs(scale - 1) > 1e-3:
        s = s.resize((max(1, int(s.width * scale)), max(1, int(s.height * scale))), Image.BICUBIC)
    if abs(rot) > 0.05:
        s = s.rotate(-rot, resample=Image.BICUBIC, expand=True)
    paste_c(dst, s, cx, cy, alpha)


def cam(img, zoom=1.0, dx=0.0, dy=0.0, rot=0.0, cx=W / 2, cy=H / 2):
    """câmera: zoom/rotação em torno de (cx,cy) e deslocamento; devolve imagem do mesmo tamanho"""
    if abs(zoom - 1) < 1e-3 and abs(rot) < 0.02 and abs(dx) < 0.5 and abs(dy) < 0.5:
        return img
    a = math.radians(rot); c, s = math.cos(a) / zoom, math.sin(a) / zoom
    # mapa inverso: saída (u,v) -> entrada
    a0 = c; b0 = s; c0 = cx - c * (cx + dx) - s * (cy + dy)
    d0 = -s; e0 = c; f0 = cy + s * (cx + dx) - c * (cy + dy)
    return img.transform(img.size, Image.AFFINE, (a0, b0, c0, d0, e0, f0), resample=Image.BILINEAR)


# ------------------------------------------------------------------ peças comuns
def arrow(ss, x0, y0, x1, y1, col, w=30, head=2.1, ink=INK, iw=4):
    """seta chapada com contorno (de x0,y0 até a ponta x1,y1)"""
    L = math.hypot(x1 - x0, y1 - y0)
    if L < 2: return
    ux, uy = (x1 - x0) / L, (y1 - y0) / L; px, py = -uy, ux
    hl = min(L * 0.6, w * head * 0.9); hw = w * head / 2; sw = w / 2
    bx, by = x1 - ux * hl, y1 - uy * hl
    pts = [(x0 + px * sw, y0 + py * sw), (bx + px * sw, by + py * sw), (bx + px * hw, by + py * hw), (x1, y1),
           (bx - px * hw, by - py * hw), (bx - px * sw, by - py * sw), (x0 - px * sw, y0 - py * sw)]
    ss.poly(pts, fill=col, ink=ink, w=iw)


def sticker(text, size=54, fg=INK, bg=WHITE, hi=None, kind="mont-Black", pad=(30, 16), emoji_code=None, radius=22,
            ink=INK, iw=5):
    """etiqueta arredondada; *palavra* = cor de destaque (hi)"""
    hi = hi or (230, 60, 80)
    parts = []
    for i, seg in enumerate(re.split(r"\*", text)):
        if seg: parts.append((seg, i % 2 == 1))
    f = F(size, kind)
    widths = [f.getlength(p) for p, _ in parts]
    ew = int(size * 1.15) if emoji_code else 0
    tw = sum(widths) + (ew + 12 if ew else 0)
    asc, desc = f.getmetrics()
    w = int(tw + 2 * pad[0]); h = int(asc + desc * 0.4 + 2 * pad[1])
    ss = SS(w + 16, h + 16, s=2)
    ss.rrect(8, 8, 8 + w, 8 + h, radius, fill=bg, ink=ink, w=iw)
    x = 8 + pad[0]; yb = 8 + pad[1] + asc
    for (seg, isk), wd in zip(parts, widths):
        ss.text((x, yb), seg, size, kind, fill=hi if isk else fg, anchor="ls")
        x += wd
    im = ss.get()
    if emoji_code:
        e = emoji(emoji_code, ew)
        if e is not None: paste(im, e, int(x + 12), int(8 + (h - ew) / 2))
    return im


def speed_lines(ss, t, n, cx, cy, r0, r1, col, w=3, seed=0, speed=1.0):
    """linhas radiais saindo do ponto de fuga (sensação de aproximação)"""
    rng = np.random.default_rng(seed)
    angs = rng.uniform(0, 2 * math.pi, n); ph = rng.uniform(0, 1, n); ln = rng.uniform(0.08, 0.22, n)
    for a, p, l in zip(angs, ph, ln):
        u = (p + t * speed) % 1.0
        ra = lerp(r0, r1, u ** 1.6); rb = ra + (r1 - r0) * l * (0.4 + u)
        al = int(col[3] * min(1, u * 3) if len(col) > 3 else 200)
        ss.line([(cx + math.cos(a) * ra, cy + math.sin(a) * ra), (cx + math.cos(a) * rb, cy + math.sin(a) * rb)],
                (*col[:3], al), w * (0.5 + u))


# ------------------------------------------------------------------ Visão do Bicho
_HEXC = {}


def _hex_index(w, h, R):
    key = (w, h, R)
    if key in _HEXC: return _HEXC[key]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float64)
    # leve "bojo" (olho é curvo): células maiores no centro
    cx, cy = w / 2, h / 2
    dx, dy = (xx - cx) / w, (yy - cy) / h
    k = 1 + 0.35 * (dx * dx + dy * dy)
    X = cx + (xx - cx) * k; Y = cy + (yy - cy) * k
    q = (math.sqrt(3) / 3 * X - Y / 3) / R
    r = (2 / 3 * Y) / R
    # arredondamento cúbico
    x3, z3 = q, r; y3 = -x3 - z3
    rx, ry, rz = np.round(x3), np.round(y3), np.round(z3)
    dxr, dyr, dzr = np.abs(rx - x3), np.abs(ry - y3), np.abs(rz - z3)
    m1 = (dxr > dyr) & (dxr > dzr); rx[m1] = -ry[m1] - rz[m1]
    m2 = ~m1 & (dyr > dzr); ry[m2] = -rx[m2] - rz[m2]
    m3 = ~m1 & ~m2; rz[m3] = -rx[m3] - ry[m3]
    qi, ri = rx.astype(np.int64), rz.astype(np.int64)
    xc = R * math.sqrt(3) * (qi + ri / 2); yc = R * 1.5 * ri
    ddx, ddy = np.abs(X - xc), np.abs(Y - yc)
    inr = R * math.sqrt(3) / 2
    hn = np.maximum(ddx / inr, (ddx * 0.5 + ddy * math.sqrt(3) / 2) / inr)
    qi -= qi.min(); ri -= ri.min()
    idx = ri * (qi.max() + 1) + qi
    _, inv = np.unique(idx, return_inverse=True)
    inv = inv.reshape(h, w)
    shade = np.clip(1.10 - 0.42 * hn ** 2, 0.55, 1.12)
    border = hn > 0.9
    shade[border] *= 0.22
    _HEXC[key] = (inv, shade.astype(np.float32), int(inv.max()) + 1)
    return _HEXC[key]


def compound_eye(img, cell=30, amount=1.0, tint=(1.0, 1.0, 1.0)):
    """mosaico de olho composto (cada omatídeo = 1 cor média, com borda escura e brilho no centro)"""
    if amount <= 0.01: return img
    w2, h2 = W // 2, H // 2
    small = np.asarray(img.convert("RGB").resize((w2, h2), Image.BILINEAR), dtype=np.float32)
    inv, shade, n = _hex_index(w2, h2, cell / 2 / 2)
    flat = inv.ravel(); cnt = np.bincount(flat, minlength=n).astype(np.float32) + 1e-6
    out = np.empty_like(small)
    for c in range(3):
        mean = np.bincount(flat, weights=small[..., c].ravel(), minlength=n) / cnt
        out[..., c] = mean[inv] * shade * tint[c]
    out = np.clip(out, 0, 255).astype(np.uint8)
    up = Image.fromarray(out).resize((W, H), Image.BILINEAR)
    if amount >= 0.999: return up.convert("RGBA")
    return Image.blend(img.convert("RGB"), up, amount).convert("RGBA")


def night_reveal(img, u, ox, oy, human_dark=0.26):
    """visão noturna em cores: fora do círculo = visão humana (cinza, escura, granulada); dentro = cor"""
    rgb = np.asarray(img.convert("RGB"), dtype=np.float32)
    g = rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    hum = np.stack([g * 0.92, g * 0.97, g * 1.08], axis=2) * human_dark
    rng = np.random.default_rng(int(u * 1000) % 97)
    hum += rng.normal(0, 7, hum.shape[:2]).astype(np.float32)[..., None]
    if u <= 0.001: out = hum
    else:
        # cor do bicho: saturação +25%
        mean = rgb.mean(axis=2, keepdims=True)
        col = mean + (rgb - mean) * 1.25
        R = u * 2400
        yy, xx = np.ogrid[0:H, 0:W]
        d = np.sqrt((xx - ox) ** 2 + (yy - oy) ** 2)
        m = np.clip((R - d) / 90.0, 0, 1)[..., None]
        out = hum * (1 - m) + col * m
        ring = np.exp(-((d - R) / 14.0) ** 2)[..., None] * 120 * (1 - u)
        out = out + ring * np.array([0.6, 1.0, 0.7], dtype=np.float32)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).convert("RGBA")


def vignette(img, strength=0.45):
    key = ("vig", strength)
    if key not in _GLOW:
        yy, xx = np.ogrid[0:H, 0:W]
        d = np.sqrt(((xx - W / 2) / (W * 0.72)) ** 2 + ((yy - H / 2) / (H * 0.72)) ** 2)
        a = np.clip((d - 0.55) / 0.6, 0, 1) ** 1.6 * 255 * strength
        v = np.zeros((H, W, 4), np.uint8); v[..., 3] = a.astype(np.uint8)
        _GLOW[key] = Image.fromarray(v, "RGBA")
    out = img.copy(); out.alpha_composite(_GLOW[key]); return out
