# Shortcut Lab - EP03: 7 Excel formulas that replace hours of work
# Every result shown comes from demo/ep03_results.json, computed by demo/ep03_compute.py (pandas, Microsoft's documented
# semantics). Syntax checked on support.microsoft.com (XLOOKUP, TEXTSPLIT, FILTER, UNIQUE, SORT, SUMIFS, IFS).
import os, json
TITLE = "7 Excel Formulas That Replace Hours of Work"
SPEED = 0.82
ACCENT = (255, 122, 89)  # coral (EP01 lime, EP02 sky)
R = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep03_results.json")))

ROWS = [(1001, "Ana", "East", "Laptop", 1200), (1002, "Ben", "West", "Mouse", 25), (1003, "Cara", "North", "Monitor", 300),
        (1004, "Ana", "East", "Keyboard", 80), (1005, "Dev", "West", "Laptop", 1150), (1006, "Ben", "West", "Monitor", 320),
        (1007, "Cara", "North", "Laptop", 1250), (1008, "Eli", "South", "Mouse", 30), (1009, "Dev", "West", "Keyboard", 75),
        (1010, "Ana", "East", "Monitor", 310), (1011, "Eli", "South", "Laptop", 1100), (1012, "Ben", "West", "Keyboard", 90)]
HDR = ["Order", "Rep", "Region", "Product", "Amount"]
def table(extra=None):
    c = {f"{'ABCDE'[j]}1": h for j, h in enumerate(HDR)}
    for i, r in enumerate(ROWS):
        for j, val in enumerate(r): c[f"{'ABCDE'[j]}{i + 2}"] = val
    c.update(extra or {}); return c
def rows_where(f): return [i + 2 for i, r in enumerate(ROWS) if f(r)]
HG = {f"{c}1": h for c, h in zip("GHIJK", HDR)}  # headers over a 5-column result in G:K
W5 = [110, 95, 110, 130, 115, 50, 120, 95, 110, 130, 115]
W2 = [110, 95, 110, 130, 115, 50, 150, 150]

SCENES = [
dict(chapter="The result", say="Twelve orders, five sales reps. Who sold the most? Instead of adding it up by hand, you type one formula, and Excel builds the whole report for you. Every rep, every total. And it updates itself when the data changes.",
     vis=dict(type="sheet", cells=table({"G1": "Rep", "H1": "Total", **{f"G{i + 2}": r for i, (r, _) in enumerate(R["report"])}}), widths=W2,
              at="H2", formula="=SUMIFS(E2:E13,B2:B13,G2#)", ranges=["E2:E13", "B2:B13"], result=[[x] for _, x in R["report"]], cps=34, note="One formula. The whole report.")),
dict(say="In the next ten minutes, you'll learn seven Excel formulas that replace hours of copying, filtering and adding things up by hand. One small table, step by step, no experience needed. And around the middle, I'll show you the error that confuses almost everyone the first time, and how to fix it in two seconds.",
     vis=dict(type="title", kicker="Excel for beginners", text="7 Excel Formulas That Replace Hours of Work", sub="XLOOKUP · FILTER · UNIQUE · SORT · SUMIFS · IFS · TEXTSPLIT")),
dict(chapter="The 7 formulas", say="Here's the list. XLOOKUP finds any value. FILTER pulls out every matching row. UNIQUE removes duplicates. SORT puts a table in order. SUMIFS adds up numbers with conditions. IFS labels rows using rules. And TEXTSPLIT breaks text into separate cells. One quick note. These need Excel for Microsoft 365, or Excel 2021 or newer. TEXTSPLIT needs Microsoft 365, or Excel 2024.",
     vis=dict(type="steps", title="The 7 formulas", items=["XLOOKUP: find any value", "FILTER: pull every matching row", "UNIQUE: remove duplicates", "SORT: order by any column",
              "SUMIFS: totals with conditions", "IFS: label rows with rules", "TEXTSPLIT: split text into cells"])),
dict(chapter="The practice table", say="Here's our practice table. The order number is in column A, the sales rep in B, the region in C, the product in D, and the amount in E. Twelve orders, from row two down to row thirteen. Type it in, or use any table you already have. The formulas work exactly the same way.",
     vis=dict(type="sheet", cells=table(), widths=W5, at="A1", note="Build this table to follow along")),
# 1 XLOOKUP
dict(chapter="#1 XLOOKUP: find any value", say="Formula one, XLOOKUP. It finds a value in one column, and brings back the matching value from another column. It needs three things. What you're looking for, where to look, and what to bring back. The fourth one is optional, but I always use it. It's the text to show when nothing matches.",
     vis=dict(type="args", title="#1  XLOOKUP", fn="XLOOKUP", args=[("lookup_value", "what you're looking for"), ("lookup_array", "the column to search in"),
              ("return_array", "the column to bring back"), ("if_not_found", "what to show if nothing matches", True)],
              example='=XLOOKUP(G2, A2:A13, E2:E13, "Not found")', parts=["G2", "A2:A13", "E2:E13", '"Not found"'])),
dict(say="Let's find the amount for order ten oh seven. Type the order number in G2. Then click H2 and type equals XLOOKUP, open bracket, G2, comma, A2 colon A13, that's the order column, comma, E2 colon E13, the amount column, comma, and Not found, in quotes. Press Enter. Twelve fifty. That's exactly the right row.",
     vis=dict(type="sheet", cells=table({"G1": "Find", "H1": "Amount", "G2": 1007}), widths=W2, at="H2", formula='=XLOOKUP(G2,A2:A13,E2:E13,"Not found")',
              ranges=["G2", "A2:A13", "E2:E13"], mark=rows_where(lambda r: r[0] == 1007), result=[R["xlookup_1007"]])),
dict(say="Now change G2 to an order that doesn't exist, like ten ninety nine. Instead of an ugly error, you get a clean Not found. Without that fourth argument, Excel would show hash N A.",
     vis=dict(type="sheet", cells=table({"G1": "Find", "H1": "Amount", "G2": 1099}), widths=W2, at="H2", formula='=XLOOKUP(G2,A2:A13,E2:E13,"Not found")', static=True,
              result=[R["xlookup_1099"]], rescol=(255, 211, 105))),
dict(say="Here's a pro move. The return array can be more than one column. Change E2 colon E13 to B2 colon E13, and XLOOKUP brings back the whole row. Rep, region, product and amount, spilled across four cells, from one formula.",
     vis=dict(type="sheet", cells=table({"G1": "Find", "H1": "Rep", "I1": "Region", "J1": "Product", "K1": "Amount", "G2": 1007}), widths=W5, at="H2",
              formula='=XLOOKUP(G2,A2:A13,B2:E13,"Not found")', ranges=["G2", "A2:A13", "B2:E13"], mark=rows_where(lambda r: r[0] == 1007), result=[R["xlookup_multi"]])),
# 2 FILTER
dict(chapter="#2 FILTER: every matching row", say="Formula two, FILTER. Give it a table and a condition, and it returns every row that matches. Not just the first one. All of them. The optional third argument is what to show if nothing matches.",
     vis=dict(type="args", title="#2  FILTER", fn="FILTER", args=[("array", "the rows you want back"), ("include", "the condition: TRUE or FALSE for each row"),
              ("if_empty", "what to show if nothing matches", True)], example='=FILTER(A2:E13, C2:C13="West", "No orders")', parts=["A2:E13", 'C2:C13="West"', '"No orders"'])),
dict(say="Click G2 and type equals FILTER, A2 colon E13, that's the whole table, comma, then C2 colon C13 equals West, in quotes. Press Enter. Five rows, every order from the West region, in the same order as the original table. And if you change a region in the table, this list updates by itself.",
     vis=dict(type="sheet", cells=table(HG), widths=W5, at="G2", formula='=FILTER(A2:E13,C2:C13="West")', ranges=["A2:E13", "C2:C13"],
              mark=rows_where(lambda r: r[2] == "West"), result=R["filter_west"])),
dict(say="Need two conditions? Put each one in brackets, and multiply them with a star. Region is West, and the amount is over one hundred. Each condition gives TRUE or FALSE for every row, and multiplying keeps only the rows where both are TRUE. So the star works like AND. Two orders left. For OR, use a plus sign instead.",
     vis=dict(type="sheet", cells=table(HG), widths=W5, at="G2", formula='=FILTER(A2:E13,(C2:C13="West")*(E2:E13>100))', ranges=["A2:E13", "C2:C13", "E2:E13"],
              mark=rows_where(lambda r: r[2] == "West" and r[4] > 100), result=R["filter_west_100"], note="*  means AND     +  means OR")),
dict(say="One thing to know. If nothing matches, and you skipped the third argument, FILTER shows a hash CALC error. Add a message, like No orders, as the third argument, and you get that text instead.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text='No match and no 3rd argument? FILTER shows #CALC!  Add "No orders" as the 3rd argument.', color=(108, 196, 255))),
# REENGAGE ~3:00
dict(chapter="The #SPILL! error (and the 2-second fix)", say="Now, the error that confuses almost everyone. You type the exact same formula, and instead of results, you get hash SPILL. Why? Look at the dashed box. That's where the results want to go. But cell H4 already has something in it. Excel refuses to overwrite your data, so it stops. The fix takes two seconds. Delete or move whatever is in the way, and the results spill right back.",
     vis=dict(type="sheet", cells=table({**HG, "H4": "note"}), widths=W5, at="G2", formula='=FILTER(A2:E13,C2:C13="West")', static=True, block="H4",
              error="#SPILL!", ghost="G2:K6", note="Something is in the way: clear H4", notecol=(255, 122, 89))),
# 3 UNIQUE
dict(chapter="#3 UNIQUE: remove duplicates", say="Formula three, UNIQUE. It gives you a list without duplicates. Click G2, and type equals UNIQUE, B2 colon B13. Twelve rows, but only five different reps. Ana, Ben, Cara, Dev and Eli, in the order they first appear. No more copying a column and clicking Remove Duplicates every single week.",
     vis=dict(type="sheet", cells=table({"G1": "Reps"}), widths=W2, at="G2", formula="=UNIQUE(B2:B13)", ranges=["B2:B13"], result=[[x] for x in R["unique_rep"]])),
# 4 SORT
dict(chapter="#4 SORT: order by any column", say="Formula four, SORT. Type equals SORT, then the table, then the number of the column to sort by, then the order. Five means the fifth column of the table, which is the amount. And minus one means largest first. Plus one would mean smallest first. Press Enter, and the biggest orders are on top. Your original table stays exactly as it was.",
     vis=dict(type="sheet", cells=table(HG), widths=W5, at="G2", formula="=SORT(A2:E13,5,-1)", ranges=["A2:E13"], result=R["sort_amount_desc"], note="5 = 5th column (Amount)   -1 = largest first")),
dict(say="And you can put one formula inside another. SORT of UNIQUE of the region column gives you an alphabetical list of regions. East, North, South, West. Perfect as the first column of a report.",
     vis=dict(type="sheet", cells=table({"G1": "Regions"}), widths=W2, at="G2", formula="=SORT(UNIQUE(C2:C13))", ranges=["C2:C13"], result=[[x] for x in R["sort_unique_region"]])),
# 5 SUMIFS
dict(chapter="#5 SUMIFS: totals with conditions", say="Formula five, SUMIFS. It adds up numbers, but only the ones that match your conditions. Careful with the order here. The column you want to add comes first. Then a column to check, and the value it must match. And you can keep adding more pairs of range and condition.",
     vis=dict(type="args", title="#5  SUMIFS", fn="SUMIFS", args=[("sum_range", "the numbers to add (comes first!)"), ("criteria_range1", "the column to check"),
              ("criteria1", "the value it must match"), ("criteria_range2, criteria2", "more pairs, if you need them", True)], example='=SUMIFS(E2:E13, B2:B13, "Ana")', parts=["E2:E13", "B2:B13", '"Ana"'])),
dict(say="Total sales for Ana. Equals SUMIFS, E2 colon E13, comma, B2 colon B13, comma, and Ana, in quotes. Twelve hundred, plus eighty, plus three hundred and ten. Fifteen ninety.",
     vis=dict(type="sheet", cells=table({"G1": "Rep", "H1": "Total", "G2": "Ana"}), widths=W2, at="H2", formula='=SUMIFS(E2:E13,B2:B13,"Ana")', ranges=["E2:E13", "B2:B13"],
              mark=rows_where(lambda r: r[1] == "Ana"), result=[[R["sumifs_ana"]]])),
dict(say="Two conditions? Just add another pair. Region is West, and product is Laptop. Only one order matches both, so the answer is eleven fifty.",
     vis=dict(type="sheet", cells=table({"G1": "West laptops"}), widths=W2, at="G2", formula='=SUMIFS(E2:E13,C2:C13,"West",D2:D13,"Laptop")', ranges=["E2:E13", "C2:C13", "D2:D13"],
              mark=rows_where(lambda r: r[2] == "West" and r[3] == "Laptop"), result=[[R["sumifs_west_laptop"]]])),
# REENGAGE ~6:00 bonus
dict(chapter="Bonus: a report that builds itself", say="Now, the bonus. The report from the start of the video. In G2, type equals UNIQUE of the rep column. Then in H2, type equals SUMIFS, the amount column, the rep column, and for the condition, G2 followed by a hash sign. G2 hash means the whole spilled list, however long it gets. Press Enter, and every rep gets a total. Add a new rep to the table tomorrow, and the report grows by itself.",
     vis=dict(type="sheet", cells=table({"G1": "Rep", "H1": "Total", **{f"G{i + 2}": r for i, (r, _) in enumerate(R["report"])}}), widths=W2,
              at="H2", formula="=SUMIFS(E2:E13,B2:B13,G2#)", ranges=["E2:E13", "B2:B13", "G2#"], result=[[x] for _, x in R["report"]], note="G2# = the whole spilled list in G")),
# 6 IFS
dict(chapter="#6 IFS: label rows with rules", say="Formula six, IFS. It checks conditions in order, and returns the result of the first one that's TRUE. Let's label every order. One thousand or more is Large. One hundred or more is Medium. And the last pair, TRUE comma Small, is a catch-all. TRUE is always true, so anything left over becomes Small.",
     vis=dict(type="args", title="#6  IFS", fn="IFS", args=[("logical_test1", "the first condition"), ("value_if_true1", "result if it's TRUE"), ("logical_test2, value2 ...", "the next pair, and so on"),
              ("TRUE, value", "catch-all for everything else", True)], example='=IFS(E2>=1000, "Large", E2>=100, "Medium", TRUE, "Small")', parts=["E2>=1000", '"Large"', 'E2>=100, "Medium"', 'TRUE, "Small"'])),
dict(say="Type it in F2, and press Enter. Then double click the small square in the corner of the cell, called the fill handle, to copy it all the way down. Large, Small, Medium. Every order labeled in a second.",
     vis=dict(type="sheet", cells=table({"F1": "Size"}), widths=[110, 95, 110, 130, 115, 120], at="F2", formula='=IFS(E2>=1000,"Large",E2>=100,"Medium",TRUE,"Small")', ranges=["E2"],
              result=[[x] for x in R["ifs"]], fill=True)),
dict(say="A very common mistake. If you check one hundred or more first, an order of twelve hundred stops right there, because twelve hundred is also more than one hundred. It gets labeled Medium, and Large never shows up at all. IFS stops at the first TRUE, so always test the biggest number first.",
     vis=dict(type="compare", title="The order of the conditions matters", left=("Wrong order", ["Checks >=100 first", "1200 becomes Medium", "Large never shows up"]),
              right=("Right order", ["Checks >=1000 first", "1200 becomes Large", "The first TRUE wins"]))),
# 7 TEXTSPLIT
dict(chapter="#7 TEXTSPLIT: split text into cells", say="Formula seven, TEXTSPLIT. You have full names in one column, and you need first and last names apart. In B2, type equals TEXTSPLIT, A2, comma, and a space in quotes. The space is the delimiter, the character to split on. Ana goes into B, Lopez spills into C. Copy it down, and the whole list is split.",
     vis=dict(type="sheet", cells={"A1": "Full name", "B1": "First", "C1": "Last", **{f"A{i + 2}": " ".join(n) for i, n in enumerate(R["textsplit_names"])}},
              widths=[220, 170, 170, 150, 150, 150, 150], rows=8, at="B2", formula='=TEXTSPLIT(A2," ")', ranges=["A2"], result=R["textsplit_names"], fill=True)),
dict(say="Want the pieces down a column instead? Leave the second argument empty, with two commas in a row, and put the delimiter third. That's the row delimiter. One cell with four products becomes four rows.",
     vis=dict(type="sheet", cells={"A1": "Products", "A2": "Laptop;Mouse;Monitor;Keyboard"}, widths=[420, 150, 150, 150, 150], rows=8, at="A4", formula='=TEXTSPLIT(A2,,";")',
              ranges=["A2"], result=[[x] for x in R["textsplit_rows"]])),
dict(say="Heads up. TEXTSPLIT always returns text, even when the pieces look like numbers. If you split something like ten comma twenty, and want to add the results, wrap it in VALUE first.",
     vis=dict(type="tip", tag="HEADS UP", text='TEXTSPLIT returns text, even "10" and "20". To do math, wrap it: =VALUE(TEXTSPLIT(A2,","))', color=(255, 211, 105))),
dict(chapter="Common errors", say="Quick troubleshooting. Hash NAME means Excel doesn't recognize the function. Either there's a typo, or your version of Excel is too old for it. Hash SPILL means something is blocking the results. Hash N A from XLOOKUP means no match, so add the fourth argument. And hash CALC from FILTER means nothing matched, so add the third one.",
     vis=dict(type="compare", title="Four errors, four fixes", left=("What you see", ["#NAME?", "#SPILL!", "#N/A from XLOOKUP", "#CALC! from FILTER"]),
              right=("The fix", ["Typo, or Excel too old", "Clear the cells in the way", "Add if_not_found", "Add if_empty"]))),
dict(chapter="Pro tip: turn your data into a Table", say="Pro tip. Click anywhere inside your data, and press Control T, to turn it into an Excel Table. Then, when you add new rows at the bottom, any formula that uses the table's column names includes them automatically. No more changing thirteen to fourteen in every formula.",
     vis=dict(type="keys", title="PRO TIP: turn your data into a Table", keys=["Ctrl", "T"], sub="New rows are included automatically in formulas that use the Table's column names")),
dict(chapter="Recap", say="Quick recap. XLOOKUP finds a value. FILTER returns every matching row. UNIQUE removes duplicates. SORT orders by any column. SUMIFS adds with conditions. IFS labels rows, biggest test first. And TEXTSPLIT breaks text apart. Seven formulas, and hours of manual work gone.",
     vis=dict(type="steps", title="Recap", items=["XLOOKUP: always add if_not_found", "FILTER: * for AND, + for OR", "UNIQUE: no more Remove Duplicates", "SORT: column number, -1 = largest first",
              "SUMIFS: the sum range comes first", "IFS: test the biggest number first", "TEXTSPLIT: returns text"])),
dict(say="Next on Shortcut Lab, we switch to AI, with five prompt techniques that actually work, so you get better answers from any chatbot on the first try. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Write Better AI Prompts: 5 Techniques That Actually Work")),
]
