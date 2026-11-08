#!/usr/bin/env bash
# Abre um Chrome "de verdade" (sem automação) na tela virtual do servidor para você logar
# na conta Google fitpaytech UMA vez. O robô reaproveita esse login.
#
# 1) No servidor:            sudo bash login.sh
# 2) No seu Mac (outro terminal):  ssh -L 5901:localhost:5901 root@138.197.111.48
# 3) No Mac: Finder → Ir → Conectar ao Servidor (cmd+K) → vnc://localhost:5901
#    (senha mostrada abaixo). Faça login no Google, abra studio.youtube.com, confira os 4 canais.
# 4) Feche a janela do Chrome. O script termina sozinho e religa o robô.
set -euo pipefail
BASE=/opt/canal-publisher
U=canal
systemctl stop canal-publisher.timer canal-metrics.timer 2>/dev/null || true
PASS=$(head -c 6 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9' | head -c 8)
sudo -u $U bash -c "mkdir -p $BASE/.vnc && x11vnc -storepasswd '$PASS' $BASE/.vnc/pass >/dev/null 2>&1"
sudo -u $U bash -c "Xvfb :1 -screen 0 1440x900x24 >/dev/null 2>&1 &"
sleep 2
sudo -u $U bash -c "x11vnc -display :1 -localhost -rfbport 5901 -rfbauth $BASE/.vnc/pass -forever -quiet -bg >/dev/null 2>&1"
echo "================================================"
echo " VNC pronto na porta 5901 (só via túnel SSH)."
echo " Senha do VNC: $PASS"
echo " Feche o Chrome quando terminar o login."
echo "================================================"
rm -f $BASE/profile/SingletonLock
sudo -u $U env DISPLAY=:1 google-chrome --user-data-dir=$BASE/profile --no-first-run --no-default-browser-check \
     --lang=pt-BR https://accounts.google.com/ "https://studio.youtube.com/" || true
pkill -u $U x11vnc || true
pkill -u $U Xvfb || true
systemctl start canal-publisher.timer canal-metrics.timer 2>/dev/null || true
echo "Login salvo. Teste:  sudo -u $U xvfb-run -a $BASE/venv/bin/python $BASE/repo/server/publisher/publisher.py check"
