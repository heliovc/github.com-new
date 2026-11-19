# Shortcut Lab - EP15: Clean Messy Data with Python (pandas)
# AUTHENTICITY: orders.csv is made by demo/ep15/make_messy.py (fictional online shop, seeded random data, no real people).
# Every script on screen is in demo/ep15/ and was run for real by demo/ep15/run_ep15.sh (Python 3.11, pandas 3.1.1); every
# terminal line is copied from demo/ep15/transcript.txt (long lines wrapped like a terminal does, long tracebacks shortened with
# "..."). The "clean" scenes read demo/ep15/clean.json (export_clean.py: real rows of the file and the real whole-file counts).
import os, json
TITLE = "Clean Messy Data with Python (pandas)"
SPEED = 0.82
ACCENT = (214, 232, 74)  # citron (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta, EP12 cyan, EP13 jade, EP14 cobalt)
SKY, YEL, MINT, CORAL, VIO = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep15")
def src(n): return open(os.path.join(D, n)).read().strip("\n")
TR = {}
for blk in open(os.path.join(D, "transcript.txt")).read().split("### ")[1:]:
    name, _, body = blk.partition("\n"); TR[name.strip()] = body.rstrip("\n").split("\n")
def wrapl(L, n=88):  # hard-wrap long lines the way a narrow terminal does
    out = []
    for l in L:
        while len(l) > n: out.append(l[:n]); l = l[n:]
        out.append(l)
    return out
def out(name, cmd): return ["$ " + cmd] + wrapl(TR[name])
def short_tb(name, cmd, last=1):
    L = TR[name]; i = L.index("Traceback (most recent call last):"); return ["$ " + cmd] + L[:i] + [L[i], "  ..."] + wrapl(L[-last:])
DATA = json.load(open(os.path.join(D, "clean.json")))
CLEAN = src("clean.py")

SCENES = [
dict(chapter="The result", say="One thousand orders, typed by five different people. Extra spaces, random capitals, the same order pasted twice, dates written three different ways, and prices stored as text. Watch. Six steps of pandas, and every one of those problems is gone.",
     vis=dict(type="clean", data=DATA, frm=0, upto=6, span=0.82, note="1,000 messy rows in, 892 clean rows out")),
dict(say="Today you'll write that cleaning script yourself, step by step, even if you're new to Python. You'll learn how to find the problems first, fix each one with a single line, and avoid the three mistakes that make cleaning code silently do nothing, or crash.",
     vis=dict(type="title", kicker="Python for beginners", text="Clean Messy Data with pandas", sub="spaces  ·  capitals  ·  duplicates  ·  dates  ·  numbers  ·  empty cells")),
dict(chapter="The plan", say="Here's the plan. Load the file and look at it. Run a quick health check, to count the problems. Then fix them in a smart order. Text first, then duplicates, then dates and numbers, then empty cells. And finally, save a clean copy, and check it.",
     vis=dict(type="steps", title="The plan", items=["Load the file and look at it", "Health check: count the problems", "Fix text, then remove duplicates", "Fix dates, numbers, and empty cells", "Save a clean copy (and check it)"])),
dict(chapter="Why clean at all?", say="Why bother? Because messy data gives you wrong answers, without any warning. In this file, Boston, boston, and Boston with a space at the end, are three different cities to a computer. Prices with a dollar sign aren't numbers at all. At the end of this video, I'll show you how far off the totals were. It's not a small difference.",
     vis=dict(type="compare", title="What the computer actually sees", left=("Messy", ["\"Boston\", \"boston\", \"Boston  \"", "\"$1,299.00\" is text, not a number", "The same order, counted twice"]),
              right=("Clean", ["One city: Boston", "1299.0, a real number", "Every order exactly once"]))),
dict(chapter="Setup", say="You need Python, free from python dot org, and pandas. Open a terminal, and type pip install pandas. Then check it with this one line. If you see a version number, you're ready. Mine says three point one point one.",
     vis=dict(type="term", lines=["$ pip install pandas", "", "$ python3 -c \"import pandas; print(pandas.__version__)\""] + TR["versions"])),
dict(chapter="The messy file", say="Here's our practice file, orders dot c s v. A C S V is just a table saved as plain text, one row per line, commas between the columns. Excel and Google Sheets can both export it. Look at the first few lines. You can already see trouble. Denver in capitals, a date with slashes, extra spaces after a name, and some prices with a dollar sign, some without.",
     vis=dict(type="term", lines=out("csvhead", "head -6 orders.csv"), out_gap=0.25)),
dict(chapter="Step 1: load and look", say="Step one. Create a file called clean dot p y, next to the C S V. Import pandas as p d. That's the short name everyone uses. Read c s v loads the file into a data frame, pandas' name for a table. Print the first six rows with head, and the size with shape.",
     vis=dict(type="code", file="look.py", code=src("look.py"), hl=(3, 4, 5))),
dict(say="Run it. Pandas hides the middle columns with three dots, so the table fits. And the shape says one thousand rows, eight columns. Notice the quantity column shows three point zero instead of three. That's a clue. Some quantities are missing, and pandas uses decimals when a column has empty cells.",
     vis=dict(type="term", lines=out("look", "python3 look.py"), out_gap=0.15)),
dict(chapter="Step 2: health check", say="Step two, the health check. Before fixing anything, count the problems, so you know what you're dealing with. Duplicated dot sum counts rows that are exact copies of an earlier row. N unique counts the different values in a column. And is n a dot sum counts the empty cells in every column. N a means not available.",
     vis=dict(type="code", file="health.py", code=src("health.py"), hl=(5, 6, 8))),
dict(say="Here's the report. Twenty nine duplicate rows. Fifty different cities, in a shop that only sells in six. Twenty customers with no name, forty two orders with no city, and thirty with no quantity. Now we have a to do list.",
     vis=dict(type="term", lines=out("health", "python3 health.py"), out_gap=0.15)),
dict(chapter="Step 3: fix the text", say="Step three, the text. For the customer and city columns, dot s t r gives you text tools for a whole column at once. Strip removes spaces at the start and end. Title makes the first letter of each word a capital. For status, we use lower, so everything is lower case. And notice the equals sign. We save the result back into the same column.",
     vis=dict(type="code", file="clean.py", code=CLEAN, view=(0, 9), hl=(7, 8, 9))),
dict(say="Here's what that does, on real rows from the file. The dots are the extra spaces, made visible. Watch them disappear, and the capitals line up. Across the whole file, that's one thousand three hundred and three cells fixed, by three lines of code.",
     vis=dict(type="clean", data=DATA, frm=0, upto=1, span=0.7)),
dict(chapter="Mistake 1: forgetting to save", say="Mistake number one, and almost everyone makes it. Look at line four. It strips and fixes the city, but doesn't save the result anywhere. Pandas makes a cleaned copy, and throws it away. Then on line seven, the same thing with the equals sign.",
     vis=dict(type="code", file="forgot.py", code=src("forgot.py"), hl=(4, 7))),
dict(say="Run it. The first count is still fifty. Nothing changed, and there's no error to warn you. After the line with the equals sign, six cities. Chicago, Austin, Miami, Denver, Boston, and Seattle. If a fix seems to do nothing, check that you saved it back.",
     vis=dict(type="term", lines=out("forgot", "python3 forgot.py"), out_gap=0.15)),
dict(chapter="Step 4: fix typos", say="Now, typos. The best way to find them is value counts. It lists every different value in a column, and how often it appears. After making status lower case, we get four values. Shipped, pending, cancelled, and shiped, with one p. Forty eight times.",
     vis=dict(type="term", lines=out("status", "python3 status.py"), out_gap=0.15)),
dict(say="The fix is replace, with a small dictionary. The wrong spelling on the left, the right one on the right. You can add as many pairs as you need. And here it is on the real rows. Every shiped becomes shipped.",
     vis=dict(type="clean", data=DATA, frm=1, upto=2, span=0.6)),
dict(chapter="Step 5: remove duplicates", say="Step five, duplicates. One line. Df equals df dot drop duplicates. It keeps the first copy of every row, and drops the rest. Watch rows twenty two and one fifty nine. Before the text fix, one said Zoe Hayes in capitals, with lowercase boston. Now they're identical, so the second one goes.",
     vis=dict(type="clean", data=DATA, frm=2, upto=3, span=0.6)),
dict(chapter="Mistake 2: the wrong order", say="And that's mistake number two. The order of the steps matters. If you remove duplicates first, pandas only finds twenty nine. Fix the text first, and it finds sixty. Thirty one copies were hiding behind a capital letter or a space. So, always clean the text, then remove duplicates.",
     vis=dict(type="term", lines=out("dupes_order", "python3 dupes_order.py"), out_gap=0.4)),
dict(chapter="Step 6: real dates", say="Step six, dates. Right now they're just text, in three styles. Year month day, month slash day slash year, and the month written out in words. Try the obvious fix, p d dot to datetime, and it crashes. Pandas guesses the format from the first row, and the second row doesn't match it.",
     vis=dict(type="term", lines=["$ cat dates_bad.py", "df[\"Date\"] = pd.to_datetime(df[\"Date\"])", ""] + short_tb("dates_bad", "python3 dates_bad.py", last=4), out_gap=0.12)),
dict(say="The error even tells you the fix. Pass format equals mixed, and pandas reads each date on its own. Now every date is a real date, written the same way, and you can sort by it, or group by month. One warning. If your dates are day first, like in Europe, add day first equals true. Otherwise March fifth becomes May third.",
     vis=dict(type="clean", data=DATA, frm=3, upto=4, span=0.6)),
dict(chapter="Mistake 3: numbers stored as text", say="Mistake number three. Numbers stored as text. You'd think to numeric turns the price into a number. But it crashes on the very first row. Unable to parse string, dollar thirty four ninety. A dollar sign and a comma aren't part of a number, so pandas gives up.",
     vis=dict(type="term", lines=["$ cat price_bad.py", "df[\"Price\"] = pd.to_numeric(df[\"Price\"])", ""] + short_tb("price_bad", "python3 price_bad.py"), out_gap=0.12)),
dict(say="So clean the text first. Str dot replace removes the dollar sign, then the comma. Then to numeric works. All nine hundred and forty prices are real numbers now. Pandas writes thirty four point nine, without the last zero. That's normal. It's the same number.",
     vis=dict(type="code", file="clean.py", code=CLEAN, view=(17, 20), hl=(19, 20))),
dict(say="Here it is on the rows. Dollar signs and commas gone, and every price lines up as a number.",
     vis=dict(type="clean", data=DATA, frm=4, upto=5, span=0.6)),
dict(chapter="Step 7: empty cells", say="Last, the empty cells. There's no single right answer. You decide per column. An order with no customer, or no quantity, can't be trusted, so drop n a with subset removes those rows. A missing city is less serious, so fill n a writes Unknown. And now that quantity has no gaps, as type int turns three point zero back into three.",
     vis=dict(type="code", file="clean.py", code=CLEAN, view=(21, 25), hl=(23, 24, 25))),
dict(say="Watch. Rows nineteen and ninety two are dropped. Row fifty four keeps its order, and gets Unknown as the city. That's forty eight rows removed, and thirty four cities filled.",
     vis=dict(type="clean", data=DATA, frm=5, upto=6, span=0.6)),
dict(chapter="The full script", say="Here's the whole script. Load, fix the text, fix the typo, drop duplicates, dates, prices, and empty cells. At the end, print the new shape, and the number of empty cells left. And to c s v saves a new file, orders clean dot c s v. Never overwrite the original. If something goes wrong, you want to start again from the raw data.",
     vis=dict(type="code", file="clean.py", code=CLEAN, hl=(4, 27, 28, 29), lh=25, size=19, cps=90)),
dict(say="Run it. Before, one thousand rows. After, eight hundred and ninety two. Empty cells left, zero. Saved.",
     vis=dict(type="term", lines=out("clean", "python3 clean.py"), out_gap=0.4)),
dict(chapter="Check the result", say="Always check the result. Read the clean file back, with parse dates, so the date column loads as dates. Look at the first rows. Neat. And d types shows the type of every column. Date is a date time, quantity is an integer, and price is a float, a decimal number. That's exactly what we want.",
     vis=dict(type="term", lines=out("check_clean", "python3 check_clean.py"), out_gap=0.12)),
dict(chapter="Pro tip: messy totals lie", say="Pro tip. Here's why all of this matters. This script computes revenue by city, on the messy file, and on the clean one. On the messy file, pandas can't read the prices with dollar signs, so it quietly skips them.",
     vis=dict(type="code", file="report.py", code=src("report.py"), hl=(6, 7, 8))),
dict(say="The messy file says fifty cities, and five hundred and fifty six thousand dollars. The clean file says seven cities, counting Unknown, and seven hundred and eighty three thousand. The messy report was off by more than two hundred thousand dollars, and nothing warned us.",
     vis=dict(type="term", lines=out("report", "python3 report.py"), out_gap=0.6)),
dict(chapter="How fast is it?", say="And the speed? I timed the full cleaning script on these one thousand rows. A quarter of a second. And next month, when a new export arrives, you just run it again.",
     vis=dict(type="tip", tag="TIMED FOR REAL", text="1,000 messy rows cleaned in " + TR["timing"][0] + " with the full script. Run it again on every new export.", color=ACCENT)),
dict(chapter="Cheat sheet", say="Here's your cheat sheet. Strip and title for messy text. Value counts to find typos, and replace to fix them. Drop duplicates, after the text. To datetime with format mixed. Replace, then to numeric, for prices. And drop n a or fill n a for empty cells.",
     vis=dict(type="cards", title="The data cleaning cheat sheet", cols=2, span=0.6, colors=[ACCENT, SKY, YEL, MINT, CORAL, VIO],
              items=[["df[c].str.strip().str.title()", "Trim spaces, fix capitals"], ["df[c].value_counts()", "See every variant (find typos)"], ["df.drop_duplicates()", "Remove copies (after fixing text!)"],
                     ["pd.to_datetime(s, format=\"mixed\")", "Dates in any style become real dates"], ["s.str.replace(\"$\", \"\")", "Then pd.to_numeric(s)"], ["df.dropna(subset=[...])", "Or df[c].fillna(\"Unknown\")"]])),
dict(chapter="Recap", say="Quick recap. Look first, and run a health check. Fix the text, and save it back with the equals sign. Remove duplicates after the text. Turn dates and prices into real dates and numbers. Decide what to do with empty cells. And save a clean copy.",
     vis=dict(type="steps", title="Recap", items=["head(), shape, isna().sum()", "str.strip() / title() / lower(), saved back", "drop_duplicates() after the text fix", "to_datetime(format=\"mixed\"), to_numeric()", "dropna / fillna, then to_csv() a copy"])),
dict(say="Next on Shortcut Lab, we take this clean table, and turn it into an automatic Excel report, with totals by city and by month, in one script. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Automate an Excel Report with Python (pandas)")),
]
