# Ranking PTD #21 — os 5 canais por onde o brasileiro faz transações bancárias (participação no total de 2025).
# Base: Febraban/Deloitte, Pesquisa Febraban de Tecnologia Bancária 2026 (ano-base 2025, divulgada em jun/2026), via imprensa
# (O Tempo, 26/06/2026; Mobile Time; Coletivo Tech): 240,8 bilhões de transações em 2025; mobile banking 78% (187,5 bi);
# POS/maquininhas 11%; internet banking 5%; agências 3%; autoatendimento (caixas eletrônicos) 2%; outros canais 1% (fora).
# Digitais (celular + internet) = 83%. "Mais de 7 vezes o 2º lugar" = 78 / 11 = 7,1, CÁLCULO do canal.
# Visual: tema NOVO verde-esmeralda/âmbar com o gráfico "waffle" (grade 10x10 = 100%).
# Dia SEM longo (terça): o Short aponta para o EP18 (bancos por trás dos apps).
TITLE = "Os 5 lugares onde o brasileiro usa o banco (a agência ficou com 3%) #shorts"
THEME = {"accent": (70, 220, 150), "accent2": (255, 190, 80), "bar_col": (24, 70, 50), "hl_col": (70, 220, 150),
         "glow": (16, 48, 40), "bar": "ONDE O BRASILEIRO USA O BANCO", "chart": "waffle",
         "rest_label": "o 1% que sobra: outros canais"}
HOOK = {"say": "Em 2025, os brasileiros fizeram duzentas e quarenta bilhões de transações bancárias. Onde? Os cinco canais, do menor para o maior. E a agência, que já foi o centro de tudo, quase sumiu.",
        "top": "Onde o brasileiro usa o banco", "sub": "% das transações de 2025", "tease": "240,8 bilhões de transações"}
SRC = "Febraban/Deloitte, Pesquisa de Tecnologia Bancária 2026"
ITEMS = [
 {"rank": 5, "name": "Caixa eletrônico", "short": "Caixa 24h", "tag": "o saque virou raridade", "num": 2.0, "suffix": "%", "dec": 0,
  "unit": "das transações bancárias", "source": SRC, "col": (150, 160, 190),
  "say": "Número cinco: o caixa eletrônico. Só dois por cento das transações."},
 {"rank": 4, "name": "Agência", "short": "Agência", "tag": "a fila que encolheu", "num": 3.0, "suffix": "%", "dec": 0,
  "unit": "das transações bancárias", "source": SRC, "col": (240, 100, 90),
  "say": "Número quatro: a agência bancária. Três por cento. Três em cada cem operações ainda passam pelo balcão."},
 {"rank": 3, "name": "Internet banking", "short": "Computador", "tag": "o banco no computador", "num": 5.0, "suffix": "%", "dec": 0,
  "unit": "das transações bancárias", "source": SRC, "col": (110, 150, 255),
  "say": "Número três: o internet banking, o banco no computador. Cinco por cento. Hoje é mais usado por empresas."},
 {"rank": 2, "name": "Maquininha", "short": "Maquininha", "tag": "cartão e Pix no caixa da loja", "num": 11.0, "suffix": "%", "dec": 0,
  "unit": "das transações bancárias", "source": SRC, "col": (255, 190, 80),
  "say": "Número dois: a maquininha no caixa da loja, com cartão e cada vez mais Pix. Onze por cento."},
 {"rank": 1, "name": "Celular", "short": "Celular", "tag": "mais de 7 vezes o 2º lugar", "num": 78.0, "suffix": "%", "dec": 0,
  "unit": "das transações bancárias", "source": SRC, "col": (70, 220, 150),
  "say": "E o número um: o celular. Setenta e oito por cento. Cento e oitenta e sete bilhões de transações no aplicativo, mais de sete vezes o segundo lugar."},
]
OUTRO = {"say": "Mas quem guarda de verdade o dinheiro do seu aplicativo? Pode não ser quem você pensa. Está no vídeo completo. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
