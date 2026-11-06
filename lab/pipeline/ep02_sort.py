# Shortcut Lab - EP02: Auto-sort a messy Downloads folder with Python
# All code below was run for real (Python 3.13); every terminal output shown is the captured output of that run.
TITLE = "Auto-Sort Your Messy Downloads Folder with Python"
SPEED = 0.82
ACCENT = (108, 196, 255)  # sky (EP01 was lime)

STEP1 = '''from pathlib import Path

downloads = Path("Downloads")

for file in sorted(downloads.iterdir()):
    print(file.name, file.suffix)'''

DRY = '''from pathlib import Path

downloads = Path("Downloads")
folders = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".csv"},
    "Audio": {".mp3", ".wav"},
    "Video": {".mp4", ".mov"},
    "Archives": {".zip", ".rar"},
}

def folder_for(ext):
    for name, exts in folders.items():
        if ext in exts:
            return name
    return "Other"

for file in sorted(downloads.iterdir()):
    if file.is_file():
        target = downloads / folder_for(file.suffix.lower())
        print(f"{file.name} -> {target.name}")
        # target.mkdir(exist_ok=True)
        # file.rename(target / file.name)'''
REAL = DRY.replace("        # target.mkdir", "        target.mkdir").replace("        # file.rename", "        file.rename")

FINAL = '''from pathlib import Path

downloads = Path("Downloads")
folders = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".csv"},
    "Audio": {".mp3", ".wav"},
    "Video": {".mp4", ".mov"},
    "Archives": {".zip", ".rar"},
}
skip = {".crdownload", ".part", ".tmp", ".ini"}

def folder_for(ext):
    for name, exts in folders.items():
        if ext in exts:
            return name
    return "Other"

def unique(dest):
    new, n = dest, 1
    while new.exists():
        new = dest.with_name(f"{dest.stem} ({n}){dest.suffix}")
        n += 1
    return new

for file in sorted(downloads.iterdir()):
    ext = file.suffix.lower()
    if not file.is_file() or file.name.startswith(".") or ext in skip:
        continue
    target = downloads / folder_for(ext)
    target.mkdir(exist_ok=True)
    dest = unique(target / file.name)
    file.rename(dest)
    print(f"{file.name} -> {target.name}/{dest.name}")'''

MONTH = '''from pathlib import Path
from datetime import datetime

downloads = Path("Downloads")

for file in sorted(downloads.iterdir()):
    if file.is_file() and not file.name.startswith("."):
        modified = datetime.fromtimestamp(file.stat().st_mtime)
        target = downloads / modified.strftime("%Y-%m")
        target.mkdir(exist_ok=True)
        file.rename(target / file.name)
        print(f"{file.name} -> {target.name}")'''

NAMES = ["IMG_2041.JPG", "budget.xlsx", "clip.mp4", "data.csv", "font.ttf", "invoice_october.pdf", "meme.gif", "photos_backup.zip",
         "podcast_ep12.mp3", "project-files/", "report.txt", "resume.docx", "screenshot.png", "setup.zip", "voice_memo.wav"]
TREE = [("Archives", ["photos_backup.zip", "setup.zip"]), ("Audio", ["podcast_ep12.mp3", "voice_memo.wav"]),
        ("Documents", ["budget.xlsx", "data.csv", "invoice_october.pdf", "report.txt", "resume.docx"]),
        ("Images", ["IMG_2041.JPG", "meme.gif", "screenshot.png"]), ("Other", ["font.ttf"]), ("Video", ["clip.mp4"]), ("project-files", ["main.py"])]

LS0 = ["IMG_2041.JPG  data.csv             meme.gif           project-files  screenshot.png",
       "budget.xlsx   font.ttf             photos_backup.zip  report.txt     setup.zip",
       "clip.mp4      invoice_october.pdf  podcast_ep12.mp3   resume.docx    voice_memo.wav"]
OUT1 = ["IMG_2041.JPG .JPG", "budget.xlsx .xlsx", "clip.mp4 .mp4", "data.csv .csv", "font.ttf .ttf", "invoice_october.pdf .pdf", "meme.gif .gif",
        "photos_backup.zip .zip", "podcast_ep12.mp3 .mp3", "project-files ", "report.txt .txt", "resume.docx .docx", "screenshot.png .png",
        "setup.zip .zip", "voice_memo.wav .wav"]
DRYOUT = ["IMG_2041.JPG -> Images", "budget.xlsx -> Documents", "clip.mp4 -> Video", "data.csv -> Documents", "font.ttf -> Other",
          "invoice_october.pdf -> Documents", "meme.gif -> Images", "photos_backup.zip -> Archives", "podcast_ep12.mp3 -> Audio",
          "report.txt -> Documents", "resume.docx -> Documents", "screenshot.png -> Images", "setup.zip -> Archives", "voice_memo.wav -> Audio"]
MONTHOUT = ["IMG_2041.JPG -> 2026-09", "budget.xlsx -> 2026-10", "clip.mp4 -> 2026-11", "data.csv -> 2026-10", "font.ttf -> 2026-09",
            "invoice_october.pdf -> 2026-10", "meme.gif -> 2026-11", "photos_backup.zip -> 2026-09", "podcast_ep12.mp3 -> 2026-10",
            "report.txt -> 2026-11", "resume.docx -> 2026-09", "screenshot.png -> 2026-11", "setup.zip -> 2026-10", "voice_memo.wav -> 2026-11"]

SCENES = [
dict(chapter="The result", say="This is a messy downloads folder. Fifteen random items, all mixed together. Now watch. One command, and everything lands in Images, Documents, Audio, Video and Archives, in under a second.",
     vis=dict(type="tree", title="One command later", before=NAMES, after=TREE[:6], build=0.6, hdr1="(before)", hdr2="(after)")),
dict(say="In the next few minutes, you'll build this exact script from scratch. About thirty lines of Python, nothing to install, and it works on Windows, Mac and Linux. And stay for the second half, because this kind of script can silently destroy a file when you run it twice. I'll show you exactly how, and the one line that prevents it.",
     vis=dict(type="title", kicker="Python for beginners", text="Auto-Sort Your Downloads Folder", sub="about 30 lines · built-in Python only · Windows, Mac, Linux")),
dict(chapter="The plan", say="Here's the plan. First, list everything in the folder. Second, decide where each file belongs, based on its extension. Third, a dry run, which prints what would happen without moving anything. Fourth, move the files for real. And fifth, make it safe to run again and again.",
     vis=dict(type="steps", title="The plan", items=["List everything in the folder", "Pick a folder from the extension", "Dry run: print the plan", "Move the files for real", "Make it safe to run every day"])),
dict(chapter="Set up a safe test folder", say="Don't start on your real downloads folder. Make a new folder on your desktop called sorter, and copy your downloads folder into it. That way, any mistake happens on a copy. Open a terminal inside sorter, like we did in episode one, and list what's in Downloads. On Windows, type d i r instead of l s.",
     vis=dict(type="term", title="Terminal", lines=["$ cd ~/Desktop/sorter", "$ ls Downloads"] + LS0)),
dict(chapter="Step 1: list the files", say="Now create a file called sort downloads dot p y, next to the Downloads folder. Import Path from pathlib, and point it at Downloads. Then loop over iterdir, which hands you everything inside the folder, one item at a time. We wrap it in sorted, so the order is the same every run. For now, just print each name, and its suffix.",
     vis=dict(type="code", code=STEP1, file="sort_downloads.py", hl=(5, 6), cps=30)),
dict(say="Run it with python sort downloads dot p y. Every file shows up next to its extension. But look at project dash files. It has no suffix at all, because it's not a file. It's a folder. Remember that, because it's about to matter.",
     vis=dict(type="term", title="Terminal", lines=["$ python sort_downloads.py"] + OUT1, out_gap=0.12)),
dict(say="A quick note on suffix. It includes the dot, and it keeps the original capital letters. Cameras love capital J P G, so we'll always convert the suffix to lowercase before we compare it. That one detail saves a lot of confusion.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text=".suffix is the extension, dot included. Compare it in lowercase: .JPG and .jpg are the same type.", color=(108, 196, 255))),
dict(chapter="Step 2: a folder for each type", say="Now the rules. Images get J P G, J P E G, P N G and GIF. Documents get P D F, Word, text, Excel and C S V. Audio gets M P 3 and wave. Video gets M P 4 and M O V. Archives get zip and rar. And anything we don't recognize goes into a folder called Other, so nothing is ever left behind.",
     vis=dict(type="map", title="Which extension goes where?", rows=[("Images", [".jpg", ".jpeg", ".png", ".gif"], (108, 196, 255)), ("Documents", [".pdf", ".docx", ".txt", ".xlsx", ".csv"], (255, 211, 105)),
          ("Audio", [".mp3", ".wav"], (190, 150, 255)), ("Video", [".mp4", ".mov"], (255, 122, 89)), ("Archives", [".zip", ".rar"], (182, 243, 92))], default="Other")),
dict(say="In Python, those rules become a dictionary. Each key is a folder name, and each value is a set of extensions, inside curly braces. A set is perfect here, because checking whether something is in a set is instant, no matter how big it gets. Want a new category, like Ebooks, with dot e pub? Just add one line.",
     vis=dict(type="code", code=DRY, view=(0, 10), file="sort_downloads.py", hl=(4, 5, 6, 7, 8, 9, 10), cps=40)),
dict(say="Next, a small function called folder for. It takes an extension, walks through the dictionary, and returns the first folder whose set contains it. If the loop finishes without a match, it returns Other. Keeping this in its own function makes the main loop short and easy to read.",
     vis=dict(type="code", code=DRY, view=(0, 16), file="sort_downloads.py", hl=(12, 13, 14, 15, 16), lh=40, size=26, **{"from": 11}, cps=30)),
# REENGAGE (~3:00): the mistake almost everyone makes
dict(chapter="The mistake almost everyone makes", say="Remember project dash files? Here's the mistake almost everyone makes on their first try. If you don't check that each item is a file, the script moves folders too. On the first run, project files disappears into Other. And on the second run, it gets worse. Here's what happened when I ran that version twice. Archives, Audio, Documents and Images all get moved inside Other. Then it tries to move Other into itself, and crashes.",
     vis=dict(type="term", title="Terminal — 2nd run, without is_file()", lines=["$ python sort_downloads.py", "Archives -> Other", "Audio -> Other", "Documents -> Other", "Images -> Other", "Other -> Other",
              "Traceback (most recent call last):", "# (traceback trimmed)", "OSError: [Errno 22] Invalid argument: 'Downloads/Other' -> 'Downloads/Other/Other'"], out_gap=0.5)),
dict(say="The fix is a single line. if file dot is file. Only real files get touched, folders stay exactly where they are, and the script is safe to run again tomorrow.",
     vis=dict(type="compare", title="One line makes the difference", left=("Without is_file()", ["Folders get moved into Other", "2nd run moves Images/ into Other/", "Then it crashes halfway"]),
              right=("With if file.is_file():", ["Only files are touched", "Folders stay where they are", "Safe to run again"]))),
dict(chapter="Step 3: dry run", say="Here's the main loop. For each item that's a file, we work out the target. downloads, slash, folder for, gives us a path like Downloads slash Images. Yes, in pathlib, the slash operator joins paths, on every operating system. Then we print where the file would go. And notice the last two lines are commented out. This is a dry run.",
     vis=dict(type="code", code=DRY, view=(10, 23), file="sort_downloads.py", hl=(19, 20, 21), lh=44, **{"from": 17}, cps=34, note="Dry run: nothing moves yet")),
dict(say="Run it. Fourteen files, fourteen decisions, and project files isn't on the list, because it's a folder. Read the list slowly. If something is heading to the wrong place, fix the dictionary, and run it again. Nothing has moved yet, so there's zero risk.",
     vis=dict(type="term", title="Terminal — dry run", lines=["$ python sort_downloads.py"] + DRYOUT, out_gap=0.14)),
dict(chapter="Step 4: move the files", say="Happy with the plan? Remove the hash symbols from the last two lines. target dot mkdir creates the folder, and exist ok equals true means no error if it's already there. Then file dot rename moves the file into it. In pathlib, renaming a file into another folder is how you move it. One catch. If you ever move files to a different drive, use shutil dot move instead.",
     vis=dict(type="code", code=REAL, view=(10, 23), file="sort_downloads.py", hl=(22, 23), lh=44, **{"from": 21}, note="Uncomment: mkdir + rename")),
dict(say="Run it again. The same list, but this time it's real. List the Downloads folder, and instead of fifteen loose items, there are six tidy folders, plus project files, untouched.",
     vis=dict(type="term", title="Terminal — for real", lines=["$ python sort_downloads.py"] + DRYOUT + ["$ ls Downloads", "Archives  Audio  Documents  Images  Other  Video  project-files"], out_gap=0.12)),
dict(say="Here's the full picture. Every image in Images, every document in Documents, and the font file we never planned for, safely in Other.",
     vis=dict(type="tree", title="Sorted", after=TREE, build=0.6, hdr2="(sorted)")),
# REENGAGE (~5:30): the hidden danger promised in the intro
dict(chapter="The hidden danger: running it twice", say="Now, the danger I promised at the start. Next week, you download a new version of report dot t x t, and run the script again. Watch closely. Before the run, the report in Documents says version one. Run the script. And now it says version two. The old report is gone. No warning, no error, no recycle bin.",
     vis=dict(type="term", title="Terminal — a week later", lines=["$ cat Downloads/Documents/report.txt", "report version 1", "$ python sort_downloads.py", "report.txt -> Documents", "$ cat Downloads/Documents/report.txt", "report version 2"], out_gap=0.6)),
dict(say="And it depends on your system. On Mac and Linux, rename quietly replaces the existing file. On Windows, you get a file exists error instead, and the script stops halfway, with some files sorted and some not. Neither is what we want.",
     vis=dict(type="tip", tag="MAC & LINUX vs WINDOWS", text="Mac/Linux: rename silently replaces the old file. Windows: FileExistsError, and the script stops halfway.", color=(255, 122, 89))),
dict(chapter="Fix: never overwrite a file", say="The fix is a tiny function called unique. It starts with the destination path. While a file with that name already exists, it builds a new name. The stem, then a number in brackets, then the suffix. So report dot t x t becomes report, one, then report, two, and so on, until it finds a free name. Then we move the file to that path instead.",
     vis=dict(type="code", code=FINAL, view=(18, 34), file="sort_downloads.py", hl=(19, 20, 21, 22, 23, 24, 32, 33), lh=40, size=26, cps=40)),
dict(say="Same test again, with the new version. This time, the new report lands as report, one, and both versions are still there. That's the line that makes this script safe to run every single day.",
     vis=dict(type="term", title="Terminal — with unique()", lines=["$ python sort_downloads.py", "report.txt -> Documents/report (1).txt", "$ ls Downloads/Documents",
              "budget.xlsx  data.csv  invoice_october.pdf  report (1).txt  report.txt  resume.docx", "$ cat \"Downloads/Documents/report.txt\"", "report version 1"], out_gap=0.5)),
dict(chapter="Skip unfinished downloads", say="Two more things live in a real downloads folder. Files that are still downloading, which Chrome and Edge name dot c r download, and Firefox names dot part. Move those mid download, and they break. And hidden system files, like dot D S underscore store on a Mac, or desktop dot i n i on Windows. So we add a skip set, and at the top of the loop, if it's not a file, starts with a dot, or has a skipped extension, continue jumps straight to the next one.",
     vis=dict(type="code", code=FINAL, view=(10, 30), file="sort_downloads.py", hl=(11, 27, 28, 29), lh=36, size=24, cps=60)),
dict(say="Final test. A new report, a half finished movie download, and a hidden file. Only the real new file moved. The download in progress and the hidden file were left alone, exactly as they should be.",
     vis=dict(type="term", title="Terminal — final script", lines=["$ ls -A Downloads", ".DS_Store  Audio      Images  Video                 project-files", "Archives   Documents  Other   movie.mp4.crdownload  report.txt",
              "$ python sort_downloads.py", "report.txt -> Documents/report (2).txt", "$ ls -A Downloads", ".DS_Store  Audio      Images  Video                 project-files", "Archives   Documents  Other   movie.mp4.crdownload"], out_gap=0.5)),
dict(chapter="Use it on your real Downloads", say="When you're confident, point it at your real downloads folder. Path dot home gives you your user folder on any system. So Path dot home, slash, Downloads, works on Windows, Mac and Linux without changing anything else. Do one more dry run first. Always.",
     vis=dict(type="code", code='downloads = Path("Downloads")\n\n# your real Downloads folder, on any system:\ndownloads = Path.home() / "Downloads"', file="sort_downloads.py", hl=(4,), cps=34, note="Dry run first. Always.")),
# REENGAGE (~7:00): bonus variant
dict(chapter="Bonus: sort by month", say="Bonus. Some people prefer folders by date instead of by type. A file's last modified time lives in file dot stat, dot s t underscore m time. datetime dot from timestamp turns that number into a date, and s t r f time, with percent capital Y, dash, percent m, gives you a folder name like twenty twenty six dash eleven.",
     vis=dict(type="code", code=MONTH, file="sort_by_month.py", hl=(8, 9), cps=40)),
dict(say="Run it, and your downloads are grouped by month. Year first, then month, so the folders also sort in time order, automatically.",
     vis=dict(type="term", title="Terminal — by month", lines=["$ python sort_by_month.py"] + MONTHOUT + ["$ ls Downloads", "2026-09  2026-10  2026-11  project-files"], out_gap=0.1)),
dict(chapter="If something goes wrong", say="If something goes wrong, it's usually one of three things. Nothing moves? The two lines at the bottom are probably still commented out. Permission error on Windows? A file is open in another program, so close it and run again. And file not found error means the terminal is open in the wrong folder, or Downloads is spelled differently, and capital letters matter on Mac and Linux.",
     vis=dict(type="compare", title="Three common problems", left=("What you see", ["Nothing moves", "PermissionError (Windows)", "FileNotFoundError"]),
              right=("The fix", ["Uncomment the last two lines", "Close the file in other apps", "Right folder? Right spelling?"]))),
dict(say="Pro tip. Make the dictionary yours. Download a lot of installers? Add a line for Installers, with dot e x e, dot m s i and dot d m g. Code files? Add dot p y and dot j s. The rest of the script doesn't change at all.",
     vis=dict(type="code", code='folders = {\n    "Images": {".jpg", ".jpeg", ".png", ".gif"},\n    # ...\n    "Installers": {".exe", ".msi", ".dmg"},\n    "Code": {".py", ".js", ".html"},\n}', file="sort_downloads.py", hl=(4, 5), cps=40, note="PRO TIP: one line per category")),
dict(chapter="Recap", say="Quick recap. iterdir lists the folder. A dictionary of sets maps each extension to a folder. A dry run shows the plan, then mkdir and rename do the work. unique makes sure nothing is ever overwritten. And the skip check leaves unfinished downloads alone.",
     vis=dict(type="steps", title="Recap", items=["iterdir() lists the folder", "dict of sets: extension to folder", "dry run, then mkdir + rename", "unique() never overwrites", "skip partial + hidden files"])),
dict(say="Next on Shortcut Lab, we switch to Excel, with seven formulas that replace hours of manual work, like X lookup, filter, and unique. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="7 Excel Formulas That Replace Hours of Work")),
]
