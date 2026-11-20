# Gera o publish.json do EP17 (sexta 20/11/2026: ranking #17 12:00, longo 18:00 e Short do episódio 19:00).
# O ranking aponta para o EP07 (Como o Pix mudou os bancos, já publicado), porque às 12:00 o EP17 ainda não está no ar.
# Uso: python3 pub_ep17.py out/ep17/durs.json ep17/publish.json "<created_at>"
import json, sys
durs = json.load(open(sys.argv[1]))
def ts(i):
    s = int(sum(durs[:i])); return f"{s//60}:{s%60:02d}"
caps = [(0, "Três mil reais em segundos"), (4, "Marca 1: o Pix sai"), (7, "Marca 2: o dinheiro se espalha"),
        (11, "Marca 3: a primeira hora"), (15, "Marca 4: o bloqueio de 72 horas"), (18, "Marca 5: a devolução (e por que 9 em 10 são negados)"),
        (23, "Marca 6: o prazo de 80 dias e quem paga"), (27, "Os três freios"), (28, "As seis marcas"), (31, "Próximo episódio")]
chap = "\n".join(f"{ts(i)} {t}" for i, t in caps)
LONG_TITLE = "Golpe do Pix: para onde vai o seu dinheiro em segundos (e quem tem que devolver)"
desc = f"""Um golpe do Pix acompanhado num cronômetro de seis marcas: o segundo em que o Pix sai, os segundos em que o dinheiro se espalha por contas laranja, a primeira hora (o botão de contestação), o bloqueio de 72 horas, a devolução pelo Mecanismo Especial de Devolução (MED) e o prazo final de 80 dias. E a pergunta que mais importa: por que 9 em cada 10 pedidos de devolução são negados, e quando o banco tem que pagar.

Capítulos
{chap}

Fontes
- Banco Central, dados do MED de janeiro de 2022 a abril de 2026, via O POVO (julho de 2026): R$ 24,52 bilhões notificados em golpes no Pix, R$ 2,2 bilhões devolvidos (8,9%, ou R$ 8,90 a cada R$ 100); R$ 13,7 bilhões não devolvidos por falta de saldo na conta recebedora
- Banco Central, dados de janeiro a abril de 2026, via SBT News (agosto de 2026): 11,8 milhões de pedidos de devolução abertos, 10,7 milhões recusados (90,3%), R$ 264,7 milhões devolvidos
- Banco Central: falta de saldo como principal motivo das devoluções não realizadas; estimativa de devolução em até 11 dias após a contestação; botão de contestação nos aplicativos desde 01/10/2025 (via imprensa)
- Resolução BCB 103/2021 (criação do MED, em vigor desde 16/11/2021); Resolução BCB 142/2021 (limite de R$ 1.000 para Pix entre pessoas físicas das 20h às 6h, com prazo de 24 a 48 horas para aumentar); Resolução BCB 147/2021 (bloqueio cautelar de até 72 horas)
- Resolução BCB 493/2025 (MED 2.0: rastreio dos valores pelas contas seguintes; obrigatório desde 02/02/2026; prazo de até 80 dias para pedir a devolução)
- Banco Central, estatísticas de meios de pagamento do 1º semestre de 2026 (divulgadas em 27/10/2026, via imprensa): Pix com 55,2% das transações e cartões com 30,8%
- Fórum Brasileiro de Segurança Pública, Anuário Brasileiro de Segurança Pública 2026: 2,26 milhões de estelionatos registrados em 2025
- STJ, Súmula 479, e decisões recentes do STJ sobre o golpe da falsa central (banco não responde quando as transações são compatíveis com o perfil do cliente), via imprensa jurídica
- Exemplo do golpe de R$ 3.000 e tempos de "10 segundos" e "1 hora" = EXEMPLO ILUSTRATIVO.

Em caso de golpe, procure o seu banco pelos canais oficiais e registre um boletim de ocorrência.

Este vídeo é informativo e não é recomendação financeira nem orientação jurídica. Narração com voz sintética; roteiro, pesquisa e visual próprios. "Análise" na tela = interpretação do canal.

#pix #golpedopix #med #bancocentral #portrasdodinheiro"""
tags = ["golpe do pix", "pix", "med pix", "mecanismo especial de devolução", "med 2.0", "devolução pix", "contestar pix",
        "golpe da falsa central", "conta laranja", "banco central", "fraude pix", "golpes", "educacao financeira", "por tras do dinheiro"]
SH_TITLE = "Caiu no golpe do Pix? Por que 9 em 10 pedidos de devolução são negados #shorts"
RK_TITLE = "Os 5 países que mais usam pagamento instantâneo (o Brasil não é o nº 1) #shorts"
EP07 = "Como o Pix mudou os bancos (e quem perdeu dinheiro)"
data = {"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": sys.argv[3], "items": [
  {"key": "ptd-rank17-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE,
   "description": "Os 5 países com mais transações de pagamento instantâneo em 2023: 5) Coreia do Sul, 9,1 bilhões; 4) China, 17,2 bilhões; 3) Tailândia, 20,4 bilhões; 2) Brasil, 37,4 bilhões (o Pix, com crescimento de 77,9% no ano); 1) Índia, 129,3 bilhões (49% do total mundial de 266,2 bilhões). \"Mais de 100 milhões por dia\" no Brasil = cálculo do canal. Fonte: ACI Worldwide, Prime Time for Real-Time 2024 (dados de 2023). Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #pix #pagamentos #fintech",
   "tags": ["pix", "pagamento instantâneo", "upi", "pagamentos", "fintech", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-20T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep07-long",
   "pinned_comment": "Você ainda usa dinheiro vivo ou já faz tudo no Pix? Vídeo completo: " + EP07},
  {"key": "ptd-ep17-long", "kind": "long", "video": "video.mp4", "title": LONG_TITLE, "description": desc, "tags": tags,
   "thumbnail": "thumbnail.jpg", "captions": "legendas.srt", "publish_at": "2026-11-20T18:00:00-03:00", "if_late": "public_now",
   "made_for_kids": False, "altered_content": True,
   "pinned_comment": "Na sua opinião, quando alguém é enganado e faz o Pix para um golpista, o banco deveria dividir o prejuízo? Conta aqui."},
  {"key": "ptd-ep17-short", "kind": "short", "video": "vertical.mp4", "title": SH_TITLE,
   "description": "De cada R$ 100 notificados em golpes no Pix desde 2022, só R$ 8,90 voltaram. O principal motivo: quando o pedido chega, a conta do golpista já está vazia (Banco Central, dados de jan/2022 a abr/2026, via O POVO). Vídeo completo no canal: \"" + LONG_TITLE + "\". Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #pix #golpedopix #med",
   "tags": ["golpe do pix", "med pix", "devolução pix", "pix", "shorts", "por tras do dinheiro"],
   "publish_at": "2026-11-20T19:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
   "related_key": "ptd-ep17-long",
   "pinned_comment": "Você ou alguém que você conhece já tentou pedir um Pix de volta? Conseguiu? Vídeo completo: " + LONG_TITLE},
]}
for it in data["items"]:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump(data, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(chap); print("total", round(sum(durs)), "s", len(desc))
