# EP08 — Americanas: como esconder R$ 25 bilhões no balanço (e por que ninguém viu)
# Estrutura NOVA: "truque de mágica em 4 atos" — o caso contado como um número de ilusionismo:
# Ato 1 O número (o lucro que aparecia), Ato 2 O segredo (os 2 truques: risco sacado e VPC), Ato 3 A plateia
# (por que auditoria, bancos e mercado não viram), Ato 4 As luzes acendem (9 dias, RJ, 1.369 dias, réus) + payoff.
# Diferente do EP04 (extrato), EP05 (rounds), EP06 (siga o recebível) e EP07 (autópsia).
# Cenas novas: act (cortina de palco que abre com holofote) e ledger (balanço em que uma ficha de dívida muda de linha).
# Loops: (1) por que ninguém viu -> Ato 3; (2) o truque cabe numa linha do balanço -> Ato 2 (ledger);
#        (3) quem vendeu ações antes -> Ato 4.
# Re-engajamentos: ~3:00 o truque do VPC (R$ 21,7 bi); ~6:00 R$ 287 milhões em ações vendidas antes do anúncio.
# Exemplos com R$ 100 são ILUSTRATIVOS (marcados na tela).
TITLE = "Americanas: como esconder R$ 25 bilhões no balanço (e por que ninguém viu)"

SCENES = [
 # ---------- GANCHO ----------
 {"say": "Doze de janeiro de dois mil e vinte e três. A ação de uma das varejistas mais conhecidas do Brasil abre o pregão valendo doze reais. Fecha valendo dois e setenta e dois. Uma queda de setenta e sete por cento em um único dia.",
  "vis": {"type": "bignumber", "from": 0, "to": -77.33, "suffix": "%", "decimals": 2, "warn": True, "caption": "AMER3 em 12/01/2023: de R$ 12,00 para R$ 2,72",
          "source": "Fonte: B3 (Bora Investir) e Forbes Brasil, 12/01/2023"}},
 {"say": "O motivo cabia numa frase: faltavam vinte bilhões de reais no balanço. Depois, a própria empresa refez a conta, e o número passou de vinte e cinco bilhões. E isso não foi um assalto de uma noite. Foi um número de mágica apresentado durante anos, diante de auditores, bancos e analistas.",
  "vis": {"type": "title", "title": "O truque de\nR$ 25 bilhões", "sub": "Americanas — POR TRÁS DO DINHEIRO", "brand": True}},
 {"say": "Hoje vamos desmontar esse truque em quatro atos. Como o lucro aparecia, onde ficava o segredo, por que a plateia inteira aplaudiu sem ver nada, e o que aconteceu quando as luzes acenderam. E o segredo principal cabe em uma única linha do balanço.",
  "vis": {"type": "bullets", "title": "O show em 4 atos", "items": ["Ato 1: o número", "Ato 2: o segredo", "Ato 3: a plateia", "Ato 4: as luzes acendem"], "highlight": 1}},

 # ---------- ATO 1: O NÚMERO ----------
 {"say": "Ato um. O número. Para entender um truque, primeiro você precisa ver o que a plateia viu.",
  "vis": {"type": "act", "n": 1, "title": "O número", "sub": "o que a plateia via"}},
 {"say": "A Americanas nasceu em mil novecentos e vinte e nove, em Niterói. Virou sinônimo de loja de bairro, de chocolate na Páscoa e, depois, de compra pela internet. Em dois mil e vinte e um, juntou a rede de lojas com o braço digital e formou uma só empresa. Por trás dela estavam três dos homens mais ricos do país: Jorge Paulo Lemann, Marcel Telles e Beto Sicupira, os acionistas de referência.",
  "vis": {"type": "timeline", "even": True, "points": [["1929", "nasce em Niterói"], ["anos 2000", "vira gigante do online"], ["2021", "lojas + digital viram 1 empresa"], ["jan/2023", "o rombo"]],
          "caption": "Fonte: histórico da companhia e imprensa econômica"}},
 {"say": "O número que a plateia via era o de uma varejista que vendia muito, crescia no online e tinha uma dívida considerada administrável. No fim do terceiro trimestre de dois mil e vinte e dois, segundo a Forbes Brasil, a empresa informava dever cerca de vinte vírgula oito bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 20.8, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "caption": "dívida que a Americanas informava no 3º trimestre de 2022",
          "source": "Fonte: Forbes Brasil, 19/01/2023"}},
 {"say": "Guarde esse número. Porque, uma semana depois do escândalo, quando a empresa pediu proteção na Justiça, a lista de dívidas tinha mais que o dobro: quarenta e três bilhões de reais, com mais de dezesseis mil credores. A diferença entre esses dois números é o truque.",
  "vis": {"type": "compare", "left": ["O que aparecia", "R$ 20,8 bilhões", "dívida informada", "3º trimestre de 2022"], "right": ["O que existia", "R$ 43 bilhões", "dívida no pedido de RJ", "19/01/2023 · 16,3 mil credores"],
          "caption": "Fonte: Forbes Brasil, 19/01/2023 (critérios diferentes: o pedido inclui fornecedores e outras dívidas)"}},

 # ---------- ATO 2: O SEGREDO ----------
 {"say": "Ato dois. O segredo. Todo truque de mágica depende de desviar o seu olhar. E aqui o desvio aconteceu dentro de uma planilha.",
  "vis": {"type": "act", "n": 2, "title": "O segredo", "sub": "dois truques, uma planilha"}},
 {"say": "O primeiro truque tem um nome estranho: risco sacado. Funciona assim, num exemplo ilustrativo. A Americanas compra cem reais de um fornecedor e combina pagar em noventa dias. Só que o fornecedor quer o dinheiro agora. Então um banco paga o fornecedor hoje, e a Americanas passa a dever esses cem reais ao banco, com juros.",
  "vis": {"type": "flow", "nodes": ["Americanas compra", "Banco paga o fornecedor", "Americanas deve ao banco", "Paga depois, com juros"], "notes": ["R$ 100 em 90 dias", "hoje", "não mais ao fornecedor", ""], "pulse": True,
          "caption": "Exemplo ilustrativo: como funciona o risco sacado"}},
 {"say": "Até aqui, nada de ilegal. Muitas varejistas usam isso. O problema é onde essa dívida aparece. Se a empresa agora deve a um banco, com juros, isso parece muito com um empréstimo. Mas no balanço da Americanas essa dívida continuava escrita na linha de fornecedores, como se fosse uma simples conta a pagar.",
  "vis": {"type": "ledger", "title": "A mesma dívida, em outra linha", "rows": [["Empréstimos (bancos)", "juros"], ["Fornecedores", "a pagar"], ["Outras obrigações", "…"]],
          "move": [0, 1, "R$ 100 risco sacado"], "stamp": "ESCONDIDO", "caption": "Exemplo ilustrativo — o valor real do risco sacado foi de R$ 18,4 bilhões"}},
 {"say": "Parece só uma troca de lugar. Mas faz toda a diferença. Analistas e bancos medem o risco de uma empresa olhando a dívida financeira. Ao esconder a dívida com bancos entre os fornecedores, a empresa parecia muito menos endividada do que era. E os juros dessa dívida também sumiam da conta. Segundo a própria Americanas, o risco sacado registrado de forma inadequada somava dezoito vírgula quatro bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 18.4, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "warn": True, "caption": "risco sacado registrado de forma inadequada no balanço",
          "source": "Fonte: fato relevante da Americanas, 13/06/2023, via Mercado & Consumo"}},
 # REENGAJE ~3:00
 {"say": "Mas esse ainda não é o truque maior. O maior tem outra sigla: V P C, verba de propaganda cooperada. É um dinheiro real e comum no varejo. O fornecedor paga para a loja dar destaque ao produto dele, num encarte, numa vitrine, numa campanha.",
  "vis": {"type": "cards", "title": "VPC: o truque maior", "cards": [["1", "Fornecedor", "paga para aparecer\nna loja"], ["2", "Loja", "registra a verba\ne reduz o custo"], ["3", "Lucro", "sobe no\nbalanço"]],
          "highlight": 2, "caption": "Verba de propaganda cooperada: prática legal e comum no varejo"}},
 {"say": "Agora o truque. Segundo a empresa, foram criados contratos de VPC que não existiam de verdade. Era uma verba que nenhum fornecedor ia pagar. Mas ela entrava na contabilidade, diminuía a conta de fornecedores e engordava o lucro. Pela conta da Americanas, esses contratos artificiais inflaram o resultado em vinte e um vírgula sete bilhões de reais.",
  "vis": {"type": "bignumber", "from": 0, "to": 21.7, "prefix": "R$ ", "suffix": " bi", "decimals": 1, "warn": True, "caption": "resultado inflado por contratos artificiais de VPC",
          "source": "Fonte: fato relevante da Americanas, 13/06/2023, via Mercado & Consumo"}},
 {"say": "Some a isso três vírgula seis bilhões em juros que não foram contabilizados, e você chega ao valor total que a empresa anunciou em junho de dois mil e vinte e três: vinte e cinco vírgula três bilhões de reais de resultado que, na prática, não existia.",
  "vis": {"type": "stack", "title": "R$ 25,3 bilhões de resultado inflado (% do total)", "parts": [["VPC artificial", 86, "#E06C5A", "R$ 21,7 bi"], ["Juros", 14, "#F2A93B", "R$ 3,6 bi\nnão contabilizados"]],
          "caption": "Fonte: fato relevante da Americanas, 13/06/2023, via Mercado & Consumo e Suno"}},
 {"say": "Repare na elegância sombria do esquema. Os dois truques mexiam na mesma linha: fornecedores. O risco sacado enfiava dívida de banco ali dentro. O VPC falso tirava valor de lá, para virar lucro. Quem olhasse só o resultado final via uma empresa saudável.",
  "vis": {"type": "flow", "nodes": ["Dívida de banco", "Linha de fornecedores", "VPC falso", "Lucro maior"], "notes": ["entra escondida", "vira o esconderijo", "reduz a conta", "o número do show"], "pulse": True,
          "caption": "Análise: os dois truques passavam pela mesma linha do balanço"}},

 {"say": "E por que alguém montaria um truque desses? A Polícia Federal descreveu o objetivo como enganar o mercado. A lógica, numa análise do canal, é direta: um lucro maior deixa a ação mais cara, a dívida menor deixa o crédito mais barato, e os executivos com ações e bônus ligados ao resultado ganham junto. Enquanto o número do show continuasse de pé, todo mundo no palco saía ganhando.",
  "vis": {"type": "flow", "nodes": ["Lucro inflado", "Ação mais cara", "Crédito mais barato", "Bônus e ações valem mais"], "notes": ["no balanço", "na bolsa", "nos bancos", "para quem estava no palco"], "pulse": True,
          "caption": "Análise do canal sobre o incentivo; objetivo descrito pela PF, jun/2024"}},

 # ---------- ATO 3: A PLATEIA ----------
 {"say": "Ato três. A plateia. Essa é a pergunta que todo mundo fez: como ninguém viu? Auditores, bancos, conselho, analistas, investidores. Tinha muita gente olhando para o palco.",
  "vis": {"type": "act", "n": 3, "title": "A plateia", "sub": "por que ninguém viu?"}},
 {"say": "Primeiro, a auditoria. Uma auditoria independente não confere cada nota fiscal. Ela trabalha por amostragem e confia em documentos, como cartas enviadas por bancos confirmando os saldos. Na CPI da Americanas, em junho de dois mil e vinte e três, o atual presidente da empresa falou em números maquiados e em assinaturas falsas. Se o documento que chega ao auditor já vem montado, a amostra confirma a mentira.",
  "vis": {"type": "cards", "title": "Por que a auditoria não pegou", "cards": [["1", "Amostragem", "não confere\ncada operação"], ["2", "Documentos", "confia em cartas\ne contratos"], ["3", "Montagem", "papéis forjados,\nsegundo a empresa"]],
          "highlight": 2, "caption": "Fonte: depoimento do presidente da Americanas à CPI, jun/2023, via Folha de Pernambuco"}},
 {"say": "Segundo, a própria forma do truque. Ele não aparecia como um buraco no caixa. A empresa dizia, no próprio fato relevante de janeiro, que o efeito no caixa seria pequeno. O dinheiro não sumiu de uma conta. O que sumiu foi a verdade sobre quanto a empresa devia e quanto realmente lucrava.",
  "vis": {"type": "compare", "left": ["Roubo comum", "dinheiro sai do caixa", "aparece no extrato", "fácil de rastrear"], "right": ["Este truque", "o caixa fecha", "a dívida muda de linha", "o lucro é inventado"],
          "caption": "Análise própria; efeito caixa 'imaterial' segundo o fato relevante de 11/01/2023"}},
 {"say": "Terceiro, a confiança. Uma empresa quase centenária, com acionistas bilionários e auditada todo ano, ganha o benefício da dúvida. Ninguém revisa o truque de um mágico que se apresenta há décadas. E o relatório do comitê independente, em dois mil e vinte e quatro, apontou a participação da antiga diretoria, mas disse não ter identificado participação dos conselhos.",
  "vis": {"type": "bullets", "title": "Comitê independente (2024)", "items": ["Fraude confirmada", "Aponta ex-diretores, incluindo o ex-CEO", "Não identificou participação dos conselhos", "As defesas negam as acusações"], "highlight": 1,
          "caption": "Fonte: Americanas, comunicado de 17/07/2024, via Mercado & Consumo"}},
 {"say": "E é aqui que entra o personagem que quebrou o feitiço. Sergio Rial assumiu como presidente no começo de janeiro de dois mil e vinte e três. Em nove dias de gestão, ele e o novo diretor financeiro, André Covre, encontraram as tais inconsistências. Na noite de onze de janeiro, a empresa publicou o fato relevante, e os dois renunciaram.",
  "vis": {"type": "timeline", "even": True, "points": [["2/jan/2023", "Rial assume"], ["~9 dias", "acha as inconsistências"], ["11/jan", "fato relevante: R$ 20 bi"], ["11/jan", "Rial e Covre saem"]],
          "caption": "Fonte: fato relevante de 11/01/2023, via InfoMoney"}},

 # ---------- ATO 4: AS LUZES ACENDEM ----------
 {"say": "Ato quatro. As luzes acendem. E quando as luzes acendem num truque desse tamanho, tudo acontece muito rápido.",
  "vis": {"type": "act", "n": 4, "title": "As luzes acendem", "sub": "de 2023 a 2026"}},
 {"say": "No dia seguinte ao anúncio, a ação desabou setenta e sete por cento, e a empresa perdeu cerca de oito vírgula quatro bilhões de reais em valor de mercado em um único pregão. Sete dias depois, em dezenove de janeiro, pediu recuperação judicial, com quarenta e três bilhões em dívidas. O pedido foi aceito no mesmo dia.",
  "vis": {"type": "timeline", "even": True, "points": [["11/jan", "fato relevante: R$ 20 bi"], ["12/jan", "ação −77%: R$ 12 → R$ 2,72"], ["19/jan", "recuperação judicial: R$ 43 bi"]],
          "caption": "Fontes: B3 (Bora Investir), TradeMap, Forbes Brasil — jan/2023"}},
 # REENGAJE ~6:00
 {"say": "Mas teve um detalhe que mudou a história de vez. Em junho de dois mil e vinte e quatro, a Polícia Federal fez a Operação Disclosure. Segundo a investigação, ex-executivos venderam duzentos e oitenta e sete milhões de reais em ações da empresa antes de o rombo ser anunciado.",
  "vis": {"type": "bignumber", "from": 0, "to": 287, "prefix": "R$ ", "suffix": " mi", "decimals": 0, "warn": True, "caption": "ações vendidas por ex-executivos antes do anúncio do rombo, segundo a PF",
          "source": "Fonte: Polícia Federal, Operação Disclosure, 27/06/2024, via Mercado & Consumo"}},
 {"say": "A operação teve mandados de prisão contra o ex-presidente Miguel Gutierrez e a ex-diretora Anna Saicali, e o bloqueio de mais de quinhentos milhões de reais em bens. Gutierrez, que estava na Espanha, chegou a ser detido em Madri e foi solto no dia seguinte. A investigação usou a delação de dois ex-diretores da área financeira. As defesas negam participação na fraude.",
  "vis": {"type": "cards", "title": "Operação Disclosure (jun/2024)", "cards": [["1", "Mandados", "ex-CEO e\nex-diretora"], ["2", "R$ 500 mi+", "em bens\nbloqueados"], ["3", "Delação", "dois ex-diretores\nda área financeira"]],
          "highlight": 0, "caption": "Fonte: PF e MPF, via InfoMoney e IstoÉ Dinheiro, jun/2024 — as defesas negam"}},
 {"say": "Enquanto isso, a empresa tentava sobreviver. Os credores aprovaram o plano em dezembro de dois mil e vinte e três. A Justiça homologou em fevereiro de dois mil e vinte e quatro. E, em julho, veio um aumento de capital de cerca de vinte e quatro vírgula cinco bilhões de reais, a um real e trinta por ação. Quase metade veio dos acionistas de referência. A outra metade, de credores que trocaram dívida por ações.",
  "vis": {"type": "stack", "title": "Aumento de capital (jul/2024): ~R$ 24,5 bi (%)", "parts": [["Acionistas de referência", 49, "#5B8DEF", "~R$ 12 bi"], ["Credores", 51, "#3AC47D", "trocaram dívida\npor ações"]],
          "caption": "Fonte: Americanas, via Mercado & Consumo (27/07/2024) — divisão aproximada"}},
 {"say": "E chegamos a outubro de dois mil e vinte e seis, há três semanas. No dia dezenove, a Justiça do Rio encerrou a recuperação judicial da Americanas. Pelas nossas contas, mil trezentos e sessenta e nove dias depois do pedido.",
  "vis": {"type": "bignumber", "from": 0, "to": 1369, "suffix": " dias", "decimals": 0, "caption": "de 19/01/2023 (pedido) a 19/10/2026 (fim da recuperação judicial)",
          "source": "Fonte: Agência Brasil, out/2026; contagem de dias do canal"}},
 {"say": "Só que o fim da recuperação não é o fim do caso. No mesmo mês, a Justiça Federal no Rio aceitou a denúncia do Ministério Público e tornou réus doze ex-executivos, entre eles o ex-presidente Miguel Gutierrez. As acusações incluem manipulação de mercado e uso de informação privilegiada. Ser réu não é ser condenado, e as defesas negam os crimes.",
  "vis": {"type": "obit", "case": "PROCESSO", "name": "12 ex-executivos", "born": "denúncia do MPF: mar/2025", "died": "réus: out/2026", "cause": "manipulação de mercado e outros crimes",
          "note": "ser réu não é ser condenado; as defesas negam", "stamp": "EM ANDAMENTO", "stamp_col": "#2E86C1", "caption": "Fonte: Justiça Federal do RJ, via Band, out/2026"}},

 {"say": "E quem pagou o ingresso desse show? Quem tinha a ação viu o papel perder mais de três quartos do valor em um dia. Mais de dezesseis mil credores entraram na fila da recuperação judicial. Fornecedores, bancos e investidores de títulos tiveram de renegociar. E parte dos credores aceitou virar sócia de uma empresa que tinha acabado de mentir para eles.",
  "vis": {"type": "cards", "title": "Quem pagou o ingresso", "cards": [["1", "Acionistas", "−77% em\num único dia"], ["2", "16,3 mil", "credores na\nrecuperação"], ["3", "Credores", "viraram sócios\na R$ 1,30 por ação"]],
          "highlight": 1, "caption": "Fontes: B3 (Bora Investir), Forbes Brasil, Mercado & Consumo"}},

 # ---------- PAYOFF ----------
 {"say": "Então, como se escondem vinte e cinco bilhões de reais? Não com um cofre. Com uma linha do balanço. Dívida de banco que vira conta de fornecedor. Verba que nunca ia chegar e vira lucro. E uma plateia que confiava demais no mágico.",
  "vis": {"type": "bullets", "title": "O truque, desmontado", "items": ["Risco sacado: dívida escondida (R$ 18,4 bi)", "VPC falso: lucro inventado (R$ 21,7 bi)", "Juros que sumiram (R$ 3,6 bi)", "Plateia: confiança no nome"], "highlight": -1}},
 {"say": "A lição para quem acompanha empresas é simples e incômoda. Lucro é uma opinião contábil. Caixa e dívida são fatos. Quando o lucro sobe e a dívida parece pequena demais para o tamanho do negócio, vale perguntar onde está o resto. Isso não é conselho de investimento. É só o jeito de olhar o palco sem cair no truque.",
  "vis": {"type": "title", "title": "Lucro é opinião.\nDívida é fato.", "sub": "análise do canal — não é recomendação"}},
 {"say": "No próximo episódio, outro rombo, mas desta vez num banco. Como o Banco Master conseguia pagar tão acima do mercado nos seus investimentos, o que a Polícia Federal diz que encontrou, e quem paga a conta quando um banco quebra: o Fundo Garantidor de Créditos.",
  "vis": {"type": "title", "title": "Próximo: Banco Master", "sub": "e quem paga quando um banco quebra"}},
]
