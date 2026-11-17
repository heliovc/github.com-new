# Gera rank14/publish.json (terça 17/11/2026: dia sem longo, só o ranking).
import json, sys, os
out = sys.argv[1] if len(sys.argv) > 1 else "rank14"
RK_TITLE = "Os 5 estados com mais empresas no vermelho (o nº 1 supera os outros 4 juntos) #shorts"
desc = ("O Brasil chegou a 9,4 milhões de empresas inadimplentes em setembro de 2026, recorde. Os 5 estados com mais CNPJs negativados: "
        "5) Rio Grande do Sul, 545.837; 4) Paraná, 621.879; 3) Rio de Janeiro, 889.525; 2) Minas Gerais, 946.410; 1) São Paulo, 3.205.708 "
        "(mais que os outros quatro somados). O número absoluto reflete o tamanho da economia de cada estado, não a taxa de inadimplência. "
        "Fonte: Serasa Experian, Indicador de Inadimplência das Empresas (setembro de 2026). "
        "Este vídeo é informativo e não é recomendação financeira. Voz sintética.\n#shorts #inadimplencia #empresas #serasa")
items = [{"key": "ptd-rank14-short", "kind": "short", "video": "ranking.mp4", "title": RK_TITLE, "description": desc,
  "tags": ["inadimplencia", "empresas inadimplentes", "serasa experian", "dividas", "economia", "shorts", "por tras do dinheiro"],
  "publish_at": "2026-11-17T12:00:00-03:00", "if_late": "public_now", "made_for_kids": False, "altered_content": True,
  "related_key": "ptd-ep15-long",
  "pinned_comment": "Por que você acha que tanta empresa está com conta atrasada agora? Vídeo completo: Score de crédito: a prova secreta que decide quanto juro você paga"}]
for it in items:
    assert len(it["title"]) <= 100 and len(it["description"]) <= 5000, it["key"]
    assert "<" not in it["title"] + it["description"] and ">" not in it["title"] + it["description"]
json.dump({"version": 1, "channel_id": "UCd_BGmJ5gbQ0kECAxmbvQHA", "created_at": "2026-11-17T07:40:00-03:00", "items": items},
          open(os.path.join(out, "publish.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
