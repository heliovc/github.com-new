import pdfplumber

with pdfplumber.open("scanned_receipt.pdf") as pdf:
    page = pdf.pages[0]
    print(repr(page.extract_text()))
    print("Images on the page:", len(page.images))
