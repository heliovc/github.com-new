import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    page = pdf.pages[1]
    print(page.extract_table())
