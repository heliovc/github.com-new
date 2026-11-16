# EP15 — Score de crédito: quem decide quanto juro você paga
# Estrutura NOVA: "a prova que você faz sem saber" — o score visto como uma prova de 6 questões, com o peso de cada
# questão (cena nova: exam) e um velocímetro de 0 a 1.000 (cena nova: gauge). Abre com dois vizinhos (EXEMPLO
# ILUSTRATIVO) que pedem o mesmo empréstimo e pagam juros diferentes; depois: quem aplica a prova (os birôs),
# de onde veio (FICO e a lei brasileira), as 6 questões da menor para a maior, o boletim do Brasil, o círculo vicioso,
# os seus direitos, e o fechamento.
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação em pistas), EP12 (contrato em 5 cláusulas),
# EP13 (prédio em 5 andares), EP14 (cebola em 5 camadas).
# Promessa do EP14 cumprida ("quem calcula o seu score, o que faz ele subir ou cair, e por que dois vizinhos pagam
# juros diferentes pelo mesmo empréstimo").
# Loops: (1) "qual questão vale mais?" -> questão 6; (2) "o mito de que consultar o próprio score derruba a nota" -> questão 3.
# Re-engajamentos: ~3:00 começa a prova; ~6:00 o boletim do Brasil.
# Números/fatos: Serasa, FAQ do Serasa Score 2.0 (escala 0-1.000, faixas, pesos 29/24/21/12/8/6, consulta própria não
# afeta); Serasa, Mapa Score do Brasil (média 548 em abr/2025, 542 em abr/2026; 500 aos 18-25 anos, 603 acima de 65),
# via release e imprensa (ago/2026); Serasa, Mapa da Inadimplência (84,2 milhões em set/2026, R$ 597,4 bilhões), via
# imprensa (02/11/2026); BC, "Análise dos efeitos do Cadastro Positivo" (2021): diferença de 31 p.p. na taxa do crédito
# pessoal não consignado, amostra com taxa média de 299% a.a.; Equifax, 10-K de 2023 (compra da Boa Vista em
# 07/08/2023, ~US$ 510 milhões em dinheiro); Quod (cinco grandes bancos, constituída em 2017); FICO (fundada em 1956,
# score geral em 1989); Lei 12.414/2011; LC 166/2019; STJ, Súmulas 550 (2015) e 548; LGPD, art. 20.
# Exemplo dos vizinhos (R$ 10 mil em 24 meses a 4% e 7% ao mês) = EXEMPLO ILUSTRATIVO, cálculo do canal (Price).
TITLE = "Score de crédito: a prova secreta que decide quanto juro você paga"

QS = ["Contratos ativos", "Seus dados", "Busca por crédito", "Dívidas", "Tempo de mercado", "Pagar em dia"]
WS = [6, 8, 12, 21, 24, 29]
SRC_W = "Fonte dos pesos: Serasa, perguntas frequentes do Serasa Score 2.0"
SCENES = [
 # ---------- GANCHO: DOIS VIZINHOS ----------
 {"say": "Dois vizinhos. Mesmo prédio, mesmo salário, mesmo banco. Os dois pedem dez mil reais emprestados, para pagar em dois anos. Um recebe a proposta de quatro por cento ao mês. O outro, de sete. No fim, um paga quinze mil e setecentos. O outro paga quase vinte e um mil.",
  "vis": {"type": "compare", "left": ["Vizinho A", "R$ 10 mil em 24x", "4% ao mês", "paga R$ 15.741"], "right": ["Vizinho B", "R$ 10 mil em 24x", "7% ao mês", "paga R$ 20.925"],
          "caption": "EXEMPLO ILUSTRATIVO · cálculo do canal (parcelas fixas)"}},
 {"say": "A diferença é de mais de cinco mil reais. Pelo mesmo dinheiro, no mesmo prazo. E nenhum dos dois sabe direito por quê. O que separa os dois é um número de três ou quatro dígitos, calculado sem que eles tenham pedido, com dados que eles nunca viram juntos. O score de crédito.",
  "vis": {"type": "bignumber", "from": 0, "to": 5184, "prefix": "R$ ", "decimals": 0, "warn": True, "caption": "a mais, pelo mesmo empréstimo",
          "source": "EXEMPLO ILUSTRATIVO · cálculo do canal"}},
 {"say": "No episódio passado, a gente viu que o calote é a maior camada do juro no Brasil. Hoje, a pergunta é: como o banco decide quem tem cara de caloteiro? A resposta é uma prova. Uma prova que você faz todos os dias, sem saber que está fazendo, e que tem seis questões.",
  "vis": {"type": "exam", "n": 0, "qs": QS, "weights": WS, "title": "A prova que você\nfaz sem saber", "sub": "POR TRÁS DO DINHEIRO"}},
 {"say": "E cada questão tem um peso. Antes de começar, pense: qual você acha que vale mais? A maioria das pessoas aposta nas dívidas, no nome sujo. Guarde a sua aposta. A gente confere na última questão.",
  "vis": {"type": "bullets", "title": "Qual questão vale mais?", "items": ["Ter dívida no nome", "Pagar as contas em dia", "Consultar muito o CPF", "Ter cartão há muito tempo"], "highlight": 0,
          "caption": "Guarde a sua aposta"}},

 # ---------- QUEM APLICA A PROVA ----------
 {"say": "Primeiro: quem aplica essa prova? Não é o banco, pelo menos não sozinho. São empresas chamadas birôs de crédito. Elas juntam informações sobre milhões de pessoas e vendem para quem empresta dinheiro. No Brasil, quatro nomes dominam esse mercado.",
  "vis": {"type": "cards", "title": "Quem aplica a prova", "cards": [["S", "Serasa", "Serasa Experian,\ndo grupo Experian"], ["B", "Boa Vista", "comprada pela\nEquifax em 2023"], ["Q", "Quod", "criada pelos cinco\nmaiores bancos"], ["$", "SPC Brasil", "ligado ao comércio\n(CNDL)"]],
          "highlight": 0, "caption": "Cada birô tem o seu próprio modelo e a sua própria nota"}},
 {"say": "A Serasa é a mais conhecida. A Boa Vista foi comprada pela americana Equifax, em agosto de dois mil e vinte e três, num negócio de mais de meio bilhão de dólares. A Quod foi criada em dois mil e dezessete por Banco do Brasil, Bradesco, Caixa, Itaú e Santander. E o SPC nasceu do comércio. Cada um tem a sua fórmula. Por isso, o mesmo CPF pode ter notas diferentes em cada birô.",
  "vis": {"type": "timeline", "even": True, "points": [["2017", "nasce a Quod"], ["2019", "cadastro positivo automático"], ["2023", "Equifax compra a Boa Vista"]],
          "caption": "Fontes: Equifax, relatório anual de 2023; Quod; Lei Complementar 166/2019"}},
 {"say": "E a nota vai de zero a mil. Na escala da Serasa, até trezentos é baixo. De trezentos e um a quinhentos, regular. De quinhentos e um a setecentos, bom. Acima de setecentos, excelente. O número tenta responder uma pergunta só: qual a chance de você pagar as suas contas em dia nos próximos meses.",
  "vis": {"type": "gauge", "title": "A nota: de 0 a 1.000", "needles": [], "caption": "Faixas do Serasa Score 2.0 · fonte: Serasa"}},

 # ---------- DE ONDE VEIO ----------
 {"say": "Essa ideia não nasceu aqui. Em mil novecentos e cinquenta e seis, um engenheiro e um matemático americanos, Bill Fair e Earl Isaac, fundaram uma empresa para transformar o risco de crédito em estatística. Em mil novecentos e oitenta e nove, ela lançou o score FICO, que virou o padrão nos Estados Unidos.",
  "vis": {"type": "timeline", "even": True, "points": [["1956", "nasce a Fair Isaac"], ["1989", "o score FICO"], ["2011", "lei do cadastro positivo"], ["2019", "vira automático"]],
          "caption": "Fontes: FICO; Lei 12.414/2011; Lei Complementar 166/2019"}},
 {"say": "No Brasil, a virada veio em duas leis. Em dois mil e onze, nasceu o cadastro positivo, o histórico de quem paga em dia. Só que era preciso pedir para entrar, e quase ninguém pedia. Em dois mil e dezenove, uma lei complementar inverteu a regra: todo mundo entra automaticamente, e quem não quiser precisa pedir para sair.",
  "vis": {"type": "compare", "left": ["Até 2019", "você pedia para entrar", "quase ninguém pedia", "o banco via só o calote"], "right": ["Desde 2019", "todo mundo entra", "quem quiser, pede para sair", "o banco vê quem paga"],
          "caption": "Fontes: Lei 12.414/2011; Lei Complementar 166/2019"}},
 {"say": "E aí vem uma pergunta justa: alguém pode calcular uma nota sobre mim sem me pedir licença? A Justiça já respondeu. Em dois mil e quinze, o Superior Tribunal de Justiça decidiu, na súmula quinhentos e cinquenta, que o score é legal e não depende do seu consentimento. Mas, se você pedir, eles têm que explicar quais informações usaram e de onde elas vieram.",
  "vis": {"type": "cards", "title": "O que a Justiça decidiu", "cards": [["✓", "É legal", "o score não precisa\ndo seu consentimento"], ["?", "Mas explique", "você pode pedir as fontes\ne os dados usados"]],
          "highlight": 1, "caption": "Fonte: STJ, Súmula 550 (2015)"}},

 # ---------- A PROVA: 6 QUESTÕES ----------
 # REENGAJE ~3:00
 {"say": "Agora, a prova. A Serasa divulga quanto pesa cada parte da nota. Não divulga a fórmula, mas divulga os pesos. E eu vou abrir as seis questões da menor para a maior. Questão um, a mais leve: os contratos de crédito que você tem ativos. Quantos são e há quanto tempo existem. Seis por cento.",
  "vis": {"type": "exam", "n": 1, "qs": QS, "weights": WS, "title": "Os contratos\nque você tem", "sub": "quantos e há quanto tempo", "caption": SRC_W}},
 {"say": "Questão dois: os seus dados cadastrais. Se o endereço e o telefone estão atualizados, se você é sócio de alguma empresa. Oito por cento. Parece burocracia, mas é coerência: para o modelo, quem mantém os dados em dia costuma ser mais fácil de encontrar e de cobrar.",
  "vis": {"type": "exam", "n": 2, "qs": QS, "weights": WS, "title": "Os seus dados", "sub": "atualizados e coerentes", "caption": SRC_W}},
 {"say": "Questão três: a busca por crédito. Toda vez que uma empresa consulta o seu CPF para te oferecer um empréstimo ou um cartão, isso fica registrado. Muitas consultas em pouco tempo acendem um alerta: parece alguém desesperado atrás de dinheiro. Doze por cento.",
  "vis": {"type": "exam", "n": 3, "qs": QS, "weights": WS, "title": "A busca\npor crédito", "sub": "empresas consultando\no seu CPF", "caption": SRC_W}},
 {"say": "E aqui cai um mito muito comum. Consultar o seu próprio score não derruba a nota. Quem conta são as consultas feitas por empresas que concedem crédito. Você pode olhar o seu número quantas vezes quiser.",
  "vis": {"type": "compare", "left": ["Você consulta", "o próprio score", "no app ou no site", "não afeta a nota"], "right": ["Empresas consultam", "o seu CPF", "várias, em pouco tempo", "pode pesar"],
          "caption": "Fonte: Serasa"}},
 {"say": "Questão quatro: as dívidas negativadas. O famoso nome sujo. Vinte e um por cento. É bastante, mas repare: não é a questão mais pesada. E tem um detalhe que pouca gente sabe. Quando você paga uma dívida negativada, o credor tem cinco dias úteis para pedir a retirada do seu nome do cadastro de inadimplentes. Isso também é uma súmula do mesmo tribunal, a quinhentos e quarenta e oito.",
  "vis": {"type": "exam", "n": 4, "qs": QS, "weights": WS, "title": "As dívidas\nnegativadas", "sub": "o nome sujo\npagou? 5 dias úteis para limpar", "caption": SRC_W + " · STJ, Súmula 548"}},
 {"say": "Questão cinco: a sua experiência com o mercado. Há quanto tempo você tem conta, cartão, financiamento. Vinte e quatro por cento. É aqui que mora uma armadilha para os mais jovens. Quem nunca usou crédito não tem histórico. E, para o modelo, quem não tem histórico é uma incógnita. E incógnita, no crédito, custa caro.",
  "vis": {"type": "exam", "n": 5, "qs": QS, "weights": WS, "title": "O tempo\nde mercado", "sub": "há quanto tempo\nvocê usa crédito", "caption": SRC_W}},
 {"say": "E a questão seis, a mais pesada de todas: pagar em dia. Os seus hábitos de pagamento registrados no cadastro positivo. Contas de luz, de água, de telefone, parcelas, faturas. Vinte e nove por cento. Se você apostou nas dívidas, errou. O score olha mais para o que você paga do que para o que você deve.",
  "vis": {"type": "exam", "n": 6, "qs": QS, "weights": WS, "title": "Pagar em dia", "sub": "o cadastro positivo\na questão que mais vale", "caption": SRC_W}},
 {"say": "Somando: pagar em dia e o tempo de mercado valem mais da metade da prova. Cinquenta e três por cento. As dívidas, que todo mundo teme, valem pouco mais de um quinto. É uma mudança de lógica. O sistema antigo só via o lado ruim, o calote. O de hoje tenta enxergar também o lado bom.",
  "vis": {"type": "stack", "title": "A prova inteira", "parts": [["Em dia", 29, "#3AC47D", "29%\npagar em dia"], ["Mercado", 24, "#5B8DEF", "24%\ntempo"], ["Dívidas", 21, "#E06C5A", "21%\nnome sujo"], ["Outros", 26, "#4A5876", "26%\nconsultas, dados, contratos"]], "highlight": 0,
          "caption": SRC_W + " · soma = cálculo do canal"}},

 # ---------- O QUE ISSO VALE EM JURO ----------
 {"say": "E isso vale dinheiro? Vale. Em dois mil e vinte e um, o Banco Central publicou um estudo sobre os efeitos do cadastro positivo. Numa amostra de crédito pessoal sem consignado, quem tinha nota no cadastro conseguiu, em média, uma taxa trinta e um pontos percentuais menor por ano do que quem não tinha.",
  "vis": {"type": "bignumber", "from": 0, "to": 31, "suffix": " pontos", "decimals": 0, "caption": "a menos na taxa anual para quem tinha nota no cadastro positivo",
          "source": "Fonte: Banco Central, Análise dos efeitos do Cadastro Positivo (2021) · crédito pessoal não consignado, amostra"}},
 {"say": "Parece muito, e é. Mas atenção ao contexto: naquela amostra, a taxa média era altíssima, perto de trezentos por cento ao ano. É o tipo de crédito mais caro que existe. Mesmo assim, a lógica é a mesma para qualquer empréstimo: quanto mais o banco sabe que você paga, menos ele cobra pelo risco de você não pagar.",
  "vis": {"type": "flow", "nodes": ["Você paga em dia", "Cadastro registra", "Score sobe", "Juro cai"], "notes": ["conta, fatura, parcela", "histórico positivo", "risco menor", "menos camada de calote"], "pulse": True,
          "caption": "Análise do canal · a camada do calote foi o tema do EP14"}},

 # ---------- O BOLETIM DO BRASIL ----------
 # REENGAJE ~6:00
 {"say": "Agora vamos olhar o boletim do país inteiro. A Serasa publica a média do score dos brasileiros. Em abril de dois mil e vinte e cinco, era quinhentos e quarenta e oito. Em abril de dois mil e vinte e seis, caiu para quinhentos e quarenta e dois. Ainda na faixa boa, mas descendo.",
  "vis": {"type": "gauge", "title": "A média do Brasil", "needles": [[542, "abril de 2026", "#F2A93B"]],
          "caption": "Fonte: Serasa, Mapa Score do Brasil (abr/2025: 548; abr/2026: 542), via imprensa"}},
 {"say": "E a idade pesa. Entre os jovens de dezoito a vinte e cinco anos, a média é de quinhentos pontos, na fronteira entre regular e bom. Acima dos sessenta e cinco anos, chega a seiscentos e três. É a questão cinco, o tempo de mercado, aparecendo na prática.",
  "vis": {"type": "gauge", "title": "A idade pesa", "needles": [[603, "65+ anos", "#3AC47D"], [500, "18 a 25 anos", "#E06C5A"]], "big": False,
          "caption": "Fonte: Serasa, Mapa Score do Brasil (abr/2026), via imprensa"}},
 {"say": "E por que a média caiu? Porque a inadimplência não para de bater recorde. Segundo a Serasa, em setembro de dois mil e vinte e seis, o Brasil chegou a oitenta e quatro vírgula dois milhões de pessoas inadimplentes. As dívidas somadas passam de quinhentos e noventa e sete bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 84.2, "suffix": " milhões", "decimals": 1, "warn": True, "caption": "de brasileiros inadimplentes em setembro de 2026 (recorde)",
          "source": "Fonte: Serasa, Mapa da Inadimplência (divulgado em 02/11/2026), via imprensa · dívidas: R$ 597,4 bilhões"}},

 # ---------- O CÍRCULO VICIOSO ----------
 {"say": "E aqui está a parte desconfortável dessa história, a minha análise. O score cria um círculo. Quem atrasa uma conta perde pontos. Com menos pontos, paga um juro maior. Com juro maior, a parcela pesa mais, e fica mais difícil pagar em dia. E aí perde mais pontos.",
  "vis": {"type": "flow", "nodes": ["Atrasa", "Score cai", "Juro sobe", "Parcela pesa"], "notes": ["uma conta", "menos pontos", "mais risco no preço", "e atrasa de novo"], "pulse": True,
          "caption": "Análise do canal"}},
 {"say": "O mesmo vale ao contrário. Quem já tem crédito barato paga com mais folga, mantém o histórico limpo e ganha mais pontos. O score não cria a desigualdade, mas pode amplificar a que já existe. É por isso que o vizinho B, lá do começo, tende a continuar sendo o vizinho B, se nada mudar.",
  "vis": {"type": "compare", "left": ["Círculo bom", "crédito barato", "parcela cabe", "score sobe"], "right": ["Círculo ruim", "crédito caro", "parcela aperta", "score cai"],
          "caption": "Análise do canal · os vizinhos são um EXEMPLO ILUSTRATIVO"}},
 {"say": "E tem um outro lado, que é o lado a favor do sistema. Antes do cadastro positivo automático, o banco só enxergava quem tinha dado calote. Quem pagava tudo em dia, mas nunca tinha tido cartão, era invisível, e pagava como se fosse arriscado. O cadastro positivo deu um jeito de ser visto para quem paga a conta de luz e nunca teve crédito.",
  "vis": {"type": "title", "title": "Pagar a conta de luz\ntambém conta", "sub": "o histórico positivo enxerga quem era invisível"}},

 # ---------- OS SEUS DIREITOS ----------
 {"say": "Por fim, o que a lei garante para você nessa prova. São quatro coisas. Um: você pode pedir quais dados e quais fontes foram usados no seu score. Dois: pela lei de proteção de dados, você pode pedir a revisão de uma decisão tomada só por algoritmo. Três: você pode sair do cadastro positivo, se quiser. E quatro: pagou uma dívida negativada, o nome tem que ser limpo em até cinco dias úteis.",
  "vis": {"type": "bullets", "title": "O que a lei garante", "items": ["Saber os dados e as fontes do score", "Pedir revisão de decisão automática", "Sair do cadastro positivo", "Nome limpo em 5 dias úteis após pagar"], "highlight": 1,
          "caption": "Fontes: STJ, Súmulas 550 e 548; LGPD (Lei 13.709/2018), art. 20; Lei 12.414/2011"}},
 {"say": "Um cuidado: sair do cadastro positivo é um direito, mas tem um efeito colateral. A questão que mais pesa na prova é justamente a do pagamento em dia. Sem esse histórico, o modelo tem menos informação boa sobre você. Não é uma recomendação, é só como a conta funciona.",
  "vis": {"type": "compare", "left": ["Ficar no cadastro", "o banco vê", "quem paga em dia", "a questão de 29% conta"], "right": ["Sair do cadastro", "o banco vê", "menos sobre você", "a questão de 29% some"],
          "caption": "Análise do canal com os pesos da Serasa · não é recomendação"}},

 # ---------- FECHAMENTO ----------
 {"say": "Então, vamos corrigir a prova inteira. Seis questões. Contratos, seis por cento. Dados, oito. Busca por crédito, doze. Dívidas, vinte e um. Tempo de mercado, vinte e quatro. E pagar em dia, vinte e nove, a que mais vale.",
  "vis": {"type": "exam", "n": -1, "qs": QS, "weights": WS, "title": "A prova\ncorrigida", "sub": "pagar em dia vale mais", "caption": SRC_W}},
 {"say": "E a lição deste episódio é esta. O juro que você paga não é só o preço do dinheiro. É o preço da sua história, contada por um algoritmo que você não vê. Os dois vizinhos do começo ganham o mesmo salário. O que muda é o que o sistema sabe, ou acha que sabe, sobre cada um.",
  "vis": {"type": "title", "title": "O juro é o preço\nda sua história", "sub": "contada por um algoritmo que você não vê"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira, nem de investimento. É só a prova aberta, para você entender quem dá a nota e como ela é calculada.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E falando em calote: o que acontece com uma dívida que ninguém paga? Muitas vezes, o banco vende essa dívida para outra empresa, por uma fração do valor. No próximo episódio, vamos entrar no mercado bilionário das dívidas vendidas. Quem compra, quanto paga, e por que essa empresa pode aceitar um desconto enorme no feirão de renegociação.",
  "vis": {"type": "title", "title": "Próximo: quem compra\na sua dívida", "sub": "o mercado das dívidas vendidas"}},
]
