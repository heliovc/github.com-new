# Shortcut Lab - EP09: Build Your First Web Page in 15 Minutes (HTML + CSS)
# AUTHENTICITY: every file typed on screen is in demo/ep09/ (step1.html, step2.html, index.html, style.css and its partial versions),
# and every browser picture is a REAL Chromium screenshot of exactly that file, made by demo/ep09/shoot.js (Playwright, headless Chromium).
# The two error scenes are real too: err_path.html (href="styles.css") and err_brace.css (one missing "}").
# Syntax checked against MDN (HTML elements, CSS rules, flexbox, media queries, viewport meta). DevTools shortcut from developer.chrome.com.
# The avatar picture is drawn by code (no third-party media).
import os
TITLE = "Build Your First Web Page in 15 Minutes (HTML + CSS)"
SPEED = 0.82
ACCENT = (125, 140, 255)  # periwinkle (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange)
SKY, VIO, YEL, LIME, CORAL, MINT = (108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 122, 89), (80, 220, 190)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep09")
def src(n): return open(os.path.join(D, n)).read()
def shot(n): return os.path.join(D, f"shot_{n}.png")
HTML1, HTML2, HTML, ERRH = src("step1.html"), src("step2.html"), src("index.html"), src("err_path.html")
CSS1, CSSA, CSSB, CSSC, CSS, ERRC = src("style1.css"), src("style_a.css"), src("style_b.css"), src("style_c.css"), src("style.css"), src("err_brace.css")
def LV(code, sh, **kw): return dict(type="live", code=code, shot=shot(sh), **kw)
def CS(code, sh, **kw): return dict(type="live", code=code, shot=shot(sh), lang="css", file="style.css", **kw)

SCENES = [
dict(chapter="The result", say="This is a real web page. A profile card, a round photo, a button that changes color when you point at it, and three cards that stack up neatly on a phone. And it's made from just two small text files. In the next fifteen minutes, you'll build it yourself, line by line, from an empty folder.",
     vis=LV(HTML, "s4", typed=False, note="Two text files. One real web page.")),
dict(say="No experience needed, and nothing to buy. You need a text editor and a web browser, and you already have a browser. By the end, you'll understand what every line does. And I'll show you the two mistakes that break almost every beginner's first page, with the real result on screen.",
     vis=dict(type="title", kicker="Web basics for beginners", text="Build Your First Web Page", sub="HTML for the content  ·  CSS for the looks  ·  15 minutes")),
dict(chapter="The plan", say="Here's the plan. First, make a folder and an empty file. Then write the HTML, that's the content. Open it in the browser. Then add CSS, that's the style. Make a button and cards. And finally, make it work on a phone.",
     vis=dict(type="steps", title="The plan", items=["Make a folder and index.html", "Write the content with HTML", "Open it in your browser", "Style it with CSS: button and cards", "Make it work on a phone"])),
dict(chapter="HTML vs CSS", say="Two languages, two jobs. HTML says what is on the page. A heading, a paragraph, a picture, a link. CSS says how it looks. Colors, fonts, spacing, rounded corners. Think of HTML as the walls of a house, and CSS as the paint and the furniture. You'll keep them in two separate files.",
     vis=dict(type="compare", title="Two files, two jobs", left=("index.html = content", ["Headings and paragraphs", "Pictures and links", "What is on the page"]),
              right=("style.css = looks", ["Colors and fonts", "Spacing and corners", "How the page looks"]))),
dict(chapter="Create the file", say="Make a new folder anywhere, and call it my site. Open a plain text editor. I recommend VS Code, it's free, but Notepad works too. Create a new file and save it inside that folder as index dot html. That exact name matters. Browsers and web servers look for index dot html first, as the home page.",
     vis=dict(type="steps", title="Create the file", items=["New folder: my-site", "Open VS Code (free) or Notepad", "New file, then Save As...", "Name it: index.html", "Save it inside my-site"])),
dict(say="One trap, especially on Windows. Notepad can secretly save your file as index dot html dot t x t. Then the browser shows your code as plain text. In the Save As window, set the type to All files. And turn on file name extensions in File Explorer, so you always see the real name.",
     vis=dict(type="tip", tag="WATCH OUT", text="index.html.txt is NOT a web page. In Notepad choose 'All files', and show file extensions in File Explorer.", color=CORAL)),
dict(chapter="Your first HTML", say="Now type this. The first line, doctype html, tells the browser this is a modern web page. Then the html tag wraps everything. Inside, the head holds information about the page, like the character set and the title on the browser tab. And the body holds everything you actually see. A big heading with h1, and a paragraph with p.",
     vis=LV(HTML1, "s1", cps=34, note="head = info about the page     body = what you see")),
dict(say="Notice the pattern. Almost every tag comes in a pair. An opening tag, like h1, and a closing tag with a slash, slash h1. The text goes between them. The pair together is called an element. And elements go inside other elements, like boxes inside boxes. That's why I indent them, so you can see which box is inside which.",
     vis=dict(type="cards", title="The tags you'll use today", cols=3, span=0.6, colors=[ACCENT, SKY, YEL, MINT, VIO, CORAL],
              items=[["<h1> </h1>", "Big heading (h2 = smaller)"], ["<p> </p>", "Paragraph of text"], ["<ul> <li>", "List and list items"],
                     ["<a href=...>", "Link: href = where it goes"], ["<img src=...>", "Picture: no closing tag"], ["<div> </div>", "A box to group things"]])),
dict(chapter="Open it in the browser", say="Save the file. Then go to your folder and double click index dot html. It opens in your browser. Look at the tab. It says Sam Rivera, from the title tag. And on the page, the heading and the paragraph. No styling yet, just the browser's plain default look. That's normal. You just made a web page.",
     vis=LV(HTML1, "s1", typed=False, note="Double-click index.html to open it", url="file:///C:/Users/you/my-site/index.html")),
dict(chapter="Add a list and a link", say="Let's add more content. Below the paragraph, an h2, a smaller heading, What I do. Then u l, an unordered list, with three l i items inside. And a link. The a tag, with an attribute called h ref. That's where the link goes. Here it opens an email. Save with Control S, or Command S on a Mac, and refresh the browser with F5. There's the list, and the blue link.",
     vis=LV(HTML2, "s2", prev=shot("s1"), **{"from": 10}, hl=(11, 12, 13, 14, 15, 16, 18), cps=34)),
dict(say="This is your work loop for the rest of the video. Change the file, save, refresh the browser. Every time. If something doesn't change on screen, nine times out of ten you just forgot to save, or forgot to refresh.",
     vis=dict(type="tip", tag="THE LOOP", text="Edit, save (Ctrl+S / Cmd+S), refresh the browser (F5 / Cmd+R). Nothing changed? You forgot one of them.", color=SKY)),
dict(chapter="Give it structure", say="Now the final HTML. We wrap the top part in a header with a class called hero. A class is a name we'll use later, in the CSS. We add a picture with the img tag. Src is the file name, and alt describes the picture for people using screen readers. The link gets the class button. And the list becomes three divs, each with the class card.",
     vis=LV(HTML, "s3a", prev=shot("s2"), **{"from": 10}, hl=(11, 12, 15, 16, 19, 20, 21, 22, 23), cps=48)),
dict(say="Refresh, and, honestly, it looks the same as before, plus a square picture. That's expected. Classes don't do anything by themselves. They're just labels. The magic happens when CSS finds those labels and styles them. So let's write some CSS.",
     vis=LV(HTML, "s3a", typed=False, view=(9, 24), note="Classes are just labels. CSS uses them.")),
dict(chapter="Connect the CSS", say="Two steps. First, in the head of the HTML, this link line. Rel equals stylesheet, h ref equals style dot css. It tells the browser where your style file is. Second, create a new file called style dot css, in the same folder, right next to index dot html. Those two names must match exactly, letter for letter.",
     vis=LV(HTML, "s3a", typed=False, view=(0, 9), hl=(8,), note="href must match the file name exactly")),
dict(say="Every CSS rule has the same shape. A selector, which says what to style. Then curly brackets. Inside, property, colon, value, semicolon. One per line. So body, open curly bracket, background colon, a color code, semicolon, close curly bracket. That's all of CSS, repeated.",
     vis=dict(type="cards", title="The shape of a CSS rule", cols=3, span=0.55, colors=[CORAL, SKY, YEL],
              items=[["body { ... }", "Selector: what to style"], ["background:", "Property: what to change"], ["#f4f1ea;", "Value, then a semicolon"]])),
dict(chapter="Style the page", say="Our first rule styles the body, the whole page. A clean font, Arial. A warm background color. Dark text. Then max width, eight hundred pixels, and margin zero auto. Together, those two keep the page in a neat column, centered in the middle of the screen. And padding adds some breathing room. Save, refresh. Already better.",
     vis=CS(CSS1, "s3", prev=shot("s3a"), cps=34, note="max-width + margin: 0 auto = centered column")),
dict(chapter="Classes: the hero card", say="Now we use the class names. To select a class in CSS, start with a dot. Dot hero. White background, rounded corners with border radius, padding inside, and everything centered. Then dot hero space img, which means only images inside the hero. Border radius fifty percent turns the square picture into a circle.",
     vis=CS(CSSA, "s4a", prev=shot("s3"), **{"from": 9}, hl=(10, 11, 12, 13, 14, 15, 17, 18, 19), cps=34, note=".name = a class     .hero img = images inside .hero")),
dict(chapter="A real button", say="Next, the button. Remember, it's really just a link with the class button. Display inline block lets it have padding like a box. An orange background, white text, padding, a huge border radius for the pill shape, and text decoration none removes the underline. Then dot button colon hover. That's the style only while the mouse is over it. A darker orange.",
     vis=CS(CSSB, "s4b", prev=shot("s4a"), view=(16, 32), **{"from": 20}, hl=(21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32), cps=34)),
dict(say="Here's the hover, for real. When I point at the button, it turns darker. No JavaScript, just one small CSS rule. That tiny change makes a page feel alive, and it tells people this thing is clickable.",
     vis=CS(CSSB, "s4_hover", typed=False, view=(16, 32), hl=(30, 31, 32), note=":hover = only while the mouse is on it")),
dict(chapter="Cards side by side with flexbox", say="Now the cards. Dot cards is the box around all three. Display flex puts the boxes inside it side by side, in a row. Gap adds sixteen pixels between them. Then each dot card gets flex one, so they share the width equally, plus a white background, rounded corners and padding. Save, refresh, and there's the page from the start.",
     vis=CS(CSSC, "s4", prev=shot("s4b"), view=(20, 44), **{"from": 13}, hl=(34, 35, 36, 37, 39, 40, 41, 42, 43, 44), cps=34)),
dict(say="Flexbox is worth remembering. Display flex on the parent box, and its children line up in a row. Flex one on each child, and they share the space equally. Gap sets the space between them. That one idea builds menus, toolbars and card grids all over the web.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="display: flex on the parent = children in a row. flex: 1 on each child = equal widths. gap = space between.", color=MINT)),
dict(chapter="Make it work on a phone", say="Now, phones. Here's the same page on a narrow screen. The three cards are squeezed into tiny columns. Ugly, and hard to read. Two fixes. First, the viewport line in the head, which tells phones to use their real screen width instead of pretending to be a desktop.",
     vis=LV(HTML, "s4c_mobile", typed=False, view=(0, 9), hl=(5, 6), phone=True, url="my-site/index.html", note="390 pixels wide: the cards are squeezed")),
dict(say="Second, a media query. At max width six hundred pixels, which means on screens six hundred pixels wide or less, the cards switch to flex direction column. They stack, one under the other. Save, refresh, and now it looks like it was made for the phone. On a big screen, nothing changes.",
     vis=CS(CSS, "s4_mobile", prev=shot("s4c_mobile"), view=(32, 50), **{"from": 45}, hl=(46, 47, 48, 49, 50), phone=True, url="my-site/index.html", cps=30)),
dict(chapter="Common mistakes", say="Now the two mistakes I promised. Mistake one. Your CSS is ignored completely, and the page looks plain again. Here, the link says styles dot css, with an s, but the file is called style dot css. One letter. The browser can't find the file, so it silently skips all of your styles. No error message.",
     vis=LV(ERRH, "e1", typed=False, view=(0, 13), hl=(8,), notecol=CORAL, note="styles.css is not style.css: all styles ignored")),
dict(say="Mistake two. Half of your styles work, and the rest are just gone. Here, one closing curly bracket is missing, after the round picture rule. Now the picture is still a circle, but look at the button. It's a plain blue link again. The browser thinks the button rule is inside the broken rule, and it throws it away. Always close every curly bracket.",
     vis=CS(ERRC, "e2", typed=False, view=(8, 30), hl=(17, 18), notecol=CORAL, note="One missing } breaks the rule after it")),
dict(say="Three more you'll meet. Text in the wrong place, because a closing tag is missing. A broken picture icon, because the image file name or folder doesn't match. And changes that don't show up, because you forgot to save, or refresh.",
     vis=dict(type="compare", title="3 more problems, 3 fixes", left=("You see", ["Text in the wrong place", "Broken picture icon", "Nothing changes"]),
              right=("The fix", ["Check every closing tag", "Check the img src file name", "Save, then refresh (F5)"]))),
dict(chapter="Pro tip: DevTools", say="Pro tip. Right click anything on your page and choose Inspect. Or press F12, or Control Shift I, or Command Option I on a Mac. These are the developer tools, built into every browser. Click an element, and you see exactly which CSS rules apply to it. You can even change a color right there, and watch it update live. When you like it, copy it into your file.",
     vis=dict(type="keys", title="Open the developer tools", keys=["Ctrl", "Shift", "I"], sub="Mac: Cmd + Option + I   ·   or F12   ·   or right-click, Inspect")),
dict(chapter="Recap", say="Quick recap. HTML is the content, CSS is the looks. Every page starts with the same skeleton. Tags come in pairs. Classes are labels, and CSS selects them with a dot. Flexbox puts boxes in a row. A media query fixes phones. And edit, save, refresh, every time. Pause and screenshot this cheat sheet.",
     vis=dict(type="cards", title="HTML + CSS cheat sheet", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, VIO, LIME, ACCENT, SKY, CORAL],
              items=[["<h1> <p> <a> <img>", "Heading, text, link, picture"], ['class="card"', "A label for CSS"], ['<link href="style.css">', "Connect the CSS file"],
                     ["prop: value;", "Inside { } in every rule"], [".card { }", "Dot = select a class"], ["border-radius: 50%", "Square to circle"],
                     [".button:hover", "Style on mouse-over"], ["display: flex", "Children side by side"], ["@media (max-width:600px)", "Rules for small screens"]])),
dict(say="Your page lives on your computer for now. Next on Shortcut Lab, we go back to Python, and pull the text and the tables out of P D F files automatically. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Extract Text and Tables from PDFs with Python")),
]
