# Shortcut Lab - EP14: Merge Hundreds of Excel Files into One with Python (pandas + openpyxl)
# AUTHENTICITY: the 240 practice workbooks are made by demo/ep14/make_files.py (fictional coffee chain, seeded random data, no real
# data). Every script on screen is in demo/ep14/ and was run for real by demo/ep14/run_ep14.sh (Python 3.11, pandas 3.1.1, openpyxl
# 3.1.5); every terminal line is copied from demo/ep14/transcript.txt. The "~$" lock file is a few-byte stand-in for the hidden owner
# file Excel leaves next to an open workbook; the error it causes is the real pandas message. The "merge" scenes read
# demo/ep14/merge.json (export_merge.py: real file names, real row counts, real first row of each file).
import os, json
TITLE = "Merge Hundreds of Excel Files into One with Python"
SPEED = 0.82
ACCENT = (95, 120, 255)  # cobalt (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta, EP12 cyan, EP13 jade)
SKY, YEL, MINT, CORAL, VIO = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep14")
def src(n): return open(os.path.join(D, n)).read().strip("\n")
TR = {}
for blk in open(os.path.join(D, "transcript.txt")).read().split("### ")[1:]:
    name, _, body = blk.partition("\n"); TR[name.strip()] = body.rstrip("\n").split("\n")
def out(name, cmd): return ["$ " + cmd] + TR[name]
def short_tb(name, cmd):  # traceback shortened: first line(s) before it, "...", last line
    L = TR[name]; i = L.index("Traceback (most recent call last):"); return ["$ " + cmd] + L[:i + 1] + ["  ..."] + L[-1:]
ALL = json.load(open(os.path.join(D, "merge.json")))
CLEAN = [f for f in ALL if f["flag"] != "lock"]
MERGE = src("merge.py"); FINAL = src("merge_final.py")

SCENES = [
dict(chapter="The result", say="Two hundred and forty Excel files. One for every store, for every month of the year. Watch. In about two seconds, Python opens every single one, and stacks them into one clean spreadsheet. Five thousand seven hundred and eighteen rows, and not one copy and paste.",
     vis=dict(type="merge", files=CLEAN, skip=True, span=0.75, accel=2.4, note="240 files in, 1 spreadsheet out")),
dict(say="Today you'll build that script, step by step, even if you've never written Python before. You'll read one Excel file, then a whole folder, and save the result as one file. And I'll show you the three mistakes that break this script for almost everyone, including one that gives you the wrong numbers without any error at all.",
     vis=dict(type="title", kicker="Python for beginners", text="Merge Hundreds of Excel Files into One", sub="pandas reads every file  ·  one script  ·  about two seconds")),
dict(chapter="The plan", say="Here's the plan. Install two free libraries. Read one file, to see what pandas gives you. Find every file in the folder. Stack them together, and save. Then check the result, because a merge that runs is not always a merge that's right.",
     vis=dict(type="steps", title="The plan", items=["Install pandas and openpyxl", "Read one Excel file", "Find every file in the folder", "Stack them and save one file", "Check the result (always!)"])),
dict(chapter="Why not copy and paste", say="Why not just open each file and copy the rows over? With five files, sure. With two hundred and forty, that's an afternoon of clicking, and it's very easy to skip a file, or paste one twice. And next month, you'd have to do it all again. A script does the same job the same way every time, in seconds.",
     vis=dict(type="compare", title="Copy and paste vs. a script", left=("Copy and paste", ["240 files = hours of clicking", "Easy to skip or double a file", "Start over every month"]),
              right=("A Python script", ["240 files in about 2 seconds", "Every file, exactly once", "Run it again next month"]))),
dict(chapter="Install pandas", say="You need Python installed, free from python dot org. Open a terminal and type pip install pandas openpyxl. Pandas is the library that works with tables. Openpyxl is what pandas uses to read and write Excel files. Without it, read excel won't work. Then check both with this one line. Two version numbers means you're ready.",
     vis=dict(type="term", lines=["$ pip install pandas openpyxl", "", "$ python3 -c \"import pandas, openpyxl; print(pandas.__version__, openpyxl.__version__)\""] + TR["versions"])),
dict(chapter="The practice files", say="Here's our project folder. Inside reports, there are two hundred and forty workbooks, named by month and store. There's also one workbook with several sheets, which we'll use for a bonus at the end. Your scripts go right here, next to the reports folder.",
     vis=dict(type="files", title="The project folder", before=["reports/  (240 .xlsx files)", "online_2026.xlsx  (4 sheets)", "merge.py  (your script)"], hdr1="project/")),
dict(say="List the folder, and you can see the pattern. Twenty twenty six, dash, the month, then the store number. Two hundred and forty files in total. Every one of them has the same four columns. Date, product, units, and price.",
     vis=dict(type="term", lines=["$ ls reports | head -3"] + TR["ls"][:3] + ["$ ls reports | tail -2"] + TR["ls"][4:6] + ["$ ls reports | wc -l"] + TR["ls"][6:])),
dict(chapter="Step 1: read one file", say="Step one. Before touching two hundred and forty files, read just one. Create peek dot py. Import pandas as p d, that's the short name everybody uses. Then p d dot read excel, with the path to one file, gives you a data frame. That's pandas' word for a table. Print df dot head, to see the first five rows. And df dot shape tells you the size.",
     vis=dict(type="code", file="peek.py", code=src("peek.py"), hl=(3, 4, 5))),
dict(say="Run it. There's the first store's January sales, as a neat table. The numbers on the left are just row numbers that pandas adds. And the shape, nineteen comma four, means nineteen rows and four columns. If this works, the hard part is already done. Merging is just doing this in a loop.",
     vis=dict(type="term", lines=out("peek", "python3 peek.py"), out_gap=0.2)),
dict(chapter="Step 2: find every file", say="Step two. Create merge dot p y. From pathlib, import Path. Path, reports, dot glob, star dot x l s x, finds every file in the reports folder that ends in dot x l s x. The star means any name. Sorted puts them in alphabetical order, so the result is the same every time you run it. Then print how many files it found. That one number will save you a lot of confusion later.",
     vis=dict(type="code", file="merge.py", code=MERGE, view=(0, 5), hl=(4, 5))),
dict(chapter="Step 3: read them in a loop", say="Step three, the loop. Start with an empty list, called frames. For each file, read it with read excel, exactly like before. Then add a new column, called Source, with the file's name. That way, every row remembers where it came from. Trust me, when a number looks wrong later, this column is how you find the file to blame. And append the table to the list.",
     vis=dict(type="code", file="merge.py", code=MERGE, view=(0, 11), hl=(7, 9, 10, 11), **{"from": 6})),
dict(chapter="Step 4: stack and save", say="Step four. P d dot concat takes the list of tables, and stacks them one under the other. Ignore index equals true renumbers the rows from zero, so you don't get two hundred and forty row zeros. Print the number of rows. Then to excel saves everything into one file, all sales dot x l s x. Index equals false leaves out the row numbers.",
     vis=dict(type="code", file="merge.py", code=MERGE, hl=(13, 15), **{"from": 12})),
dict(say="Save, and run python three merge dot p y. Files found, two hundred and forty. Rows, five thousand seven hundred and eighteen. Saved all sales dot x l s x. That's it. That's the whole merge.",
     vis=dict(type="term", lines=out("merge", "python3 merge.py"), out_gap=0.35)),
dict(say="Here's what just happened, file by file. Each workbook is read, gets its Source name, and lands at the bottom of the big table. But look closely. One file just turned yellow. Something in it didn't fit. And Python didn't say a word.",
     vis=dict(type="merge", files=CLEAN, naive=True, span=0.75, accel=2.0)),
dict(chapter="Check the result", say="This is why step five matters. Always check a merge. Create check dot p y, read the merged file back, and print three things. The shape, the column names, and is n a dot sum, which counts the empty cells in each column. N a means not available, an empty value.",
     vis=dict(type="code", file="check.py", code=src("check.py"), hl=(4, 5, 6))),
dict(say="And there's the problem. We expected five columns, but there are six. A column called Qty appeared out of nowhere. Units has twenty five empty cells, and Qty is empty almost everywhere. So when you add up units, you'd be missing sales, and you'd never know.",
     vis=dict(type="term", lines=out("check", "python3 check.py"), out_gap=0.12)),
dict(say="Which file did it? Thanks to the Source column, that's easy. Keep the rows where units is empty, and count them by source. One file. Store seven, September. Twenty five rows.",
     vis=dict(type="term", lines=out("find_bad", "python3 find_bad.py"))),
dict(chapter="Mistake 1: different column names", say="Open that file, and the mystery is solved. Somebody typed Qty in the header, instead of Units. To pandas, those are two different columns, so concat keeps both, and fills the gaps with empty values. The fix is one line. Right after reading each file, rename Qty to Units. Now every file speaks the same language.",
     vis=dict(type="compare", title="Same data, different header", left=("2026-09_store07.xlsx", ["Date | Product | Qty | Price", "pandas sees a NEW column", "Units = empty (NaN)"]),
              right=("The fix", ["Rename right after reading", "{\"Qty\": \"Units\"}", "Units everywhere, no gaps"]))),
dict(chapter="Mistake 2: the wrong folder", say="Mistake number two. You run the script from the wrong folder. Here I moved up one level, and ran it from there. Files found, zero. And then a scary error. Value error, no objects to concatenate. It just means the list was empty. Python looked for a reports folder where you are, and found nothing. Use c d to go to the project folder first. And that's exactly why we print the number of files.",
     vis=dict(type="term", lines=["$ cd .."] + short_tb("wrong_folder", "python3 project/merge.py") + ["", "# fix: cd project, then run it again"])),
dict(chapter="Mistake 3: a file that's open", say="Mistake number three, and this one gets everybody. Leave one of the workbooks open in Excel, and run the script. Excel quietly creates a hidden file next to it, starting with tilde dollar. It ends in x l s x, so glob picks it up. But it isn't a real workbook. Watch what happens.",
     vis=dict(type="merge", files=ALL, span=0.6, accel=2.2, error="ValueError: Excel file format cannot be determined")),
dict(say="Two hundred and forty files read, and then it crashes on the very last one. Files found, two hundred and forty one, one more than we have. And the error says, Excel file format cannot be determined. Close the workbook in Excel and the file disappears. But it's better to make the script skip it.",
     vis=dict(type="term", lines=short_tb("lockfile", "python3 merge.py") + ["", "$ ls reports | grep '~'", "~$2026-11_store04.xlsx"])),
dict(chapter="The final script", say="Here's the final script, with both fixes. Inside the loop, if the file name starts with tilde dollar, print a message and continue, which jumps to the next file. Then the rename, so Qty becomes Units. And one extra print at the end, the total count of missing values. If that number isn't zero, you know to look closer.",
     vis=dict(type="code", file="merge.py", code=FINAL, hl=(9, 10, 11, 13, 19), lh=38, size=25, cps=60, **{"from": 7})),
dict(say="Run it, with the lock file still there. Files found, two hundred and forty one. Skipping lock file. Rows, five thousand seven hundred and eighteen. Missing values, zero.",
     vis=dict(type="term", lines=out("merge_final", "python3 merge.py"), out_gap=0.35)),
dict(say="Same run, file by file. The lock file is skipped and crossed out, store seven's Qty column is renamed on the way in, and every row lands under the right header.",
     vis=dict(type="merge", files=ALL, skip=True, span=0.7, accel=2.2, note="5,718 rows  ·  0 missing values")),
dict(say="And the check agrees. Five columns, all of them with zero empty cells. Now you can trust the totals.",
     vis=dict(type="term", lines=out("check2", "python3 check.py"), out_gap=0.12)),
dict(chapter="Pro tip: a summary sheet", say="Pro tip. Once everything is in one table, the report is a few lines away. Multiply units by price to get revenue. The store number is inside the file name, characters eight to fifteen, so string slicing pulls it out. Group by store, and sum the revenue. Then an Excel writer saves two sheets into one workbook. All the rows, and the summary by store.",
     vis=dict(type="code", file="summary.py", code=src("summary.py"), hl=(4, 5, 7, 10, 11, 12), lh=40, size=25, cps=55)),
dict(say="Run it. The top five stores by revenue, with store nine in first place. And report dot x l s x, with both sheets inside, ready to send.",
     vis=dict(type="term", lines=out("summary", "python3 summary.py"), out_gap=0.2)),
dict(chapter="Bonus: many sheets in one file", say="Bonus. What if the data is in one workbook, but split across many sheets? Read excel with sheet name equals None reads every sheet at once. You get a dictionary, sheet name, and its table. Concat on the dictionary's values stacks them, exactly like before.",
     vis=dict(type="code", file="sheets.py", code=src("sheets.py"), hl=(3, 6))),
dict(say="Four sheets, quarter one to quarter four, and one table with twenty four rows. Want to know which sheet each row came from? Pass the whole dictionary to concat, and name the levels. Reset index turns the sheet name into a normal column.",
     vis=dict(type="term", lines=out("sheets", "python3 sheets.py") + [""] + out("sheets_tag", "python3 sheets_tag.py"), out_gap=0.15)),
dict(chapter="How fast is it?", say="And how fast is all this? I timed the final script on these two hundred and forty files. Two point three seconds, including saving the result. By hand, at even thirty seconds per file, that's two hours.",
     vis=dict(type="tip", tag="TIMED FOR REAL", text="240 workbooks, 5,718 rows: " + TR["timing"][0] + " with the final script. By hand: about 2 hours.", color=ACCENT)),
dict(chapter="Cheat sheet", say="Here's your cheat sheet. Read excel for one file. Glob to find them all. A Source column to remember where rows came from. Concat to stack. Rename when headers don't match. And skip anything that starts with tilde dollar.",
     vis=dict(type="cards", title="The merge cheat sheet", cols=2, span=0.6, colors=[ACCENT, SKY, YEL, MINT, CORAL, VIO],
              items=[["pd.read_excel(f)", "Read one workbook into a table"], ["Path(\"reports\").glob(\"*.xlsx\")", "Find every Excel file"], ["df[\"Source\"] = f.name", "Remember where each row came from"],
                     ["pd.concat(frames, ignore_index=True)", "Stack all the tables"], ["df.rename(columns={\"Qty\": \"Units\"})", "Fix headers that don't match"], ["f.name.startswith(\"~$\")", "Skip Excel's lock files"]])),
dict(chapter="Recap", say="Quick recap. Install pandas and openpyxl. Read one file first. Glob finds every file, and a loop reads them, adding a Source column. Concat stacks them, and to excel saves one file. Then always check, with is n a dot sum.",
     vis=dict(type="steps", title="Recap", items=["pip install pandas openpyxl", "pd.read_excel() one file first", "glob + loop + Source column", "pd.concat() + to_excel()", "Check: shape, columns, isna().sum()"])),
dict(say="Next on Shortcut Lab, we take this merged table, and clean it. Extra spaces, duplicates, dates written five different ways, and empty cells, fixed with pandas in a few lines. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Clean Messy Data with Python (pandas)")),
]
