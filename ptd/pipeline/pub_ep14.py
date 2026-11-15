# Gera o publish.json do EP14 (longo 18:00 e Short do episódio 19:00 em 15/11; ranking #12 12:00 em 16/11,
# porque o horário de 12:00 de 15/11 já estava com o ranking #11)
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "O paradoxo: a Selic caiu, o juro subiu"), (4, "O que é spread"), (7, "Camada 1: o custo do dinheiro"),
        (10, "Camada 2: o calote"), (14, "Camada 3: a operação do banco"), (17, "Camada 4: impostos e FGC"),
        (19, "Camada 5: a margem do banco"), (23, "O Brasil no mundo"), (25, "Por que a Selic cai e o juro não"),
        (28, "O que já foi tentado"), (30, "A cebola inteira"), (33, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Spread bancário: por que o juro no Brasil não cai quando a Selic cai"
desc = f"""Em 2026, o Banco Central cortou a Selic cinco vezes, de 15% para 13,75% ao ano. Mesmo assim, o juro médio do crédito livre subiu de 48,3% para 49,0% ao ano. Por quê? Neste episódio, o juro que você paga é descascado como uma cebola, camada por camada: o custo do dinheiro, o calote, a operação do banco, os impostos e, no miolo, a margem. E a gente confere qual camada é a maior (spoiler: não é o lucro).

Capítulos
{chap}

Fontes
- Banco Central, Estatísticas monetárias e de crédito de março de 2026 (27/04/2026) e de setembro de 2026 (29/10/2026), via imprensa e Reuters: juro médio do crédito livre de 48,3% (mar) e 49,0% ao ano (set); pessoas físicas 61,5% (mar) e 62,4% (set); spread médio do crédito livre de 34,6 p.p. (mar) e 35,5 p.p. (set); inadimplência acima de 90 dias no crédito livre das famílias de 8,1% em setembro (recorde da série); estoque de crédito de R$ 7,4 trilhões
- Banco Central, Relatório de Estabilidade Financeira de maio de 2026 (decomposição do custo do crédito de 2025), via imprensa: ICC médio de 20,93% ao ano em 2025; custo de captação perto de 40% do ICC; composição do spread: inadimplência 36,61%, despesas administrativas 22,90%, tributos e FGC 20,52%, margem financeira 19,97%
- Copom: Selic em 15% de junho de 2025 ao início de 2026; cinco cortes até 13,75% (setembro de 2026); mantida em 13,75% em 04/11/2026
- Banco Mundial, indicador de spread de juros (taxa de empréstimo menos taxa de depósito), 2024, via Helgi Library e Cbonds: Brasil com 32,5 pontos, Quirguistão com 18,1 (metodologia diferente da do Banco Central)
- Lei Complementar 166/2019 (cadastro positivo automático); Banco Central (Pix, 2020; open finance, 2021); Lei 14.690/2023 (limite dos juros do rotativo do cartão, em vigor desde 2024)
- Cálculos do canal: exemplo dos R$ 100 de juros (fatias do spread multiplicadas pela parte do spread no custo médio do crédito; média de toda a carteira, não de um empréstimo específico) e variações em pontos.

Este vídeo é informativo e não é recomendação financeira nem de investimento. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#spread #juros #selic #bancos #portrasdodinheiro"""
tags = ["spread bancario", "spread", "juros", "selic", "por que o juro é alto", "juros no brasil", "banco central", "taxa de juros",
        "inadimplencia", "credito", "bancos", "custo do credito", "educacao financeira", "economia", "por tras do dinheiro"]
SH_TITLE = "A Selic caiu 5 vezes. O seu juro subiu. Por quê? #shorts"
RK_TITLE = "5 fatias de cada R$ 100 de juros no Brasil (o lucro do banco é a menor) #shorts"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-ep14-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-15T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Antes de ver o vídeo, qual camada você apostava que era a maior: o lucro do banco, o calote ou os impostos? Conta aqui."},
  {"key": "ptd-ep14-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "Em 2026, a Selic caiu de 15% para 13,75%. Mas o juro médio do crédito livre subiu de 48,3% para 49,0% ao ano, e o spread passou de 34,6 para 35,5 pontos. O motivo principal: o calote em alta. Fontes: Copom; Banco Central (março e setembro de 2026). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #juros #selic #spread",
   "tags": ["spread bancario", "juros", "selic", "banco central", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-15T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep14-long",
   "pinned_comment": "O juro do seu cartão ou empréstimo caiu este ano? Vídeo completo: " + LONG_TITLE},
  {"key": "ptd-rank12-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Para onde vão R$ 100 de juros no Brasil, na média de 2025: 5) margem do banco, cerca de R$ 12,00; 4) impostos e FGC, R$ 12,40; 3) custo de operar, R$ 13,80; 2) calote, R$ 22,00; 1) custo do dinheiro (captação), R$ 39,80. Fonte: Banco Central, Relatório de Estabilidade Financeira de maio de 2026 (dados de 2025), via imprensa; valores em reais = cálculo do canal, média de toda a carteira. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #juros #spread #bancos #financas",
   "tags": ["juros", "spread bancario", "bancos", "lucro dos bancos", "selic", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-16T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep14-long",
   "pinned_comment": "Você imaginava que o lucro do banco era a menor fatia? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
