import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for number, page in enumerate(pdf.pages, start=1):
        print(f"--- page {number} ---")
        print(page.extract_text())
