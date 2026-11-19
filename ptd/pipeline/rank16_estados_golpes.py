# Ranking PTD #16 — os 5 estados com mais golpes (estelionatos registrados) por 100 mil habitantes em 2025.
# Base: Fórum Brasileiro de Segurança Pública, 20º Anuário Brasileiro de Segurança Pública (23/07/2026), via imprensa
# (Metrópoles, Brasil 61, Correio da Manhã): Brasil 2.261.055 registros, taxa 1.059,43 por 100 mil; SP 1.808,3; DF 1.717,0;
# PR 1.339,1; RO 1.329,6; SC 1.294,8. Inclui estelionato comum e por fraude eletrônica. Taxa mede REGISTROS (boletins),
# não necessariamente ocorrências — dito na descrição. "1 a cada 55 moradores" e "mais de 4 por minuto" (2.261.055 / 525.600 min) = CÁLCULO do canal (100.000 / 1.808,3).
# Dia sem longo (quinta); prepara o EP17 (golpe do Pix, sexta). Diferente do rank #14 (empresas inadimplentes, número absoluto).
# Variação visual: tema NOVO laranja-alerta/ciano + gráfico NOVO "hooks" (linhas de pesca com anzol; piso 1.000).
TITLE = "Os 5 estados onde mais se cai em golpe no Brasil (no nº 1, 1 registro a cada 55 pessoas) #shorts"
THEME = {"accent": (255, 140, 50), "accent2": (80, 210, 230), "bar_col": (90, 50, 20), "hl_col": (255, 140, 50),
         "glow": (58, 30, 18), "bar": "O MAPA DO GOLPE NO BRASIL", "chart": "hooks", "floor": 1000, "rod_y": 780,
         "floor_note": "por 100 mil habitantes · escala a partir de 1.000"}
HOOK = {"say": "Em dois mil e vinte e cinco, o Brasil registrou mais de dois milhões de golpes. Mais de quatro por minuto. Estes são os cinco estados onde mais se registra golpe por habitante. E no número um, é um registro a cada cinquenta e cinco moradores.",
        "top": "Onde mais se cai em golpe", "sub": "estelionatos por 100 mil habitantes · 2025", "tease": "2,26 milhões de registros no país"}
SRC = "Fórum Brasileiro de Segurança Pública, Anuário 2026 (dados de 2025)"
ITEMS = [
 {"rank": 5, "name": "Santa Catarina", "short": "SC", "tag": "região Sul", "num": 1294.8, "dec": 1,
  "unit": "estelionatos por 100 mil habitantes", "source": SRC,
  "say": "Número cinco: Santa Catarina. Mil duzentos e noventa e cinco registros de estelionato para cada cem mil habitantes."},
 {"rank": 4, "name": "Rondônia", "short": "RO", "tag": "o único do Norte no top 5", "num": 1329.6, "dec": 1,
  "unit": "estelionatos por 100 mil habitantes", "source": SRC,
  "say": "Número quatro: Rondônia. Mil trezentos e trinta. O único estado do Norte na lista."},
 {"rank": 3, "name": "Paraná", "short": "PR", "tag": "o maior do Sul", "num": 1339.1, "dec": 1,
  "unit": "estelionatos por 100 mil habitantes", "source": SRC,
  "say": "Número três: Paraná. Mil trezentos e trinta e nove. Quase empatado com Rondônia."},
 {"rank": 2, "name": "Distrito Federal", "short": "DF", "tag": "51 mil registros no ano", "num": 1717.0, "dec": 1,
  "unit": "estelionatos por 100 mil habitantes", "source": SRC,
  "say": "Número dois: Distrito Federal. Mil setecentos e dezessete. Um salto enorme em relação ao terceiro lugar."},
 {"rank": 1, "name": "São Paulo", "short": "SP", "tag": "1 registro a cada 55 pessoas", "num": 1808.3, "dec": 1,
  "unit": "estelionatos por 100 mil habitantes", "source": SRC,
  "say": "E o número um: São Paulo. Mil oitocentos e oito registros por cem mil habitantes. Na prática, um boletim de golpe para cada cinquenta e cinco moradores."},
]
OUTRO = {"say": "E boa parte desses golpes hoje passa pelo Pix. Para onde vai o dinheiro, e quem tem que devolver, é o episódio de amanhã. Segue o Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
