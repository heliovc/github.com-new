from pathlib import Path
import pandas as pd

files = sorted(Path("reports").glob("*.xlsx"))
print("Files found:", len(files))

frames = []
for f in files:
    df = pd.read_excel(f)
    df["Source"] = f.name
    frames.append(df)

merged = pd.concat(frames, ignore_index=True)
print("Rows:", len(merged))
merged.to_excel("all_sales.xlsx", index=False)
print("Saved all_sales.xlsx")
