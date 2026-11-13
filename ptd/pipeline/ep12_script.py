# EP12 — Consignado: o empréstimo que o banco recebe antes de você
# Estrutura NOVA: "o contrato em 5 cláusulas" — cada bloco abre uma folha de contrato com a frase-chave marcada (cena nova: clause).
# Cláusula 1 A garantia (desconto em folha), 2 O preço (o teto e a comparação), 3 A margem (o vaivém de 45% -> 40% -> 45%),
# 4 O vendedor (correspondentes e assédio), 5 Quem ganha (o tamanho da carteira e os bancos). Fecha com "letra miúda" (análise).
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento), EP11 (investigação em pistas).
# Promessa do EP11 cumprida: "o desconto que é legal: o consignado; por que os bancos disputam o aposentado, quanto custa, quem ganha".
# Loops: (1) por que o crédito mais barato pode ser perigoso -> Cláusulas 2 e 3 + letra miúda; (2) quem ganha -> Cláusula 5.
# Re-engajamentos: ~3:00 a conta dos R$ 10 mil; ~6:00 quem ganha.
# Números da carteira (mar/2026) = séries do BCB citadas no estudo técnico da FACIAP (mai/2026). Simulação de R$ 10 mil = ILUSTRATIVA
# (tabela Price, cálculo do canal com o teto de 1,85% a.m. e a média de 6,42% a.m. do crédito pessoal não consignado).
TITLE = "Consignado: o empréstimo que o banco recebe antes de você (e quem ganha com ele)"

DOC = "CONTRATO DE CRÉDITO CONSIGNADO"
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Existe um empréstimo em que o banco quase não corre o risco de levar calote. Porque ele recebe a parcela antes de você. Antes de o salário ou a aposentadoria cair na sua conta, a parte do banco já saiu.",
  "vis": {"type": "receipt", "title": "Contracheque do mês (exemplo)", "head": "PAGAMENTO · MÊS DE REFERÊNCIA", "lines": [["Valor bruto", "R$ 2.500,00", "#1E2A40"], ["CONSIGNADO", "- R$ 235,50", "#D63E34"]], "total": ["Cai na conta", "R$ 2.264,50"],
          "caption": "Exemplo ilustrativo do canal — valores fictícios"}},
 {"say": "Esse é o crédito consignado. E ele não é pequeno. Segundo os dados do Banco Central, em março de dois mil e vinte e seis o saldo de todos os empréstimos consignados do país chegava a quase setecentos e setenta bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 770, "prefix": "R$ ", "suffix": " bilhões", "decimals": 0, "caption": "saldo de todo o crédito consignado no Brasil (mar/2026)",
          "source": "Fonte: Banco Central (séries de crédito), via estudo técnico da FACIAP (mai/2026) — R$ 769,98 bi"}},
 {"say": "É o empréstimo mais barato que uma pessoa comum consegue no Brasil. E, ao mesmo tempo, é o crédito que o governo tentou frear este ano, e que milhões de aposentados reclamam de receber por telefone todos os dias. Como uma coisa pode ser barata e perigosa ao mesmo tempo? E quem ganha com isso?",
  "vis": {"type": "compare", "left": ["Pergunta 1", "se é o mais barato,", "por que pode", "ser perigoso?"], "right": ["Pergunta 2", "quem ganha com", "quase R$ 770 bi", "emprestados?"],
          "caption": "As duas perguntas deste episódio"}},
 {"say": "Para responder, a gente vai ler esse contrato como ele merece. Cláusula por cláusula. São cinco. E a quinta é a que ninguém lê.",
  "vis": {"type": "title", "title": "Consignado:\no contrato em 5 cláusulas", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- CLÁUSULA 1: A GARANTIA ----------
 {"say": "Cláusula primeira. A garantia. Todo empréstimo tem um medo: o de não receber de volta. O consignado resolveu esse medo de um jeito simples.",
  "vis": {"type": "clause", "n": 1, "label": "A GARANTIA", "title": "Desconto\nna fonte", "sub": "o banco recebe primeiro", "mark": "desconto direto na folha de pagamento", "doc": DOC}},
 {"say": "Funciona assim. Você pede o empréstimo. O banco avisa quem paga o seu salário ou o seu benefício: pode ser a empresa, o órgão público ou o INSS. E todo mês a parcela é descontada na folha, antes do pagamento. O banco não precisa cobrar, mandar boleto ou ligar. O dinheiro simplesmente chega.",
  "vis": {"type": "flow", "nodes": ["Você pede", "Banco avisa a fonte", "Desconto na folha", "Banco recebe"], "notes": ["o empréstimo", "empresa, órgão ou INSS", "todo mês, antes", "sem cobrar ninguém"], "pulse": True,
          "caption": "Lei 10.820/2003 e regras do INSS e dos órgãos públicos"}},
 {"say": "Essa ideia virou lei no fim de dois mil e três, com a Lei dez mil oitocentos e vinte, e ganhou força a partir de dois mil e quatro, quando chegou aos aposentados e pensionistas do INSS. Um estudo do próprio Banco Central mostra o tamanho da explosão: em pouco mais de onze anos, até dois mil e dezoito, o saldo saiu de cinquenta e três vírgula sete bilhões para trezentos e vinte e três vírgula oito bilhões de reais.",
  "vis": {"type": "bars", "title": "Saldo do crédito consignado", "items": [["~2007", 53.7, "#5B8DEF"], ["jun/2018", 323.8, "#F2A93B"], ["mar/2026", 770.0, "#3AC47D"]], "prefix": "R$ ", "suffix": " bi", "decimals": 1,
          "caption": "Fontes: Banco Central, estudo sobre o consignado (dados até 2018); BCB via FACIAP (mar/2026)"}},
 {"say": "No mesmo estudo, o Banco Central mostra que, desde dois mil e sete, o consignado sempre foi pelo menos sessenta por cento de todo o crédito pessoal do país. Ou seja: quando um brasileiro pega dinheiro emprestado sem dar um carro ou uma casa como garantia, na maioria das vezes é consignado.",
  "vis": {"type": "bignumber", "from": 0, "to": 60, "suffix": "%", "decimals": 0, "caption": "fatia mínima do consignado no crédito pessoal, desde 2007",
          "source": "Fonte: Banco Central, estudo sobre o empréstimo consignado (chegou a 75% em jun/2018)"}},

 # ---------- CLÁUSULA 2: O PREÇO ----------
 {"say": "Cláusula segunda. O preço. Se o banco quase não corre risco, ele pode cobrar menos. E cobra.",
  "vis": {"type": "clause", "n": 2, "label": "O PREÇO", "title": "O juro\nmais baixo", "sub": "e um teto definido pelo governo", "mark": "taxa máxima de 1,85% ao mês", "doc": DOC}},
 {"say": "No consignado do INSS existe até um teto. Quem define é o Conselho Nacional de Previdência Social. Desde março de dois mil e vinte e cinco, o limite é de um vírgula oitenta e cinco por cento ao mês. Isso dá uns vinte e quatro vírgula seis por cento ao ano. E a média que o Banco Central mede para o consignado do INSS ficou bem perto disso: vinte e quatro vírgula um por cento ao ano em agosto de dois mil e vinte e seis.",
  "vis": {"type": "bars", "title": "Juro médio ao ano, pessoa física", "items": [["Consignado INSS", 24.1, "#3AC47D"], ["Pessoal comum", 111.0, "#E06C5A"]], "suffix": "%", "decimals": 1,
          "caption": "Fontes: CNPS (teto de 1,85% a.m., mar/2025); Banco Central, médias de ago/2026 e jul/2026"}},
 {"say": "Agora compare com o empréstimo pessoal comum, aquele sem desconto em folha. A média do Banco Central foi de seis vírgula quarenta e dois por cento ao mês em julho de dois mil e vinte e seis. Mais de cento e dez por cento ao ano. Quatro vezes e meia o preço do consignado.",
  "vis": {"type": "compare", "left": ["Consignado INSS", "teto de 1,85% ao mês", "cerca de 24% ao ano", "o banco recebe antes"], "right": ["Pessoal comum", "média de 6,42% ao mês", "cerca de 111% ao ano", "o banco corre o risco"],
          "caption": "Fontes: CNPS e Banco Central (2025-2026)"}},
 # REENGAJE ~3:00
 {"say": "Só que barato por mês não quer dizer barato no total. Vamos a uma conta, que é um exemplo do canal. Dez mil reais no consignado, a um vírgula oitenta e cinco por cento ao mês, em oitenta e quatro parcelas. A parcela fica em uns duzentos e trinta e cinco reais. Parece leve. Mas, no fim de sete anos, você terá pago quase vinte mil reais. Praticamente o dobro do que pegou.",
  "vis": {"type": "receipt", "title": "R$ 10 mil no consignado (exemplo)", "head": "SIMULAÇÃO · 84 PARCELAS · 1,85% A.M.", "lines": [["Valor emprestado", "R$ 10.000,00", "#1E2A40"], ["Parcela mensal", "R$ 235,50", "#1E2A40"], ["Juros no total", "R$ 9.781,66", "#D63E34"]], "total": ["Total pago", "R$ 19.781,66"],
          "caption": "Exemplo ilustrativo — cálculo do canal pela tabela Price, sem tarifas e seguros"}},
 {"say": "E aqui vem a surpresa. Os mesmos dez mil reais no empréstimo pessoal comum, a seis vírgula quarenta e dois por cento ao mês, pagos em só dois anos, custariam um total parecido: uns dezenove mil e novecentos reais. O juro do consignado é quatro vezes menor. Mas o prazo longo devolve boa parte da diferença para o banco.",
  "vis": {"type": "compare", "left": ["Consignado", "1,85% ao mês", "84 parcelas de R$ 235", "total: R$ 19,8 mil"], "right": ["Pessoal comum", "6,42% ao mês", "24 parcelas de R$ 828", "total: R$ 19,9 mil"],
          "caption": "Exemplo ilustrativo — cálculo do canal (tabela Price, sem tarifas)"}},
 {"say": "Não é que os dois sejam iguais. A parcela do consignado é muito menor, e isso faz diferença para quem tem renda apertada. O ponto é outro: o consignado é barato por mês e caro pelo tempo. E tempo, para um aposentado, é exatamente o que ele está comprometendo.",
  "vis": {"type": "title", "title": "Barato por mês,\ncaro pelo tempo.", "sub": "análise do canal"}},

 # ---------- CLÁUSULA 3: A MARGEM ----------
 {"say": "Cláusula terceira. A margem. Se a parcela sai antes de o dinheiro chegar, alguém precisa limitar quanto pode sair. Esse limite se chama margem consignável.",
  "vis": {"type": "clause", "n": 3, "label": "A MARGEM", "title": "Quanto da\nrenda pode sair", "sub": "o limite que mudou duas vezes", "mark": "limitado a 45% do benefício", "doc": DOC}},
 {"say": "Para os aposentados e pensionistas do INSS, a regra soma quarenta e cinco por cento do benefício. Trinta e cinco por cento para empréstimos. Cinco por cento para o cartão de crédito consignado. E mais cinco para o chamado cartão consignado de benefício.",
  "vis": {"type": "bars", "title": "Margem consignável: até 45% do benefício", "items": [["Empréstimos", 35, "#5B8DEF"], ["Cartão", 5, "#F2A93B"], ["Cartão benefício", 5, "#E06C5A"]], "suffix": "%", "decimals": 0,
          "caption": "Regra do INSS para benefícios previdenciários, via imprensa (set/2026)"}},
 {"say": "Pense no que isso significa para quem ganha um salário mínimo. Quase metade do benefício pode estar comprometida antes de o mês começar. E o desconto não para se aparecer um remédio caro ou uma conta de luz mais alta.",
  "vis": {"type": "bignumber", "from": 0, "to": 45, "suffix": "%", "decimals": 0, "warn": True, "caption": "do benefício pode sair antes de chegar à conta",
          "source": "Regra do INSS: 35% empréstimos + 5% cartão consignado + 5% cartão de benefício"}},
 {"say": "Em maio de dois mil e vinte e seis, o governo tentou mexer nisso. Uma medida provisória, a mil trezentos e cinquenta e cinco, baixou a margem total para quarenta por cento, e previa cortes de dois pontos por ano, até chegar a trinta por cento em dois mil e trinta e um. Junto vieram mais travas, como a confirmação por biometria.",
  "vis": {"type": "timeline", "even": True, "points": [["até mai/2026", "margem de 45%"], ["19/05/2026", "MP baixa para 40%"], ["plano", "30% em 2031"]],
          "caption": "MP 1.355/2026"}},
 {"say": "O efeito apareceu rápido. Segundo dados do Banco Central divulgados pela imprensa, as novas concessões de consignado do INSS caíram de seis vírgula cinco bilhões de reais em março para três vírgula sete bilhões em maio.",
  "vis": {"type": "bars", "title": "Novos consignados do INSS por mês", "items": [["mar/2026", 6.5, "#5B8DEF"], ["abr/2026", 5.0, "#F2A93B"], ["mai/2026", 3.7, "#E06C5A"]], "prefix": "R$ ", "suffix": " bi", "decimals": 1,
          "caption": "Fonte: Banco Central, via NC News (jul/2026)"}},
 {"say": "Mas a medida provisória não foi votada a tempo pelo Congresso e perdeu a validade no início de setembro. Resultado: a margem voltou aos quarenta e cinco por cento. Enquanto isso, o Tribunal de Contas da União mandou suspender a emissão de novos cartões consignados. A regra mudou duas vezes em quatro meses. Para quem empresta, isso é risco. Para quem toma, é confusão.",
  "vis": {"type": "timeline", "even": True, "points": [["mai/2026", "cai para 40%"], ["set/2026", "MP perde validade"], ["hoje", "volta a 45%"]],
          "caption": "Duas mudanças em quatro meses"}},

 # ---------- CLÁUSULA 4: O VENDEDOR ----------
 {"say": "Cláusula quarta. O vendedor. Um produto com risco baixo e lucro garantido atrai muita gente querendo vender. E é aí que o consignado fica barulhento.",
  "vis": {"type": "clause", "n": 4, "label": "O VENDEDOR", "title": "Quem oferece\no empréstimo", "sub": "e quanto ganha para isso", "mark": "venda por correspondente bancário", "doc": DOC}},
 {"say": "Boa parte dos consignados não é vendida dentro do banco. É vendida por correspondentes bancários: empresas e promotoras que oferecem o crédito em nome dos bancos, por telefone, em lojas ou de porta em porta. E elas costumam ganhar comissão por contrato fechado. Quanto mais contratos, mais comissão.",
  "vis": {"type": "flow", "nodes": ["Banco", "Correspondente", "Ligação ou loja", "Aposentado"], "notes": ["empresta o dinheiro", "vende em nome do banco", "a oferta chega", "assina o contrato"], "pulse": True,
          "caption": "Como funciona a venda do consignado"}},
 {"say": "Esse incentivo explica o assédio que muitos aposentados conhecem: ligações em série, logo depois de o benefício ser concedido. A própria Febraban, a federação dos bancos, criou regras de autorregulação. E, até novembro de dois mil e vinte e cinco, aplicou mil novecentas e oitenta e três medidas contra correspondentes. Cento e treze foram proibidos de atuar de vez.",
  "vis": {"type": "cards", "title": "Punições a correspondentes (Febraban)", "cards": [["!", "1.983", "medidas\nadministrativas"], ["X", "113", "proibidos de\natuar de vez"], ["?", "Não me Perturbe", "cadastro contra\nligações"]],
          "highlight": 1, "caption": "Fonte: Febraban, autorregulação do consignado (até nov/2025)"}},
 {"say": "Repare que a própria punição é um termômetro. Quase duas mil medidas significam que o problema não é um caso isolado. É uma consequência do desenho: quando a venda é paga por volume, e o cliente mais disputado é justamente o que tem renda garantida, a pressão vai para cima de quem tem menos defesa.",
  "vis": {"type": "compare", "left": ["O incentivo", "comissão por contrato", "renda garantida", "cliente disputado"], "right": ["O resultado", "ligações em série", "contratos empurrados", "aposentado pressionado"],
          "caption": "Análise do canal"}},

 # ---------- CLÁUSULA 5: QUEM GANHA ----------
 # REENGAJE ~6:00
 {"say": "Cláusula quinta. A que ninguém lê. Quem ganha. E aqui volta a pergunta do começo: para onde vão os quase setecentos e setenta bilhões?",
  "vis": {"type": "clause", "n": 5, "label": "QUEM GANHA", "title": "Para onde\nvai o dinheiro", "sub": "a cláusula que ninguém lê", "mark": "o credor recebe antes do devedor", "doc": DOC}},
 {"say": "Primeiro, quem toma. Pelos dados do Banco Central em março de dois mil e vinte e seis, os servidores públicos respondiam por trezentos e oitenta e quatro bilhões de reais, metade de tudo. Os aposentados e pensionistas do INSS, por quase duzentos e oitenta e quatro bilhões. E os trabalhadores do setor privado, por pouco mais de cem bilhões.",
  "vis": {"type": "stack", "title": "Quem deve os R$ 770 bi do consignado (mar/2026)", "parts": [["Servidores públicos", 49.9, "#5B8DEF", "R$ 384,5 bi\nservidores"], ["INSS", 36.9, "#F2A93B", "R$ 283,9 bi\naposentados e pensionistas"], ["Setor privado", 13.2, "#3AC47D", "R$ 101,6 bi\nCLT"]], "highlight": 1,
          "caption": "Fonte: Banco Central, via estudo técnico da FACIAP (mai/2026)"}},
 {"say": "Essa última fatia é a que mais cresce. Em março de dois mil e vinte e cinco, o governo lançou o Crédito do Trabalhador, que levou o consignado para quem tem carteira assinada, pelo aplicativo da Carteira de Trabalho Digital. No primeiro ano, segundo o balanço oficial, foram mais de cento e dezessete bilhões de reais emprestados em quase vinte e um milhões de contratos.",
  "vis": {"type": "bignumber", "from": 0, "to": 117.1, "prefix": "R$ ", "suffix": " bilhões", "decimals": 1, "caption": "emprestados no 1º ano do Crédito do Trabalhador (20,9 milhões de contratos)",
          "source": "Fonte: balanço do programa (mar/2026), via Meu Tudo e Let's Money"}},
 {"say": "Mas o consignado do trabalhador privado é mais caro que o do aposentado. A taxa média divulgada pelo Ministério do Trabalho no início de dois mil e vinte e seis era de três vírgula dois por cento ao mês. Por quê? Porque o emprego pode acabar. A aposentadoria, não. Para o banco, o aposentado é o devedor mais seguro do país.",
  "vis": {"type": "bars", "title": "Juro médio ao mês, por tipo de crédito", "items": [["INSS (teto)", 1.85, "#3AC47D"], ["CLT (média)", 3.2, "#F2A93B"], ["Pessoal comum", 6.42, "#E06C5A"]], "suffix": "%", "decimals": 2,
          "caption": "Fontes: CNPS (mar/2025); Ministério do Trabalho (início de 2026); Banco Central (jul/2026)"}},
 {"say": "E do outro lado da mesa, quem empresta? Os grandes bancos. Segundo um levantamento do Bank of America, de dois mil e vinte e seis, o Itaú lidera as concessões de consignado, com cerca de dezoito por cento do mercado. O Banco do Brasil vem em seguida, com treze. E o Bradesco tem uns seis por cento.",
  "vis": {"type": "bars", "title": "Fatia nas concessões de consignado", "items": [["Itaú", 18, "#F2A93B"], ["Banco do Brasil", 13, "#5B8DEF"], ["Bradesco", 6, "#E06C5A"]], "suffix": "%", "decimals": 0,
          "caption": "Fonte: Bank of America (2026), via CB Insights e Seu Dinheiro"}},
 {"say": "Juro menor do que no crédito comum, sim. Mas sobre uma carteira gigante, com prazos de muitos anos e calote baixo, porque a parcela sai antes. É um lucro menos vistoso que o do rotativo do cartão, mas muito mais previsível. Para um banco, previsível vale ouro.",
  "vis": {"type": "compare", "left": ["Rotativo do cartão", "juro altíssimo", "muito calote", "lucro arriscado"], "right": ["Consignado", "juro baixo", "calote baixo", "lucro previsível"],
          "caption": "Análise do canal — o rotativo foi o tema do EP10"}},

 # ---------- A LETRA MIÚDA ----------
 {"say": "Fechadas as cinco cláusulas, vamos à letra miúda. A análise do canal. Por que o crédito mais barato pode ser perigoso?",
  "vis": {"type": "title", "title": "A letra\nmiúda", "sub": "análise do canal"}},
 {"say": "Primeiro: porque o consignado inverte quem tem prioridade. Num empréstimo comum, você decide no fim do mês o que paga primeiro. No consignado, o banco já decidiu por você. Isso é ótimo para baixar o juro. E péssimo quando a vida aperta, porque a parcela é a única conta que você não consegue atrasar.",
  "vis": {"type": "bullets", "title": "Lições do contrato", "items": ["O banco passa na frente", "Prazo longo pesa no total", "Margem é renda futura", "Quem vende ganha por volume"], "highlight": 0}},
 {"say": "Segundo: porque a margem é a renda do futuro sendo vendida no presente. Quarenta e cinco por cento de margem não é um limite de segurança. É o máximo permitido. E terceiro: porque a mesma regra que protege o banco atrai quem vende por volume. Por isso o governo, o TCU e a própria Febraban passaram os últimos anos tentando apertar esse mercado.",
  "vis": {"type": "compare", "left": ["Para o banco", "parcela garantida", "juro baixo compensa", "cliente disputado"], "right": ["Para quem toma", "parcela intocável", "anos de desconto", "pouco espaço no mês"],
          "caption": "Análise do canal"}},
 {"say": "Uma dica prática, que vale para qualquer crédito: antes de assinar, olhe o valor total que você vai pagar, e não só a parcela. Se você é aposentado do INSS, dá para consultar todos os seus empréstimos no extrato do Meu INSS. E nunca passe dados ou faça biometria por causa de uma ligação que você não pediu.",
  "vis": {"type": "cards", "title": "Antes de assinar", "cards": [["1", "Valor total", "não só a parcela"], ["2", "Extrato", "Meu INSS mostra\ntodos os contratos"], ["3", "Ligação", "não peça,\nnão aceite"]],
          "highlight": 0, "caption": "Canais oficiais: app Meu INSS e telefone 135"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira. É só a leitura do contrato, para você entender como o dinheiro se move.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E já que falamos dos bancos que ganham com o crédito, no próximo episódio vamos falar de quem prometeu acabar com as tarifas e virou um dos maiores bancos do país: o Nubank. Como um banco sem agência e sem tarifa ganha dinheiro, e de onde vem o lucro dele.",
  "vis": {"type": "title", "title": "Próximo: o Nubank", "sub": "como um banco sem tarifa dá lucro"}},
]
