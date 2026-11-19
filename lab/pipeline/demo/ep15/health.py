import pandas as pd

df = pd.read_csv("orders.csv")
print("Rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Cities:", df["City"].nunique())
print("Empty cells:")
print(df.isna().sum())
