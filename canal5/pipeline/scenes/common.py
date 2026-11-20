"""Peças reaproveitáveis entre episódios do Canal 5 (texturas urbanas, nuvens, cache)."""
import math
import numpy as np
from PIL import Image, ImageFilter
import art as A

_C = {}


def cached(key, fn):
    if key not in _C: _C[key] = fn()
    return _C[key]


def calcada(w, h, scale=1.0, seed=0, light=(238, 232, 222), dark=(44, 40, 46)):
    """pedra portuguesa em ondas (calçada carioca), por numpy"""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    lam, amp, band = 150 * scale, 38 * scale, 70 * scale
    v = (yy + amp * np.sin(2 * np.pi * xx / lam)) / band
    b = (np.floor(v) % 2)
    cell = 11 * scale
    row = np.floor(yy / cell)
    cx = (xx + (row % 2) * cell / 2) % cell; cy = yy % cell
    col = np.floor((xx + (row % 2) * cell / 2) / cell)
    rnd = ((np.sin(row * 12.9898 + col * 78.233 + seed) * 43758.5453) % 1.0) - 0.5
    edge = (cx < 1.6 * scale) | (cy < 1.6 * scale)
    L = np.array(light, np.float32); D = np.array(dark, np.float32)
    rgb = np.where(b[..., None] > 0, D, L) + (rnd * 22)[..., None]
    rgb[edge] = rgb[edge] * 0.55 + 30
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).convert("RGBA")


def cloud(w, h, seed=0, col=(255, 236, 220), a=150, blur=10):
    rng = np.random.default_rng(seed)
    ss = A.SS(w, h, s=1)
    for _ in range(9):
        cx = rng.uniform(0.2, 0.8) * w; cy = rng.uniform(0.45, 0.7) * h
        r = rng.uniform(0.12, 0.25) * w
        ss.ellipse(cx, cy, r, r * 0.6, fill=(*col, a))
    return ss.get().filter(ImageFilter.GaussianBlur(blur))


def noise_tex(w, h, seed=0, amp=10):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, amp, (h, w)).astype(np.float32)
    return n


def motion_blur_v(img, amount):
    """borrão vertical barato (média de cópias deslocadas)"""
    if amount < 2: return img
    acc = np.zeros((img.height, img.width, 4), np.float32)
    k = 5
    for i in range(k):
        off = int((i - (k - 1) / 2) * amount / (k - 1))
        acc += np.asarray(A.cam(img, dy=off), dtype=np.float32)
    return Image.fromarray((acc / k).astype(np.uint8), "RGBA")
