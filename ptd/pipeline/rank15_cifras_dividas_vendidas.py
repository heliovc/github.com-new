# Ranking PTD #15 — as 5 cifras bilionárias do mercado de dívidas vendidas (countdown pelo valor, em R$ bilhões).
# Base: comunicado do Itaú (31/12/2015) / Reuters: 81,94% da Recovery por R$ 640 milhões; MP 1.393/2026 (Desenrola 3.0):
# despesa da União limitada a R$ 15 bilhões; Deloitte, pesquisa de NPL ciclo 2025/2026: R$ 30,2 bilhões cedidos em 2025;
# Ministério da Fazenda (min. Dario Durigan, out/2026): até R$ 90 bilhões em dívidas antigas na 1ª chamada do Desenrola 3.0;
# Recovery, via Bloomberg Línea (2026): mais de R$ 144 bilhões em créditos inadimplidos sob gestão.
# Abre a quarta-feira do EP16 (quem compra a sua dívida). Gráfico: "bubbles" (área proporcional) com tema NOVO
# roxo/âmbar — a faixa de valores vai de 0,64 a 144, e a bolha minúscula do nº 5 é parte da história.
TITLE = "5 cifras bilionárias por trás da sua dívida vendida (o nº 1 passa de R$ 140 bi) #shorts"
THEME = {"accent": (190, 140, 255), "accent2": (255, 190, 90), "bar_col": (70, 52, 110), "hl_col": (190, 140, 255),
         "glow": (40, 26, 70), "bar": "O MERCADO DAS DÍVIDAS VENDIDAS", "chart": "bubbles", "bubble_rmax": 230}
HOOK = {"say": "Quando você não paga uma dívida, ela pode ser vendida. E esse mercado movimenta bilhões. Estas são as cinco cifras que mostram o tamanho dele. A número um passa de cento e quarenta bilhões de reais.",
        "top": "Sua dívida à venda", "sub": "5 cifras do mercado de dívidas", "tease": "em R$ bilhões"}
ITEMS = [
 {"rank": 5, "name": "A compra da Recovery", "short": "Itaú", "tag": "Itaú compra do BTG, em 2015", "num": 0.64, "prefix": "R$ ", "suffix": " bi", "dec": 2,
  "unit": "por 82% da maior compradora de dívidas", "source": "comunicado do Itaú (31/12/2015) e Reuters",
  "say": "Número cinco: seiscentos e quarenta milhões de reais. Foi quanto o Itaú pagou, em dois mil e quinze, por oitenta e dois por cento da Recovery, uma empresa que vive de comprar dívida atrasada."},
 {"rank": 4, "name": "O cofre do governo", "short": "União", "tag": "Desenrola 3.0", "num": 15, "prefix": "R$ ", "suffix": " bi", "dec": 0,
  "unit": "teto para a União comprar dívidas", "source": "Medida Provisória 1.393/2026",
  "say": "Número quatro: quinze bilhões de reais. É o teto que o governo reservou, no Desenrola três ponto zero, para comprar dívidas antigas dos bancos. Com desconto mínimo de noventa por cento."},
 {"rank": 3, "name": "Vendidas em 2025", "short": "2025", "tag": "dívidas cedidas no ano", "num": 30.2, "prefix": "R$ ", "suffix": " bi", "dec": 1,
  "unit": "em dívidas vendidas pelos credores", "source": "Deloitte, pesquisa sobre o mercado de NPL (2025/2026)",
  "say": "Número três: trinta vírgula dois bilhões. É quanto os credores venderam em dívidas não pagas em dois mil e vinte e cinco, segundo a Deloitte."},
 {"rank": 2, "name": "A oferta ao governo", "short": "Oferta", "tag": "1ª chamada do Desenrola 3.0", "num": 90, "prefix": "R$ ", "suffix": " bi", "dec": 0,
  "unit": "em dívidas antigas que podem ir a leilão", "source": "Ministério da Fazenda (out/2026), via imprensa",
  "say": "Número dois: noventa bilhões. É o volume de dívidas antigas que os bancos podem oferecer ao governo na primeira chamada do Desenrola. Segundo o ministro da Fazenda."},
 {"rank": 1, "name": "Na mão de uma empresa", "short": "Recovery", "tag": "a maior compradora do país", "num": 144, "prefix": "R$ ", "suffix": " bi", "dec": 0,
  "unit": "em dívidas atrasadas sob gestão", "source": "Recovery, via Bloomberg Línea (2026)",
  "say": "E o número um: cento e quarenta e quatro bilhões de reais. É o tamanho das dívidas atrasadas que a Recovery administra. São mais de trinta e três milhões de devedores."},
]
OUTRO = {"say": "Quem compra a sua dívida, quanto paga por ela, e por que pode te dar noventa por cento de desconto. Episódio completo hoje, no Por Trás do Dinheiro.",
         "note": "Informativo · não é recomendação financeira"}
