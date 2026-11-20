import pandas as pd

df = pd.read_csv("orders_clean.csv")
df["Month"] = df["Date"].dt.strftime("%Y-%m")
