# Ranking PTD #12 — para onde vão R$ 100 de juros: as 5 fatias do custo médio do crédito no Brasil (2025), da menor para a maior.
# Base: Banco Central, Relatório de Estabilidade Financeira de maio de 2026 (decomposição do ICC e do spread de 2025), via imprensa:
# custo de captação ~39,8% do ICC; spread = o resto (~60,2%), dividido em inadimplência 36,61%, despesas administrativas 22,90%,
# tributos e FGC 20,52% e margem financeira 19,97%. Valores em R$ = CÁLCULO do canal (fatia do spread x 60,2%), arredondados.
# Liga com o EP14 (spread bancário). Variação visual: tema NOVO verde-limão/laranja + gráfico NOVO "donut" (rosca de fatias).
TITLE = "5 fatias de cada R$ 100 de juros no Brasil (o lucro do banco é a menor) #shorts"
THEME = {"accent": (190, 230, 70), "accent2": (255, 170, 80), "bar_col": (40, 60, 30), "hl_col": (190, 230, 70),
         "glow": (24, 44, 30), "bar": "PARA ONDE VÃO OS SEUS JUROS", "chart": "donut"}
HOOK = {"say": "A cada cem reais de juros que você paga no Brasil, para onde vai o dinheiro? O Banco Central fez a conta. São cinco fatias. E o lucro do banco é a menor delas.",
        "top": "Para onde vão R$ 100 de juros", "sub": "Banco Central · média de 2025", "tease": "o lucro é o nº 5?"}
SRC = "Banco Central, REF de maio/2026 (dados de 2025) · cálculo do canal"
ITEMS = [
 {"rank": 5, "name": "Margem do banco", "short": "Margem", "tag": "onde mora o lucro", "num": 12.0, "prefix": "R$ ", "suffix": "", "dec": 2,
  "unit": "de cada R$ 100 de juros", "source": SRC, "col": (80, 200, 120),
  "say": "Número cinco: a margem do banco, que é onde mora o lucro. Só uns doze reais de cada cem. Parece pouco, mas sobre uma montanha de crédito."},
 {"rank": 4, "name": "Impostos e FGC", "short": "Governo", "tag": "tributos e o seguro dos depósitos", "num": 12.4, "prefix": "R$ ", "suffix": "", "dec": 2,
  "unit": "de cada R$ 100 de juros", "source": SRC, "col": (160, 110, 240),
  "say": "Número quatro: impostos e o fundo garantidor, o seguro dos depósitos. Doze reais e quarenta. O governo leva um pouco mais que o banco."},
 {"rank": 3, "name": "Custo de operar", "short": "Operação", "tag": "pessoas, agências, sistemas", "num": 13.8, "prefix": "R$ ", "suffix": "", "dec": 2,
  "unit": "de cada R$ 100 de juros", "source": SRC, "col": (90, 140, 240),
  "say": "Número três: o custo de funcionar. Funcionários, agências, sistemas e combate a fraudes. Treze reais e oitenta."},
 {"rank": 2, "name": "O calote", "short": "Calote", "tag": "quem paga em dia paga pelos outros", "num": 22.0, "prefix": "R$ ", "suffix": "", "dec": 2,
  "unit": "de cada R$ 100 de juros", "source": SRC, "col": (235, 100, 85),
  "say": "Número dois: o calote. Vinte e dois reais. É a maior fatia do spread. Ou seja: quem paga em dia está pagando pelos que não pagam."},
 {"rank": 1, "name": "O custo do dinheiro", "short": "Captação", "tag": "o que o banco paga para captar", "num": 39.8, "prefix": "R$ ", "suffix": "", "dec": 2,
  "unit": "de cada R$ 100 de juros", "source": SRC, "col": (255, 170, 80),
  "say": "E o número um: o custo do dinheiro, o que o banco paga para captar, puxado pela Selic. Trinta e nove e oitenta."},
]
OUTRO = {"say": "Descascamos o juro camada por camada no episódio completo sobre o spread. Segue o Por Trás do Dinheiro.",
         "note": "Média da carteira toda · não é recomendação financeira"}
