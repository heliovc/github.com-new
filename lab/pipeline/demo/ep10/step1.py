import pdfplumber

with pdfplumber.open("invoice_1042.pdf") as pdf:
    print("Pages:", len(pdf.pages))
    page = pdf.pages[0]
    text = page.extract_text()
    print(text)
