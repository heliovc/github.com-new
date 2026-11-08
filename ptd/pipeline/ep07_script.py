# EP07 — Como o Pix mudou os bancos (e quem perdeu dinheiro)
# Estrutura NOVA: "autópsia" — o legista abre 4 fichas (vítimas do Pix), uma por bloco, com carimbo de estado
# (MORTO / FERIDO / EM OBSERVAÇÃO / PRÓXIMO?) + a virada (se o Pix é grátis, quem paga?) + payoff.
# Diferente do EP04 (extrato), EP05 (luta em rounds) e EP06 (siga o recebível).
# Cenas novas: obit (ficha de autópsia com carimbo) e race (corrida de transferências DOC x TED x Pix).
# Loops: (1) se o Pix é de graça, quem está pagando? -> virada; (2) a vítima que você usa todo dia -> vítima 3 (débito);
#        (3) o banco que mais movimentou Pix foi o que mais perdeu -> vítima 2.
# Re-engajamentos: ~3:00 BB -17,2% (o maior do Pix foi o que mais perdeu); ~6:00 a virada (receita de serviços subiu para R$ 122 bi).
TITLE = "Como o Pix mudou os bancos (e quem perdeu dinheiro)"

SCENES = [
 # ---------- GANCHO ----------
 {"say": "Trezentos e dezoito milhões. Foi o número de Pix feitos no Brasil num único dia, quatro de setembro de dois mil e vinte e seis. Pessoa física não pagou nada por nenhum deles. Então alguém, em algum lugar, perdeu dinheiro.",
  "vis": {"type": "bignumber", "from": 0, "to": 318073816, "decimals": 0, "caption": "Pix liquidados em 24 horas — recorde de 04/09/2026 (R$ 186,9 bilhões)",
          "source": "Fonte: Banco Central (SPI), via Metrópoles e Let's Money, set/2026"}},
 {"say": "Hoje vamos fazer uma autópsia. Quatro vítimas do Pix, uma por uma: quem morreu, quem ficou ferido e quem ainda está na fila. Uma delas você usa toda semana e nem percebeu que está doente.",
  "vis": {"type": "title", "title": "A autópsia do Pix", "sub": "4 vítimas — POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "E no fim, a pergunta que quase ninguém faz: se o Pix é de graça, quem está pagando a conta? A resposta tem a ver com o que os bancos fizeram depois de perder.",
  "vis": {"type": "bullets", "title": "O que vamos abrir", "items": ["Quem morreu", "Quem ficou ferido", "Quem está em observação", "Se é grátis, quem paga?"], "highlight": 3}},

 # ---------- A ARMA ----------
 {"say": "Antes das vítimas, a arma. Até dois mil e vinte, mandar dinheiro para outro banco tinha duas opções. O DOC, que só caía no dia útil seguinte. E a TED, que caía no mesmo dia, mas só em horário bancário. As duas, em geral, com tarifa.",
  "vis": {"type": "race", "title": "Mandar R$ 100 para outro banco", "lanes": [["DOC", "dia útil seguinte", 0.25, "#E06C5A"], ["TED", "mesmo dia, horário bancário", 0.5, "#F2A93B"], ["Pix", "segundos, 24 horas por dia", 3.0, "#3AC47D"]],
          "cap": [0.35, 0.6, 1], "caption": "Pix: lançado pelo Banco Central em novembro de 2020"}},
 {"say": "Aí o Banco Central lançou o Pix, em novembro de dois mil e vinte. Cai em segundos, a qualquer hora, inclusive domingo de madrugada. E pela regra do próprio Banco Central, para pessoa física, transferir é de graça.",
  "vis": {"type": "compare", "left": ["Pix", "segundos", "24 horas, 7 dias", "grátis para pessoa física"], "right": ["DOC / TED", "horas ou 1 dia útil", "horário bancário", "tarifa por envio"],
          "caption": "Regras do Pix: Banco Central do Brasil"}},
 {"say": "O resultado foi uma das adoções mais rápidas da história dos pagamentos. Em dois mil e vinte e cinco foram setenta e nove vírgula oito bilhões de transações. Cento e quarenta e oito milhões de pessoas usaram o Pix, oitenta e seis por cento dos adultos do país, além de doze vírgula oito milhões de empresas.",
  "vis": {"type": "cards", "title": "O Pix em 2025", "cards": [["1", "79,8 bi", "transações\nno ano"], ["2", "148 mi", "pessoas\n(86% dos adultos)"], ["3", "12,8 mi", "empresas\nusaram"]],
          "highlight": 0, "caption": "Fonte: Banco Central, Relatório de Gestão do Pix 2023–2025"}},
 {"say": "No segundo semestre de dois mil e vinte e cinco, o Pix já era cinquenta e quatro vírgula sete por cento de todas as transações de pagamento do país. Os cartões, somando crédito, débito e pré-pago, ficaram com trinta vírgula quatro. Mais da metade de tudo que se paga no Brasil passa por um sistema que não existia seis anos atrás.",
  "vis": {"type": "stack", "title": "Fatia no número de transações (2º sem/2025)", "parts": [["Pix", 54.7, "#3AC47D", "54,7%"], ["Cartões", 30.4, "#5B8DEF", "crédito, débito\ne pré-pago"], ["Outros", 14.9, "#78879F", "boleto, TED,\nsaque..."]],
          "highlight": 0, "caption": "Fonte: Banco Central, estatísticas de pagamentos de varejo, via Finsiders Brasil"}},

 {"say": "E o ritmo não diminuiu. Só no segundo trimestre de dois mil e vinte e seis foram vinte e dois vírgula nove bilhões de Pix, movimentando dez vírgula cinco trilhões de reais. O segundo colocado, o cartão de crédito, fez seis bilhões de operações no mesmo período. Quase quatro Pix para cada compra no crédito. Quando um meio de pagamento cresce assim, o dinheiro que ele carrega sai de algum lugar. E é exatamente aí que começam as vítimas.",
  "vis": {"type": "bars", "title": "Operações no 2º trimestre de 2026 (bilhões)", "items": [["Pix", 22.93, "#3AC47D"], ["Cartão de crédito", 6.05, "#5B8DEF"]],
          "decimals": 2, "caption": "Fonte: Banco Central, via Let's Money (set/2026)"}},

 # ---------- VÍTIMA 1: O DOC ----------
 {"say": "Vítima número um. Essa não resistiu. E a data da morte tem um detalhe curioso.",
  "vis": {"type": "obit", "case": "CASO 1/4", "name": "O DOC", "born": "1985, criado pelo Banco Central", "died": "29 de fevereiro de 2024", "cause": "substituído pelo Pix",
          "note": "1º semestre de 2023: só 0,05% das operações", "stamp": "MORTO", "stamp_col": "#C0392B"}},
 {"say": "O DOC nasceu em mil novecentos e oitenta e cinco. Por quase quarenta anos foi o jeito comum de mandar dinheiro entre bancos. Mas no primeiro semestre de dois mil e vinte e três, segundo a Febraban, sobravam só dezoito vírgula três milhões de DOCs, contra trinta e sete bilhões de operações no período. Zero vírgula zero cinco por cento.",
  "vis": {"type": "bignumber", "from": 100, "to": 0.05, "suffix": "%", "decimals": 2, "caption": "fatia do DOC nas operações do 1º semestre de 2023 (18,3 milhões de 37 bilhões)",
          "source": "Fonte: Febraban com dados do Banco Central, via InfoMoney (jan/2024)"}},
 {"say": "A Febraban parou a emissão em quinze de janeiro de dois mil e vinte e quatro. O último agendamento foi em vinte e nove de fevereiro. Repare na data: um dia que só existe de quatro em quatro anos. O DOC não foi morto por lei. Foi abandonado pelos próprios clientes, até não valer mais a pena manter o sistema ligado.",
  "vis": {"type": "timeline", "even": True, "points": [["1985", "nasce o DOC"], ["nov/2020", "chega o Pix"], ["1º sem/2023", "0,05% das operações"], ["29/02/2024", "fim do DOC"]],
          "caption": "Fonte: Febraban, via InfoMoney"}},

 # ---------- VÍTIMA 2: A TARIFA DA CONTA ----------
 {"say": "Vítima número dois. Essa sobreviveu, mas saiu ferida. E o ferimento aparece no balanço dos maiores bancos do país.",
  "vis": {"type": "obit", "case": "CASO 2/4", "name": "A tarifa da conta", "born": "pacotes de conta corrente", "died": "sobreviveu, menor", "cause": "transferência virou grátis",
          "note": "4 maiores bancos: −R$ 1,5 bilhão em 2021", "stamp": "FERIDA", "stamp_col": "#D68910"}},
 {"say": "Parte do que você pagava no pacote da conta corrente era justamente para ter direito a transferências. Quando a transferência virou grátis, esse argumento perdeu força. Em dois mil e vinte e um, o primeiro ano inteiro com Pix, a receita com conta corrente dos quatro maiores bancos listados caiu de vinte e seis vírgula nove para vinte e cinco vírgula quatro bilhões de reais. Um bilhão e meio a menos, em um ano.",
  "vis": {"type": "bignumber", "from": 26.9, "to": 25.4, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "caption": "receita com conta corrente de BB, Itaú, Bradesco e Santander: 2020 → 2021 (−5,7%)",
          "source": "Fonte: balanços dos bancos, via TradeMap e Money Times (fev/2022)"}},
 # REENGAJE ~3:00
 {"say": "Agora o detalhe que ninguém esperava. Quem mais perdeu não foi o banco mais atrasado. Foi o Banco do Brasil, que respondia por quase trinta por cento do volume do Pix. A receita dele com conta corrente caiu dezessete vírgula dois por cento. O Itaú caiu um vírgula oito. O Santander, três vírgula nove. E o Bradesco ainda subiu zero vírgula sete.",
  "vis": {"type": "ticker", "title": "Receita com conta corrente em 2021", "date": "2021 x 2020", "rows": [["Banco do Brasil", -17.2, "~30% do volume do Pix"], ["Santander", -3.9, ""], ["Itaú", -1.8, ""], ["Bradesco", 0.7, ""]],
          "caption": "Fonte: balanços dos bancos, via TradeMap e Money Times"}},
 {"say": "E por que o Bradesco escapou? Uma pista está no próprio balanço do período. No fim de dois mil e vinte e um, os bancos digitais do grupo, o Next e o Bitz, somavam mais de catorze milhões de clientes. E oitenta e seis por cento deles não tinham conta no banco tradicional. Ou seja: em vez de só perder tarifa para o Pix, o grupo usou o digital para buscar clientes novos.",
  "vis": {"type": "cards", "title": "Bradesco: o banco que não caiu", "cards": [["1", "+0,7%", "receita com conta\ncorrente em 2021"], ["2", "14 mi+", "clientes no\nNext e Bitz"], ["3", "86%", "não tinham conta\nno Bradesco"]],
          "highlight": 2, "caption": "Fonte: Bradesco, via Money Times (fev/2022)"}},
 {"say": "Por que justo o banco que mais movimentou Pix? Uma leitura possível: quanto mais clientes usavam transferência paga, mais receita havia para perder. O Pix não pune quem é pequeno. Pune quem vivia de cobrar pelo caminho que ele tornou grátis.",
  "vis": {"type": "flow", "nodes": ["Cliente pagava por TED", "Pix chega grátis", "Pacote perde valor", "Receita cai"], "notes": ["", "nov/2020", "", "BB −17,2%"], "pulse": True,
          "caption": "Análise: quem dependia de tarifa de transferência perdeu mais"}},

 # ---------- VÍTIMA 3: O DÉBITO ----------
 {"say": "Vítima número três. Essa você conhece bem: está na sua carteira.",
  "vis": {"type": "obit", "case": "CASO 3/4", "name": "O cartão de débito", "born": "dinheiro da conta na maquininha", "died": "ainda vivo", "cause": "Pix na hora do pagamento",
          "note": "1º semestre de 2026: valor −1,8% em um ano", "stamp": "EM OBSERVAÇÃO", "stamp_col": "#2E86C1"}},
 {"say": "O débito e o Pix fazem a mesma coisa: tiram o dinheiro da sua conta na hora. E para muita loja, receber por Pix custa menos que a taxa do débito. Os números mostram o efeito. No primeiro semestre de dois mil e vinte e seis, segundo a Abecs, o débito movimentou quatrocentos e oitenta e um vírgula seis bilhões de reais, uma queda de um vírgula oito por cento em um ano. O número de transações caiu zero vírgula oito.",
  "vis": {"type": "bignumber", "from": 0, "to": -1.8, "suffix": "%", "decimals": 1, "warn": True, "caption": "variação do valor pago no débito: 1º sem/2026 x 1º sem/2025 (R$ 481,6 bilhões)",
          "source": "Fonte: Abecs, balanço do 1º semestre de 2026, via Mercado & Consumo"}},
 {"say": "Agora compare com o crédito, no mesmo período: um vírgula sete trilhão de reais, alta de doze vírgula um por cento. O Pix não matou o cartão. Ele matou a parte do cartão que só servia para pagar à vista. O crédito sobreviveu por um motivo simples: o Pix não parcela e não dá prazo.",
  "vis": {"type": "compare", "left": ["Crédito", "R$ 1,7 trilhão", "+12,1% em um ano", "parcela e dá prazo"], "right": ["Débito", "R$ 481,6 bilhões", "−1,8% em um ano", "faz o mesmo que o Pix"],
          "caption": "Fonte: Abecs, 1º semestre de 2026"}},
 {"say": "E o Banco Central chegou a desenhar um Pix Parcelado com regras próprias. Depois de vários adiamentos, em dezembro de dois mil e vinte e cinco, desistiu de regulamentar. Por enquanto, a última trincheira do cartão de crédito continua de pé.",
  "vis": {"type": "timeline", "even": True, "points": [["2024–2025", "Pix Parcelado em estudo"], ["vários adiamentos", "regras não saem"], ["dez/2025", "BC desiste de regular"]],
          "caption": "Fonte: O Povo / IstoÉ Dinheiro, 04/12/2025"}},

 # ---------- VÍTIMA 4: O BOLETO ----------
 {"say": "Vítima número quatro. Essa ainda não morreu. Está na fila, e o Banco Central já entregou a arma.",
  "vis": {"type": "obit", "case": "CASO 4/4", "name": "Boleto e débito automático", "born": "contas que se repetem todo mês", "died": "—", "cause": "Pix Automático (desde jun/2025)",
          "note": "a próxima frente do Pix", "stamp": "PRÓXIMA?", "stamp_col": "#8E44AD"}},
 {"say": "Desde dezesseis de junho de dois mil e vinte e cinco existe o Pix Automático. Você autoriza uma vez, e a conta de luz, a escola ou a assinatura passam a ser cobradas sozinhas, todo mês. E desde janeiro de dois mil e vinte e seis, a instituição que já oferece débito automático com outros bancos é obrigada a oferecer o Pix Automático também.",
  "vis": {"type": "flow", "nodes": ["Você autoriza 1 vez", "Empresa cobra no dia", "Pix cai sozinho", "Todo mês"], "notes": ["no app do banco", "", "sem boleto", ""], "pulse": True,
          "caption": "Pix Automático: desde 16/06/2025 (Banco Central)"}},
 {"say": "É exatamente o terreno do boleto e do débito automático tradicional. Se o Pix repetir aqui o que fez com o DOC, a próxima ficha de autópsia já tem nome.",
  "vis": {"type": "title", "title": "A próxima ficha\njá tem nome?", "sub": "boleto e débito automático"}},

 # ---------- HERDEIROS ----------
 {"say": "Toda autópsia termina com uma pergunta: quem herdou? O primeiro herdeiro é você. Um levantamento do Movimento Brasil Competitivo estimou que o Pix gerou cento e dezessete bilhões de reais de economia direta em cinco anos, só em tarifas e custos que deixaram de ser pagos.",
  "vis": {"type": "bignumber", "from": 0, "to": 117, "prefix": "R$ ", "suffix": " bi", "decimals": 0, "caption": "economia direta estimada com o Pix em 5 anos (nov/2020 a 2025)",
          "source": "Fonte: Movimento Brasil Competitivo (MBC), via BPMoney, 16/11/2025"}},
 {"say": "O segundo herdeiro são os bancos digitais. Antes, abrir conta em banco novo era chato porque mandar dinheiro para fora dele custava caro. Com o Pix, o dinheiro entra e sai de qualquer banco em segundos. A troca de banco ficou barata, e isso ajudou quem estava chegando. O Nubank, por exemplo, já passa de cento e dezenove milhões de clientes no Brasil, pelo ranking do Banco Central.",
  "vis": {"type": "bars", "title": "Clientes no Brasil (milhões, 3º tri/2026)", "items": [["Nubank", 119.6, "#8E44AD"], ["Mercado Pago", 77.5, "#5B8DEF"], ["PicPay", 72.2, "#3AC47D"], ["Inter", 45.9, "#F2A93B"]],
          "decimals": 1, "caption": "Fonte: ranking de clientes do Banco Central, 3º tri/2026, via Finsiders (22/10/2026)"}},

 # ---------- A VIRADA ~6:00 ----------
 # REENGAJE ~6:00
 {"say": "Agora a parte que não fecha. Lembra do bilhão e meio que os quatro grandes perderam em conta corrente em dois mil e vinte e um? No mesmo ano, a receita total de serviços desses quatro bancos não caiu. Cresceu, e chegou a cento e vinte e dois bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 122, "prefix": "R$ ", "suffix": " bi", "decimals": 0, "caption": "receita de serviços dos 4 maiores bancos listados em 2021 — cresceu mesmo com o Pix",
          "source": "Fonte: balanços dos bancos, via Money Times (18/02/2022)"}},
 {"say": "Então, se o Pix é grátis, quem está pagando? A resposta tem três partes. Primeira: o Pix é grátis para pessoa física, não para empresa. As regras do Banco Central permitem que o banco cobre Pix de empresas. No lançamento, grandes bancos chegaram a cobrar até dez reais por Pix de pessoa jurídica.",
  "vis": {"type": "cards", "title": "Se é grátis, quem paga?", "cards": [["1", "Empresas", "Pix de pessoa\njurídica pode ser cobrado"], ["2", "Dinheiro grande", "TED ainda lidera\nem valor"], ["3", "Crédito", "o lucro mudou\nde lugar"]],
          "highlight": 0, "caption": "Tecnoblog: até R$ 10 por Pix de PJ em grandes bancos no lançamento"}},
 {"say": "Segunda: o dinheiro grande ainda não migrou. No segundo semestre de dois mil e vinte e cinco, a TED movimentou trinta e quatro vírgula sete por cento do valor dos pagamentos, contra vinte e oito vírgula seis do Pix. O Pix ganhou na quantidade, no cafezinho e no aluguel. A transferência de empresa grande continua passando pelo trilho antigo.",
  "vis": {"type": "scoreboard", "title": "Fatia no VALOR movimentado (2º sem/2025)", "cols": [["TED", 34.7, "#F2A93B"], ["Pix", 28.6, "#3AC47D"], ["Boleto", 7.6, "#78879F"]],
          "highlight": 0, "decimals": 1, "caption": "Fonte: Banco Central, via Finsiders Brasil"}},
 {"say": "E a terceira parte é a mais importante. O Pix tirou dos bancos a cobrança por mover dinheiro. Mas não tirou a cobrança por emprestar dinheiro. E é aí que o lucro foi parar: no crédito, que cresceu doze por cento em valor no primeiro semestre, no parcelado e nos juros, como vimos nos episódios do rotativo e da antecipação.",
  "vis": {"type": "flow", "nodes": ["Tarifa de transferência", "Pix zera", "Banco disputa cliente", "Lucro vem do crédito"], "notes": ["antes de 2020", "pessoa física", "conta digital, app", "juros, parcelado"], "pulse": True,
          "caption": "Análise própria: o preço não sumiu, mudou de lugar"}},

 # ---------- PAYOFF ----------
 {"say": "Então, quem perdeu dinheiro com o Pix? O DOC morreu. A tarifa da conta encolheu, e quem mais dependia dela, como o Banco do Brasil, sentiu primeiro. O débito parou de crescer. E o boleto está na fila.",
  "vis": {"type": "bullets", "title": "O laudo final", "items": ["DOC: morto em 2024", "Tarifa da conta: −R$ 1,5 bi em 2021", "Débito: −1,8% em 2026", "Boleto: na fila (Pix Automático)"], "highlight": -1}},
 {"say": "Mas o sistema bancário não ficou mais pobre. Ele trocou de fonte. O Pix é de graça para você porque o banco passou a ganhar em outro ponto da sua vida financeira. Na próxima vez que um app te oferecer crédito logo depois de um Pix, você já sabe por quê.",
  "vis": {"type": "title", "title": "O preço não sumiu.\nMudou de lugar.", "sub": "Pix grátis, crédito caro"}},
 {"say": "No próximo episódio, outra autópsia, mas de um rombo. Como uma varejista com quase cem anos de história escondeu vinte e cinco bilhões de reais no próprio balanço, e por que ninguém viu. Americanas: o rombo explicado.",
  "vis": {"type": "title", "title": "Próximo: Americanas", "sub": "R$ 25,2 bilhões escondidos no balanço"}},
]
