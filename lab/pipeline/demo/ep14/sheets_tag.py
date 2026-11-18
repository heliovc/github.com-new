import pandas as pd

sheets = pd.read_excel("online_2026.xlsx", sheet_name=None)
online = pd.concat(sheets, names=["Sheet", "Row"]).reset_index()
print(online.head(3))
