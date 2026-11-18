# Reads the real practice workbooks and writes merge.json for the "merge" scenes (file names, real row counts, real first rows).
import sys, json
from pathlib import Path
import pandas as pd
rep = Path(sys.argv[1]) / "reports"; out = []
for f in sorted(rep.glob("*.xlsx")):
    if f.name.startswith("~$"): out.append({"name": f.name, "rows": 0, "flag": "lock"}); continue
    df = pd.read_excel(f); flag = "qty" if "Qty" in df.columns else ""
    df = df.rename(columns={"Qty": "Units"})
    out.append({"name": f.name, "rows": len(df), "flag": flag,
                "sample": [[r.Date.strftime("%Y-%m-%d"), r.Product, int(r.Units), float(r.Price)] for r in df.head(3).itertuples()]})
json.dump(out, open(Path(__file__).with_name("merge.json"), "w"))
print(len(out), sum(x["rows"] for x in out))
