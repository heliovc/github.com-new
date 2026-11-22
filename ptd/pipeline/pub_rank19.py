# Gera rank19/publish.json (domingo 22/11/2026: dia sem longo, só o ranking).
import json, sys, os
out = sys.argv[1] if len(sys.argv) > 1 else "rank19"
RK_TITLE = "As 5 dívidas mais comuns das famílias brasileiras (o nº 1 está em 85% delas) #shorts"
desc = ("Segundo a Pesquisa de Endividamento e Inadimplência do Consumidor (Peic) da CNC, 82% das famílias brasileiras tinham dívidas em julho de 2026 "
        "(contas a vencer, não só atrasadas), recorde da série. Entre as famílias endividadas, os tipos mais comuns: 5) financiamento de carro, 9%; "
        "4) financiamento de casa, 9,6%; 3) crédito pessoal, 13%; 2) carnês, 16,1%; 1) cartão de crédito, 85,3%. "
        "Uma família pode ter mais de um tipo de dívida, por isso a soma passa de 100%. "
        "Fonte: CNC, Peic de julho de 2026 (divulgada em 06/08/2026), via imprensa. "
        "Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #dividas #cartaodecredito #financaspessoais")
items = [{"key": "ptd-rank19-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE, "description": desc,
  "tags": ["endividamento", "dívidas", "cartão de crédito", "carnê", "crédito pessoal", "cnc", "peic", "finanças pessoais", "shorts", "por tras do dinheiro"],
  "publish_at": "2026-11-22T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
  "related_key": "ptd-ep10-long",
  "pinned_comment": "Qual dessas dívidas mais pesa aí na sua casa? Vídeo completo: Rotativo do cartão: o juro de 451% ao ano (e quem ganha com ele)"}]
for it in items:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump({"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": "2026-11-22T07:30:00-03:00", "items": items},
          open(os.path.join(out, "publish.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
