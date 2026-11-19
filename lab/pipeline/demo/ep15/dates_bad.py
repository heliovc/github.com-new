import pandas as pd

df = pd.read_csv("orders.csv")
df["Date"] = pd.to_datetime(df["Date"])
