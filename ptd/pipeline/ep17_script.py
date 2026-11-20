# EP17 — O golpe do Pix: para onde vai o dinheiro em segundos, quem tem que devolver, e o MED (Mecanismo Especial de Devolução)
# Estrutura NOVA: "o cronômetro do golpe" — o mesmo golpe acompanhado em 6 marcas de tempo: 0 segundo (o Pix sai),
# segundos (o dinheiro se espalha), 1 hora (a sua reação), 72 horas (o bloqueio), 11 dias (a devolução), 80 dias (o prazo
# e quem paga). Cena nova: clock (cronômetro com anel de progresso + régua das marcas; recap com os 6 cronômetros).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação), EP12 (contrato), EP13 (prédio), EP14 (cebola), EP15 (prova),
# EP16 (etiquetas).
# Promessa do EP16 cumprida ("o golpe do Pix: para onde vai o dinheiro em poucos segundos, quem tem que devolver, e o
# mecanismo de devolução que quase ninguém conhece").
# Loop: "por que 9 em cada 10 pedidos são negados?" -> marca 5. Re-engajamentos: ~3:00 (a hora de ouro); ~6:30 (quem paga).
# Números/fatos: Banco Central, balanço de meios de pagamento do 1º sem./2026 (divulgado 27/10/2026, via imprensa): Pix =
# 55,2% das transações, ticket médio R$ 459; FBSP, Anuário 2026: 2,26 milhões de estelionatos registrados em 2025;
# Res. BCB 103/2021 (MED, em vigor desde 16/11/2021); Res. BCB 142/2021 (limite noturno de R$ 1.000 entre 20h e 6h para
# pessoas físicas, ajustável) e 147/2021 (bloqueio cautelar de até 72 h pela instituição do recebedor);
# Res. BCB 493/2025 (MED 2.0: rastreio do dinheiro além da 1ª conta, obrigatório desde 02/02/2026; prazo de 80 dias para
# pedir); botão de contestação no app desde 01/10/2025; BC: devolução em até 11 dias após a contestação (estimativa);
# O POVO (jul/2026), com dados do BC de jan/2022 a abr/2026: R$ 24,52 bi em golpes notificados, R$ 2,2 bi devolvidos
# (8,9%), R$ 13,7 bi não devolvidos por falta de saldo na conta do golpista; SBT News (ago/2026), dados do BC de
# jan-abr/2026: 11,8 mi pedidos, 10,7 mi recusados (90,3%), R$ 264,7 mi devolvidos; BC: em cerca de 80% dos casos sem
# devolução falta saldo na conta recebedora (via imprensa, 2025); STJ, Súmula 479 e decisões recentes (falsa central:
# banco não responde se as transações são compatíveis com o perfil do cliente).
# Exemplo do golpe de R$ 3.000 (falsa central, 4 contas) = EXEMPLO ILUSTRATIVO.
TITLE = "Golpe do Pix: para onde vai o seu dinheiro em segundos (e quem tem que devolver)"

MARKS = ["0 s", "segundos", "1 h", "72 h", "11 dias", "80 dias"]
RECAP = [["0", "segundo", "o Pix sai"], ["10", "segundos", "o dinheiro\nse espalha"], ["1", "hora", "a sua reação"],
         ["72", "horas", "o bloqueio"], ["11", "dias", "a devolução"], ["80", "dias", "o prazo final"]]
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Você recebe uma ligação. Do outro lado, alguém que diz ser do seu banco. Há uma compra suspeita na sua conta, e para proteger o seu dinheiro você precisa fazer um Pix para uma conta de segurança. Você faz. Três mil reais. E em poucos segundos, esse dinheiro já não está mais lá.",
  "vis": {"type": "clock", "n": 0, "label": "0:00", "unit": "o Pix sai", "frac": 0.02, "col": "#E06C5A", "kicker": "UM GOLPE COMUM",
          "title": "Três mil reais.\nSegundos.", "sub": "e o dinheiro sumiu", "caption": "EXEMPLO ILUSTRATIVO · golpe da falsa central"}},
 {"say": "E o mais duro vem depois. Desde que o Banco Central criou o mecanismo de devolução do Pix, de cada cem reais que as vítimas disseram ter perdido em golpes, menos de nove voltaram. Mais de vinte e quatro bilhões notificados. Pouco mais de dois bilhões devolvidos.",
  "vis": {"type": "bignumber", "from": 100, "to": 8.9, "prefix": "R$ ", "decimals": 2, "warn": True, "caption": "voltam de cada R$ 100 notificados em golpes no Pix",
          "source": "Fonte: Banco Central, dados de jan/2022 a abr/2026, via O POVO (jul/2026): R$ 24,52 bi notificados, R$ 2,2 bi devolvidos"}},
 {"say": "Hoje a gente vai ligar um cronômetro. São seis marcas de tempo, do segundo zero até o octogésimo dia. Em cada uma, o que acontece com o seu dinheiro, o que você pode fazer, e quem tem obrigação de devolver.",
  "vis": {"type": "title", "title": "O cronômetro\ndo golpe do Pix", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "E guarde uma pergunta para o meio do caminho. Se existe um mecanismo oficial de devolução, por que nove em cada dez pedidos são negados? A resposta está na marca cinco.",
  "vis": {"type": "title", "title": "Por que 9 em cada 10\npedidos são negados?", "sub": "a resposta está na marca 5"}},

 # ---------- MARCA 1: 0 SEGUNDO ----------
 {"say": "Marca um: o segundo zero. O momento em que você aperta o botão. E aqui está o primeiro ponto que quase ninguém percebe. Para o sistema, esse Pix não tem nada de errado. Foi você quem digitou a senha, no seu celular, no seu aplicativo. O golpe não quebrou a segurança do banco. Ele convenceu você.",
  "vis": {"type": "clock", "n": 1, "label": "0", "unit": "segundo", "frac": 0.02, "head": "O PIX SAI", "title": "Foi você\nquem apertou", "sub": "e isso muda tudo", "marks": MARKS}},
 {"say": "Esse tipo de golpe tem nome: engenharia social. A falsa central do banco. O falso parente, com número novo de celular. A loja que não existe. O falso emprego que pede uma taxa. Muda a história, mas o objetivo é sempre o mesmo: fazer com que a própria vítima mande o dinheiro.",
  "vis": {"type": "cards", "title": "Muda a história, não o objetivo", "cards": [["1", "Falsa central", "\"proteja o seu\ndinheiro\""], ["2", "Falso parente", "\"troquei de\nnúmero\""], ["3", "Loja falsa", "preço bom\ndemais"], ["4", "Falso emprego", "\"pague a taxa\""]],
          "highlight": 0, "caption": "Análise do canal"}},
 {"say": "E o tamanho do problema é enorme. Em dois mil e vinte e cinco, o Brasil registrou mais de dois milhões e duzentos mil estelionatos. E o Pix virou o principal meio de pagamento do país. No primeiro semestre deste ano, ele foi usado em mais da metade de todas as transações.",
  "vis": {"type": "stack", "title": "Transações de pagamento no Brasil (1º sem. 2026)", "parts": [["Pix", 55.2, "#3AC47D", "55,2%"], ["Cartões", 30.8, "#5B8DEF", "30,8%"], ["Outros", 14.0, "#7884A0", "boleto, TED e outros"]], "highlight": 0,
          "caption": "Fontes: Banco Central, balanço de meios de pagamento (out/2026), via imprensa; FBSP, Anuário 2026 (2,26 mi de estelionatos em 2025)"}},

 # ---------- MARCA 2: SEGUNDOS ----------
 {"say": "Marca dois: os primeiros segundos. O Pix é liquidado na hora. O dinheiro não fica em trânsito, como numa transferência antiga. Ele cai na conta de destino em segundos. E é exatamente essa velocidade, a maior qualidade do Pix, que o golpista usa a seu favor.",
  "vis": {"type": "clock", "n": 2, "label": "10", "unit": "segundos", "frac": 0.12, "head": "O DINHEIRO SE ESPALHA", "title": "Chega na hora.\nSai na hora.", "sub": "a velocidade vira arma", "marks": MARKS,
          "caption": "Tempo ilustrativo · o Pix é liquidado em segundos"}},
 {"say": "Porque a conta que recebe o seu dinheiro quase nunca é do golpista. É de um laranja. Alguém que emprestou, vendeu ou teve a conta roubada. E dessa primeira conta o dinheiro pula para uma segunda, uma terceira, uma quarta. Às vezes vira saque, criptomoeda ou boleto pago.",
  "vis": {"type": "flow", "nodes": ["Você", "Laranja 1", "Laranja 2", "Laranja 3", "Saque"], "notes": ["R$ 3.000", "recebe", "repassa", "repassa", "some"], "pulse": True,
          "caption": "EXEMPLO ILUSTRATIVO · o caminho em camadas"}},
 {"say": "Por que tantas camadas? Porque cada pulo ganha tempo. Enquanto a vítima ainda está tentando entender o que aconteceu, o dinheiro já passou por várias contas, em bancos diferentes. E cada banco só enxerga a sua parte do caminho. Para quem investiga, é como montar um quebra-cabeça com as peças espalhadas em cinco casas diferentes.",
  "vis": {"type": "cards", "title": "Por que o golpista usa laranjas", "cards": [["1", "Esconde o dono", "a conta não está\nno nome dele"], ["2", "Ganha tempo", "cada pulo atrasa\no rastreio"], ["3", "Espalha o rastro", "bancos diferentes,\npeças separadas"]],
          "highlight": 1, "caption": "Análise do canal"}},
 {"say": "Durante quatro anos, o mecanismo de devolução só enxergava a primeira conta. Se o dinheiro já tivesse saído de lá, não havia o que bloquear. Era como tentar fechar a porta depois que o ladrão já virou a esquina.",
  "vis": {"type": "compare", "left": ["MED original", "desde nov/2021", "olha só a 1ª conta", "saiu? não há o que bloquear"], "right": ["MED 2.0", "obrigatório desde fev/2026", "segue o dinheiro", "várias camadas de contas"],
          "caption": "Fontes: Resoluções BCB 103/2021 e 493/2025"}},

 # ---------- MARCA 3: 1 HORA ----------
 # REENGAJE ~3:00
 {"say": "Marca três: a primeira hora. Essa é a marca mais importante do vídeo, porque é a única que depende de você. Cada minuto conta. Quanto antes você avisa, maior a chance de ainda existir saldo em alguma conta do caminho.",
  "vis": {"type": "clock", "n": 3, "label": "1", "unit": "hora", "frac": 0.3, "col": "#3AC47D", "head": "A SUA REAÇÃO", "title": "A hora\nde ouro", "sub": "a única marca que depende de você", "marks": MARKS}},
 {"say": "Desde outubro de dois mil e vinte e cinco, os aplicativos dos bancos têm de oferecer um botão de contestação do Pix. Você abre o comprovante, toca em contestar, explica que foi golpe. Não precisa ligar, nem esperar atendente. O pedido vai direto para o banco de quem recebeu.",
  "vis": {"type": "bullets", "title": "O que fazer na primeira hora", "items": ["Contestar o Pix no app do banco", "Avisar o banco pelos canais oficiais", "Registrar boletim de ocorrência", "Guardar prints e comprovantes"], "highlight": 0,
          "caption": "Fonte: Banco Central (botão de contestação desde 01/10/2025) · informativo, não é recomendação"}},
 {"say": "Um detalhe importante: esse caminho é para golpe, fraude ou coação. Não serve para arrependimento de compra, briga com uma loja ou chave digitada errada. Nesses casos, a conversa é outra, com quem recebeu, e às vezes na Justiça.",
  "vis": {"type": "compare", "left": ["Serve para", "golpe", "fraude", "coação"], "right": ["Não serve para", "arrependimento", "briga com a loja", "chave digitada errada"],
          "caption": "Fonte: Banco Central, regras do Mecanismo Especial de Devolução"}},
 {"say": "E existe uma barreira que você pode ativar antes de qualquer golpe. Desde dois mil e vinte e um, o Pix entre pessoas físicas tem limite de mil reais à noite, das oito da noite às seis da manhã. Você pode baixar esse limite, e aumentar não é imediato: o banco tem prazo para atender. É um freio de propósito.",
  "vis": {"type": "timeline", "even": True, "points": [["20h", "começa o limite"], ["R$ 1.000", "teto padrão à noite"], ["6h", "volta o limite do dia"]],
          "caption": "Resolução BCB 142/2021 · aumento leva de 24 a 48 horas"}},

 # ---------- MARCA 4: 72 HORAS ----------
 {"say": "Marca quatro: setenta e duas horas. Quando o pedido chega ao banco de quem recebeu, o dinheiro que ainda estiver na conta suspeita é bloqueado. E o próprio banco recebedor, se desconfiar de uma transferência, pode segurar o valor por até setenta e duas horas, antes mesmo de qualquer reclamação.",
  "vis": {"type": "clock", "n": 4, "label": "72", "unit": "horas", "frac": 0.48, "col": "#5B8DEF", "head": "O BLOQUEIO", "title": "O dinheiro\nfica congelado", "sub": "se ainda estiver lá", "marks": MARKS,
          "caption": "Bloqueio cautelar: Resolução BCB 147/2021"}},
 {"say": "Com o MED dois ponto zero, obrigatório desde fevereiro de dois mil e vinte e seis, os bancos passaram a seguir o dinheiro pelas contas seguintes, e a bloquear o que encontrarem pelo caminho. É a mudança mais importante desde a criação do mecanismo. Na prática, a pergunta deixou de ser só onde o dinheiro caiu, e passou a ser para onde ele foi depois. Os bancos trocam essas informações entre si, por canais internos, sem que você precise fazer nada além da contestação.",
  "vis": {"type": "flow", "nodes": ["Contestação", "Conta 1", "Conta 2", "Conta 3", "Bloqueio"], "notes": ["você avisa", "rastreia", "rastreia", "rastreia", "o que sobrou"], "pulse": True,
          "caption": "Fonte: Resolução BCB 493/2025 (MED 2.0, obrigatório desde 02/02/2026)"}},
 {"say": "Mas repare na frase: o que encontrarem. O bloqueio só pega o saldo que ainda existe. Se o laranja já sacou tudo, a conta está vazia, e não há o que congelar. É aqui que começa a resposta da nossa pergunta.",
  "vis": {"type": "title", "title": "Só bloqueia\no que sobrou", "sub": "conta vazia não devolve nada"}},

 # ---------- MARCA 5: 11 DIAS ----------
 {"say": "Marca cinco: onze dias. É a estimativa do Banco Central para o dinheiro voltar, quando o golpe é confirmado. Quem analisa não é o Banco Central. São os bancos envolvidos. Eles conferem o caso e decidem se aceitam ou recusam o pedido.",
  "vis": {"type": "clock", "n": 5, "label": "11", "unit": "dias", "frac": 0.7, "col": "#F2A93B", "head": "A DEVOLUÇÃO", "title": "Quem decide\né o banco", "sub": "não o Banco Central", "marks": MARKS,
          "caption": "Fonte: Banco Central (estimativa de até 11 dias após a contestação)"}},
 {"say": "E os números são duros. Entre janeiro e abril deste ano, as vítimas abriram onze milhões e oitocentos mil pedidos. Dez milhões e setecentos mil foram recusados. Noventa por cento. No mesmo período, duzentos e sessenta e quatro milhões de reais voltaram para as vítimas.",
  "vis": {"type": "bars", "title": "Pedidos de devolução (jan-abr/2026)", "items": [["Abertos", 11.8, "#5B8DEF"], ["Recusados", 10.7, "#E06C5A"]],
          "suffix": " milhões", "decimals": 1, "caption": "Fonte: Banco Central, via SBT News (ago/2026) · R$ 264,7 milhões devolvidos no período"}},
 {"say": "Agora, a resposta da pergunta. Por que tanta recusa? O principal motivo, segundo o Banco Central, é simples: falta de saldo. A conta que recebeu já estava vazia. Nos dados desde dois mil e vinte e dois, treze vírgula sete bilhões de reais não voltaram por esse motivo. É a maior parte de tudo o que se perdeu.",
  "vis": {"type": "bignumber", "from": 0, "to": 13.7, "prefix": "R$ ", "suffix": " bilhões", "decimals": 1, "warn": True, "caption": "não voltaram porque a conta do golpista já estava vazia",
          "source": "Fonte: Banco Central, dados de jan/2022 a abr/2026, via O POVO (jul/2026)"}},
 {"say": "Há também pedidos recusados porque o caso não era golpe, ou porque faltaram informações. Mas a lição central é esta: o mecanismo de devolução não é um seguro. Ele é uma corrida. Ele só devolve o que conseguir alcançar antes do golpista. E quando a devolução acontece, pode ser parcial: volta o que foi encontrado, não necessariamente tudo o que você mandou.",
  "vis": {"type": "title", "title": "Não é um seguro.\nÉ uma corrida.", "sub": "análise do canal"}},
 {"say": "Repare que a culpa da recusa, na maior parte das vezes, não é de quem decide. É do tempo. Por isso, a marca três, a primeira hora, vale mais do que todas as outras juntas. E por isso os bancos investem cada vez mais em detectar a conta laranja antes de o dinheiro chegar nela.",
  "vis": {"type": "cards", "title": "Por que a devolução falha", "cards": [["1", "Sem saldo", "o laranja\njá sacou"], ["2", "Não era golpe", "acordo, compra\nou erro"], ["3", "Faltou prova", "pedido\nincompleto"]],
          "highlight": 0, "caption": "Fonte: Banco Central, via imprensa · análise do canal"}},

 # ---------- MARCA 6: 80 DIAS ----------
 # REENGAJE ~6:30
 {"say": "Marca seis: oitenta dias. É o prazo máximo para pedir a devolução pelo mecanismo, contado a partir do Pix. Passou disso, o caminho pelo aplicativo fecha. E aí sobra a pergunta que mais gente faz: e o banco? O banco não tem que devolver?",
  "vis": {"type": "clock", "n": 6, "label": "80", "unit": "dias", "frac": 1.0, "col": "#E06C5A", "head": "O PRAZO FINAL", "title": "E o banco\nnão paga?", "sub": "depende de uma coisa", "marks": MARKS,
          "caption": "Fonte: Resolução BCB 493/2025 (prazo de 80 dias para pedir)"}},
 {"say": "Depende. Uma súmula do Superior Tribunal de Justiça diz que o banco responde por fraudes de terceiros dentro das suas operações. Por exemplo, quando alguém invade a sua conta, ou quando o sistema deixa passar algo que deveria ter barrado.",
  "vis": {"type": "bullets", "title": "Quando o banco tende a responder", "items": ["Falha no sistema de segurança", "Conta invadida sem a sua senha", "Pix muito fora do seu perfil", "Banco não bloqueou após o aviso"], "highlight": 2,
          "caption": "STJ, Súmula 479 · cada caso é analisado pela Justiça"}},
 {"say": "Mas, quando foi a própria vítima que fez o Pix, enganada por um golpista, decisões recentes do STJ têm afastado a culpa do banco, se as transferências eram compatíveis com o perfil do cliente. O critério que mais pesa é este: o Pix era normal para você, ou destoava de tudo o que você costuma fazer?",
  "vis": {"type": "compare", "left": ["Pix atípico", "valor muito alto", "horário fora do padrão", "o banco deveria barrar"], "right": ["Pix compatível", "valor do dia a dia", "padrão de sempre", "a culpa tende a não ser do banco"],
          "caption": "Fonte: decisões recentes do STJ (golpe da falsa central), via imprensa jurídica · não é orientação jurídica"}},
 {"say": "A minha análise: o sistema brasileiro cobra caro da vítima pelo erro de ter sido convencida. Em outros países, a discussão é se os bancos deveriam dividir esse prejuízo. Aqui, a aposta do Banco Central foi outra: rastrear melhor o dinheiro e caçar as contas laranja. O MED dois ponto zero ainda está sendo testado na prática.",
  "vis": {"type": "title", "title": "Quem paga o golpe?\nNa maioria das vezes, você", "sub": "análise do canal"}},
 {"say": "Então, o que de fato protege? Três hábitos simples. Antes de confirmar qualquer Pix, leia o nome de quem vai receber, que aparece na tela. Banco de verdade não pede transferência para conta de segurança, nunca. E, se a ligação parecer urgente demais, desligue e ligue você mesmo para o número que está no verso do cartão.",
  "vis": {"type": "cards", "title": "Os três freios", "cards": [["1", "Leia o nome", "quem recebe aparece\nantes de confirmar"], ["!", "Conta de segurança", "não existe"], ["✓", "Desligue", "e ligue você\npara o banco"]],
          "highlight": 1, "caption": "Análise do canal · informativo, não é recomendação"}},

 # ---------- FECHAMENTO ----------
 {"say": "Recapitulando o cronômetro. No segundo zero, o Pix sai, e foi você quem apertou. Em segundos, o dinheiro se espalha por contas laranja. Na primeira hora, a sua reação decide quase tudo. Em setenta e duas horas, o que sobrou é bloqueado. Em onze dias, pode voltar. E em oitenta dias, o prazo acaba.",
  "vis": {"type": "clock", "recap": RECAP, "title": "As 6 marcas do golpe", "caption": "Prazos: Banco Central · tempos de 10 segundos e 1 hora são ilustrativos"}},
 {"say": "E a lição deste episódio é esta. A velocidade que fez o Pix dar certo é a mesma que faz o golpe dar certo. Contra um sistema que leva segundos, a sua melhor defesa é desconfiar antes, e agir rápido depois.",
  "vis": {"type": "title", "title": "Desconfie antes.\nAja rápido depois.", "sub": "a velocidade vale para os dois lados"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira nem orientação jurídica. Em caso de golpe, procure o seu banco pelos canais oficiais e registre um boletim de ocorrência.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira nem jurídica"}},
 {"say": "E se a ligação da falsa central viesse de um banco que você nunca ouviu falar? No próximo episódio: os bancos que ninguém conhece. As instituições de pagamento que viraram gigantes sem agência, como elas ganham dinheiro, e por que algumas delas acabam virando porta de entrada para contas laranja.",
  "vis": {"type": "title", "title": "Próximo: os bancos\nque ninguém conhece", "sub": "as instituições de pagamento"}},
]
