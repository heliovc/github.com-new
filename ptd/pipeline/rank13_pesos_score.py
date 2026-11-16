# Ranking PTD #13 — o que mais pesa no seu score: os 5 maiores pesos do Serasa Score 2.0, do menor para o maior.
# Base: Serasa, perguntas frequentes do Serasa Score 2.0 (pesos divulgados pela própria Serasa): hábitos de pagamento
# do Cadastro Positivo 29%, experiência/relacionamento com o mercado de crédito 24%, dívidas negativadas 21%,
# busca por crédito (consultas ao CPF feitas por empresas) 12%, informações cadastrais 8%, contratos de crédito 6% (fica de fora).
# Liga com o EP15 (score de crédito). Variação visual: tema NOVO azul-ciano/rosa + gráfico NOVO "waffle" (grade 10x10 = 100%).
TITLE = "5 coisas que mais pesam no seu score (o nº 1 não é ter dívida) #shorts"
THEME = {"accent": (90, 210, 240), "accent2": (255, 120, 170), "bar_col": (30, 50, 70), "hl_col": (90, 210, 240),
         "glow": (20, 40, 60), "bar": "O QUE PESA NO SEU SCORE", "chart": "waffle",
         "rest_label": "os outros 6%: contratos de crédito ativos"}
HOOK = {"say": "O seu score de crédito é uma conta com pesos. E a própria Serasa divulga quanto vale cada coisa. Estas são as cinco que mais pesam. E a número um não é ter dívida.",
        "top": "O que mais pesa no seu score", "sub": "pesos do Serasa Score 2.0", "tease": "o nº 1 não é a dívida"}
SRC = "Serasa, perguntas frequentes do Serasa Score 2.0"
ITEMS = [
 {"rank": 5, "name": "Dados cadastrais", "short": "Cadastro", "tag": "endereço, renda, dados atualizados", "num": 8, "prefix": "", "suffix": "%", "dec": 0,
  "unit": "do peso do score", "source": SRC, "col": (160, 110, 240),
  "say": "Número cinco: os seus dados cadastrais. Se estão atualizados, se você é sócio de alguma empresa. Oito por cento."},
 {"rank": 4, "name": "Busca por crédito", "short": "Consultas", "tag": "empresas consultando o seu CPF", "num": 12, "prefix": "", "suffix": "%", "dec": 0,
  "unit": "do peso do score", "source": SRC, "col": (255, 170, 80),
  "say": "Número quatro: a busca por crédito. Muitas empresas consultando o seu CPF em pouco tempo. Doze por cento. Consultar o próprio score não conta."},
 {"rank": 3, "name": "Dívidas negativadas", "short": "Dívidas", "tag": "o nome sujo", "num": 21, "prefix": "", "suffix": "%", "dec": 0,
  "unit": "do peso do score", "source": SRC, "col": (235, 100, 85),
  "say": "Número três: as dívidas negativadas, o famoso nome sujo. Vinte e um por cento. Pesa muito, mas não é o topo."},
 {"rank": 2, "name": "Tempo de mercado", "short": "Histórico", "tag": "há quanto tempo você usa crédito", "num": 24, "prefix": "", "suffix": "%", "dec": 0,
  "unit": "do peso do score", "source": SRC, "col": (90, 140, 240),
  "say": "Número dois: a sua experiência com o mercado. Há quanto tempo você tem conta, cartão e empréstimo. Vinte e quatro por cento."},
 {"rank": 1, "name": "Pagar em dia", "short": "Em dia", "tag": "o seu Cadastro Positivo", "num": 29, "prefix": "", "suffix": "%", "dec": 0,
  "unit": "do peso do score", "source": SRC, "col": (80, 210, 130),
  "say": "E o número um: pagar em dia, o que aparece no Cadastro Positivo. Vinte e nove por cento. O score olha mais para o que você paga do que para o que você deve."},
]
OUTRO = {"say": "O episódio completo abre a caixa do score: quem calcula e por que dois vizinhos pagam juros diferentes. Segue o Por Trás do Dinheiro.",
         "note": "Cada birô tem o seu modelo · não é recomendação financeira"}
