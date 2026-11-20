import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
df["Revenue"] = df["Qty"] * df["Price"]
by_city = df.groupby("City")["Revenue"].sum().reset_index()

by_city.to_excel("report.xlsx", sheet_name="By city", index=False)
df.to_excel("report.xlsx", sheet_name="Data", index=False)

print(pd.ExcelFile("report.xlsx").sheet_names)
