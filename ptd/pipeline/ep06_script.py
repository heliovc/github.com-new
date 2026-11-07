# EP06 — Antecipação de recebíveis: o negócio bilionário que ninguém vê
# Estrutura NOVA: "siga o recebível" — uma venda de R$ 1.200 em 12x (exemplo ilustrativo) percorre 6 paradas
# (a venda -> a agenda -> o balcão -> o preço -> quem lucra -> a porta aberta) + a virada (quem paga) + payoff.
# Diferente do EP03 (autópsia de uma taxa), EP04 (extrato de um cliente) e EP05 (luta em rounds).
# Cenas novas: journey (mapa de paradas com a moeda viajando) e calendar (agenda de recebíveis; pull = antecipar).
# Loops: (1) para onde vão os quase R$ 190 -> paradas 4 e 5; (2) por que uma taxa derrubou a Stone 23,7% num dia -> parada 5;
#        (3) quem paga a conta no fim -> a virada.
# Exemplo ilustrativo (marcado na tela): MDR 3% no parcelado e antecipação a 2% ao mês (desconto linear por mês adiantado).
#   1.200 x 0,97 = 1.164 -> 12 parcelas de R$ 97; custo = 97 x 0,02 x (1+...+12) = 97 x 0,02 x 78 = R$ 151,32;
#   na conta hoje = 1.164 - 151,32 = R$ 1.012,68; diferença total = R$ 187,32 (15,6% da venda).
TITLE = "Antecipação de recebíveis: o negócio bilionário que ninguém vê"

STOPS = ["A venda", "A agenda", "O balcão", "O preço", "Quem lucra", "A porta"]
ILU = "Exemplo ilustrativo: taxa de 3% no parcelado e antecipação a 2% ao mês — as taxas reais variam por negócio"
PARC = [[f"mês {i}", "R$ 97"] for i in range(1, 13)]

SCENES = [
 # ---------- GANCHO (0–30 s) ----------
 {"say": "Você compra uma coisa de mil e duzentos reais em doze vezes sem juros. A loja não recebe mil e duzentos. Se quiser o dinheiro hoje, pode ficar com pouco mais de mil.",
  "vis": {"type": "bignumber", "from": 1200, "to": 1013, "prefix": "R$ ", "decimals": 0, "caption": "o que sobra para a loja que quer receber hoje uma venda de R$ 1.200 em 12x",
          "source": ILU}},
 {"say": "Os quase duzentos reais que somem no caminho alimentam um mercado que movimentou mais de seiscentos bilhões de reais no ano passado. E foi uma taxa desse mercado que fez a Stone perder quase um quarto do valor na bolsa em um único dia.",
  "vis": {"type": "title", "title": "R$ 614,9 bilhões\nantecipados em 2025", "sub": "um negócio que quase ninguém vê"}},
 {"say": "Para entender quem fica com esse dinheiro, vamos seguir essa venda de mil e duzentos reais, parada por parada, da maquininha até a conta da loja. São seis paradas. E na última está o motivo de esse mercado estar crescendo três vezes mais rápido que o próprio cartão de crédito.",
  "vis": {"type": "title", "title": "Siga o recebível", "sub": "6 paradas — POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- PARADA 1: A VENDA ----------
 {"say": "Parada um: a venda. O cliente aproxima o cartão e escolhe doze vezes. Para ele, acabou: a compra está feita e as parcelas vão aparecer na fatura, mês a mês. Para a loja, a história está só começando.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 0, "title": "A venda", "sub": "R$ 1.200 em 12x sem juros"}},
 {"say": "Esse jeito de comprar é a regra no Brasil. Segundo a Abecs, a associação das empresas de cartão, o parcelado sem juros respondeu por quarenta e três vírgula dois por cento de todo o valor pago no crédito no primeiro trimestre de dois mil e vinte e seis. Quase metade.",
  "vis": {"type": "bignumber", "from": 0, "to": 43.2, "suffix": "%", "decimals": 1, "caption": "fatia do parcelado sem juros no valor pago com cartão de crédito (1º tri/2026)",
          "source": "Fonte: Abecs, balanço do 1º trimestre de 2026"}},
 {"say": "E não é só compra grande. Ainda segundo a Abecs, sessenta e dois vírgula quatro por cento das compras parceladas são feitas em até seis vezes. E quase todo o volume parcelado, noventa e sete vírgula oito por cento, fica em até doze parcelas. Ou seja: o país inteiro vende hoje e recebe ao longo de meses.",
  "vis": {"type": "cards", "title": "Como o Brasil parcela", "cards": [["1", "62%", "das compras: até 6x"], ["2", "98%", "do volume: até 12x"], ["3", "43%", "do crédito é sem juros"]],
          "highlight": 1, "caption": "Fonte: Abecs, 1º trimestre de 2026"}},

 # ---------- PARADA 2: A AGENDA ----------
 {"say": "Parada dois: a agenda. A maquininha desconta a taxa dela. No nosso exemplo, três por cento, o que dá trinta e seis reais. Sobram mil cento e sessenta e quatro. Mas esse dinheiro não cai de uma vez.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 1, "title": "A agenda", "sub": "R$ 1.200 − 3% de taxa = R$ 1.164", "caption": ILU}},
 {"say": "Ele vira doze parcelas de noventa e sete reais. A primeira cai em cerca de trinta dias. A última, perto de um ano depois. Isso é a agenda de recebíveis: um calendário de dinheiro que a loja já ganhou, mas ainda não tem.",
  "vis": {"type": "calendar", "title": "A agenda de recebíveis da loja", "cells": PARC, "today_txt": "R$ 0", "today_note": "na conta hoje", "caption": ILU}},
 {"say": "O problema é que as contas da loja não esperam um ano. O fornecedor quer receber este mês. O aluguel vence este mês. O salário da equipe também. A loja vendeu bem, mas está sem dinheiro. É nesse buraco entre vender e receber que mora um dos negócios mais lucrativos do sistema financeiro.",
  "vis": {"type": "compare", "left": ["O que a loja tem", "12 parcelas a receber", "R$ 97 por mês", "até daqui a 1 ano"], "right": ["O que a loja deve", "fornecedor, aluguel", "salários, impostos", "vencem este mês"],
          "caption": "O buraco entre vender e receber"}},

 # ---------- PARADA 3: O BALCÃO ----------
 {"say": "Parada três: o balcão. Alguém oferece um atalho. Pode ser a própria empresa da maquininha, pode ser um banco. A proposta é simples: me passa essas doze parcelas, e eu te pago hoje. Com um desconto, claro.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 2, "title": "O balcão", "sub": "\"me passa as parcelas, eu te pago hoje\""}},
 {"say": "Isso é antecipar recebíveis. Não é um empréstimo comum: a loja não pede dinheiro emprestado, ela vende um dinheiro que já é dela, só que do futuro. E muitas lojas fazem isso no automático. Toda venda já entra antecipada, e a taxa sai sem ninguém perceber.",
  "vis": {"type": "flow", "nodes": ["Venda parcelada", "Agenda de 12 meses", "Antecipação", "Dinheiro hoje"], "notes": ["no cartão", "o dinheiro do futuro", "com desconto", "menos a taxa"],
          "caption": "Antecipar = vender hoje o que só cairia depois"}},
 {"say": "Por que alguém aceitaria pagar adiantado? Porque o risco é baixo. Quem vai pagar essas parcelas não é bem o cliente da loja, é o banco que emitiu o cartão. Se o cliente atrasar a fatura, o problema é do banco dele. A loja recebe do mesmo jeito. Para quem antecipa, é quase como emprestar dinheiro com a garantia de um banco.",
  "vis": {"type": "flow", "nodes": ["Cliente", "Banco do cartão", "Maquininha", "Loja"], "notes": ["paga a fatura", "garante as parcelas", "repassa", "recebe mesmo se o cliente atrasar"],
          "caption": "Por isso o risco de antecipar é baixo"}},

 # ---------- PARADA 4: O PREÇO ----------
 {"say": "Parada quatro: o preço. Hora de responder a pergunta do começo: para onde vão os quase duzentos reais? Vamos fazer a conta com uma taxa de antecipação de dois por cento ao mês, um número só para o exemplo.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 3, "title": "O preço", "sub": "antecipação a 2% ao mês (exemplo)", "caption": ILU}},
 {"say": "A primeira parcela, que cairia em um mês, perde dois por cento. A segunda, que cairia em dois meses, perde quatro. A última, que só cairia em doze meses, perde vinte e quatro por cento. Somando as doze, a loja paga cento e cinquenta e um reais de antecipação. E fica com mil e treze na conta hoje.",
  "vis": {"type": "calendar", "title": "Antecipar as 12 parcelas", "cells": PARC, "pull": True, "today_to": 1013, "cost_to": 151, "caption": ILU}},
 {"say": "Juntando a taxa da maquininha e a antecipação, a venda de mil e duzentos reais perdeu cento e oitenta e sete reais no caminho. Quinze vírgula seis por cento. Numa loja que trabalha com margem de dez ou quinze por cento, isso pode ser a diferença entre lucro e prejuízo naquela venda.",
  "vis": {"type": "receipt", "title": "Para onde foram os R$ 1.200", "head": "VENDA DE R$ 1.200 EM 12x",
          "lines": [["Venda", "R$ 1.200", "#14202F"], ["Taxa da maquininha", "− R$ 36", "#E06C5A"], ["Antecipação", "− R$ 151", "#E06C5A"]],
          "total": ["Na conta hoje", "R$ 1.013"], "caption": ILU}},
 # REENGAJE ~3:00 — o número mais absurdo: o tamanho do mercado
 {"say": "Agora multiplica isso pelo país. Segundo a Núclea, uma das empresas que registram esses recebíveis, o volume antecipado no Brasil saltou de quatrocentos e vinte e oito vírgula seis bilhões de reais em dois mil e vinte e quatro para seiscentos e catorze vírgula nove bilhões em dois mil e vinte e cinco. Uma alta de quarenta e três por cento em um ano.",
  "vis": {"type": "bars", "title": "Volume antecipado no Brasil (R$ bilhões)", "items": [["2024", 428.6, "#5B8DEF"], ["2025", 614.9, "#F2A93B"]], "decimals": 1,
          "caption": "Fonte: Núclea, via Valor Econômico (balanço de 2025)"}},
 {"say": "No mesmo período, o pagamento com cartão de crédito cresceu catorze vírgula cinco por cento. A antecipação cresceu três vezes mais rápido. E o número de estabelecimentos que usaram esse atalho subiu trinta e três por cento. Cada vez mais lojas vendem o próprio futuro para pagar o presente.",
  "vis": {"type": "scoreboard", "title": "2025 contra 2024", "cols": [["Crédito", 14.5, "#5B8DEF"], ["Lojas que anteciparam", 33.4, "#3AC47D"], ["Volume antecipado", 43.5, "#F2A93B"]],
          "highlight": 2, "suffix": "%", "caption": "Fontes: Abecs (crédito); Núclea, via Valor Econômico (antecipação)"}},

 # ---------- PARADA 5: QUEM LUCRA ----------
 {"say": "Parada cinco: quem lucra. Pensa na posição de quem antecipa. Ele capta dinheiro mais ou menos ao custo da Selic, que o Banco Central manteve em treze vírgula setenta e cinco por cento ao ano na reunião de quatro de novembro. Isso dá perto de um vírgula um por cento ao mês.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 4, "title": "Quem lucra", "sub": "Selic: 13,75% ao ano ≈ 1,1% ao mês",
          "caption": "Fonte: Banco Central, decisão do Copom de 04/11/2026"}},
 {"say": "Se ele cobra dois por cento ao mês, como no nosso exemplo, a diferença é de quase um ponto por mês, emprestando com a garantia de um banco. Em um ano, dois por cento ao mês viram quase vinte e sete por cento. É um negócio de margem gorda e risco baixo. Por isso todo mundo quer ficar no meio dessa conta.",
  "vis": {"type": "line", "title": "R$ 100 crescendo em 12 meses", "points": [["0", 100], ["3", 106.1], ["6", 112.6], ["9", 119.5], ["12", 126.8]],
          "prefix": "R$ ", "decimals": 0, "color": "#F2A93B", "cap": 114.4, "cap_label": "custo do dinheiro: Selic 13,75% → R$ 114",
          "caption": "2% ao mês = exemplo ilustrativo; Selic: Banco Central (04/11/2026)"}},
 # REENGAJE — fecha o loop 2 (a Stone)
 {"say": "Olha o peso disso numa empresa de maquininha. Na Stone, no segundo trimestre de dois mil e vinte e seis, a receita financeira, onde entra a antecipação, somou dois vírgula sete bilhões de reais. Setenta e quatro por cento de toda a receita da empresa. Três de cada quatro reais.",
  "vis": {"type": "stack", "title": "Receita da Stone no 2º tri de 2026", "parts": [["Receita financeira", 74.3, "#F2A93B", "R$ 2,67 bi — inclui antecipação"], ["Todo o resto", 25.7, "#5B8DEF", "transações, assinaturas e outras"]],
          "highlight": 0, "caption": "Fonte: StoneCo, resultados do 2º trimestre de 2026 (formulário 6-K, ago/2026)"}},
 {"say": "Agora dá para entender o tombo de dezoito de abril de dois mil e dezenove. Naquele dia, a Rede, do Itaú, anunciou que ia antecipar de graça, em dois dias, as vendas no crédito à vista de quem tinha conta no banco. E as ações da Stone caíram vinte e três vírgula sete por cento. O mercado não estava com medo de perder a maquininha. Estava com medo de perder a antecipação.",
  "vis": {"type": "ticker", "title": "O dia em que a antecipação virou arma", "date": "18/04/2019", "decimals": 1,
          "rows": [["Stone", -23.69, "Nasdaq"], ["PagSeguro", -9.74, "NYSE"]], "caption": "Fonte: IstoÉ Dinheiro (19/04/2019)"}},
 {"say": "Repara num detalhe do balanço mais recente da Stone. A receita com transações caiu trinta e cinco por cento em um ano. A receita financeira subiu dez vírgula sete. A própria empresa fala em ajustes de preço entre a taxa da maquininha e a antecipação. Traduzindo: a taxa que aparece pode até cair. A que fica escondida no prazo pode subir.",
  "vis": {"type": "ticker", "title": "Stone: 2º tri de 2026 contra 2º tri de 2025", "date": "2T26", "decimals": 1,
          "rows": [["Transações", -35.1, "a taxa que aparece"], ["Receita financeira", 10.7, "onde entra a antecipação"]],
          "caption": "Fonte: StoneCo, resultados do 2º trimestre de 2026"}},

 # ---------- PARADA 6: A PORTA ABERTA ----------
 {"say": "Parada seis: a porta. Durante anos, a agenda de recebíveis ficava presa na empresa da maquininha. Se a loja quisesse antecipar com outro banco, era difícil, porque ninguém de fora enxergava aquelas parcelas. Quem tinha a agenda, tinha o cliente.",
  "vis": {"type": "journey", "stops": STOPS, "cur": 5, "title": "A porta", "sub": "a agenda presa na maquininha"}},
 {"say": "Isso mudou em sete de junho de dois mil e vinte e um. Por regra do Banco Central, os recebíveis de cartão passaram a ser registrados em empresas chamadas registradoras. São quatro: Cerc, Núclea, B3 e a TAG, que pertence à Stone. Com o registro, qualquer instituição pode ver a agenda da loja, se ela autorizar, e oferecer um preço melhor.",
  "vis": {"type": "timeline", "even": True, "points": [["Jun/2019", "BC cria a regra do registro"], ["07/06/2021", "Registro começa a valer"], ["2022–2024", "Cancelar em 2 dias úteis"]],
          "caption": "Fontes: Banco Central (Res. CMN 4.734/2019; Res. BCB 264/2022 e 349/2023)"}},
 {"say": "E a concorrência apareceu. Segundo um levantamento da Cerc, com dados do Banco Central, o saldo de antecipação quase dobrou entre dois mil e vinte e dois e dois mil e vinte e três, chegando a noventa e sete vírgula cinco bilhões de reais. E a queda das taxas teria economizado vinte e nove bilhões de reais para o comércio só em dois mil e vinte e três.",
  "vis": {"type": "bignumber", "from": 0, "to": 29, "prefix": "R$ ", "suffix": " bi", "decimals": 0, "caption": "economia do comércio com a queda das taxas em 2023 (cálculo da Cerc)",
          "source": "Fonte: Cerc, com dados do Banco Central, via Broadcast (12/06/2024)"}},
 {"say": "Esse é o motivo de o mercado crescer tão rápido. Quando a agenda virou uma garantia que qualquer banco pode usar, antecipar ficou mais fácil, mais competitivo e mais barato para quem pesquisa. Só que nem todo mundo pesquisa.",
  "vis": {"type": "title", "title": "A agenda virou\ngarantia.", "sub": "mais competição — para quem compara preço"}},

 # ---------- A VIRADA: QUEM PAGA (~6:00) ----------
 # REENGAJE ~6:00 — a virada: quem perde
 {"say": "E aqui vem a virada. Lembra que a compra foi sem juros? Para você, foi. Mas os cento e oitenta e sete reais saíram de algum lugar. A loja que antecipa sabe que vai pagar isso. E a forma mais simples de não ter prejuízo é embutir esse custo no preço.",
  "vis": {"type": "title", "title": "\"Sem juros\"\npara quem?", "sub": "a virada"}},
 {"say": "Aí acontece uma coisa curiosa. Se a loja cobra o mesmo preço à vista e parcelado, quem paga no Pix ou no dinheiro também está pagando, sem saber, a antecipação de quem parcelou. O custo do prazo se espalha por todo mundo que compra naquela loja.",
  "vis": {"type": "compare", "left": ["Quem parcela", "12x de R$ 100", "sem juros na fatura", "recebe o prazo de graça"], "right": ["Quem paga à vista", "R$ 1.200 no Pix", "mesmo preço", "ajuda a pagar o prazo"],
          "caption": "Quando o preço é igual, o custo do prazo se espalha (análise do canal)"}},
 {"say": "E quem mais perde é o pequeno lojista que deixa a antecipação no automático e nunca compara preço. Ele não sente a taxa, porque ela não aparece como uma cobrança. Aparece como um dinheiro que simplesmente veio menor. É a taxa mais silenciosa do comércio.",
  "vis": {"type": "bullets", "title": "Quem perde nessa história", "items": ["O lojista que antecipa no automático", "Quem paga à vista pelo mesmo preço", "Quem não compara a taxa entre bancos"], "highlight": 0,
          "caption": "Análise do canal — não é recomendação financeira"}},

 # ---------- PAYOFF ----------
 {"say": "Então, para onde vão os quase duzentos reais? Para quem consegue ficar no meio do caminho entre a venda e o dinheiro: a empresa da maquininha, os bancos e quem tem dinheiro barato para adiantar. O parcelado sem juros não é de graça. É um empréstimo que o lojista faz, e que alguém cobra.",
  "vis": {"type": "cards", "title": "Quem fica com a diferença", "cards": [["1", "A maquininha", "a taxa de cada venda"], ["2", "Quem antecipa", "o desconto pelo prazo"], ["3", "Dinheiro barato", "a margem entre Selic e taxa"]],
          "highlight": 1, "caption": "Exemplo ilustrativo — taxas reais variam"}},
 {"say": "Só que existe um meio de pagamento que chega na conta da loja na hora, sem agenda, sem parcela e sem antecipação. Ele já é o jeito mais usado de pagar no Brasil, e mudou a conta de muitos bancos. No próximo episódio: como o Pix mudou os bancos, e quem perdeu dinheiro com isso.",
  "vis": {"type": "title", "title": "Próximo episódio:\ncomo o Pix mudou os bancos", "sub": "e quem perdeu dinheiro com isso"}},
]
