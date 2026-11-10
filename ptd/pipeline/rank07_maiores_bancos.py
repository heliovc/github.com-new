# Ranking PTD #7 — os 5 maiores bancos do Brasil em ativos totais (set/2025)
# Variação visual: tema NOVO azul-noite/dourado + gráfico NOVO "towers" (arranha-céus, altura proporcional aos ativos).
# Gancho ligado ao EP09: o Master tinha R$ 82 bi em ativos (2024); o nº 1 tem mais de 30 vezes isso.
TITLE = "Os 5 maiores bancos do Brasil (o nº 1 tem mais de R$ 2,6 trilhões) #shorts"
THEME = {"accent": (250, 204, 92), "accent2": (140, 190, 255), "bar_col": (60, 80, 130), "hl_col": (250, 204, 92),
         "glow": (20, 34, 74), "tower": (38, 56, 96), "bar": "OS MAIORES BANCOS DO BRASIL", "chart": "towers"}
HOOK = {"say": "Os cinco maiores bancos do Brasil, pelo tamanho do que têm em ativos. O Banco Master, que quebrou em dois mil e vinte e cinco, tinha oitenta e dois bilhões. O número um aqui tem mais de trinta vezes isso.",
        "top": "Maiores bancos do Brasil", "sub": "ativos totais · set/2025", "tease": "o nº 1: R$ 2,65 trilhões"}
SRC_BC = "Banco Central (set/2025), via Olhar Digital"
ITEMS = [
 {"rank": 5, "name": "Santander Brasil", "short": "Santander", "tag": "braço do grupo espanhol", "num": 1.25, "prefix": "R$ ", "suffix": " tri", "dec": 2,
  "unit": "trilhão em ativos", "source": "balanço do Santander (3º tri/2025), via InfoMoney",
  "say": "Número cinco: o Santander Brasil, o braço brasileiro do grupo espanhol, com um vírgula vinte e cinco trilhão de reais em ativos."},
 {"rank": 4, "name": "Bradesco", "short": "Bradesco", "tag": "banco privado com sede em Osasco (SP)", "num": 1.794, "prefix": "R$ ", "suffix": " tri", "dec": 2,
  "unit": "trilhão em ativos", "source": SRC_BC,
  "say": "Número quatro: o Bradesco, o banco de Osasco, com um vírgula setenta e nove trilhão de reais."},
 {"rank": 3, "name": "Caixa", "short": "Caixa", "tag": "banco público do FGTS e da habitação", "num": 2.209, "prefix": "R$ ", "suffix": " tri", "dec": 2,
  "unit": "trilhões em ativos", "source": SRC_BC,
  "say": "Número três: a Caixa Econômica Federal, o banco público da casa própria, com dois vírgula vinte e um trilhões."},
 {"rank": 2, "name": "Banco do Brasil", "short": "BB", "tag": "controlado pela União", "num": 2.538, "prefix": "R$ ", "suffix": " tri", "dec": 2,
  "unit": "trilhões em ativos", "source": SRC_BC,
  "say": "Número dois: o Banco do Brasil, controlado pela União, com dois vírgula cinquenta e quatro trilhões. Quase empatado com o primeiro."},
 {"rank": 1, "name": "Itaú Unibanco", "short": "Itaú", "tag": "o maior banco do país", "num": 2.652, "prefix": "R$ ", "suffix": " tri", "dec": 2,
  "unit": "trilhões em ativos", "source": SRC_BC,
  "say": "E o número um: o Itaú Unibanco, com dois vírgula sessenta e cinco trilhões de reais em ativos."},
]
OUTRO = {"say": "Quer saber como um banco de oitenta bilhões quebrou e quem pagou a conta? O episódio do Banco Master está no canal. Segue o Por Trás do Dinheiro.",
         "note": "Ativos totais, set/2025 · não é recomendação financeira"}
