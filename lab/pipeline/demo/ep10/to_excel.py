import pdfplumber
import pandas as pd

with pdfplumber.open("report.pdf") as pdf:
    table = pdf.pages[0].extract_table()

df = pd.DataFrame(table[1:], columns=table[0])
print(df)
df.to_excel("sales.xlsx", index=False)
df.to_csv("sales.csv", index=False)
print("Saved sales.xlsx and sales.csv")
