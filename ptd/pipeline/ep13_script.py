# EP13 — O Nubank virou banco: de onde vem o lucro recorde (e o número que preocupa)
# Estrutura NOVA: "o prédio em 5 andares" — o modelo de negócio do Nubank visto como uma construção que sobe andar por andar
# (cena nova: floor). 1º A porta (o cartão sem anuidade e os clientes), 2º O cofre (depósitos e custo do dinheiro),
# 3º A máquina (o cartão de crédito), 4º O empréstimo (pessoal, com garantia, margem), 5º A cobertura (México e Colômbia).
# Depois: "as rachaduras" (inadimplência, margem ajustada ao risco) e "a placa na porta" (a licença bancária de 13/11/2026).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação em pistas), EP12 (contrato em 5 cláusulas).
# Promessa do EP12 cumprida ("o Nubank: como um banco sem agência e sem tarifa ganha dinheiro, e de onde vem o lucro").
# Ângulo NOVO em relação ao episódio antigo sobre o Nubank (custo x receita por cliente): o balanço do 3T26 (12/11/2026)
# e a licença bancária aprovada pelo BC em 13/11/2026 — quanto do dinheiro vem de tarifa x juros, e o risco.
# Loops: (1) "quase nada vem de tarifa" -> resposta no fim do 4º andar; (2) "o número que preocupa" -> as rachaduras.
# Re-engajamentos: ~3:00 o cofre; ~6:00 as rachaduras.
# Números: Nu Holdings, resultados do 3T26 (12/11/2026), via Business Moment, Investing.com, EuQueroInvestir, Visno e MarketScreener.
# Licença: Banco Central (13/11/2026), via O Tempo/Reuters e Seu Dinheiro; 6-K de 20/07/2026 (compra do Banco Porto Real).
# Fatia de tarifas na receita (13%) e lucro por dia = CÁLCULOS do canal. Exemplo dos R$ 1.000 = ILUSTRATIVO.
TITLE = "O Nubank virou banco: de onde vem o lucro recorde (e o número que preocupa)"

FL = ["A porta: o cartão", "O cofre: depósitos", "A máquina: crédito", "O empréstimo", "A cobertura: exterior"]
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Ontem, sexta-feira, treze de novembro, o Banco Central aprovou um negócio pequeno, com uma consequência enorme. O Nubank, que passou treze anos dizendo que não era banco, recebeu o aval para comprar um banco de verdade. E, com ele, a licença para se chamar oficialmente de banco.",
  "vis": {"type": "timeline", "even": True, "points": [["2013", "nasce a fintech"], ["jul/2026", "compra anunciada"], ["13/11/2026", "aval do Banco Central"]],
          "caption": "Fonte: Banco Central, via Reuters e O Tempo (13/11/2026)"}},
 {"say": "Um dia antes, o Nubank tinha divulgado o maior lucro da sua história. Um bilhão e noventa milhões de dólares em apenas três meses. Pela conta do canal, isso dá perto de doze milhões de dólares de lucro por dia.",
  "vis": {"type": "bignumber", "from": 0, "to": 1.09, "prefix": "US$ ", "suffix": " bilhão", "decimals": 2, "caption": "lucro líquido do Nubank no 3º trimestre de 2026 (recorde)",
          "source": "Fonte: Nu Holdings, resultados do 3T26 (12/11/2026)"}},
 {"say": "E aqui está o paradoxo. A empresa nasceu prometendo acabar com tarifa e anuidade. Então, de onde vem esse dinheiro todo? A resposta curta é: quase nada vem de tarifa. E, no mesmo balanço do lucro recorde, apareceu um número que preocupa.",
  "vis": {"type": "compare", "left": ["Pergunta 1", "se não cobra tarifa,", "de onde vem", "o lucro?"], "right": ["Pergunta 2", "qual é o número", "que preocupa", "no balanço?"],
          "caption": "As duas perguntas deste episódio"}},
 {"say": "Para responder, a gente vai olhar o Nubank como um prédio. Ele foi construído andar por andar. Cada andar é um jeito de ganhar dinheiro. São cinco. E no fim, a gente desce até a fundação, para procurar as rachaduras.",
  "vis": {"type": "title", "title": "Nubank:\no prédio em 5 andares", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- 1º ANDAR: A PORTA ----------
 {"say": "Primeiro andar. A porta de entrada. Todo prédio começa por onde as pessoas entram. E a porta do Nubank foi um cartão roxo, sem anuidade, pedido pelo celular.",
  "vis": {"type": "floor", "n": 1, "label": "A PORTA", "title": "O cartão\nsem anuidade", "sub": "a isca que trouxe todo mundo", "floors": FL}},
 {"say": "A empresa foi fundada em dois mil e treze, em São Paulo, e lançou o cartão no ano seguinte. Naquela época, abrir conta ou pedir cartão quase sempre significava fila em agência, papelada e tarifa. O Nubank inverteu a lógica: primeiro, ganha o cliente. Depois, pensa em como ganhar dinheiro com ele.",
  "vis": {"type": "flow", "nodes": ["Cartão grátis", "Milhões de clientes", "Dados de uso", "Crédito sob medida"], "notes": ["sem anuidade", "custo baixo por cliente", "como cada um gasta", "onde está o lucro"], "pulse": True,
          "caption": "Análise do canal: a lógica do modelo"}},
 {"say": "E a porta funcionou. No fim de setembro de dois mil e vinte e seis, eram cento e quarenta e três milhões de clientes no total. Quase cento e vinte milhões só no Brasil. Isso é mais da metade da população do país, que o IBGE estimou em duzentos e treze milhões de pessoas.",
  "vis": {"type": "bars", "title": "Clientes do Nubank (set/2026)", "items": [["Brasil", 120.0, "#9B5DE5"], ["México", 16.6, "#F2A93B"], ["Colômbia", 6.1, "#3AC47D"]], "suffix": " mi", "decimals": 1,
          "caption": "Fonte: Nu Holdings, 3T26 (143 milhões no total) · População: IBGE, estimativa de 2025"}},
 {"say": "Mais importante do que ter o cliente é ele usar. E, segundo o balanço, a taxa de atividade no Brasil bateu recorde: oitenta e seis vírgula três por cento dos clientes usaram a conta no mês. Um banco não ganha dinheiro com cliente parado. E o Nubank tem pouquíssimo cliente parado.",
  "vis": {"type": "bignumber", "from": 0, "to": 86.3, "suffix": "%", "decimals": 1, "caption": "dos clientes no Brasil estão ativos (3º tri de 2026, recorde)",
          "source": "Fonte: Nu Holdings, 3T26, via EuQueroInvestir"}},

 # ---------- 2º ANDAR: O COFRE ----------
 {"say": "Segundo andar. O cofre. Todo banco precisa de dinheiro para emprestar. E o dinheiro mais barato que existe é o dos próprios clientes.",
  "vis": {"type": "floor", "n": 2, "label": "O COFRE", "title": "O dinheiro\nque dorme na conta", "sub": "a matéria-prima do banco", "floors": FL}},
 # REENGAJE ~3:00
 {"say": "Os depósitos dos clientes do Nubank somaram quarenta e sete e meio bilhões de dólares no terceiro trimestre. Trinta e oito vírgula seis bilhões no Brasil. E aqui tem um detalhe que pouca gente percebe: o Nubank paga, em média, oitenta e sete por cento do CDI por esse dinheiro.",
  "vis": {"type": "bars", "title": "Depósitos no Nubank (3º tri de 2026)", "items": [["Brasil", 38.6, "#9B5DE5"], ["México", 5.3, "#F2A93B"], ["Colômbia", 3.5, "#3AC47D"]], "prefix": "US$ ", "suffix": " bi", "decimals": 1,
          "caption": "Fonte: Nu Holdings, 3T26 (total de US$ 47,5 bi; custo médio de 87% do CDI)"}},
 {"say": "Como assim, se tanta gente recebe cem por cento do CDI? Porque é uma média. Tem dinheiro parado na conta, rendendo menos ou nada, e tem dinheiro nas caixinhas, rendendo mais. No total, o custo fica abaixo da taxa que os bancos cobram entre si. E é com esse dinheiro, mais barato que o do mercado, que o Nubank empresta.",
  "vis": {"type": "flow", "nodes": ["Seu depósito", "Custo: 87% do CDI", "Vira empréstimo", "Cobra bem mais"], "notes": ["na conta e nas caixinhas", "média paga pelo banco", "cartão e crédito pessoal", "a diferença é a margem"], "pulse": True,
          "caption": "Fonte do custo: Nu Holdings, 3T26 · esquema: análise do canal"}},
 {"say": "Vamos a um exemplo do canal, só para entender a mecânica. Mil reais depositados, que custam ao banco algo perto de doze por cento ao ano. Se esses mesmos mil reais viram crédito a três ou quatro por cento ao mês, a diferença é enorme. É essa diferença que os bancos chamam de spread. E é o coração do negócio.",
  "vis": {"type": "compare", "left": ["O que o banco paga", "R$ 1.000 depositados", "~12% ao ano", "custo do dinheiro"], "right": ["O que o banco cobra", "R$ 1.000 emprestados", "3% a 4% ao mês", "receita de juros"],
          "caption": "Exemplo ilustrativo do canal — sem considerar calotes, impostos e custos"}},

 # ---------- 3º ANDAR: A MÁQUINA ----------
 {"say": "Terceiro andar. A máquina. Aquele cartão grátis da porta de entrada voltou, só que agora do outro lado do balcão.",
  "vis": {"type": "floor", "n": 3, "label": "A MÁQUINA", "title": "O cartão\nde crédito", "sub": "o grátis que gera juros", "floors": FL}},
 {"say": "A carteira de crédito do Nubank chegou a quarenta e um vírgula seis bilhões de dólares. E o cartão é, de longe, a maior parte: vinte e sete vírgula dois bilhões. Quase dois terços de tudo o que o Nubank empresta está no cartão de crédito.",
  "vis": {"type": "stack", "title": "Carteira de crédito do Nubank: US$ 41,6 bi", "parts": [["Cartão", 65.4, "#9B5DE5", "US$ 27,2 bi\ncartão"], ["Pessoal", 26.4, "#F2A93B", "US$ 11 bi\nsem garantia"], ["Garantia", 8.2, "#3AC47D", "US$ 3,4 bi"]], "highlight": 0,
          "caption": "Fonte: Nu Holdings, 3T26 · percentuais: cálculo do canal"}},
 {"say": "O cartão ganha dinheiro de dois jeitos. Primeiro, a cada compra, a loja paga uma taxa, e uma parte dela fica com quem emitiu o cartão. É o caminho dos três reais da maquininha que a gente já mostrou aqui no canal. Segundo, e principalmente, quando o cliente parcela a fatura ou cai no rotativo. Aí entram os juros.",
  "vis": {"type": "cards", "title": "Como o cartão dá dinheiro", "cards": [["1", "Intercâmbio", "a loja paga\nem cada compra"], ["2", "Parcelamento", "juros da fatura\nparcelada"], ["3", "Rotativo", "o juro mais caro\ndo país"]],
          "highlight": 2, "caption": "O rotativo foi o tema do EP10 · a taxa da maquininha, do EP03"}},
 {"say": "E esse andar não para de crescer. Segundo o balanço, a carteira de cartões cresceu trinta e dois por cento em um ano. Um relatório do BTG, com dados da Card Monitor, mostra que o Nubank cresce mais rápido que o mercado, enquanto os quatro grandes bancos tradicionais perderam espaço no cartão.",
  "vis": {"type": "bignumber", "from": 0, "to": 32, "suffix": "%", "decimals": 0, "caption": "de crescimento da carteira de cartões em um ano",
          "source": "Fonte: Nu Holdings, 3T26 (câmbio constante) · BTG Pactual / Card Monitor (2T26)"}},

 # ---------- 4º ANDAR: O EMPRÉSTIMO ----------
 {"say": "Quarto andar. O empréstimo. Depois de conhecer o cliente pelo cartão, o banco sabe quanto ele ganha, como ele gasta e se paga em dia. E aí oferece o produto que mais dá dinheiro por real emprestado.",
  "vis": {"type": "floor", "n": 4, "label": "O EMPRÉSTIMO", "title": "Crédito\npessoal", "sub": "o andar que mais cresce", "floors": FL}},
 {"say": "O empréstimo pessoal sem garantia chegou a onze bilhões de dólares, e cresceu trinta e nove por cento em um ano. É o andar que mais cresce no prédio. Já o crédito com garantia, onde entram o consignado e a antecipação do FGTS, somou três vírgula quatro bilhões.",
  "vis": {"type": "bars", "title": "Crescimento em um ano, por produto", "items": [["Pessoal sem garantia", 39, "#F2A93B"], ["Cartão", 32, "#9B5DE5"], ["Com garantia", 23, "#3AC47D"]], "suffix": "%", "decimals": 0,
          "caption": "Fonte: Nu Holdings, 3T26 (câmbio constante) · o consignado foi o tema do EP12"}},
 {"say": "Juntando tudo, o balanço mostra uma margem financeira de vinte e dois e meio por cento. Em português claro: para cada cem dólares que o Nubank tem emprestados ou aplicados, sobram, ao longo de um ano, uns vinte e dois e meio depois de pagar o custo do dinheiro. É uma das margens mais altas do mundo dos bancos.",
  "vis": {"type": "bignumber", "from": 0, "to": 22.5, "suffix": "%", "decimals": 1, "caption": "margem financeira líquida (NIM) no 3º trimestre de 2026",
          "source": "Fonte: Nu Holdings, 3T26, via MarketScreener e Yahoo Finance"}},
 {"say": "E agora a resposta da primeira pergunta. No trimestre, as tarifas e comissões, que incluem aquela taxa que a loja paga em cada compra, somaram oitocentos e dezessete milhões de dólares. Pela conta do canal, isso é só uns treze por cento de uma receita total de seis vírgula três bilhões. Os outros oitenta e sete por cento vêm, basicamente, de juros.",
  "vis": {"type": "stack", "title": "De onde vem a receita do Nubank (3T26)", "parts": [["Juros", 87, "#9B5DE5", "~87%\njuros e outras receitas financeiras"], ["Tarifas", 13, "#F2A93B", "~13%\ntarifas"]], "highlight": 0,
          "caption": "Fonte: Nu Holdings, 3T26 (US$ 817 mi de tarifas e comissões; receita de US$ 6,3 bi) · % = cálculo do canal"}},
 {"say": "Ou seja: o Nubank nunca prometeu não ganhar dinheiro. Ele prometeu não cobrar tarifa. E cumpriu, em grande parte. O lucro não vem de quem usa a conta e paga a fatura em dia. Vem de quem toma crédito.",
  "vis": {"type": "title", "title": "Não é a tarifa.\nÉ o crédito.", "sub": "análise do canal"}},

 # ---------- 5º ANDAR: A COBERTURA ----------
 {"say": "Quinto andar. A cobertura. Com o prédio cheio no Brasil, o Nubank começou a construir para fora.",
  "vis": {"type": "floor", "n": 5, "label": "A COBERTURA", "title": "México e\nColômbia", "sub": "o mesmo prédio, em outro país", "floors": FL}},
 {"say": "No México, já são dezesseis vírgula seis milhões de clientes. E lá o Nubank já opera como banco. Só no primeiro trimestre com essa licença, ganhou oitocentos e setenta mil clientes. Na Colômbia, são seis vírgula um milhões. Os depósitos fora do Brasil já passam de oito bilhões de dólares.",
  "vis": {"type": "cards", "title": "Fora do Brasil (3º tri de 2026)", "cards": [["MX", "16,6 mi", "clientes\nno México"], ["+", "870 mil", "novos no 1º tri\ncomo banco"], ["CO", "6,1 mi", "clientes\nna Colômbia"]],
          "highlight": 0, "caption": "Fonte: Nu Holdings, 3T26, via Business Moment e EuQueroInvestir"}},
 {"say": "A aposta é repetir a receita: entrar pelo cartão, juntar depósitos, e só depois vender crédito. O risco é que cada país tem seus juros, suas regras e seus caloteiros. O que deu certo no Brasil não tem garantia de dar certo em outro lugar.",
  "vis": {"type": "compare", "left": ["A aposta", "mesma receita", "cartão, depois crédito", "custo baixo"], "right": ["O risco", "outras regras", "outros juros", "outro calote"],
          "caption": "Análise do canal"}},

 # ---------- AS RACHADURAS ----------
 # REENGAJE ~6:00
 {"say": "Prédio de pé. Agora vamos descer até a fundação e procurar as rachaduras. E aqui está o número que preocupa.",
  "vis": {"type": "title", "title": "As rachaduras", "sub": "o número que preocupa"}},
 {"say": "No mesmo balanço do lucro recorde, a inadimplência subiu. Os empréstimos com mais de noventa dias de atraso passaram de seis vírgula nove por cento para sete vírgula três por cento da carteira, em apenas um trimestre. E os atrasos mais curtos, de quinze a noventa dias, também subiram, para quatro vírgula nove por cento.",
  "vis": {"type": "bars", "title": "Atraso acima de 90 dias (% da carteira)", "items": [["2º tri 2026", 6.9, "#F2A93B"], ["3º tri 2026", 7.3, "#E06C5A"]], "suffix": "%", "decimals": 1,
          "caption": "Fonte: Nu Holdings, 3T26, via EuQueroInvestir e Visno (15 a 90 dias: 4,9%)"}},
 {"say": "Por que isso importa? Porque a margem gorda do quarto andar só existe enquanto o cliente paga. Quando o calote sobe, o banco precisa reservar mais dinheiro para cobrir as perdas. Por isso, a margem ajustada ao risco, que já desconta o calote, caiu de doze vírgula quatro para doze vírgula um por cento.",
  "vis": {"type": "compare", "left": ["Margem cheia", "22,5%", "antes dos calotes", "o que o crédito rende"], "right": ["Ajustada ao risco", "12,1%", "depois dos calotes", "o que sobra de verdade"],
          "caption": "Fonte: Nu Holdings, 3T26 (12,4% no 2T26)"}},
 {"say": "Repare na conta. Quase metade da margem vai embora com calote. É o preço de emprestar caro para muita gente que não tinha crédito antes. E com a Selic ainda alta, em treze vírgula setenta e cinco por cento, o bolso do cliente fica mais apertado. A rachadura não derruba o prédio. Mas é ela que o mercado vai vigiar nos próximos trimestres.",
  "vis": {"type": "bullets", "title": "O que vigiar", "items": ["Atraso acima de 90 dias", "Margem ajustada ao risco", "Selic alta pesa no bolso", "Crescimento x qualidade"], "highlight": 0,
          "caption": "Análise do canal · Selic: Copom (04/11/2026)"}},

 # ---------- A PLACA NA PORTA ----------
 {"say": "E então, a licença de ontem. Se o Nubank já era tão grande, por que precisou comprar um banco?",
  "vis": {"type": "title", "title": "A placa\nna porta", "sub": "por que o Nubank precisou virar banco"}},
 {"say": "Até agora, o Nubank funcionava com outras licenças: instituição de pagamento, financeira e corretora. Só que uma regra nova do Banco Central e do Conselho Monetário Nacional, a Resolução Conjunta número dezessete, proibiu quem não é banco de usar palavras como banco ou bank no nome e na marca.",
  "vis": {"type": "cards", "title": "As licenças do Nubank no Brasil", "cards": [["1", "Pagamento", "instituição\nde pagamento"], ["2", "Financeira", "crédito,\nfinanciamento"], ["3", "Corretora", "títulos e\ninvestimentos"]],
          "highlight": 1, "caption": "A 4ª, de banco, veio com a compra do Banco Porto Real (aval do BC em 13/11/2026)"}},
 {"say": "A solução foi comprar um banco pequeno que já tinha a licença: o Banco Porto Real de Investimentos, do estado do Rio de Janeiro, fundado em mil novecentos e noventa e dois. Em março, ele tinha só trinta e dois milhões de reais em ativos. Ou seja: o Nubank não comprou clientes, nem agências. Comprou a placa na porta.",
  "vis": {"type": "compare", "left": ["Banco Porto Real", "fundado em 1992", "R$ 32,1 mi em ativos", "uma licença"], "right": ["Nubank", "143 mi de clientes", "US$ 47,5 bi em depósitos", "a marca"],
          "caption": "Fontes: Nu Holdings (6-K, 20/07/2026); BC (13/11/2026), via Reuters e O Tempo"}},
 {"say": "Para o cliente, segundo a própria empresa, nada muda: mesmo aplicativo, mesma marca. E o Nubank diz que a licença não exige capital extra. A mudança é mais simbólica do que prática. Mas o símbolo é forte. A fintech que nasceu contra os bancos agora é, oficialmente, um deles.",
  "vis": {"type": "title", "title": "A fintech que nasceu\ncontra os bancos", "sub": "agora é um deles"}},

 # ---------- FECHAMENTO ----------
 {"say": "Então, vamos juntar as peças. A porta é o cartão grátis. O cofre é o dinheiro barato dos depósitos. A máquina é o cartão de crédito. O empréstimo é o andar que mais rende. E a cobertura é o exterior. Quase todo o lucro vem de um lugar só: a diferença entre o que o banco paga e o que ele cobra.",
  "vis": {"type": "bullets", "title": "O prédio inteiro", "items": ["Porta: cartão sem anuidade", "Cofre: depósitos a 87% do CDI", "Máquina e empréstimo: juros", "Cobertura: México e Colômbia"], "highlight": 2}},
 {"say": "E a lição vale para qualquer banco, digital ou não. Quando um serviço financeiro é grátis, vale perguntar onde o banco ganha. Quase sempre, a resposta está no crédito. Se você paga a fatura em dia, você é o cliente que custa pouco. Se você parcela e entra no rotativo, você é o cliente que paga o prédio.",
  "vis": {"type": "compare", "left": ["Paga em dia", "usa o grátis", "custa pouco", "não paga juros"], "right": ["Parcela e atrasa", "toma crédito caro", "gera os juros", "paga o prédio"],
          "caption": "Análise do canal"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira, nem de investimento. É só a planta do prédio, para você entender como o dinheiro se move.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E já que a palavra de hoje foi spread, a diferença entre o que o banco paga e o que ele cobra, no próximo episódio vamos atrás dela. Por que o juro no Brasil é um dos mais altos do mundo, mesmo quando a Selic cai? Quem fica com essa diferença? É o spread bancário, explicado.",
  "vis": {"type": "title", "title": "Próximo: o spread", "sub": "por que o juro no Brasil é tão alto"}},
]
