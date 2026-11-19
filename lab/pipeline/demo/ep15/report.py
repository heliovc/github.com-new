import pandas as pd

for name in ["orders.csv", "orders_clean.csv"]:
    df = pd.read_csv(name)
    if name == "orders.csv":
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["Revenue"] = df["Qty"] * df["Price"]
    by_city = df.groupby("City")["Revenue"].sum()
    print(name, "->", len(by_city), "cities, total", round(by_city.sum(), 2))
