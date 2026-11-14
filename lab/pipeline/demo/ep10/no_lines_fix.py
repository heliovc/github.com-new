import pdfplumber

settings = {"vertical_strategy": "text", "horizontal_strategy": "text"}

with pdfplumber.open("report.pdf") as pdf:
    page = pdf.pages[1]
    table = page.extract_table(settings)

table = [row for row in table if any(row)]
for row in table:
    print(row)
