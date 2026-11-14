import pdfplumber

with pdfplumber.open("invoice-1042.pdf") as pdf:
    print(pdf.pages[0].extract_text())
