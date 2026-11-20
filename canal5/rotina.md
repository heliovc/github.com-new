# Canal 5 — prompt da rotina diária (NÃO agendada: só depois de o Hélio aprovar o piloto e criar o canal)

Rotina na nuvem (Claude Code, ambiente "Ambiente Cloud Padrão", fonte github.com-new), como as dos outros canais.
Horário sugerido: 06:30 BRT, produzindo o par do dia (A 12:00 e B 19:00). Dias 1–15: 2 vídeos; Dia 16+: 1 vídeo.

---

Você produz os Shorts do Canal 5 ("E se você fosse…") no repositório github.com-new.

1. `bash canal5/setup.sh`.
2. Leia `canal5/plano.md` (seções 3–12) e `canal5/controle.md`. Descubra o próximo dia do calendário (seção 9) que ainda não está no controle. Nunca repita animal; mude paleta, abertura e capa em relação aos últimos 3.
3. Cheque os fatos de cada roteiro em fontes confiáveis (1–2 por vídeo) e corrija o roteiro se o fato não se sustentar. A "Visão do Bicho" tem que ser o sentido REAL do animal.
4. Escreva `canal5/dNNa-<animal>/script.json` e `canal5/dNNb-<animal>/script.json` (modelo: `d01a-formiga`): 110–140 palavras, frases ≤ 12 palavras, gancho em 1ª pessoa com contraste de escala, payoff por último, última frase emendando na primeira.
5. Escreva as cenas em `canal5/pipeline/scenes/<animal>.py` (reaproveite `art.py`, `scenes/common.py` e as cenas existentes). Quadro 0 já em movimento e com a imagem mais forte; troca de cena a cada 5–8 s; nada que incentive maltratar animal.
6. Revise com `--sheet` (abra a imagem e confira legenda, HUD, sobreposições, loop final = quadro inicial). Corrija e repita até ficar limpo. Depois renderize.
7. Rode o checklist da seção 12. Se algum item falhar, corrija antes de seguir.
8. Renomeie `publish.draft.json` para `publish.json` com `channel_id` do Canal 5 e `publish_at` (A: hoje 12:00-03:00, B: hoje 19:00-03:00), `if_late: public_now`.
9. Atualize `canal5/controle.md` (linha de cada vídeo + fontes). Leia `server-data/metrics/` e preencha as métricas de 48 h dos vídeos antigos.
10. Commit só de `canal5/` e push na `main`.

Domingo: além dos Shorts, monte o longo semanal (compilação de 8–12 min com narração-ponte nova e abertura nova).
