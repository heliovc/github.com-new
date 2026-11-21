# Canal 5 — controle ("E se você fosse…")

Ler antes de cada vídeo (plano.md, seção 8). Atualizar depois de produzir e 48 h depois de publicar.

## Status do canal
- Nome: **Na Pele De** — YouTube `@napeledebicho`, channel_id `UCO5Fa5_HJxd-aeTiyQcw0Sw` (criado pelo Hélio em 20/11/2026). Cadastrado em `server/publisher/channels.json`.
- Instagram / TikTok: **pendente (Hélio criar)**; depois, ligar no Buffer.
- Piloto (Dia 1 A e B): aprovado pelo Hélio em 20/11/2026. O robô agendou para 21/11, mas o Hélio pediu para sair no mesmo dia: formiga pública em 20/11 22:00 e lagartixa às 23:00 (ajuste manual no Studio; o robô não reagenda vídeo já enviado).
- Rotina diária na nuvem: LIGADA em 20/11/2026 (OK do Hélio), prompt em `rotina.md`, 06:30 Brasília, até 2 dias adiantado. Dia 2 = 21/11.
- Pendente: longo semanal de domingo (compilação) ainda não implementado; Instagram/TikTok no Buffer.

## Animais e temas usados
| Dia | Vídeo | Animal | Grupo | Tipo | Gancho | Tema | Paleta | Abertura | Visão do Bicho | Duração | Palavras | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | formiga | inseto | escala extrema | queda/perigo | cidade | fim de tarde dourado | escorregando do parapeito | olho composto (mosaico hexagonal no pouso) | 48,5 s | 136 | público 20/11 22:00 |
| 1 | B | lagartixa | réptil | mecânica do dia a dia | lugar proibido | casa | cozinha à noite, laranja × azul | close rasteiro atrás da geladeira | cores no escuro (visão noturna em cores) | 45,6 s | 137 | público 20/11 23:00 |

## Fontes por vídeo
**1A — formiga**
- University of Illinois, Physics Van Q&A, "An ant Dropped off the Empire State Building" — velocidade terminal de formiga pequena ≲ 2 m/s (≈ 6–7 km/h). https://van.physics.illinois.edu/ask/listing/2099
- Universe Today / FAI — pessoa de barriga para baixo ≈ 195–200 km/h. https://www.universetoday.com/articles/terminal-velocity · https://fai.org/node/24646
- J.B.S. Haldane, "On Being the Right Size" (1926) — camundongo sai andando, cavalo não.

**1B — lagartixa**
- Danfoss, "How a refrigerator works"; Penn State EGEE 102, "6.4 Refrigerators" — evaporador, compressor, condensador, tubo capilar. https://www.danfoss.com/en/about-danfoss/our-businesses/cooling/the-fridge-how-it-works · https://courses.ems.psu.edu/egee102/node/2402
- Roth & Kelber (2004), "Nocturnal colour vision in geckos", Proc. R. Soc. B — lagartixas noturnas enxergam cores com luz muito fraca. https://pmc.ncbi.nlm.nih.gov/articles/PMC1810110

## Métricas (48 h após publicar)
Metas: continuaram assistindo ≥ 70% · % visualizada ≥ 80%.

| Vídeo | Publicado em | Link | Continuaram assistindo | % visualizada | Views 48 h | Inscritos / 1.000 views |
|---|---|---|---|---|---|---|
| 1A formiga | 20/11 22:00 | https://youtube.com/shorts/Wcw5EPuTlpg | — | — | — | — |
| 1B lagartixa | 20/11 23:00 | https://youtube.com/shorts/v88xGAAAzmw | — | — | — | — |

## Decisões e desvios do plano
- **20/11 — Visão do Bicho da lagartixa:** o roteiro pedia visão térmica, mas lagartixa não enxerga calor (quem enxerga é cobra, Dia 11A). Trocado pelo sentido real: enxergar cores no escuro (Roth & Kelber 2004). A cena de calor continua como raio-X explicativo.
- **20/11 — Trilha e efeitos:** sintetizados por código (`pipeline/audio.py`), em vez da Biblioteca de Áudio do YouTube: não depende de download manual e não tem risco de direitos. Trilha a −20 dB sob a voz, 0,3 s de silêncio antes do payoff.
- **20/11 — Voz:** o Hélio achou a Kokoro `pf_dora` com sotaque de estrangeiro. Trocada pela voz neural brasileira `pt-BR-ThalitaMultilingualNeural` (Microsoft, via edge-tts, grátis), velocidade normal. Ela também devolve o tempo exato de cada palavra, que agora sincroniza a legenda. Alternativas com amostra: Francisca e Antonio. Nenhum outro canal usa essas vozes. Risco: edge-tts usa o serviço de leitura do navegador Edge, não oficial; a via oficial com a mesma voz é o Azure Speech (camada grátis de 500 mil caracteres/mês, exige conta Azure).
- **20/11 — Palavras:** contagem corrigida (a primeira versão contava pontuação como palavra): 136 e 137 palavras, dentro de 110–140.
- **20/11 — Cenas:** 9 cenas por vídeo (o plano sugere 5–7), para manter troca a cada ~5 s.
- 20/11: comentário fixado sempre SEM emoji (o YouTube mostra o emoji como imagem e o robô não reconhecia o próprio comentário: a formiga ganhou 3 cópias, 2 apagadas). Fixar comentário no canal novo exige verificar o telefone no YouTube (pendente do Hélio).
- 20/11: a rede da nuvem bloqueia o servidor da voz (speech.platform.bing.com, 403 no proxy). A rotina só produz depois que o domínio for liberado no ambiente.
- 21/11 — **Capa nova** (pedido do Hélio): faixa amarela "E SE VOCÊ FOSSE…" maior, título, bicho ampliado dentro de um anel amarelo com o selo "VOCÊ" e seta (a ideia da série: você = o bicho), "NA PELE DE" no rodapé; o "º" agora sai certo. Campos novos em `cover`: `focus`, `zoom`, `at`, `r`. Capas do Dia 1 refeitas. Obs.: o YouTube não usa capa enviada em Shorts; ela vale para Instagram/TikTok, longo semanal e escolha manual no app.
- 21/11 — Rotina das 06:30 não produziu o Dia 2: a voz continua bloqueada na rede da nuvem (403 em speech.platform.bing.com). Dia 2 (mosquito + barata) fica para a próxima rodada depois da liberação.

