# Ranking PTD #3 — 5 jeitos de pegar dinheiro emprestado, do mais barato ao mais caro (juros médios, pessoa física, set/2026)
# Variação visual: tema roxo/ciano + gráfico NOVO "gauge" (termômetro com escala 0–500% e pinos por item).
TITLE = "5 jeitos de pegar dinheiro emprestado (o nº 1 cobra 451% ao ano)"
THEME = {"accent": (168, 120, 255), "accent2": (80, 210, 230), "bar_col": (90, 80, 130), "hl_col": (168, 120, 255),
         "glow": (40, 26, 70), "bar": "QUANTO CUSTA PEGAR DINHEIRO EMPRESTADO", "chart": "gauge",
         "gauge_max": 500, "gauge_step": 100, "gauge_unit": "%", "cold": (80, 210, 230), "hot": (240, 80, 90)}
HOOK = {"say": "Cinco jeitos de pegar dinheiro emprestado no Brasil, do mais barato ao mais caro. O número um cobra mais de quatrocentos e cinquenta por cento ao ano.",
        "top": "Jeitos de pegar dinheiro emprestado", "sub": "juros médios ao ano · setembro de 2026", "tease": "o nº 1: 451% ao ano"}
SRC = "Banco Central, set/2026 (via O Povo)"
ITEMS = [
 {"rank": 5, "name": "Consignado", "short": "Consignado", "tag": "parcela descontada do salário", "num": 28.5, "suffix": "%", "dec": 1,
  "unit": "ao ano, em média", "source": SRC,
  "say": "Número cinco: o consignado, com a parcela descontada direto do salário ou da aposentadoria. Vinte e oito vírgula cinco por cento ao ano. O mais barato da lista."},
 {"rank": 4, "name": "Crédito pessoal", "short": "Pessoal", "tag": "sem desconto em folha", "num": 110.9, "suffix": "%", "dec": 1,
  "unit": "ao ano, em média", "source": SRC,
  "say": "Número quatro: o crédito pessoal sem consignação. Sem a garantia do salário, o juro quase quadruplica: cento e dez vírgula nove por cento ao ano."},
 {"rank": 3, "name": "Cheque especial", "short": "Cheque esp.", "tag": "o limite da conta", "num": 139.0, "suffix": "%", "dec": 1,
  "unit": "ao ano, em média", "source": SRC,
  "say": "Número três: o cheque especial, aquele limite que aparece na conta. Cento e trinta e nove por cento ao ano, mesmo com o teto criado pelo Banco Central."},
 {"rank": 2, "name": "Parcelado da fatura", "short": "Parcelado", "tag": "parcelar o que não pagou", "num": 193.0, "suffix": "%", "dec": 1,
  "unit": "ao ano, em média", "source": SRC,
  "say": "Número dois: parcelar a fatura do cartão que você não conseguiu pagar. Cento e noventa e três por cento ao ano."},
 {"rank": 1, "name": "Rotativo do cartão", "short": "Rotativo", "tag": "pagar só uma parte da fatura", "num": 451.7, "suffix": "%", "dec": 1,
  "unit": "ao ano, em média", "source": SRC,
  "say": "E o número um: o rotativo do cartão, quando você paga só uma parte da fatura. Quatrocentos e cinquenta e um vírgula sete por cento ao ano. Quase dezesseis vezes o consignado."},
]
OUTRO = {"say": "Um alívio: desde dois mil e vinte e quatro, os juros e encargos do rotativo não podem passar do valor da dívida original. Quer entender por que esses juros são tão altos? Segue o Por Trás do Dinheiro.",
         "note": "Juros médios para pessoa física. Não é recomendação financeira."}
