import pandas as pd

df = pd.read_csv("orders.csv")
print("Duplicates before fixing text:", df.duplicated().sum())

for col in ["Customer", "City", "Status"]:
    df[col] = df[col].str.strip().str.title()
print("Duplicates after fixing text:", df.duplicated().sum())
