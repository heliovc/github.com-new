import pandas as pd

merged = pd.read_excel("all_sales.xlsx")
merged["Revenue"] = merged["Units"] * merged["Price"]
merged["Store"] = merged["Source"].str[8:15]

by_store = merged.groupby("Store")["Revenue"].sum().round(2)
print(by_store.sort_values(ascending=False).head(5))

with pd.ExcelWriter("report.xlsx") as writer:
    merged.to_excel(writer, sheet_name="All rows", index=False)
    by_store.to_excel(writer, sheet_name="By store")
print("Saved report.xlsx")
