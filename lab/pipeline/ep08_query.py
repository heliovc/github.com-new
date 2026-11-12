# Shortcut Lab - EP08: Google Sheets QUERY: Automatic Reports in One Formula
# AUTHENTICITY: every result on screen comes from demo/ep08_results.json, produced by demo/ep08_compute.py, which runs the
# equivalent SQL in a real engine (sqlite3) on the same 12-row table, following Google's documented QUERY semantics.
# Syntax checked on support.google.com/docs/answer/3093343 (QUERY) and the Google Visualization API Query Language reference
# (clause order select/where/group by/pivot/order by/limit/offset/label/format/options; strings in single quotes; date 'yyyy-mm-dd';
# contains is case-sensitive; mixed-type columns: the majority type wins, the rest become null). Sample data: demo/ep08_sample.csv.
import os, json
TITLE = "Google Sheets QUERY: Automatic Reports in One Formula"
SPEED = 0.82
ACCENT = (255, 155, 50)  # orange (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink)
SKY, VIO, YEL, LIME, CORAL, MINT = (108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 122, 89), (80, 220, 190)
R = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep08_results.json")))
ROWS = R["rows"]; HDR = R["hdr"]

def table(extra=None):
    c = {f"{'ABCDE'[j]}1": h for j, h in enumerate(HDR)}
    for i, r in enumerate(ROWS):
        for j, val in enumerate(r): c[f"{'ABCDE'[j]}{i + 2}"] = val
    c.update(extra or {}); return c
def where(f): return [i + 2 for i, r in enumerate(ROWS) if f(r)]
def Q(q): return f'=QUERY(A1:E13,"{q}",1)'
BASE = [150, 82, 96, 118, 104, 30]
W3 = BASE + [92, 118, 104]
W2 = BASE + [110, 120]
W3W = BASE + [92, 150, 150]
W5 = BASE + [80, 80, 80, 80, 80]
def S(name, extra=None, widths=W3, at="G1", ranges=("A1:E13",), **kw):
    return dict(type="sheet", cells=table(extra), widths=widths, at=at, formula=Q(R["queries"][name]) if "formula" not in kw else kw.pop("formula"),
                ranges=list(ranges), result=R[name], cps=30, **kw)

SCENES = [
dict(chapter="The result", say="Twelve sales, four reps. Who sold the most? Instead of sorting, filtering and adding by hand, you type one formula, and Google Sheets builds the whole report. Every rep, every total, biggest first. And when a new sale comes in, the report updates itself.",
     vis=S("report", widths=W2, note="One formula. The whole report.")),
dict(say="That formula is called QUERY, and it's the most powerful function in Google Sheets. In the next few minutes you'll learn it from zero. Picking columns, filtering rows, sorting, totals, and even a pivot table, all in one formula. Around the middle, I'll show you the one rule that causes most QUERY errors.",
     vis=dict(type="title", kicker="Google Sheets for beginners", text="Google Sheets QUERY", sub="Automatic reports in one formula · select · where · order by · group by · pivot")),
dict(chapter="How QUERY works", say="QUERY takes three things. First, the data. That's your table, including the header row. Second, the query itself, written in double quotes. It's a short sentence in a simple language, that says which columns you want and which rows to keep. And third, the number of header rows, usually one. You can leave it out, but I always type it, so Sheets never has to guess.",
     vis=dict(type="args", title="The QUERY function", fn="QUERY", args=[("data", "your table, with the header row"), ("query", "what you want, in double quotes"), ("headers", "how many header rows (usually 1)", True)],
              example='=QUERY(A1:E13, "select B, D, E", 1)', parts=["A1:E13", '"select B, D, E"', "1"])),
dict(chapter="The practice table", say="Here's our practice table. Date in column A, the sales rep in B, the region in C, the product in D, and the amount in E. Twelve sales, rows two to thirteen. Type it in, or import any table you already have. And notice, QUERY talks about columns by their letters. A, B, C, D, E. Not by their names.",
     vis=dict(type="sheet", cells=table(), widths=BASE + [92, 118, 104], at="A1", note="Columns are called by their letters: A B C D E")),
# select
dict(chapter="select: pick your columns", say="Let's start. Click G1 and type equals QUERY, open bracket, A1 colon E13, comma. Then in double quotes, select B comma D comma E. Close the quotes, comma, one, close the bracket. Press Enter. You get just the rep, the product and the amount, with the headers on top. Three columns out of five, in any order you want.",
     vis=S("select")),
dict(say="Two things to notice. First, the whole result comes from one cell, G1. It spills down and to the right on its own. So keep that area empty, or you'll get an error. And second, select star means every column. That's the default. If you leave select out completely, you get the whole table.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="The result spills from one cell: keep the area below and to the right empty. select * = every column.", color=SKY)),
dict(say="And about that last argument, the one. It tells QUERY your first row is a header, not data. If you type zero by mistake, the word Amount is treated like a normal value, and your results can come back with blanks or a strange header. So when your table has one header row, always finish with comma one.",
     vis=dict(type="tip", tag="HEADERS", text="End with ,1 when row 1 holds the headers. With ,0 the header row is treated as data.", color=YEL)),
# where
dict(chapter="where: filter rows", say="Now the useful part. Filtering. Add where, then a condition. Where C equals West. And look carefully at the quotes. The whole query is in double quotes, so the text you're looking for, West, goes in single quotes. Press Enter, and you get only the three sales from the West region.",
     vis=S("west", mark=where(lambda r: r[2] == "West"))),
dict(say="Numbers are even easier. No quotes at all. Where E is greater than five hundred. Four sales, and they're all laptops. You can use equals, greater than, less than, and greater or less than or equal. Not equal is written as an exclamation mark and an equals sign.",
     vis=S("big", mark=where(lambda r: r[4] > 500))),
dict(say="To combine conditions, just use the words and, and or, the way you'd say it out loud. Where C equals East, and E is at least ninety. Two sales. With or, a row only needs one of the conditions to be true. Where D equals Mouse, or D equals Monitor. Five sales.",
     vis=S("mon_or", mark=where(lambda r: r[3] in ("Mouse", "Monitor")), note="and = both must be true     or = either one")),
dict(say="And for text, you're not limited to exact matches. Contains finds a piece of text anywhere in the cell. Where D contains top, in single quotes, finds every laptop. You also have starts with, and ends with. One catch. These are case sensitive. Top with a capital T would find nothing here.",
     vis=S("contains", mark=where(lambda r: "top" in r[3]))),
dict(say="Here's the quote rule as a picture, because it's the number one reason a QUERY breaks. Double quotes around the whole query. Single quotes around text. No quotes around numbers. Get this right, and most errors disappear.",
     vis=dict(type="cards", title="The quote rule", cols=3, span=0.55, colors=[ACCENT, SKY, YEL],
              items=[['"select ..."', "Double quotes around the whole query"], ["C = 'West'", "Single quotes around text"], ["E > 500", "No quotes around numbers"]])),
# order by + limit
dict(chapter="order by and limit: top 3", say="Next, sorting. Add order by, then a column. Order by E desc, short for descending, puts the biggest amounts first. Asc, or nothing, means smallest first. Then add limit three, and you keep only the first three rows. That's a top three list, in one line. The original table never moves.",
     vis=S("top3", note="desc = biggest first     limit 3 = keep 3 rows")),
# group by
dict(chapter="group by: totals in one line", say="Now the real magic. Group by. Select C, comma, sum of E, then group by C. QUERY puts all the sales from the same region together, and adds up their amounts. Four regions, four totals. And the result is sorted by region automatically. Look at the header it creates. Sum Amount. The function name, plus the original header.",
     vis=S("byregion", widths=W3W)),
dict(say="Sum is one of five functions you can use. Sum, count, average, written a v g, max and min. You can even use several at once. Select B, count of E, max of E, group by B. Every rep has three sales, and now you can see each one's biggest sale.",
     vis=S("countmax", widths=W3W)),
dict(say="Here's the one rule I promised. When you use group by, every column in select must be either inside a function, like sum or count, or listed after group by. If you select B and D, but only group by B, QUERY doesn't know which product to show for each rep, and it gives you an error. Fix it by grouping by both, or removing D.",
     vis=dict(type="compare", title="The group by rule", left=("Error", ["select B, D, sum(E)", "group by B", "D is not grouped"]), right=("Works", ["select B, sum(E)", "group by B", "Every column is grouped or summed"]))),
# funnel (re-engage)
dict(chapter="How QUERY reads your query", say="So how does QUERY actually think? Watch this query, step by step. It starts with all twelve sales. Where keeps only sales over one hundred. Seven left. Group by puts them together, one row per rep. Order by sorts the totals, biggest first. And limit two keeps the top two. Lena and Omar. Every clause does one small job, in this exact order.",
     vis=dict(type="funnel", title="One query, step by step", span=0.8, note="Each clause does one job, in this order",
              stages=[dict(clause="select B, sum(E)", label="All 12 sales", rows=R["funnel"]["all"], color=(200, 206, 216)),
                      dict(clause=" where E > 100", label="where", rows=R["funnel"]["where"], color=SKY),
                      dict(clause=" group by B", label="group by", rows=R["funnel"]["group"], color=YEL, hl=True),
                      dict(clause=" order by sum(E) desc", label="order by", rows=R["funnel"]["order"], color=MINT, hl=True),
                      dict(clause=" limit 2", label="limit", rows=R["funnel"]["limit"], color=ACCENT, hl=True)])),
dict(say="Here's that same query in the sheet. Select B, sum of E, where E is greater than one hundred, group by B, order by sum of E descending, limit two. Press Enter. Lena with sixteen hundred, and Omar with fourteen ninety. Exactly what the steps predicted. The small sales under one hundred were never counted.",
     vis=dict(type="sheet", cells=table(), widths=W3W, at="G1", formula=Q("select B, sum(E) where E > 100 group by B order by sum(E) desc limit 2"), ranges=["A1:E13"], cps=30,
              result=[["Rep", "sum Amount"]] + R["funnel"]["limit"], mark=where(lambda r: r[4] > 100))),
dict(say="And that order matters when you write it, too. The clauses must always come in this order. Select, where, group by, pivot, order by, limit, and label. You can skip any of them, but you can't shuffle them. Put order by before where, and you get a parse error.",
     vis=dict(type="steps", title="Always in this order", items=["select: which columns", "where: which rows", "group by: combine rows", "pivot: turn values into columns", "order by: sort", "limit: keep the first N rows", "label: rename headers"])),
# label = the hook report
dict(chapter="label: the full report", say="Last piece of the report from the start. Sum Amount is an ugly header. Add label, sum of E, and the new name in single quotes. Total. Now put it all together. Select B, sum of E, group by B, order by sum of E descending, label sum of E as Total. Every rep, every total, biggest first. Lena on top, with sixteen seventy.",
     vis=S("report", widths=W2, note="label sum(E) 'Total' renames the header")),
# pivot
dict(chapter="pivot: a pivot table in one formula", say="Want a pivot table, without the pivot table menu? Add pivot, and a column. Select B, sum of E, group by B, pivot C. Now each rep is a row, each region becomes its own column, and every cell is a total. Empty cells mean that rep had no sales in that region. Lena sold sixteen hundred in the North.",
     vis=S("pivot", widths=W5, note="pivot C = one column per region")),
# dates
dict(chapter="Filter by date", say="Dates trip up almost everyone. You can't just type the date in quotes. You write the word date, then the date in single quotes, as year, month, day, with dashes. Always that format, no matter how dates look in your country. Where A is greater than or equal to date, twenty twenty six, eleven, oh one. Every sale from November, seven of them.",
     vis=S("nov", mark=where(lambda r: r[0] >= "2026-11-01"), note="date 'yyyy-mm-dd' : always this format")),
dict(say="One more thing you'll run into. If your data isn't a normal range, for example two tabs stacked together inside curly brackets, the letters stop working. Then you call the columns Col1, Col2, Col3, with a capital C, in the order they appear. Everything else stays exactly the same.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="Data in curly brackets, like {Jan!A2:E; Feb!A2:E}? Use Col1, Col2, Col3... instead of A, B, C.", color=SKY)),
# dynamic cell
dict(chapter="Bonus: a report you control from a cell", say="Bonus. Make the report change from a cell. Type a rep's name in H1, Lena. Then, inside the query, close the double quotes, add an ampersand, H1, another ampersand, and open the double quotes again. Keep the single quotes around it, because it's text. Now change H1 to Omar, and the report changes by itself. Add a dropdown to H1 from the Insert menu, and anyone can use it.",
     vis=S("lena", extra={"G1": "Rep:", "H1": "Lena"}, widths=W2, at="G3", ranges=("A1:E13", "H1"), formula=f'''=QUERY(A1:E13,"select D, E where B = '"&H1&"'",1)''',
           mark=where(lambda r: r[1] == "Lena"), note="'\"&H1&\"'  puts the text from H1 into the query")),
# errors
dict(chapter="Common errors", say="Now the errors. Unable to parse query string means the query itself has a mistake. Usually a missing single quote, a comma in the wrong place, or the clauses in the wrong order. No column means you used a letter outside your data, like G, when the data is only A to E. And if the result shows hash REF, something is sitting where the results want to spill. Clear it.",
     vis=dict(type="compare", title="3 errors, 3 fixes", left=("You see", ["Unable to parse query string", "NO_COLUMN: G", "#REF! (array result was not expanded)"]),
              right=("The fix", ["Check quotes, commas, clause order", "Use only columns inside your data", "Clear the cells in the way"]))),
dict(say="And the sneakiest problem of all. No error, just missing values. If a column mixes numbers and text, like a few amounts typed as N A, QUERY treats the whole column as whichever type is most common, and the rest come back empty. Keep one kind of data per column.",
     vis=dict(type="tip", tag="SNEAKY", text="A column with numbers AND text? QUERY keeps the most common type and returns the others as blank cells.", color=CORAL)),
# pro tip
dict(chapter="Pro tip: a report that grows by itself", say="Pro tip. Instead of A1 colon E13, use A colon E, the whole columns. Then every new sale you add at the bottom is included automatically. Add where B is not null, so the empty rows below your data are skipped. Now your report really does update itself, forever.",
     vis=dict(type="tip", tag="PRO TIP", text="Use A:E instead of A1:E13, and add where B is not null. New rows join the report automatically.", color=MINT)),
dict(chapter="Recap", say="Quick recap. QUERY takes the data, the query in double quotes, and the header count. Select picks columns. Where filters rows, with single quotes around text. Order by and limit make top lists. Group by with sum or count makes totals. Label renames headers. And pivot turns values into columns. Pause and screenshot this cheat sheet.",
     vis=dict(type="cards", title="QUERY cheat sheet", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, VIO, LIME, ACCENT, SKY, CORAL],
              items=[["select B, E", "Pick columns by letter"], ["where C = 'West'", "Text in single quotes"], ["where E > 500", "Numbers: no quotes"],
                     ["contains 'top'", "Part of the text (case sensitive)"], ["order by E desc", "Sort, biggest first"], ["limit 3", "Keep the first 3 rows"],
                     ["sum(E) group by B", "One total per rep"], ["pivot C", "One column per value"], ["A >= date '2026-11-01'", "Dates: yyyy-mm-dd"]])),
dict(say="Next on Shortcut Lab, we build your first web page, with HTML and CSS, in fifteen minutes. No experience needed. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Build Your First Web Page in 15 Minutes (HTML + CSS)")),
]
