# Ranking PTD #17 — os 5 países com mais transações de pagamento instantâneo (em tempo real) em 2023.
# Base: ACI Worldwide, Prime Time for Real-Time 2024 (release de 30/04/2024 e infográfico executivo): Índia 129,3 bi
# (49% do total mundial), Brasil 37,4 bi (14%; crescimento de 77,9% no ano), Tailândia 20,4 bi (8%), China 17,2 bi (7%),
# Coreia do Sul 9,1 bi (3%); total mundial 266,2 bi. "Mais de 100 milhões por dia" no Brasil = 37,4 bi / 365, CÁLCULO
# do canal. Dados de 2023 = os mais recentes por país publicados pela ACI encontrados; dito na tela e na descrição.
# Dia com longo (sexta, EP17 golpe do Pix às 18:00); às 12:00 o EP17 ainda não está no ar, então o ranking aponta para o
# EP07 (Como o Pix mudou os bancos). Diferente do rank #8 (recordes diários do Pix no Brasil).
# Visual: tema NOVO índigo/coral com o gráfico "bubbles" (área da bolha proporcional ao volume).
TITLE = "Os 5 países que mais usam pagamento instantâneo (o Brasil não é o nº 1) #shorts"
THEME = {"accent": (255, 120, 100), "accent2": (130, 140, 255), "bar_col": (52, 56, 120), "hl_col": (255, 120, 100),
         "glow": (30, 28, 72), "bar": "PAGAMENTO INSTANTÂNEO NO MUNDO", "chart": "bubbles", "bubble_rmax": 220}
HOOK = {"say": "Os cinco países que mais fazem pagamento instantâneo no mundo. O Brasil, com o Pix, está na lista. Mas não é o número um. E o primeiro lugar faz mais do que os outros quatro juntos.",
        "top": "O Pix contra o mundo", "sub": "transações em tempo real · 2023", "tease": "266 bilhões no mundo"}
SRC = "ACI Worldwide, Prime Time for Real-Time 2024 (dados de 2023)"
ITEMS = [
 {"rank": 5, "name": "Coreia do Sul", "short": "Coreia", "tag": "3% do total mundial", "num": 9.1, "suffix": " bi", "dec": 1,
  "unit": "transações em tempo real no ano", "source": SRC,
  "say": "Número cinco: Coreia do Sul. Nove vírgula um bilhões de pagamentos instantâneos em um ano."},
 {"rank": 4, "name": "China", "short": "China", "tag": "crescimento de só 3,8%", "num": 17.2, "suffix": " bi", "dec": 1,
  "unit": "transações em tempo real no ano", "source": SRC,
  "say": "Número quatro: China. Dezessete vírgula dois bilhões, e quase parada: cresceu só três vírgula oito por cento no ano."},
 {"rank": 3, "name": "Tailândia", "short": "Tailândia", "tag": "o sistema PromptPay", "num": 20.4, "suffix": " bi", "dec": 1,
  "unit": "transações em tempo real no ano", "source": SRC,
  "say": "Número três: Tailândia, com vinte vírgula quatro bilhões. Um país de setenta milhões de habitantes à frente da China."},
 {"rank": 2, "name": "Brasil", "short": "Brasil", "tag": "o Pix cresceu 77,9% no ano", "num": 37.4, "suffix": " bi", "dec": 1,
  "unit": "transações em tempo real no ano", "source": SRC,
  "say": "Número dois: o Brasil. Trinta e sete vírgula quatro bilhões de Pix. Mais de cem milhões por dia, e quase o dobro da Tailândia."},
 {"rank": 1, "name": "Índia", "short": "Índia", "tag": "49% de todo o mundo", "num": 129.3, "suffix": " bi", "dec": 1,
  "unit": "transações em tempo real no ano", "source": SRC,
  "say": "E o número um: a Índia, com o sistema UPI. Cento e vinte e nove bilhões de transações. Sozinha, quase metade de todos os pagamentos instantâneos do planeta."},
]
OUTRO = {"say": "E o Pix é tão rápido que virou a ferramenta preferida dos golpistas. Para onde vai o dinheiro, e quem tem que devolver, é o episódio de hoje à noite. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
