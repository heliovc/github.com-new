import pandas as pd

df = pd.read_csv("books.csv")
print(df[["title", "price", "stars"]].head(3))
print()
deals = df[(df["stars"] >= 4) & df["in_stock"]].sort_values("price")
print(deals[["title", "price", "stars"]].head(5).to_string(index=False))
print()
print("Average price:", round(df["price"].mean(), 2))
