# EP05 — A guerra das maquininhas: Stone x PagSeguro x Cielo (quem ganhou?)
# Estrutura NOVA: "luta em 4 rounds" (abertura 2010 -> desafiantes 2012-2018 -> contra-ataque dos bancos 2019 -> Pix)
# + placar + payoff "quem ganhou" (nenhuma maquininha). Cenas novas: round, ticker, scoreboard.
# Diferente do EP02 (investigação), EP03 (autópsia de uma taxa) e EP04 (extrato de um cliente).
# Loops: (1) quem ganhou -> cena 27; (2) o inimigo inesperado -> round 4; (3) quem baixou a taxa -> rounds + payoff.
TITLE = "A guerra das maquininhas: Stone x PagSeguro x Cielo"

WIN = [["1", "O lojista", "taxa média do crédito\ncaiu quase 30%"], ["2", "O emissor", "intercâmbio\nem alta"],
       ["3", "Quem virou banco", "conta, crédito\ne depósitos"]]

SCENES = [
 # ---------- GANCHO ----------
 {"say": "Em dois mil e nove, a cada cem reais vendidos no cartão de crédito, o lojista pagava, em média, dois reais e noventa e nove de taxa. Hoje, paga dois e onze. Quem derrubou esse preço foi uma guerra.",
  "vis": {"type": "bignumber", "from": 2.99, "to": 2.11, "suffix": "%", "decimals": 2, "caption": "taxa média paga pelo lojista no crédito: 2009 → 1º semestre de 2026",
          "source": "Fonte: Banco Central (Relatório de Cartões, adendo 2010; Estatísticas de Pagamentos de Varejo, 1º sem/2026)"}},
 {"say": "Uma briga de mais de quinze anos entre Cielo, Stone e PagSeguro, com os grandes bancos no meio. A Cielo chegou a ter cerca de metade do mercado e terminou fora da bolsa. Até o fim do vídeo, você vai saber quem ganhou essa guerra. E a resposta não é nenhuma das três empresas.",
  "vis": {"type": "title", "title": "Uma guerra.\nTrês exércitos.", "sub": "Cielo · Stone · PagSeguro — e os bancos no meio"}},
 {"say": "A história vem em quatro rounds: a abertura do mercado, a chegada dos desafiantes, o contra-ataque dos bancos e o inimigo que ninguém esperava. No fim, o placar.",
  "vis": {"type": "title", "title": "A guerra das\nmaquininhas", "sub": "em 4 rounds — POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- ANTES DA GUERRA ----------
 {"say": "Antes da guerra, o mercado era um duopólio com uma regra curiosa. A VisaNet, que depois virou Cielo, era a credenciadora exclusiva da Visa. A Redecard, hoje Rede, era a casa da Mastercard. Na prática, quem queria aceitar as duas bandeiras costumava ter duas maquininhas no balcão. E as duas empresas tinham grandes bancos como donos.",
  "vis": {"type": "compare", "left": ["VisaNet", "hoje: Cielo", "exclusiva da Visa", "donos: Bradesco e BB"], "right": ["Redecard", "hoje: Rede", "casa da Mastercard", "dono: Itaú"],
          "caption": "Antes de julho de 2010 — composição acionária: Banco Central, Relatório de Cartões (adendo 2010)"}},
 {"say": "Para quem estava dentro, era um negócio espetacular. Em dois mil e nove, ano em que abriu capital na bolsa, a Cielo tinha margem Ebitda de sessenta e sete vírgula seis por cento. Traduzindo: de cada cem reais de receita, quase sessenta e oito sobravam como resultado operacional, antes de juros, impostos e depreciação.",
  "vis": {"type": "bignumber", "from": 0, "to": 67.6, "suffix": "%", "decimals": 1, "caption": "margem Ebitda da Cielo em 2009, ano em que abriu capital",
          "source": "Fonte: Mercado&Consumo (16/08/2024), com dados da Cielo"}},

 # ---------- ROUND 1 ----------
 {"say": "Round um. Dois mil e dez. O Banco Central e os órgãos de defesa da concorrência vinham apontando os problemas desse modelo fechado. Em primeiro de julho de dois mil e dez, a Visa deixou de ter um credenciador exclusivo no Brasil. A partir daí, a mesma maquininha podia aceitar várias bandeiras.",
  "vis": {"type": "round", "n": 1, "year": "1º DE JULHO DE 2010", "left": "Duopólio", "right": "Multibandeira", "sub": "o fim da exclusividade",
          "caption": "Fonte: Banco Central, Relatório de Cartões (adendo 2010)"}},
 {"say": "No mesmo ano, o Santander comprou a GetNet e passou a disputar lojistas com condições especiais, como isenção do aluguel da maquininha. E o primeiro efeito apareceu rápido: a taxa média do crédito caiu de dois vírgula noventa e nove para dois vírgula oitenta e quatro por cento. Parece pouco. Mas, num mercado de bilhões, cada décimo é muito dinheiro.",
  "vis": {"type": "bullets", "title": "Round 1 — o que mudou", "items": ["Fim da exclusividade da Visa", "Santander compra a GetNet", "Isenção de aluguel vira arma", "Crédito: 2,99% → 2,84% (2009 → 2010)"], "highlight": 3,
          "caption": "Fontes: Banco Central (adendo 2010); Capital Aberto (18/01/2019)"}},
 {"say": "Só que, para os dois gigantes, pouca coisa mudou no começo. O próprio Banco Central registrou que a participação das duas maiores credenciadoras ficou praticamente igual em dois mil e dez. Abrir a porta não bastava. Faltava alguém disposto a entrar brigando.",
  "vis": {"type": "title", "title": "Abrir a porta\nnão bastava.", "sub": "faltava um desafiante"}},

 # ---------- ROUND 2 ----------
 {"say": "Round dois. Os desafiantes. Em dois mil e doze, André Street e Eduardo Pontes fundaram a Stone, mirando lojas pequenas e médias. Do outro lado, a PagSeguro, do grupo UOL, que nasceu processando pagamentos na internet, decidiu ir atrás de quem os gigantes praticamente ignoravam: o microempreendedor, o ambulante, a cabeleireira, o taxista.",
  "vis": {"type": "round", "n": 2, "year": "2012 — 2018", "left": "Stone", "right": "PagSeguro", "sub": "os desafiantes chegam ao balcão"}},
 {"say": "A arma da PagSeguro foi mudar o jeito de cobrar. Em vez de alugar a maquininha, ela vendia o aparelho. Em janeiro de dois mil e dezenove, segundo a revista Capital Aberto, o aluguel de uma maquininha da Cielo chegava a cento e setenta e nove reais e noventa por mês a partir do quarto mês. A maquininha mais simples da PagSeguro custava cinquenta e oito e oitenta, uma vez só. Para quem vende pouco, essa conta decide tudo.",
  "vis": {"type": "compare", "left": ["Alugar", "Cielo (jan/2019)", "R$ 179,90 por mês", "a partir do 4º mês"], "right": ["Comprar", "PagSeguro (jan/2019)", "a partir de R$ 58,80", "uma vez só, sem aluguel"],
          "caption": "Fonte: Capital Aberto, \"Guerra das maquininhas ameaça Cielo\" (18/01/2019)"}},
 {"say": "E decidiu. Segundo um levantamento do Sebrae citado pela mesma reportagem, entre os pequenos negócios que aceitavam cartão, a fatia de Cielo e Redecard caiu de oitenta e seis para quarenta e seis por cento entre dois mil e dezesseis e dois mil e dezoito. Em dois anos, os gigantes perderam quase metade do pequeno varejo.",
  "vis": {"type": "bignumber", "from": 86, "to": 46, "suffix": "%", "decimals": 0, "caption": "fatia de Cielo + Redecard entre pequenos negócios: 2016 → 2018",
          "source": "Fonte: Sebrae, via Capital Aberto (18/01/2019)"}},
 {"say": "Em dois mil e dezoito, os desafiantes foram buscar munição. Em janeiro, a PagSeguro abriu capital na bolsa de Nova York e levantou dois vírgula três bilhões de dólares. Em outubro, foi a vez da Stone, na Nasdaq, com a Berkshire Hathaway, de Warren Buffett, entre os investidores. Dinheiro para bancar preço baixo e conquistar clientes.",
  "vis": {"type": "timeline", "even": True, "points": [["2012", "Stone é fundada"], ["Jan/2018", "PagSeguro na NYSE: US$ 2,3 bi"], ["Out/2018", "Stone na Nasdaq"]],
          "caption": "Dinheiro para a guerra de preços", "_src": "Renaissance Capital (24/01/2018); Seu Dinheiro (16/10/2018)"}},
 # REENGAJE ~3:00 — o número mais absurdo até aqui: a queda da Cielo
 {"say": "E o efeito na Cielo foi brutal. Nos doze meses até janeiro de dois mil e dezenove, as ações caíram cinquenta e um por cento. O lucro do terceiro trimestre de dois mil e dezoito veio vinte por cento menor. A explicação da própria empresa: menos receita com aluguel de maquininhas e preços mais baixos num mercado mais competitivo. A resposta foi lançar uma marca para pequenos negócios, a Stelo, com preços parecidos com os da PagSeguro. Ou seja: a líder passou a brigar com as armas do inimigo.",
  "vis": {"type": "ticker", "title": "Round 2 — o estrago na Cielo", "date": "2018–2019", "decimals": 1,
          "rows": [["Ação da Cielo", -51.0, "12 meses até 15/01/2019"], ["Lucro do 3º tri", -20.1, "3T18 contra 3T17"]],
          "caption": "Fonte: Capital Aberto (18/01/2019), com dados da Economatica e da Cielo"}},

 # ---------- ROUND 3 ----------
 {"say": "Round três. Dois mil e dezenove. Quando parecia que a briga era só entre a Cielo e os novatos, um banco entrou de vez no ringue. No dia dezoito de abril, a Rede, do Itaú, anunciou que ia antecipar de graça, em dois dias, o dinheiro das vendas no crédito à vista para lojistas com conta no Itaú. Normalmente, esse dinheiro levava cerca de um mês para cair. E quem quisesse antes pagava uma taxa.",
  "vis": {"type": "round", "n": 3, "year": "18 DE ABRIL DE 2019", "left": "Rede (Itaú)", "right": "Todo o resto", "sub": "antecipação de graça para quem tem conta no banco",
          "caption": "Fonte: IstoÉ Dinheiro (19/04/2019)"}},
 {"say": "O mercado entendeu o recado na hora. Naquele mesmo dia, as ações da Stone caíram vinte e três vírgula sete por cento em Nova York. As da PagSeguro, nove vírgula sete. As da Cielo, sete vírgula três. Tudo por causa de uma taxa que a maioria das pessoas nem sabe que existe.",
  "vis": {"type": "ticker", "title": "O dia em que a guerra mudou", "date": "18/04/2019", "decimals": 1,
          "rows": [["Stone", -23.69, "Nasdaq"], ["PagSeguro", -9.74, "NYSE"], ["Cielo", -7.3, "B3"]],
          "caption": "Fonte: IstoÉ Dinheiro (19/04/2019)"}},
 {"say": "Por que doeu tanto? Porque antecipar recebíveis é uma fonte importante de receita para as credenciadoras. O lojista vende parcelado ou no crédito, só receberia depois de trinta dias, pede o dinheiro antes e paga por isso. Um banco grande, com muito dinheiro em caixa, consegue abrir mão dessa receita. Quem precisa captar no mercado tem mais dificuldade. Tanto que o Cade, o órgão de defesa da concorrência, abriu um procedimento para apurar se a vantagem dada só a clientes do Itaú prejudicava os concorrentes.",
  "vis": {"type": "flow", "nodes": ["Venda no crédito", "Espera ~30 dias", "Antecipa", "Paga a taxa"], "notes": ["o lojista vende", "o prazo normal", "pede o dinheiro antes", "receita da maquininha"],
          "caption": "A Rede zerou essa taxa — e o Cade foi investigar"}},
 {"say": "Esse foi o momento em que a guerra mudou de natureza. A maquininha deixou de ser o produto e virou a porta de entrada. Quem tinha conta, crédito e dinheiro barato ganhou vantagem. E os desafiantes aprenderam a lição: começaram a virar bancos também.",
  "vis": {"type": "title", "title": "A maquininha virou\nporta de entrada.", "sub": "o produto passou a ser a conta e o crédito"}},
 {"say": "Hoje, a PagSeguro se apresenta como PagBank e soma trinta e quatro milhões de clientes. A Stone tem quatro vírgula oito milhões de clientes ativos e dez vírgula oito bilhões de reais em depósitos. As duas oferecem conta, cartão e crédito para o lojista. A maquininha é só a primeira porta da casa.",
  "vis": {"type": "compare", "left": ["Stone", "4,8 mi de clientes ativos", "R$ 10,8 bi em depósitos", "conta, cartão e crédito"], "right": ["PagBank", "34,1 mi de clientes", "ex-PagSeguro", "conta, cartão e crédito"],
          "caption": "Fontes: StoneCo e PagBank, resultados do 2º trimestre de 2026 (agosto/2026)"}},

 # ---------- ROUND 4 ----------
 {"say": "Round quatro. O inimigo que ninguém esperava. Em novembro de dois mil e vinte, o Banco Central lançou o Pix. Ele não é uma empresa, não aluga maquininha e não cobra nada da pessoa física. Mas disputa exatamente o mesmo momento: a hora de pagar.",
  "vis": {"type": "round", "n": 4, "year": "NOVEMBRO DE 2020", "left": "Maquininhas", "right": "Pix", "sub": "o inimigo que ninguém esperava"}},
 {"say": "No primeiro semestre de dois mil e vinte e seis, o Pix respondeu por cinquenta e cinco vírgula dois por cento de todas as transações de pagamento do país. Foram quase quarenta e quatro bilhões de operações em seis meses. Os cartões, somados, ficaram com trinta vírgula oito por cento.",
  "vis": {"type": "bignumber", "from": 0, "to": 55.2, "suffix": "%", "decimals": 1, "caption": "fatia do Pix nas transações de pagamento (1º sem/2026) — cartões: 30,8%",
          "source": "Fonte: Banco Central, Estatísticas de Pagamentos de Varejo e de Cartões, 1º sem/2026 (via TI Inside, 27/10/2026)"}},
 {"say": "E quem mais sente é o débito, que funciona quase como o Pix: o dinheiro sai na hora da conta. Em dois mil e vinte e cinco, segundo a Abecs, os pagamentos com cartão de crédito cresceram catorze vírgula cinco por cento. Os de débito, só zero vírgula dois.",
  "vis": {"type": "bars", "title": "Crescimento dos pagamentos com cartão em 2025", "items": [["Crédito", 14.5, "#3AC47D"], ["Pré-pago", 4.4, "#5B8DEF"], ["Débito", 0.2, "#E06C5A"]],
          "suffix": "%", "decimals": 1, "caption": "Fonte: Abecs, balanço de 2025 (via Mercado&Consumo, 11/02/2026)"}},
 # REENGAJE ~6:00 — a virada: a maquininha aceita o concorrente
 {"say": "E isso já aparece no balanço das maquininhas. No segundo trimestre de dois mil e vinte e seis, o volume de cartões na Stone caiu três vírgula um por cento em um ano. Já o volume de Pix por QR Code, na própria Stone, cresceu quarenta e quatro vírgula três por cento. Repara na ironia: para não perder o cliente, a maquininha passou a aceitar o concorrente.",
  "vis": {"type": "ticker", "title": "Stone: cartão x Pix na maquininha", "date": "2º tri 2026", "decimals": 1,
          "rows": [["Pix por QR Code", 44.3, "R$ 30,7 bi no trimestre"], ["Volume com cartões", -3.1, "R$ 111,5 bi no trimestre"]],
          "caption": "Variação contra o 2º trimestre de 2025 — Fonte: StoneCo, resultado do 2º trimestre de 2026"}},

 # ---------- PLACAR ----------
 {"say": "Então vamos ao placar. Num levantamento do UBS BB com dados de janeiro de dois mil e vinte e seis, a Rede aparecia com dezoito por cento do volume. A Cielo e o PagBank, com dezessete cada. A Stone, com quinze. E o Mercado Pago, que mais cresceu, com nove. A Cielo, que já teve cerca de metade do mercado, hoje divide o topo com mais três.",
  "vis": {"type": "scoreboard", "title": "O placar: fatia do volume (jan/2026)", "highlight": 1,
          "cols": [["Rede", 18, "#5B8DEF"], ["Cielo", 17, "#F2A93B"], ["PagBank", 17, "#3AC47D"], ["Stone", 15, "#3AC47D"], ["M. Pago", 9, "#5B8DEF"], ["GetNet", 5, "#7887A0"]],
          "caption": "Fonte: UBS BB, via Let's Money (21/03/2026). \"Cerca de metade\": InvestNews (26/06/2025)"}},
 {"say": "E a Cielo saiu da bolsa. Em agosto de dois mil e vinte e quatro, Banco do Brasil e Bradesco compraram as ações que estavam no mercado, a cinco reais e oitenta e dois cada, num leilão de quatro vírgula três bilhões de reais. Um preço cerca de oitenta por cento abaixo do pico da ação, em dois mil e treze. E aquela margem de sessenta e sete por cento? No segundo trimestre de dois mil e vinte e quatro, estava em vinte e nove vírgula três.",
  "vis": {"type": "bignumber", "from": 67.6, "to": 29.3, "suffix": "%", "decimals": 1, "caption": "margem Ebitda da Cielo: 2009 → 2º trimestre de 2024 (saída da bolsa: 15/08/2024)",
          "source": "Fontes: Mercado&Consumo (16/08/2024); InvestNews (26/06/2025)"}},
 {"say": "Para ter uma ideia da virada: no terceiro trimestre de dois mil e dezoito, a Cielo movimentou cento e cinquenta vírgula sete bilhões de reais em três meses, e a PagSeguro, vinte vírgula três. No segundo trimestre de dois mil e vinte e seis, a Stone movimentou cento e quarenta e dois bilhões, e o PagBank, cento e trinta e três. Em oito anos, cada desafiante chegou perto do tamanho que a líder tinha.",
  "vis": {"type": "bars", "title": "Volume em 3 meses: antes e depois", "items": [["Cielo 3T18", 150.7, "#F2A93B"], ["PagSeguro 3T18", 20.3, "#7887A0"], ["Stone 2T26", 142.2, "#3AC47D"], ["PagBank 2T26", 133.4, "#3AC47D"]],
          "prefix": "R$ ", "suffix": " bi", "decimals": 1, "caption": "Fontes: Capital Aberto (18/01/2019); StoneCo e PagBank, 2º trimestre de 2026"}},

 # ---------- QUEM GANHOU (payoff) ----------
 {"say": "Agora, a resposta prometida: quem ganhou a guerra? Olha a conta de uma venda de cem reais no crédito, com as médias do Banco Central do primeiro semestre de dois mil e vinte e seis. O lojista paga dois reais e onze de taxa. Desse total, cerca de um real e setenta é a tarifa de intercâmbio, que vai para o banco que emitiu o cartão. Sobram uns quarenta centavos para dividir entre a maquininha e a bandeira. É uma aproximação nossa, feita com médias, mas mostra a proporção.",
  "vis": {"type": "receipt", "title": "Para onde vai a taxa de uma venda de R$ 100", "head": "VENDA DE R$ 100 · CRÉDITO",
          "lines": [["Taxa do lojista", "R$ 2,11", "#C0503C"], ["Intercâmbio (emissor)", "− R$ 1,70", "#5B8DEF"]], "total": ["Sobra*", "≈ R$ 0,41"],
          "caption": "*dividida entre maquininha e bandeira — médias do Banco Central, 1º sem/2026; divisão aproximada (cálculo do canal)"}},
 {"say": "E a tendência é clara. Entre os primeiros semestres de dois mil e vinte e quatro e de dois mil e vinte e seis, a taxa média do lojista no crédito caiu de dois vírgula vinte e seis para dois vírgula onze por cento. No mesmo período, o intercâmbio subiu de um vírgula sessenta e quatro para um vírgula setenta, puxado em parte pelos cartões premium, segundo o Banco Central. O preço final cai, a fatia do emissor cresce, e quem fica espremido no meio é a maquininha.",
  "vis": {"type": "compare", "left": ["Taxa do lojista", "1º sem 2024: 2,26%", "1º sem 2025: 2,24%", "1º sem 2026: 2,11%"], "right": ["Intercâmbio", "2024: 1,64%", "2025: 1,66%", "2026: 1,70%"],
          "caption": "Crédito, médias do Banco Central (Estatísticas de Pagamentos de Varejo, 1º sem/2026)"}},
 {"say": "Então, na nossa leitura, essa guerra teve três vencedores, e nenhum deles é uma maquininha. Primeiro, o lojista: a taxa média do crédito caiu quase trinta por cento desde dois mil e nove. Segundo, os bancos que emitem cartões, que ficam com uma fatia cada vez maior de cada venda. Terceiro, quem entendeu cedo que a maquininha era só a porta de entrada e virou banco.",
  "vis": {"type": "cards", "title": "Quem ganhou a guerra", "cards": WIN, "highlight": -1, "caption": "2,99% → 2,11% = queda de 29% (cálculo do canal)"}},
 {"say": "E o perdedor também fica claro: o modelo antigo, o de cobrar caro pelo aluguel e pela taxa de quem não tinha opção. Isso não é recomendação de nenhuma empresa, é só a leitura do mercado. A taxa da maquininha virou a parte mais barata da conta. O dinheiro de verdade foi para outro lugar.",
  "vis": {"type": "title", "title": "A maquininha virou\na parte barata.", "sub": "o dinheiro foi para outro lugar"}},

 # ---------- PRÓXIMO ----------
 {"say": "E esse outro lugar tem nome: antecipação de recebíveis. A mesma taxa que fez as ações da Stone despencarem vinte e três por cento num único dia. Como funciona esse negócio bilionário que quase ninguém vê? Esse é o próximo vídeo do Por Trás do Dinheiro.",
  "vis": {"type": "title", "title": "Próximo vídeo:", "sub": "Antecipação de recebíveis: o negócio bilionário que ninguém vê", "brand": True}},
]
