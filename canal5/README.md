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
3. Capa v2 (21/11): no módulo da cena, `cover_bg(cv)` = cenário do gancho SEM o bicho e `cover_sprite(cv)` = o bicho sozinho, grande, fundo transparente (modelos em `scenes/formiga.py` e `scenes/lagartixa.py`). No script.json, `cover`: `t`, `focus` = [x, y] do ponto do cenário que vai para `at`, `zoom`, `at` = centro do bicho na capa (~540, 1150), `title` = 2 linhas curtas com o bicho entre `*asteriscos*` (amarelo), `hook` = chip de 2–4 palavras (ex. "QUEDA DE 90 METROS"), `sprite_s` (tamanho), `sprite_rot` (graus), `you` = [x, y] da cabeça (seta do selo VOCÊ), `you_side` = "left"/"right". O motor desfoca o cenário, põe raios de luz atrás, recorta o bicho com contorno branco e sombra, faixa "E SE VOCÊ FOSSE…" no topo e "NA PELE DE" embaixo. Sem `cover_sprite` no módulo, cai na capa antiga (quadro do vídeo + anel). Refazer só a capa, sem voz: `python3 -I canal5/pipeline/engine.py canal5/dNNx-animal --cover`.
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
Shorts aceitam miniatura enviada no Studio (botão "Enviar arquivo" da página de edição, 9:16), mas só com o canal verificado por telefone (visto em 21/11: "Para adicionar miniaturas personalizadas, confirme seu número de telefone"). O `publish.draft.json` já sai com `"thumbnail": "capa.jpg"`: o robô guarda uma cópia da capa no servidor e, depois do envio do Short, sobe a miniatura na página de edição. Enquanto o canal não for verificado, ele tenta de novo a cada 6 h sem gastar tentativa (o mesmo vale para fixar o comentário). Em vídeos longos, a miniatura sobe no próprio envio.
