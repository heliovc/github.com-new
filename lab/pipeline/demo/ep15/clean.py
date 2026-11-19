import pandas as pd

df = pd.read_csv("orders.csv")
print("Before:", df.shape)

# 1. Text: trim spaces, fix capitals
df["Customer"] = df["Customer"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["Status"] = df["Status"].str.strip().str.lower()
df["Status"] = df["Status"].replace({"shiped": "shipped"})

# 2. Duplicates
df = df.drop_duplicates()

# 3. Dates
df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# 4. Numbers stored as text
df["Price"] = df["Price"].str.replace("$", "").str.replace(",", "")
df["Price"] = pd.to_numeric(df["Price"])

# 5. Empty cells
df = df.dropna(subset=["Customer", "Qty"])
df["City"] = df["City"].fillna("Unknown")
df["Qty"] = df["Qty"].astype(int)

print("After:", df.shape)
print("Empty cells left:", df.isna().sum().sum())
df.to_csv("orders_clean.csv", index=False)
print("Saved orders_clean.csv")
