#!/usr/bin/env bash
# Instala o robô publicador no servidor (Ubuntu 22.04/24.04). Rodar como root:
#   sudo bash setup.sh            (passo 1: instala tudo e mostra a chave para o GitHub)
#   sudo bash setup.sh clone      (passo 2: depois de cadastrar a chave no GitHub)
set -euo pipefail
BASE=/opt/canal-publisher
REPO_URL=git@github.com:heliovc/github.com-new.git
U=canal

step_install() {
  apt-get update -y
  DEBIAN_FRONTEND=noninteractive apt-get install -y git python3-venv python3-pip xvfb x11vnc wget ca-certificates \
      fonts-liberation fonts-noto-color-emoji fonts-noto-core xauth
  if ! command -v google-chrome >/dev/null; then
    wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    DEBIAN_FRONTEND=noninteractive apt-get install -y /tmp/chrome.deb
  fi
  id -u $U >/dev/null 2>&1 || useradd --system --home-dir $BASE --shell /bin/bash $U
  mkdir -p $BASE/{profile,state,logs,.ssh}
  chown -R $U:$U $BASE
  chmod 700 $BASE/.ssh $BASE/profile
  sudo -u $U python3 -m venv $BASE/venv
  sudo -u $U $BASE/venv/bin/pip install -q --upgrade pip
  sudo -u $U $BASE/venv/bin/pip install -q playwright==1.63.0
  if [ ! -f $BASE/.ssh/id_ed25519 ]; then
    sudo -u $U ssh-keygen -t ed25519 -N "" -C "canal-publisher@$(hostname)" -f $BASE/.ssh/id_ed25519 >/dev/null
  fi
  sudo -u $U bash -c "ssh-keyscan -t ed25519 github.com >> $BASE/.ssh/known_hosts 2>/dev/null"
  [ -f /etc/canal-publisher.env ] || { echo "ATENÇÃO: crie /etc/canal-publisher.env (modelo em canal-publisher.env.example)"; }
  echo
  echo "=================================================================="
  echo " CADASTRE ESTA CHAVE NO GITHUB (repo heliovc/github.com-new):"
  echo "   Settings → Deploy keys → Add deploy key → marque 'Allow write access'"
  echo "------------------------------------------------------------------"
  cat $BASE/.ssh/id_ed25519.pub
  echo "=================================================================="
  echo " Depois rode:  sudo bash setup.sh clone"
}

step_clone() {
  if [ ! -d $BASE/repo/.git ]; then
    sudo -u $U git clone --depth 1 $REPO_URL $BASE/repo
  fi
  SRC=$BASE/repo/server/publisher
  [ -f /etc/canal-publisher.env ] || cp $SRC/canal-publisher.env.example /etc/canal-publisher.env
  cp $SRC/systemd/*.service $SRC/systemd/*.timer /etc/systemd/system/
  systemctl daemon-reload
  echo
  echo "Instalado. Próximo passo: login no Google (uma vez):  sudo bash $SRC/login.sh"
  echo "Depois do login:  sudo bash $SRC/setup.sh enable"
}

step_enable() {
  systemctl enable --now canal-publisher.timer canal-metrics.timer
  systemctl list-timers 'canal-*'
}

case "${1:-install}" in
  install) step_install ;;
  clone)   step_clone ;;
  enable)  step_enable ;;
  *) echo "uso: setup.sh [install|clone|enable]"; exit 1 ;;
esac
