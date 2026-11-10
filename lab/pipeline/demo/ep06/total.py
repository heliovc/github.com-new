import pandas as pd

df = pd.read_excel("sales.xlsx")
df["Total"] = df[["Coffee", "Tea", "Cakes"]].sum(axis=1)
best = df.loc[df["Total"].idxmax()]
print(df.tail(3))
print("Best month:", best["Month"], best["Total"])
