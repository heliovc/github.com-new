# Gera o publish.json do EP09 (longo 18:00 e Short do episódio 19:00 em 10/11; ranking #7 12:00 em 11/11,
# porque o horário de 12:00 de 10/11 já estava com o ranking #6)
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Gancho: preso antes da decolagem"), (4, "Trecho 1: a decolagem (de R$ 3,7 bi a R$ 82 bi)"), (7, "O combustível: CDB a até 140% do CDI"),
        (12, "Trecho 2: os alarmes"), (16, "Risco moral: a garantia vira motor"), (18, "Trecho 3: o pouso forçado no BRB"),
        (21, "R$ 12,2 bi em carteiras suspeitas"), (22, "Trecho 4: a queda"), (26, "O paraquedas: como o FGC funciona"),
        (29, "Quem paga a conta"), (31, "As regras mudaram"), (32, "O laudo: 15 indiciados"), (34, "O que a caixa-preta ensina"), (36, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Banco Master: o banco que pagava demais (e quem pagou a conta de R$ 40 bilhões)"
desc = f"""Em 18 de novembro de 2025 o Banco Central liquidou o Banco Master, horas depois de o dono ser preso em Guarulhos. O Fundo Garantidor de Créditos estimou cerca de R$ 40,6 bilhões para devolver aos investidores — o maior acionamento da sua história. Neste episódio abrimos a caixa-preta: a decolagem (de R$ 3,7 bi para R$ 82 bi em ativos, com CDB a até 140% do CDI), os alarmes que tocaram antes, o pouso forçado no BRB, a queda — e quem está pagando o paraquedas.

Capítulos
{chap}

Fontes
- Polícia Federal e Banco Central (17-18/11/2025), via Diário de Pernambuco, InfoMoney e Itatiaia: prisão em Guarulhos, Operação Compliance Zero e liquidação extrajudicial
- FGC (nov/2025), via NeoFeed e InfoMoney: estimativa líquida de ~R$ 40,6 bi e base estimada de ~1,6 milhão de credores
- Dados do Banco Central compilados por Revista Oeste e TMC (2025): ativos de R$ 3,7 bi (2019) para R$ 82 bi (2024); da 90ª para a 23ª posição
- Nord Investimentos e Seu Dinheiro (2025): CDBs a até 140% do CDI; faixa de ~110% a 120% em bancos parecidos
- Times Brasil e Band (2025-2026): ativos de difícil liquidez (precatórios, participações, créditos); nota técnica do BC sobre o modelo de negócios (nov/2024); relatório da Warren (ago/2023)
- Correio Braziliense (abr/2026): relatório da Diretoria de Fiscalização do BC — problemas no radar desde 2022 e 31 ofícios
- InfoMoney, Suno e Mercado & Consumo: anúncio da compra de 58% do Master pelo BRB (28/03/2025, ~R$ 2 bi) e veto do BC (03/09/2025)
- PF e MPF, via Correio Braziliense: R$ 12,2 bi em carteiras de crédito supostamente inexistentes vendidas ao BRB (as defesas negam)
- BP Money e Agência Brasil: soltura com tornozeleira (nov/2025) e nova prisão (mar/2026)
- Agência Brasil (jan/2026): R$ 32,5 bi pagos a 75% dos credores
- CNN Brasil e Diário do Comércio: patrimônio do FGC de R$ 140,4 bi (2024) e R$ 123,2 bi (2025), com provisão de R$ 17,1 bi
- Let's Money: plano de recomposição do FGC (fev/2026) com contribuição extraordinária de 50%
- Resolução do CMN, via InvestNews e Nord Investimentos: contribuição adicional de 0,01% para 0,02% e gatilho de 75% para 60%, desde 01/06/2026; limite de R$ 250 mil mantido
- Agência Brasil (out/2026): PF indicia Daniel Vorcaro e mais 14 pessoas (28/10/2026). Indiciamento não é condenação; as defesas negam os crimes.
- O exemplo com R$ 10 mil e CDI de 15% é ilustrativo. A curva do "voo" é uma ilustração.

Este vídeo é informativo e não é recomendação financeira. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#bancomaster #fgc #cdb #financas #portrasdodinheiro"""
tags = ["banco master", "fgc", "fundo garantidor de creditos", "vorcaro", "daniel vorcaro", "liquidacao banco master", "cdb", "cdb banco master",
        "brb", "compliance zero", "banco central", "risco moral", "precatorios", "renda fixa", "economia", "financas", "por tras do dinheiro"]
SH_TITLE = "Como o Banco Master pagava 140% do CDI (e por que caiu) #shorts"
RK_TITLE = "Os 5 maiores bancos do Brasil (o nº 1 tem mais de R$ 2,6 trilhões) #shorts"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-ep09-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-10T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Você colocaria dinheiro num CDB pagando 140% do CDI só porque tem a garantia do FGC? Conta aqui por quê."},
  {"key": "ptd-ep09-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "CDB a até 140% do CDI, dinheiro preso em ativos difíceis de vender e a garantia do FGC como argumento de venda: como o Banco Master cresceu e caiu. Fontes: Nord Investimentos; Times Brasil; Banco Central (liquidação em 18/11/2025). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #bancomaster #fgc #cdb",
   "tags": ["banco master", "fgc", "cdb", "vorcaro", "risco moral", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-10T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep09-long",
   "pinned_comment": "Taxa alta demais te dá vontade de investir ou te deixa desconfiado? Vídeo completo: " + LONG_TITLE},
  {"key": "ptd-rank07-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Os 5 maiores bancos do Brasil em ativos totais (set/2025): 5) Santander Brasil R$ 1,25 tri; 4) Bradesco R$ 1,79 tri; 3) Caixa R$ 2,21 tri; 2) Banco do Brasil R$ 2,54 tri; 1) Itaú Unibanco R$ 2,65 tri. Fontes: Banco Central (set/2025), via Olhar Digital; balanço do Santander (3º tri/2025), via InfoMoney. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #bancos #itau #bancodobrasil #financas",
   "tags": ["maiores bancos do brasil", "itau", "banco do brasil", "caixa", "bradesco", "santander", "bancos", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-11T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep09-long",
   "pinned_comment": "Em qual desses bancos você tem conta? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
