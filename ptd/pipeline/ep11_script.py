# EP11 — Os descontos no INSS: o golpe que saiu do benefício dos aposentados
# Estrutura NOVA: "investigação em 5 pistas" — cada bloco abre uma pasta de arquivo com carimbo (cena nova: dossier).
# Pista 1 A porta (a regra que permitia o desconto), Pista 2 A escala (quanto cresceu), Pista 3 As vítimas (a auditoria),
# Pista 4 Os alarmes (os sinais que vieram antes), Pista 5 A conta (quem devolveu e quem paga). Fecha com "o que o caso ensina".
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível), EP07 (autópsia), EP08 (truque em 4 atos),
# EP09 (caixa-preta), EP10 (julgamento).
# Loops: (1) como ninguém percebeu -> Pistas 1 e 3; (2) quem devolveu o dinheiro -> Pista 5.
# Re-engajamentos: ~3:00 a auditoria (97,6%); ~6:00 quem paga a devolução.
# R$ 6,3 bilhões = estimativa da PF/CGU de tudo o que foi descontado por entidades investigadas de 2019 a 2024 (nem todo desconto
# foi comprovadamente irregular; valor sob apuração). Exemplo de R$ 45 por mês é ILUSTRATIVO (marcado na tela).
TITLE = "O golpe dos descontos no INSS: como R$ 6,3 bilhões saíram dos aposentados"

CASE = "CASO: DESCONTOS NO INSS"
SCENES = [
 # ---------- GANCHO ----------
 {"say": "Imagine um desconto de quarenta e cinco reais por mês, todo mês, saindo da sua aposentadoria. Com um nome que você nunca ouviu, e para uma associação que você nunca procurou.",
  "vis": {"type": "receipt", "title": "Extrato do benefício (exemplo)", "head": "BENEFÍCIO · MÊS DE REFERÊNCIA", "lines": [["Valor do benefício", "R$ 1.518,00", "#1E2A40"], ["CONTRIB. ASSOC. XYZ", "- R$ 45,00", "#D63E34"]], "total": ["Valor líquido", "R$ 1.473,00"],
          "caption": "Exemplo ilustrativo do canal — nome e valores fictícios"}},
 {"say": "Agora multiplique isso por milhões de aposentados e pensionistas, durante anos. Segundo a Polícia Federal e a Controladoria-Geral da União, as entidades investigadas descontaram até seis vírgula três bilhões de reais de benefícios do INSS entre dois mil e dezenove e dois mil e vinte e quatro.",
  "vis": {"type": "bignumber", "from": 0, "to": 6.3, "prefix": "R$ ", "suffix": " bilhões", "decimals": 1, "warn": True, "caption": "descontados por entidades investigadas, de 2019 a 2024",
          "source": "Fonte: PF e CGU, Operação Sem Desconto (abr/2025) — estimativa sob apuração"}},
 {"say": "Como um esquema desse tamanho passou anos sem ninguém perceber? E quando ele foi descoberto, quem devolveu o dinheiro? A resposta para a segunda pergunta é a mais incômoda, porque envolve o seu dinheiro também, mesmo que você nunca tenha sido aposentado do INSS.",
  "vis": {"type": "compare", "left": ["Pergunta 1", "como ninguém", "percebeu", "por anos?"], "right": ["Pergunta 2", "quem devolveu", "o dinheiro", "aos aposentados?"],
          "caption": "As duas perguntas deste episódio"}},
 {"say": "Hoje a gente vai investigar esse caso como um detetive. São cinco pistas. Cada uma explica uma parte de como o dinheiro saiu, e de onde ele voltou.",
  "vis": {"type": "title", "title": "O golpe dos\ndescontos no INSS", "sub": "POR TRÁS DO DINHEIRO", "brand": True}},

 # ---------- PISTA 1: A PORTA ----------
 {"say": "Pista número um. A porta. Todo golpe precisa de uma entrada. E essa entrada estava na própria lei.",
  "vis": {"type": "dossier", "n": 1, "label": "A PORTA", "title": "Uma regra\nlegal", "sub": "o desconto associativo", "stamp": "EVIDÊNCIA", "case": CASE}},
 {"say": "A lei de benefícios da Previdência, de mil novecentos e noventa e um, sempre permitiu que associações de aposentados legalmente reconhecidas cobrassem a mensalidade direto no benefício, desde que o filiado autorizasse. Não havia nada de ilegal nisso. Funcionava assim: a entidade assinava um acordo de cooperação técnica com o INSS. O aposentado autorizava. E o desconto já vinha na folha, antes de o dinheiro cair na conta.",
  "vis": {"type": "flow", "nodes": ["Entidade", "Acordo com o INSS", "Autorização", "Desconto na folha"], "notes": ["associação ou sindicato", "cooperação técnica", "do aposentado", "antes do pagamento"], "pulse": True,
          "caption": "Lei 8.213/1991, art. 115; funcionamento segundo a CGU e o MPF"}},
 {"say": "Na teoria, era uma comodidade. A associação oferecia benefícios, como assistência jurídica ou descontos em serviços, e o associado não precisava pagar um boleto todo mês.",
  "vis": {"type": "title", "title": "Na teoria,\numa comodidade.", "sub": "sem boleto, direto na folha"}},
 {"say": "O ponto fraco estava na palavra autorização. Quem conferia se o aposentado realmente tinha autorizado? As investigações apontaram termos assinados sem o aposentado saber, uso indevido de biometria e até assinaturas falsificadas. E entidades sem estrutura real para entregar o que prometiam.",
  "vis": {"type": "bullets", "title": "O que as investigações apontaram", "items": ["Termos assinados sem ciência", "Uso indevido de biometria", "Assinaturas falsificadas", "Entidades sem estrutura real"], "highlight": 2,
          "caption": "Fontes: PF, CGU e MPF, via Politize e imprensa (2025)"}},
 {"say": "Repare no desenho. O dinheiro saía antes de chegar ao aposentado. Para parar de pagar, era ele quem tinha que descobrir o desconto e pedir para cancelar. O ônus da prova estava invertido.",
  "vis": {"type": "compare", "left": ["Como deveria ser", "a entidade prova", "a autorização", "antes de cobrar"], "right": ["Como funcionava", "o aposentado descobre", "o desconto", "e pede para cancelar"],
          "caption": "Análise do canal"}},

 # ---------- PISTA 2: A ESCALA ----------
 {"say": "Pista número dois. A escala. Um golpe pequeno não chama atenção. O problema é quando o pequeno é multiplicado.",
  "vis": {"type": "dossier", "n": 2, "label": "A ESCALA", "title": "O desconto\nque cresceu", "sub": "de milhões a bilhões", "stamp": "ALERTA", "case": CASE}},
 {"say": "Os números da CGU mostram a curva. Em dois mil e dezesseis, os descontos de mensalidades associativas somavam quatrocentos e treze milhões de reais. Em dois mil e vinte e três, já eram um vírgula três bilhão. E em dois mil e vinte e quatro, dois vírgula oito bilhões.",
  "vis": {"type": "bars", "title": "Descontos associativos em benefícios do INSS, por ano", "items": [["2016", 0.413, "#5B8DEF"], ["2023", 1.3, "#F2A93B"], ["2024", 2.8, "#E06C5A"]], "prefix": "R$ ", "suffix": " bi", "decimals": 2,
          "caption": "Fonte: CGU, via Band e Agência Gov (abr/2025)"}},
 {"say": "Em oito anos, o valor ficou quase sete vezes maior. E só entre dois mil e vinte e três e dois mil e vinte e quatro, mais que dobrou. Nenhum clube de benefícios cresce assim de forma orgânica. O que cresceu foi a máquina de filiação.",
  "vis": {"type": "bignumber", "from": 1, "to": 6.8, "suffix": "x", "decimals": 1, "warn": True, "caption": "crescimento dos descontos entre 2016 e 2024",
          "source": "Cálculo do canal com dados da CGU: R$ 2,8 bi ÷ R$ 413 mi"}},
 {"say": "Segundo o ministro da CGU, cerca de seis milhões de pessoas tinham algum desconto associativo todo mês no benefício. É mais gente do que a população inteira de vários estados brasileiros.",
  "vis": {"type": "bignumber", "from": 0, "to": 6, "suffix": " milhões", "decimals": 0, "caption": "de beneficiários com desconto associativo todo mês",
          "source": "Fonte: ministro da CGU, Vinicius Marques de Carvalho (abr/2025)"}},
 {"say": "E aqui está o segredo da escala. Um desconto de quarenta e cinco reais quase não aparece num extrato. Mas quarenta e cinco reais vezes um milhão de pessoas são quarenta e cinco milhões por mês. Em um ano, mais de meio bilhão. Um valor pequeno para cada vítima, enorme para quem recebe.",
  "vis": {"type": "flow", "nodes": ["R$ 45", "x 1 milhão", "R$ 45 milhões", "R$ 540 milhões"], "notes": ["por pessoa, por mês", "de beneficiários", "por mês", "por ano"], "pulse": True,
          "caption": "Exemplo ilustrativo do canal"}},

 # ---------- PISTA 3: AS VÍTIMAS ----------
 # REENGAJE ~3:00
 {"say": "Pista número três. As vítimas. Aqui está a prova mais forte do caso inteiro.",
  "vis": {"type": "dossier", "n": 3, "label": "AS VÍTIMAS", "title": "O que disseram\nos aposentados", "sub": "a auditoria da CGU", "stamp": "PROVA", "case": CASE}},
 {"say": "A CGU foi atrás de quem estava pagando. Entrevistou mil duzentos e setenta e três aposentados e pensionistas que tinham desconto associativo no benefício. E fez uma pergunta simples: você autorizou esse desconto?",
  "vis": {"type": "bignumber", "from": 0, "to": 1273, "decimals": 0, "caption": "aposentados e pensionistas entrevistados pela CGU",
          "source": "Fonte: relatório da CGU (abr/2025), via Agência Gov e Agência Brasil"}},
 {"say": "Noventa e sete vírgula seis por cento disseram que não. Quase noventa e seis por cento disseram que nem eram filiados a associação nenhuma. Só trinta e uma pessoas, de mil duzentos e setenta e três, confirmaram que tinham autorizado.",
  "vis": {"type": "stack", "title": "Entrevistados pela CGU: autorizaram o desconto?", "parts": [["Não autorizaram", 97.6, "#E06C5A", "97,6%"], ["Autorizaram", 2.4, "#3AC47D", "31 pessoas"]], "highlight": 0,
          "caption": "Fonte: CGU (abr/2025), via Agência Gov e Tribuna de Minas"}},
 {"say": "Pense no perfil dessas vítimas. Muita gente idosa, que recebe pouco, que não acessa aplicativo e que não confere o extrato do benefício linha por linha. Não é falta de atenção. É um golpe desenhado para o público que menos tem como se defender.",
  "vis": {"type": "cards", "title": "Por que o golpe funcionava", "cards": [["1", "Valor pequeno", "some no\nextrato"], ["2", "Público idoso", "menos acesso\ndigital"], ["3", "Desconto na fonte", "o dinheiro sai\nantes de chegar"]],
          "highlight": 2, "caption": "Análise do canal"}},

 {"say": "E quarenta e cinco reais não é pouco para todo mundo. Para quem recebe um salário mínimo, é perto de três por cento do benefício. É o gás de cozinha, parte da conta de luz ou um remédio do mês. Para uma pessoa, um prejuízo silencioso. Para o esquema, uma receita garantida.",
  "vis": {"type": "bignumber", "from": 0, "to": 3, "suffix": "%", "decimals": 0, "warn": True, "caption": "de um benefício de um salário mínimo (R$ 1.518) vão em R$ 45 por mês",
          "source": "Exemplo ilustrativo do canal com o salário mínimo de 2025"}},

 # ---------- PISTA 4: OS ALARMES ----------
 {"say": "Pista número quatro. Os alarmes. Um esquema dessa escala raramente acontece em silêncio. A pergunta é quem ouviu os alarmes, e quando.",
  "vis": {"type": "dossier", "n": 4, "label": "OS ALARMES", "title": "Os sinais\nque vieram antes", "sub": "2023 e 2024", "stamp": "IGNORADO?", "case": CASE}},
 {"say": "O primeiro alarme veio dos próprios aposentados. Entre janeiro de dois mil e vinte e três e o primeiro semestre de dois mil e vinte e quatro, o INSS recebeu mais de um milhão de pedidos para tirar descontos de associações e sindicatos. Mais de um milhão de pessoas reclamando da mesma coisa. Quando o mesmo problema aparece um milhão de vezes, ele deixa de ser um erro isolado e vira um padrão.",
  "vis": {"type": "bignumber", "from": 0, "to": 1.2, "suffix": " milhão", "decimals": 1, "warn": True, "caption": "de pedidos de exclusão de descontos, jan/2023 a meados de 2024",
          "source": "Fonte: auditoria do INSS e CGU, via Jornal do Comércio e Agência Brasil (mai/2025)"}},
 {"say": "Em dois mil e vinte e quatro vieram as auditorias. O próprio INSS identificou descontos irregulares em setembro daquele ano, e a partir de novembro a exclusão passou a ser feita pelo aplicativo Meu INSS. Mas os descontos continuaram, e o valor de dois mil e vinte e quatro foi o maior da série.",
  "vis": {"type": "timeline", "even": True, "points": [["2023-24", "+1 milhão de pedidos"], ["set/2024", "INSS vê irregularidades"], ["nov/2024", "exclusão pelo app"], ["2024", "recorde de descontos"]],
          "caption": "Os alarmes tocaram"}},
 {"say": "O alarme final soou em vinte e três de abril de dois mil e vinte e cinco. A Polícia Federal e a CGU deflagraram a Operação Sem Desconto: duzentos e onze mandados de busca e apreensão, em treze estados e no Distrito Federal, e o bloqueio de bens de um bilhão de reais.",
  "vis": {"type": "cards", "title": "Operação Sem Desconto (23/04/2025)", "cards": [["211", "mandados", "de busca e\napreensão"], ["13 + DF", "estados", "alcançados"], ["R$ 1 bi", "bloqueados", "em bens"]],
          "highlight": 0, "caption": "Fonte: PF e CGU, via SBT News e Agência Gov"}},
 {"say": "No mesmo dia, o presidente do INSS, Alessandro Stefanutto, foi afastado do cargo. Dias depois, o ministro da Previdência, Carlos Lupi, deixou o cargo. E o governo suspendeu todos os acordos que permitiam os descontos associativos.",
  "vis": {"type": "bullets", "title": "As consequências imediatas", "items": ["Presidente do INSS afastado", "Ministro da Previdência sai", "Todos os acordos suspensos", "Investigação em várias frentes"], "highlight": 2,
          "caption": "Fontes: Agência Gov, Agência Brasil e imprensa (abr-mai/2025)"}},
 {"say": "No Congresso, uma CPI mista investigou o caso por meses. Mas ela terminou em março de dois mil e vinte e seis sem relatório final aprovado: o parecer do relator foi rejeitado por dezenove votos a doze. A investigação criminal, essa continua, com novas fases da operação em dois mil e vinte e seis.",
  "vis": {"type": "compare", "left": ["CPMI do INSS", "terminou em mar/2026", "relatório rejeitado", "19 votos a 12"], "right": ["Investigação criminal", "PF e CGU", "novas fases", "em 2026"],
          "caption": "Fontes: Agência Senado, Nexo e Movimento Econômico (2026)"}},

 # ---------- PISTA 5: A CONTA ----------
 # REENGAJE ~6:00
 {"say": "Pista número cinco. A conta. E aqui volta a pergunta do começo: quem devolveu o dinheiro aos aposentados?",
  "vis": {"type": "dossier", "n": 5, "label": "A CONTA", "title": "Quem devolveu\no dinheiro", "sub": "e quem paga no fim", "stamp": "EM ABERTO", "case": CASE}},
 {"say": "O caminho natural seria cobrar de quem recebeu. Mas isso leva anos na Justiça. Então o governo inverteu a ordem: primeiro devolve ao aposentado, depois tenta recuperar das entidades. Em julho de dois mil e vinte e cinco, uma medida provisória abriu um crédito extraordinário de cerca de três vírgula três bilhões de reais para pagar os ressarcimentos.",
  "vis": {"type": "flow", "nodes": ["Tesouro Nacional", "Aposentado", "AGU na Justiça", "Bens das entidades"], "notes": ["paga primeiro", "recebe de volta", "cobra os responsáveis", "para recompor o caixa"], "pulse": True,
          "caption": "Fontes: AGU, via Agência Brasil e Gazeta do Povo (jun-jul/2025)"}},
 {"say": "Até outubro de dois mil e vinte e seis, segundo o governo, cerca de três vírgula seis bilhões de reais tinham sido devolvidos a cinco vírgula um milhões de aposentados e pensionistas que contestaram os descontos. Outro um vírgula seis milhão de pedidos ainda esperava, porque as entidades questionaram as cobranças.",
  "vis": {"type": "bars", "title": "Ressarcimento dos descontos (até out/2026)", "items": [["Pessoas ressarcidas", 5.1, "#3AC47D"], ["Pedidos à espera", 1.6, "#F2A93B"]], "suffix": " mi", "decimals": 1,
          "caption": "Fonte: governo federal, via Diário do Comércio e Contec (out/2026) — R$ 3,6 bilhões devolvidos"}},
 {"say": "Como funcionou a devolução na prática? O aposentado contestava o desconto pelo aplicativo Meu INSS, pelo telefone cento e trinta e cinco ou numa agência dos Correios. A entidade era chamada a provar que tinha autorização. Se não provasse, o aposentado recebia o dinheiro de volta. Simples no papel, mas foram milhões de pedidos para analisar.",
  "vis": {"type": "flow", "nodes": ["Aposentado contesta", "Entidade é notificada", "Sem prova", "Dinheiro devolvido"], "notes": ["Meu INSS, 135, Correios", "precisa provar", "da autorização", "pelo INSS"], "pulse": True,
          "caption": "Fontes: INSS e governo federal, via imprensa (2025-2026)"}},
 {"say": "Agora compare com o que foi bloqueado. Em junho de dois mil e vinte e cinco, a Justiça Federal bloqueou dois vírgula oito bilhões de reais em bens de doze entidades, seis consultorias e quatro pessoas. Bloquear não é recuperar. Até esse dinheiro voltar de verdade, a devolução saiu do Tesouro. Ou seja, do bolso de todos os contribuintes.",
  "vis": {"type": "compare", "left": ["Devolvido", "R$ 3,6 bilhões", "pagos pelo Tesouro", "até out/2026"], "right": ["Bloqueado", "R$ 2,8 bilhões", "em bens, na Justiça", "ainda a recuperar"],
          "caption": "Fontes: governo federal e AGU, via Agência Brasil — comparação do canal"}},
 {"say": "A resposta do Congresso veio em janeiro de dois mil e vinte e seis. A Lei quinze mil trezentos e vinte e sete proibiu de vez os descontos de mensalidades associativas nos benefícios do INSS, mesmo com autorização. E determinou que qualquer desconto indevido seja devolvido integralmente em até trinta dias.",
  "vis": {"type": "timeline", "even": True, "points": [["abr/2025", "Operação Sem Desconto"], ["jul/2025", "crédito para devolver"], ["06/01/2026", "Lei 15.327 proíbe"]],
          "caption": "A porta foi fechada"}},

 # ---------- O QUE O CASO ENSINA ----------
 {"say": "Fechadas as pistas, vamos à análise do canal. O que esse caso ensina sobre dinheiro?",
  "vis": {"type": "title", "title": "O que o caso\nensina", "sub": "análise do canal"}},
 {"say": "Primeiro: o desconto na fonte é o meio de cobrança mais poderoso que existe. Quem cobra antes de o dinheiro chegar nunca enfrenta calote. Por isso esse canal é tão disputado, por associações, por bancos e por qualquer um que queira receber em dia. E por isso ele precisa de muito mais controle do que um boleto, porque o erro só aparece depois que o dinheiro já saiu.",
  "vis": {"type": "bullets", "title": "Lições do caso", "items": ["Desconto na fonte é poder", "Valor pequeno esconde escala", "Alarme ignorado custa caro", "A conta vai para o contribuinte"], "highlight": 0}},
 {"say": "Segundo: golpe em escala não precisa de valor alto. Precisa de valor pequeno, repetido milhões de vezes, contra quem tem menos chance de conferir. Terceiro: os sinais estavam lá. Mais de um milhão de pedidos de exclusão é um alarme do tamanho de uma cidade.",
  "vis": {"type": "compare", "left": ["Para a vítima", "R$ 45 por mês", "quase invisível", "no extrato"], "right": ["Para o esquema", "milhões de pessoas", "bilhões de reais", "em poucos anos"],
          "caption": "Análise do canal — valor de R$ 45 ilustrativo"}},
 {"say": "E quarto: quando o controle falha, a conta raramente fica só com quem errou. Ela se espalha. Primeiro no bolso do aposentado, e depois no orçamento público, que é dinheiro de todo mundo.",
  "vis": {"type": "title", "title": "Quando o controle falha,\na conta se espalha.", "sub": "do aposentado para todos os contribuintes"}},
 {"say": "Uma dica prática, que vale para qualquer pessoa: confira o extrato do benefício, do salário ou do cartão linha por linha, pelo menos uma vez por mês. E se você tem pais ou avós aposentados, confira com eles.",
  "vis": {"type": "cards", "title": "Hábito de proteção", "cards": [["1", "Extrato mensal", "linha por linha"], ["2", "Desconto estranho", "pergunte e conteste"], ["3", "Família", "confira com os\nmais velhos"]],
          "highlight": 2, "caption": "Canais oficiais: app Meu INSS e telefone 135"}},
 {"say": "Este vídeo é informativo e não é recomendação financeira. É só a leitura dos documentos, para você entender como o dinheiro se move.",
  "vis": {"type": "title", "title": "Este vídeo é informativo", "sub": "não é recomendação financeira"}},
 {"say": "E já que falamos de descontos na aposentadoria, no próximo episódio vamos falar do desconto que é legal, e que movimenta muito mais dinheiro: o empréstimo consignado. Por que os bancos disputam tanto o aposentado, quanto custa esse crédito, e quem ganha com ele.",
  "vis": {"type": "title", "title": "Próximo: o consignado", "sub": "por que os bancos disputam o aposentado"}},
]
