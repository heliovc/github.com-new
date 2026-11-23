# EP18 — Os bancos que ninguém conhece: as instituições de pagamento (IPs), como ganham dinheiro, onde fica o seu saldo,
# por que viraram porta dos fundos para dinheiro sujo e contas laranja, e como o Banco Central fechou o cerco.
# Estrutura NOVA: "a vistoria" — uma IP vistoriada como uma casa, cômodo por cômodo: 1 a fachada (o que é), 2 o caixa
# (como ganha), 3 o cofre (onde fica o seu saldo), 4 a porta dos fundos (conta-bolsão, laranjas, ataques), 5 o fiscal
# (o aperto do BC e da Receita). Cena nova: house (planta da casa com o cômodo atual aceso).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação), EP12 (contrato), EP13 (prédio), EP14 (cebola), EP15 (prova),
# EP16 (etiquetas), EP17 (cronômetro).
# Promessa do EP17 cumprida ("os bancos que ninguém conhece: as instituições de pagamento que viraram gigantes sem agência,
# como ganham dinheiro, e por que algumas acabam virando porta de entrada para contas laranja").
# Loop: "o seu saldo está protegido se a empresa quebrar?" -> cômodo 3. Re-engajamentos: ~3:30 (o cofre); ~6:00 (o fiscal).
# Fatos e fontes:
# - Lei 12.865/2013 (cria arranjos e instituições de pagamento; art. 12: recursos em conta de pagamento são patrimônio
#   separado, não respondem por obrigações da IP e não entram na falência/liquidação).
# - Regras do BC: saldo de conta de pagamento aplicado em espécie no BC ou em títulos públicos federais (via imprensa e
#   votos do BC); conta de pagamento sem cobertura do FGC (FGC/Serasa/imprensa).
# - Will Bank: liquidação extrajudicial decretada pelo BC em 21/01/2026; saldo em conta de pagamento bloqueado, sem FGC,
#   devolução depende do liquidante, sem prazo (Jornal de Brasília, Diario de Pernambuco, InfoMoney, jan/2026).
# - IPs autorizadas passam de 200 (Finsiders Brasil, 2026).
# - Res. BCB 246/2022: teto da tarifa de intercâmbio de 0,7% no pré-pago e 0,5% no débito desde 01/04/2023; antes, pré-pago
#   praticava 1,1% a 1,5% em média; no Nubank, intercâmbio do pré-pago = 7% da receita (jul/2021-jun/2022) (InfoMoney,
#   Finsiders, 2022).
# - Operação Carbono Oculto (28/08/2025, Receita/PF/MPSP): uma única IP movimentou mais de R$ 46 bilhões entre 2020 e 2024;
#   rede de ~1.000 postos movimentou R$ 52 bi; fintechs usadas como "bancos paralelos" com contas-bolsão (InfoMoney, CNN,
#   BBC). 2ª fase Fluxo Oculto (28/05/2026): seis fintechs, mais de R$ 26 bilhões entre 2022 e 2025 (Band, Metrópoles).
# - Receita, IN RFB 2.278/2025 (29/08/2025): IPs e fintechs passam a entregar a e-Financeira como os bancos; secretário:
#   bancos só viam o nome da fintech (conta-bolsão).
# - Ataque à C&M Software (30/06-01/07/2025): R$ 541 milhões desviados da conta reserva da BMP, segundo a Polícia Civil
#   de SP (CNN Brasil).
# - Res. BCB 494/2025 (05/09/2025): IP nova só opera depois de autorizada; prazo para as que já operavam pedirem
#   autorização antecipado de dez/2029 para maio/2026. Res. BCB 496 e 497/2025: limite de R$ 15 mil por Pix/TED para IPs
#   não autorizadas e quem usa PSTI (Agência Brasil, Forbes, set/2025). Na época, 75 IPs sem pedido e 40 aguardando
#   (CartaCapital).
# - Res. Conjunta 14 e Res. BCB 517 (03/11/2025): capital mínimo de IPs de R$ 1 mi-R$ 9 mi para R$ 9,2 mi-R$ 32,8 mi;
#   transição a partir de 01/07/2026 (25% da diferença), plena até 2028 (InfoMoney, SBT News, Bloomberg Línea).
# - FGC: cobre depósitos e investimentos garantidos até R$ 250 mil por CPF por instituição.
# Exemplo da compra de R$ 100 no pré-pago = EXEMPLO ILUSTRATIVO.
TITLE = "Os bancos que ninguém conhece: quem guarda o seu dinheiro no app (e por que o BC fechou o cerco)"

ROOMS = ["A fachada", "O caixa", "O cofre", "Porta dos fundos", "O fiscal"]
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Vinte e um de janeiro de dois mil e vinte e seis. Milhares de pessoas abrem o aplicativo do Will Bank e descobrem que o saldo está bloqueado. Não dá para sacar, nem pagar conta, nem fazer Pix. E a pergunta que todo mundo faz é: mas o FGC não garante? Para boa parte desse dinheiro, a resposta foi não.",
  "vis": {"type": "title", "title": "Saldo bloqueado.\nSem FGC.", "sub": "21 de janeiro de 2026"}},
 {"say": "Porque o dinheiro estava numa conta de pagamento. Não numa conta corrente de banco. E essa diferença, que quase ninguém lê no contrato, decide quem garante o seu saldo, quanto tempo você espera, e quem fiscaliza a empresa que guarda o seu dinheiro.",
  "vis": {"type": "compare", "left": ["Conta corrente", "num banco", "FGC até R$ 250 mil", "pode emprestar"], "right": ["Conta de pagamento", "numa instituição de pagamento", "sem FGC", "não empresta o seu saldo"],
          "caption": "Fontes: Lei 12.865/2013; FGC · liquidação do Will Bank decretada pelo Banco Central em 21/01/2026"}},
 {"say": "E não é um nicho. Mais de duzentas instituições de pagamento já têm autorização do Banco Central para funcionar. A maioria você nunca ouviu falar. Mas uma delas, sozinha, movimentou mais de quarenta e seis bilhões de reais em cinco anos, segundo a Receita Federal. E não era dinheiro limpo.",
  "vis": {"type": "bignumber", "from": 0, "to": 46, "prefix": "R$ ", "suffix": " bilhões", "decimals": 0, "warn": True, "caption": "movimentados por uma única instituição de pagamento (2020-2024)",
          "source": "Fonte: Receita Federal, Operação Carbono Oculto (ago/2025), via imprensa"}},
 {"say": "Hoje a gente vai fazer uma vistoria. Vamos entrar nesses bancos que ninguém conhece como quem entra numa casa. São cinco cômodos: a fachada, o caixa, o cofre, a porta dos fundos, e o fiscal que bate na porta.",
  "vis": {"type": "house", "n": 0, "rooms": ROOMS, "all": True, "kicker": "A VISTORIA", "title": "Os bancos que\nninguém conhece", "sub": "cinco cômodos"}},
 {"say": "E guarde uma pergunta para o meio do caminho. Se a empresa do seu aplicativo quebrar amanhã, o seu saldo está protegido? A resposta curta é: em tese, sim. Na prática, depende. E esse depende está no cômodo três.",
  "vis": {"type": "title", "title": "Se a empresa quebrar,\no seu saldo volta?", "sub": "a resposta está no cômodo 3"}},

 # ---------- CÔMODO 1: A FACHADA ----------
 {"say": "Cômodo um: a fachada. O que é, afinal, uma instituição de pagamento? A figura nasceu com uma lei de dois mil e treze, a doze mil oitocentos e sessenta e cinco. A ideia era abrir o mercado: deixar empresas que não são bancos guardarem e movimentarem dinheiro, emitirem cartões e oferecerem maquininhas.",
  "vis": {"type": "house", "n": 1, "rooms": ROOMS, "head": "A FACHADA", "title": "Parece banco.\nNão é banco.", "sub": "Lei 12.865, de 2013",
          "caption": "Fonte: Lei 12.865/2013 (arranjos e instituições de pagamento)"}},
 {"say": "Por fora, a experiência é a mesma. Você tem um aplicativo, um cartão, uma chave Pix, recebe salário e paga boleto. A diferença está no motor. Um banco pega o dinheiro dos depósitos e empresta. Uma instituição de pagamento não pode fazer isso com o seu saldo. Ela só guarda e movimenta.",
  "vis": {"type": "flow", "nodes": ["Seu saldo", "Instituição de pagamento", "Guardado", "Movimentado"], "notes": ["no app", "não é banco", "não emprestado", "Pix, boleto, cartão"],
          "caption": "Análise do canal"}},
 {"say": "E elas vêm em vários tipos. Tem a que emite a conta pré-paga, chamada de emissora de moeda eletrônica. Tem a que emite o cartão de crédito. Tem a credenciadora, que é a empresa da maquininha. E tem a iniciadora, que dispara um Pix a pedido de outro aplicativo.",
  "vis": {"type": "cards", "title": "Os tipos de instituição de pagamento", "cards": [["1", "Conta pré-paga", "moeda\neletrônica"], ["2", "Cartão de crédito", "emissor\npós-pago"], ["3", "Maquininha", "credenciador"], ["4", "Iniciador", "dispara o Pix\nde outro app"]],
          "highlight": 0, "caption": "Fonte: Banco Central, modalidades de instituição de pagamento"}},
 {"say": "Agora vem o detalhe que dá nome a este episódio. Muitas vezes, a marca que aparece no seu aplicativo não é a instituição que tem a licença. Uma empresa de varejo, um aplicativo de entrega ou uma plataforma qualquer aluga a estrutura de uma instituição de pagamento, que fica nos bastidores. É o chamado banco como serviço.",
  "vis": {"type": "compare", "left": ["O que você vê", "a marca do app", "o cartão colorido", "o atendimento"], "right": ["O que fica atrás", "a instituição licenciada", "a conta no Banco Central", "o nome no comprovante"],
          "caption": "Análise do canal · confira o nome da instituição no comprovante do Pix"}},
 {"say": "Quer saber quem guarda o seu dinheiro de verdade? Faça um Pix de um real para alguém e abra o comprovante. O nome da instituição que aparece ali é o de quem tem a licença. Muitas vezes, é um nome que você nunca viu.",
  "vis": {"type": "title", "title": "Abra o comprovante\ndo seu Pix", "sub": "o nome que aparece é quem guarda o dinheiro"}},

 # ---------- CÔMODO 2: O CAIXA ----------
 {"say": "Cômodo dois: o caixa. Se a instituição de pagamento não pode emprestar o seu saldo, e muitas não cobram tarifa nenhuma, de onde vem o dinheiro? A principal fonte, por muitos anos, foi uma taxa que você não vê. A tarifa de intercâmbio.",
  "vis": {"type": "house", "n": 2, "rooms": ROOMS, "head": "O CAIXA", "title": "Conta grátis.\nQuem paga?", "sub": "uma taxa que você não vê"}},
 {"say": "Funciona assim. Toda vez que você paga com o cartão, a loja paga uma taxa para a maquininha. Uma fatia dessa taxa vai para quem emitiu o seu cartão. Numa compra de cem reais com um cartão pré-pago, hoje essa fatia pode chegar a setenta centavos.",
  "vis": {"type": "receipt", "title": "Compra de R$ 100 no cartão pré-pago", "head": "COMPRA NO CARTÃO", "lines": [["Valor da compra", "R$ 100,00", "#141E30"], ["Loja paga taxa à", "maquininha", "#5F697D"], ["Fatia de quem emitiu", "até R$ 0,70", "#E06C5A"]],
          "total": ["Teto no pré-pago", "0,7%"], "caption": "EXEMPLO ILUSTRATIVO · teto da Resolução BCB 246/2022"}},
 {"say": "Setenta centavos parece pouco. Mas multiplique por bilhões de compras. Antes de dois mil e vinte e três, não havia teto para o pré-pago, e a tarifa média ficava entre um vírgula um e um vírgula cinco por cento. No Nubank, esse intercâmbio do pré-pago chegou a ser sete por cento de toda a receita em doze meses.",
  "vis": {"type": "bars", "title": "Tarifa de intercâmbio no cartão pré-pago", "items": [["Antes (média até)", 1.5, "#E06C5A"], ["Teto desde abr/2023", 0.7, "#3AC47D"], ["Débito (teto)", 0.5, "#5B8DEF"]],
          "suffix": "%", "decimals": 1, "caption": "Fontes: Resolução BCB 246/2022; InfoMoney (2022) · Nubank: 7% da receita entre jul/2021 e jun/2022"}},
 {"say": "Foi o Banco Central que impôs esse teto, a partir de abril de dois mil e vinte e três. Zero vírgula sete por cento no pré-pago e zero vírgula cinco no débito. E isso obrigou o setor a procurar outras fontes: crédito, por meio de empresas parceiras, maquininha, seguros, e taxas cobradas de outras empresas que alugam a estrutura.",
  "vis": {"type": "cards", "title": "Depois do teto, de onde vem o dinheiro", "cards": [["1", "Crédito", "com empresas\nparceiras"], ["2", "Maquininha", "taxa da loja"], ["3", "Banco como serviço", "aluguel da\nestrutura"], ["4", "Seguros e extras", "dentro do app"]],
          "highlight": 2, "caption": "Fonte: Resolução BCB 246/2022 (vigente desde 01/04/2023) · análise do canal"}},
 {"say": "Repare no terceiro item. Alugar a estrutura para outras empresas é um bom negócio. Quanto mais clientes, mais transações, mais receita. O problema é quando ninguém pergunta direito quem é o cliente. Guarde isso, porque é exatamente o que vamos achar no cômodo quatro.",
  "vis": {"type": "title", "title": "Mais transações,\nmais receita", "sub": "mesmo quando ninguém pergunta quem é o cliente"}},

 # ---------- CÔMODO 3: O COFRE ----------
 # REENGAJE ~3:30
 {"say": "Cômodo três: o cofre. E a resposta da nossa pergunta. Onde fica o seu saldo numa conta de pagamento? Pela regra do Banco Central, esse dinheiro não pode ficar no caixa da empresa. Ele tem que ficar depositado no próprio Banco Central, ou aplicado em títulos públicos federais.",
  "vis": {"type": "house", "n": 3, "rooms": ROOMS, "head": "O COFRE", "title": "O seu saldo\nfica separado", "sub": "no Banco Central ou em títulos públicos",
          "caption": "Fonte: regras do Banco Central para contas de pagamento"}},
 {"say": "E a lei vai além. Ela diz que o dinheiro nas contas de pagamento é um patrimônio separado. Não se mistura com o da empresa, não paga as dívidas dela, e não entra na massa da falência se ela quebrar. No papel, é uma proteção forte.",
  "vis": {"type": "bullets", "title": "O que a lei diz sobre o seu saldo", "items": ["É patrimônio separado", "Não paga dívidas da empresa", "Não entra na falência", "Não pode ser dado em garantia"], "highlight": 2,
          "caption": "Fonte: Lei 12.865/2013, artigo 12"}},
 {"say": "Então por que os clientes do Will Bank ficaram sem acesso ao dinheiro? Porque entre o papel e a prática existe um liquidante. Quando o Banco Central decreta a liquidação, tudo trava. E a devolução do saldo das contas de pagamento passa a depender do processo conduzido por esse liquidante, sem prazo definido.",
  "vis": {"type": "timeline", "even": True, "points": [["21/01/2026", "liquidação decretada"], ["Saldo", "bloqueado"], ["Devolução", "sem prazo definido"]],
          "caption": "Fontes: imprensa (Jornal de Brasília, Diario de Pernambuco, InfoMoney), jan/2026"}},
 {"say": "E aqui está a diferença para o banco. Num depósito em conta corrente, poupança ou CDB de um banco associado, o FGC paga até duzentos e cinquenta mil reais por pessoa, em semanas. Na conta de pagamento, não existe esse atalho. O dinheiro está separado, mas você espera na fila do processo.",
  "vis": {"type": "compare", "left": ["Banco", "FGC até R$ 250 mil", "pagamento em semanas", "seguro do sistema"], "right": ["Conta de pagamento", "sem FGC", "depende do liquidante", "dinheiro separado, mas travado"],
          "caption": "Fontes: FGC; Lei 12.865/2013 · análise do canal · não é recomendação"}},
 {"say": "A minha análise: a conta de pagamento é segura contra a empresa gastar o seu dinheiro. Ela não é segura contra a espera. Para quem recebe o salário ali e não tem outra conta, uma liquidação significa ficar sem acesso ao dinheiro do mês. Por isso, vale saber em que tipo de conta você está.",
  "vis": {"type": "title", "title": "Segura contra o desvio.\nNão contra a espera.", "sub": "análise do canal"}},

 # ---------- CÔMODO 4: A PORTA DOS FUNDOS ----------
 {"say": "Cômodo quatro: a porta dos fundos. E aqui a vistoria fica pesada. Lembra dos quarenta e seis bilhões? Em agosto de dois mil e vinte e cinco, a Receita Federal, a Polícia Federal e o Ministério Público de São Paulo deflagraram a Operação Carbono Oculto, contra um esquema ligado ao crime organizado no setor de combustíveis.",
  "vis": {"type": "house", "n": 4, "rooms": ROOMS, "head": "A PORTA DOS FUNDOS", "title": "O banco\nparalelo", "sub": "Operação Carbono Oculto, agosto de 2025",
          "caption": "Fonte: Receita Federal, Polícia Federal e MPSP, via imprensa"}},
 {"say": "Segundo os investigadores, fintechs funcionavam como bancos paralelos. E o truque tinha nome: a conta-bolsão. A fintech abre uma única conta num banco grande, em nome dela. Dentro dessa conta, mistura o dinheiro de milhares de clientes. O banco só enxerga o nome da fintech. Quem é o dono de cada real, ele não vê.",
  "vis": {"type": "flow", "nodes": ["Milhares de clientes", "Fintech", "Conta-bolsão", "Banco grande"], "notes": ["dinheiro misturado", "um só nome", "numa conta só", "só vê a fintech"], "pulse": True,
          "caption": "Fonte: Receita Federal, explicação à Câmara (ago/2025), via imprensa"}},
 {"say": "E isso não parou na primeira operação. Em maio de dois mil e vinte e seis, uma nova fase, chamada Fluxo Oculto, mirou seis outras fintechs que, segundo a investigação, tinham substituído as primeiras. Juntas, elas movimentaram mais de vinte e seis bilhões de reais entre dois mil e vinte e dois e dois mil e vinte e cinco.",
  "vis": {"type": "bars", "title": "Dinheiro movimentado, segundo as investigações", "items": [["Rede de postos", 52, "#E06C5A"], ["Uma instituição", 46, "#F2A93B"], ["Seis fintechs", 26, "#5B8DEF"]],
          "prefix": "R$ ", "suffix": " bi", "decimals": 0, "caption": "Postos e instituição: 2020-2024 (Carbono Oculto, ago/2025) · seis fintechs: 2022-2025 (Fluxo Oculto, mai/2026) · Receita e MPSP, via imprensa"}},
 {"say": "E a porta dos fundos tem outra entrada: a das contas laranja do episódio passado. Quando abrir uma conta é fácil demais, e a verificação é fraca, o golpista consegue dezenas de contas para espalhar o dinheiro de um golpe do Pix em segundos. Quanto mais frágil a portaria, mais laranjas passam.",
  "vis": {"type": "title", "title": "Portaria frágil,\nmais laranjas", "sub": "análise do canal"}},
 {"say": "E teve o ataque. Na virada de junho para julho de dois mil e vinte e cinco, criminosos usaram credenciais de clientes de uma empresa de tecnologia que conecta instituições ao Banco Central. Segundo a Polícia Civil de São Paulo, quinhentos e quarenta e um milhões de reais foram desviados da conta de reserva de uma única instituição de pagamento.",
  "vis": {"type": "bignumber", "from": 0, "to": 541, "prefix": "R$ ", "suffix": " milhões", "decimals": 0, "warn": True, "caption": "desviados da conta de reserva de uma instituição de pagamento",
          "source": "Fonte: Polícia Civil de São Paulo, ataque à C&M Software (jul/2025), via CNN Brasil"}},

 # ---------- CÔMODO 5: O FISCAL ----------
 # REENGAJE ~6:00
 {"say": "Cômodo cinco: o fiscal. Depois desses casos, o fiscal bateu na porta, e com força. Primeiro, a Receita Federal. Em agosto de dois mil e vinte e cinco, uma instrução normativa obrigou as fintechs e instituições de pagamento a entregar à Receita as mesmas informações de movimentação que os bancos já entregavam.",
  "vis": {"type": "house", "n": 5, "rooms": ROOMS, "head": "O FISCAL", "title": "O fiscal\nbateu na porta", "sub": "Receita e Banco Central",
          "caption": "Fonte: Receita Federal, Instrução Normativa RFB 2.278/2025 (e-Financeira)"}},
 {"say": "Depois, o Banco Central. Em setembro de dois mil e vinte e cinco, ele mudou uma regra que existia desde o começo: instituições pequenas podiam operar sem autorização. Agora, quem é novo só começa depois de autorizado. E as que já funcionavam tiveram que pedir licença até maio de dois mil e vinte e seis, e não mais até dois mil e vinte e nove.",
  "vis": {"type": "timeline", "even": True, "points": [["Set/2025", "nova regra"], ["Mai/2026", "prazo para pedir licença"], ["Dez/2029", "prazo antigo"]],
          "caption": "Fonte: Resolução BCB 494/2025, via Agência Brasil e CartaCapital"}},
 {"say": "No mesmo pacote, um freio direto no bolso. Instituições sem autorização passaram a ter limite de quinze mil reais por Pix ou TED. É uma forma de impedir que uma empresa sem licença vire um cano para grandes volumes de dinheiro.",
  "vis": {"type": "bignumber", "from": 0, "to": 15000, "prefix": "R$ ", "decimals": 0, "caption": "limite por Pix ou TED para instituições sem autorização do Banco Central",
          "source": "Fonte: Resoluções BCB 496 e 497/2025 (set/2025)"}},
 {"say": "E, em novembro de dois mil e vinte e cinco, veio o aperto mais caro: o capital mínimo. O dinheiro próprio que uma instituição de pagamento precisa ter subiu de uma faixa entre um e nove milhões de reais para uma faixa entre nove vírgula dois e trinta e dois vírgula oito milhões, dependendo do que ela faz. A transição começou em julho deste ano e vai até dois mil e vinte e oito.",
  "vis": {"type": "bars", "title": "Capital mínimo de uma instituição de pagamento", "items": [["Antes (mínimo)", 1, "#7884A0"], ["Agora (mínimo)", 9.2, "#F2A93B"], ["Agora (máximo)", 32.8, "#E06C5A"]],
          "prefix": "R$ ", "suffix": " mi", "decimals": 1, "caption": "Fonte: Resolução Conjunta 14 e Resolução BCB 517 (nov/2025), via imprensa · transição até 2028"}},
 {"say": "A minha análise: o Banco Central está trocando quantidade por segurança. Por mais de uma década, a regra leve ajudou a criar concorrência e baixou o preço dos serviços. Agora, a conta dessa leveza chegou. Muitas empresas pequenas devem fechar, ser vendidas ou se juntar a outras. Menos nomes desconhecidos, e mais fiscalizados.",
  "vis": {"type": "compare", "left": ["Regra leve", "mais concorrência", "conta grátis", "portaria frágil"], "right": ["Regra dura", "menos empresas", "mais capital e licença", "mais fiscalização"],
          "caption": "Análise do canal"}},

 # ---------- FECHAMENTO ----------
 {"say": "Então, o que fazer com tudo isso? Três perguntas simples sobre a conta onde está o seu dinheiro. Quem é a instituição que aparece no comprovante? Ela é banco ou instituição de pagamento? E ela tem autorização do Banco Central? Dá para conferir isso no próprio site do Banco Central.",
  "vis": {"type": "cards", "title": "Três perguntas sobre a sua conta", "cards": [["1", "Quem é?", "o nome no\ncomprovante"], ["2", "Banco ou IP?", "muda a proteção\ndo saldo"], ["3", "Autorizada?", "consulte no site\ndo Banco Central"]],
          "highlight": 1, "caption": "Análise do canal · informativo, não é recomendação"}},
 {"say": "Recapitulando a vistoria. Na fachada, um aplicativo que parece banco, mas não é. No caixa, uma taxa invisível em cada compra. No cofre, um saldo separado por lei, mas sem FGC. Na porta dos fundos, contas-bolsão e laranjas. E na porta da frente, um fiscal que chegou atrasado, mas chegou.",
  "vis": {"type": "house", "n": 6, "rooms": ROOMS, "all": True, "kicker": "A VISTORIA COMPLETA", "title": "Parece banco.\nAgora você sabe.", "sub": "fachada, caixa, cofre, fundos e fiscal"}},
 {"say": "E a lição deste episódio é esta. A facilidade de abrir uma conta em dois minutos é uma conquista. Mas a mesma facilidade serve para quem quer esconder dinheiro. Saber quem guarda o seu saldo é o primeiro passo para não ser surpreendido.",
  "vis": {"type": "title", "title": "Saiba quem guarda\no seu dinheiro", "sub": "a facilidade vale para os dois lados"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira. Os casos citados foram descritos com base em investigações e reportagens públicas.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E por falar em dinheiro que corre por aplicativos: tem um setor que, em poucos anos, passou a movimentar bilhões pelo Pix dos brasileiros. As apostas. No próximo episódio: as bets. Quanto os brasileiros colocam nelas, para onde vai esse dinheiro, e quem realmente ganha.",
  "vis": {"type": "title", "title": "Próximo: as bets", "sub": "para onde vai o dinheiro de quem aposta"}},
]
