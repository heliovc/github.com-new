# Renders the real PDF pages to PNG (pdfplumber + pypdfium2) and saves the REAL boxes pdfplumber finds, as fractions of the page.
import json, pdfplumber
out = {}
def frac(b, p): return [b[0] / p.width, b[1] / p.height, b[2] / p.width, b[3] / p.height]
def lines_of(page):  # one box per text line (extract_text_lines)
    return [dict(text=l["text"], box=frac((l["x0"], l["top"], l["x1"], l["bottom"]), page)) for l in page.extract_text_lines()]
with pdfplumber.open("invoice_1042.pdf") as pdf:
    p = pdf.pages[0]; p.to_image(resolution=110).save("page_invoice.png")
    out["invoice"] = dict(lines=lines_of(p))
with pdfplumber.open("report.pdf") as pdf:
    p = pdf.pages[0]; p.to_image(resolution=110).save("page_report1.png")
    t = p.find_tables()[0]
    out["report1"] = dict(lines=lines_of(p), table=frac(t.bbox, p), rows=[frac(r.bbox, p) for r in t.rows])
    p = pdf.pages[1]; p.to_image(resolution=110).save("page_report2.png")
    out["report2"] = dict(lines=lines_of(p), tables_default=len(p.find_tables()))
with pdfplumber.open("scanned_receipt.pdf") as pdf:
    p = pdf.pages[0]; p.to_image(resolution=60).save("page_scanned.png")
    out["scanned"] = dict(lines=lines_of(p))
json.dump(out, open("boxes.json", "w"), indent=1)
print({k: len(v["lines"]) for k, v in out.items()}, out["report1"]["table"], out["report2"]["tables_default"])
