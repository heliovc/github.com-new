#!/usr/bin/env bash
# Canal 5 — prepara o ambiente para renderizar (Mac ou nuvem). Idempotente. Uso: bash canal5/setup.sh
# Precisa de Python >= 3.10 (kokoro-onnx). Fontes já vêm no repositório (canal5/fonts).
set -u
log() { echo "[canal5-setup] $*"; }
PY=${PY:-python3}
PKGS="kokoro-onnx soundfile numpy pillow imageio-ffmpeg"
$PY -m pip install --break-system-packages -q $PKGS 2>/dev/null || $PY -m pip install -q $PKGS
$PY -c "import kokoro_onnx, soundfile, numpy, PIL, imageio_ffmpeg" && log "python OK" || log "ERRO: pacotes python ($PY)"

K=~/.cache/kokoro; mkdir -p $K
REL=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -s $K/kokoro-v1.0.onnx ] || curl -fsSL -o $K/kokoro-v1.0.onnx $REL/kokoro-v1.0.onnx
[ -s $K/voices-v1.0.bin ] || curl -fsSL -o $K/voices-v1.0.bin $REL/voices-v1.0.bin
[ -s $K/kokoro-v1.0.onnx ] && [ -s $K/voices-v1.0.bin ] && log "voz Kokoro OK" || log "ERRO: modelos Kokoro"
log "pronto: $PY -I canal5/pipeline/engine.py canal5/<episodio> --sheet"
