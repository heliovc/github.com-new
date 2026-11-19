# Runs the EP15 cleaning steps one by one on the REAL practice file and writes clean.json for the "clean" scenes:
# per step: name, code, columns touched, cells really changed and rows really removed (whole file), and the values of a few
# display rows after every step (None = row removed). Usage: python3 export_clean.py <project dir>
import sys, json
from pathlib import Path
import pandas as pd
df = pd.read_csv(Path(sys.argv[1]) / "orders.csv")
COLS = ["OrderID", "Date", "Customer", "City", "Qty", "Price", "Status"]
def s1(d):
    d = d.copy()
    for c in ["Customer", "City"]: d[c] = d[c].str.strip().str.title()
    d["Status"] = d["Status"].str.strip().str.lower(); return d
def s2(d): d = d.copy(); d["Status"] = d["Status"].replace({"shiped": "shipped"}); return d
def s3(d): return d.drop_duplicates()
def s4(d): d = d.copy(); d["Date"] = pd.to_datetime(d["Date"], format="mixed"); return d
def s5(d): d = d.copy(); d["Price"] = pd.to_numeric(d["Price"].str.replace("$", "").str.replace(",", "")); return d
def s6(d):
    d = d.dropna(subset=["Customer", "Qty"]).copy(); d["City"] = d["City"].fillna("Unknown"); d["Qty"] = d["Qty"].astype(int); return d
STEPS = [("Trim spaces + fix capitals", ".str.strip().str.title()", ["Customer", "City", "Status"], s1),
         ("Fix typos", '.replace({"shiped": "shipped"})', ["Status"], s2),
         ("Remove duplicates", "df.drop_duplicates()", [], s3),
         ("Real dates", 'pd.to_datetime(..., format="mixed")', ["Date"], s4),
         ("Text to numbers", 'str.replace("$", "") + pd.to_numeric', ["Price"], s5),
         ("Empty cells", 'dropna(...) + fillna("Unknown")', ["City", "Qty"], s6)]
def show(v, col):
    if v is None or (not isinstance(v, str) and pd.isna(v)): return "NaN"
    if isinstance(v, pd.Timestamp): return v.strftime("%Y-%m-%d")
    if col == "Qty" and isinstance(v, float): return f"{v:.1f}"  # pandas shows a column with NaN as floats (3.0)
    return str(v)
# display rows: first rows + one example of each problem (all real rows of the file)
dup = df.duplicated(keep="first"); key = s1(df).duplicated(keep="first")
pick = list(range(5))
def first(mask, avoid): return next(i for i in df.index[mask] if i not in avoid)
pick.append(first(df["Status"].str.contains("shiped"), pick))
pick.append(first(df["Customer"].isna(), pick))
pick.append(first(df["Qty"].isna(), pick))
pick.append(first(df["City"].isna(), pick))
dk = next(i for i in df.index[key & ~dup] if i > 5)  # a duplicate that only shows up after the text fix
orig = next(j for j in df.index if j < dk and s1(df).loc[j].equals(s1(df).loc[dk]))
pick += [orig, dk]
pick = sorted(set(pick))
states, stats, cur = [df], [], df
for name, code, cols, fn in STEPS:
    nxt = fn(cur); common = nxt.index
    changed = 0
    for c in COLS + ["Product"]:
        if fn is s6 and c == "Qty": continue  # 3.0 -> 3 is only the type; count the cells really filled
        a, b = cur.loc[common, c].map(lambda x: show(x, c)), nxt.loc[common, c].map(lambda x: show(x, c))
        changed += int((a != b).sum())
    stats.append({"name": name, "code": code, "cols": cols, "changed": changed, "removed": int(len(cur) - len(nxt)), "rows": int(len(nxt))})
    states.append(nxt); cur = nxt
rows = [{"idx": int(i), "vals": [[show(st.loc[i, c], c) for c in COLS] if i in st.index else None for st in states]} for i in pick]
json.dump({"cols": COLS, "rows0": len(df), "steps": stats, "rows": rows}, open(Path(__file__).with_name("clean.json"), "w"), indent=1)
for s in stats: print(s)
print("display rows:", pick)
