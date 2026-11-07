# EP03: computes every formula result shown in the video from the sample table, with pandas,
# following Microsoft's documented semantics (XLOOKUP exact match, FILTER include array, UNIQUE in order
# of appearance, SORT by column index, SUMIFS, IFS first-TRUE-wins, TEXTSPLIT returns text).
# Also writes ep03_sample.xlsx with the real formulas (open it in Excel 365/2021/2024 to check).
import json, pandas as pd

rows = [(1001, "Ana", "East", "Laptop", 1200), (1002, "Ben", "West", "Mouse", 25), (1003, "Cara", "North", "Monitor", 300),
        (1004, "Ana", "East", "Keyboard", 80), (1005, "Dev", "West", "Laptop", 1150), (1006, "Ben", "West", "Monitor", 320),
        (1007, "Cara", "North", "Laptop", 1250), (1008, "Eli", "South", "Mouse", 30), (1009, "Dev", "West", "Keyboard", 75),
        (1010, "Ana", "East", "Monitor", 310), (1011, "Eli", "South", "Laptop", 1100), (1012, "Ben", "West", "Keyboard", 90)]
df = pd.DataFrame(rows, columns=["Order", "Rep", "Region", "Product", "Amount"])
R = {}

def xlookup(v, look, ret, nf=None):
    m = df[df[look] == v]
    return m.iloc[0][ret].tolist() if len(m) else nf
R["xlookup_1007"] = xlookup(1007, "Order", ["Amount"])
R["xlookup_1099"] = xlookup(1099, "Order", ["Amount"], ["Not found"])
R["xlookup_multi"] = xlookup(1007, "Order", ["Rep", "Region", "Product", "Amount"])
R["filter_west"] = df[df.Region == "West"].values.tolist()
R["filter_west_100"] = df[(df.Region == "West") & (df.Amount > 100)].values.tolist()
R["filter_central"] = df[df.Region == "Central"].values.tolist() or "No orders"
R["unique_rep"] = list(dict.fromkeys(df.Rep))
R["unique_region"] = list(dict.fromkeys(df.Region))
R["sort_amount_desc"] = df.sort_values("Amount", ascending=False, kind="stable").values.tolist()
R["sort_unique_region"] = sorted(dict.fromkeys(df.Region))
R["sumifs_ana"] = int(df[df.Rep == "Ana"].Amount.sum())
R["sumifs_west_laptop"] = int(df[(df.Region == "West") & (df.Product == "Laptop")].Amount.sum())
R["report"] = [[r, int(df[df.Rep == r].Amount.sum())] for r in dict.fromkeys(df.Rep)]
R["total"] = int(df.Amount.sum())

def ifs(a):  # =IFS(E2>=1000,"Large",E2>=100,"Medium",TRUE,"Small")
    return "Large" if a >= 1000 else "Medium" if a >= 100 else "Small"
def ifs_wrong(a):  # =IFS(E2>=100,"Medium",E2>=1000,"Large",TRUE,"Small")
    return "Medium" if a >= 100 else "Large" if a >= 1000 else "Small"
R["ifs"] = [ifs(a) for a in df.Amount]
R["ifs_wrong"] = [ifs_wrong(a) for a in df.Amount]
names = ["Ana Lopez", "Ben Carter", "Cara Singh", "Dev Patel", "Eli Moreau"]
R["textsplit_names"] = [n.split(" ") for n in names]
R["textsplit_rows"] = "Laptop;Mouse;Monitor;Keyboard".split(";")
R = json.loads(json.dumps(R, default=int))
json.dump(R, open("ep03_results.json", "w"), indent=1)

# workbook with the real formulas
from openpyxl import Workbook
wb = Workbook(); ws = wb.active; ws.title = "Orders"
ws.append(list(df.columns))
for r in rows: ws.append(list(r))
ws["G1"], ws["H1"] = "Lookup", 1007
ws["H2"] = '=XLOOKUP(H1,A2:A13,E2:E13,"Not found")'
ws["G4"], ws["H4"] = "Report", "=UNIQUE(B2:B13)"
ws["I4"] = "=SUMIFS(E2:E13,B2:B13,H4#)"
for i in range(2, 14): ws[f"F{i}"] = f'=IFS(E{i}>=1000,"Large",E{i}>=100,"Medium",TRUE,"Small")'
wb.save("ep03_sample.xlsx"); print("xlsx ok")
