# Exports the REAL workbooks (report_v1.xlsx = before formatting, report.xlsx = final) and the real groupby stream for the EP16 scenes.
# Usage: python3 export_xlsx.py <project dir> <out json>
import sys, json
from pathlib import Path
from openpyxl import load_workbook
import pandas as pd

P = Path(sys.argv[1]); out = {}
def fmt(v, nf):
    if v is None: return ""
    if hasattr(v, "strftime"): return v.strftime("%Y-%m-%d %H:%M:%S") if nf == "General" or "h" in nf.lower() else v.strftime("%Y-%m-%d")
    if isinstance(v, float) and nf == "#,##0.00": return f"{v:,.2f}"
    if isinstance(v, int) and nf == "#,##0.00": return f"{v:,.2f}"
    if isinstance(v, float): return f"{v:.10g}"
    return str(v)
for name in ["report_v1.xlsx", "report.xlsx"]:
    wb = load_workbook(P / name); books = {}
    for ws in wb.worksheets:
        rows = []
        for r in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 16), max_col=min(ws.max_column, 9)):
            row = []
            for c in r:
                f = c.font; fill = c.fill.fgColor.rgb if c.fill and c.fill.fill_type == "solid" else None
                val = c.value; formula = None
                if isinstance(val, str) and val.startswith("="):
                    formula = val; rng = val[5:-1].split(":"); a, b = int(rng[0][1:]), int(rng[1][1:])
                    val = sum(ws.cell(row=i, column=c.column).value for i in range(a, b + 1))  # what Excel shows after it calculates
                row.append(dict(v=fmt(val, c.number_format), num=isinstance(val, (int, float)) or hasattr(val, "strftime"), b=bool(f.bold), fc=(f.color.rgb if f.color is not None and isinstance(f.color.rgb, str) else None),
                                fill=fill if isinstance(fill, str) else None, formula=formula, nf=c.number_format))
            rows.append(row)
        widths = {k: v.width for k, v in ws.column_dimensions.items() if v.width}
        books[ws.title] = dict(rows=rows, max_row=ws.max_row, max_col=ws.max_column, widths=widths, freeze=ws.freeze_panes)
    out[name] = books
df = pd.read_csv(P / "orders_clean.csv", parse_dates=["Date"]); df = df[df["Status"] != "cancelled"]
df["Revenue"] = df["Qty"] * df["Price"]
out["stream"] = [[c, round(float(r), 2), o, p, int(q)] for c, r, o, p, q in zip(df["City"], df["Revenue"], df["OrderID"], df["Product"], df["Qty"])]
out["totals"] = {k: round(float(v), 2) for k, v in df.groupby("City")["Revenue"].sum().sort_values(ascending=False).items()}
json.dump(out, open(sys.argv[2], "w"))
print("rows in stream:", len(out["stream"]), out["totals"])
