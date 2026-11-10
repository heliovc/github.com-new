import pandas as pd

df = pd.read_excel("sales.xlsx")
df.plot(x="Month", y="coffee")
