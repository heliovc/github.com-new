import pandas as pd

df = pd.read_excel("sales.xlsx", sheet_name="Sheet1")
df.to_csv("sales.csv", index=False)
df2 = pd.read_csv("sales.csv")
print(df2.shape)
print(df2.columns)
