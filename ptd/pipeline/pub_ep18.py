# Gera o publish.json do EP18 (segunda 23/11/2026: ranking #20 12:00, longo 18:00 e Short do episódio 19:00).
# O ranking aponta para o EP17 (golpe do Pix, já publicado), porque às 12:00 o EP18 ainda não está no ar.
# Uso: python3 pub_ep18.py out/ep18/durs.json ep18/publish.json "<created_at>" [só-ranking]
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Saldo bloqueado, sem FGC"), (5, "Cômodo 1: a fachada (o que é uma instituição de pagamento)"),
        (10, "Cômodo 2: o caixa (como ganham dinheiro)"), (15, "Cômodo 3: o cofre (onde fica o seu saldo)"),
        (20, "Cômodo 4: a porta dos fundos (contas-bolsão e laranjas)"), (25, "Cômodo 5: o fiscal (o cerco do BC e da Receita)"),
        (30, "Três perguntas sobre a sua conta"), (31, "A vistoria completa"), (34, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Os bancos que ninguém conhece: quem guarda o seu dinheiro no app (e por que o BC fechou o cerco)"
desc = f"""Uma vistoria, cômodo por cômodo, nas instituições de pagamento: as empresas que guardam e movimentam o dinheiro de milhões de brasileiros sem serem bancos. O que elas são, como ganham dinheiro, onde fica o seu saldo (e por que ele não tem FGC), como algumas viraram "bancos paralelos" para dinheiro sujo e contas laranja, e o que o Banco Central e a Receita mudaram depois disso.

Capítulos
{chap}

Fontes
- Lei 12.865/2013 (arranjos e instituições de pagamento; artigo 12: recursos em conta de pagamento são patrimônio separado e não entram na falência ou liquidação da instituição)
- Banco Central: regras para aplicação do saldo de contas de pagamento (em espécie no BC ou em títulos públicos federais) e modalidades de instituição de pagamento
- Will Bank: liquidação extrajudicial decretada pelo Banco Central em 21/01/2026; saldo em conta de pagamento sem cobertura do FGC e devolução a cargo do liquidante (Jornal de Brasília, Diario de Pernambuco, InfoMoney, janeiro de 2026)
- FGC: garantia de até R$ 250 mil por pessoa por instituição para depósitos e investimentos cobertos
- Finsiders Brasil (2026): instituições de pagamento autorizadas pelo BC passam de 200
- Resolução BCB 246/2022: teto da tarifa de intercâmbio de 0,7% no pré-pago e 0,5% no débito desde 01/04/2023; antes, o pré-pago praticava de 1,1% a 1,5% em média; no Nubank, o intercâmbio do pré-pago foi 7% da receita entre julho de 2021 e junho de 2022 (InfoMoney, 2022)
- Operação Carbono Oculto (agosto de 2025, Receita Federal, PF e MPSP): uma única instituição de pagamento movimentou mais de R$ 46 bilhões entre 2020 e 2024; rede de postos movimentou R$ 52 bilhões; fintechs como "bancos paralelos" com contas-bolsão (via InfoMoney, CNN Brasil, BBC)
- Operação Fluxo Oculto (maio de 2026, Receita e MPSP): seis fintechs movimentaram mais de R$ 26 bilhões entre 2022 e 2025 (via Band e Metrópoles)
- Receita Federal, Instrução Normativa RFB 2.278/2025 (fintechs e instituições de pagamento passam a entregar a e-Financeira)
- Ataque à C&M Software (julho de 2025): R$ 541 milhões desviados da conta de reserva de uma instituição de pagamento, segundo a Polícia Civil de São Paulo (via CNN Brasil)
- Resolução BCB 494/2025 (autorização prévia; prazo para pedir licença antecipado de dezembro de 2029 para maio de 2026) e Resoluções BCB 496 e 497/2025 (limite de R$ 15 mil por Pix ou TED para instituições não autorizadas), via Agência Brasil e CartaCapital
- Resolução Conjunta 14 e Resolução BCB 517 (novembro de 2025): capital mínimo de instituições de pagamento de R$ 1 milhão a R$ 9 milhões para R$ 9,2 milhões a R$ 32,8 milhões, com transição de julho de 2026 a 2028 (via InfoMoney, SBT News, Bloomberg Línea)
- Exemplo da compra de R$ 100 no cartão pré-pago = EXEMPLO ILUSTRATIVO.

Os casos citados foram descritos com base em investigações e reportagens públicas.

Este vídeo é informativo e não é recomendação financeira. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#fintech #instituicaodepagamento #bancocentral #fgc #portrasdodinheiro"""
tags = ["instituição de pagamento", "fintech", "conta de pagamento", "fgc", "banco central", "will bank", "carbono oculto",
        "conta bolsão", "conta laranja", "banco digital", "capital mínimo", "e-financeira", "educacao financeira", "por tras do dinheiro"]
SH_TITLE = "Seu app quebrou. O FGC paga? Nem sempre #shorts"
RK_TITLE = "As 5 plataformas por onde mais chega golpe no Brasil (o nº 1 está em 64%) #shorts"
EP17 = "Golpe do Pix: para onde vai o seu dinheiro em segundos (e quem tem que devolver)"
items = [
  {"key": "ptd-rank20-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "As plataformas digitais mais citadas por quem recebeu tentativas de golpe no Brasil: 5) Google, 13%; 4) Facebook, 17%; 3) Instagram, 22%; 2) Gmail, 32%; 1) WhatsApp, 64%. Uma pessoa pode citar mais de uma plataforma, por isso a soma passa de 100%. 81% dos adultos tiveram contato com algum golpe em 12 meses. \"O dobro do 2º lugar\" = cálculo do canal. Fonte: Global Anti-Scam Alliance (GASA) e Opinium, O Estado dos Golpes no Brasil 2026 (1.170 adultos, março e abril de 2026), via imprensa. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #golpes #whatsapp #seguranca",
   "tags": ["golpes", "golpe whatsapp", "golpe digital", "fraude", "segurança digital", "gasa", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-23T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep17-long",
   "pinned_comment": "Por qual desses golpes você mais recebe tentativa? Vídeo completo: " + EP17},
  {"key": "ptd-ep18-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-23T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Você sabia que o seu saldo no app pode não ter FGC? Na sua opinião, o Banco Central demorou para apertar as regras das fintechs? Conta aqui."},
  {"key": "ptd-ep18-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "Quando o Will Bank foi liquidado pelo Banco Central, em 21/01/2026, o saldo de quem tinha conta de pagamento ficou bloqueado, sem cobertura do FGC e com devolução a cargo do liquidante (imprensa, jan/2026; Lei 12.865/2013). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #fintech #fgc #bancocentral",
   "tags": ["fgc", "conta de pagamento", "fintech", "will bank", "banco central", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-23T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep18-long",
   "pinned_comment": "Você sabe se a sua conta no app é de banco ou de instituição de pagamento? Vídeo completo: " + LONG_TITLE},
]
if len(sys.argv) > 4: items = items[:1]
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": items}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s", len(desc), len(LONG_TITLE))
