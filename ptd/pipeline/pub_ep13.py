# Gera o publish.json do EP13 (longo 18:00 e Short do episódio 19:00 em 14/11; ranking #11 12:00 em 15/11,
# porque o horário de 12:00 de 14/11 já estava com o ranking #10)
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Gancho: o Nubank virou banco"), (4, "1º andar: a porta — o cartão sem anuidade"),
        (8, "2º andar: o cofre — depósitos a 87% do CDI"), (12, "3º andar: a máquina — o cartão de crédito"),
        (16, "4º andar: o empréstimo — margem de 22,5%"), (19, "Tarifa ou juros? A resposta"),
        (21, "5º andar: México e Colômbia"), (24, "As rachaduras: a inadimplência"),
        (28, "A placa na porta: a licença de banco"), (32, "O prédio inteiro"), (35, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "O Nubank virou banco: de onde vem o lucro recorde (e o número que preocupa)"
desc = f"""Nesta semana, o Nubank divulgou o maior lucro da sua história (US$ 1,09 bilhão em um trimestre) e recebeu do Banco Central o aval para comprar um banco e ter a licença oficial de banco no Brasil. Mas se a empresa nasceu prometendo acabar com tarifa, de onde vem esse dinheiro? Neste episódio, o Nubank é visto como um prédio de 5 andares: a porta, o cofre, a máquina, o empréstimo e a cobertura. E depois a gente desce até a fundação para procurar as rachaduras.

Capítulos
{chap}

Fontes
- Nu Holdings, resultados do 3º trimestre de 2026 (12/11/2026), via Business Moment, Investing.com, EuQueroInvestir, Visno Invest, MarketScreener e Yahoo Finance: lucro líquido de US$ 1,09 bi; 143 milhões de clientes (cerca de 120 mi no Brasil, 16,6 mi no México, 6,1 mi na Colômbia); taxa de atividade no Brasil de 86,3%; receita de cerca de US$ 6,3 bi; tarifas e comissões de US$ 817 mi; carteira de crédito de US$ 41,6 bi (cartão US$ 27,2 bi, pessoal sem garantia US$ 11 bi, com garantia US$ 3,4 bi); crescimento em 1 ano (câmbio constante): cartão 32%, pessoal 39%, com garantia 23%; depósitos de US$ 47,5 bi (Brasil US$ 38,6 bi, México US$ 5,3 bi, Colômbia US$ 3,5 bi) a um custo de 87% do CDI; margem financeira (NIM) de 22,5% e ajustada ao risco de 12,1% (12,4% no 2T26); atraso acima de 90 dias de 7,3% (6,9% no 2T26) e de 15 a 90 dias de 4,9%; 870 mil novos clientes no México no 1º trimestre como banco
- Banco Central (13/11/2026), via Reuters/TradingView, O Tempo e Seu Dinheiro: aprovação da compra do Banco Porto Real de Investimentos pelo Nubank (licença bancária)
- Nu Holdings, 6-K de 20/07/2026: acordo para comprar 100% do Banco Porto Real; Resolução Conjunta nº 17 (BC/CMN) sobre o uso de "banco" no nome; licença sem exigência adicional de capital
- Banco Porto Real: fundado em 1992, R$ 32,1 mi em ativos em março de 2026 (via imprensa, 13/11/2026)
- BTG Pactual com dados da Card Monitor (2T26): grandes bancos tradicionais perdem fatia no cartão de crédito
- IBGE, estimativa da população de 2025 (cerca de 213 milhões)
- Copom (04/11/2026): Selic em 13,75% ao ano
- Cálculos do canal: lucro por dia (cerca de US$ 12 mi), fatia de tarifas na receita (cerca de 13%) e percentuais da carteira. O exemplo dos R$ 1.000 é ilustrativo.

Este vídeo é informativo e não é recomendação financeira nem de investimento. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#nubank #bancos #fintech #financas #portrasdodinheiro"""
tags = ["nubank", "nubank virou banco", "licença bancaria", "nubank lucro", "nu holdings", "balanço nubank", "banco digital", "fintech",
        "cartão de credito", "spread bancario", "inadimplencia", "bancos", "banco central", "educacao financeira", "por tras do dinheiro"]
SH_TITLE = "Nubank lucrou US$ 1 bilhão sem cobrar tarifa. De onde veio? #shorts"
RK_TITLE = "Os 5 bancos com mais clientes no Brasil (o nº 2 não tem agência) #shorts"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-ep13-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-14T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Para você, o Nubank virar banco oficialmente muda alguma coisa, ou é só uma placa nova na porta? Conta aqui."},
  {"key": "ptd-ep13-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "O Nubank lucrou US$ 1,09 bilhão no 3º trimestre de 2026, recorde. Mas tarifas e comissões foram só US$ 817 milhões de uma receita de cerca de US$ 6,3 bilhões (cerca de 13%, cálculo do canal). O resto vem de juros. Fonte: Nu Holdings, resultados do 3T26 (12/11/2026). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #nubank #bancos #juros",
   "tags": ["nubank", "lucro nubank", "juros", "banco digital", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-14T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep13-long",
   "pinned_comment": "Você paga a fatura inteira ou já parcelou alguma vez? Vídeo completo: " + LONG_TITLE},
  {"key": "ptd-rank11-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Os 5 bancos com mais clientes no Brasil, pelos dados do Banco Central de dezembro de 2025: 5) Banco do Brasil, 81,9 milhões; 4) Itaú, 100,3 milhões; 3) Bradesco, 110,5 milhões; 2) Nubank, 112,0 milhões; 1) Caixa, 158,1 milhões. Fonte: Banco Central (dez/2025), via Olhar Digital e Finsiders (jan/2026). Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #bancos #nubank #caixa #financas",
   "tags": ["bancos", "maiores bancos do brasil", "nubank", "caixa", "bradesco", "itau", "banco do brasil", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-15T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep13-long",
   "pinned_comment": "Qual desses bancos é o seu principal hoje? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
