# Shortcut Lab - EP11: Regex for Beginners: Find Anything in Text (Python re module)
# AUTHENTICITY: every script on screen is in demo/ep11/ and was run for real (Python 3.11.18, built-in re module); every terminal output
# is copied from demo/ep11/transcript.txt / err_paren.txt. inbox.txt is fictional (555 numbers, made-up shops). The "rx" scenes run
# re.finditer / re.sub on the same text at render time, so every highlighted match is a real match.
import os
TITLE = "Regex for Beginners: Find Anything in Text"
SPEED = 0.82
ACCENT = (230, 90, 230)  # magenta (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby)
SKY, YEL, MINT, CORAL, VIO = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep11")
def src(n): return open(os.path.join(D, n)).read()
INBOX = src("inbox.txt").rstrip("\n").split("\n")
TR = src("transcript.txt")
def out(name): return TR.split(f"### {name}\n")[1].split("###")[0].rstrip("\n").split("\n")
def fold(ln, n=72):  # long printed list wrapped like a narrow terminal (same text, only line breaks added)
    res = []
    while len(ln) > n: k = ln.rfind(" ", 0, n); res.append(ln[:k]); ln = ln[k + 1:]
    return res + [ln]
EMAIL = r"[\w.+-]+@[\w-]+\.\w+"; PHONE = r"\d{3}-\d{3}-\d{4}"; DATE = r"(\d{4})-(\d{2})-(\d{2})"

SCENES = [
dict(chapter="The result", say="This is a messy inbox. Names, order numbers, dates, phone numbers, all mixed together. Now watch. One short pattern, and Python found every email address in it. Not by searching for one email, but by describing what any email looks like. That pattern is called a regular expression. And by the end of this video, you'll write it yourself.",
     vis=dict(type="rx", pattern=EMAIL, text=INBOX, span=0.55, note="One pattern, every email address")),
dict(say="Regex sounds scary. It looks like a cat walked across the keyboard. But it's built from a handful of small pieces, and once you know them, you can find phone numbers, dates, codes, anything with a shape, in seconds. Step by step, from zero.",
     vis=dict(type="title", kicker="Python for beginners", text="Regex for Beginners: Find Anything in Text", sub="built into Python  ·  nothing to install")),
dict(chapter="Find vs. regex", say="Here's the big idea. Normal find, the Control F you already know, looks for exact text. Type five five five, and it finds five five five. A regular expression looks for a shape. Three digits, a dash, three digits, a dash, four digits. It doesn't care which digits. That's what makes it so powerful.",
     vis=dict(type="compare", title="Ctrl+F vs. a regular expression", left=("Normal find", ["Looks for exact text", "\"555-201-7788\" finds one number", "You must know what you want"]),
              right=("Regular expression", ["Looks for a shape", "\\d{3}-\\d{3}-\\d{4} finds them all", "You only describe the pattern"]))),
dict(chapter="The plan", say="Here's the plan. Learn the basic building blocks. Find every phone number. Find every email. Pull dates apart into day, month and year. Hide sensitive numbers automatically. And check if a code is valid. Then the three mistakes everyone makes, so you don't.",
     vis=dict(type="steps", title="The plan", items=["Building blocks: \\d  +  {3}", "Find every phone number and email", "Groups: split a date into parts", "re.sub: hide numbers automatically", "fullmatch: is this code valid?"])),
dict(chapter="Setup", say="All you need is Python. Regex lives in a module called r e, and it comes built in, so there's nothing to install. Make a folder, and put a text file in it called inbox dot t x t. You can use any text you like, or copy mine from the description. Then check your Python version in a terminal.",
     vis=dict(type="term", lines=["$ python3 --version", "Python 3.11.18", "$ ls", "inbox.txt  step1.py"])),
dict(chapter="Step 1: your first pattern", say="Create step one dot py. Import r e. Then read the whole file into a variable called text. Now, re dot findall takes two things. A pattern, and the text to search. It returns a list with every match. First pattern, the plain word Invoice. Then, backslash d plus. Notice the little r before the quotes. That's a raw string, and it matters. I'll show you why later.",
     vis=dict(type="code", file="step1.py", code=src("step1.py"), hl=(5, 6), note="re.findall(pattern, text) = a list of every match")),
dict(say="Run it. The plain word finds exactly one match, Invoice. But backslash d plus found every number in the file. Order numbers, years, months, phone number pieces. Seventeen of them. We never told it which numbers. We just said, digits.",
     vis=dict(type="term", lines=["$ python3 step1.py"] + [x for l in out("step1") for x in fold(l)], out_gap=0.3)),
dict(say="Let's slow down and see why. Backslash d means one digit, any digit from zero to nine. And plus means one or more of the thing before it. So together, a run of digits, as long as it goes. Watch it light up every number in the text.",
     vis=dict(type="rx", pattern=r"\d+", text=INBOX, parts=[(r"\d", "any digit 0-9", SKY), ("+", "one or more", YEL)], span=0.75)),
dict(chapter="The building blocks", say="Here are the building blocks you'll use ninety percent of the time. Backslash d, a digit. Backslash w, a word character, letters, digits, or underscore. Backslash s, a space. A dot means any character at all. Plus is one or more, star is zero or more, and question mark makes something optional. Curly braces with a number mean exactly that many. And square brackets mean any one of the characters inside.",
     vis=dict(type="cards", title="The regex building blocks", cols=3, span=0.75, colors=[SKY, YEL, MINT, CORAL, ACCENT, VIO],
              items=[["\\d", "A digit, 0 to 9"], ["\\w", "Letter, digit or _"], ["\\s", "A space, tab or newline"], [".", "Any character"], ["+", "One or more"], ["*", "Zero or more"],
                     ["?", "Optional (0 or 1)"], ["{3}", "Exactly 3 times"], ["[abc]", "One of a, b or c"]])),
dict(chapter="Step 2: find phone numbers", say="Step two. Phone numbers. Our numbers look like five five five, dash, two oh one, dash, seven seven eight eight. So let's describe that shape. Backslash d, curly three, means exactly three digits. Then a dash, which is just a normal character. Three more digits, another dash, and four digits.",
     vis=dict(type="rx", pattern=PHONE, text=INBOX, parts=[(r"\d{3}", "3 digits", SKY), ("-", "a dash", YEL), (r"\d{3}", "3 digits", SKY), ("-", "a dash", YEL), (r"\d{4}", "4 digits", MINT)], span=0.75)),
dict(say="In code, it's the same findall. Put the pattern in, and save the list in a variable called phones. Then print the list, and its length, with len.",
     vis=dict(type="code", file="phones.py", code=src("phones.py"), hl=(5,))),
dict(say="Run it. Three phone numbers, and nothing else. Not the order number, not the dates. The dates have dashes too, but they have four digits first, so they don't fit the shape. That's the precision you get with a pattern.",
     vis=dict(type="term", lines=["$ python3 phones.py"] + out("phones"), out_gap=0.3)),
dict(chapter="Step 3: find email addresses", say="Step three. Emails, the pattern from the start. Let's build it piece by piece. First, the name before the at sign. Square brackets with backslash w, dot, plus and dash mean, any one of these characters. The plus after the bracket means one or more of them. Then the at sign. Then the domain name, word characters or dashes. Then backslash dot, a real dot. And finally the ending, like com or org.",
     vis=dict(type="rx", pattern=EMAIL, text=INBOX, parts=[(r"[\w.+-]+", "the name", SKY), ("@", "the @ sign", YEL), (r"[\w-]+", "the domain", MINT), (r"\.", "a real dot", CORAL), (r"\w+", "the ending", VIO)], span=0.78)),
dict(say="Why backslash dot, and not just a dot? Because, remember, a plain dot means any character. Backslash in front turns a special character back into a normal one. That's called escaping. In the code, we loop over the list and print one email per line.",
     vis=dict(type="code", file="emails.py", code=src("emails.py"), hl=(5,))),
dict(say="Run it. All three emails. Notice the tricky ones. Tom's uses an underscore, and a dot cafe ending. Dana's has a plus sign in the name. The pattern handles both, because we listed those characters in the square brackets.",
     vis=dict(type="term", lines=["$ python3 emails.py"] + out("emails"), out_gap=0.35)),
dict(chapter="Step 4: groups", say="Step four, groups. Our dates are written year, month, day. But say you want day, slash, month, slash, year. Put round brackets around each part of the pattern. Each pair of brackets is a group. Python finds the whole date, and also remembers each group separately. Watch the colored lines under each match. Blue for the year, yellow for the month, green for the day.",
     vis=dict(type="rx", pattern=DATE, text=INBOX, parts=[(r"(\d{4})", "group 1: year", SKY), ("-", "dash", (200, 206, 216)), (r"(\d{2})", "group 2: month", YEL), ("-", "dash", (200, 206, 216)), (r"(\d{2})", "group 3: day", MINT)], span=0.75)),
dict(say="When a pattern has groups, findall gives you the groups instead of the whole match. One small tuple per date, with year, month and day. So we can unpack them right in the for loop, and print them in any order we like.",
     vis=dict(type="code", file="dates.py", code=src("dates.py"), hl=(5, 6))),
dict(say="Run it. Third of October, and twentieth of November. Same dates, new format. This is how you clean up dates from a hundred different files in one go.",
     vis=dict(type="term", lines=["$ python3 dates.py"] + out("dates"), out_gap=0.4)),
dict(chapter="Step 5: hide numbers with re.sub", say="Step five. Finding is great, but you can also replace. Say you want to share this inbox, but hide the phone numbers. re dot sub finds every match and swaps it for something else. Watch. Every phone number lights up, and then gets replaced. Only the last four digits survive.",
     vis=dict(type="rx", pattern=r"\d{3}-\d{3}-(\d{4})", text=INBOX, sub=r"XXX-XXX-\1", subshow="XXX-XXX-", sublabel="re.sub() replaced 3", span=0.55, label="PATTERN  ·  replace with XXX-XXX-\\1")),
dict(say="Here's the trick. We put round brackets around the last four digits, making them group one. In the replacement, backslash one means, put group one back here. So XXX dash XXX dash, and then the real last four digits. Both strings start with r, raw strings, because both use backslashes.",
     vis=dict(type="code", file="hide.py", code=src("hide.py"), hl=(5,), note="\\1 in the replacement = whatever group 1 matched")),
dict(say="Run it. The whole inbox, and every phone number is masked. The emails, dates and order numbers are untouched. Imagine doing this by hand across a thousand customer messages.",
     vis=dict(type="term", lines=["$ python3 hide.py"] + out("hide")[:-1], out_gap=0.2)),
dict(chapter="Step 6: is this code valid?", say="Step six. Checking input. Say product codes must be two capital letters, a dash, and four digits. Square brackets, A dash Z, means any capital letter, and curly two means two of them. The key is re dot fullmatch. It only says yes if the whole string fits the pattern, from the first character to the last.",
     vis=dict(type="code", file="check.py", code=src("check.py"), hl=(6,))),
dict(say="Run it. A B dash one two three four is valid. Lowercase fails, because we asked for capital letters. Five digits fails. And an extra letter in front fails too. With re dot search instead, those last two would sneak through, because search is happy to find the pattern anywhere inside the text.",
     vis=dict(type="term", lines=["$ python3 check.py"] + out("check"), out_gap=0.35)),
dict(chapter="Mistake 1: greedy matches", say="Now, the three mistakes everyone makes. Mistake one. You want each word inside angle brackets. So you write, less than, dot star, greater than. But it grabs everything from the first bracket to the very last one, as one big match. Dot star is greedy. It eats as much as it can.",
     vis=dict(type="rx", pattern=r"<.*>", text=["Colors: <red> and <blue>"], file="greedy.py", parts=[("<", "a <", YEL), (".*", "anything, as MUCH as possible", CORAL), (">", "a >", YEL)], span=0.6, size=40)),
dict(say="The fix is one question mark. Dot star question mark is lazy. It stops at the first closing bracket it can. Now we get two clean matches, red and blue.",
     vis=dict(type="rx", pattern=r"<.*?>", text=["Colors: <red> and <blue>"], file="greedy.py", parts=[("<", "a <", YEL), (".*?", "anything, as LITTLE as possible", MINT), (">", "a >", YEL)], span=0.6, size=40, note="Add ? after * or + to make it lazy")),
dict(chapter="Mistake 2: forgetting the r", say="Mistake two. Forgetting the r. Backslash b means a word boundary, the edge of a word. Without the r, Python turns backslash b into a special invisible character before regex ever sees it. So you get an empty list, and no error. With the r, it finds cat. Just always write the r. It never hurts.",
     vis=dict(type="term", lines=["$ cat raw.py"] + src("raw.py").rstrip("\n").split("\n") + ["$ python3 raw.py"] + out("raw"), out_gap=0.3)),
dict(chapter="Mistake 3: the dot and brackets", say="Mistake three. The unescaped dot. A dot in your pattern matches any character, so this date pattern also matched two oh two six x ten x oh three. Escape it with a backslash when you mean a real dot. And if you ever see re dot error, missing closing bracket, you opened a round bracket and forgot to close it. Count your brackets.",
     vis=dict(type="term", lines=["$ python3 dot.py"] + out("dot") + ["", "$ python3 typo.py", "  ..."] + src("err_paren.txt").rstrip("\n").split("\n")[-1:], out_gap=0.3)),
dict(chapter="Pro tip: ignore upper and lower case", say="Pro tip. Regex is case sensitive. Search for invoice with a small i, and you get nothing, because the text says Invoice with a capital. Add re dot IGNORECASE as a third argument, and it matches any mix of upper and lower case.",
     vis=dict(type="term", lines=["$ python3 ignore.py"] + out("ignore"), out_gap=0.4)),
dict(say="And one more. Most code editors, and many text editors, let you search with regex too. Look for a dot star button in the search box. Turn it on, and every pattern from today works there, no Python needed. It's the fastest way to practice.",
     vis=dict(type="tip", tag="PRO TIP", text="Test a new pattern on a few lines first. Most code editors have a .* button in Find that turns on regex search.", color=ACCENT)),
dict(chapter="Recap", say="Quick recap. Import r e. Use findall to get every match. Backslash d for digits, backslash w for word characters, plus for one or more, and curly braces for an exact count. Round brackets make groups. re dot sub replaces, and fullmatch checks a whole string. And always use raw strings.",
     vis=dict(type="steps", title="Recap", items=["import re  ·  re.findall(r\"pattern\", text)", "\\d digit  ·  \\w word  ·  +  one or more  ·  {3} exactly", "( ) groups split a match into parts", "re.sub() replaces  ·  re.fullmatch() validates", "Lazy .*?  ·  escape the dot  ·  always use r\"\""])),
dict(say="Next on Shortcut Lab, make a Python script run automatically, every single day, without you touching it. On Windows and on Mac. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Run a Python Script Automatically Every Day")),
]
