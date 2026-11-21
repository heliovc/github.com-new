# Canal 5 — "E se você fosse…" (Shorts POV animal, PT-BR)

Plano completo: `plano.md`. Controle (animais usados, fontes, métricas, decisões): `controle.md`.

## Como um vídeo é feito
Tudo por código, custo zero: voz neural brasileira (Microsoft, via edge-tts, com tempo por palavra), desenho 2D vetorial em Python (PIL), trilha e efeitos sintetizados.

```
canal5/
  pipeline/engine.py      motor: voz + tempos por palavra, legendas, HUD, etiquetas, Visão do Bicho, áudio, render paralelo
  pipeline/art.py         kit de desenho (superamostragem, setas, etiquetas, gradientes, olho composto, visão noturna)
  pipeline/audio.py       trilha (marimba/pluck), efeitos (whoosh, vento, tic, baque, zumbido…) e mixagem
  pipeline/scenes/*.py    cenas de cada episódio (uma função por cena: fn(ctx, lt) -> imagem 1080x1920)
  pipeline/scenes/common.py  peças reaproveitáveis (calçada portuguesa, nuvens, borrão de movimento)
  fonts/                  Anton + Montserrat (licença OFL junto)
  assets/emoji/           emojis Noto (Apache 2.0) usados nas etiquetas
  dNNx-animal/            um episódio: script.json -> video.mp4, capa.jpg, legendas.srt, timeline.json, publish.draft.json
```

### Passo a passo de um episódio novo
1. Copiar `d01a-formiga/script.json` para `dNNx-animal/script.json` e reescrever: `beats` (uma frase por item; `*palavra*` = destaque amarelo; `scene` = id da cena; o último beat leva `"payoff": true` e `"pause_before": 0.3`), `scenes` (HUD, etiquetas com `at` = palavra que dispara, SFX, `vision`), `say_map` (só para a voz Kokoro; a voz neural lê números e unidades sozinha), `music` (bpm/tom/semente diferentes a cada vídeo), `publish` e `sources`.
2. Criar `pipeline/scenes/<animal>.py` com uma função por id de cena. `ctx.wt("palavra")` dá o instante (s) em que a palavra é falada dentro da cena, para sincronizar a animação com a narração.
3. Capa (`cover` no script.json): `t` = instante do quadro de fundo (escolha um em que o bicho aparece inteiro e grande), `title` = 2–3 linhas curtas do título, `focus` = [x, y] de onde o bicho está nesse quadro, `zoom` (1,0–1,6; cuidado para não aparecer borda preta), `at` = [x, y] onde o bicho fica na capa (padrão 540, 1240), `r` = raio do anel amarelo (~270–440). A capa sai com a faixa amarela "E SE VOCÊ FOSSE…", o título, um anel no bicho com o selo "VOCÊ" e a seta (você = o bicho) e "NA PELE DE" embaixo. Refazer só a capa, sem voz: `python3 -I canal5/pipeline/engine.py canal5/dNNx-animal --cover` (usa o timeline.json). Abrir `capa.jpg` e conferir: bicho dentro do anel, selo sem tapar o título, sem borda preta.
4. Revisar sem gerar vídeo: `python3 -I canal5/pipeline/engine.py canal5/dNNx-animal --sheet` (folha de contato em `.cache/sheet.png`) e `--stills 0,12.5` (quadros em tamanho real).
5. Render: `python3 -I canal5/pipeline/engine.py canal5/dNNx-animal` (~3 min no Mac com 8 núcleos).
6. Publicar: copiar `publish.draft.json` para `publish.json` (o `channel_id` e o `publish_at` vêm do bloco `publish` do script.json; A 12:00, B 19:00, com `-03:00`). O robô do servidor publica **qualquer** `publish.json` que chegar na `main`.
7. Atualizar `controle.md`.

### Regras que o motor já cumpre
- 1080×1920, 30 fps, H.264 + AAC; volume final ≈ −16 dB médio.
- Legenda queimada a ~62% da altura, 1–3 palavras, palavra a palavra; destaque amarelo; números 1,3× maiores.
- HUD de escala no topo ("VOCÊ: 5 mm · PRÉDIO: 90 m"), etiqueta da cena logo abaixo (máx. 1 emoji por vídeo).
- Troca de cena com "soco" de zoom + flash curto + 1 SFX; trilha a −20 dB; 0,3 s de silêncio antes do payoff.
- `vision: {"type": "compound"}` aplica o olho composto; outras visões (noturna, UV, térmica, sonar) ficam na própria cena (`art.night_reveal` é a primeira).

### Sobre a capa no YouTube
O YouTube não aceita capa enviada para Shorts: no feed de Shorts aparece um quadro do próprio vídeo (por isso o quadro 0 tem de ser a imagem mais forte). O robô só envia `capa.jpg` em vídeos longos. A capa serve para Instagram/TikTok (Buffer), para o longo semanal e, se o Hélio quiser, para escolher manualmente no app do YouTube.

## Ambiente
- Mac: `~/.venvs/canal5` (Python 3.11 via `uv`). Rodar com `~/.venvs/canal5/bin/python -I canal5/pipeline/engine.py …`.
- Nuvem / máquina nova: `bash canal5/setup.sh` (se der `cannot import name '_imaging' from 'PIL'`, rode `python3 -m pip install --break-system-packages --ignore-installed pillow`) (pacotes Python e ffmpeg; testa a voz neural). Rotina diária: prompt em `canal5/rotina.md`.
- Voz: `"tts": {"engine": "edge", "voice": "pt-BR-ThalitaMultilingualNeural", "rate": "+0%"}` no script.json (precisa de internet). Kokoro (`"engine": "kokoro"`, offline) continua disponível, mas soa estrangeira em PT-BR e foi REPROVADA pelo Hélio: não usar.
- Na nuvem, a voz só funciona se o ambiente liberar `speech.platform.bing.com` na rede (sem isso: erro 403 no proxy / "No server date in headers"). Se a voz falhar 2 vezes, parar sem entregar e avisar o Hélio.
