# Builds the messy practice file for EP15 (fictional online shop, seeded random data, no real people). Run: python3 make_messy.py <project dir>
# orders.csv: 1,000 order lines typed by different people -> extra spaces, mixed case, duplicates, dates in 3 formats,
# prices as text ("$1,299.00"), status typos and empty cells.
import sys, random, csv
from pathlib import Path
from datetime import date, timedelta

root = Path(sys.argv[1] if len(sys.argv) > 1 else "project"); root.mkdir(parents=True, exist_ok=True)
random.seed(15)
FIRST = ["Ava", "Liam", "Noah", "Mia", "Ethan", "Zoe", "Lucas", "Ivy", "Owen", "Nora", "Leo", "Ruby", "Max", "Ella", "Theo", "Lily"]
LAST = ["Stone", "Rivera", "Park", "Hayes", "Brooks", "Quinn", "Lane", "Frost", "Reed", "Wolfe"]
CITY = ["Austin", "Denver", "Boston", "Seattle", "Chicago", "Miami"]
PROD = {"Desk Lamp": 34.90, "Keyboard": 59.00, "Monitor": 1299.00, "Mouse": 19.50, "Webcam": 74.00, "Headset": 89.90}
STATUS = ["shipped", "pending", "cancelled"]

def messy_case(s):
    r = random.random()
    return s.upper() if r < 0.12 else s.lower() if r < 0.27 else s
def spaces(s):
    r = random.random()
    return "  " + s if r < 0.1 else s + "   " if r < 0.2 else s

rows = []
for i in range(1, 941):
    d = date(2026, 1, 1) + timedelta(days=random.randint(0, 303))
    p = random.choice(list(PROD)); price = PROD[p]
    fmt = random.random()
    ds = d.strftime("%m/%d/%Y") if fmt < 0.25 else d.strftime("%B %d, %Y") if fmt < 0.4 else d.isoformat()
    ps = f"${price:,.2f}" if random.random() < 0.3 else f"{price:.2f}"
    st = random.choices(STATUS, [70, 22, 8])[0]
    r = random.random()
    st = st.upper() if r < 0.1 else st.title() if r < 0.3 else ("shiped" if st == "shipped" and r < 0.36 else st)
    name = spaces(messy_case(random.choice(FIRST) + " " + random.choice(LAST)))
    city = spaces(messy_case(random.choice(CITY)))
    qty = str(random.randint(1, 5))
    if random.random() < 0.03: qty = ""
    if random.random() < 0.04: city = ""
    if random.random() < 0.015: name = ""
    rows.append([f"A{1000 + i}", ds, name, city, p, qty, ps, spaces(st)])
# 60 duplicates: same order pasted twice, about half of them with different spaces/case so they don't look identical
for k in random.sample(range(len(rows)), 60):
    dup = list(rows[k])
    if random.random() < 0.55: dup[2] = dup[2].strip().upper() + " "; dup[3] = dup[3].strip().lower()
    rows.insert(random.randint(k + 1, len(rows)), dup)
with open(root / "orders.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["OrderID", "Date", "Customer", "City", "Product", "Qty", "Price", "Status"]); w.writerows(rows)
print("ok", len(rows), "rows")
