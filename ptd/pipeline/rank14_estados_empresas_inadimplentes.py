# Ranking PTD #14 — os 5 estados com mais empresas inadimplentes (CNPJs negativados), set/2026.
# Base: Serasa Experian, Indicador de Inadimplência das Empresas (divulgado em nov/2026): Brasil 9,4 milhões (recorde);
# SP 3.205.708, MG 946.410, RJ 889.525, PR 621.879, RS 545.837. SP > MG+RJ+PR+RS (3.003.651).
# Número absoluto reflete o tamanho da economia de cada estado, não a taxa (dito na nota final).
# Prepara o EP16 (o mercado das dívidas vendidas). Variação visual: tema NOVO âmbar/vermelho + gráfico NOVO "shops"
# (fileiras de lojinhas, 1 = 100 mil empresas).
TITLE = "Os 5 estados com mais empresas no vermelho (o nº 1 supera os outros 4 juntos) #shorts"
THEME = {"accent": (255, 184, 60), "accent2": (240, 90, 80), "bar_col": (70, 45, 20), "hl_col": (255, 184, 60),
         "glow": (60, 30, 18), "bar": "EMPRESAS COM DÍVIDA ATRASADA", "chart": "shops", "per_icon": 100.0}
HOOK = {"say": "Nove vírgula quatro milhões de empresas estão com contas atrasadas no Brasil. É recorde. Estes são os cinco estados com mais empresas no vermelho. E o número um tem mais do que os outros quatro somados.",
        "top": "Empresas no vermelho", "sub": "os 5 estados · Serasa Experian, set/2026", "tease": "1 lojinha = 100 mil empresas"}
SRC = "Serasa Experian, Indicador de Inadimplência das Empresas (set/2026)"
ITEMS = [
 {"rank": 5, "name": "Rio Grande do Sul", "short": "RS", "tag": "região Sul", "num": 546, "suffix": " mil", "dec": 0,
  "unit": "empresas inadimplentes", "source": SRC,
  "say": "Número cinco: Rio Grande do Sul. Quinhentas e quarenta e seis mil empresas com dívida atrasada."},
 {"rank": 4, "name": "Paraná", "short": "PR", "tag": "o maior do Sul", "num": 622, "suffix": " mil", "dec": 0,
  "unit": "empresas inadimplentes", "source": SRC,
  "say": "Número quatro: Paraná. Seiscentas e vinte e duas mil. O maior número de toda a região Sul."},
 {"rank": 3, "name": "Rio de Janeiro", "short": "RJ", "tag": "região Sudeste", "num": 890, "suffix": " mil", "dec": 0,
  "unit": "empresas inadimplentes", "source": SRC,
  "say": "Número três: Rio de Janeiro. Oitocentas e noventa mil empresas no vermelho."},
 {"rank": 2, "name": "Minas Gerais", "short": "MG", "tag": "quase 1 milhão", "num": 946, "suffix": " mil", "dec": 0,
  "unit": "empresas inadimplentes", "source": SRC,
  "say": "Número dois: Minas Gerais. Novecentas e quarenta e seis mil. Quase um milhão de empresas."},
 {"rank": 1, "name": "São Paulo", "short": "SP", "tag": "mais que os outros 4 juntos", "num": 3206, "suffix": " mil", "dec": 0,
  "unit": "empresas inadimplentes", "source": SRC,
  "say": "E o número um: São Paulo. Três vírgula dois milhões de empresas. Mais do que Minas, Rio, Paraná e Rio Grande do Sul somados."},
]
OUTRO = {"say": "E quando ninguém paga, essa dívida muitas vezes é vendida, por uma fração do valor. Quem compra, e por quê, é o próximo episódio. Segue o Por Trás do Dinheiro.",
         "note": "Número absoluto, não taxa · não é recomendação financeira"}
