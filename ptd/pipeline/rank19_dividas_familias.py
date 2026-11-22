# Ranking PTD #19 — as 5 dívidas mais comuns das famílias brasileiras endividadas (julho de 2026).
# Base: CNC, Pesquisa de Endividamento e Inadimplência do Consumidor (Peic), julho de 2026, divulgada em 06/08/2026,
# via imprensa (InfoMoney, Folha de Pernambuco, Metrópoles, Jornal de Brasília, Gazeta SP): 82% das famílias endividadas
# (recorde da série, 6º mês seguido); entre as endividadas: cartão de crédito 85,3%, carnês 16,1%, crédito pessoal 13%,
# financiamento de casa 9,6%, financiamento de carro 9%. Inadimplência 29,8% em julho.
# Percentuais somam mais de 100%: uma família pode ter mais de um tipo de dívida (dito na narração).
# Peic considera endividada a família com contas a vencer (não só atrasadas) — dito no gancho.
# "Mais de 5 vezes o 2º lugar" = 85,3 / 16,1 = 5,3, CÁLCULO do canal.
# Dia SEM longo (domingo). Short aponta para o EP10 (rotativo do cartão).
# Visual: tema NOVO violeta/verde-água com o gráfico novo "jars" (potes 0-100%, escala absoluta).
TITLE = "As 5 dívidas mais comuns das famílias brasileiras (o nº 1 está em 85% delas) #shorts"
THEME = {"accent": (178, 128, 255), "accent2": (90, 222, 200), "bar_col": (64, 46, 110), "hl_col": (178, 128, 255),
         "glow": (40, 26, 72), "bar": "PESQUISA DE ENDIVIDAMENTO · CNC", "chart": "jars"}
HOOK = {"say": "Oito em cada dez famílias brasileiras têm alguma dívida, mesmo sem atraso. Mas de que tipo? As cinco dívidas mais comuns. E o primeiro lugar não tem nem concorrência.",
        "top": "As dívidas mais comuns", "sub": "% das famílias endividadas", "tease": "82% das famílias têm dívida"}
SRC = "CNC, Peic, julho de 2026"
ITEMS = [
 {"rank": 5, "name": "Financiamento de carro", "short": "Carro", "tag": "parcela que dura anos", "num": 9.0, "suffix": "%", "dec": 0,
  "unit": "das famílias endividadas", "source": SRC,
  "say": "Número cinco: financiamento de carro. Nove por cento das famílias endividadas pagam um."},
 {"rank": 4, "name": "Financiamento de casa", "short": "Casa", "tag": "o juro mais baixo da lista", "num": 9.6, "suffix": "%", "dec": 1,
  "unit": "das famílias endividadas", "source": SRC,
  "say": "Número quatro: financiamento da casa própria. Nove vírgula seis por cento."},
 {"rank": 3, "name": "Crédito pessoal", "short": "Pessoal", "tag": "o empréstimo sem garantia", "num": 13.0, "suffix": "%", "dec": 0,
  "unit": "das famílias endividadas", "source": SRC,
  "say": "Número três: crédito pessoal, o empréstimo sem garantia nenhuma. Treze por cento."},
 {"rank": 2, "name": "Carnês", "short": "Carnês", "tag": "a prestação da loja", "num": 16.1, "suffix": "%", "dec": 1,
  "unit": "das famílias endividadas", "source": SRC,
  "say": "Número dois: os carnês, a velha prestação da loja. Dezesseis por cento. E repara: uma família pode ter mais de um tipo de dívida."},
 {"rank": 1, "name": "Cartão de crédito", "short": "Cartão", "tag": "mais de 5x o 2º lugar", "num": 85.3, "suffix": "%", "dec": 1,
  "unit": "das famílias endividadas", "source": SRC,
  "say": "E o número um: cartão de crédito. Oitenta e cinco vírgula três por cento das famílias endividadas devem no cartão. Mais de cinco vezes o segundo lugar. E se a fatura não é paga inteira, entra o juro mais caro do Brasil."},
]
OUTRO = {"say": "Por que o rotativo do cartão é o juro mais caro do país, e quem ganha com ele, está no vídeo completo. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
