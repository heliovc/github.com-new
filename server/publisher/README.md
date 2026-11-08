# Robô publicador — Canais Dark (roda no servidor, sem o Mac)

O que ele faz:
- **A cada 10 min:** baixa este repositório e procura `publish.json` nas pastas dos episódios. Publica no YouTube Studio o que estiver pendente (vídeo, título, descrição, thumbnail, legenda, "feito com IA", tags, agendamento) e grava o resultado em `server-data/published.json`.
- **Todo dia às 08:50:** coleta as métricas dos 4 canais e grava em `server-data/metrics/AAAA-MM-DD.json`.
- **Antes de subir:** confere se já existe vídeo com o mesmo título no canal (evita duplicar quando o Claude publica pelo Chrome do Mac).
- **Se der erro:** tenta até 3 vezes, tira print (`/opt/canal-publisher/logs`) e avisa no celular (opcional, via ntfy).

Como funciona: um Google Chrome de verdade, numa tela virtual (Xvfb), com a conta **fitpaytech** logada uma vez. Usa os mesmos passos que as rotinas já validaram no Studio.

> Transição: a API oficial do YouTube exige auditoria do Google para publicar vídeo público (sem ela, fica privado). Enquanto a auditoria não sai, o robô de navegador resolve. Ver `claude/auditoria-api-youtube.md` no Projeto.

---

## Instalação (uma vez, ~20 min)

Pode pedir para o Claude Code do VSCode fazer: "conecte no droplet 138.197.111.48 e siga server/publisher/README.md".

**0. Requisitos:** Ubuntu 22.04+ e ≥ 2 GB de RAM livres (Chrome + upload). Conferir com `free -h`. Se faltar, criar swap de 2 GB.

**1. Instalar**
```bash
ssh root@138.197.111.48
git clone --depth 1 https://github.com/heliovc/github.com-new /tmp/gcn
sudo bash /tmp/gcn/server/publisher/setup.sh
```
No fim ele mostra uma **chave SSH**. Cadastre no GitHub em heliovc/github.com-new → Settings → Deploy keys → **Add deploy key**, marcando **Allow write access**.

**2. Clonar e configurar**
```bash
sudo bash /tmp/gcn/server/publisher/setup.sh clone
sudo nano /etc/canal-publisher.env      # opcional: NOTIFY_URL (ntfy) e GRACE_MINUTES
```

**3. Login no Google (só você pode fazer, 5 min)**
```bash
sudo bash /opt/canal-publisher/repo/server/publisher/login.sh
```
- Em **outro terminal do Mac**: `ssh -L 5901:localhost:5901 root@138.197.111.48`
- No Mac: Finder → **Ir → Conectar ao Servidor** (cmd+K) → `vnc://localhost:5901` → senha mostrada pelo script.
- No Chrome do servidor: entre na conta **fitpaytech@gmail.com** (o Google pode pedir confirmação no celular). Abra studio.youtube.com e confira se os 4 canais aparecem. Depois **feche o Chrome**.

**4. Testar**
```bash
sudo -u canal xvfb-run -a /opt/canal-publisher/venv/bin/python /opt/canal-publisher/repo/server/publisher/publisher.py check
```
Precisa aparecer "login OK" e "OK" nos 4 canais.

Teste real com um vídeo **privado** (exige um `publish.json` no repo):
```bash
sudo -u canal bash -c 'set -a; . /etc/canal-publisher.env; xvfb-run -a /opt/canal-publisher/venv/bin/python /opt/canal-publisher/repo/server/publisher/publisher.py test-upload --key <key>'
```
Depois de conferir no Studio, apague o vídeo de teste.

**5. Ligar**
```bash
sudo bash /opt/canal-publisher/repo/server/publisher/setup.sh enable
```

---

## Dia a dia

| Para quê | Comando |
|---|---|
| Ver o que ele faria agora | `sudo -u canal bash -c 'set -a; . /etc/canal-publisher.env; /opt/canal-publisher/venv/bin/python /opt/canal-publisher/repo/server/publisher/publisher.py plan'` |
| Log | `tail -f /opt/canal-publisher/logs/publisher.log` |
| Prints de erro | `ls -t /opt/canal-publisher/logs/*.png | head` |
| Rodar já | `sudo systemctl start canal-publisher.service` |
| Timers | `systemctl list-timers 'canal-*'` |
| Google pediu login de novo | repetir o passo 3 |

O código se atualiza sozinho: a cada execução ele faz `git reset --hard origin/main`, então qualquer correção feita em `server/publisher/` no GitHub entra na próxima rodada.

## Contrato com as rotinas do Claude
- Toda pasta de episódio leva um `publish.json` (modelo: `publish.example.json`; regras em `manifest.py`).
- `key` precisa ser única (ex.: `ptd-ep07-long`, `cosmic-ep06-short`, `cosmic-rank05`, `quiet-ep03-long`, `lab-ep04-long`).
- Datas sempre com fuso: `2026-11-08T18:00:00-03:00`. `publish_at: null` = publicar já.
- Se a rotina publicar pelo Chrome do Mac, ela preenche `done_url` e o robô pula. Mesmo sem isso, o robô não duplica: ele confere o título no Studio.
- `GRACE_MINUTES=90`: o robô espera 90 min depois de `created_at`, para dar tempo de a rotina publicar pelo Mac. Quando o Mac sair de vez do fluxo, mude para `0`.
- **Não apague a pasta do episódio** antes de `server-data/published.json` mostrar `"status": "published"` em todas as keys dela.
- Saídas para as rotinas lerem: `server-data/published.json` (links), `server-data/heartbeat.json` (o robô está vivo?) e `server-data/metrics/*.json`.

## Limitações conhecidas (v1)
- "Vídeo relacionado" dos Shorts ainda não é feito pelo robô.
- Se o Studio mudar o layout, um passo pode quebrar. O print do erro mostra onde; é só ajustar o seletor em `studio.py`.
- Os testes em `tests/` usam um Studio falso (`pytest -q tests/`). Eles validam a lógica, não o Studio real.
