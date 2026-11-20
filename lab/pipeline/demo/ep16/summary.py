import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
df = df[df["Status"] != "cancelled"]
df["Revenue"] = df["Qty"] * df["Price"]
df["Month"] = df["Date"].dt.strftime("%Y-%m")

by_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print(by_city.round(2))
