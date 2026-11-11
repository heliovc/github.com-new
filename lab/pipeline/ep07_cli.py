# Shortcut Lab - EP07: Command Line Basics Everyone Should Know
# AUTHENTICITY: every command on screen was typed into a REAL interactive bash 5.2 session (pty, 80 columns, as a practice user "alex")
# by demo/ep07_cli.py; the terminal lines come verbatim from the captured transcript demo/ep07_transcript.txt (coreutils 9.4).
# Commands/options checked against the GNU coreutils and Bash manuals. Windows/Mac notes: Git for Windows ships Git Bash; macOS Terminal uses zsh.
import os, re
TITLE = "Command Line Basics Everyone Should Know"
SPEED = 0.82
ACCENT = (255, 160, 200)  # pink (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint)
SKY, VIO, YEL, LIME, CORAL, MINT = (108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 122, 89), (80, 220, 190)

_T = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep07_transcript.txt")).read()
_S = {m.group(1): [l.expandtabs(8) for l in m.group(2).strip("\n").split("\n")] for m in re.finditer(r"### (\w+)\n(.*?)(?=\n### |\Z)", _T, re.S)}
def T(k, a=0, b=None): return _S[k][a:b]

TREE = [(0, "alex/"), (1, "Desktop/"), (1, "Documents/"), (2, "resume.txt"), (2, "school/"), (1, "Downloads/"), (1, "notes.txt")]
PATHS = {0: "/home/alex", 2: "/home/alex/Documents", 4: "/home/alex/Documents/school"}

SCENES = [
dict(chapter="The result", say="Three photos stuck in your Downloads folder. Watch. One line, and they're all moved into a new folder. No dragging, no clicking. That's the command line, and in the next few minutes you'll learn the commands everyone should know, from zero.",
     vis=dict(type="term", title="Terminal — trip", lines=T("mvphotos"), out_gap=0.15)),
dict(say="The command line looks scary, but it's just a window where you type instructions instead of clicking. About a dozen commands cover almost everything a beginner needs. Let's learn them, one at a time.",
     vis=dict(type="title", kicker="Command line for beginners", text="Command Line Basics", sub="The commands everyone should know · Windows, Mac and Linux")),
dict(chapter="Why learn the command line?", say="Why bother, when you have a mouse? Because typing is faster for repetitive jobs. One command can move a hundred files. It's also how you run Python scripts, use Git, and follow almost every programming tutorial. Once you know the basics, none of that feels scary anymore.",
     vis=dict(type="compare", title="Clicking vs typing", left=("Clicking", ["Drag files one by one", "Hunt through menus", "Hard to repeat"]), right=("Typing", ["One line moves them all", "Runs scripts and Git", "Easy to repeat and reuse"]))),
dict(say="Here's the plan. Open a terminal. Find out where you are and what's there. Move between folders. Create, copy, move and delete files. And then the errors you'll see, and two shortcuts that make it all faster.",
     vis=dict(type="steps", title="The plan", items=["Open a terminal", "Where am I, and what's here?", "Move around between folders", "Create, copy, move, delete", "Errors, and two pro shortcuts"])),
dict(chapter="Open a terminal", say="First, open a terminal. On a Mac, press command space, type terminal, and press enter. On Linux, it's called Terminal in your apps. On Windows, the easiest way to follow along is Git Bash, which comes free with Git for Windows. We installed it in the Git episode. Windows PowerShell understands some of these commands too, but not all of them, and the options are different.",
     vis=dict(type="steps", title="Open a terminal", items=["Mac: Command + Space, type Terminal", "Linux: open the Terminal app", "Windows: Git Bash (free with Git for Windows)", "PowerShell: some commands differ"])),
dict(say="A quick note. The dollar sign at the start of each line is the prompt. It means the terminal is waiting for you. You don't type it. On a Mac the prompt ends with a percent sign instead, and that's fine. Every command in this video works the same.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="The $ is the prompt: don't type it. On a Mac it may be %. Type the command, then press Enter.", color=SKY)),
dict(chapter="Where am I? pwd", say="The terminal is always inside one folder. To see which one, type p w d. It stands for print working directory, and directory is just another word for folder. Mine says slash home slash alex. That's my home folder, where the terminal usually starts.",
     vis=dict(type="term", title="Terminal", lines=T("pwd"))),
dict(chapter="What's here? ls", say="Now, what's in this folder? Type l s, short for list. You see Desktop, Documents, Downloads, and a file called notes dot t x t. The same things you'd see in your file explorer, just as text.",
     vis=dict(type="term", title="Terminal", lines=T("ls"))),
dict(say="Add a space and dash l, for long, and you get one item per line, with more details. Lines starting with a d are directories, so folders. Then the owner, the size in bytes, and the date it was last changed. Notes dot t x t is eighteen bytes.",
     vis=dict(type="term", title="Terminal", lines=T("lsl"))),
dict(say="And l s dash a shows all files, including hidden ones. Hidden files start with a dot, like dot bash r c, which holds terminal settings. You'll also see a single dot, which means this folder, and two dots, which means the folder above. Remember those two dots. We'll use them in a second.",
     vis=dict(type="term", title="Terminal", lines=T("lsa"))),
dict(say="Notice the pattern. Every command has the same shape. First the command, the action. Then options, which start with a dash and change how it works. Then the argument, which is what you want it to work on. Command, option, argument. That's the grammar of the whole command line.",
     vis=dict(type="cards", title="Every command has the same shape", cols=3, items=[["ls", "The command: what to do"], ["-l", "An option: how to do it (starts with a dash)"], ["Documents", "An argument: what to do it to"]], colors=[ACCENT, SKY, YEL], span=0.5)),
dict(chapter="Move around: cd", say="To go into a folder, type c d, for change directory, then the folder name. c d Documents. Nothing is printed, and that's normal. Type p w d, and you're now in slash home slash alex slash Documents. And l s shows what's in here. A resume, and a folder called school.",
     vis=dict(type="term", title="Terminal", lines=T("cd"))),
dict(say="Here's what that looks like as a map. c d school goes one level deeper. c d, space, dot dot, goes up one level, back to Documents. And c d, tilde, jumps straight home, from anywhere. The tilde is the little wave key, usually at the top left of your keyboard.",
     vis=dict(type="nav", title="cd moves you around the folder tree", tree=TREE, paths=PATHS, start=2, steps=[["cd school", 4], ["cd ..", 2], ["cd ~", 0]], span=0.7)),
dict(say="And here it is in the real terminal. After each c d, p w d confirms where we are. School, then Documents again, then home.",
     vis=dict(type="term", title="Terminal", lines=T("cdup"), out_gap=0.12)),
dict(say="You can also jump several levels at once. c d Documents slash school goes two folders deep in one step. And c d dot dot slash dot dot goes up two levels. Back home again.",
     vis=dict(type="nav", title="Several levels in one step", tree=TREE, paths=PATHS, start=0, steps=[["cd Documents/school", 4], ["cd ../..", 0]], span=0.6)),
dict(say="One idea makes paths click. A path that starts with a slash is a full address, from the very top of the computer. Slash home slash alex works from anywhere. A path without a slash at the start is relative, so it starts from the folder you're in right now.",
     vis=dict(type="compare", title="Two kinds of paths", left=("Relative", ["Documents/school", "Starts where you are now", "Short and handy"]), right=("Full (absolute)", ["/home/alex/Documents", "Starts at the top: /", "Works from anywhere"]))),
dict(chapter="Create folders and files", say="Let's build something. We're planning a trip. m k dir trip makes a new folder. That's make directory. c d trip goes inside. Then touch, followed by two names, creates two empty files at once. Packing dot t x t, and budget dot t x t. l s shows them both.",
     vis=dict(type="term", title="Terminal — trip", lines=T("mkdir"))),
dict(chapter="Write and read files", say="To put text in a file, use echo. echo passport, then a greater than sign, then packing dot t x t. The greater than sign sends the text into the file. Then two greater than signs to add more lines. Phone charger. Sunscreen. And cat shows what's inside a file. Our packing list, three lines.",
     vis=dict(type="term", title="Terminal — trip", lines=T("echo"))),
dict(say="Careful with this one. A single greater than sign replaces everything in the file. Two of them add to the end. Mix them up, and your list is gone. When in doubt, use two.",
     vis=dict(type="tip", tag="CAREFUL", text="> replaces the whole file. >> adds a line at the end. When in doubt, use >>.", color=CORAL)),
dict(chapter="Copy, rename and move", say="To copy a file, type c p, then the file, then the name of the copy. c p packing dot t x t, packing dash backup dot t x t. Now there are two.",
     vis=dict(type="term", title="Terminal — trip", lines=T("cp"))),
dict(say="To rename, use m v, which means move. m v budget dot t x t, costs dot t x t. In the terminal, renaming is just moving a file to a new name, in the same folder.",
     vis=dict(type="term", title="Terminal — trip", lines=T("mv"))),
dict(say="And m v also moves files between folders. That's the trick from the start. I make a photos folder. l s tilde slash Downloads shows three beach photos and a ticket. Then m v, tilde slash Downloads slash star dot j p g, photos slash. All three photos move in one go, and only the ticket stays behind.",
     vis=dict(type="term", title="Terminal — trip", lines=T("mvphotos"), out_gap=0.15)),
dict(say="The star is a wildcard. It means anything. So star dot j p g means every file that ends in dot j p g. It works with any command. l s star dot t x t lists only the text files.",
     vis=dict(type="term", title="Terminal — trip", lines=T("glob"))),
dict(chapter="Delete (carefully)", say="To delete a file, type r m, for remove. r m packing dash backup dot t x t. Gone. And when I say gone, I mean it. More on that in a second.",
     vis=dict(type="term", title="Terminal — trip", lines=T("rm"))),
dict(say="r m won't delete a folder. Cannot remove photos, is a directory. The command for folders is r m dir, but it only removes empty folders. Our photos folder still has photos, so it refuses. Directory not empty. An empty folder, like this one called old, goes away fine.",
     vis=dict(type="term", title="Terminal — trip", lines=T("rmdir"))),
dict(say="Here's the most important warning in this video. r m does not use the trash. There's no undo. And r m dash r deletes a folder and everything inside it. So before you delete, run l s with the same name first, and check what's going to disappear.",
     vis=dict(type="tip", tag="WARNING", text="rm skips the trash: there is no undo. rm -r deletes a folder and everything in it. Run ls first to check.", color=CORAL)),
dict(chapter="Common errors", say="Now the errors you'll see most. No such file or directory, usually means a typo, like Documnets. Or you're in a different folder than you think. Command not found means the command name is misspelled, or not installed. And file exists means there's already a folder with that name.",
     vis=dict(type="term", title="Terminal", lines=T("err"), out_gap=0.15)),
dict(say="So, three errors, three fixes. Check the spelling, and remember that capital letters matter. Documents with a capital D is not the same as documents. Run p w d and l s to see where you really are. And pick a new name, or use the folder that already exists.",
     vis=dict(type="compare", title="3 errors, 3 fixes", left=("You see", ["No such file or directory", "command not found", "File exists"]), right=("The fix", ["Check spelling and capitals, run ls", "Check the command name", "Use another name, or just cd in"]))),
dict(say="One more trap. Spaces in names. c d summer plans fails with too many arguments, because the terminal thinks summer and plans are two separate things. Put the name in quotes, and it works.",
     vis=dict(type="term", title="Terminal — trip", lines=T("space", 0, 6))),
dict(chapter="Pro tip: Tab and history", say="Pro tip number one. Never type a full name again. Type the first few letters, like c d Doc, and press Tab. The terminal finishes the name for you, and it never makes typos. If nothing happens, press Tab twice to see all the options.",
     vis=dict(type="keys", title="PRO TIP: let the terminal finish names", keys=["Tab"], sub="Type the first letters, press Tab: the name is completed for you")),
dict(say="Pro tip number two. Press the up arrow to bring back your last command, and keep pressing to go further back. Type history to see the full list, with numbers. Here, the vertical bar sends the list into tail, which keeps only the last five lines.",
     vis=dict(type="term", title="Terminal — trip", lines=T("history"))),
dict(say="And when you forget what a command can do, ask it. l s dash dash help prints the instructions. On a Mac, type man, space, l s instead, and press q to quit. And if a command ever gets stuck, control C stops it.",
     vis=dict(type="term", title="Terminal — trip", lines=T("help"))),
dict(chapter="Recap", say="Quick recap. p w d, where am I. l s, what's here. c d, go somewhere. m k dir and touch, create. echo and cat, write and read. c p, copy. m v, move or rename. And r m, delete, carefully. Pause the video and screenshot this cheat sheet.",
     vis=dict(type="cards", title="Cheat sheet: 9 commands", cols=3, span=0.75, colors=[ACCENT, SKY, YEL, MINT, VIO, LIME, ACCENT, SKY, CORAL], items=[["pwd", "Where am I?"], ["ls  ls -l  ls -a", "What's in this folder?"], ["cd folder  cd ..  cd ~", "Go somewhere"], ["mkdir name", "Create a folder"], ["touch file.txt", "Create an empty file"], ["echo \"hi\" >> f.txt", "Write; cat f.txt reads"], ["cp a.txt b.txt", "Copy a file"], ["mv old new", "Move or rename"], ["rm file", "Delete (no undo!)"]])),
dict(say="Next on Shortcut Lab, Google Sheets QUERY. Automatic reports, in one formula. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Google Sheets QUERY: Automatic Reports in One Formula")),
]
