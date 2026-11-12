# EP08: every QUERY result shown in the video is computed here by running the equivalent SQL in a real engine (sqlite3),
# following Google's documented QUERY semantics (support.google.com/docs/answer/3093343 + Google Visualization API Query
# Language reference): headers=1 -> first row is the header; group by sorts by the group keys; aggregate headers are
# "<fn> <header>" (e.g. "sum Amount") unless relabeled with label; pivot makes one column per distinct value, sorted.
# Also writes ep08_sample.csv (File > Import it into Google Sheets to try every formula).
import json, sqlite3, csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [("2026-10-20", "Maya", "East", "Laptop", 1150), ("2026-10-22", "Omar", "West", "Monitor", 280),
        ("2026-10-25", "Lena", "North", "Laptop", 1290), ("2026-10-27", "Maya", "West", "Mouse", 35),
        ("2026-10-30", "Jon", "South", "Keyboard", 85), ("2026-11-02", "Omar", "West", "Laptop", 1210),
        ("2026-11-03", "Lena", "North", "Monitor", 310), ("2026-11-05", "Jon", "South", "Laptop", 1080),
        ("2026-11-06", "Maya", "East", "Keyboard", 95), ("2026-11-09", "Omar", "East", "Mouse", 40),
        ("2026-11-10", "Lena", "South", "Keyboard", 70), ("2026-11-11", "Jon", "North", "Monitor", 295)]
HDR = ["Date", "Rep", "Region", "Product", "Amount"]
db = sqlite3.connect(":memory:"); db.execute("create table t (A date, B text, C text, D text, E integer)")
db.executemany("insert into t values (?,?,?,?,?)", rows)
def q(sql, header):
    return [header] + [list(r) for r in db.execute(sql).fetchall()]
R = {"rows": rows, "hdr": HDR, "queries": {}}
def add(name, query, sql, header):
    R[name] = q(sql, header); R["queries"][name] = query
add("select", "select B, D, E", "select B, D, E from t", ["Rep", "Product", "Amount"])
add("west", "select B, D, E where C = 'West'", "select B, D, E from t where C = 'West'", ["Rep", "Product", "Amount"])
add("big", "select B, D, E where E > 500", "select B, D, E from t where E > 500", ["Rep", "Product", "Amount"])
add("east100", "select B, D, E where C = 'East' and E >= 90", "select B, D, E from t where C = 'East' and E >= 90", ["Rep", "Product", "Amount"])
add("mon_or", "select B, D, E where D = 'Mouse' or D = 'Monitor'", "select B, D, E from t where D = 'Mouse' or D = 'Monitor'", ["Rep", "Product", "Amount"])
add("contains", "select B, D, E where D contains 'top'", "select B, D, E from t where instr(D, 'top') > 0", ["Rep", "Product", "Amount"])
add("top3", "select B, D, E order by E desc limit 3", "select B, D, E from t order by E desc limit 3", ["Rep", "Product", "Amount"])
add("byregion", "select C, sum(E) group by C", "select C, sum(E) from t group by C order by C", ["Region", "sum Amount"])
add("countmax", "select B, count(E), max(E) group by B", "select B, count(E), max(E) from t group by B order by B", ["Rep", "count Amount", "max Amount"])
add("report", "select B, sum(E) group by B order by sum(E) desc label sum(E) 'Total'", "select B, sum(E) from t group by B order by sum(E) desc", ["Rep", "Total"])
regs = [r[0] for r in db.execute("select distinct C from t order by C")]
piv = [["Rep"] + regs]
for (rep,) in db.execute("select distinct B from t order by B").fetchall():
    piv.append([rep] + [db.execute("select sum(E) from t where B=? and C=?", (rep, g)).fetchone()[0] or "" for g in regs])
R["pivot"] = piv; R["queries"]["pivot"] = "select B, sum(E) group by B pivot C"
add("nov", "select B, D, E where A >= date '2026-11-01'", "select B, D, E from t where A >= '2026-11-01'", ["Rep", "Product", "Amount"])
add("lena", "select D, E where B = 'Lena'", "select D, E from t where B = 'Lena'", ["Product", "Amount"])
# funnel: select B, sum(E) where E > 100 group by B order by sum(E) desc limit 2
f_where = [list(r) for r in db.execute("select B, E from t where E > 100")]
f_group = [list(r) for r in db.execute("select B, sum(E) from t where E > 100 group by B order by B")]
f_order = [list(r) for r in db.execute("select B, sum(E) from t where E > 100 group by B order by sum(E) desc")]
R["funnel"] = {"all": [[r[1], r[4]] for r in rows], "where": f_where, "group": f_group, "order": f_order, "limit": f_order[:2]}
R["total"] = sum(r[4] for r in rows)
json.dump(R, open(os.path.join(HERE, "ep08_results.json"), "w"), indent=1)
with open(os.path.join(HERE, "ep08_sample.csv"), "w", newline="") as fh: w = csv.writer(fh); w.writerow(HDR); w.writerows(rows)
for k, v in R.items():
    if k not in ("rows", "queries", "hdr"): print(k, v)
