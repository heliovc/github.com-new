# Ranking PTD #11 — os 5 bancos com mais clientes no Brasil (todas as instituições, não só fintechs), dados do Banco Central
# de dez/2025 divulgados em jan/2026. Diferente do rank #4 (só fintechs) e do rank #7 (bancos por ativos).
# Liga com o EP13 (o Nubank virou banco). Variação visual: tema NOVO roxo/menta + gráfico NOVO "crowd" (bonequinhos, 1 = 10 milhões).
TITLE = "Os 5 bancos com mais clientes no Brasil (o nº 2 não tem agência) #shorts"
THEME = {"accent": (178, 120, 255), "accent2": (120, 230, 190), "bar_col": (60, 36, 96), "hl_col": (178, 120, 255),
         "glow": (36, 20, 60), "bar": "OS BANCOS COM MAIS CLIENTES", "chart": "crowd", "per_icon": 10.0}
HOOK = {"say": "Os cinco bancos com mais clientes no Brasil. E o número dois não tem uma única agência.",
        "top": "Bancos com mais clientes", "sub": "no Brasil · Banco Central, dez/2025", "tease": "1 boneco = 10 milhões"}
SRC = "Banco Central (dez/2025), via Olhar Digital e Finsiders"
ITEMS = [
 {"rank": 5, "name": "Banco do Brasil", "short": "BB", "tag": "banco público federal", "num": 81.9, "suffix": " mi", "dec": 1,
  "unit": "de clientes no Brasil", "source": SRC,
  "say": "Número cinco: o Banco do Brasil, com oitenta e um vírgula nove milhões de clientes."},
 {"rank": 4, "name": "Itaú Unibanco", "short": "Itaú", "tag": "o maior banco privado em ativos", "num": 100.3, "suffix": " mi", "dec": 1,
  "unit": "de clientes no Brasil", "source": SRC,
  "say": "Número quatro: o Itaú, o maior banco privado do país em tamanho. Cem vírgula três milhões de clientes."},
 {"rank": 3, "name": "Bradesco", "short": "Bradesco", "tag": "perdeu o 2º lugar em 2025", "num": 110.5, "suffix": " mi", "dec": 1,
  "unit": "de clientes no Brasil", "source": SRC,
  "say": "Número três: o Bradesco, cento e dez vírgula cinco milhões. Ele era o segundo, até ser ultrapassado."},
 {"rank": 2, "name": "Nubank", "short": "Nubank", "tag": "nenhuma agência", "num": 112.0, "suffix": " mi", "dec": 1,
  "unit": "de clientes no Brasil", "source": SRC,
  "say": "Número dois: o Nubank, cento e doze milhões, só pelo celular. E nesta semana ele ganhou a licença oficial de banco."},
 {"rank": 1, "name": "Caixa", "short": "Caixa", "tag": "paga os benefícios sociais", "num": 158.1, "suffix": " mi", "dec": 1,
  "unit": "de clientes no Brasil", "source": SRC,
  "say": "E o número um: a Caixa, com cento e cinquenta e oito milhões de clientes, puxada pelo pagamento de benefícios sociais."},
]
OUTRO = {"say": "Mas cliente não é lucro. A gente explicou de onde vem o dinheiro do Nubank no episódio completo. Segue o Por Trás do Dinheiro.",
         "note": "Clientes por instituição · não é recomendação financeira"}
