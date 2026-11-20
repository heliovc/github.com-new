import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
df = df[df["Status"] != "cancelled"]
df["Revenue"] = df["Qty"] * df["Price"]
df["Month"] = df["Date"].dt.strftime("%Y-%m")

by_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False).reset_index()
by_month = df.pivot_table(index="Month", columns="City", values="Revenue",
                          aggfunc="sum", fill_value=0)

with pd.ExcelWriter("report.xlsx") as writer:
    by_city.to_excel(writer, sheet_name="By city", index=False)
    by_month.to_excel(writer, sheet_name="By month")
    df.to_excel(writer, sheet_name="Data", index=False)

print("Saved report.xlsx")
