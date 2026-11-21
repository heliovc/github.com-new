# Gera rank18/publish.json (sábado 21/11/2026: dia sem longo, só o ranking).
import json, sys, os
out = sys.argv[1] if len(sys.argv) > 1 else "rank18"
RK_TITLE = "Os 5 bancos com mais reclamações no Banco Central (o nº 1 é um gigante) #shorts"
desc = ("O ranking de reclamações do Banco Central mede reclamações procedentes (em que o BC deu razão ao cliente) por milhão de clientes. "
        "No 3º trimestre de 2026, entre bancos e financeiras com mais de 4 milhões de clientes: 5) PicPay, 35,51; 4) BTG Pactual/Banco Pan, 40,60; "
        "3) Itaú, 43,20 (4.252 procedentes); 2) C6, 52,31 (1.893); 1) Bradesco, 57,23 (6.333), que no trimestre anterior tinha 84,90. "
        "Fonte: Banco Central do Brasil, Ranking de Instituições por Índice de Reclamações, 3º trimestre de 2026 (divulgado em 22/10/2026), via imprensa. "
        "Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #bancos #bancocentral #reclamacao")
items = [{"key": "ptd-rank18-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE, "description": desc,
  "tags": ["ranking de reclamações", "banco central", "bradesco", "c6 bank", "itau", "picpay", "bancos", "shorts", "por tras do dinheiro"],
  "publish_at": "2026-11-21T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
  "related_key": "ptd-ep17-long",
  "pinned_comment": "Você já precisou reclamar do seu banco no Banco Central? Resolveu? Vídeo completo: Golpe do Pix: para onde vai o seu dinheiro em segundos (e quem tem que devolver)"}]
for it in items:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump({"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": "2026-11-21T07:10:00-03:00", "items": items},
          open(os.path.join(out, "publish.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
