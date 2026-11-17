# Shortcut Lab - EP13: VS Code Shortcuts That Save Hours
# AUTHENTICITY: every key binding was checked against VS Code's own source (microsoft/vscode main: linesOperations.ts, multicursor.ts,
# comment.ts, rename.ts, coreCommands.ts, quickAccess/gotoLine/terminal contributions, preferences.contribution.ts) and the official docs
# (vscode-docs: codebasics.md, default-keybindings.md). Ctrl+D from an empty cursor = whole word + match case; from a hand-made selection
# it follows the Find options (default: no match case, no whole word) - that is the "mistake" scene. The "vsc" scenes run the edit
# engine at render time; demo/ep13/run_ep13.py writes the final files of each scene and really runs them with Python 3; every terminal
# line comes verbatim from demo/ep13/transcript.txt.
import os, sys
TITLE = "VS Code Shortcuts That Save Hours"
SPEED = 0.82
ACCENT = (70, 225, 120)  # jade (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta, EP12 cyan)
SKY, YEL, MINT, CORAL, VIO = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep13")
TRP = os.path.join(D, "transcript.txt")
TR = open(TRP).read() if os.path.exists(TRP) else ""
def T(name): return TR.split(f"### {name}\n")[1].split("###")[0].rstrip("\n").split("\n") if f"### {name}\n" in TR else ["$ (pending)"]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tutor import vsc_final

CART = '''prices = {
    "apple": 1.20,
    "bread": 2.50,
    "milk": 0.99,
}
tax = 0.08

total = sum(prices.values())
print("Total:", round(total * (1 + tax), 2))
print("Subtotal:", round(total, 2))
print("DEBUG", prices)
'''
LIST = '''apple
bread
milk
eggs
coffee
'''
REPORT = '''# calc: quantity times price
def calc(qty, price):
    return qty * price

orders = [("apple", 3, 1.20), ("milk", 2, 0.99)]
print("calc for each order:")
for name, qty, price in orders:
    print(name, calc(qty, price))
'''
FILES = ["cart.py", "list.py", "report.py", "notes.txt"]
def K(keys, mac, name, *do, **kw): return dict(keys=keys, mac=mac, name=name, do=list(do), **kw)
TYPE = lambda s, name="Just type": K("Type", "Type", name, ("type", s))
CD = lambda name="Add next match": K("Ctrl+D", "Cmd+D", name, ("next",))
CDL = lambda name="Add next match": K("Ctrl+D", "Cmd+D", name, ("next", "loose"))  # selection made by hand: default Find options

V_LIST = dict(type="vsc", file="list.py", code=LIST, car=[(1, 0, 0)], ops=[
    K("Ctrl+Alt+Down", "Cmd+Option+Down", "Add cursor below", ("below",)), K("Ctrl+Alt+Down", "Cmd+Option+Down", "Add cursor below", ("below",)),
    K("Ctrl+Alt+Down", "Cmd+Option+Down", "Add cursor below", ("below",)), K("Ctrl+Alt+Down", "Cmd+Option+Down", "Add cursor below", ("below",)),
    TYPE('    "', "Type on 5 lines at once"), K("End", "Cmd+Right", "Jump to end of line", ("end",)), TYPE('",', "Type on 5 lines at once"),
    K("Esc", "Esc", "Back to one cursor", ("esc",)),
    K("Ctrl+Shift+Enter", "Cmd+Shift+Enter", "Insert line above", ("above_line",)), K("Backspace", "Delete", "Remove the indent", ("bs",)), TYPE("items = ["),
    K("Ctrl+G", "Ctrl+G", "Go to line", ("goto", 6)), K("End", "Cmd+Right", "Jump to end of line", ("end",)),
    K("Ctrl+Enter", "Cmd+Enter", "Insert line below", ("below_line",)), K("Backspace", "Delete", "Remove the indent", ("bs",)), TYPE("]"),
    K("Ctrl+Enter", "Cmd+Enter", "Insert line below", ("below_line",)), TYPE('print(len(items), "items:", ", ".join(items))'),
], span=0.86)
V_HOOK = dict(V_LIST, ops=V_LIST["ops"][:7], span=0.8)

V_QUICK = dict(type="vsc", file="cart.py", code=CART, car=[(1, 0, 0)], ops=[
    K("Ctrl+B", "Cmd+B", "Show / hide the sidebar", ("side", FILES)),
    K("Ctrl+P", "Cmd+P", "Quick Open a file", ("palette", "", "rep", FILES), ("open", "report.py", REPORT)),
    K("Ctrl+B", "Cmd+B", "Show / hide the sidebar", ("side", FILES)),
], span=0.8)
V_GOTO = dict(type="vsc", file="report.py", code=REPORT, car=[(1, 0, 0)], ops=[
    K("Ctrl+G", "Ctrl+G", "Go to line", ("goto", 8)), K("End", "Cmd+Right", "Jump to end of line", ("end",)),
    K("Ctrl+`", "Ctrl+`", "Open the terminal", ("term", ["(filled below)"])),
], span=0.75)

# cart.py line edits (scene by scene, each starts from the previous result)
V_MOVE = dict(type="vsc", file="cart.py", code=CART, car=[(10, 0, 0)], ops=[K("Alt+Up", "Option+Up", "Move line up", ("mvu",))], span=0.55, delay=1.2)
V_COPY = dict(type="vsc", file="cart.py", code=vsc_final(V_MOVE), car=[(4, 5, 5)], ops=[
    K("Shift+Alt+Down", "Shift+Option+Down", "Copy line down", ("cpd",)), K("Ctrl+D", "Cmd+D", "Select the word", ("word",)), TYPE("eggs"),
    K("Click", "Click", "Click before the price", ("cur", 5, 12), mouse=(5, 12)), K("Shift+End", "Shift+Cmd+Right", "Select to end of line", ("selend",)), TYPE("3.10,"),
], span=0.85)
V_CMT = dict(type="vsc", file="cart.py", code=vsc_final(V_COPY), car=[(12, 0, 0)], ops=[
    K("Ctrl+/", "Cmd+/", "Comment the line", ("cmt",)), K("Ctrl+/", "Cmd+/", "Uncomment it", ("cmt",)),
    K("Ctrl+Shift+K", "Cmd+Shift+K", "Delete the whole line", ("del",)),
], span=0.8)
CART2 = vsc_final(V_CMT)
V_D = dict(type="vsc", file="cart.py", code=CART2, car=[(9, 2, 2)], ops=[
    K("Ctrl+D", "Cmd+D", "Select the word", ("word",)), CD(), CD(), TYPE("subtotal", "Type once: 3 edits"),
], span=0.85)
V_LOOSE = dict(type="vsc", file="cart.py", code=CART2, car=[(9, 0, 5)], ops=[
    CDL(), CDL(), CDL(), CDL(),
], span=0.8, delay=1.0, hud="THE MISTAKE")
V_UP = dict(type="vsc", file="cart.py", code=vsc_final(V_D), car=[(7, 1, 1)], ops=[
    K("Ctrl+D", "Cmd+D", "Select the word", ("word",)), K("Ctrl+Shift+L", "Cmd+Shift+L", "Select ALL matches", ("all",)),
    K("Ctrl+Shift+P", "Cmd+Shift+P", "Command Palette", ("palette", ">", "upper", ["Transform to Uppercase", "Transform to Lowercase", "Transform to Title Case",
      "View: Toggle Word Wrap", "View: Toggle Zen Mode", "Preferences: Open Keyboard Shortcuts", "Preferences: Color Theme", "Format Document"]), ("upper",)),
], span=0.8)
CART3 = vsc_final(V_UP)
V_F2 = dict(type="vsc", file="report.py", code=REPORT, car=[(2, 5, 5)], ops=[K("F2", "F2", "Rename Symbol", ("rename", "line_total"))], span=0.6, delay=1.0)

SCENES = [
dict(chapter="The result", say="Five words. In five seconds, they become a real Python list. No copy and paste, no typing the same thing five times. One cursor became five, and I typed once. In this video, you'll learn the V S Code shortcuts that do this kind of thing every day, and save you hours.",
     vis=V_HOOK),
dict(say="Every shortcut here is shown for Windows and Linux, and for Mac, side by side. And every result you see, I ran for real. Let's go.",
     vis=dict(type="title", kicker="VS Code for beginners", text="VS Code Shortcuts That Save Hours", sub="Windows / Linux and Mac keys side by side")),
dict(chapter="Why shortcuts matter", say="Here's the difference. With the mouse, you scroll to find a file, you drag to select, and you fix the same word in five places, one at a time. With the keyboard, you jump straight to any file or line, you move whole lines with one key, and you edit many places at once.",
     vis=dict(type="compare", title="Mouse vs. keyboard", left=("With the mouse", ["Scroll and hunt for files", "Drag to select, then retype", "Fix the same word 5 times"]),
              right=("With shortcuts", ["Jump to any file or line", "Move and copy whole lines", "Edit many places at once"]))),
dict(chapter="The plan", say="Here's the plan. First, moving around: files, lines, the sidebar and the terminal. Then editing whole lines. Then the real superpower, multiple cursors. Then the rename shortcut, the mistake that trips up almost everyone, and a few pro tips.",
     vis=dict(type="steps", title="The plan", items=["Move around: files, lines, panels", "Edit whole lines without selecting", "Multiple cursors", "Rename safely with F2", "The common mistake + pro tips"])),
dict(chapter="Ctrl vs Cmd", say="One quick rule before we start. On a Mac, Control usually becomes Command, and Alt becomes Option. I'll show both on the right side of the screen every time. And on Linux, a couple of shortcuts are different, I'll point those out.",
     vis=dict(type="cards", title="Windows / Linux  vs  Mac", cols=2, span=0.6, colors=[ACCENT, SKY, ACCENT, SKY],
              items=[["Ctrl", "Windows and Linux"], ["Cmd", "Mac"], ["Alt", "Windows and Linux"], ["Option", "Mac"]])),
dict(chapter="Ctrl+P: open any file", say="Shortcut one. Control B shows or hides the sidebar, the file list on the left. Hide it, and your code gets the whole screen. Now, Control P, P for project. It's quick open. Type a few letters of any file name, like r e p, and the list filters as you type. Press Enter, and report dot py opens. No scrolling, no clicking through folders. Control B again, and the sidebar is gone.",
     vis=V_QUICK),
dict(chapter="Ctrl+G and the terminal", say="Shortcut two. Control G, go to line. When an error says line eight, type eight and press Enter. You land right there. On a Mac, it's Control G too. And shortcut three. Control and the backtick key, the one under Escape. It opens the terminal right inside V S Code. Here I run python three report dot py, and see the output, without leaving the editor.",
     vis=V_GOTO),
dict(chapter="Ctrl+Shift+P: the Command Palette", say="Shortcut four is the most important one. Control Shift P opens the Command Palette. Every single feature in V S Code is in there. Can't remember a shortcut? Press this, type what you want, like word wrap, or color theme, and press Enter. Even better, the list shows the shortcut next to each command, so you learn them as you go.",
     vis=dict(type="keys", title="The Command Palette", keys=["Ctrl", "Shift", "P"], sub="Mac: Cmd + Shift + P   ·   also F1   ·   every feature, searchable")),
dict(chapter="Move a line: Alt+Up/Down", say="Now let's edit. Here's a small shopping cart script. The subtotal should be printed before the total. Don't cut and paste. Put your cursor anywhere on the line, and press Alt and the up arrow. The whole line moves up. On a Mac, Option up.",
     vis=V_MOVE),
dict(chapter="Copy a line: Shift+Alt+Down", say="Need one more item? Put the cursor on the milk line, and press Shift, Alt, down arrow. The line is copied right below. Control D selects the word under the cursor, so I type eggs. Then I click before the price, and Shift End selects to the end of the line. Type the new price. Done, without retyping the whole line. On Linux, copy line is Control Shift Alt down.",
     vis=V_COPY),
dict(chapter="Comment and delete lines", say="This debug line prints the whole dictionary. Control slash comments it out, so Python skips it. Press it again, and it's back. This is perfect for testing things. And when you're sure you don't need it, Control Shift K deletes the whole line. No selecting first.",
     vis=V_CMT),
dict(say="Two bonus moves that need no selection at all. With nothing selected, Control C copies the whole line, and Control X cuts the whole line. Then paste it anywhere with Control V. It's the fastest way to move a line a long distance, when Alt and the arrows would take too many presses.",
     vis=dict(type="tip", tag="BONUS", text="Nothing selected? Ctrl+C copies the whole line and Ctrl+X cuts it. Mac: Cmd+C, Cmd+X.", color=SKY)),
dict(say="Let's run it. Subtotal seven seventy nine, then the total with tax, eight forty one. The eggs are in, and the debug line is gone. Four quick shortcuts, and the mouse never moved.",
     vis=dict(type="term", title="Terminal — shortcuts", lines=T("cart2"), out_gap=0.4)),
dict(chapter="Multiple cursors: Ctrl+D", say="Now the superpower. I want to rename the variable total, to subtotal. Put the cursor inside the word, and press Control D. It selects the word. Press Control D again, and it adds the next match. And again. Three cursors. Now type once, and all three change together. Look closely. The word Total inside the text, and Subtotal, were not touched. That's because we started with just a cursor.",
     vis=V_D),
dict(chapter="The mistake: selecting by hand first", say="And this is the mistake that trips up almost everyone. If you first select the word by hand, with the mouse or Shift and the arrows, Control D works differently. It now ignores upper and lower case, and it matches inside other words too. Watch. It grabs Total, inside the text. And total, inside Subtotal. Type now, and you'd break your output. The fix is simple. Press Escape, click once inside the word with no selection, and then press Control D.",
     vis=V_LOOSE),
dict(chapter="Ctrl+Shift+L: all matches at once", say="When a word appears twenty times, pressing Control D twenty times is slow. Select it once with Control D, then press Control Shift L. Every match gets a cursor, all at once. Now I'll use the Command Palette. Control Shift P, type upper, and choose Transform to Uppercase. Tax becomes a capital TAX, in both places. In Python, capitals are the usual style for a constant.",
     vis=V_UP),
dict(say="Same result as before, so nothing broke. Subtotal seven seventy nine, total eight forty one. Renaming with multiple cursors is safe, as long as you start from a plain cursor.",
     vis=dict(type="term", title="Terminal — shortcuts", lines=T("cart3"), out_gap=0.4)),
dict(chapter="Cursor below: Ctrl+Alt+Down", say="Now, the trick from the start of the video. A plain list of words. Press Control Alt down arrow four times. On a Mac, Command Option down. Now there are five cursors, one per line. Type four spaces and a quote. Press End, to jump every cursor to the end of its own line, even though the lines have different lengths. Type a quote and a comma. Escape goes back to one cursor.",
     vis=dict(V_LIST, ops=V_LIST["ops"][:8], span=0.85)),
dict(say="To finish, Control Shift Enter adds a new line above. It keeps the indent, so one Backspace removes it. I type items equals, open bracket. Control G, line six, and End. Control Enter adds a line below, without breaking the current one. Backspace removes the indent, close the bracket. One more Control Enter, and a print line. Let's run it.",
     vis=dict(V_LIST, code=vsc_final(dict(V_LIST, ops=V_LIST["ops"][:8])), car=[(1, 0, 0)], ops=V_LIST["ops"][8:], span=0.88)),
dict(say="Five items. Apple, bread, milk, eggs, coffee. A real Python list, built in seconds. And on Linux, add cursor below is Shift Alt down instead.",
     vis=dict(type="term", title="Terminal — shortcuts", lines=T("list"), out_gap=0.4)),
dict(chapter="Rename safely: F2", say="Renaming a function is different. Its name can also appear in comments, and in text. Put the cursor on the name and press F2. Type the new name, line total, and press Enter. V S Code renames the function and every call to it. But the comment on line one and the text on line six stay the same, because they're not code. This needs the Python extension, and it works the same on Mac.",
     vis=V_F2),
dict(say="And it still runs. Milk, one point nine eight. And apple shows three point five nine nine, with lots of nines. That's not the rename. It's how computers store decimal numbers. Wrap it in round, if you want a clean three point six.",
     vis=dict(type="term", title="Terminal — shortcuts", lines=T("report2"), out_gap=0.4)),
dict(chapter="Other common mistakes", say="Two more problems beginners hit. First, a shortcut does nothing, or does something else. Your operating system, or another app, may use the same keys. Open the Keyboard Shortcuts editor, search the command, and pick new keys. Second, a different keyboard layout. The backtick key isn't in the same place on every keyboard. If Control backtick doesn't open the terminal, use the Command Palette, and search for terminal.",
     vis=dict(type="compare", title="When a shortcut doesn't work", left=("Does nothing", ["The system or another app", "uses the same keys", "Fix: pick new keys for it"]),
              right=("Different keyboard", ["The ` key moves around", "Ctrl+` may not match", "Fix: Ctrl+Shift+P, \"terminal\""]))),
dict(chapter="Cheat sheet", say="Here's your cheat sheet. Control P to open files. Control Shift P for every command. Control G to go to a line. Alt up and down to move lines. Shift Alt down to copy a line. Control slash to comment. Control Shift K to delete a line. Control D and Control Shift L for multiple cursors. And F2 to rename. Pause the video, and take a screenshot.",
     vis=dict(type="cards", title="VS Code cheat sheet (Mac: Ctrl = Cmd, Alt = Option)", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, CORAL, VIO, ACCENT, SKY, YEL],
              items=[["Ctrl+P", "Open any file"], ["Ctrl+Shift+P", "Every command"], ["Ctrl+G", "Go to line (Mac: Ctrl+G)"],
                     ["Alt+Up / Down", "Move the line"], ["Shift+Alt+Down", "Copy the line"], ["Ctrl+/", "Comment / uncomment"],
                     ["Ctrl+Shift+K", "Delete the line"], ["Ctrl+D  ·  Ctrl+Shift+L", "Next match  ·  all matches"], ["F2", "Rename a symbol"]])),
dict(chapter="Pro tips", say="Pro tip one. Shift Alt right arrow expands the selection. Press it again, and it grows from the word, to the text, to the whole line. On a Mac, it's Control Shift Command right. Pro tip two. Alt and click, Option click on a Mac, adds a cursor anywhere you click. Great when the places you want to edit aren't in a column.",
     vis=dict(type="tip", tag="PRO TIP", text="Shift+Alt+Right grows the selection step by step. Alt+Click adds a cursor anywhere you click.", color=ACCENT)),
dict(say="Pro tip three. Control K, then Control S, opens the Keyboard Shortcuts editor. Search any command, and you'll see its shortcut. You can even change it. And don't try to learn everything today. Pick two shortcuts this week, use them until they're automatic, then add two more.",
     vis=dict(type="keys", title="See and change every shortcut", keys=["Ctrl", "K", "Ctrl", "S"], sub="Mac: Cmd+K, then Cmd+S   ·   learn 2 shortcuts a week")),
dict(chapter="How to make them stick", say="Here's how to make these stick. This week, use only two. Control P to open files, and Alt up and down to move lines. Next week, add Control D and Control G. The week after, the Command Palette and F2. Each time you reach for the mouse, stop, and ask, is there a shortcut for this? Then check the Command Palette.",
     vis=dict(type="steps", title="Learn them in 3 weeks", items=["Week 1:  Ctrl+P  and  Alt+Up / Down", "Week 2:  Ctrl+D  and  Ctrl+G", "Week 3:  Ctrl+Shift+P  and  F2", "Reaching for the mouse? Check the palette"])),
dict(chapter="Recap", say="Quick recap. Control P to jump to files, Control G to jump to lines. Control Shift P when you forget anything. Alt arrows to move lines, Shift Alt to copy them. Control D for the next match, starting from a plain cursor. Control Shift L for all of them. And F2 to rename safely.",
     vis=dict(type="steps", title="Recap", items=["Ctrl+P files  ·  Ctrl+G lines", "Ctrl+Shift+P: every command", "Alt+Up/Down move  ·  Shift+Alt+Down copy", "Ctrl+D from a plain cursor  ·  Ctrl+Shift+L all", "F2 renames code, not comments"])),
dict(say="Next on Shortcut Lab, merge hundreds of Excel files into one, with a few lines of Python. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Merge Hundreds of Excel Files into One with Python")),
]
# real terminal output inside the editor's terminal panel (Ctrl+`)
V_GOTO["ops"][2]["do"][0] = ("term", T("report2"))
