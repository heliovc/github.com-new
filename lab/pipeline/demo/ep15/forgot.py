import pandas as pd

df = pd.read_csv("orders.csv")
df["City"].str.strip().str.title()
print("Cities:", df["City"].nunique())

df["City"] = df["City"].str.strip().str.title()
print("Cities:", df["City"].nunique())
print(df["City"].value_counts())
