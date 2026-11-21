# Ranking PTD #18 — os 5 bancos com o maior índice de reclamações no Banco Central (3º trimestre de 2026, jul–set).
# Base: Banco Central, Ranking de Instituições por Índice de Reclamações (bancos e financeiras com mais de 4 milhões de
# clientes), divulgado em 22/10/2026, via imprensa (Let's Money, BPMoney, Finsiders Brasil): Bradesco 57,23 (6.333
# reclamações procedentes), C6 52,31 (1.893), Itaú 43,20 (4.252), BTG Pactual/Banco Pan 40,60 (1.127), PicPay 35,51.
# Índice = reclamações procedentes / clientes x 1.000.000. Bradesco no 2º tri/2026: 84,90 (Let's Money).
# "1 a cada ~17.500 clientes" = 1.000.000 / 57,23, CÁLCULO do canal.
# Dia SEM longo (sábado). Short aponta para o EP17 (golpe do Pix: quem tem que devolver).
# Visual: tema NOVO vermelho/âmbar com o gráfico "phones" (app do banco enchendo), escala sem piso.
TITLE = "Os 5 bancos com mais reclamações no Banco Central (o nº 1 é um gigante) #shorts"
THEME = {"accent": (255, 92, 92), "accent2": (255, 190, 70), "bar_col": (110, 44, 52), "hl_col": (255, 92, 92),
         "glow": (60, 20, 26), "bar": "RANKING DE RECLAMAÇÕES DO BC", "chart": "phones", "floor": 0}
HOOK = {"say": "Os cinco bancos que mais levaram reclamação no Banco Central. E não é só banco digital: o primeiro lugar é um dos maiores bancos do país.",
        "top": "Quem mais irrita o cliente", "sub": "queixas por milhão de clientes", "tease": "3º trimestre de 2026"}
SRC = "Banco Central, Ranking de Reclamações, 3º tri 2026"
ITEMS = [
 {"rank": 5, "name": "PicPay", "short": "PicPay", "tag": "liderava no fim de 2025", "num": 35.51, "suffix": "", "dec": 1,
  "unit": "reclamações por milhão de clientes", "source": SRC,
  "say": "Número cinco: PicPay. Trinta e cinco vírgula cinco reclamações procedentes por milhão de clientes. No fim de 2025, ele era o primeiro."},
 {"rank": 4, "name": "BTG Pactual / Banco Pan", "short": "BTG/Pan", "tag": "o Pan pesa na conta", "num": 40.60, "suffix": "", "dec": 1,
  "unit": "reclamações por milhão de clientes", "source": SRC,
  "say": "Número quatro: o grupo BTG Pactual e Banco Pan. Quarenta vírgula seis por milhão."},
 {"rank": 3, "name": "Itaú", "short": "Itaú", "tag": "4.252 reclamações procedentes", "num": 43.20, "suffix": "", "dec": 1,
  "unit": "reclamações por milhão de clientes", "source": SRC,
  "say": "Número três: Itaú. Quarenta e três vírgula dois. Foram mais de quatro mil e duzentas reclamações que o Banco Central deu razão ao cliente."},
 {"rank": 2, "name": "C6 Bank", "short": "C6", "tag": "1.893 reclamações procedentes", "num": 52.31, "suffix": "", "dec": 1,
  "unit": "reclamações por milhão de clientes", "source": SRC,
  "say": "Número dois: o C6 Bank, o primeiro digital da lista. Cinquenta e dois vírgula três por milhão de clientes."},
 {"rank": 1, "name": "Bradesco", "short": "Bradesco", "tag": "6.333 reclamações procedentes", "num": 57.23, "suffix": "", "dec": 1,
  "unit": "reclamações por milhão de clientes", "source": SRC,
  "say": "E o número um: Bradesco. Cinquenta e sete vírgula dois. Seis mil trezentas e trinta e três reclamações procedentes em três meses. E isso já é uma melhora: no trimestre anterior, o índice era oitenta e quatro."},
]
OUTRO = {"say": "Muitas dessas reclamações começam num golpe do Pix. Para onde vai o dinheiro e quem tem que devolver está no vídeo completo. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
