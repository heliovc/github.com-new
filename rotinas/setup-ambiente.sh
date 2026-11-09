#!/usr/bin/env bash
# Prepara o container da nuvem (rotinas do Claude) para renderizar os vídeos dos canais.
# Idempotente: pode rodar toda vez. Uso, na raiz do repositório:  bash claude/setup-ambiente.sh
# Instala: pacotes Python, ffmpeg, fontes (Inter, Poppins, Lora, DejaVu Mono) e os modelos de voz Kokoro
# em ~/.cache/kokoro (copie ou ligue para <canal>/models/).
set -u
log() { echo "[setup] $*"; }
SUDO=""
if [ "$(id -u)" != 0 ] && command -v sudo >/dev/null 2>&1; then SUDO="sudo"; fi
TMP=$(mktemp -d)

# ---------------------------------------------------------------- Python
# "python3 -m pip": no container da nuvem o comando pip é de outro Python (3.13) e o python3 é o 3.11
python3 -m pip install --break-system-packages -q kokoro-onnx soundfile numpy pillow 2>/dev/null \
  || python3 -m pip install -q kokoro-onnx soundfile numpy pillow
python3 -c "import kokoro_onnx, soundfile, numpy, PIL" && log "python OK" || log "ERRO: pacotes python"

# ---------------------------------------------------------------- ffmpeg
APT_UPDATED=0
apt_install() {
  if [ $APT_UPDATED = 0 ]; then $SUDO apt-get update -qq >/dev/null 2>&1; APT_UPDATED=1; fi
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq "$@" >/dev/null 2>&1
}
command -v ffmpeg >/dev/null 2>&1 || apt_install ffmpeg
if ! command -v ffmpeg >/dev/null 2>&1; then
  python3 -m pip install --break-system-packages -q imageio-ffmpeg 2>/dev/null || python3 -m pip install -q imageio-ffmpeg
  FF=$(python3 -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())" 2>/dev/null)
  [ -n "$FF" ] && $SUDO ln -sf "$FF" /usr/local/bin/ffmpeg
fi
command -v ffmpeg >/dev/null 2>&1 && log "ffmpeg OK" || log "ERRO: sem ffmpeg"
command -v ffprobe >/dev/null 2>&1 || log "aviso: sem ffprobe (meça duração com soundfile ou 'ffmpeg -i')"

# ---------------------------------------------------------------- fontes
fetch() {  # url destino
  [ -s "$2" ] && return 0
  $SUDO mkdir -p "$(dirname "$2")"
  curl -fsSL "$1" -o "$TMP/f" && $SUDO cp "$TMP/f" "$2"
}
INTER=/usr/share/fonts/opentype/inter
[ -s $INTER/Inter-Bold.otf ] || apt_install fonts-inter
if [ ! -s $INTER/Inter-Bold.otf ]; then
  curl -fsSL -o "$TMP/inter.zip" https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip \
    && python3 -c "import zipfile,sys; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])" "$TMP/inter.zip" "$TMP/inter" \
    && $SUDO mkdir -p $INTER && find "$TMP/inter" -name 'Inter-*.otf' -exec $SUDO cp {} $INTER/ \;
fi
[ -s $INTER/Inter-Bold.otf ] && log "Inter OK" || log "ERRO: fonte Inter"

GF=/usr/share/fonts/truetype/google-fonts
GH=https://raw.githubusercontent.com/google/fonts/main/ofl
for w in Thin ExtraLight Light Regular Medium SemiBold Bold ExtraBold Black Italic; do
  fetch "$GH/poppins/Poppins-$w.ttf" "$GF/Poppins-$w.ttf"
done
fetch "$GH/lora/Lora%5Bwght%5D.ttf" "$GF/Lora-Variable.ttf"
fetch "$GH/lora/Lora-Italic%5Bwght%5D.ttf" "$GF/Lora-Italic-Variable.ttf"
[ -s $GF/Poppins-Bold.ttf ] && log "Poppins OK" || log "ERRO: fonte Poppins"
[ -s $GF/Lora-Variable.ttf ] && log "Lora OK" || log "ERRO: fonte Lora"

DJ=/usr/share/fonts/truetype/dejavu
[ -s $DJ/DejaVuSansMono-Bold.ttf ] || apt_install fonts-dejavu-core
if [ ! -s $DJ/DejaVuSansMono-Bold.ttf ]; then
  curl -fsSL -o "$TMP/dj.tar.bz2" https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.tar.bz2 \
    && tar -xjf "$TMP/dj.tar.bz2" -C "$TMP" && $SUDO mkdir -p $DJ && $SUDO cp "$TMP"/dejavu-fonts-ttf-2.37/ttf/DejaVuSans*.ttf $DJ/
fi
[ -s $DJ/DejaVuSansMono-Bold.ttf ] && log "DejaVu OK" || log "ERRO: fonte DejaVu"

# ---------------------------------------------------------------- voz (Kokoro)
K=~/.cache/kokoro
mkdir -p $K
REL=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -s $K/kokoro-v1.0.onnx ] || curl -fsSL -o $K/kokoro-v1.0.onnx $REL/kokoro-v1.0.onnx
[ -s $K/kokoro-v1.0.int8.onnx ] || curl -fsSL -o $K/kokoro-v1.0.int8.onnx $REL/kokoro-v1.0.int8.onnx
[ -s $K/voices-v1.0.bin ] || curl -fsSL -o $K/voices-v1.0.bin $REL/voices-v1.0.bin
ls -la $K | sed 's/^/[setup] /'
log "modelos: copie para <canal>/models/ (kokoro.onnx = kokoro-v1.0.onnx, ou o int8 no Por Trás do Dinheiro; voices.bin = voices-v1.0.bin)"
rm -rf "$TMP"
