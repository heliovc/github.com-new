import pdfplumber

with pdfplumber.open("invoice_1042.pdf") as pdf:
    text = pdf.pages[0].extract_text()

for line in text.splitlines():
    if line.startswith("Total:"):
        total = line.split(":")[1].strip()
        print("Found the total:", total)
