# Shortcut Lab - EP01: Rename hundreds of files with Python (all code run for real; output captured from the actual run)
TITLE = "Rename Hundreds of Files in Seconds with Python"
SPEED = 0.82
CODE1 = '''from pathlib import Path

folder = Path("photos")
files = sorted(folder.glob("*.JPG"))

for i, old in enumerate(files, start=1):
    new = old.with_name(f"trip-{i:03d}{old.suffix.lower()}")
    print(old.name, "->", new.name)
    # old.rename(new)'''
CODE2 = CODE1.replace("    # old.rename(new)", "    old.rename(new)")
CODE3 = '''from pathlib import Path

folder = Path("photos")
files = sorted(folder.glob("*.JPG"), key=lambda p: p.stat().st_mtime)

for i, old in enumerate(files, start=1):
    new = old.with_name(f"trip-{i:03d}{old.suffix.lower()}")
    if new.exists():
        print("skip:", new.name, "already exists")
        continue
    old.rename(new)'''
BEFORE = ["IMG_4817.JPG", "IMG_4818.JPG", "IMG_4821.JPG", "IMG_4822.JPG", "IMG_4830.JPG", "IMG_4831.JPG", "notes.txt"]
AFTER = ["trip-001.jpg", "trip-002.jpg", "trip-003.jpg", "trip-004.jpg", "trip-005.jpg", "trip-006.jpg", "notes.txt"]
OUT = [f"{b} -> {a}" for b, a in zip(BEFORE[:6], AFTER[:6])]

SCENES = [
dict(chapter="The problem", say="You have a folder with hundreds of photos, all named like I M G underscore four eight one seven dot J P G. Renaming them one by one would take an afternoon. Today we'll do it in about ten seconds, with nine lines of Python.",
     vis=dict(type="title", kicker="Python for beginners", text="Rename Hundreds of Files in Seconds", sub="9 lines of Python · no extra libraries")),
dict(say="Here's the folder we're starting with. Six photos with camera names, and one text file that we don't want to touch. On the right is where we want to end up. Clean names, numbered in order, with a lowercase extension.",
     vis=dict(type="files", title="The goal", before=BEFORE, after=AFTER, hdr1="photos/ — before", hdr2="photos/ — after")),
dict(chapter="What you need", say="All you need is Python three, installed on Windows, Mac or Linux. Everything we use today comes built in. Here's the plan. Find the files, decide the new names, preview the result, and only then rename for real.",
     vis=dict(type="steps", title="The plan", items=["Find the photo files", "Build each new name", "Preview first (dry run)", "Rename for real"])),
dict(chapter="Open a terminal in the right folder", say="One thing trips up almost every beginner, so let's get it right first. The script has to run from the folder that contains your photos folder. On Windows, open that folder in File Explorer, click the address bar, type c m d, and press Enter. A terminal opens right there. On a Mac, open Terminal, type c d and a space, then drag the folder into the window and press Enter.",
     vis=dict(type="steps", title="Open a terminal in the right place", items=["Windows: click the address bar, type cmd, Enter", "Mac: open Terminal, type cd + space, drag the folder in", "Check: ls (Mac) or dir (Windows)", "You should see photos/ and rename.py"])),
dict(say="To check you're in the right place, type l s on a Mac, or d i r on Windows. You should see the photos folder listed. If you do, you're ready.",
     vis=dict(type="term", title="Terminal", lines=["$ cd ~/Desktop/trip", "$ ls", "photos  rename.py"])),
dict(chapter="Step 1: find the files", say="Create a file called rename dot p y, in the same place as your photos folder. First, we import Path from pathlib. Path is the modern way to work with files in Python. Then we point it at our folder, and use glob to grab every file ending in dot J P G. We wrap that in sorted, so the order is predictable.",
     vis=dict(type="code", code=CODE1.split("\n\nfor")[0], file="rename.py", hl=(4,), cps=30)),
dict(say="Notice what glob does here. The star means anything, so star dot J P G matches every file with that ending, and quietly ignores notes dot t x t. One small warning. On Windows, file names are not case sensitive, so this pattern also catches files ending in lowercase dot j p g.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="*.JPG means \"any name ending in .JPG\". On Windows the match ignores upper and lower case.", color=(108, 196, 255))),
dict(chapter="Step 2: build the new names", say="Now the loop. enumerate gives us a counter alongside each file, and start equals one makes it count from one instead of zero. For each old file, with name builds a new path in the same folder. Inside the f string, i colon zero three d pads the number to three digits, so one becomes zero zero one. And suffix dot lower turns J P G into j p g.",
     vis=dict(type="code", code=CODE1, file="rename.py", **{"from": 5}, hl=(6, 7), cps=34)),
dict(say="That zero padding matters more than it looks. Without it, your file explorer would sort trip ten before trip two. With three digits, everything lines up perfectly, all the way to nine hundred and ninety nine.",
     vis=dict(type="compare", title="Why pad with zeros?", left=("Without padding", ["trip-1.jpg", "trip-10.jpg", "trip-2.jpg  (wrong order)"]), right=("With {i:03d}", ["trip-001.jpg", "trip-002.jpg", "trip-010.jpg  (correct order)"]))),
dict(chapter="Step 3: dry run", say="Here's the most important habit in this whole video. Notice the last line is commented out. Right now the script only prints what it would do. This is called a dry run. Let's run it.",
     vis=dict(type="code", code=CODE1, file="rename.py", hl=(8, 9), note="Dry run: print first, rename later", **{"from": 9})),
dict(say="In the terminal, type python rename dot p y. And there it is. Every old name, an arrow, and the new name. Nothing has changed on disk yet. If something looks wrong, you fix the script and run it again, with zero risk.",
     vis=dict(type="term", title="Terminal — dry run", lines=["$ python rename.py"] + OUT + ["$ ls photos", "IMG_4817.JPG  IMG_4818.JPG  IMG_4821.JPG  IMG_4822.JPG", "IMG_4830.JPG  IMG_4831.JPG  notes.txt"])),
dict(chapter="Step 4: rename for real", say="Happy with the preview? Remove the hash symbol in front of old dot rename, so that line actually runs. Save the file, and run it one more time.",
     vis=dict(type="code", code=CODE2, file="rename.py", hl=(9,), **{"from": 8}, note="Uncomment the rename line")),
dict(say="Same output as before, but this time it's real. List the folder, and every photo now has a clean, numbered name. And notes dot t x t is exactly where we left it. Six files here, but it would be the same ten seconds for six thousand.",
     vis=dict(type="term", title="Terminal — for real", lines=["$ python rename.py"] + OUT + ["$ ls photos", "notes.txt  trip-001.jpg  trip-002.jpg  trip-003.jpg", "trip-004.jpg  trip-005.jpg  trip-006.jpg"])),
dict(say="Before and after. Seven files, one command, and nothing done by hand.",
     vis=dict(type="files", title="Done", before=BEFORE, after=AFTER, hdr1="before", hdr2="after"), hold=0.8),
dict(chapter="If something goes wrong", say="If it didn't work, it's almost always one of three things. If nothing prints at all, the pattern didn't match anything, so check the folder name and the extension. If you see python is not recognized, or command not found, try typing python three instead, or py on Windows. And if you get file not found error, the terminal is open in the wrong folder, so go back and check with l s or d i r.",
     vis=dict(type="compare", title="Three common problems", left=("What you see", ["Nothing prints", "'python' not found", "FileNotFoundError"]), right=("The fix", ["Check folder name and *.JPG", "Try python3, or py on Windows", "Open the terminal in the right folder"]))),
dict(say="And here's a question people always ask. Is there an undo? Not by itself. Once a file is renamed, Python doesn't remember the old name. That's exactly why we do the dry run first, and why a quick copy of the folder is your best friend.",
     vis=dict(type="tip", tag="NO UNDO", text="Renaming can't be undone automatically. Dry run first, and keep a copy.", color=(255, 122, 89))),
dict(chapter="Two upgrades", say="Two quick upgrades make this script safer for real life. First, sorting by name isn't always the order the photos were taken. Add key equals lambda, p dot stat, dot s t underscore m time, and the files are sorted by the time they were last modified instead. Second, before renaming, check if the new name already exists. If it does, skip it, so you never overwrite a file by accident.",
     vis=dict(type="code", code=CODE3, file="rename.py", hl=(4, 8, 9, 10), cps=40)),
dict(chapter="Bonus: your own naming pattern", say="And because the new name is just an f string, you can make it anything you like. Want the year and a place in front? Write twenty twenty six, dash, lisbon, dash, then the padded number. Want to keep part of the old name? old dot stem gives you the name without the extension, so you could write trip dash, then old dot stem, and keep the camera number for reference.",
     vis=dict(type="code", code='''new = old.with_name(f"2026-lisbon-{i:03d}.jpg")
# 2026-lisbon-001.jpg

new = old.with_name(f"trip-{old.stem}.jpg")
# trip-IMG_4817.jpg''', file="patterns.py", hl=(1, 4), cps=40)),
dict(chapter="Bonus: more than one file type", say="What if your folder mixes J P G, J P E G and P N G files? Instead of glob, use iterdir, which lists everything in the folder, and keep only the files whose lowercase suffix is in a small set of extensions. This one line works the same on every operating system, because we lower the suffix ourselves, so upper and lower case no longer matter. The rest of the loop stays exactly the same, except you keep each file's own extension with old dot suffix dot lower.",
     vis=dict(type="code", code='''from pathlib import Path

folder = Path("photos")
images = {".jpg", ".jpeg", ".png"}
files = sorted(p for p in folder.iterdir() if p.suffix.lower() in images)

for i, old in enumerate(files, start=1):
    new = old.with_name(f"trip-{i:03d}{old.suffix.lower()}")
    print(old.name, "->", new.name)''', file="rename_any.py", hl=(4, 5), cps=42)),
dict(say="One last tip. Before you run any script that changes files, make a copy of the folder first. It takes two seconds, and it turns any mistake into a non event.",
     vis=dict(type="tip", tag="PRO TIP", text="Copy the folder before running any script that renames, moves or deletes files.", color=(255, 211, 105))),
dict(chapter="Recap", say="So, to recap. Path and glob find the files. enumerate and an f string build the new names. A dry run shows you the result first. And one line does the actual rename.",
     vis=dict(type="steps", title="Recap", items=["Path(\"photos\").glob(\"*.JPG\")", "enumerate + f\"trip-{i:03d}\"", "print first: dry run", "old.rename(new)"])),
dict(say="Next on Shortcut Lab, we'll go one step further, and automatically sort a messy downloads folder into subfolders by file type. If this saved you some time, subscribe, and I'll see you in the next one.",
     vis=dict(type="outro", next="Auto-Sort Your Messy Downloads Folder with Python")),
]
