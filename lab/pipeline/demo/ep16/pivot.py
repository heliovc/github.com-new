import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
df = df[df["Status"] != "cancelled"]
df["Revenue"] = df["Qty"] * df["Price"]
df["Month"] = df["Date"].dt.strftime("%Y-%m")

by_month = df.pivot_table(index="Month", columns="City", values="Revenue",
                          aggfunc="sum", fill_value=0)
print(by_month.round(0).astype(int))
