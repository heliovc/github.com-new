import pandas as pd

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
print(df.head(4))
print(df.dtypes)
