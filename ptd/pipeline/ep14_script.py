# EP14 — Spread bancário: por que o juro no Brasil não cai quando a Selic cai
# Estrutura NOVA: "a cebola do juro" — o juro que o cliente paga descascado camada por camada, de fora para dentro
# (cena nova: onion). Camada 1 O custo do dinheiro (captação/Selic), 2 O calote, 3 A operação (despesas administrativas),
# 4 O governo (tributos e FGC), 5 O miolo (a margem do banco). Antes: o paradoxo (Selic caiu, juro subiu).
# Depois: o Brasil no mundo, por que a Selic cai e o juro não, o que já foi tentado, e o fechamento.
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação em pistas), EP12 (contrato em 5 cláusulas), EP13 (prédio em 5 andares).
# Promessa do EP13 cumprida ("por que o juro no Brasil é um dos mais altos do mundo, mesmo quando a Selic cai? É o spread").
# Loops: (1) "o paradoxo da Selic" -> resposta na parte "por que a Selic cai e o juro não"; (2) "qual camada é a maior?" -> o miolo.
# Re-engajamentos: ~3:00 o calote; ~6:00 o Brasil no mundo.
# Números: BC, Estatísticas monetárias e de crédito de março (27/04/2026) e setembro de 2026 (29/10/2026), via imprensa e Reuters;
# BC, Relatório de Estabilidade Financeira de maio de 2026 (decomposição do spread do ICC em 2025), via imprensa;
# Copom (Selic 15% de jun/2025 ao início de 2026; cinco cortes até 13,75%; mantida em 04/11/2026);
# Banco Mundial, indicador de spread de juros (2024), via Helgi Library e Cbonds; LC 166/2019; Lei 14.690/2023.
# Exemplo dos R$ 100 de juros = CÁLCULO do canal a partir da decomposição do BC (média de 2025, carteira toda).
TITLE = "Spread bancário: por que o juro no Brasil não cai quando a Selic cai"

LY = ["CUSTO", "CALOTE", "OPERAÇÃO", "GOVERNO", "MIOLO"]
SCENES = [
 # ---------- GANCHO: O PARADOXO ----------
 {"say": "Em dois mil e vinte e seis, o Banco Central cortou a taxa Selic cinco vezes seguidas. Ela saiu de quinze por cento ao ano, o maior nível em quase duas décadas, e chegou a treze vírgula setenta e cinco. Seria de esperar que o juro do empréstimo caísse junto. Não caiu. Subiu.",
  "vis": {"type": "compare", "left": ["A Selic", "15% ao ano", "cinco cortes", "13,75% em setembro"], "right": ["O juro do crédito livre", "48,3% em março", "subiu", "49,0% em setembro"],
          "caption": "Fontes: Copom; Banco Central, estatísticas de crédito de março e setembro de 2026"}},
 {"say": "Em março, o juro médio do crédito livre, aquele que o banco define sem regra do governo, estava em quarenta e oito vírgula três por cento ao ano. Em setembro, com a Selic mais baixa, foi para quarenta e nove por cento. E para as pessoas físicas, chegou a sessenta e dois vírgula quatro.",
  "vis": {"type": "bignumber", "from": 0, "to": 49.0, "suffix": "% ao ano", "decimals": 1, "caption": "juro médio das novas operações de crédito livre em setembro de 2026",
          "source": "Fonte: Banco Central (29/10/2026), via imprensa · pessoas físicas: 62,4%"}},
 {"say": "Então a pergunta deste episódio é simples. Se o dinheiro ficou mais barato para o banco, por que ele não ficou mais barato para você? A resposta tem nome. É o spread bancário. E para entender o spread, a gente vai fazer uma coisa diferente: descascar o juro como uma cebola, camada por camada, até chegar no miolo.",
  "vis": {"type": "title", "title": "A cebola do juro", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "Antes de começar, uma aposta. Das cinco camadas, qual você acha que é a maior? A maioria das pessoas responde: o lucro do banco. Guarde a sua resposta. No fim, a gente confere.",
  "vis": {"type": "bullets", "title": "Qual camada é a maior?", "items": ["O custo do dinheiro", "O calote", "A operação do banco", "Impostos", "O lucro do banco"], "highlight": 4,
          "caption": "Guarde a sua resposta"}},

 # ---------- O QUE É SPREAD ----------
 {"say": "Primeiro, o básico. Um banco é, no fundo, um intermediário. Ele pega dinheiro emprestado de alguém, paga um juro por isso, e empresta esse dinheiro para outra pessoa, cobrando um juro maior. A diferença entre o que ele cobra e o que ele paga é o spread.",
  "vis": {"type": "flow", "nodes": ["Quem guarda", "O banco", "Quem toma", "A diferença"], "notes": ["recebe um juro", "paga pouco, cobra muito", "paga um juro maior", "é o spread"], "pulse": True,
          "caption": "Esquema: análise do canal"}},
 {"say": "Em setembro, pelas contas do Banco Central, o spread médio do crédito livre foi de trinta e cinco vírgula cinco pontos percentuais. Em março, era trinta e quatro vírgula seis. Ou seja: enquanto a Selic caía, a diferença entre o que o banco paga e o que ele cobra aumentou.",
  "vis": {"type": "bars", "title": "Spread médio do crédito livre", "items": [["Março de 2026", 34.6, "#F2A93B"], ["Setembro de 2026", 35.5, "#E06C5A"]], "suffix": " p.p.", "decimals": 1,
          "caption": "Fonte: Banco Central, estatísticas monetárias e de crédito (27/04 e 29/10/2026), via imprensa e Reuters"}},
 {"say": "Mas spread não é sinônimo de lucro. Dentro dessa diferença tem muita coisa. E o próprio Banco Central faz, todo ano, a conta de onde vai cada pedaço. A edição mais recente, publicada em maio de dois mil e vinte e seis, olha o ano de dois mil e vinte e cinco. É ela que vai guiar a nossa cebola.",
  "vis": {"type": "cards", "title": "A fonte da cebola", "cards": [["BC", "Banco Central", "Relatório de Estabilidade\nFinanceira, maio de 2026"], ["ICC", "Custo do crédito", "média de toda a\ncarteira em 2025"], ["%", "Decomposição", "de onde vem cada\npedaço do juro"]],
          "highlight": 0, "caption": "O ICC médio de 2025 foi de 20,93% ao ano"}},

 # ---------- CAMADA 1: O CUSTO DO DINHEIRO ----------
 {"say": "Camada um. A casca. O custo do dinheiro. Antes de emprestar, o banco precisa conseguir o dinheiro. Ele paga juros a quem deposita, a quem compra um CDB, a quem empresta para ele no mercado. E quem dita o preço desse dinheiro é, principalmente, a Selic.",
  "vis": {"type": "onion", "n": 1, "label": "A CASCA", "title": "O custo\ndo dinheiro", "sub": "o que o banco paga para captar", "layers": LY,
          "pct": "~40%", "pct_note": "do custo médio do crédito em 2025"}},
 {"say": "Essa casca, tecnicamente, nem faz parte do spread. É o ponto de partida. Mas ela é grossa. Pela decomposição do Banco Central, o custo de captação respondeu por perto de quarenta por cento do custo médio do crédito em dois mil e vinte e cinco. E o banco central explica por quê: foi o ano da Selic a quinze por cento.",
  "vis": {"type": "stack", "title": "Custo médio do crédito em 2025", "parts": [["Captação", 40, "#5B8DEF", "~40%\ncusto do dinheiro"], ["Spread", 60, "#F2A93B", "~60%\no resto da cebola"]], "highlight": 1,
          "caption": "Fonte: BC, REF de maio de 2026, via imprensa · valores arredondados"}},
 {"say": "Aqui está o primeiro detalhe do paradoxo. Quando a Selic cai, essa casca afina. Mas ela afina devagar. Um CDB contratado no ano passado continua pagando a taxa antiga até vencer. O banco não renova todo o seu dinheiro de uma vez. A casca leva meses para encolher.",
  "vis": {"type": "compare", "left": ["Selic cai", "hoje", "decisão do Copom", "efeito imediato"], "right": ["Custo do banco cai", "aos poucos", "dívidas antigas vencem", "meses de atraso"],
          "caption": "Análise do canal"}},

 # ---------- CAMADA 2: O CALOTE ----------
 # REENGAJE ~3:00
 {"say": "Camada dois. E agora a gente entra no spread de verdade. A camada mais grossa de todas é o calote. Todo banco sabe que parte das pessoas não vai pagar. Então ele coloca esse prejuízo esperado no preço. Quem paga em dia, paga também pelo calote dos outros.",
  "vis": {"type": "onion", "n": 2, "label": "O CALOTE", "title": "Quem paga em dia\npaga pelos outros", "sub": "a maior camada do spread", "layers": LY,
          "pct": "36,6%", "pct_note": "do spread em 2025 (BC)"}},
 {"say": "Segundo o Banco Central, a inadimplência respondeu por trinta e seis vírgula seis por cento do spread em dois mil e vinte e cinco. É mais de um terço. E o problema é que esse número não está parado. Em setembro, o atraso acima de noventa dias no crédito livre das famílias chegou a oito vírgula um por cento. O maior da série histórica.",
  "vis": {"type": "bignumber", "from": 0, "to": 8.1, "suffix": "%", "decimals": 1, "caption": "do crédito livre das famílias com mais de 90 dias de atraso (set/2026, recorde)",
          "source": "Fonte: Banco Central (29/10/2026), via imprensa"}},
 {"say": "E isso explica a segunda parte do paradoxo. O banco não olha só a Selic. Ele olha o risco. Se o calote está subindo, ele cobra mais caro de todo mundo, para se proteger. A Selic diz que o dinheiro ficou mais barato. O calote diz que emprestar ficou mais arriscado. E, em dois mil e vinte e seis, o calote falou mais alto.",
  "vis": {"type": "compare", "left": ["A Selic diz", "dinheiro mais barato", "o juro pode cair", "13,75%"], "right": ["O calote diz", "risco maior", "o juro precisa subir", "8,1% em atraso"],
          "caption": "Análise do canal com dados do BC e do Copom"}},
 {"say": "Tem mais um detalhe. No Brasil, quando alguém não paga, recuperar o dinheiro é lento e caro. Processos que demoram anos, garantias difíceis de executar. Quanto menos o banco consegue recuperar, mais ele cobra antes. O calote não pesa só pelo tamanho. Pesa porque a conta quase nunca volta.",
  "vis": {"type": "flow", "nodes": ["Não pagou", "Cobrança lenta", "Pouco volta", "Juro mais alto"], "notes": ["prejuízo para o banco", "anos na Justiça", "a perda vira certeza", "para todos os clientes"], "pulse": True,
          "caption": "Análise do canal"}},

 # ---------- CAMADA 3: A OPERAÇÃO ----------
 {"say": "Camada três. A operação. Banco é uma empresa como outra qualquer. Tem funcionários, agências, sistemas, segurança, tecnologia, atendimento, combate a fraudes. Tudo isso tem custo. E esse custo também entra no juro que você paga.",
  "vis": {"type": "onion", "n": 3, "label": "A OPERAÇÃO", "title": "O custo\nde funcionar", "sub": "pessoas, agências, sistemas, fraude", "layers": LY,
          "pct": "22,9%", "pct_note": "do spread em 2025 (BC)"}},
 {"say": "Pelo Banco Central, as despesas administrativas foram vinte e dois vírgula nove por cento do spread em dois mil e vinte e cinco. É aqui que os bancos digitais dizem ter vantagem. Sem agência, o custo por cliente cai. Foi esse o argumento do Nubank, que a gente viu no episódio passado.",
  "vis": {"type": "compare", "left": ["Banco com agência", "prédios e caixas", "milhares de funcionários", "custo alto por cliente"], "right": ["Banco digital", "aplicativo", "atendimento remoto", "custo baixo por cliente"],
          "caption": "Análise do canal · o modelo do Nubank foi o tema do EP13"}},
 {"say": "Só que repare numa coisa. Mesmo com a chegada de dezenas de bancos digitais, o juro médio não despencou. Por quê? Porque a operação é só uma das camadas. Dá para cortar custo de agência. Não dá para cortar, com um aplicativo, o calote, os impostos e o preço do dinheiro.",
  "vis": {"type": "title", "title": "O aplicativo afina\numa camada só", "sub": "análise do canal"}},

 # ---------- CAMADA 4: O GOVERNO ----------
 {"say": "Camada quatro. O governo. Cada empréstimo carrega impostos. Tem o IOF, cobrado do cliente na operação. E tem os tributos que o banco paga sobre o que ganha, como o PIS, a Cofins, o imposto de renda e a contribuição social. Além disso, os bancos pagam uma taxa para o Fundo Garantidor de Créditos, o FGC, que protege os depositantes quando um banco quebra.",
  "vis": {"type": "onion", "n": 4, "label": "O GOVERNO", "title": "Impostos\ne o seguro", "sub": "tributos e o Fundo Garantidor (FGC)", "layers": LY,
          "pct": "20,5%", "pct_note": "do spread em 2025 (BC)"}},
 {"say": "Juntos, tributos e FGC foram vinte vírgula cinco por cento do spread em dois mil e vinte e cinco. Um quinto. E o FGC tem a ver com uma história que a gente já contou aqui: foi ele que pagou a conta bilionária do Banco Master. Esse seguro é pago pelo sistema, e o custo, no fim, chega ao preço do crédito.",
  "vis": {"type": "cards", "title": "O que está nessa camada", "cards": [["1", "IOF", "imposto cobrado\nna operação"], ["2", "Tributos", "PIS, Cofins, IR\ne CSLL do banco"], ["3", "FGC", "o seguro dos\ndepositantes"]],
          "highlight": 2, "caption": "O caso do Banco Master foi o tema do EP09"}},

 # ---------- CAMADA 5: O MIOLO ----------
 {"say": "E chegamos ao miolo. Camada cinco. A margem do banco. É o que sobra depois de pagar o dinheiro, o calote, a operação e os impostos. É aqui que mora o lucro. E agora vem a resposta da aposta do começo.",
  "vis": {"type": "onion", "n": 5, "label": "O MIOLO", "title": "A margem\ndo banco", "sub": "o que sobra no fim", "layers": LY,
          "pct": "20,0%", "pct_note": "do spread em 2025 (BC)"}},
 {"say": "Segundo o Banco Central, a margem financeira foi dezenove vírgula nove sete por cento do spread em dois mil e vinte e cinco. Praticamente um quinto. É a menor das quatro camadas do spread. Menor que o calote, menor que a operação, e um pouquinho menor que os impostos.",
  "vis": {"type": "bars", "title": "Do que é feito o spread (2025)", "items": [["Calote", 36.61, "#E06C5A"], ["Operação", 22.90, "#5B8DEF"], ["Impostos e FGC", 20.52, "#9B5DE5"], ["Margem do banco", 19.97, "#3AC47D"]], "suffix": "%", "decimals": 1,
          "caption": "Fonte: Banco Central, Relatório de Estabilidade Financeira (maio de 2026), via imprensa"}},
 {"say": "Vamos transformar isso num exemplo do canal. Pense em cada cem reais de juros que o sistema cobrou, em média, em dois mil e vinte e cinco. Perto de quarenta reais pagaram o custo do dinheiro. Vinte e dois cobriram o calote. Quase catorze pagaram a operação. Uns doze ficaram com o governo. E uns doze foram a margem do banco.",
  "vis": {"type": "stack", "title": "Para onde vão R$ 100 de juros (média de 2025)", "parts": [["Dinheiro", 39.8, "#5B8DEF", "R$ 39,80"], ["Calote", 22.0, "#E06C5A", "R$ 22,00"], ["Operação", 13.8, "#F2A93B", "R$ 13,80"], ["Governo", 12.4, "#9B5DE5", "R$ 12,40"], ["Margem", 12.0, "#3AC47D", "R$ 12,00"]], "highlight": 4,
          "caption": "Cálculo do canal a partir da decomposição do BC (custo médio de toda a carteira, não de um empréstimo específico)"}},
 {"say": "Então, se você apostou no lucro do banco, errou. Mas calma. Isso não quer dizer que os bancos ganham pouco. Doze por cento de uma montanha de juros ainda é uma montanha de dinheiro. O crédito no Brasil passou de sete trilhões de reais. E os maiores bancos lucram dezenas de bilhões por ano. A fatia é fina. O bolo é que é gigante.",
  "vis": {"type": "compare", "left": ["A fatia", "~12% dos juros", "a menor camada", "parece pouco"], "right": ["O bolo", "R$ 7,4 trilhões", "de crédito no país", "lucro bilionário"],
          "caption": "Estoque de crédito: Banco Central (set/2026) · análise do canal"}},

 # ---------- O BRASIL NO MUNDO ----------
 # REENGAJE ~6:00
 {"say": "Agora vamos sair da cozinha e olhar para fora. Quão estranho é o spread brasileiro? Nos dados do Banco Mundial de dois mil e vinte e quatro, que comparam o juro do empréstimo com o juro do depósito, o Brasil aparece no topo, com trinta e dois vírgula cinco pontos. O segundo da lista, o Quirguistão, tinha dezoito vírgula um.",
  "vis": {"type": "bars", "title": "Spread de juros em 2024 (Banco Mundial)", "items": [["Brasil", 32.5, "#E06C5A"], ["Quirguistão", 18.1, "#F2A93B"]], "suffix": " p.p.", "decimals": 1,
          "caption": "Fonte: Banco Mundial (empréstimo menos depósito), via Helgi Library e Cbonds · metodologia diferente da do BC"}},
 {"say": "Um cuidado aqui. Essa conta do Banco Mundial usa uma metodologia diferente da do Banco Central, e nem todos os países informam o dado todo ano. Mas a mensagem é a mesma em qualquer régua: o Brasil cobra muito mais pelo crédito, em relação ao que paga pelo depósito, do que quase qualquer outro país.",
  "vis": {"type": "title", "title": "Em qualquer régua,\no Brasil está no topo", "sub": "comparações internacionais variam por metodologia"}},

 # ---------- POR QUE A SELIC CAI E O JURO NÃO ----------
 {"say": "Então, vamos responder o paradoxo do começo. Por que a Selic caiu cinco vezes e o seu juro subiu? Juntando as camadas, são três motivos.",
  "vis": {"type": "title", "title": "Por que a Selic cai\ne o juro não?", "sub": "a resposta"}},
 {"say": "Primeiro: a casca afina devagar. O custo do dinheiro do banco demora meses para acompanhar a Selic. Segundo: o calote subiu. Com a inadimplência das famílias em recorde, o banco aumenta a camada de risco, e isso come o corte da Selic. Terceiro: as outras camadas, operação, impostos e margem, não dependem da Selic. Elas ficam onde estão.",
  "vis": {"type": "bullets", "title": "Três motivos", "items": ["A casca afina devagar", "O calote está em alta", "Três camadas nem ligam para a Selic"], "highlight": 1,
          "caption": "Análise do canal com dados do BC"}},
 {"say": "Repare na conta. A Selic caiu um ponto e um quarto. O spread do crédito livre subiu quase um ponto no mesmo período. Um movimento praticamente anulou o outro. Para o cliente, o corte da Selic chegou como um sussurro.",
  "vis": {"type": "compare", "left": ["Selic", "-1,25 ponto", "de 15% para 13,75%", "o dinheiro barateou"], "right": ["Spread livre", "+0,9 ponto", "de 34,6 para 35,5", "o risco encareceu"],
          "caption": "Fontes: Copom; Banco Central (março e setembro de 2026) · cálculo do canal"}},

 # ---------- O QUE JÁ FOI TENTADO ----------
 {"say": "E não é por falta de tentativa. Nos últimos anos, o país mexeu em várias camadas da cebola. Em dois mil e dezenove, o cadastro positivo virou automático, para o banco conhecer melhor quem paga em dia. Em dois mil e vinte, chegou o Pix. Em dois mil e vinte e um, o open finance, para o cliente levar o seu histórico de um banco para outro. E, desde dois mil e vinte e quatro, uma lei limita os juros do rotativo do cartão ao valor da própria dívida.",
  "vis": {"type": "timeline", "even": True, "points": [["2019", "cadastro positivo automático"], ["2020", "Pix"], ["2021", "open finance"], ["2024", "teto do rotativo"]],
          "caption": "Fontes: Lei Complementar 166/2019; BC; Lei 14.690/2023"}},
 {"say": "Cada medida atacou uma camada. O cadastro positivo e o open finance miram o calote, porque ajudam a separar o bom do mau pagador. O Pix e os bancos digitais miram a operação. E o teto do rotativo mira o pedaço mais caro do cartão, que a gente destrinchou no episódio onze. Mas nenhuma delas mexe na casca, que depende da Selic, nem na camada do governo.",
  "vis": {"type": "cards", "title": "Cada medida, uma camada", "cards": [["2", "Calote", "cadastro positivo\ne open finance"], ["3", "Operação", "Pix e bancos\ndigitais"], ["4", "Governo", "nenhuma mudança\nrelevante"]],
          "highlight": 0, "caption": "Análise do canal · o rotativo foi o tema do EP11"}},

 # ---------- FECHAMENTO ----------
 {"say": "Então, vamos montar a cebola inteira de novo. Por fora, o custo do dinheiro, que segue a Selic com atraso. Depois o calote, a camada mais grossa do spread. Depois a operação do banco. Depois o governo. E, no miolo, a margem, menor do que a maioria das pessoas imagina, mas sobre um bolo enorme.",
  "vis": {"type": "bullets", "title": "A cebola inteira", "items": ["Casca: o custo do dinheiro", "Calote: 36,6% do spread", "Operação: 22,9%", "Governo: 20,5%", "Miolo, a margem: 20,0%"], "highlight": 1,
          "caption": "Fonte das fatias: Banco Central (2025)"}},
 {"say": "E a lição que fica é desconfortável. O juro alto no Brasil não tem um vilão só. Não é só a Selic, nem só o lucro dos bancos. É uma cebola grossa em todas as camadas. E a camada que mais pesa no spread é o calote. Ou seja: em parte, quem paga em dia está pagando pelo crédito de quem não paga.",
  "vis": {"type": "title", "title": "Não existe um vilão só", "sub": "existe uma cebola grossa"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira, nem de investimento. É só a cebola descascada, para você entender o que está dentro do juro que você paga.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E se o calote é a maior camada, existe uma ferramenta que os bancos usam para decidir quem é bom pagador, e quanto cada um vai pagar de juro: o seu score de crédito. No próximo episódio, vamos abrir essa caixa. Quem calcula o seu score, o que faz ele subir ou cair, e por que dois vizinhos pagam juros diferentes pelo mesmo empréstimo.",
  "vis": {"type": "title", "title": "Próximo: o seu score", "sub": "quem decide quanto você paga de juro"}},
]
