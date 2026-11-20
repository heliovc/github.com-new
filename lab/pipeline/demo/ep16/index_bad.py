import pandas as pd

df = pd.read_csv("orders_clean.csv")
df.head(3).to_excel("test.xlsx")
print(pd.read_excel("test.xlsx").columns.tolist())
