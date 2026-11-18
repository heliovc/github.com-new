import pandas as pd

merged = pd.read_excel("all_sales.xlsx")
print(merged.shape)
print(merged.columns.tolist())
print(merged.isna().sum())
