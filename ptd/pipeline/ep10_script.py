# EP10 — O rotativo do cartão: o juro mais caro do Brasil (e quem ganha com ele)
# Estrutura NOVA: "julgamento" — o réu é o rotativo. Fase 1 Os autos (o que é), Fase 2 A acusação (os números),
# Fase 3 A defesa (o argumento dos bancos: calote e parcelado sem juros), Fase 4 As provas (o que aconteceu quando
# mexeram na regra: 2017 e o teto de 2024), Fase 5 O veredito (análise do canal: quem ganha e quem paga).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos), EP09 (caixa-preta).
# Cena nova: court (martelo de juiz + placa de fase).
# Loops: (1) como 451% convive com um teto de 100% -> Fase 4; (2) quem ganha -> Fase 5; (3) o que o calote tem a ver -> Fase 3.
# Re-engajamentos: ~3:00 a defesa (66% do saldo em atraso); ~6:00 a matemática do teto.
# Exemplos com fatura de R$ 1.000 são ILUSTRATIVOS (marcados na tela). 15,3% ao mês = conversão do canal de 451,7% ao ano.
TITLE = "Rotativo do cartão: o juro de 451% ao ano (e quem ganha com ele)"

SRC_SET = "Fonte: Banco Central, set/2026, via O Povo (29/10/2026)"
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Imagine uma fatura de mil reais que você não conseguiu pagar inteira. Se essa dívida ficasse um ano inteiro no rotativo do cartão, na taxa média cobrada hoje no Brasil, ela viraria mais de cinco mil e quinhentos reais.",
  "vis": {"type": "bignumber", "from": 1000, "to": 5517, "prefix": "R$ ", "decimals": 0, "warn": True, "caption": "R$ 1.000 depois de 12 meses à taxa média do rotativo, sem teto",
          "source": "Exemplo ilustrativo do canal com a taxa média do BC de set/2026 (451,7% ao ano)"}},
 {"say": "Esse é o juro mais caro do país. Em setembro de dois mil e vinte e seis, segundo o Banco Central, a taxa média do rotativo chegou a quatrocentos e cinquenta e um vírgula sete por cento ao ano.",
  "vis": {"type": "bignumber", "from": 0, "to": 451.7, "suffix": "%", "decimals": 1, "warn": True, "caption": "juro médio do rotativo do cartão, ao ano",
          "source": SRC_SET}},
 {"say": "Só que existe uma lei que diz que os juros do rotativo não podem passar de cem por cento da dívida. Então como é que um número desses continua existindo? E quem, no fim, fica com esse dinheiro?",
  "vis": {"type": "compare", "left": ["A estatística", "451,7% ao ano", "taxa média do rotativo", "set/2026"], "right": ["A lei", "teto de 100%", "da dívida original", "desde jan/2024"],
          "caption": "Fontes: Banco Central; Lei 14.690/2023 e Resolução CMN 5.112/2023"}},
 {"say": "Hoje o rotativo vai a julgamento. Vamos abrir os autos, ouvir a acusação, dar a palavra à defesa, examinar as provas e, no fim, dar o veredito.",
  "vis": {"type": "title", "title": "O julgamento\ndo rotativo", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- FASE 1: OS AUTOS ----------
 {"say": "Fase um. Os autos. Antes de julgar, é preciso saber quem é o réu.",
  "vis": {"type": "court", "n": 1, "label": "OS AUTOS", "title": "Quem é\no réu", "sub": "o que é o rotativo", "side": "neutral"}},
 {"say": "Quando a fatura do cartão chega, você tem três caminhos. Pagar tudo, e não paga juro nenhum. Pagar só uma parte, e o resto vira um empréstimo automático. Ou parcelar a fatura num plano que o próprio banco oferece. Esse empréstimo automático, que nasce quando você paga menos que o total, é o rotativo.",
  "vis": {"type": "cards", "title": "A fatura chegou: três caminhos", "cards": [["1", "Pagar tudo", "sem juros"], ["2", "Pagar uma parte", "o resto vira\nrotativo"], ["3", "Parcelar a fatura", "juros menores,\nparcelas fixas"]],
          "highlight": 1, "caption": "Como funciona a fatura do cartão de crédito"}},
 {"say": "Ninguém assina um contrato novo para entrar no rotativo. Não tem simulação, não tem gerente, não tem análise. Basta pagar um real a menos que o total. É o crédito mais fácil de pegar do país, e justamente por isso é o mais perigoso.",
  "vis": {"type": "flow", "nodes": ["Fatura de R$ 1.000", "Paga R$ 300", "R$ 700 no rotativo", "Juros no mês seguinte"], "notes": ["vencimento", "pagamento parcial", "empréstimo automático", "sobre o saldo"], "pulse": True,
          "caption": "Exemplo ilustrativo"}},
 {"say": "Durante anos, essa dívida podia ficar no rotativo indefinidamente, mês após mês. Isso mudou em três de abril de dois mil e dezessete. Uma resolução do Conselho Monetário Nacional passou a permitir o rotativo só até o vencimento da fatura seguinte. Depois disso, o banco tem que oferecer um parcelamento, com juros menores.",
  "vis": {"type": "timeline", "even": True, "points": [["até 2017", "rotativo sem prazo"], ["03/04/2017", "só até a fatura seguinte"], ["depois", "vira parcelamento"]],
          "caption": "Fonte: Resolução CMN 4.549/2017, Banco Central"}},
 {"say": "Ou seja, hoje o rotativo é, na teoria, uma ponte de trinta dias. O problema é o preço do pedágio dessa ponte.",
  "vis": {"type": "title", "title": "Uma ponte\nde 30 dias.", "sub": "com o pedágio mais caro do país"}},

 # ---------- FASE 2: A ACUSAÇÃO ----------
 {"say": "Fase dois. A acusação. Com a palavra, os números.",
  "vis": {"type": "court", "n": 2, "label": "A ACUSAÇÃO", "title": "Os números\ncontra o réu", "sub": "quanto custa o rotativo", "side": "acc"}},
 {"say": "Quatrocentos e cinquenta e um vírgula sete por cento ao ano. Convertendo para o mês, numa conta do canal, isso dá cerca de quinze vírgula três por cento ao mês. Para comparar, o parcelamento da fatura cobrava em média cento e noventa e dois por cento ao ano em agosto. Caro, mas menos da metade.",
  "vis": {"type": "bars", "title": "Juro médio ao ano, pessoa física", "items": [["Parcelamento (ago/26)", 192.1, "#F2A93B"], ["Rotativo (set/26)", 451.7, "#E06C5A"]], "suffix": "%", "decimals": 1,
          "caption": "Fonte: Banco Central, via Rankia e O Povo — 15,3% ao mês é conversão do canal"}},
 {"say": "E esse número não é um ponto fora da curva. É uma curva inteira. Em dezembro de dois mil e dezesseis, o rotativo bateu quatrocentos e oitenta e quatro vírgula seis por cento ao ano, o recorde da série do Banco Central. Despencou depois da regra de dois mil e dezessete, mas voltou a subir. Em julho de dois mil e vinte e quatro, já estava em quatrocentos e trinta e dois. E agora passa de quatrocentos e cinquenta.",
  "vis": {"type": "line", "title": "Juro médio do rotativo (% ao ano)", "points": [["dez/2016", 484.6], ["abr/2017", 233.9], ["jul/2024", 432.3], ["set/2026", 451.7]], "prefix": "", "suffix": "%", "decimals": 1, "max": 520, "color": "#E06C5A",
          "caption": "Fontes: Banco Central, via Monitor Mercantil, Folha/JB (abr/2017, 3ª semana) e Meu Tudo — intervalo entre pontos não é proporcional"}},
 {"say": "A acusação também chama uma testemunha: o tamanho do aperto. Em setembro de dois mil e vinte e seis, a Serasa contou oitenta e quatro vírgula dois milhões de brasileiros inadimplentes, um recorde. E as dívidas com bancos e cartões eram a maior fatia de tudo que estava atrasado no país, cerca de vinte e sete por cento.",
  "vis": {"type": "bignumber", "from": 0, "to": 84.2, "suffix": " milhões", "decimals": 1, "warn": True, "caption": "de brasileiros inadimplentes em set/2026 — bancos e cartões: 27,16% das dívidas",
          "source": "Fonte: Mapa da Inadimplência da Serasa, set/2026, via Mercado & Consumo"}},
 {"say": "Para a acusação, o caso é simples. Um produto que se pega sem querer, que cobra quinze por cento ao mês e que pesa mais justamente em quem já está no aperto. Mas todo réu tem direito à defesa.",
  "vis": {"type": "bullets", "title": "O que diz a acusação", "items": ["Entra-se sem perceber", "~15% ao mês", "Recorde de inadimplentes", "Pesa em quem já está apertado"], "highlight": 1}},

 # ---------- FASE 3: A DEFESA ----------
 # REENGAJE ~3:00
 {"say": "Fase três. A defesa. E aqui a história fica mais interessante do que parece.",
  "vis": {"type": "court", "n": 3, "label": "A DEFESA", "title": "O argumento\ndos bancos", "sub": "por que o juro é tão alto", "side": "def"}},
 {"say": "O primeiro argumento da defesa é o calote. Em agosto de dois mil e vinte e seis, sessenta e seis vírgula quinze por cento de todo o saldo do rotativo estava com mais de noventa dias de atraso. Isso mesmo: de cada cem reais emprestados no rotativo, sessenta e seis não estavam sendo pagos havia mais de três meses. É o maior percentual da série do Banco Central, que começa em dois mil e onze.",
  "vis": {"type": "stack", "title": "Saldo do rotativo em ago/2026", "parts": [["Mais de 90 dias de atraso", 66, "#E06C5A", "recorde da série\n(66,15%)"], ["Em dia ou atraso menor", 34, "#5B8DEF", "o restante\ndo saldo"]], "highlight": 0,
          "caption": "Fonte: Banco Central, via Rankia, out/2026"}},
 {"say": "Na lógica de um banco, o juro precisa cobrir o dinheiro que não volta. Se uma parte enorme da carteira vira calote, quem paga em dia acaba pagando pelo resto. É o mesmo raciocínio de um seguro: o preço reflete o risco do grupo inteiro.",
  "vis": {"type": "flow", "nodes": ["Muito calote", "Perda para o banco", "Juro mais alto", "Mais gente sem pagar"], "notes": ["66% do saldo atrasado", "dinheiro que não volta", "para cobrir a perda", "o ciclo se repete"], "pulse": True,
          "caption": "Análise do canal: o círculo vicioso do rotativo"}},
 {"say": "O segundo argumento é mais polêmico: o parcelado sem juros. O brasileiro adora comprar em dez vezes sem juros. Só que, para o banco que emite o cartão, esse dinheiro também é um crédito, que fica semanas ou meses sem render nada. Em maio de dois mil e vinte e seis, setenta e quatro vírgula seis por cento de todo o saldo da carteira de cartões não pagava juro nenhum.",
  "vis": {"type": "stack", "title": "Saldo da carteira de cartões (mai/2026)", "parts": [["Sem juros", 74.6, "#3AC47D", "74,6%: à vista e\nparcelado sem juros"], ["Com juros", 25.4, "#E06C5A", "rotativo e\nparcelamentos"]], "highlight": 1,
          "caption": "Fonte: Banco Central, via Times Brasil"}},
 {"say": "Em dois mil e vinte e três, esse debate explodiu. O então presidente do Banco Central, Roberto Campos Neto, chegou a ligar os juros altos do rotativo ao parcelado sem juros, e a Febraban, a federação dos bancos, defendeu essa tese. O Banco Central chegou a estudar um limite de doze parcelas sem juros.",
  "vis": {"type": "compare", "left": ["Bancos (Febraban)", "o parcelado sem juros", "pesa no custo", "e encarece o rotativo"], "right": ["Varejo e maquininhas", "parcelar sem juros", "move as vendas", "não é a causa do juro"],
          "caption": "Fontes: A Gazeta, InfoMoney, Brazil Journal e Correio Braziliense, 2023"}},
 {"say": "Do outro lado, o varejo e as empresas de maquininha reagiram. Para eles, mexer no parcelado derrubaria as vendas sem garantir juro menor. Até o ministro da Fazenda, Fernando Haddad, disse que acabar com o parcelado sem juros não era solução para o rotativo. O limite de parcelas não saiu do papel.",
  "vis": {"type": "bullets", "title": "Como a briga terminou", "items": ["BC estudou limitar a 12 parcelas", "Varejo e maquininhas reagiram", "Haddad: não é a solução", "O parcelado sem juros ficou"], "highlight": 3,
          "caption": "Fontes: InfoMoney, A Gazeta e Brazil Journal, 2023"}},

 # ---------- FASE 4: AS PROVAS ----------
 {"say": "Fase quatro. As provas. Se o juro é alto por causa do risco e do modelo de negócio, o que acontece quando alguém mexe nas regras? Esse caso tem dois experimentos reais.",
  "vis": {"type": "court", "n": 4, "label": "AS PROVAS", "title": "Dois\nexperimentos", "sub": "2017 e 2024", "side": "neutral"}},
 {"say": "Prova número um: a regra de dois mil e dezessete, a da ponte de trinta dias. No mês em que ela entrou em vigor, o juro médio do rotativo caiu pela metade. Na terceira semana de abril daquele ano, estava em duzentos e trinta e três vírgula nove por cento ao ano.",
  "vis": {"type": "bars", "title": "Juro do rotativo antes e depois da regra de 2017", "items": [["dez/2016 (recorde)", 484.6, "#E06C5A"], ["abr/2017 (3ª semana)", 233.9, "#3AC47D"]], "suffix": "%", "decimals": 1,
          "caption": "Fontes: Banco Central, via Monitor Mercantil e Folha/JB, mai/2017"}},
 {"say": "Mas a queda não durou. Com os anos, a taxa foi subindo de novo, e um voto do próprio Conselho Monetário Nacional, em dois mil e vinte e três, reconheceu um aumento gradual depois dos resultados iniciais. A lição da prova número um é que encurtar a ponte ajuda, mas não muda o preço do pedágio para sempre.",
  "vis": {"type": "title", "title": "A queda\nnão durou.", "sub": "o juro voltou a passar de 400%"}},
 # REENGAJE ~6:00
 {"say": "Prova número dois: o teto. Em outubro de dois mil e vinte e três, a lei do programa Desenrola deu noventa dias para os bancos proporem um limite para os juros do rotativo. Eles não apresentaram proposta no prazo. Então o Conselho Monetário Nacional decidiu: a partir de três de janeiro de dois mil e vinte e quatro, juros e encargos do rotativo e do parcelamento da fatura não podem passar de cem por cento do valor original da dívida.",
  "vis": {"type": "timeline", "even": True, "points": [["out/2023", "Lei 14.690 (Desenrola)"], ["90 dias", "bancos sem proposta"], ["03/01/2024", "teto de 100% da dívida"]],
          "caption": "Fontes: Lei 14.690/2023; Resolução CMN 5.112/2023; Migalhas e Mattos Filho"}},
 {"say": "E aqui está a resposta para a pergunta do começo. O teto não limita a taxa. Ele limita o total. Numa dívida de mil reais, o máximo que se pode cobrar de juros e encargos é mais mil reais. A dívida pode chegar a dois mil, e para por aí.",
  "vis": {"type": "line", "title": "Dívida de R$ 1.000 no rotativo, a 15,3% ao mês", "points": [["início", 1000], ["3 meses", 1533], ["6 meses", 2349], ["9 meses", 3601], ["12 meses", 5517]], "prefix": "R$ ", "decimals": 0, "cap": 2000, "cap_label": "teto: R$ 2.000 (100% da dívida)", "color": "#E06C5A",
          "caption": "Exemplo ilustrativo do canal — a curva mostra a conta SEM o teto; com o teto, a cobrança para em R$ 2.000"}},
 {"say": "Já a taxa de quatrocentos e cinquenta e um por cento é uma estatística. O Banco Central pega o juro cobrado em um mês e projeta como se ele durasse doze meses. Por isso o número pode passar de cem por cento sem que nenhum banco esteja quebrando a lei. No exemplo ilustrativo, a dívida de mil reais bateria o teto em pouco mais de cinco meses.",
  "vis": {"type": "compare", "left": ["A taxa (451,7%)", "juro de um mês", "projetado para 12", "é uma estatística"], "right": ["O teto (100%)", "soma de juros e encargos", "sobre a dívida original", "é o limite do total"],
          "caption": "Fonte: Banco Central (metodologia da taxa anualizada); exemplo ilustrativo do canal"}},
 {"say": "Repare na consequência. O teto protege quem ficaria preso por muito tempo. Mas quem entra e sai do rotativo em um mês ainda paga o pedágio cheio, cerca de quinze por cento sobre o saldo. Junto com o teto veio uma terceira regra: a portabilidade. Desde o segundo semestre de dois mil e vinte e quatro, o saldo da fatura pode ser levado para outro banco que ofereça condição melhor.",
  "vis": {"type": "cards", "title": "As regras do jogo hoje", "cards": [["1", "Ponte de 30 dias", "depois vira\nparcelamento"], ["2", "Teto de 100%", "juros e encargos\naté o valor da dívida"], ["3", "Portabilidade", "levar o saldo\npara outro banco"]],
          "highlight": 1, "caption": "Fontes: Resoluções CMN 4.549/2017 e 5.112/2023"}},

 # ---------- FASE 5: O VEREDITO ----------
 {"say": "Fase cinco. O veredito. Daqui em diante é a análise do canal, com base nas provas.",
  "vis": {"type": "court", "n": 5, "label": "O VEREDITO", "title": "Quem ganha,\nquem paga", "sub": "análise do canal", "side": "neutral"}},
 {"say": "Primeiro: o rotativo não é um acidente do sistema. Ele é uma peça do modelo de negócio do cartão no Brasil. Três quartos do saldo não pagam juro nenhum. O cartão ainda tem que bancar as compras parceladas sem juros, os pontos, as milhas e o cashback. Uma parte importante dessa conta é coberta por quem, em algum mês, não conseguiu pagar a fatura inteira.",
  "vis": {"type": "flow", "nodes": ["Quem paga juros", "Banco emissor", "Benefícios do cartão", "Quem paga em dia"], "notes": ["rotativo e parcelamento", "cobre perdas e custos", "parcelado, milhas, cashback", "usa sem pagar juros"], "pulse": True,
          "caption": "Análise do canal: o subsídio cruzado do cartão de crédito"}},
 {"say": "Segundo: o calote é causa e consequência ao mesmo tempo. O juro é alto porque muita gente não paga. E muita gente não paga porque o juro é alto. Os dados de dois mil e dezessete mostram que regra mexe no preço, mas não quebra esse ciclo sozinha.",
  "vis": {"type": "bullets", "title": "O veredito do canal", "items": ["O rotativo é parte do modelo", "Calote é causa e consequência", "Regra ajuda, mas não basta", "O teto limita o total, não a taxa"], "highlight": 0}},
 {"say": "Terceiro: quem ganha não é só o banco. Ganha também quem usa o cartão como ferramenta e paga a fatura toda, todo mês, aproveitando prazo, parcelamento e pontos sem pagar nada por isso. A conta fica com quem está no aperto. No fim, o rotativo funciona como uma transferência silenciosa de quem tem menos folga para quem tem mais.",
  "vis": {"type": "compare", "left": ["Quem paga a fatura toda", "usa prazo e parcelas", "acumula pontos", "não paga juros"], "right": ["Quem entra no rotativo", "paga ~15% ao mês", "pesa no orçamento", "financia o sistema"],
          "caption": "Análise do canal"}},
 {"say": "E a sentença? O rotativo existe como ponte de emergência, e a lei hoje limita o estrago. Mas entender que a taxa é cobrada todo mês, que o teto não zera o custo e que existem parcelamentos e portabilidade é a diferença entre atravessar a ponte e morar nela.",
  "vis": {"type": "title", "title": "Atravessar a ponte,\nnão morar nela.", "sub": "o rotativo é emergência, não plano"}},
 {"say": "Isso não é recomendação financeira. É só a leitura dos autos, para você decidir com os números na mão.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "No próximo episódio, um golpe que saiu direto do benefício de milhões de aposentados. Como descontos que ninguém autorizou tiraram bilhões de reais do INSS, quem ficou com o dinheiro, e como o esquema foi descoberto.",
  "vis": {"type": "title", "title": "Próximo: os descontos\nno INSS", "sub": "o golpe que saiu do benefício dos aposentados"}},
]
