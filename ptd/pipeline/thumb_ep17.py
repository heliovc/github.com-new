# Thumbnail EP17 (estilo do thumb_ep07/ep16): à esquerda, o cronômetro do golpe (cena "clock") com o anel vermelho
# quase cheio e "10 s" no centro; à direita, a frase em 3 linhas ("SEU PIX / SUMIU EM / 10 SEGUNDOS") e o selo
# "SÓ 8,9% VOLTA" (de cada R$ 100 notificados em golpes, R$ 8,90 devolvidos — BC via O POVO, jul/2026).
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import render as R
G, BG1, W_, AM, RED = R.GREEN, R.BG1, R.WHITE, R.AMBER, R.RED
F = R.F
def logo(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    m = size * 0.14; s = size - 2 * m
    d.rounded_rectangle([m, m, m + s, m + s], int(s * 0.22), fill=G)
    d.text((size / 2, size / 2 + size * 0.02), "$", font=F(int(size * 0.62), "Black"), fill=BG1, anchor="mm")
    return img
old = (R.W, R.H); R.W, R.H = 1280, 720
t = R.make_bg().convert("RGBA"); R.W, R.H = old
R._stopwatch(t, 330, 390, 245, 0.88, 1.0, "10 s", "R$ 3.000 · sumiu", (230, 70, 60), lw=26)
d = ImageDraw.Draw(t)
d.text((640, 135), "SEU PIX", font=F(104, "Black"), fill=W_, anchor="lm")
d.text((640, 255), "SUMIU EM", font=F(104, "Black"), fill=W_, anchor="lm")
d.text((640, 380), "10 SEGUNDOS", font=F(84, "Black"), fill=AM, anchor="lm")
d.rounded_rectangle([640, 470, 1180, 570], 22, fill=(70, 30, 34))
d.text((910, 520), "SÓ 8,9% VOLTA", font=F(62, "Black"), fill=(255, 150, 130), anchor="mm")
lg = logo(60); t.alpha_composite(lg, (40, 645))
d.text((112, 675), "POR TRÁS DO DINHEIRO", font=F(26, "Bold"), fill=G, anchor="lm")
t.convert("RGB").save(sys.argv[1], quality=92); print("ok")
