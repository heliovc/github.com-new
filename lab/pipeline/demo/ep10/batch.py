from pathlib import Path
import pdfplumber
import pandas as pd

rows = []
for path in sorted(Path("invoices").glob("*.pdf")):
    with pdfplumber.open(path) as pdf:
        text = pdf.pages[0].extract_text()
    info = {"file": path.name}
    for line in text.splitlines():
        for label in ["Invoice number", "Date", "Customer", "Total"]:
            if line.startswith(label + ":"):
                info[label] = line.split(":", 1)[1].strip()
    rows.append(info)

df = pd.DataFrame(rows)
df["Total"] = df["Total"].astype(float)
print(df)
print("Grand total:", df["Total"].sum())
df.to_excel("invoices_summary.xlsx", index=False)
