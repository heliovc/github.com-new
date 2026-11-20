import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
print(df.shape)
print(df.head(4))
