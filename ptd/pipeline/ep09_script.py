# EP09 — Banco Master: o banco que pagava demais (e quem paga a conta quando um banco quebra)
# Estrutura NOVA: "investigação de acidente aéreo" — abrimos a caixa-preta e ouvimos 4 trechos do voo:
# Trecho 1 A decolagem (2019-2024: ativos de R$ 3,7 bi a R$ 82 bi com CDB a até 140% do CDI),
# Trecho 2 Os alarmes (alertas ignorados: Warren 2023, BC desde 2022), Trecho 3 O pouso forçado (BRB, 2025),
# Trecho 4 A queda (17-18/11/2025) + O paraquedas (FGC: como funciona e quem paga) + o laudo (indiciamento out/2026).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia) e EP08 (truque em 4 atos).
# Cenas novas: blackbox (caixa-preta laranja com onda de áudio) e flight (rota de voo com alarmes e queda).
# Loops: (1) como um banco paga 140% do CDI -> Trecho 1; (2) quem avisou antes -> Trecho 2;
#        (3) quem paga a conta de R$ 40 bilhões -> O paraquedas.
# Re-engajamentos: ~3:00 os alarmes (31 ofícios do BC); ~6:00 o paraquedas (o FGC perdeu R$ 17 bi de patrimônio).
# Exemplo com R$ 10 mil e CDI de 15% é ILUSTRATIVO (marcado na tela).
TITLE = "Banco Master: o banco que pagava demais (e quem pagou a conta de R$ 40 bilhões)"

SCENES = [
 # ---------- GANCHO ----------
 {"say": "Dezessete de novembro de dois mil e vinte e cinco, noite, aeroporto de Guarulhos. O dono de um banco que tinha crescido mais de vinte vezes em cinco anos está prestes a embarcar num jatinho para o exterior. A Polícia Federal chega antes da decolagem.",
  "vis": {"type": "timeline", "even": True, "points": [["17/nov", "noite: prisão em Guarulhos"], ["18/nov", "manhã: Operação Compliance Zero"], ["18/nov", "liquidação do banco"]],
          "caption": "Fonte: Polícia Federal e Banco Central, via Diário de Pernambuco e InfoMoney"}},
 {"say": "Na manhã seguinte, o Banco Central decreta a liquidação do Banco Master. E começa a maior operação de resgate da história do Fundo Garantidor de Créditos: cerca de quarenta bilhões de reais para devolver a mais de um milhão de investidores.",
  "vis": {"type": "bignumber", "from": 0, "to": 40.6, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "warn": True, "caption": "estimativa líquida do FGC para cobrir as garantias do Master",
          "source": "Fonte: FGC, nov/2025, via NeoFeed e InfoMoney"}},
 {"say": "Hoje vamos fazer o que se faz depois de todo acidente aéreo: abrir a caixa-preta. Ouvir a decolagem, os alarmes que tocaram e ninguém desligou, a tentativa de pouso forçado e a queda. E, no fim, responder a pergunta que interessa para você: quando um banco cai, quem paga a conta?",
  "vis": {"type": "title", "title": "A caixa-preta\ndo Banco Master", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "E já adianto uma coisa: o paraquedas que salvou os investidores não é do governo. Ele é pago, todo mês, por um grupo de que você provavelmente faz parte.",
  "vis": {"type": "bullets", "title": "O que tem na caixa-preta", "items": ["Trecho 1: a decolagem", "Trecho 2: os alarmes", "Trecho 3: o pouso forçado", "Trecho 4: a queda (e o paraquedas)"], "highlight": 3}},

 # ---------- TRECHO 1: A DECOLAGEM ----------
 {"say": "Trecho um. A decolagem. Toda investigação começa pelo plano de voo.",
  "vis": {"type": "blackbox", "n": 1, "title": "A decolagem", "sub": "de banco pequeno a 23º do país", "time": "2019 – 2024"}},
 {"say": "Em dois mil e dezenove, o empresário mineiro Daniel Vorcaro já comandava um banco pequeno chamado Banco Máxima, que depois ganharia o nome de Banco Master. Naquele ano, a instituição tinha três vírgula sete bilhões de reais em ativos. Em dois mil e vinte e quatro, tinha oitenta e dois bilhões. Saiu da nonagésima para a vigésima terceira posição entre os maiores do país.",
  "vis": {"type": "line", "title": "Ativos do conglomerado Master (R$ bilhões)", "points": [["2019", 3.7], ["2024", 82]], "prefix": "R$ ", "suffix": " bi", "decimals": 1, "color": "#F2A93B",
          "caption": "Fonte: dados do Banco Central compilados pela imprensa (Revista Oeste, TMC), 2025"}},
 {"say": "Um crescimento de mais de dois mil por cento em cinco anos. Para comparar, um banco médio saudável costuma crescer alguns pontos percentuais por ano. Então a primeira pergunta do investigador é: qual era o combustível desse avião?",
  "vis": {"type": "bignumber", "from": 0, "to": 2123, "suffix": "%", "decimals": 0, "warn": True, "caption": "crescimento dos ativos do Master entre 2019 e 2024",
          "source": "Fonte: dados do Banco Central compilados pela imprensa (TMC), 2025"}},
 {"say": "O combustível tinha nome: CDB. O Master captava dinheiro vendendo certificados de depósito bancário em plataformas de investimento. E pagava muito. Havia papéis rendendo até cento e quarenta por cento do CDI, quando bancos parecidos costumavam pagar algo entre cento e dez e cento e vinte por cento.",
  "vis": {"type": "bars", "title": "Quanto pagava um CDB (% do CDI)", "items": [["Bancos médios (faixa)", 120, "#5B8DEF"], ["Banco Master (até)", 140, "#E06C5A"]], "suffix": "%", "decimals": 0,
          "caption": "Fontes: Nord Investimentos e Seu Dinheiro (2025) — faixas aproximadas"}},
 {"say": "Num exemplo ilustrativo, com o CDI a quinze por cento ao ano: dez mil reais a cem por cento do CDI rendem mil e quinhentos reais brutos em um ano. A cento e quarenta por cento, rendem dois mil e cem. Seiscentos reais a mais, no mesmo produto, com o mesmo selo de garantia. É fácil entender por que tanta gente comprou.",
  "vis": {"type": "compare", "left": ["100% do CDI", "R$ 10.000 aplicados", "R$ 1.500 em 1 ano", "rendimento bruto"], "right": ["140% do CDI", "R$ 10.000 aplicados", "R$ 2.100 em 1 ano", "R$ 600 a mais"],
          "caption": "Exemplo ilustrativo: CDI de 15% ao ano, antes do imposto de renda"}},
 {"say": "Mas aqui está o problema que todo piloto conhece. Combustível caro precisa de um motor que gere ainda mais. Se você paga vinte e um por cento ao ano pelo dinheiro, precisa aplicar esse dinheiro em algo que renda mais do que isso. E coisas que rendem muito, quase sempre, são arriscadas ou difíceis de vender.",
  "vis": {"type": "flow", "nodes": ["CDB caro", "Precisa render mais", "Ativos arriscados", "Difíceis de vender"], "notes": ["até 140% do CDI", "para fechar a conta", "precatórios, participações", "o dinheiro fica preso"], "pulse": True,
          "caption": "Análise do canal: o descasamento que derruba bancos"}},
 {"say": "Foi o que aconteceu, segundo reportagens e investigações. Boa parte do dinheiro foi parar em ativos de difícil venda: precatórios, que são dívidas do governo reconhecidas pela Justiça e que podem levar anos para ser pagas, participações em empresas e créditos a receber. A Polícia Federal e o Ministério Público ainda investigam suspeitas de compra de precatórios a preços inflados.",
  "vis": {"type": "cards", "title": "Onde o dinheiro foi parar", "cards": [["1", "Precatórios", "dívidas do governo\nque demoram anos"], ["2", "Participações", "fatias de\nempresas"], ["3", "Créditos", "valores a\nreceber"]],
          "highlight": 0, "caption": "Fonte: Times Brasil e Band, 2025-2026 — suspeitas em investigação"}},
 {"say": "Repare no desenho. De um lado, o investidor podia pedir o dinheiro de volta no vencimento do CDB, em datas certas. Do outro, o banco tinha aplicado esse dinheiro em coisas que não viram dinheiro rápido. É como um avião que decola com combustível só para a ida.",
  "vis": {"type": "compare", "left": ["O que o banco devia", "CDBs com data marcada", "dinheiro prometido", "no vencimento"], "right": ["O que o banco tinha", "ativos difíceis de vender", "valor incerto", "sem data para virar caixa"],
          "caption": "Análise do canal sobre o descasamento entre captação e aplicação"}},

 # ---------- TRECHO 2: OS ALARMES ----------
 {"say": "Trecho dois. Os alarmes. Em quase todo acidente, a caixa-preta mostra que algum alarme tocou antes. Aqui, tocaram vários.",
  "vis": {"type": "blackbox", "n": 2, "title": "Os alarmes", "sub": "quem avisou antes da queda", "time": "2022 – 2024"}},
 # REENGAJE ~3:00
 {"say": "O primeiro alarme veio de dentro do próprio sistema. Segundo um relatório da Diretoria de Fiscalização do Banco Central, revelado pelo Correio Braziliense, as irregularidades e a piora da liquidez do conglomerado estavam no radar desde dois mil e vinte e dois. O Banco Central mandou trinta e um ofícios exigindo ajustes.",
  "vis": {"type": "bignumber", "from": 0, "to": 31, "suffix": " ofícios", "decimals": 0, "warn": True, "caption": "do Banco Central ao Master exigindo ajustes, desde 2022",
          "source": "Fonte: relatório da Diretoria de Fiscalização do BC, via Correio Braziliense, abr/2026"}},
 {"say": "O segundo alarme tocou no mercado. Em agosto de dois mil e vinte e três, a corretora Warren enviou um relatório aos clientes desaconselhando a compra de CDBs do Master. E, em outubro daquele ano, o Banco Central mudou a forma como precatórios contam no cálculo de risco dos bancos, apertando justamente o tipo de ativo que o Master tinha de sobra.",
  "vis": {"type": "flight", "title": "O voo do Master", "points": [["2019", 8], ["2021", 35], ["2022", 60], ["2023", 78], ["2024", 90], ["2025", 70], ["nov/25", 0]],
          "alerts": [[2, "BC: irregularidades\nno radar"], [3, "Warren desaconselha CDBs;\nBC aperta precatórios"]],
          "caption": "Ilustração da trajetória; alertas: Correio Braziliense (abr/2026) e Times Brasil (2025)"}},
 {"say": "O terceiro alarme é o mais grave. Segundo uma nota técnica do Banco Central, citada pela Band, em novembro de dois mil e vinte e quatro o modelo de negócios do banco teria ficado insustentável. Ou seja: um ano antes da queda, o avião já estaria sem combustível para chegar ao destino.",
  "vis": {"type": "flight", "title": "O voo do Master", "points": [["2019", 8], ["2021", 35], ["2022", 60], ["2023", 78], ["2024", 90], ["2025", 70], ["nov/25", 0]],
          "alerts": [[2, "BC: irregularidades\nno radar"], [3, "Warren desaconselha\nos CDBs"], [4, "nota técnica do BC:\nmodelo insustentável"]],
          "caption": "Ilustração da trajetória; nota técnica do BC via Band, jan/2026"}},
 {"say": "E por que o avião continuou voando? Aqui entra a peça mais importante desta história. O próprio banco usava como argumento de venda a garantia do Fundo Garantidor de Créditos. Para o investidor, a conta parecia simples: se o banco quebrar, o FGC devolve até duzentos e cinquenta mil reais. Então, para que olhar o risco do banco?",
  "vis": {"type": "flow", "nodes": ["Investidor vê o FGC", "Não olha o risco", "Banco capta mais", "Arrisca mais"], "notes": ["até R$ 250 mil garantidos", "só a taxa importa", "a 140% do CDI", "e o ciclo continua"], "pulse": True,
          "caption": "Análise do canal: o risco moral da garantia; argumento de venda via Correio Braziliense"}},
 {"say": "Os economistas chamam isso de risco moral. Quando alguém sabe que vai ser protegido da perda, passa a tomar mais risco. O FGC existe para proteger o pequeno poupador, e isso é bom. Mas um banco pode usar essa proteção como motor. E foi exatamente essa a suspeita que a investigação levantou: um modelo de negócio fortemente apoiado na cobertura do fundo.",
  "vis": {"type": "title", "title": "Risco moral", "sub": "quando a garantia vira o motor do avião"}},

 # ---------- TRECHO 3: O POUSO FORÇADO ----------
 {"say": "Trecho três. O pouso forçado. Quando o combustível acaba, o piloto procura uma pista. A pista do Master tinha nome: BRB, o Banco de Brasília, controlado pelo governo do Distrito Federal.",
  "vis": {"type": "blackbox", "n": 3, "title": "O pouso forçado", "sub": "a tentativa de venda ao BRB", "time": "2025"}},
 {"say": "Em vinte e oito de março de dois mil e vinte e cinco, o BRB anunciou que ia comprar cinquenta e oito por cento do Master, num negócio avaliado em cerca de dois bilhões de reais. Faltava só uma assinatura: a do Banco Central.",
  "vis": {"type": "stack", "title": "O que o BRB queria comprar (% do Master)", "parts": [["Fatia do BRB", 58, "#5B8DEF", "~R$ 2 bi"], ["Ficaria com os sócios", 42, "#3A4A66", ""]],
          "caption": "Fonte: anúncio de 28/03/2025, via InfoMoney e Suno"}},
 {"say": "Durante cinco meses, a operação virou novela em Brasília, com pressão política dos dois lados. Na noite de três de setembro, o Banco Central disse não. Rejeitou a compra, sem detalhar publicamente os motivos. A pista estava fechada.",
  "vis": {"type": "timeline", "even": True, "points": [["28/mar/2025", "BRB anuncia compra"], ["abr–ago", "novela em Brasília"], ["3/set/2025", "BC rejeita"]],
          "caption": "Fonte: Banco Central, via InfoMoney e Mercado & Consumo, set/2025"}},
 {"say": "Só que, segundo a investigação, o BRB já tinha embarcado antes do pouso. A Polícia Federal e o Ministério Público apontam que o Master vendeu ao banco de Brasília doze vírgula dois bilhões de reais em carteiras de crédito que não existiam de verdade. As defesas negam irregularidades.",
  "vis": {"type": "bignumber", "from": 0, "to": 12.2, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "warn": True, "caption": "em carteiras de crédito supostamente inexistentes vendidas ao BRB",
          "source": "Fonte: PF e MPF, via Correio Braziliense — as defesas negam"}},

 # ---------- TRECHO 4: A QUEDA ----------
 {"say": "Trecho quatro. A queda. E, como em todo acidente, os últimos minutos são os mais rápidos.",
  "vis": {"type": "blackbox", "n": 4, "title": "A queda", "sub": "48 horas em novembro", "time": "17 – 18/11/2025"}},
 {"say": "Na noite de dezessete de novembro, Vorcaro foi preso em Guarulhos, quando se preparava para embarcar num jatinho rumo ao exterior. Na manhã seguinte, a Polícia Federal deflagrou a Operação Compliance Zero, contra a emissão de títulos de crédito falsos. E, no mesmo dia, o Banco Central decretou a liquidação extrajudicial do Master.",
  "vis": {"type": "flight", "title": "O voo do Master", "points": [["2019", 8], ["2021", 35], ["2022", 60], ["2023", 78], ["2024", 90], ["2025", 70], ["nov/25", 0]],
          "alerts": [[2, "BC: irregularidades\nno radar"], [4, "modelo\ninsustentável"], [5, "BC veta\no BRB"]], "crash": True, "crash_from": 5,
          "caption": "Ilustração da trajetória; fontes: PF e Banco Central, nov/2025"}},
 {"say": "Liquidação extrajudicial é o fim da linha para um banco. O Banco Central afasta os donos, nomeia um liquidante, e o banco para de funcionar. A partir daí, quem tinha dinheiro lá vira credor. E é nesse momento que abre o paraquedas.",
  "vis": {"type": "flow", "nodes": ["Liquidação", "Donos afastados", "Liquidante assume", "Clientes viram credores"], "notes": ["decretada pelo BC", "fim da gestão", "vende o que sobrou", "e esperam o FGC"], "pulse": True,
          "caption": "Como funciona uma liquidação extrajudicial"}},
 {"say": "Uma nota importante: Vorcaro foi solto cerca de dez dias depois, com tornozeleira eletrônica. Em março de dois mil e vinte e seis, numa nova fase da operação, foi preso de novo, e segue preso. Ele nega as acusações.",
  "vis": {"type": "timeline", "even": True, "points": [["17/nov/2025", "preso em Guarulhos"], ["~10 dias", "solto com tornozeleira"], ["mar/2026", "preso de novo"]],
          "caption": "Fonte: BP Money, Agência Brasil — ele nega as acusações"}},

 # ---------- O PARAQUEDAS ----------
 # REENGAJE ~6:00
 {"say": "Agora, o paraquedas. O Fundo Garantidor de Créditos não é do governo. É uma entidade privada, sem fins lucrativos, mantida pelos próprios bancos e financeiras associados. Todo mês, cada um deles deposita no fundo uma pequena parte do dinheiro que guarda dos clientes.",
  "vis": {"type": "cards", "title": "O paraquedas: como o FGC funciona", "cards": [["1", "Quem paga", "os bancos,\ntodo mês"], ["2", "Quem protege", "até R$ 250 mil\npor CPF e banco"], ["3", "Quanto custou", "~R$ 40,6 bi\nno caso Master"]],
          "highlight": 2, "caption": "Fonte: FGC; estimativa do caso Master via NeoFeed, nov/2025"}},
 {"say": "Quem tinha até duzentos e cinquenta mil reais no Master recebe tudo de volta pelo fundo. Quem tinha mais recebe o teto e entra na fila dos credores pelo resto, sem prazo e sem garantia. O FGC estimou uma base de cerca de um vírgula seis milhão de credores. Os pagamentos começaram dois meses depois, e, em janeiro de dois mil e vinte e seis, o fundo já tinha pago trinta e dois vírgula cinco bilhões de reais a setenta e cinco por cento deles.",
  "vis": {"type": "bignumber", "from": 0, "to": 32.5, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "caption": "pagos pelo FGC a 75% dos credores do Master até jan/2026",
          "source": "Fonte: FGC, via Agência Brasil, jan/2026"}},
 {"say": "Um paraquedas desse tamanho faz um buraco no fundo. O patrimônio do FGC, que era de cento e quarenta vírgula quatro bilhões em dois mil e vinte e quatro, fechou dois mil e vinte e cinco em cento e vinte e três vírgula dois bilhões, já descontada uma provisão de dezessete vírgula um bilhões para as garantias.",
  "vis": {"type": "bars", "title": "Patrimônio do FGC (R$ bilhões)", "items": [["2024", 140.4, "#3AC47D"], ["2025", 123.2, "#E06C5A"]], "prefix": "R$ ", "suffix": " bi", "decimals": 1,
          "caption": "Fonte: FGC, via CNN Brasil e Diário do Comércio — inclui provisão de R$ 17,1 bi"}},
 {"say": "E aí vem a resposta para a pergunta do começo. Para recompor o fundo, foi aprovado em fevereiro de dois mil e vinte e seis um plano com uma contribuição extra de cinquenta por cento sobre o valor mensal que os bancos pagam. Ou seja: os bancos que não quebraram estão pagando a conta do banco que quebrou.",
  "vis": {"type": "bignumber", "from": 0, "to": 50, "prefix": "+", "suffix": "%", "decimals": 0, "warn": True, "caption": "contribuição extraordinária dos bancos ao FGC no plano de recomposição",
          "source": "Fonte: plano de recomposição do FGC, fev/2026, via Let's Money"}},
 {"say": "E quem paga os bancos? Numa análise do canal, a resposta mais honesta é: os clientes. Custo maior para captar dinheiro tende a aparecer em algum lugar, seja num CDB que rende um pouco menos, seja numa tarifa ou num juro um pouco maior. O paraquedas do Master não saiu de graça. Ele está sendo costurado, devagar, por todo o sistema.",
  "vis": {"type": "flow", "nodes": ["Banco quebra", "FGC paga", "Bancos repõem o fundo", "Custo chega ao cliente"], "notes": ["Master", "~R$ 40,6 bi", "+50% na contribuição", "análise do canal"], "pulse": True,
          "caption": "Análise do canal: quem paga a conta no fim"}},
 {"say": "O sistema também mudou as regras. A partir de primeiro de junho de dois mil e vinte e seis, o Conselho Monetário Nacional dobrou a contribuição adicional cobrada de bancos que dependem demais de captação garantida pelo FGC. O limite de duzentos e cinquenta mil reais por pessoa e por banco não mudou.",
  "vis": {"type": "compare", "left": ["Antes", "contribuição adicional: 0,01%", "cobrada acima de 75%", "de captação garantida"], "right": ["Desde jun/2026", "contribuição adicional: 0,02%", "cobrada acima de 60%", "limite de R$ 250 mil mantido"],
          "caption": "Fonte: resolução do CMN, via InvestNews e Nord Investimentos"}},

 # ---------- O LAUDO ----------
 {"say": "E o laudo do acidente? Em vinte e oito de outubro de dois mil e vinte e seis, há menos de duas semanas, a Polícia Federal indiciou Daniel Vorcaro e mais catorze pessoas, entre elas o ex-presidente do BRB, por gestão fraudulenta, organização criminosa e lavagem de dinheiro. O relatório foi para a Procuradoria-Geral da República, que decide se denuncia.",
  "vis": {"type": "obit", "case": "LAUDO", "name": "Vorcaro + 14", "born": "Compliance Zero: nov/2025", "died": "indiciamento: 28/10/2026", "cause": "gestão fraudulenta, organização criminosa e lavagem",
          "note": "indiciado não é condenado; a defesa chama de precipitado", "stamp": "EM ANDAMENTO", "stamp_col": "#2E86C1", "caption": "Fonte: Polícia Federal, via Agência Brasil, out/2026"}},
 {"say": "Indiciamento não é condenação. A defesa de Vorcaro chama o indiciamento de precipitado e diz que faltam provas técnicas. O caso deve chegar ao Supremo Tribunal Federal e ainda pode levar anos.",
  "vis": {"type": "bullets", "title": "Onde o caso está", "items": ["PF: 15 indiciados (out/2026)", "PGR decide se denuncia", "Julgamento deve ir ao STF", "As defesas negam os crimes"], "highlight": 1,
          "caption": "Fonte: Agência Brasil, out/2026"}},

 # ---------- PAYOFF ----------
 {"say": "Então, o que a caixa-preta do Master ensina? Primeiro: quando um banco paga muito mais que os outros pelo mesmo produto, a pergunta não é quanto eu ganho, e sim por que ele precisa tanto do meu dinheiro. Segundo: o FGC protege o poupador, mas tem limite, tem fila e tem custo. E terceiro: os alarmes quase sempre tocam antes. O difícil é alguém ter coragem de ouvi-los.",
  "vis": {"type": "bullets", "title": "O que a caixa-preta ensina", "items": ["Taxa alta demais é uma pergunta", "O FGC tem limite, fila e custo", "Os alarmes tocam antes", "Quem paga o paraquedas: o sistema"], "highlight": 0}},
 {"say": "Isso não é recomendação de investimento. É só o jeito de ler o painel do avião antes de embarcar.",
  "vis": {"type": "title", "title": "Taxa alta demais\né uma pergunta.", "sub": "análise do canal — não é recomendação"}},
 {"say": "No próximo episódio, o juro mais caro do Brasil. Por que o rotativo do cartão de crédito chegou a passar de quatrocentos por cento ao ano, o que mudou com o teto criado pela lei, e quem ganha com cada parcela que você atrasa.",
  "vis": {"type": "title", "title": "Próximo: o rotativo\ndo cartão", "sub": "o juro mais caro do Brasil"}},
]
