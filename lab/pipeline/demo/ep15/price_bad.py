import pandas as pd

df = pd.read_csv("orders.csv")
df["Price"] = pd.to_numeric(df["Price"])
