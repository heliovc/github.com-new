# Handoff → Claude Code: Canal 5 "E se você fosse..." (POV animal, Shorts)

Data: 20/11/2026 · Origem: projeto "Canal Dark" no claude.ai

## Sua tarefa
1. Salvar este arquivo no repo em `canais/canal5/plano.md`.
2. Criar o pipeline do Canal 5 reaproveitando o que já existe nos outros canais (render por código, TTS grátis, robô publicador do servidor, `publish.json`, Buffer).
3. Produzir os **vídeos A e B do Dia 1** (roteiros no fim deste arquivo) como **piloto** e mostrar ao Helio ANTES de agendar a rotina diária.
4. Depois da aprovação: rotina de 2 vídeos/dia (Dias 1–15) e 1/dia (Dia 16+), seguindo as seções abaixo.
5. Manter um `canais/canal5/controle.md` com animais/temas usados e métricas por vídeo.

**Pendências que dependem do Helio:** criar o canal no YouTube (e conta Instagram/TikTok), aprovar o piloto, escolher o nome final.

> Nota de implementação (20/11): no repositório os canais ficam na raiz (`cosmic/`, `ptd/`, `lab/`, `quiet/`), então o Canal 5 ficou em `canal5/` (este arquivo é `canal5/plano.md`). Pipeline e decisões em `canal5/README.md`; controle em `canal5/controle.md`.

---

## 1. Conceito
- **Nome sugerido:** "Na Pele De" (alternativas: "Olhos de Bicho", "Se Eu Fosse Bicho"). Série fixa: "E se você fosse…"
- **Formato:** Shorts/Reels em 1ª pessoa: como as coisas funcionam por dentro, vistas por um animal. PT-BR.
- **Assinatura do canal:** todo vídeo tem 1 cena **"Visão do Bicho"** com o sentido real do animal (UV da abelha, térmico da cobra, câmera lenta da mosca, sonar do morcego, olho composto, campo magnético).
- **HUD de escala** no canto superior: "você: 5 mm · prédio: 90 m".
- **Personalidade por espécie:** mesma voz, jeito diferente (formiga prática, pombo malandro, gato blasé).

## 2. Monetização
- Regra atual do YouTube: 1.000 inscritos + 10 mi views de Shorts/90 dias OU 4.000 h de longos/12 meses.
- A partir de 01/02/2027: canais novos precisam de 8.000 h OU 20 mi views de Shorts/90 dias; para ganhar com Shorts, manter 10 mi views/90 dias.
- Estratégia:
  1. Shorts (2/dia → 1/dia).
  2. **1 longo por semana (domingo):** compilação de 8–12 min dos Shorts da semana + narração-ponte NOVA + abertura nova.
  3. Mesmo vídeo no Instagram Reels e TikTok via Buffer.
  4. Teste de versão EN a partir do Dia 16 se a retenção provar o formato.

## 3. Formato do Short
**40–55 s · 1080×1920 · 30 fps · 110–140 palavras (~2,6 palavras/s)**

| Tempo | Função | Regra |
|---|---|---|
| 0–2 s | Gancho | 1ª pessoa + contraste de escala. Frame 0 = imagem mais forte, já em movimento. Texto na tela = fala. |
| 2–10 s | Situação | Onde estou e por que é extremo pra mim. |
| 10–40 s | Mecanismo em 3 passos | 1 ideia e 1 cena por passo, comparando com o corpo/sentidos do animal. |
| ~25–35 s | Visão do Bicho | Re-engajamento: troca brusca de visual. |
| 40–50 s | Payoff | Fato mais surpreendente por ÚLTIMO. |
| últimos 2 s | Loop | Última frase emenda na primeira. |

- Frases ≤ 12 palavras; ≥ 1 número concreto; proibido "olá", "hoje vamos ver", "você sabia que".
- Todo fato com fonte (1–2 por vídeo, registrar no controle).
- **Nunca** cenas que incentivem pôr animal em perigo (micro-ondas, máquina de lavar, freezer).

## 4. Animação (estilo visual)
**Base: 2D vetorial animado por código (Python), custo zero.**
- Formas chapadas, contorno fino, sombras suaves, cores saturadas; 3 camadas de parallax.
- Câmera POV na altura dos olhos do animal, grande-angular, leve balanço de andar/voar/nadar.
- Patas/antenas/bico aparecem na borda da tela de vez em quando.
- **Corte raio-X:** máquina translúcida + fluxos (azul = frio, vermelho = quente, amarelo = eletricidade, verde = ar/água).
- **Visão do Bicho:** filtro por espécie (UV roxo, térmico, mosaico de olho composto, câmera lenta, ondas de sonar).
- Troca de cena a cada 5–8 s; 1 movimento principal por cena.
- **Anti-template:** paleta/cenário mudam a cada vídeo; nunca 2 vídeos seguidos com o mesmo tipo de abertura; capa diferente dos últimos 3.
- Opcional (gasta créditos): Kling image-to-video só nos 0–3 s.

## 5. Som
- TTS grátis PT-BR, **voz diferente da dos outros canais**.
- Trilha sem direitos (Biblioteca de Áudio do YouTube) a −20 dB sob a voz.
- SFX de escala: mundo humano grave/lento; animal agudo/rápido. 1 SFX por troca de cena; 0,3 s de silêncio antes do payoff.

## 6. Legendas
- Queimadas a ~60–65% da altura (fora dos botões do Shorts/Reels).
- 1–3 palavras por vez, sincronizadas palavra a palavra (tempos do TTS ou Whisper).
- Montserrat ExtraBold ou Anton, branco com contorno preto grosso.
- Palavra-chave em amarelo; números 1,3× maiores; máx. 1 emoji por vídeo.

## 7. Pipeline
1. Roteiro + plano de cenas → `script.json`
2. TTS → `voz.mp3` + tempos por palavra
3. Render das cenas por código
4. Legendas + SFX + trilha
5. Render final 1080×1920 + capa
6. `publish.json` → robô do servidor publica no YouTube; Buffer agenda Instagram/TikTok
7. Atualizar `controle.md`

Horários iniciais: **A 12h, B 19h** (Brasília).

## 8. Rotina diária
1. Ler `controle.md` (animais usados + métricas).
2. Tema do calendário (seção 9); checar fatos.
3. Escrever no formato da seção 11.
4. Checklist (seção 12).
5. Produzir e publicar.
6. Registrar no controle.
Domingo: longo semanal.

## 9. Calendário Dias 1–15 (sem repetir animal)
| Dia | A — escala extrema | B — mecânica do dia a dia |
|---|---|---|
| 1 | Formiga cai do 30º andar e sai andando (velocidade terminal) | Lagartixa atrás da geladeira (ciclo de refrigeração) |
| 2 | Mosquito atingido por gota de chuva (massa × impacto) | Barata no ralo (sifão: por que o cheiro não volta) |
| 3 | Krill na boca da baleia-azul (filtro de barbatanas) | Pombo no semáforo (como detecta carros) |
| 4 | Peixe a 8.000 m (pressão) | Rato no poço do elevador (cabos, contrapeso, freio) |
| 5 | Pulga pula 100× a altura (catapulta de resilina) | Cachorro no banco de trás (motor de 4 tempos) |
| 6 | Morcego no escuro (ecolocalização = sensor de ré) | Sabiá no fio de alta tensão (por que não leva choque) |
| 7 | Elefante ouvindo pelos pés (infrassom) | Mariposa na lâmpada (incandescente × LED) |
| 8 | Beija-flor, coração a 1.200 bpm | Capivara na represa (hidrelétrica) |
| 9 | Lula-gigante, olho do tamanho de uma bola | Aranha no controle remoto (infravermelho) |
| 10 | Abelha vendo ultravioleta | Cupim e o ar-condicionado do cupinzeiro |
| 11 | Cobra vendo calor (térmico) | Pardal no supermercado (código de barras) |
| 12 | Cachalote mergulhando 2 km | Gaivota no porto (navio de aço flutua) |
| 13 | Mosca vendo em câmera lenta | Minhoca embaixo da rua (bueiro e galeria de chuva) |
| 14 | Tartaruga marinha navegando pelo campo magnético | Hamster na rodinha (dínamo) |
| 15 | Polvo: 3 corações e sangue azul | Coruja na torre do relógio (relógio mecânico) |

**Reserva (Dia 16+):** ácaro no travesseiro, formiga-cortadeira e fungos, pinguim (pé que não congela), gato no telhado (escoamento/caixa-d'água), camaleão, vagalume, peixe-elétrico, urubu no aterro, mosquito no ar-condicionado split, pombo-correio, tubarão sentindo eletricidade, abelha e a colmeia hexagonal.

## 10. Regra do Dia 16
Métricas 48 h após postar (de `server-data/metrics` ou print do Studio):
1. "Continuaram assistindo" (meta ≥ 70%)
2. % visualizada média (meta ≥ 80%)
3. Views em 48 h
4. Inscritos por 1.000 views

- Ordenar os 30 vídeos por (1) e depois (2).
- Nos 5 melhores, marcar padrão: A/B · grupo do animal (inseto, ave, mamífero, marinho, réptil) · tipo de gancho (queda/perigo, número, lugar proibido, visão do bicho, som) · tema (casa, cidade, natureza, corpo).
- Dias 16–30: 70% padrão vencedor, 30% testes. Padrão com < 50% "continuaram assistindo" em 3 vídeos → pausar.

## 11. Formato de saída por vídeo
1. Título + gancho · 2. Narração com timestamps · 3. Plano de cenas (5–7): tempo, enquadramento, ação, luz/paleta, som, arte · 4. Legendas · 5. Descrição + pergunta para comentários + 3–5 hashtags (`#esevocefosse` sempre) · 6. Fontes

## 12. Checklist antes do render
1. 1ª frase com 1ª pessoa + contraste em ≤ 12 palavras?
2. Frame 0 com movimento e a imagem mais forte?
3. Mecanismo em 3 passos corretos, com fonte?
4. Tem a cena Visão do Bicho?
5. Fato mais forte no fim + loop para o início?
6. Nenhuma cena parada > 8 s?
7. Diferente dos últimos 3 em abertura, paleta e capa?
8. Nada que incentive maltratar animal?
9. 40–55 s e 110–140 palavras?

---

## 13. Roteiros do Dia 1 (piloto)

### Vídeo A — "E se você fosse uma formiga caindo do 30º andar?"
**Narração (~136 palavras)**
- 0–3s: Eu acabei de escorregar da janela do 30º andar. E vou sair andando.
- 3–12s: Pra você, o vento é uma brisa. Pra mim, é uma parede. Eu peso quase nada, mas tenho muita superfície pra esse peso.
- 12–27s: Quando algo cai, a gravidade puxa pra baixo e o ar empurra pra cima. Quanto menor você é, mais o ar ganha essa briga. Em menos de um segundo, eu paro de acelerar: uns 6 km/h, no máximo. Um humano passaria de 190.
- 27–38s: E a força do impacto depende de massa e velocidade. Minha massa é minúscula, minha velocidade é de passeio, e meu esqueleto fica por fora, como uma armadura.
- 38–50s: Por isso, no mundo animal, tamanho é destino: um camundongo levanta e vai embora. Um cavalo, não. Pra mim, cair de um prédio é só… um caminho mais longo.

**Cenas**
1. Close no parapeito, formiga escorrega · luz dourada · vento forte, buzinas
2. POV caindo, prédio passando devagar · contraluz · vento abafado
3. Tela dividida formiga × humano, setas gravidade ↓ / ar ↑ · whoosh + velocímetro
4. Câmera lenta tocando a calçada · luz de rua · "tic" minúsculo × baque grave
5. Raio-X do exoesqueleto (Visão do Bicho: olho composto no pouso) · luz azul · zumbido
6. Fila formiga → camundongo → cavalo · fundo neutro · batida
7. Câmera rasteira: formiga sai andando · passinhos + trilha sobe

**Legendas:** 30º ANDAR 😳 / o ar vira PAREDE / gravidade ↓ × ar ↑ / máx 6 km/h — humano +190 / impacto minúsculo / esqueleto POR FORA / TAMANHO É DESTINO

**Descrição:** Uma formiga cai do 30º andar e sai andando. A física explica. Qual animal você quer ser no próximo? 👇
`#esevocefosse #formiga #fisica #curiosidades #shorts`

### Vídeo B — "E se você fosse uma lagartixa atrás da geladeira?"
**Narração (~142 palavras)**
- 0–3s: Eu moro atrás da geladeira. E aqui é quente. Esse calor saiu lá de dentro.
- 3–15s: A geladeira não cria frio. Ela tira calor de dentro e joga aqui fora, em mim. Quem faz isso é um fluido que corre pelos canos: o gás refrigerante.
- 15–28s: Lá dentro, ele passa por canos com pressão baixa e evapora. E evaporar rouba calor, igual o suor secando na sua pele. Por isso tudo lá dentro esfria.
- 28–40s: Aí ele chega no motor, aqui embaixo: o compressor. Esse zumbido que eu escuto o dia todo. Ele espreme o gás e deixa ele quente, bem quente.
- 40–52s: Esse gás quente passa pela grade atrás da geladeira, solta o calor no ar e vira líquido de novo. E o ciclo recomeça. Ou seja: cada sorvete gelado que você tira lá de dentro… esquentou a minha casa.

**Cenas**
1. Close rasteiro: lagartixa na poeira, grade preta · luz alaranjada · zumbido grave
2. Raio-X da geladeira: canos azuis (frio) e vermelhos (quente) · líquido correndo
3. Congelador: gás evaporando em partículas azuis + pele suando · luz fria · chiado
4. Compressor: câmera treme, partículas vermelhas aceleram · zumbido sobe
5. Visão do Bicho (térmica): grade traseira brilhando de calor, lagartixa se aquecendo · estalos metálicos
6. Ciclo completo em loop animado · batida rítmica
7. Mão tira sorvete → lagartixa relaxada no calor · "tunc" da porta + trilha

**Legendas:** AQUI ATRÁS É QUENTE 🔥 / ela não cria frio / ela TIRA calor / evaporar = roubar calor / COMPRESSOR = o zumbido / calor sai pela grade / seu sorvete esquentou minha casa

**Descrição:** Por que atrás da geladeira é quente? Uma lagartixa explica. Qual eletrodoméstico a gente desmonta no próximo? 👇
`#esevocefosse #lagartixa #geladeira #comofunciona #shorts`
