# Shortcut Lab - EP06: Turn a spreadsheet into charts with Python (pandas + matplotlib)
# Every script below is in demo/ep06/ and was run for real (Python 3.11, pandas 3.1.1, matplotlib 3.11.2, openpyxl 3.1.5).
# Every terminal output is copied from demo/ep06/transcript.txt / err_openpyxl.txt, every chart is the PNG those scripts saved.
import os
TITLE = "Turn a Spreadsheet into Charts with Python"
SPEED = 0.82
ACCENT = (80, 220, 190)  # mint (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep06")
def src(n): return open(os.path.join(D, n)).read()
def png(n): return os.path.join(D, n)

DF_OUT = """   Month  Coffee   Tea  Cakes
0    Jan    1820   940    610
1    Feb    1750   910    650
2    Mar    1980   880    700
3    Apr    2100   760    720
4    May    2240   640    790
5    Jun    2050   520    830
6    Jul    1900   480    870
7    Aug    1950   500    860
8    Sep    2300   690    760
9    Oct    2480   850    740
10   Nov    2610   990    820
11   Dec    2950  1120   1040""".split("\n")

SCENES = [
dict(chapter="The result", say="This is a whole year of sales from a spreadsheet. And this dashboard was drawn by twenty lines of Python. No clicking through chart menus, no dragging ranges. Change the numbers in the spreadsheet, run the script again, and every chart updates in one second.",
     vis=dict(type="figure", img=png("dashboard.png"), win="dashboard.png", wipe=0.45, maxw=1560, note="20 lines of Python. Every chart, every time.")),
dict(say="In the next ten minutes, you'll go from a plain Excel file to a line chart, a bar chart, a pie chart and a full dashboard, saved as an image you can paste anywhere. Step by step, no experience needed. And I'll show you the three errors that stop almost every beginner, with the real error messages, and how to fix each one.",
     vis=dict(type="title", kicker="Python for beginners", text="Turn a Spreadsheet into Charts with Python", sub="pandas reads the data  ·  matplotlib draws the chart")),
dict(chapter="The plan", say="Here's the plan. First, install two free libraries. Then read the spreadsheet into Python. Then draw a line chart, and make it look professional. Then a bar chart and a pie chart. And finally, put everything into one dashboard and save it as a picture.",
     vis=dict(type="steps", title="The plan", items=["Install pandas and matplotlib", "Read the spreadsheet", "Line chart, then make it pro", "Bar chart and pie chart", "One dashboard, saved as an image"])),
dict(chapter="Why not just use Excel charts?", say="You might be thinking, Excel already makes charts. True. But every month you click through the same menus, select the same ranges, and fix the same titles, by hand. With Python, you write the steps once. Next month, you run one command, and every chart is rebuilt, exactly the same way, from the new numbers. And it works the same with ten rows, or ten thousand.",
     vis=dict(type="compare", title="Excel clicks vs. a Python script", left=("Clicking in Excel", ["Same menus every month", "Re-select ranges by hand", "Easy to miss a step"]),
              right=("One Python script", ["Write the steps once", "Run it again: all charts rebuilt", "10 rows or 10,000 rows"]))),
dict(chapter="Install the tools", say="You need Python installed. If you don't have it yet, get it free from python dot org. Then open a terminal and type pip install pandas matplotlib openpyxl. Pandas reads and organizes tables. Matplotlib draws the charts. And openpyxl is the small helper pandas uses to open Excel files. To check that everything worked, run this one line. It prints the versions. If you see numbers and no error, you're ready.",
     vis=dict(type="term", lines=["$ pip install pandas matplotlib openpyxl", "", "$ python3 -c \"import pandas, matplotlib; print(pandas.__version__, matplotlib.__version__)\"", "3.1.1 3.11.2"])),
dict(chapter="The practice spreadsheet", say="Here's our practice file, sales dot xlsx. A small café, twelve months, and three products. Coffee, tea and cakes. The first row has the column names. That matters, because pandas uses that first row as the names of the columns. Put the file in the same folder as your script.",
     vis=dict(type="term", title="sales.xlsx  (first row = column names)", lines=DF_OUT[:7] + ["..."])),
dict(chapter="Step 1: read the spreadsheet", say="Step one. Create a file called step one dot py. Import pandas, and give it the short name p d. Everybody does this, so you'll see it in every tutorial. Then read excel, with the file name in quotes. The whole sheet lands in a variable called d f, short for data frame. That's just pandas' word for a table. And print it.",
     vis=dict(type="code", file="step1.py", code=src("step1.py"), hl=(3,), note="DataFrame = a table inside Python")),
dict(say="Run it with python step one dot py. On a Mac, it's usually python three. And there's your spreadsheet, inside Python. Twelve rows. The numbers on the left are the row numbers pandas adds, starting at zero. Your data didn't change. It's just a label.",
     vis=dict(type="term", lines=["$ python3 step1.py"] + DF_OUT, out_gap=0.12)),
dict(say="Two quick variations. If your workbook has several tabs, add sheet name, with the name of the tab. And if your data is a CSV file, use read csv instead. Everything else in this video works exactly the same way. Print d f dot columns any time, to see the exact column names pandas found.",
     vis=dict(type="code", file="other_files.py", code=src("other_files.py"), hl=(3, 5), note="Same DataFrame, whatever the file type")),
dict(chapter="Step 2: your first line chart", say="Step two, your first chart. Import matplotlib dot pyplot as p l t. That's another name everyone uses. Read the file again. Then one line does the work. d f dot plot, x equals Month, y equals Coffee. The x is the horizontal axis, y is the values. Then plt dot savefig saves the picture to a file, and plt dot show opens it in a window.",
     vis=dict(type="code", file="line_chart.py", code=src("line_chart.py"), hl=(5,), note="x = across the bottom   y = the values")),
dict(say="Run it, and here it is. Coffee sales month by month. You can see the dip in the summer, and the big climb at the end of the year. That's something you'd never notice by staring at a column of numbers. It works, but it looks a bit plain. Let's fix that.",
     vis=dict(type="figure", img=png("line1.png"), win="Figure 1 - line1.png", maxh=760, callouts=[(0.12, 0.1, "y = Coffee"), (0.5, 0.9, "x = Month")])),
dict(chapter="Step 3: make it look professional", say="Step three. Five small changes. First, give y a list of columns, Coffee, Tea and Cakes, and you get three lines, with a legend for free. Marker equals o puts a dot on each month. Figsize sets the size in inches, ten wide and five tall. Then set title, and set y label. Tight layout stops the labels from getting cut off. And d p i equals one fifty makes the saved image sharp.",
     vis=dict(type="code", file="line_all.py", code=src("line_all.py"), hl=(5, 6, 7, 10), cps=44)),
dict(say="Run it again. Now that's a chart you can put in a report. Three products, a title, labeled axes, and dots on every month. And look at what it tells you. Tea sinks in the summer, cakes climb, and coffee takes off from September. Notice that matplotlib shows every other month on the bottom, so the labels don't crash into each other.",
     vis=dict(type="figure", img=png("line_all.png"), win="Figure 1 - line_all.png", callouts=[(0.5, 0.04, "set_title"), (0.04, 0.4, "set_ylabel")])),
dict(say="So where did the pictures go? Into the same folder as your script. List the folder, and there they are, line one dot png and line all dot png, ready to paste into an email, a slide, or a report. Want a P D F, for print? Just change the end of the file name to dot p d f, and savefig does the rest.",
     vis=dict(type="term", lines=["$ ls *.png", "line1.png  line_all.png", "", "# savefig picks the format from the name:", "# plt.savefig(\"line_all.pdf\")"])),
dict(chapter="Step 4: a bar chart of totals", say="Step four, a bar chart. First we need the total for each product. Pick the three columns, with two pairs of square brackets, and add dot sum. Pandas adds up every column for you. Then totals dot plot, kind equals bar. Color takes a list, one color per bar. Rot equals zero keeps the labels flat. And bar label writes the exact number on top of each bar.",
     vis=dict(type="code", file="bar_chart.py", code=src("bar_chart.py"), hl=(5, 8, 10), cps=44)),
dict(say="The print shows the real totals. Twenty six thousand one hundred thirty for coffee. Ninety two eighty for tea, and ninety three ninety for cakes. And the chart makes it obvious. Coffee sells almost three times more than anything else.",
     vis=dict(type="term", lines=["$ python3 bar_chart.py", "Coffee    26130", "Tea        9280", "Cakes      9390", "dtype: int64"])),
dict(say="Here's the picture. Three bars, the exact number on top of each one, and colors that match the products. This is the chart your boss actually reads.",
     vis=dict(type="figure", img=png("bar.png"), win="Figure 1 - bar.png", maxh=740, callouts=[(0.23, 0.08, "bar_label")])),
dict(chapter="Step 5: a pie chart", say="Step five, a pie chart. Same totals, but kind equals pie. Auto p c t adds the percentages. That little code, percent one point zero f, percent percent, just means a number with no decimals, then a percent sign. And set y label with empty quotes removes a leftover label on the side.",
     vis=dict(type="code", file="pie_chart.py", code=src("pie_chart.py"), hl=(6, 7))),
dict(say="Coffee is fifty eight percent of the year. Tea and cakes, twenty one percent each. One honest tip about pie charts. They only work with a few slices. With more than five or six, use a bar chart instead. It's much easier to compare.",
     vis=dict(type="figure", img=png("pie.png"), win="Figure 1 - pie.png", maxh=760, fade=True, wipe=0.25, note="More than 5 or 6 slices? Use a bar chart.")),
dict(chapter="Common errors", say="Now, the three errors that stop almost everyone. Error one. You run the script and get Import openpyxl failed. That means the Excel helper isn't installed. The fix is in the message itself. Run pip install openpyxl, and run your script again.",
     vis=dict(type="term", lines=["$ python3 step1.py", "Traceback (most recent call last):", "  ...", "ImportError: `Import openpyxl` failed.  Use pip, conda, or your", "preferred package management tool to install the openpyxl package.", "", "$ pip install openpyxl"])),
dict(say="Error two. File not found. Python looks for the file in the folder your terminal is in, not in the folder where you saved it in your head. Use c d to move the terminal into the folder with the script and the spreadsheet, and run it again.",
     vis=dict(type="term", lines=["$ python3 step1.py", "Traceback (most recent call last):", "  ...", "FileNotFoundError: [Errno 2] No such file or directory: 'sales.xlsx'", "", "# fix: move into the folder that has sales.xlsx", "$ cd my-charts"])),
dict(say="Error three. Key error, coffee. Look closely. I typed coffee with a small c, but the column is Coffee with a capital C. Column names must match the spreadsheet exactly. Capital letters, spaces, everything. Print d f dot columns, and copy the name from there.",
     vis=dict(type="term", lines=["$ python3 typo.py", "Traceback (most recent call last):", "  ...", "KeyError: 'coffee'", "", "# the column is 'Coffee' (capital C). Names must match exactly."])),
dict(say="And one more, that's not an error at all. If you run the script and no window appears, check that plt dot show is the last line. And always call savefig before show, never after. Once the window closes, the figure is gone, and you'd save a blank picture.",
     vis=dict(type="compare", title="No window? Blank image?", left=("Wrong", ["plt.show() is missing", "savefig after show", "Saved picture is blank"]),
              right=("Right", ["End with plt.show()", "savefig first, then show", "Picture saved, then shown"]))),
dict(chapter="Bonus: add a Total column", say="Quick bonus. Want the best month? Make a new column. d f, Total, equals the three columns, dot sum, axis equals one. Axis one means add across each row, instead of down each column. Then idx max finds the row with the biggest total.",
     vis=dict(type="code", file="total.py", code=src("total.py"), hl=(4, 5))),
dict(say="Run it. Every month now has a total, and the best month is December, with fifty one ten. Two lines of code, and you'd never have to scroll and compare by hand again.",
     vis=dict(type="term", lines=["$ python3 total.py", "   Month  Coffee   Tea  Cakes  Total", "9    Oct    2480   850    740   4070", "10   Nov    2610   990    820   4420", "11   Dec    2950  1120   1040   5110", "Best month: Dec 5110"])),
dict(chapter="Step 6: one dashboard, one image", say="Now, the dashboard from the start. plt dot subplots, one comma two, creates one figure with two empty charts side by side, ax one and ax two. Then the trick is ax equals. You tell each plot which space to draw in. The line chart goes into ax one. The bar chart goes into ax two. And one savefig saves the whole thing as one picture.",
     vis=dict(type="code", file="charts.py", code=src("charts.py"), hl=(8, 10, 14), lh=36, size=24, cps=50)),
dict(say="Run it, and the dashboard is saved. Monthly sales on the left, yearly totals on the right. Next month, paste the new numbers into the spreadsheet, run the same command, and the report is done. That's the real shortcut.",
     vis=dict(type="figure", img=png("dashboard.png"), win="Figure 1 - dashboard.png", maxw=1560, callouts=[(0.3, 0.55, "ax1"), (0.85, 0.5, "ax2", "r")], note="New data? Run it again. Done.")),
dict(chapter="Pro tip: one-word chart types", say="Pro tip. That word kind is all you change to try a different chart. Bar h gives you horizontal bars, great for long names. Area fills the space under the lines. Scatter compares two columns. Hist shows how values are spread out. Same data, same line of code, one word different.",
     vis=dict(type="steps", title="PRO TIP: change one word, get a new chart", items=['kind="line"   trends over time', 'kind="bar" / "barh"   compare totals', 'kind="pie"   share of a whole (few slices)', 'kind="area"   stacked trends', 'kind="scatter" / "hist"   relations and spread'])),
dict(chapter="Recap", say="Quick recap. Install pandas, matplotlib and openpyxl. Read the file with read excel. Draw with d f dot plot, x and y. Add a title and labels. Use sum for totals, and kind for the chart type. Save with savefig, before show. And subplots puts everything into one dashboard.",
     vis=dict(type="steps", title="Recap", items=["pip install pandas matplotlib openpyxl", "df = pd.read_excel(\"sales.xlsx\")", "df.plot(x=..., y=...) + set_title", "kind=\"bar\" / \"pie\" for other charts", "savefig before show, subplots for dashboards"])),
dict(say="Next on Shortcut Lab, the command line basics everyone should know. The ten commands that make the terminal feel easy, instead of scary. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Command Line Basics Everyone Should Know")),
]
