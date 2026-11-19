import pandas as pd

df = pd.read_csv("orders.csv")
df["Status"] = df["Status"].str.strip().str.lower()
print(df["Status"].value_counts())
