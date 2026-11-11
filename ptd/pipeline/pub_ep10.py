# Gera o publish.json do EP10 (longo 18:00 e Short do episódio 19:00 em 11/11; ranking #8 12:00 em 12/11,
# porque o horário de 12:00 de 11/11 já estava com o ranking #7)
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Gancho: R$ 1.000 que viram R$ 5.517"), (4, "Fase 1: os autos — o que é o rotativo"), (7, "A regra de 2017: a ponte de 30 dias"),
        (9, "Fase 2: a acusação — 451,7% ao ano"), (11, "A curva do rotativo desde 2016"), (12, "84,2 milhões de inadimplentes"),
        (14, "Fase 3: a defesa — o calote"), (17, "O parcelado sem juros e a briga de 2023"), (20, "Fase 4: as provas — 2017"),
        (23, "O teto de 100% da dívida"), (25, "Por que 451% não fura o teto"), (26, "Portabilidade e as regras de hoje"),
        (27, "Fase 5: o veredito — quem ganha"), (31, "A sentença"), (33, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Rotativo do cartão: o juro de 451% ao ano (e quem ganha com ele)"
desc = f"""Em setembro de 2026, o juro médio do rotativo do cartão de crédito chegou a 451,7% ao ano, segundo o Banco Central. Mas existe uma lei que limita os juros a 100% da dívida. Como as duas coisas convivem? Neste episódio, o rotativo vai a julgamento: os autos (o que é), a acusação (os números), a defesa (o calote e o parcelado sem juros), as provas (o que aconteceu em 2017 e com o teto de 2024) e o veredito: quem ganha e quem paga.

Capítulos
{chap}

Fontes
- Banco Central, via O Povo (29/10/2026): juro médio do rotativo de 451,7% ao ano em set/2026 (444,9% em ago/2026)
- Banco Central, via Rankia (out/2026): parcelamento da fatura a 192,1% ao ano e 66,15% do saldo do rotativo com mais de 90 dias de atraso em ago/2026, recorde da série iniciada em 2011
- Banco Central, via Monitor Mercantil: recorde de 484,6% ao ano em dez/2016
- Folha de S.Paulo, via JB (mai/2017): 233,9% ao ano na 3ª semana de abril de 2017, após a Resolução CMN 4.549/2017 (em vigor desde 03/04/2017)
- Banco Central, via Meu Tudo (ago/2024): 432,3% ao ano em jul/2024
- Voto CMN 67/2023: aumento gradual das taxas após os resultados iniciais da regra de 2017
- Serasa, Mapa da Inadimplência, via Mercado & Consumo (nov/2026): 84,2 milhões de inadimplentes em set/2026; bancos e cartões com 27,16% das dívidas
- Banco Central, via Times Brasil: 74,6% do saldo da carteira de cartões sem juros (mai/2026)
- A Gazeta, InfoMoney, Brazil Journal e Correio Braziliense (2023): debate sobre o parcelado sem juros, proposta de limite de 12 parcelas e declaração de Fernando Haddad
- Lei 14.690/2023 (Desenrola) e Resolução CMN 5.112/2023, via Migalhas e Mattos Filho: teto de 100% da dívida original para juros e encargos do rotativo e do parcelamento da fatura desde 03/01/2024; portabilidade do saldo
- A conversão de 451,7% ao ano para ~15,3% ao mês e os exemplos com fatura de R$ 1.000 são cálculos ilustrativos do canal (sem IOF, multa e outros encargos).

Este vídeo é informativo e não é recomendação financeira. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#cartaodecredito #rotativo #juros #financas #portrasdodinheiro"""
tags = ["rotativo do cartao", "juros do cartao de credito", "cartao de credito", "rotativo", "teto de juros", "desenrola", "banco central",
        "parcelado sem juros", "inadimplencia", "serasa", "fatura do cartao", "juros", "dividas", "economia", "financas", "por tras do dinheiro"]
SH_TITLE = "Por que o rotativo cobra 451% se a lei limita a 100%? #shorts"
RK_TITLE = "Os 5 maiores recordes do Pix em um dia (o nº 1 foi semana passada) #shorts"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-ep10-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-11T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Na sua opinião, quem deveria pagar a conta do parcelado sem juros: quem usa o rotativo, o lojista ou ninguém? Conta aqui."},
  {"key": "ptd-ep10-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "O juro médio do rotativo chegou a 451,7% ao ano em set/2026, mas desde 2024 juros e encargos não podem passar de 100% da dívida original. A diferença: um é a taxa anualizada, o outro limita o total. Fontes: Banco Central; Lei 14.690/2023 e Resolução CMN 5.112/2023. Exemplo de R$ 1.000 ilustrativo. Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #cartaodecredito #rotativo #juros",
   "tags": ["rotativo", "cartao de credito", "juros", "teto de juros", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-11T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep10-long",
   "pinned_comment": "Você sabia que o teto limita o total e não a taxa? Vídeo completo: " + LONG_TITLE},
  {"key": "ptd-rank08-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Os 5 últimos recordes do Pix em um único dia: 5) set/2025, 290 milhões; 4) Black Friday 2025, 297,4 milhões; 3) 05/12/2025, 313,3 milhões; 2) 04/09/2026, 318,1 milhões; 1) 06/11/2026, 319,7 milhões (R$ 180,5 bilhões). Fontes: Banco Central, via Times Brasil, Jovem Pan, IstoÉ Dinheiro, Agência Brasil e SBT News. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #pix #bancocentral #financas",
   "tags": ["pix", "recorde do pix", "banco central", "pagamentos", "transferencias", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-12T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep10-long",
   "pinned_comment": "Hoje você paga mais com Pix ou com cartão? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
