# Gera o publish.json do EP08 (longo 18:00, Short do episódio 19:00 em 09/11; ranking #6 12:00 em 10/11)
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Gancho: −77% em um dia"), (3, "Ato 1: o número que a plateia via"), (7, "Ato 2: o segredo — risco sacado"),
        (11, "O truque maior: VPC (R$ 21,7 bi)"), (15, "Por que montar um truque desses"), (16, "Ato 3: por que ninguém viu"),
        (21, "Ato 4: as luzes acendem"), (23, "Operação Disclosure: R$ 287 mi em ações"), (26, "1.369 dias e 12 réus"),
        (28, "Quem pagou o ingresso"), (29, "O truque, desmontado"), (31, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Americanas: como esconder R$ 25 bilhões no balanço (e por que ninguém viu)"
desc = f"""Em 12 de janeiro de 2023 a ação da Americanas caiu 77,33% em um único dia. O motivo: um rombo que começou em R$ 20 bilhões e passou de R$ 25 bilhões. Neste episódio desmontamos o truque em 4 atos: o número que a plateia via, o segredo (risco sacado e VPC falso), por que auditores, bancos e mercado não viram, e o que aconteceu quando as luzes acenderam — da recuperação judicial (encerrada em 19/10/2026) aos 12 ex-executivos que viraram réus.

Capítulos
{chap}

Fontes
- B3 (Bora Investir) e Forbes Brasil (12/01/2023): AMER3 −77,33%, de R$ 12,00 para R$ 2,72; TradeMap: perda de ~R$ 8,4 bi em valor de mercado
- Fato relevante de 11/01/2023, via InfoMoney: inconsistências de ~R$ 20 bi; saída de Sergio Rial e André Covre
- Forbes Brasil (19/01/2023): dívida informada de ~R$ 20,8 bi no 3º tri/2022; pedido de recuperação judicial com R$ 43 bi e 16,3 mil credores
- Fato relevante de 13/06/2023, via Mercado & Consumo e Suno: resultado inflado em R$ 25,3 bi (VPC artificial R$ 21,7 bi; juros não contabilizados R$ 3,6 bi); risco sacado R$ 18,4 bi registrado de forma inadequada
- Depoimento do presidente da Americanas à CPI (jun/2023), via Folha de Pernambuco
- Americanas, comunicado de 17/07/2024 sobre o comitê independente, via Mercado & Consumo
- Polícia Federal / MPF, Operação Disclosure (27/06/2024), via Mercado & Consumo, InfoMoney e IstoÉ Dinheiro: R$ 287 mi em ações vendidas antes do anúncio; bloqueio de mais de R$ 500 mi
- Plano aprovado em 19/12/2023 e homologado em fev/2024; aumento de capital de ~R$ 24,5 bi a R$ 1,30 por ação (Mercado & Consumo, 27/07/2024)
- Agência Brasil (out/2026): fim da recuperação judicial em 19/10/2026 (contagem de 1.369 dias feita pelo canal)
- Band (out/2026): Justiça Federal do RJ torna réus 12 ex-executivos; denúncia do MPF de mar/2025. Ser réu não é ser condenado; as defesas negam os crimes.
- Exemplos com R$ 100 são ilustrativos.

Este vídeo é informativo e não é recomendação financeira. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#americanas #fraude #balanço #financas #portrasdodinheiro"""
tags = ["americanas", "fraude americanas", "rombo americanas", "risco sacado", "vpc", "verba de propaganda cooperada", "fraude contabil",
        "recuperacao judicial", "americanas recuperacao judicial", "operacao disclosure", "miguel gutierrez", "sergio rial", "amer3",
        "balanço", "contabilidade", "economia", "financas", "por tras do dinheiro"]
SH_TITLE = "Como a Americanas escondeu R$ 25 bilhões numa linha do balanço #shorts"
RK_TITLE = "As 5 maiores recuperações judiciais do Brasil (a nº 1 devia quase R$ 100 bilhões) #shorts"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-ep08-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-09T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Na sua opinião, quem deveria ter percebido primeiro o rombo da Americanas: auditoria, bancos, conselho ou o mercado?"},
  {"key": "ptd-ep08-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "Dívida de banco escondida em fornecedores e verba que nunca existiu virando lucro: o truque de R$ 25,3 bilhões da Americanas. Fonte: fato relevante da Americanas (13/06/2023), via Mercado & Consumo. Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #americanas #fraude #financas",
   "tags": ["americanas", "fraude", "risco sacado", "vpc", "balanço", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-09T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep08-long",
   "pinned_comment": "Você já tinha ouvido falar em risco sacado? Vídeo completo: " + LONG_TITLE},
  {"key": "ptd-rank06-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "As 5 maiores recuperações judiciais do Brasil pela dívida declarada no pedido (valores da época, sem correção): 5) Sete Brasil (2016) R$ 19,3 bi; 4) Americanas (2023) R$ 43 bi; 3) Samarco (2021) ~R$ 50 bi; 2) Oi (2016) R$ 65 bi; 1) Odebrecht (2019) R$ 98,5 bi. Fonte: Forbes Brasil, fev/2023. Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #recuperacaojudicial #americanas #odebrecht #financas",
   "tags": ["recuperacao judicial", "maiores recuperacoes judiciais", "odebrecht", "oi", "samarco", "americanas", "sete brasil", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-10T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep08-long",
   "pinned_comment": "Qual dessas cinco quebras mais te surpreendeu? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s")
