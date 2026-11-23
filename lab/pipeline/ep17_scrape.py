# Shortcut Lab - EP17: Web Scraping with Python for Beginners (requests + BeautifulSoup -> CSV)
# AUTHENTICITY: the shop is a fictional practice site built by demo/ep17/make_site.py and served on this machine (python3 -m http.server 8000),
# so nobody else's website is scraped. Every script on screen is in demo/ep17/ and was run for real by demo/ep17/run_ep17.sh
# (Python 3.11, requests 2.34.2, beautifulsoup4 4.15.0, pandas 3.1.1); every terminal line is copied from demo/ep17/transcript.txt
# (long tracebacks shortened with "..."). The "scrape" scenes use REAL Chromium screenshots (demo/ep17/shoot.js: one with JavaScript on,
# one with JavaScript off) and the REAL bounding boxes Playwright measured for each selector (boxes.json); table rows are the real values.
# Syntax checked against the requests docs (get, timeout, raise_for_status, json), Beautiful Soup docs (html.parser, select, select_one,
# get_text(strip=True), tag["attr"]) and the Python docs (urllib.parse.urljoin, urllib.robotparser).
import os, json, csv
TITLE = "Web Scraping with Python for Beginners"
SPEED = 0.82
ACCENT = (240, 170, 60)  # honey (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta, EP12 cyan, EP13 jade, EP14 cobalt, EP15 citron, EP16 apricot)
SKY, YEL, MINT, CORAL, VIO, LIME = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255), (182, 243, 92)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep17")
def src(n): return open(os.path.join(D, n)).read().strip("\n")
TR = {}
for blk in open(os.path.join(D, "transcript.txt")).read().split("### ")[1:]:
    name, _, body = blk.partition("\n"); TR[name.strip()] = body.rstrip("\n").split("\n")
def out(name, cmd): return ["$ " + cmd] + TR[name]
def short_tb(name, cmd, pre=0):
    L = TR[name]; i = L.index("Traceback (most recent call last):"); return ["$ " + cmd] + L[:i][:pre] + [L[i], "  ...", L[-1]]
BX = json.load(open(os.path.join(D, "boxes.json")))
SHOT, SHOT2 = os.path.join(D, "shot_page1.png"), os.path.join(D, "shot_page1_nojs.png")
BOOKS = list(csv.DictReader(open(os.path.join(D, "books.csv"))))
P1 = BOOKS[:8]
HTML = open(os.path.join(D, "page1_card.html")).read().strip("\n").split("\n")
SCRAPER = src("scraper.py")
def SCR(sel, **kw): return dict(type="scrape", boxes=BX, shot=SHOT, sel=sel, **kw)

SCENES = [
dict(chapter="The result", say="This web page has twenty four books, spread over three pages. Copying them into a spreadsheet by hand would take half an hour. This Python script visits every page, reads every title, price and rating, and saves them all to a file, in about three seconds. Today you'll write it, from zero.",
     vis=SCR("article.book", rows=[[i + 1, b["title"], f"${float(b['price']):.2f}"] for i, b in enumerate(P1)], cols=["#", "title", "price"], note="24 books, 3 pages, about 3 seconds")),
dict(say="This is web scraping. A program that reads a web page the way you do, and copies out the parts you care about. Prices, lists, tables, anything you can see on a page. And I'll show you the three errors every beginner hits, with the real message on screen.",
     vis=dict(type="title", kicker="Python for beginners", text="Web Scraping with Python", sub="requests downloads  ·  BeautifulSoup finds  ·  pandas saves")),
dict(chapter="Scrape the right way", say="First, a quick word about doing this the right way. Only scrape public pages. Read the site's terms, and its robots dot t x t file, which we'll check later. Go slow, one page at a time. And never collect personal data. To keep things safe, every example today runs against a small practice shop I built, running on my own computer. That's why the address says localhost.",
     vis=dict(type="compare", title="Scrape the right way", left=("Don't", ["Log in and copy private data", "Hit a site hundreds of times a second", "Collect names, emails, phone numbers"]), right=("Do", ["Public pages only", "Check the terms and robots.txt", "Go slow: pause between pages"]))),
dict(chapter="The plan", say="Here's the plan. Download the page with requests. Turn the H T M L into something searchable with Beautiful Soup. Find the parts you want with C S S selectors. Loop over every page. And save everything to a C S V file you can open in Excel.",
     vis=dict(type="steps", title="The plan", items=["Download the page (requests)", "Parse the HTML (BeautifulSoup)", "Find the parts (CSS selectors)", "Loop over every page", "Save to CSV (pandas)"])),
dict(chapter="Setup", say="You need Python and three free libraries. In a terminal, type pip install requests beautiful soup four pandas. Requests downloads pages. Beautiful soup four, imported as b s four, reads the H T M L. And pandas saves the table. This prints the versions I'm using.",
     vis=dict(type="term", title="Terminal", lines=["$ pip install requests beautifulsoup4 pandas", "$ python versions.py"] + TR["versions"])),
dict(chapter="Step 1: download the page", say="Step one. Import requests. Put the address in a variable called url, and call requests dot get. Always add timeout equals ten, so your script never waits forever if a site doesn't answer. Then print three things. The status code, how long the text is, and the first characters of it.",
     vis=dict(type="code", code=src("get_page.py"), file="get_page.py", hl=(4,), cps=30)),
dict(say="Run it. Two hundred. That's the code for O K, the page arrived. Three thousand eight hundred and ten characters. And here's the start of it. That's the raw H T M L, the same text your browser receives, before it draws the page.",
     vis=dict(type="term", title="Terminal", lines=out("get_page", "python get_page.py"))),
dict(chapter="Step 2: read the HTML", say="But how do we find a price in all that text? Open the page in your browser, right click a book, and choose Inspect. The developer tools show the H T M L of that exact book. Every book is an article tag with the class book. Inside it, the title is in an h three with the class title. The price is a paragraph with the class price. And the rating has a data stars attribute. Those class names are our map.",
     vis=dict(type="scrape", mode="inspect", boxes=BX, shot=SHOT, sel="article.book", tag="article.book", src=HTML, hl=(1, 3, 5, 7), code="right-click a book > Inspect", label="FIND YOUR MAP")),
dict(say="Now Beautiful Soup. From b s four, import Beautiful Soup. Pass it the page text, and the name of the parser, h t m l dot parser, which comes with Python. The result is called soup, and it lets you ask questions. Soup dot title gives the page title. Soup dot find h two gives the first h two heading. And get text keeps just the words, without the tags.",
     vis=dict(type="code", code=src("soup_title.py"), file="soup_title.py", hl=(6, 8, 9), cps=30)),
dict(say="Run it. The page title, Pine Street Books, catalog page one. And the heading, all books, page one of three. Python can read the page.",
     vis=dict(type="term", title="Terminal", lines=out("soup_title", "python soup_title.py"))),
dict(chapter="Step 3: find every book", say="Step three, the important one. Soup dot select takes a C S S selector, and returns every element that matches. Article dot book means an article tag with the class book. Watch the real page. All eight books light up, one after the other. Python now has a list of eight boxes, one per book.",
     vis=SCR("article.book", rows=[[i + 1, b["title"]] for i, b in enumerate(P1)], cols=["#", "book"], panel="soup.select() returns", span=0.5)),
dict(say="Then we look inside each box. Select one returns the first match, only inside that book. Dot title for the title, dot price for the price. And get text with strip equals true removes the spaces and line breaks around the words. Without it, you get messy text full of blank space.",
     vis=dict(type="code", code=src("select_books.py"), file="select_books.py", hl=(8, 11, 12, 13), cps=34)),
dict(say="Here's the price selector, running on the real page, one book at a time. Each yellow outline is the element dot price, and on the right, the text Python pulled out of it.",
     vis=SCR("article.book", inner=".price", code='book.select_one(".price")', hilite=".price", rows=[[i + 1, b["title"], f"${float(b['price']):.2f}"] for i, b in enumerate(P1)], cols=["#", "title", "price"], span=0.55)),
dict(say="And the real output. Eight books found, and every title next to its price. That's a web scraper. Fifteen lines.",
     vis=dict(type="term", title="Terminal", lines=out("select_books", "python select_books.py"))),
dict(chapter="Mistake 1: NoneType has no get_text", say="Now mistake number one, and it's the most common error in web scraping. I typed dot prices, with an s, a class that doesn't exist. Run it. Attribute error. None type object has no attribute get text. Select one found nothing, so it returned None, and None has no text. When you see None type, check your selector. Copy the class name straight from Inspect.",
     vis=dict(type="term", title="Terminal - a typo in the selector", lines=["$ python bad_none.py", TR["bad_none"][0], "  ...", TR["bad_none"][2], TR["bad_none"][-1]])),
dict(chapter="Step 4: links, attributes and numbers", say="Step four. A table needs more than text. Here's one book. For the link, select the a tag inside the title. Get text gives its words. Square brackets with h r e f give the link address. But it's only half an address, it starts with a slash. Url join glues it to the page address, so you get a full link. Square brackets also read data stars, the rating. And for the price, strip the dollar sign and turn it into a float, a real number you can sort and add.",
     vis=dict(type="code", code=src("one_book.py"), file="one_book.py", hl=(9, 10, 11, 12, 13, 14), cps=34)),
dict(say="The real output. The title. The short link. The full link from url join. Two stars. And fourteen point nine nine, as a number, not text.",
     vis=dict(type="term", title="Terminal", lines=out("one_book", "python one_book.py"))),
dict(chapter="Mistake 2: the page that isn't there", say="Mistake number two. There are only three pages, but what if your loop asks for page four? Requests does not stop. It quietly returns status four oh four, not found, and your script carries on with an error page. The fix is one line. Raise for status. If the status is an error, it stops right there, and tells you exactly which address failed.",
     vis=dict(type="term", title="Terminal - asking for page 4", lines=["$ python bad_404.py", TR["bad_404"][0], TR["bad_404"][1], "  ...", TR["bad_404"][-1].split(" for url: ")[0], "    for url: " + TR["bad_404"][-1].split(" for url: ")[1]])),
dict(chapter="Mistake 3: data made by JavaScript", say="Mistake number three is the confusing one. In my browser, the bottom of the page shows three reviews. But Python finds zero, and the box just says, loading reviews. Why? The reviews are added by JavaScript, after the page loads. Your browser runs that JavaScript. Requests does not. It only gets the raw H T M L.",
     vis=dict(type="scrape", mode="nojs", boxes=BX, shot=SHOT, shot2=SHOT2, sel="#reviews .review", bcrop=(0.6, 1.0), bh=700, ring="#reviews", note="Browser: 3 reviews  ·  requests: 0", notecol=CORAL, notet=0.45)),
dict(say="Here's the proof. Zero reviews found, and the text is loading reviews. Nothing is broken. That data simply isn't in the file requests downloads.",
     vis=dict(type="term", title="Terminal - bad_js.py", lines=out("bad_js", "python bad_js.py"))),
dict(say="The fix? Open the developer tools again, and look at the Network tab while the page loads. You'll often find the data file the JavaScript downloads. Here it's reviews dot j s o n. Ask for that file directly, and dot j s o n turns it into a Python list. Three reviews, clean, no H T M L at all. If there's no such file, a browser tool like Playwright can run the JavaScript for you, but that's a topic for another day.",
     vis=dict(type="term", title="Terminal - reviews_json.py", lines=[src("reviews_json.py").split("\n")[3], "", "$ python reviews_json.py"] + TR["reviews_json"])),
dict(chapter="Step 5: every page", say="Step five, the full scraper. The address has a page number, so base is the address with curly braces, and format puts the number in. A for loop runs pages one to three. For each page, download, raise for status, and make the soup. Then, for every book, add a dictionary to the rows list. One key per column. Title, author, price, stars, in stock, and the full link.",
     vis=dict(type="code", code=SCRAPER, file="scraper.py", view=(6, 27), lh=36, size=24, hl=(10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24), cps=40)),
dict(say="Two details matter here. Time dot sleep one waits one second between pages. That's being polite, so you never flood a website. And at the end, pandas turns the list of rows into a table, a data frame, and to c s v saves it. Index equals false keeps pandas row numbers out of the file.",
     vis=dict(type="code", code=SCRAPER, file="scraper.py", view=(24, 31), hl=(27, 29, 30), cps=40)),
dict(say="Run it. Page one, eight books. Page two, sixteen. Page three, twenty four. Saved twenty four books to books dot c s v.",
     vis=dict(type="term", title="Terminal", lines=out("scraper", "python scraper.py"))),
dict(say="And here's the file. A header line, then one line per book. Title, author, price as a number, stars, true or false for in stock, and a full link. Double click it and it opens in Excel or Google Sheets.",
     vis=dict(type="term", title="Terminal - books.csv", lines=["$ head -4 books.csv"] + [ln if len(ln) < 86 else ln[:83] + "..." for ln in TR["head"]])),
dict(say="Here's the whole scrape on the real page one. Every book lights up, and its row lands in the table, with the price as a number and the stars from the data stars attribute. That's exactly what ended up in the file.",
     vis=SCR("article.book", inner=".rating", rows=[[i + 1, b["title"], b["price"], b["stars"]] for i, b in enumerate(P1)], cols=["#", "title", "price", "stars"], panel="rows in books.csv", span=0.6)),
dict(chapter="Use the data", say="Now the fun part. Your data is a real table. Read it back with pandas, keep the books with four stars or more that are in stock, and sort by price. Five cheap, well rated books, found in a second. And the average price, thirteen ninety five. Try doing that by scrolling through a website.",
     vis=dict(type="term", title="Terminal - analyze.py", lines=out("analyze", "python analyze.py")[:1] + TR["analyze"][5:])),
dict(chapter="If something goes wrong", say="If your scraper fails, it's usually one of these. None type has no attribute means a selector found nothing, so check the class name in Inspect. A four oh three or four oh four error means the page refused you, or doesn't exist. Read the error address. And if you get empty results while the browser shows data, that data comes from JavaScript, so look for the data file in the Network tab.",
     vis=dict(type="compare", title="Three common errors", left=("What you see", ["'NoneType' has no attribute 'get_text'", "HTTPError: 403 or 404", "Empty results, page looks full"]), right=("The fix", ["Copy the class name from Inspect", "Check the address and the terms", "Find the JSON in the Network tab"]))),
dict(chapter="Pro tip: check robots.txt in code", say="Pro tip. Python can check robots dot t x t for you. Robot file parser comes with Python. Give it the robots address and call read. Then can fetch tells you if a page is allowed. The catalog, true. The admin folder, false. And crawl delay says how many seconds to wait between pages. Here it's one, which is exactly what our sleep does.",
     vis=dict(type="term", title="Terminal - robots.py", lines=[src("robots.py").split("\n")[2], "", "$ python robots.py"] + TR["robots"])),
dict(chapter="How fast is it?", say="And the speed. Three pages, twenty four books, in three and a half seconds. And three of those seconds are the polite pauses we added on purpose. The work itself takes a blink.",
     vis=dict(type="term", title="Terminal - timing", lines=["$ time python scraper.py"] + TR["timing"])),
dict(chapter="Cheat sheet", say="Here's your cheat sheet. Requests dot get with a timeout. Raise for status. Beautiful Soup with the h t m l parser. Select for all matches, select one for the first. Get text with strip. Square brackets for attributes. Url join for links. Sleep between pages. And to c s v to save. Pause and screenshot it.",
     vis=dict(type="cards", title="Web scraping cheat sheet", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, VIO, CORAL, ACCENT, SKY, LIME],
              items=[["requests.get(url, timeout=10)", "Download a page"], ["r.raise_for_status()", "Stop on 404 / 403"], ["BeautifulSoup(...)", "Make it searchable"],
                     ['soup.select("article.book")', "Every match"], ['select_one(".price")', "First match inside"], ["get_text(strip=True)", "Clean text"],
                     ['tag["href"]', "Read an attribute"], ["urljoin(url, href)", "Full link"], ["time.sleep(1)", "Be polite"]])),
dict(chapter="Recap", say="Quick recap. Download the page with requests, with a timeout and raise for status. Make the soup. Find your map with Inspect. Select every item, and pull out text, attributes and numbers. Loop over the pages, slowly. Save it with pandas. And always scrape the right way.",
     vis=dict(type="steps", title="Recap", items=["requests.get() + raise_for_status()", "BeautifulSoup(html, \"html.parser\")", "Inspect to find the class names", "select(), select_one(), get_text(strip=True)", "Loop pages, sleep, save with to_csv()"])),
dict(say="Next on Shortcut Lab, we'll take the data you just scraped and send it somewhere useful, with an automatic email report written in Python. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Send an Automatic Email Report with Python", sub="New tutorials every Monday, Wednesday and Friday.")),
]
