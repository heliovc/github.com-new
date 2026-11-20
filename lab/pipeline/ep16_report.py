# Shortcut Lab - EP16: Automate an Excel Report with Python (pandas + openpyxl)
# AUTHENTICITY: orders_clean.csv is the cleaned file from EP15 (demo/ep16/make_messy.py + clean.py, fictional shop, seeded data).
# Every script on screen is in demo/ep16/ and was run for real by demo/ep16/run_ep16.sh (Python 3.11, pandas 3.1.1, openpyxl 3.1.5);
# every terminal line is copied from demo/ep16/transcript.txt (long tracebacks shortened with "..."). The "xlsx" scenes draw the REAL
# workbooks read back with openpyxl (demo/ep16/export_xlsx.py -> xlsx.json: values, number formats, fonts, fills, widths, freeze panes);
# the "group" scene streams the REAL rows and their real running totals. The Total cell shows the sum Excel calculates from =SUM(B2:B8).
# Syntax checked against the pandas docs (read_csv parse_dates, groupby, pivot_table, ExcelWriter, to_excel) and openpyxl docs (styles).
import os, json
TITLE = "Automate an Excel Report with Python (pandas + openpyxl)"
SPEED = 0.82
ACCENT = (255, 184, 108)  # apricot (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta, EP12 cyan, EP13 jade, EP14 cobalt, EP15 citron)
SKY, YEL, MINT, CORAL, VIO, LIME = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255), (182, 243, 92)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep16")
def src(n): return open(os.path.join(D, n)).read().strip("\n")
TR = {}
for blk in open(os.path.join(D, "transcript.txt")).read().split("### ")[1:]:
    name, _, body = blk.partition("\n"); TR[name.strip()] = body.rstrip("\n").split("\n")
def out(name, cmd): return ["$ " + cmd] + TR[name]
def short_tb(name, cmd):
    L = TR[name]; i = L.index("Traceback (most recent call last):"); return ["$ " + cmd, L[i], L[i + 1], L[i + 2], "  ...", L[-1]]
X = json.load(open(os.path.join(D, "xlsx.json")))
STREAM, TOTALS = X["stream"], X["totals"]
REPORT, V1 = src("report.py"), src("report_v1.py")
def XL(sheet, **kw): return dict(type="xlsx", data=X, sheet=sheet, **kw)

SCENES = [
dict(chapter="The result", say="Every month, someone opens a giant spreadsheet, filters it, copies numbers into a new file, adds totals, and makes it look nice. It eats a whole morning. This report was made by a Python script, in under one second. Three sheets, a totals row, bold headers, and clean numbers. Today, you'll build it.",
     vis=XL("By city", sel="B9", rows=10, cols=2, zoom=40, rh=62, note="One script. Three sheets. Under one second.")),
dict(say="We'll start from the clean orders file we made in the last episode. If you missed it, no problem, any table with dates, categories and numbers works the same way. And I'll show you the three mistakes that break almost every first report, with the real error on screen.",
     vis=dict(type="title", kicker="Python for beginners", text="Automate an Excel Report", sub="pandas for the numbers  ·  openpyxl for the looks  ·  one script")),
dict(chapter="The plan", say="Here's the plan. Load the data. Add the columns the report needs. Summarize it, by city and by month. Write everything to one Excel file with three sheets. And finally, make it look like a person made it.",
     vis=dict(type="steps", title="The plan", items=["Load the CSV with real dates", "Add Revenue and Month columns", "Summarize: by city and by month", "Write 3 sheets to one Excel file", "Format: headers, widths, totals"])),
dict(chapter="Setup", say="You need Python, and two free libraries. Pandas does the math, and openpyxl is the engine that reads and writes Excel files. Open a terminal and type pip install pandas openpyxl. Then put orders clean dot c s v in a folder, and create a new file next to it called report dot p y.",
     vis=dict(type="term", title="Terminal", lines=["$ pip install pandas openpyxl", "$ python -c \"import pandas, openpyxl; print(pandas.__version__, openpyxl.__version__)\""] + TR["versions"])),
dict(chapter="Step 1: load the data", say="Step one. Import pandas as p d, and read the file with read c s v. Notice this extra part. Parse dates equals a list with Date. It tells pandas that the Date column holds real dates, not just text. Remember that, it's the first mistake later. Then print the shape and the first four rows.",
     vis=dict(type="code", code=src("look.py"), file="report.py", hl=(3,), cps=32)),
dict(say="Run it. Eight hundred and ninety two rows and eight columns. Order I D, date, customer, city, product, quantity, price and status. Look at row two. That order was cancelled. We don't want cancelled orders in a sales report.",
     vis=dict(type="term", title="Terminal", lines=out("look", "python report.py"))),
dict(chapter="Step 2: add the columns", say="Step two. First, keep only the rows where status is not equal to cancelled. Inside the square brackets is a test, and pandas keeps the rows where the test is true. Then a new column, Revenue, which is quantity times price, for every row at once. And Month, using dot d t dot s t r f time, with percent Y dash percent m. That turns a date into text like twenty twenty six dash zero four.",
     vis=dict(type="code", code=src("summary.py").split("\n\nby_city")[0], file="report.py", **{"from": 3}, hl=(4, 5, 6), cps=30)),
dict(chapter="Mistake 1: dates stored as text", say="And here's mistake number one. If you forget parse dates when you read the file, the Date column is just text. The moment you use dot d t, pandas stops with this. Attribute error. Can only use dot d t accessor with datetime like values. In plain English, that column isn't dates. The fix is the one we already have. Add parse dates to read c s v.",
     vis=dict(type="term", title="Terminal - forgot parse_dates", lines=short_tb("month_bad", "python month_bad.py"))),
dict(chapter="Step 3: totals by city", say="Step three, the first summary. Group by City, take the Revenue column, and sum it. Group by works like sorting cards into piles. Every row goes to the pile of its city, and then each pile is added up. Here it is, running for real, on all eight hundred and twenty five orders that are left after removing the cancelled ones.",
     vis=dict(type="group", stream=STREAM, totals=TOTALS, span=0.78, slow=7, note="Every row goes to its city's pile, then each pile is summed")),
dict(say="We add sort values, ascending equals false, so the biggest city comes first. Run it. Austin on top, with almost one hundred and sixty two thousand. Denver near the bottom. And Unknown, those are orders with an empty city that we kept in the last episode. Honest data shows them, instead of hiding them.",
     vis=dict(type="term", title="Terminal", lines=["$ python report.py"] + TR["summary"])),
dict(chapter="Step 4: a pivot table", say="Step four, a pivot table, exactly like the one in Excel. Index equals Month makes one row per month. Columns equals City makes one column per city. Values is Revenue, and agg func equals sum adds them up. Fill value equals zero puts a zero where a city had no sales, instead of an empty cell.",
     vis=dict(type="code", code=src("pivot.py"), file="report.py", **{"from": 7}, hl=(8, 9), cps=30)),
dict(say="And here's the result. Ten months down the side, seven cities across the top, and every cell is the real total for that month and city. I rounded it for the screen. Building this by hand in Excel takes clicks. Here it's two lines, and it updates itself every time the data changes.",
     vis=dict(type="term", title="Terminal - pivot table", lines=["$ python pivot.py"] + TR["pivot"])),
dict(chapter="Mistake 2: sheets that disappear", say="Now we write to Excel. And this is mistake number two. It feels natural to call to excel twice, one sheet for the summary, one for the data, both into report dot x l s x. Run it, and list the sheets. Only Data. The second call created a brand new file, and silently replaced the first one. Your summary is gone.",
     vis=dict(type="code", code=src("sheets_bad.py"), file="sheets_bad.py", hl=(7, 8), note="Two to_excel calls = the second file replaces the first", notecol=CORAL, cps=60)),
dict(say="Here's the real output. One sheet, called Data. No error, no warning. That's what makes this one so sneaky.",
     vis=dict(type="term", title="Terminal - where did my sheet go?", lines=out("sheets_bad", "python sheets_bad.py"))),
dict(chapter="Step 5: one file, three sheets", say="The fix is Excel Writer. With p d dot Excel Writer, report dot x l s x, as writer. Everything indented under that line writes into the same open file. Then call to excel three times, passing writer instead of a file name, each with its own sheet name. The file is saved once, when the with block ends.",
     vis=dict(type="code", code=V1, file="report.py", **{"from": 11}, hl=(12, 13, 14, 15), cps=32)),
dict(say="Open the file. Three tabs at the bottom. By city, By month, and Data. It works. But look at it. Every column is the same narrow width. In the Data sheet, the dates are just hash signs, because they don't fit. Nobody would send this to their boss. So let's fix the looks.",
     vis=XL("Data", book="report_v1.xlsx", build=True, rows=11, span=0.35, note="#### = the column is too narrow for the date", notecol=CORAL)),
dict(chapter="Mistake 3: the mystery column", say="Quick detour for mistake number three. See index equals false in those lines? Leave it out, and pandas also writes its row numbers, zero, one, two, as an extra first column. Read the file back, and you get a column called Unnamed zero. It's harmless, but it confuses everyone who opens the file. Add index equals false, unless the index means something, like our months.",
     vis=dict(type="term", title="Terminal - forgot index=False", lines=out("index_bad", "python index_bad.py"))),
dict(chapter="Step 6: make it look good", say="Step six, formatting, with openpyxl. Import Font and Pattern Fill. Then, still inside the with block, loop over every sheet. Writer dot sheets gives you each one. For every cell in row one, the header, we set a bold white font, and a solid dark green fill. Then every column gets a width of fourteen. And freeze panes equals A two keeps the header visible while you scroll.",
     vis=dict(type="code", code=REPORT, file="report.py", view=(11, 25), **{"from": 17}, hl=(18, 19, 20, 21, 22, 23, 24), cps=34)),
dict(say="Here's the difference on the By city sheet, the same data before and after. Wider columns, a real header, and a frozen line under it.",
     vis=XL("By city", morph="report_v1.xlsx", rows=10, cols=2, zoom=40, rh=62, span=0.45, note="Same data. Now it looks like a report.")),
dict(chapter="Step 7: totals and number format", say="Step seven, a totals row. Ws dot max row is the last row with data. One row below it, we write the word Total, and in column B, an Excel formula as text. Equals sum, B two to B eight. Because it's a real formula, if someone edits a number in Excel, the total updates. Then number format, with a comma for thousands and two decimals.",
     vis=dict(type="code", code=REPORT, file="report.py", view=(25, 38), **{"from": 25}, hl=(27, 28, 29, 32, 33), cps=34)),
dict(say="Click the total cell, and the formula bar shows sum B two to B eight. A live Excel formula, written by Python. And the last two lines in the script give the Data sheet a proper date format, so the hash signs are gone.",
     vis=XL("By city", sel="B9", rows=10, cols=2, zoom=40, rh=62, note="A real formula: edit any number and the total updates")),
dict(say="Here's the By month sheet. The months down the side, cities across, the green header, and it stays frozen while you scroll down.",
     vis=XL("By month", rows=11, cols=8, build=True, span=0.35)),
dict(say="And the Data sheet. Every order, with real dates instead of hash signs, the new Revenue column at the end, with Month right after it, and a frozen header. Anyone can click a header in Excel and filter it from here.",
     vis=XL("Data", rows=11, cols=10, note="Real dates, frozen header, ready to filter")),
dict(chapter="If something goes wrong", say="If your script fails, it's usually one of three things. No module named openpyxl means the library isn't installed, so run pip install openpyxl. A permission error on Windows usually means report dot x l s x is still open in Excel. Close it and run again. And a key error means a column name doesn't match, so check the spelling and the capital letters, exactly as they appear in the header.",
     vis=dict(type="compare", title="Three common errors", left=("What you see", ["No module named 'openpyxl'", "PermissionError", "KeyError: 'Revenue'"]), right=("The fix", ["pip install openpyxl", "Close report.xlsx in Excel", "Check the column name spelling"]))),
dict(chapter="The full script", say="Here's the whole script. About forty lines. Load, filter, add two columns, two summaries, one Excel file, three sheets, and the formatting. Pause here if you want to copy it. It's also in the description, ready to paste.",
     vis=dict(type="code", code=REPORT, file="report.py", lh=20, size=17, **{"from": 38})),
dict(chapter="Check the result", say="Always check what you made. This tiny script opens the report with load workbook, prints the sheet names, and prints every row of By city. Three sheets, seven cities, and the total row with its formula. Exactly what we built.",
     vis=dict(type="term", title="Terminal - check.py", lines=out("check", "python check.py"))),
dict(chapter="Pro tip: a new file every month", say="Pro tip. Put the month in the file name, so every run makes a new report instead of overwriting the old one. From date time import date. Then an f string, report underscore, and date dot today with percent Y dash percent m. Today that gives report underscore twenty twenty six dash eleven. Combine it with episode twelve, where we scheduled a script to run by itself, and this report literally makes itself every month.",
     vis=dict(type="term", title="Terminal - name.py", lines=[src("name.py").split("\n")[0], "", src("name.py").split("\n")[2], src("name.py").split("\n")[3], "", "$ python name.py"] + TR["name"])),
dict(chapter="How fast is it?", say="And the speed? I timed the full script, reading the data, every summary, all three sheets, and all the formatting. Under half a second. The morning you used to spend on this report is now a coffee break.",
     vis=dict(type="term", title="Terminal - timing", lines=["$ time python report.py"] + TR["timing"])),
dict(chapter="Cheat sheet", say="Here's your cheat sheet. Parse dates for real dates. A filter in square brackets. Group by and sum. Pivot table. Excel Writer for many sheets. Index equals false. And openpyxl for fonts, fills, widths and formulas. Pause and screenshot it.",
     vis=dict(type="cards", title="Excel report cheat sheet", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, VIO, CORAL, ACCENT, SKY, LIME],
              items=[['parse_dates=["Date"]', "Dates, not text"], ['df[df["Status"] != "x"]', "Keep only some rows"], ['groupby("City").sum()', "One total per group"],
                     ["pivot_table(...)", "Months x cities grid"], ["pd.ExcelWriter(...)", "Many sheets, one file"], ["index=False", "No mystery column"],
                     ["Font / PatternFill", "Bold header, color"], ["column_dimensions", "Column widths"], ['"=SUM(B2:B8)"', "Live Excel formula"]])),
dict(chapter="Recap", say="Quick recap. Read the file with parse dates. Filter, and add the columns you need. Summarize with group by and pivot table. Write all the sheets inside one Excel Writer. Then format with openpyxl. And put the month in the file name.",
     vis=dict(type="steps", title="Recap", items=["read_csv(..., parse_dates=[\"Date\"])", "Filter rows, add Revenue and Month", "groupby() and pivot_table()", "One ExcelWriter, three to_excel()", "openpyxl: header, widths, =SUM, formats"])),
dict(say="Next on Shortcut Lab, we leave spreadsheets behind, and pull data straight from a web page, with your first web scraper in Python. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Web Scraping with Python for Beginners")),
]
