#!/usr/bin/env bash
# Canal 5 — prepara o ambiente para renderizar (Mac ou nuvem). Idempotente. Uso: bash canal5/setup.sh
# Precisa de Python >= 3.10. Fontes já vêm no repositório (canal5/fonts).
set -u
log() { echo "[canal5-setup] $*"; }
PY=${PY:-python3}
PKGS="edge-tts soundfile numpy pillow imageio-ffmpeg"
[ "${CANAL5_KOKORO:-0}" = 1 ] && PKGS="$PKGS kokoro-onnx"
$PY -m pip install --break-system-packages -q $PKGS 2>/dev/null || $PY -m pip install -q $PKGS
$PY -I -c "from PIL import Image" 2>/dev/null || $PY -m pip install --break-system-packages -q --ignore-installed pillow
$PY -I -c "import edge_tts, soundfile, numpy, imageio_ffmpeg; from PIL import Image" && log "python OK" || log "ERRO: pacotes python ($PY)"

# voz: neural brasileira via edge-tts (padrão, precisa de internet). Kokoro só se CANAL5_KOKORO=1 (offline, soa estrangeira).
$PY -c "import asyncio, os, ssl, edge_tts, edge_tts.communicate as etc
if os.environ.get('SSL_CERT_FILE'): etc._SSL_CTX = ssl.create_default_context(cafile=os.environ['SSL_CERT_FILE'])
async def t():
    n = 0
    async for ch in edge_tts.Communicate('teste', 'pt-BR-ThalitaMultilingualNeural').stream():
        n += ch['type'] == 'audio'
    assert n
asyncio.run(t())" && log "voz neural OK" || log "ERRO: voz neural (edge-tts) não respondeu"
if [ "${CANAL5_KOKORO:-0}" = 1 ]; then
  K=~/.cache/kokoro; mkdir -p $K
  REL=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
  [ -s $K/kokoro-v1.0.onnx ] || curl -fsSL -o $K/kokoro-v1.0.onnx $REL/kokoro-v1.0.onnx
  [ -s $K/voices-v1.0.bin ] || curl -fsSL -o $K/voices-v1.0.bin $REL/voices-v1.0.bin
fi
log "pronto: $PY -I canal5/pipeline/engine.py canal5/<episodio> --sheet"
