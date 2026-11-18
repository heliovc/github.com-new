# Builds the practice workbooks for EP14 (fictional coffee chain, random but seeded data). Run: python3 make_files.py <project dir>
# 20 stores x 12 months = 240 files in reports/; one file (store 07, September) was typed by someone who called the column "Qty".
import sys, random, calendar
from pathlib import Path
import pandas as pd

root = Path(sys.argv[1] if len(sys.argv) > 1 else "project"); rep = root / "reports"; rep.mkdir(parents=True, exist_ok=True)
random.seed(14)
MENU = {"Espresso": 2.50, "Latte": 3.80, "Cappuccino": 3.60, "Tea": 2.20, "Muffin": 2.90, "Bagel": 2.40}
for store in range(1, 21):
    for month in range(1, 13):
        n = random.randint(18, 30); days = calendar.monthrange(2026, month)[1]; rows = []
        for _ in range(n):
            p = random.choice(list(MENU))
            rows.append({"Date": pd.Timestamp(2026, month, random.randint(1, days)), "Product": p, "Units": random.randint(1, 12), "Price": MENU[p]})
        df = pd.DataFrame(rows).sort_values("Date", kind="stable").reset_index(drop=True)
        if store == 7 and month == 9: df = df.rename(columns={"Units": "Qty"})
        df.to_excel(rep / f"2026-{month:02d}_store{store:02d}.xlsx", sheet_name="Sales", index=False)
# a workbook with one sheet per quarter (for the "many sheets" bonus)
with pd.ExcelWriter(root / "online_2026.xlsx") as w:
    for q in range(1, 5):
        rows = [{"Date": pd.Timestamp(2026, 3 * q - 2 + k % 3, 1 + k), "Product": random.choice(list(MENU)), "Units": random.randint(5, 40)} for k in range(6)]
        pd.DataFrame(rows).to_excel(w, sheet_name=f"Q{q}", index=False)
print("ok", len(list(rep.glob("*.xlsx"))), "files")
