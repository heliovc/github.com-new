# EP16 — Quem compra a sua dívida: o mercado bilionário das dívidas vendidas (e o leilão do Desenrola 3.0)
# Estrutura NOVA: "as 5 etiquetas de preço de uma dívida" — a mesma dívida de R$ 1.000 (EXEMPLO ILUSTRATIVO) vista em
# cinco preços: o valor de face, o preço no atacado, quem compra, a conta do comprador e o preço que chega até você.
# Cena nova: tag (etiqueta de papel pendurada, preço antigo riscado, preço novo; recap com as 5 etiquetas).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação), EP12 (contrato), EP13 (prédio), EP14 (cebola), EP15 (prova).
# Promessa do EP15 cumprida ("o mercado bilionário das dívidas vendidas: quem compra, quanto paga, e por que essa empresa
# pode aceitar um desconto enorme no feirão de renegociação").
# Loop: "se o comprador paga tão pouco, por que não dá 100% de desconto?" -> etiqueta 4.
# Re-engajamentos: ~3:00 quem compra; ~6:30 os seus direitos.
# Números/fatos: EY-Parthenon, Panorama do Mercado de Ativos Problemáticos 2026 (fev-mar/2026; deságio esperado:
# 18% 70-80%, 36% 80-90%, 18% 90-95%, 9% 95-99%; liquidez 29% como motivo da cessão); FTC, "The Structure and Practices
# of the Debt Buying Industry" (jan/2013: 5.000+ carteiras, ~90 milhões de contas, US$ 143 bi de face; média de 4 centavos
# por dólar; < 3 anos 7,9; 6 a 15 anos 2,2); comunicado do Itaú (31/12/2015) / Reuters: 81,94% da Recovery por R$ 640 mi;
# Recovery via Bloomberg Línea e Trade Map (2026): R$ 144 bi sob gestão, 33 mi de clientes, 25-30% do mercado, R$ 34 bi
# em 2025, R$ 40 bi projetados em 2026, R$ 17 bi no 1º semestre de 2026, à vista 10% dos acordos (eram 35%);
# Deloitte, pesquisa de NPL 2025/2026: R$ 30,2 bi cedidos em 2025, R$ 52,3 bi projetados em 2026; Serasa, Mapa da
# Inadimplência de outubro de 2026: 84,6 milhões, 51,32% dos adultos; MP 1.393/2026 (25/09/2026): União compra carteiras
# de PF, valor original até R$ 10 mil, deságio mínimo de 90%, despesa até R$ 15 bi, devedor quita com deságio de até o
# mesmo percentual ou parcela; Portaria MF 3.127 (22/10/2026), chamada até 30/10; min. Dario Durigan: até R$ 90 bi em
# dívidas; leilão previsto para nov (podendo ir a dez); comissão mista instalada em 17/11/2026; Código Civil, arts. 290 e
# 292 e art. 206, §5º, I; CDC, art. 43, §1º; STJ, REsp 2.088.100/SP (17/10/2023) e REsp 2.103.726/SP (14/05/2024).
# Exemplo das 100 dívidas (compra a 10%, 20 acordos) = EXEMPLO ILUSTRATIVO, cálculo do canal.
TITLE = "Quem compra a sua dívida (e por que pode te dar 90% de desconto)"

RECAP = [["R$ 1.000", "o contrato"], ["R$ 100 a 200", "o atacado"], ["Recovery\ne fundos", "quem compra"],
         ["acordo\nou nada", "a conta"], ["o feirão", "o seu preço"]]
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Imagine uma dívida de mil reais no cartão, atrasada há dois anos. Um dia, sem te avisar antes, o banco vende essa dívida para outra empresa. Por quanto? Muitas vezes, por menos de cem reais. Nos Estados Unidos, um estudo do governo encontrou uma média de quatro centavos por dólar. Aqui, seriam quarenta reais.",
  "vis": {"type": "tag", "n": 0, "old": "R$ 1.000", "price": "R$ 40", "note": "se fosse a média\nmedida nos EUA", "label": "A SUA DÍVIDA À VENDA",
          "title": "Mil reais\npor quarenta?", "sub": "o preço que ninguém te conta",
          "caption": "EXEMPLO ILUSTRATIVO · média dos EUA: FTC, estudo sobre compradores de dívidas (2013)"}},
 {"say": "E agora o governo brasileiro quer entrar nesse mercado. Em setembro, uma medida provisória autorizou a União a comprar dívidas atrasadas dos bancos, em leilão, pagando no máximo dez por cento do valor. É o Desenrola três ponto zero. E o leilão está previsto para as próximas semanas.",
  "vis": {"type": "bignumber", "from": 0, "to": 90, "suffix": "%", "decimals": 0, "warn": True, "caption": "de desconto mínimo para a União comprar dívidas",
          "source": "Fonte: Medida Provisória 1.393, de 25/09/2026 (Desenrola 3.0)"}},
 {"say": "Para entender por que alguém vende mil reais por cem, ou menos, a gente vai seguir as etiquetas de preço de uma dívida. São cinco. Do valor que está no contrato até o valor que aparece no seu celular, no feirão de renegociação.",
  "vis": {"type": "title", "title": "As 5 etiquetas\nda sua dívida", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "E guarde uma pergunta para o meio do caminho. Se a empresa que compra paga tão pouco, por que ela não te dá cem por cento de desconto? A resposta está na etiqueta quatro.",
  "vis": {"type": "title", "title": "Por que não\n100% de desconto?", "sub": "a resposta está na etiqueta 4"}},

 # ---------- ETIQUETA 1: O VALOR DE FACE ----------
 {"say": "Etiqueta um: o valor de face. É o número que está no contrato, mais juros e multa. É o que o banco diz que você deve. No papel, essa dívida vale mil reais. Na prática, vale bem menos. E o próprio banco sabe disso.",
  "vis": {"type": "tag", "n": 1, "old": "R$ 1.000", "note": "+ juros e multa", "label": "O VALOR DE FACE", "title": "O que diz\no contrato", "sub": "o preço no papel",
          "caption": "EXEMPLO ILUSTRATIVO"}},
 {"say": "Uma dívida é uma promessa. E uma promessa que já foi quebrada vale menos. Quando o atraso cresce, as regras contábeis obrigam o banco a separar dinheiro para cobrir a perda provável, a chamada provisão. Com o tempo, a dívida pode sair do balanço como prejuízo. Mas o direito de cobrar continua existindo, e é esse direito que vai à venda.",
  "vis": {"type": "flow", "nodes": ["Atraso", "Provisão", "Prejuízo", "Venda"], "notes": ["a promessa quebra", "o banco reserva", "sai do balanço", "o direito de cobrar"], "pulse": True,
          "caption": "Regras de provisão: Resolução CMN 4.966/2021"}},
 {"say": "E cobrar custa caro. Precisa de central de atendimento, de carta, de sistema, às vezes de advogado. Para o banco, muitas vezes compensa transformar a promessa quebrada em dinheiro hoje, mesmo que pouco. Numa pesquisa da consultoria EY com quem atua nesse mercado, o motivo mais citado para vender carteiras foi justamente esse: ganhar liquidez, dinheiro em caixa.",
  "vis": {"type": "cards", "title": "Por que o banco vende", "cards": [["$", "Liquidez", "dinheiro em caixa\nhoje"], ["%", "Custo", "cobrar sai caro"], ["✓", "Balanço", "tira o problema\nda carteira"]],
          "highlight": 0, "caption": "Fonte: EY-Parthenon, Panorama 2026 (liquidez: 29% das respostas)"}},

 # ---------- ETIQUETA 2: O ATACADO ----------
 {"say": "Etiqueta dois: o preço no atacado. O banco não vende a sua dívida sozinha. Ele junta milhares, às vezes milhões de dívidas, num pacote chamado carteira. E vende esse pacote com desconto. O mercado chama esse desconto de deságio.",
  "vis": {"type": "tag", "n": 2, "old": "R$ 1.000", "price": "R$ 100 a 200", "price_col": "#B5651D", "note": "vendida em pacote,\na carteira", "label": "O PREÇO NO ATACADO",
          "title": "O pacote\nde dívidas", "sub": "deságio de 80% a 90%", "caption": "EXEMPLO ILUSTRATIVO com a faixa mais citada pela EY-Parthenon (2026)"}},
 {"say": "De quanto é esse desconto? Na pesquisa da EY, feita no começo de dois mil e vinte e seis, a resposta mais comum foi um deságio entre oitenta e noventa por cento. Ou seja, a dívida de mil reais sai por algo entre cem e duzentos. E quase um em cada dez espera descontos de noventa e cinco a noventa e nove por cento.",
  "vis": {"type": "bars", "title": "Deságio esperado (% das respostas)", "items": [["70% a 80%", 18, "#5B8DEF"], ["80% a 90%", 36, "#F2A93B"], ["90% a 95%", 18, "#5B8DEF"], ["95% a 99%", 9, "#E06C5A"]],
          "suffix": "%", "decimals": 0, "caption": "Fonte: EY-Parthenon, Panorama do Mercado de Ativos Problemáticos 2026 (fev-mar/2026) · deságio sobre o valor de face"}},
 {"say": "E quanto mais velha a dívida, mais barata. O estudo mais detalhado sobre isso é americano. A FTC, a agência de defesa do consumidor dos Estados Unidos, analisou mais de cinco mil carteiras, com cerca de noventa milhões de contas. Em média, os compradores pagaram quatro centavos por dólar. Dívidas com menos de três anos saíam por quase oito centavos. As de seis a quinze anos, por pouco mais de dois.",
  "vis": {"type": "bars", "title": "Centavos pagos por dólar de dívida (EUA)", "items": [["Menos de 3 anos", 7.9, "#3AC47D"], ["Média geral", 4.0, "#F2A93B"], ["6 a 15 anos", 2.2, "#E06C5A"]],
          "suffix": " centavos", "decimals": 1, "caption": "Fonte: FTC, The Structure and Practices of the Debt Buying Industry (2013)"}},
 {"say": "O motivo é simples. Com o tempo, a chance de receber cai. A pessoa troca de telefone, de endereço, de emprego. E a dívida vai chegando perto de um limite que a gente vai ver mais adiante: o prazo em que ela deixa de poder ser cobrada.",
  "vis": {"type": "title", "title": "O tempo corrói\no preço da dívida", "sub": "quanto mais velha, mais barata"}},

 # ---------- ETIQUETA 3: QUEM COMPRA ----------
 # REENGAJE ~3:00
 {"say": "Etiqueta três: quem paga esse preço. No Brasil, existe uma indústria inteira dedicada a isso. Empresas de recuperação de crédito, securitizadoras e fundos de investimento especializados em dívida atrasada. Eles compram o direito de cobrar e assumem o risco de não receber nada.",
  "vis": {"type": "tag", "n": 3, "old": "R$ 1.000", "price": "novo dono", "price_col": "#5B3FA0", "note": "o direito de cobrar\nmuda de mãos", "label": "QUEM COMPRA",
          "title": "Os compradores\nde dívida", "sub": "empresas, securitizadoras e fundos"}},
 {"say": "A maior delas é a Recovery. Ela pertencia ao BTG Pactual. No último dia de dois mil e quinze, o Itaú anunciou a compra de oitenta e dois por cento da empresa, por seiscentos e quarenta milhões de reais. Hoje, segundo a própria Recovery, ela administra mais de cento e quarenta e quatro bilhões de reais em dívidas atrasadas.",
  "vis": {"type": "bignumber", "from": 0, "to": 144, "prefix": "R$ ", "suffix": " bilhões", "decimals": 0, "warn": True, "caption": "em dívidas atrasadas nas mãos de uma única empresa",
          "source": "Fontes: Recovery, via Bloomberg Línea (2026); Itaú, comunicado de 31/12/2015 (81,94% por R$ 640 milhões)"}},
 {"say": "São mais de trinta e três milhões de devedores. Para ter uma ideia, é como se um em cada cinco adultos brasileiros tivesse uma dívida nas mãos dessa empresa. E ela diz ter entre vinte e cinco e trinta por cento de todo o mercado de compra de carteiras.",
  "vis": {"type": "bignumber", "from": 0, "to": 33, "suffix": " milhões", "decimals": 0, "warn": True, "caption": "de devedores com a Recovery · cerca de 1 em cada 5 adultos",
          "source": "Fonte: Recovery, via Bloomberg Línea (2026) · proporção: cálculo do canal com a base de adultos da Serasa"}},
 {"say": "E esse mercado está crescendo rápido. Segundo a Deloitte, os credores venderam trinta vírgula dois bilhões de reais em dívidas em dois mil e vinte e cinco. Para dois mil e vinte e seis, as projeções vão de quarenta bilhões, na conta da Recovery, a cinquenta e dois, na da Deloitte. Só no primeiro semestre, foram dezessete bilhões.",
  "vis": {"type": "bars", "title": "Dívidas vendidas no Brasil (2026 = projeções)", "items": [["2025", 30.2, "#5B8DEF"], ["2026 (Recovery)", 40, "#F2A93B"], ["2026 (Deloitte)", 52.3, "#E06C5A"]],
          "prefix": "R$ ", "suffix": " bi", "decimals": 1, "caption": "Fontes: Deloitte, pesquisa de NPL 2025/2026; Recovery, via Bloomberg Línea (1º sem./2026: R$ 17 bi)"}},
 {"say": "Por que agora? Porque nunca houve tanta gente devendo. Em outubro, a Serasa contou oitenta e quatro vírgula seis milhões de inadimplentes. Mais da metade dos adultos do país. E muita dívida atrasada significa muita carteira à venda.",
  "vis": {"type": "bignumber", "from": 0, "to": 84.6, "suffix": " milhões", "decimals": 1, "warn": True, "caption": "de inadimplentes em outubro de 2026 · 51,32% dos adultos",
          "source": "Fonte: Serasa, Mapa da Inadimplência (outubro de 2026), via imprensa"}},

 # ---------- ETIQUETA 4: A CONTA DO COMPRADOR ----------
 {"say": "Etiqueta quatro: a conta de quem compra. E aqui está a resposta da pergunta do começo. Vamos fazer um exemplo com números redondos. É um exemplo ilustrativo, para entender a lógica, não o resultado de uma empresa real.",
  "vis": {"type": "tag", "n": 4, "old": "R$ 1.000", "price": "acordo ou nada", "price_col": "#2E7D5B", "note": "a maioria nunca paga", "label": "A CONTA DO COMPRADOR",
          "title": "Como lucra\nquem compra", "sub": "um exemplo ilustrativo", "caption": "EXEMPLO ILUSTRATIVO"}},
 {"say": "Uma empresa compra cem dívidas de mil reais. Valor de face: cem mil. Ela paga dez por cento: dez mil reais. Começa a cobrar. A maioria das pessoas não vai pagar nunca, porque não pode ou porque não é encontrada. Digamos que só vinte fechem acordo.",
  "vis": {"type": "compare", "left": ["O que comprou", "100 dívidas de R$ 1.000", "valor de face: R$ 100 mil", "pagou: R$ 10 mil"], "right": ["O que acontece", "80 não pagam", "20 fecham acordo", "quanto cobrar?"],
          "caption": "EXEMPLO ILUSTRATIVO · cálculo do canal"}},
 {"say": "Se ela der sessenta por cento de desconto, cada acordo rende quatrocentos reais. Vinte acordos: oito mil. Ela perdeu dinheiro. Se der trinta por cento de desconto, cada acordo rende setecentos, e o total vai a catorze mil. Sobram quatro mil, antes de pagar os custos de cobrança.",
  "vis": {"type": "bars", "title": "Quanto volta com 20 acordos (exemplo)", "items": [["Desconto de 60%", 8000, "#E06C5A"], ["Custo da carteira", 10000, "#7884A0"], ["Desconto de 30%", 14000, "#3AC47D"]],
          "prefix": "R$ ", "decimals": 0, "caption": "EXEMPLO ILUSTRATIVO · cálculo do canal, antes dos custos de cobrança"}},
 {"say": "Percebe o equilíbrio? Desconto grande demais, a conta não fecha. Desconto pequeno demais, ninguém paga. Essa empresa vive de achar o ponto certo. E, cada vez mais, usa dados para isso: quem tem mais chance de pagar, por qual canal, com qual oferta, em quantas parcelas.",
  "vis": {"type": "bullets", "title": "O que o comprador calcula", "items": ["Quem tende a pagar", "Qual desconto fecha acordo", "Por qual canal oferecer", "Em quantas parcelas"], "highlight": 1,
          "caption": "Análise do canal"}},
 {"say": "Por isso, o desconto de noventa por cento no feirão não é caridade. Se a dívida foi comprada por cinco por cento do valor, receber dez já dobra o dinheiro. O seu desconto e o lucro de quem comprou podem existir ao mesmo tempo. E é por isso que a primeira oferta quase nunca é a única.",
  "vis": {"type": "title", "title": "O seu desconto\npode ser o lucro dele", "sub": "análise do canal · não é recomendação"}},
 {"say": "E um número da Recovery mostra o aperto do consumidor. Hoje, só dez por cento dos acordos são pagos à vista. Já foram trinta e cinco por cento. Os outros noventa por cento são parcelados.",
  "vis": {"type": "stack", "title": "Como os acordos são pagos", "parts": [["À vista", 10, "#3AC47D", "já foram 35%"], ["Parcelado", 90, "#F2A93B", "a grande maioria"]], "highlight": 1,
          "caption": "Fonte: Recovery, via Bloomberg Línea e Trade Map (2026)"}},

 # ---------- ETIQUETA 5: O SEU PREÇO ----------
 {"say": "Etiqueta cinco: o preço que chega até você. É a oferta do feirão, a mensagem no aplicativo, a ligação de um número que você não conhece. E é aqui que entra a grande novidade de dois mil e vinte e seis: o governo como comprador.",
  "vis": {"type": "tag", "n": 5, "old": "R$ 1.000", "price": "R$ 100?", "price_col": "#2E7D5B", "note": "a oferta do feirão", "label": "O PREÇO PARA VOCÊ",
          "title": "O que chega\nno seu celular", "sub": "e o governo entra no jogo", "caption": "EXEMPLO ILUSTRATIVO"}},
 {"say": "Pela medida provisória mil trezentos e noventa e três, de setembro, a União pode comprar carteiras de dívidas de pessoas físicas, com valor original de até dez mil reais, em leilão. A regra: deságio mínimo de noventa por cento, e ganha quem oferecer o maior desconto. O gasto do governo tem um teto de quinze bilhões de reais.",
  "vis": {"type": "cards", "title": "O Desenrola 3.0", "cards": [["1", "Até R$ 10 mil", "dívidas de pessoas\nfísicas (valor original)"], ["2", "Deságio de 90%+", "vence o maior\ndesconto"], ["3", "Teto de R$ 15 bi", "para a União\ncomprar"]],
          "highlight": 1, "caption": "Fonte: Medida Provisória 1.393/2026"}},
 {"say": "Em outubro, o Ministério da Fazenda chamou bancos, fundos e securitizadoras para oferecer as carteiras. O ministro falou em até noventa bilhões de reais em dívidas antigas. Com noventa por cento de desconto, o governo pagaria no máximo nove bilhões. Pela medida, o devedor poderá quitar com um desconto de até o mesmo percentual que a União conseguiu, ou parcelar.",
  "vis": {"type": "timeline", "even": True, "points": [["25/set", "MP publicada"], ["22/out", "bancos convocados"], ["nov/dez", "leilão previsto"], ["2/dez", "votação na comissão"]],
          "caption": "Até R$ 90 bi em dívidas → no máximo R$ 9 bi"}},
 {"say": "Mas atenção: as regras ainda podem mudar. A medida provisória precisa ser votada pelo Congresso. A comissão que analisa o texto foi instalada nesta semana, com votação prevista para o começo de dezembro. E o leilão, previsto para novembro, pode ficar para dezembro.",
  "vis": {"type": "bullets", "title": "O que ainda está em aberto", "items": ["Votação da MP no Congresso", "Data final do leilão", "Desconto final das carteiras", "Regras do parcelamento (CMN)"], "highlight": 0,
          "caption": "Fontes: Portaria MF 3.127/2026; Ministério da Fazenda e Congresso, via imprensa (nov/2026)"}},
 {"say": "Na prática, o governo vira um comprador de dívida, como a Recovery. Com uma diferença de objetivo: a ideia é passar o desconto para quem deve, e não lucrar com ele. A minha análise: o programa depende do preço do leilão. Se o desconto final for grande de verdade, o alívio é real. Se for pequeno, a conta do devedor muda pouco.",
  "vis": {"type": "compare", "left": ["Comprador privado", "paga uma fração", "cobra mais do que pagou", "objetivo: lucro"], "right": ["União no Desenrola", "paga no máximo 10%", "desconto de até o mesmo %", "objetivo: alívio"],
          "caption": "Análise do canal · regras sujeitas à votação da MP e à regulamentação"}},

 # ---------- OS SEUS DIREITOS ----------
 # REENGAJE ~6:30
 {"say": "Agora, o que você precisa saber se a sua dívida foi vendida. Primeiro: a venda é legal e não depende da sua autorização. Mas, pelo artigo duzentos e noventa do Código Civil, ela só vale contra você depois que você é notificado. Se você pagou o credor antigo antes de saber, está protegido. E atenção: para o Superior Tribunal de Justiça, a falta de aviso não apaga a dívida.",
  "vis": {"type": "bullets", "title": "Se a sua dívida foi vendida", "items": ["A venda é legal", "Vale contra você após o aviso", "Pagou o antigo antes? Vale", "Falta de aviso não apaga a dívida"], "highlight": 1,
          "caption": "Fontes: Código Civil, arts. 290 e 292; jurisprudência do STJ"}},
 {"say": "Segundo: a dívida passa como era, com o mesmo contrato por trás. Por isso, vale conferir se a cobrança identifica o contrato original: número, valor, data. E desconfie. Golpista também manda mensagem dizendo que comprou a sua dívida. Negocie só por canais oficiais, que você mesmo procurou.",
  "vis": {"type": "cards", "title": "Antes de pagar", "cards": [["1", "Confira", "número, valor e\ndata do contrato"], ["!", "Desconfie", "golpistas imitam\ncobradores"], ["✓", "Canal oficial", "procure você,\nnão clique no link"]],
          "highlight": 1, "caption": "Análise do canal · não é recomendação financeira"}},
 {"say": "Terceiro: o relógio. Pelo Código de Defesa do Consumidor, o nome só pode ficar negativado por até cinco anos. Para a maior parte das dívidas de consumo, o prazo de prescrição também é de cinco anos. E, em dois mil e vinte e três, o STJ decidiu que dívida prescrita não pode ser cobrada nem na Justiça nem fora dela. Nada de ligação ou mensagem cobrando. Em dois mil e vinte e quatro, a mesma turma disse que ela ainda pode aparecer numa plataforma de negociação.",
  "vis": {"type": "timeline", "even": True, "points": [["Dia 0", "a dívida vence"], ["5 anos", "sai do cadastro negativo"], ["Prescrita", "não pode ser cobrada"]],
          "caption": "CDC art. 43 §1º · CC art. 206 §5º · STJ REsp 2.088.100 e 2.103.726"}},

 # ---------- QUEM GANHA ----------
 {"say": "Então, quem ganha nesse mercado? O banco ganha dinheiro em caixa e limpa o balanço. O comprador ganha na diferença entre o que pagou e o que recebe. E o devedor pode ganhar um desconto que o banco original dificilmente daria. O lado ruim é a cobrança insistente, e a dívida antiga que reaparece quando você já tinha esquecido dela.",
  "vis": {"type": "flow", "nodes": ["Banco", "Comprador", "Feirão", "Você"], "notes": ["vende com deságio", "cobra com desconto", "a oferta chega", "paga menos ou nada"], "pulse": True,
          "caption": "Análise do canal"}},

 # ---------- FECHAMENTO ----------
 {"say": "Recapitulando as cinco etiquetas. Mil reais no contrato. Algo entre cem e duzentos no atacado. Um comprador especializado. Uma conta de probabilidade, acordo ou nada. E um desconto que chega até você. A mesma dívida, com preços completamente diferentes, dependendo de quem olha.",
  "vis": {"type": "tag", "recap": RECAP, "title": "A mesma dívida, cinco preços", "caption": "EXEMPLO ILUSTRATIVO"}},
 {"say": "E a lição deste episódio é esta. Uma dívida atrasada não é só um problema seu. É um produto, que se compra e se vende, com preço, mercado e lucro. Saber disso não muda o que você deve. Mas muda o jeito de ler a próxima proposta de desconto.",
  "vis": {"type": "title", "title": "A sua dívida\ntem um preço", "sub": "e não é o que está no contrato"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira, nem de investimento. É só o mapa de um mercado que quase ninguém vê.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E se o problema não for uma dívida, mas um Pix mandado para um golpista? No próximo episódio: o golpe do Pix. Para onde vai o dinheiro em poucos segundos, quem tem que devolver, e o mecanismo de devolução que quase ninguém conhece.",
  "vis": {"type": "title", "title": "Próximo: o golpe\ndo Pix", "sub": "quem devolve o seu dinheiro"}},
]
