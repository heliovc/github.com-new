import pandas as pd

merged = pd.read_excel("all_sales.xlsx")
bad = merged[merged["Units"].isna()]
print(bad["Source"].value_counts())
