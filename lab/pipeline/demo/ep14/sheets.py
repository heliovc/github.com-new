import pandas as pd

sheets = pd.read_excel("online_2026.xlsx", sheet_name=None)
print(list(sheets))

online = pd.concat(sheets.values(), ignore_index=True)
print(online.shape)
