# Builds the practice PDFs for EP10 (fictional shop "Maple & Co. Supplies"). Run once: python3 make_pdfs.py
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

W, H = A4
HERE = os.path.dirname(os.path.abspath(__file__))

def invoice(path, number, date, customer, items):
    c = canvas.Canvas(path, pagesize=A4)
    c.setFillColor(colors.HexColor("#1f6f5c")); c.rect(0, H - 90, W, 90, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 24); c.drawString(50, H - 55, "Maple & Co. Supplies")
    c.setFillColor(colors.black); c.setFont("Helvetica-Bold", 18); c.drawString(50, H - 140, "INVOICE")
    c.setFont("Helvetica", 12)
    c.drawString(50, H - 170, f"Invoice number: {number}")
    c.drawString(50, H - 188, f"Date: {date}")
    c.drawString(50, H - 206, f"Customer: {customer}")
    rows = [["Item", "Qty", "Price", "Amount"]]
    total = 0
    for name, q, p in items:
        rows.append([name, str(q), f"{p:.2f}", f"{q * p:.2f}"]); total += q * p
    t = Table(rows, colWidths=[250, 60, 80, 90])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, colors.grey), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dfeee9")),
                           ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"), ("ALIGN", (1, 0), (-1, -1), "RIGHT")]))
    tw, th = t.wrapOn(c, W, H); t.drawOn(c, 50, H - 240 - th)
    c.setFont("Helvetica-Bold", 14); c.drawString(50, H - 270 - th, f"Total: {total:.2f}")
    c.setFont("Helvetica", 10); c.setFillColor(colors.grey); c.drawString(50, 60, "Thank you for your order. Payment due in 30 days.")
    c.save()

def report(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica-Bold", 22); c.drawString(50, H - 70, "Quarterly Sales Report")
    c.setFont("Helvetica", 12); c.drawString(50, H - 95, "Maple & Co. Supplies  -  Q3")
    c.drawString(50, H - 125, "Sales grew in every region this quarter. The table below shows")
    c.drawString(50, H - 141, "units sold and revenue by region.")
    rows = [["Region", "Units", "Revenue", "Growth"], ["North", "1,240", "18,600", "+12%"], ["South", "980", "14,700", "+8%"],
            ["East", "1,515", "22,725", "+15%"], ["West", "760", "11,400", "+3%"], ["Online", "2,310", "34,650", "+27%"]]
    t = Table(rows, colWidths=[140, 90, 110, 90])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, colors.grey), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e1f5")),
                           ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"), ("ALIGN", (1, 0), (-1, -1), "RIGHT")]))
    tw, th = t.wrapOn(c, W, H); t.drawOn(c, 50, H - 170 - th)
    c.drawString(50, H - 200 - th, "Online is now the biggest channel.")
    c.showPage()
    # page 2: a table WITHOUT lines (only spacing) - the default extract_table() can't see it
    c.setFont("Helvetica-Bold", 18); c.drawString(50, H - 70, "Top Products")
    c.setFont("Helvetica-Bold", 12)
    xs = [50, 250, 350]
    for x, h in zip(xs, ["Product", "Units", "Revenue"]): c.drawString(x, H - 110, h)
    c.setFont("Helvetica", 12)
    for i, r in enumerate([["Notebook A5", "3,100", "9,300"], ["Gel pens (10)", "2,450", "12,250"], ["Desk lamp", "640", "19,200"], ["Sticky notes", "4,800", "7,200"]]):
        for x, v in zip(xs, r): c.drawString(x, H - 135 - i * 22, v)
    c.save()

def scanned(path):  # an image-only page, like a phone scan: there is no text layer at all
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (1240, 1754), (250, 248, 240)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    d.text((100, 120), "RECEIPT  #5521", font=f, fill=(40, 40, 40)); d.text((100, 200), "Total: 48.90", font=f, fill=(40, 40, 40))
    img = img.rotate(1.2, fillcolor=(250, 248, 240)); p = path.replace(".pdf", ".png"); img.save(p)
    c = canvas.Canvas(path, pagesize=A4); c.drawImage(p, 0, 0, W, H); c.save(); os.remove(p)

if __name__ == "__main__":
    os.chdir(HERE)
    invoice("invoice_1042.pdf", "INV-1042", "2026-10-03", "Bright Dental Clinic", [("Printer paper (box)", 4, 32.5), ("Toner cartridge", 2, 89.9), ("Desk organizer", 3, 14.0)])
    report("report.pdf")
    scanned("scanned_receipt.pdf")
    os.makedirs("invoices", exist_ok=True)
    data = [("INV-1040", "2026-10-01", "Lopez Bakery", [("Paper bags (500)", 2, 45.0), ("Labels", 5, 6.2)]),
            ("INV-1041", "2026-10-02", "Green Leaf Cafe", [("Napkins (case)", 3, 28.0)]),
            ("INV-1042", "2026-10-03", "Bright Dental Clinic", [("Printer paper (box)", 4, 32.5), ("Toner cartridge", 2, 89.9), ("Desk organizer", 3, 14.0)]),
            ("INV-1043", "2026-10-06", "Oak Street Gym", [("Water bottles", 24, 7.5), ("Towels", 12, 9.0)]),
            ("INV-1044", "2026-10-07", "Lopez Bakery", [("Paper bags (500)", 1, 45.0), ("Ribbon roll", 4, 3.75)])]
    for n, dt, cu, it in data: invoice(f"invoices/{n}.pdf", n, dt, cu, it)
    print("ok")
