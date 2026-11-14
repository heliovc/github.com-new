# Shortcut Lab - EP10: Extract Text and Tables from PDFs with Python (pdfplumber + pandas)
# AUTHENTICITY: the practice PDFs are made by demo/ep10/make_pdfs.py (fictional shop, no real data). Every script on screen is in
# demo/ep10/ and was run for real (Python 3.11, pdfplumber 0.11.10, pandas 3.1.1); every terminal output is copied from
# demo/ep10/transcript.txt / err_module.txt. The PDF pages in the "pdfx" scenes are real renders (pdfplumber .to_image) and every
# highlighted box is a box pdfplumber really returned (demo/ep10/shoot_pages.py -> boxes.json).
import os, json
TITLE = "Extract Text and Tables from PDFs with Python"
SPEED = 0.82
ACCENT = (240, 80, 110)  # ruby (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle)
SKY, YEL, MINT, CORAL = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep10")
def src(n): return open(os.path.join(D, n)).read()
def png(n): return os.path.join(D, n)
B = json.load(open(os.path.join(D, "boxes.json")))
INV = [l["box"] for l in B["invoice"]["lines"]]; INV_T = [l["text"] for l in B["invoice"]["lines"]]
R1 = B["report1"]
TABLE = [["Region", "Units", "Revenue", "Growth"], ["North", "1,240", "18,600", "+12%"], ["South", "980", "14,700", "+8%"],
         ["East", "1,515", "22,725", "+15%"], ["West", "760", "11,400", "+3%"], ["Online", "2,310", "34,650", "+27%"]]
TOTAL_I = INV_T.index("Total: 351.80")

STEP1_OUT = ["$ python3 step1.py", "Pages: 1"] + INV_T
BATCH_OUT = ["$ python3 batch.py",
             "           file Invoice number        Date              Customer  Total",
             "0  INV-1040.pdf       INV-1040  2026-10-01          Lopez Bakery  121.0",
             "1  INV-1041.pdf       INV-1041  2026-10-02       Green Leaf Cafe   84.0",
             "2  INV-1042.pdf       INV-1042  2026-10-03  Bright Dental Clinic  351.8",
             "3  INV-1043.pdf       INV-1043  2026-10-06        Oak Street Gym  288.0",
             "4  INV-1044.pdf       INV-1044  2026-10-07          Lopez Bakery   60.0",
             "Grand total: 904.8"]

SCENES = [
dict(chapter="The result", say="This is a PDF invoice. And in about one second, Python just read every line of it, and pulled out the total. No copying, no retyping, no squinting at the screen. Now imagine doing that for a hundred invoices at once. That's what you'll build today.",
     vis=dict(type="pdfx", page=png("page_invoice.png"), boxes=INV, out=INV_T, pick=(TOTAL_I,), outwin="python3 step1.py", span=0.4, note="Every line of the PDF, read by Python")),
dict(say="In the next ten minutes, you'll learn to get the text out of any PDF, find one value inside it, pull a whole table straight into Excel, and then process a folder full of PDFs in one go. Step by step, no experience needed. And I'll show you the PDFs that refuse to give up their text, and what to do about them.",
     vis=dict(type="title", kicker="Python for beginners", text="Extract Text and Tables from PDFs", sub="pdfplumber reads the PDF  ·  pandas saves it to Excel")),
dict(chapter="The plan", say="Here's the plan. Install one free library. Read all the text from a PDF. Find the one value you need. Extract a table, and save it as an Excel file. Then, the big one. Loop through a whole folder of invoices, and build a summary spreadsheet automatically.",
     vis=dict(type="steps", title="The plan", items=["Install pdfplumber", "Read all the text from a PDF", "Find one value (the total)", "Extract a table into Excel", "A whole folder of PDFs in one go"])),
dict(chapter="Why copy and paste fails", say="Why not just copy and paste? Try it with a table, and the columns fall apart. Everything lands in one cell, or the numbers jump to the wrong rows. And with fifty PDFs, it takes an afternoon. Python reads the PDF the way the computer stores it, so the rows and columns come out clean, and fifty files take the same effort as one.",
     vis=dict(type="compare", title="Copy and paste vs. Python", left=("Copy and paste", ["Table columns fall apart", "One file at a time", "Easy to miss a number"]),
              right=("A Python script", ["Clean rows and columns", "50 files in seconds", "Same result every time"]))),
dict(chapter="Install pdfplumber", say="You need Python installed. If you don't have it yet, it's free from python dot org. Open a terminal and type pip install pdfplumber pandas openpyxl. Pdfplumber reads PDFs. Pandas organizes tables. And openpyxl lets pandas write Excel files. Then check it with this one line. If it prints two version numbers, you're ready.",
     vis=dict(type="term", lines=["$ pip install pdfplumber pandas openpyxl", "", "$ python3 -c \"import pdfplumber, pandas; print(pdfplumber.__version__, pandas.__version__)\"", "0.11.10 3.1.1"])),
dict(chapter="The practice files", say="Here are the practice files, all in one folder. An invoice, a two page sales report, a scanned receipt, and a folder called invoices, with five more. Your scripts go in this same folder. That's important, because Python looks for files in the folder you run it from.",
     vis=dict(type="files", title="The project folder", before=["invoice_1042.pdf", "report.pdf", "scanned_receipt.pdf", "invoices/  (5 PDFs)", "step1.py  (your script)"], hdr1="pdf-tools/")),
dict(chapter="Step 1: read the text", say="Step one. Create step one dot py. Import pdfplumber. Then, with pdfplumber dot open and the file name, you open the PDF. The with keyword closes the file for you when you're done. pdf dot pages is a list of the pages. Print its length, to see how many there are. Then take the first page. Remember, Python counts from zero, so the first page is pages, zero. And extract text gives you all its text as one string.",
     vis=dict(type="code", file="step1.py", code=src("step1.py"), hl=(3, 5, 6), note="pages[0] = the first page")),
dict(say="Run it. Pages, one. And there's the whole invoice, as plain text. The shop name, the invoice number, the date, the customer, every item with its quantity and price, and the total at the bottom. Line by line, in reading order.",
     vis=dict(type="term", lines=STEP1_OUT, out_gap=0.14)),
dict(say="Here's what's happening behind the scenes. A PDF stores every piece of text with its exact position on the page. Pdfplumber finds those pieces, groups the ones that sit on the same line, and reads them top to bottom. Each box you see here is a line it found. That's why the output keeps the same order as the page.",
     vis=dict(type="pdfx", page=png("page_invoice.png"), boxes=INV, out=INV_T, outwin="what pdfplumber sees", span=0.6, size=23)),
dict(chapter="Step 2: find one value", say="Step two. Usually you don't want all the text, just one value. Like the total. Text dot split lines turns the text into a list of lines. Loop over them. If a line starts with Total colon, split it at the colon. That gives two parts, the word Total, and the number. Take part one, the number, and strip removes the extra spaces around it.",
     vis=dict(type="code", file="find_total.py", code=src("find_total.py"), hl=(7, 8, 9))),
dict(say="Run it. Found the total, three hundred fifty one point eight zero. That's exactly the number on the invoice. The same idea works for any label. Invoice number, date, customer. If the PDF writes a label and then a value, you can grab it this way.",
     vis=dict(type="pdfx", page=png("page_invoice.png"), boxes=INV, out=["$ python3 find_total.py", "Found the total: 351.80"], pick=(TOTAL_I,), outwin="python3 find_total.py", span=0.35, note="Label, colon, value: easy to grab")),
dict(chapter="Every page", say="What about a PDF with many pages? Loop over pdf dot pages. Enumerate, with start equals one, gives you a page number that starts at one, like a human would count. Print a small header for each page, then its text.",
     vis=dict(type="code", file="all_pages.py", code=src("all_pages.py"), hl=(4, 5, 6))),
dict(say="Here's the sales report. Page one has an introduction, and a table of sales by region. Page two has a list of top products. All the text, from every page. But look at the tables. In plain text, they're just words separated by spaces. To get real rows and columns, we need the next step.",
     vis=dict(type="term", lines=["$ python3 all_pages.py"] + (lambda L: L[:3] + ["..."] + L[5:])(src("transcript.txt").split("### all_pages\n")[1].split("###")[0].strip("\n").split("\n")), out_gap=0.1)),
dict(chapter="Step 3: extract a table", say="Step three, tables. This is where pdfplumber really shines. Instead of extract text, call extract table on the page. It looks for the lines that draw the table, the grid, and uses them to split the text into rows and cells. You get back a list of rows. Each row is a list of cells.",
     vis=dict(type="code", file="table.py", code=src("table.py"), hl=(4,), note="extract_table() = a list of rows")),
dict(say="Watch it work on the real page. Pdfplumber finds the table, and reads it one row at a time. Region, units, revenue, growth. North, South, East, West, and Online. Every cell in the right column, exactly like the page.",
     vis=dict(type="pdfx", page=png("page_report1.png"), win="report.pdf  (page 1)", boxes=R1["rows"], out=TABLE, mode="table", outwin="table = page.extract_table()", span=0.6)),
dict(say="And here's the printed result. Six rows. The first row is the header, the column names. Notice the square brackets and quotes. Each row is a Python list, and each cell is text, even the numbers. Keep that in mind, we'll come back to it.",
     vis=dict(type="term", lines=["$ python3 table.py"] + src("transcript.txt").split("### table\n")[1].split("###")[0].strip("\n").split("\n"))),
dict(chapter="Step 4: save it to Excel", say="Step four. Let's put it in Excel. Import pandas as p d. Then build a data frame, that's pandas' word for a table. The data is table, from one onward, that's every row except the header. And columns equals table, zero, the header row. Then to excel saves an Excel file, and index equals false skips the row numbers. To csv does the same for a CSV file.",
     vis=dict(type="code", file="to_excel.py", code=src("to_excel.py"), hl=(7, 9, 10), cps=44)),
dict(say="Run it. There's the table, now with proper columns. And two new files in the folder, sales dot x l s x and sales dot c s v. Open the Excel file, and every value sits in its own cell. No copy and paste, no columns falling apart.",
     vis=dict(type="term", lines=["$ python3 to_excel.py"] + src("transcript.txt").split("### to_excel\n")[1].split("###")[0].strip("\n").split("\n") + ["", "$ ls sales.*", "sales.csv  sales.xlsx"])),
dict(chapter="Step 5: a whole folder of invoices", say="Now the real shortcut. A folder of invoices, and one summary spreadsheet. Path, invoices, dot glob, star dot p d f, finds every PDF in the folder. For each one, read the text of the first page. Then check every line against four labels. Invoice number, date, customer and total. When a line starts with a label, keep the value. Split with a one means split only at the first colon. Each invoice becomes one row.",
     vis=dict(type="code", file="batch.py", code=src("batch.py"), hl=(6, 10, 11, 12, 13), lh=36, size=24, cps=52)),
dict(say="Then pandas turns all the rows into one table. As type float turns the totals from text into real numbers, so we can add them. Remember, cells come out as text. And sum gives the grand total. Run it. Five invoices, one clean table, and a grand total of nine hundred four point eight. Saved as an Excel file. With five hundred invoices, it's the same command.",
     vis=dict(type="term", lines=BATCH_OUT, out_gap=0.2)),
dict(say="That's the moment it pays off. The boring job, opening each PDF, finding the number, typing it into a spreadsheet, is now one command. Run it again next month, on next month's folder, and the summary builds itself.",
     vis=dict(type="tip", tag="THE SHORTCUT", text="Drop new PDFs in the folder, run python3 batch.py, open invoices_summary.xlsx. Done.", color=ACCENT)),
dict(chapter="When there's no grid", say="Now, the PDFs that fight back. Problem one. Page two of the report has a table with no lines, just columns lined up with spaces. Run extract table, and you get None. Nothing. By default, pdfplumber looks for drawn lines, and there aren't any.",
     vis=dict(type="pdfx", page=png("page_report2.png"), win="report.pdf  (page 2)", boxes=[], out=[], outwin="page.extract_table()", span=0.5, empty="None", empty_sub="No drawn lines, so no table found")),
dict(say="The fix is one setting. Tell it to use the text itself, instead of lines. Vertical strategy, text, and horizontal strategy, text. Now it splits columns at the gaps between words. It also returns some empty rows from the spacing, so this one line keeps only the rows that have something in them.",
     vis=dict(type="code", file="no_lines_fix.py", code=src("no_lines_fix.py"), hl=(3, 7, 9))),
dict(say="And there it is. Product, units, revenue, and four products, each in its own column. The title, Top Products, came along as the first row. Just skip it, with table, from one onward, like before.",
     vis=dict(type="term", lines=["$ python3 no_lines_fix.py"] + src("transcript.txt").split("### no_lines_fix\n")[1].split("###")[0].strip("\n").split("\n"))),
dict(chapter="Scanned PDFs", say="Problem two, scanned PDFs. This receipt was photographed, or scanned. Run extract text, and you get two empty quotes. An empty string. Because there is no text inside, just one picture of text. Pdfplumber confirms it, there's one image on the page. To read a scan, you need O C R, optical character recognition, which is a different tool, and a topic for its own video.",
     vis=dict(type="pdfx", page=png("page_scanned.png"), win="scanned_receipt.pdf", boxes=[], out=[], outwin="page.extract_text()", span=0.5, empty="''", empty_sub="Images on the page: 1  (no text layer)", notecol=CORAL, note="Can you select the text in your PDF viewer? No? It's a scan.")),
dict(chapter="Common errors", say="Two more errors you'll probably meet. Error one. Module not found, no module named pdfplumber. The library isn't installed for the Python you're running. Run pip install pdfplumber again. If you have several Pythons, use python three dash m pip install, so it goes to the same Python you run your script with.",
     vis=dict(type="term", lines=["$ python3 step1.py"] + src("err_module.txt").strip("\n").split("\n")[:1] + ["  ..."] + src("err_module.txt").strip("\n").split("\n")[-1:] + ["", "$ python3 -m pip install pdfplumber"])),
dict(say="Error two. File not found. Look closely at the name. I typed invoice dash ten forty two, but the file is invoice underscore ten forty two. The name must match exactly. And the terminal must be in the same folder as the PDF. Use c d to get there first.",
     vis=dict(type="term", lines=["$ python3 typo.py", "Traceback (most recent call last):", "  ...", "FileNotFoundError: [Errno 2] No such file or directory: 'invoice-1042.pdf'", "", "# the file is invoice_1042.pdf (underscore, not dash)"])),
dict(chapter="Pro tip: the pdfplumber cheat sheet", say="Pro tip. Keep these five lines handy. Extract text for all the text. Extract table for one table, and extract tables, with an s, for every table on the page. Crop, with a box, reads only part of the page, like just the header. And extract words gives you every word with its exact position, for the tricky layouts.",
     vis=dict(type="cards", title="PRO TIP: the pdfplumber cheat sheet", cols=2, span=0.6, colors=[ACCENT, SKY, YEL, MINT, CORAL, (190, 150, 255)],
              items=[["page.extract_text()", "All the text, in reading order"], ["page.extract_table()", "The table on the page, as rows"], ["page.extract_tables()", "Every table on the page"],
                     ["page.crop((x0, top, x1, bottom))", "Read only one area of the page"], ["page.extract_words()", "Every word with its position"], ["len(page.images)", "Images on the page (scan check)"]])),
dict(chapter="Recap", say="Quick recap. Install pdfplumber. Open the file with pdfplumber dot open. Extract text for the text, and split lines to find a value. Extract table for tables, and pandas to save them to Excel. Loop over a folder for the big jobs. And if a table has no lines, use the text strategy.",
     vis=dict(type="steps", title="Recap", items=["pip install pdfplumber pandas openpyxl", "with pdfplumber.open(\"file.pdf\") as pdf:", "extract_text() + splitlines() to find values", "extract_table() + pandas to_excel()", "Loop a folder; no grid? use the text strategy"])),
dict(say="Next on Shortcut Lab, regex for beginners. One small pattern that finds every email, phone number or date in any text, including the text you just pulled out of your PDFs. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Regex for Beginners: Find Anything in Text")),
]
