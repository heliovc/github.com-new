# Gera o publish.json do EP15 (ranking #13 12:00, longo 18:00 e Short do episódio 19:00 em 16/11/2026).
# O ranking aponta para o EP14 (spread/calote, já publicado), porque às 12:00 o EP15 ainda não está no ar.
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Dois vizinhos, o mesmo empréstimo"), (4, "Quem aplica a prova: os birôs"), (7, "De onde veio o score"),
        (10, "A prova: as 6 questões"), (17, "A prova inteira"), (18, "Quanto isso vale em juro"),
        (20, "O boletim do Brasil"), (23, "O círculo vicioso"), (26, "O que a lei garante"),
        (28, "A prova corrigida"), (31, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Score de crédito: a prova secreta que decide quanto juro você paga"
desc = f"""Dois vizinhos, mesmo salário, mesmo empréstimo de R$ 10 mil em 24 meses. Um paga R$ 15.741; o outro, R$ 20.925 (exemplo ilustrativo). O que separa os dois é o score de crédito. Neste episódio, o score é aberto como uma prova de seis questões: quem aplica (Serasa, Boa Vista, Quod e SPC), de onde veio, quanto pesa cada questão, o boletim do Brasil, o círculo vicioso do juro e o que a lei garante para você.

Capítulos
{chap}

Fontes
- Serasa, perguntas frequentes do Serasa Score 2.0: escala de 0 a 1.000; faixas baixo (0-300), regular (301-500), bom (501-700) e excelente (701-1.000); pesos: hábitos de pagamento do Cadastro Positivo 29%, experiência com o mercado de crédito 24%, dívidas negativadas 21%, busca por crédito 12%, informações cadastrais 8%, contratos de crédito 6%; a consulta do próprio score não afeta a nota
- Serasa, Mapa Score do Brasil, via release e imprensa (agosto de 2026): média nacional de 548 (abril de 2025) e 542 pontos (abril de 2026); 500 pontos entre 18 e 25 anos e 603 acima de 65 anos
- Serasa, Mapa da Inadimplência e Renegociação de Dívidas, divulgado em 02/11/2026, via imprensa: 84,2 milhões de inadimplentes em setembro de 2026 (recorde) e R$ 597,4 bilhões em dívidas
- Banco Central, "Análise dos efeitos do Cadastro Positivo" (2021): no crédito pessoal não consignado, diferença de 31 pontos percentuais na taxa anual para tomadores com pontuação no cadastro (amostra com taxa média de 299% ao ano)
- Equifax, relatório anual (10-K) de 2023: compra da Boa Vista Serviços concluída em 07/08/2023, cerca de US$ 510 milhões em dinheiro mais ações
- Quod (Gestora de Inteligência de Crédito), constituída em 2017 por Banco do Brasil, Bradesco, Caixa, Itaú Unibanco e Santander
- FICO: fundada em 1956 por Bill Fair e Earl Isaac; score FICO de uso geral lançado em 1989
- Lei 12.414/2011 (Cadastro Positivo); Lei Complementar 166/2019 (inclusão automática); STJ, Súmula 550 (2015) e Súmula 548; Lei 13.709/2018 (LGPD), art. 20
- Cálculos do canal: exemplo dos vizinhos (EXEMPLO ILUSTRATIVO; R$ 10 mil em 24 parcelas fixas a 4% e a 7% ao mês) e somas dos pesos.

Este vídeo é informativo e não é recomendação financeira nem de investimento. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#score #serasa #credito #juros #portrasdodinheiro"""
tags = ["score de credito", "score", "serasa score", "cadastro positivo", "como funciona o score", "aumentar score", "birô de crédito",
        "boa vista", "quod", "spc", "juros", "nome sujo", "inadimplencia", "educacao financeira", "por tras do dinheiro"]
SH_TITLE = "Mesmo salário, mesmo empréstimo. Um pagou R$ 5 mil a mais #shorts"
RK_TITLE = "5 coisas que mais pesam no seu score (o nº 1 não é ter dívida) #shorts"
EP14 = "Spread bancário: por que o juro no Brasil não cai quando a Selic cai"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-rank13-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Os pesos do Serasa Score 2.0, divulgados pela própria Serasa: 5) dados cadastrais, 8%; 4) busca por crédito, 12%; 3) dívidas negativadas, 21%; 2) tempo de mercado, 24%; 1) pagar em dia (Cadastro Positivo), 29%. Fica de fora: contratos de crédito, 6%. Cada birô tem o seu próprio modelo. Fonte: Serasa, perguntas frequentes do Serasa Score 2.0. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #score #serasa #credito",
   "tags": ["score de credito", "serasa score", "cadastro positivo", "credito", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-16T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep14-long",
   "pinned_comment": "Você achava que ter dívida era o que mais pesava no score? Vídeo completo: " + EP14},
  {"key": "ptd-ep15-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-16T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Na sua opinião, é justo um algoritmo decidir quanto juro você paga, sem você ver a fórmula? Conta aqui."},
  {"key": "ptd-ep15-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "Dois vizinhos, mesmo salário, mesmo empréstimo de R$ 10 mil em 24 meses: a 4% ao mês, um paga R$ 15.741; a 7%, o outro paga R$ 20.925 (exemplo ilustrativo, cálculo do canal). O que muda é o score. E a questão que mais pesa na nota é pagar em dia (29%, segundo a Serasa). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #score #juros #credito",
   "tags": ["score de credito", "score", "juros", "serasa", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-16T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep15-long",
   "pinned_comment": "Você sabe qual é o seu score hoje? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
