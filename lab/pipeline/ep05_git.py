# Shortcut Lab - EP05: Git in 10 minutes, save every version of your work
# AUTHENTICITY: every git command on screen was run for real (demo/ep05_git.sh, git 2.43); terminal lines come straight from the captured
# transcript demo/ep05_transcript.txt, so commit hashes and outputs are the real ones. Commands checked against git-scm.com docs
# (git init/add/commit/status/diff/log/restore/revert/switch/merge, gitignore). Demo identity is a placeholder (Sam Rivera, sam@example.com).
import os, re
TITLE = "Git in 10 Minutes: Save Every Version of Your Work"
SPEED = 0.82
ACCENT = (255, 211, 105)  # gold (EP01 lime, EP02 sky, EP03 coral, EP04 violet)
SKY, VIO, YEL, LIME, CORAL, PINK = (108, 196, 255), (190, 150, 255), (255, 211, 105), (182, 243, 92), (255, 122, 89), (255, 160, 200)

_T = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep05_transcript.txt")).read().replace("\t", "        ")
_S = {m.group(1): m.group(2).strip("\n").split("\n") for m in re.finditer(r"### (\w+)\n(.*?)(?=\n### |\Z)", _T, re.S)}
def T(k, a=0, b=None): return _S[k][a:b]
LOG = [l.split(" ", 1) for l in T("S9")[1:]]           # [[hash, msg] x3], newest first
H1, H2, H3 = LOG[2][0], LOG[1][0], LOG[0][0]
L13 = [l.split(" ", 1) for l in T("S13")[3:]]         # log incl. the bad commit
HB = L13[0][0]
HR = re.search(r"\[main (\w+)\]", "\n".join(T("S14"))).group(1)
HS = re.search(r"\[savings (\w+)\]", "\n".join(T("S16"))).group(1)
HI = re.search(r"\[main (\w+)\] Ignore", "\n".join(T("S15"))).group(1)

V1 = '''income = 3000
rent = 1200
food = 450

left = income - rent - food
print("Left this month:", left)'''
V2 = '''income = 3000
rent = 1200
food = 450
transport = 120

left = income - rent - food - transport
print("Left this month:", left)'''

SCENES = [
dict(chapter="The result", say="You changed a file, something broke, and now nothing works. Watch this. One command, and the file is back exactly as it was. No backup copies, no final version two, final version three. That's Git, and in the next ten minutes you'll learn to use it from zero.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S10", 0, 6) + T("S11"), out_gap=0.12)),
dict(say="Git saves every version of your work, so you can always go back. Programmers use it every day, but it works for any folder of files. Scripts, notes, websites. No experience needed. Just a terminal and about ten minutes.",
     vis=dict(type="title", kicker="Git for beginners", text="Git in 10 Minutes", sub="Save every version of your work · go back in time when something breaks")),
dict(chapter="What Git actually does", say="Think of Git like save points in a video game. Every time you reach a good spot, you save. Each save point is called a commit. It has a short code, called a hash, and a message that says what changed. If you mess up later, you load an older save point. Your work is never lost.",
     vis=dict(type="timeline", title="Commits are save points", commits=[[H1, "First version of budget"], [H2, "Add transport costs"], [H3, "Add fun money"]], span=0.5,
              note="Each dot = one commit (a saved version)")),
dict(say="Here's the plan. Install Git and check it works. Tell Git who you are. Start tracking a folder. Save versions with add and commit. And then the fun part. Go back in time, undo mistakes, and try ideas safely on a branch.",
     vis=dict(type="steps", title="The plan", items=["Install Git and check it", "Tell Git who you are (once)", "Start tracking a folder: git init", "Save versions: git add + git commit", "Go back in time and undo mistakes"])),
dict(chapter="Install and check", say="To install Git, go to git dash s c m dot com, the official site. On Windows, download Git for Windows and click through the installer. The default options are fine. It also gives you a terminal called Git Bash. On a Mac, open Terminal and type git space dash dash version. If Git isn't there yet, the Mac offers to install it for you. On Linux, use your package manager.",
     vis=dict(type="steps", title="Install Git (free, official: git-scm.com)", items=["Windows: Git for Windows installer, defaults are fine", "Mac: type git --version, accept the install", "Linux: sudo apt install git (or your package manager)", "Then check: git --version"])),
dict(say="Either way, check it with git dash dash version. If you see a version number, you're ready. Mine says two point four three. Yours might be newer, and that's fine. Everything in this video works the same.",
     vis=dict(type="term", title="Terminal", lines=T("S1"))),
dict(chapter="Tell Git who you are", say="Next, tell Git who you are. You only do this once per computer. Type git config dash dash global user dot name, and your name in quotes. Then the same with user dot email. Git writes this name and email into every commit, so you always know who changed what. The third line makes your main timeline be called main, which is the modern standard.",
     vis=dict(type="term", title="Terminal — one-time setup", lines=T("S3"))),
dict(say="These commands print nothing, and that's normal. In Git, no news is good news. Use your own name and email here. If you plan to put your projects on GitHub later, use the same email you'll use there.",
     vis=dict(type="tip", tag="GOOD TO KNOW", text="No output means it worked. Use your own name and email; Git stores them in every commit.", color=SKY)),
dict(chapter="Step 1: git init", say="Our project is a tiny budget script in a folder called budget. It adds up rent and food, and prints what's left. It doesn't matter what's inside. This could be any file you care about.",
     vis=dict(type="code", code=V1, file="budget.py", cps=40)),
dict(say="Open a terminal in that folder. If you type git status right now, Git says, not a git repository. That just means Git isn't watching this folder yet. Don't worry, that's what the next command fixes.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S2"))),
dict(say="Type git init. Git creates a hidden folder called dot git, where it will keep every version. Now git status works. It says we're on branch main, no commits yet, and budget dot p y is untracked. Untracked means Git sees the file, but isn't saving it yet.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S4"))),
dict(chapter="Step 2: add and commit", say="Here's the one idea that makes Git click. There are three areas. Your folder, where you edit files. The staging area, which is like a box where you put the changes for your next save. And the history, where the saved versions live. git add puts a file in the box. git commit seals the box and saves it.",
     vis=dict(type="stage", title="The 3 areas of Git", chips=[["budget.py", 0, 2]], note="git add = pick what to save · git commit = save it")),
dict(say="So, git add budget dot p y. Then git status again. Now the file is green in a real terminal, under changes to be committed. It's in the box, ready to be saved.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S5"))),
dict(say="Now commit. git commit, dash m, and a short message in quotes that says what this version is. First version of budget. Git answers with the branch, the hash of the new commit, and how many lines it saved. That's it. You just made your first save point.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S6", 0, 4))),
dict(say="Write messages your future self will understand. Add transport costs tells you exactly what happened. Update, or stuff, or asdf, tells you nothing. A good rule. Finish the sentence, this commit will, and keep it short.",
     vis=dict(type="compare", title="Commit messages", left=("Useless later", ["update", "stuff", "asdf"]), right=("Clear later", ["Add transport costs", "Fix rent total", "Rename budget file"]))),
dict(chapter="Step 3: see what changed", say="Let's change something. I add a transport line, and subtract it from what's left. Save the file. Now, what exactly did I change? Git can tell you.",
     vis=dict(type="code", code=V2, file="budget.py", hl=(4, 6), **{"from": 7})),
dict(say="git status dash dash short shows an M next to budget dot p y. M means modified. And git diff shows the exact lines. Lines starting with a plus were added. Lines with a minus were removed. Here, one new line for transport, and the total line was replaced with the new version.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S7"), out_gap=0.12)),
dict(chapter="Step 4: the history", say="Happy with it? Same two steps as before. git add, then git commit with a message. Add transport costs. And I'll do it once more after adding some fun money to the budget. Add, commit. That's the whole daily rhythm of Git. Edit, add, commit.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S8"))),
dict(say="Now type git log dash dash oneline. Here's your whole history, newest first. Each line is a commit, with its hash and its message. These hashes are your save points. And notice, budget dot p y is still a single file. No copies anywhere.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S9"))),
dict(say="As a picture, it looks like this. Three save points in a row, and the label main points at the newest one. Every new commit adds a dot on the right.",
     vis=dict(type="timeline", title="git log, as a picture", commits=[[h, m] for h, m in LOG[::-1]], span=0.45)),
dict(chapter="Undo: get back a broken file", say="Now the scary part, made easy. Say I accidentally delete the food line, and save. I run the script, and it crashes. Name error, food is not defined. And git status shows the file is modified.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S10"), out_gap=0.15)),
dict(say="To throw away those changes and get the last saved version back, type git restore budget dot p y. Run it again. Left this month, ten thirty. The file is exactly how it was at the last commit.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S11"))),
dict(say="One warning. git restore throws away your unsaved changes in that file, for good. Git can only bring back what was committed. So use it when you really want the last saved version back.",
     vis=dict(type="tip", tag="CAREFUL", text="git restore <file> deletes your uncommitted changes in that file. Only commits can come back.", color=CORAL)),
dict(chapter="Go back to any version", say="You can also go back further, to any save point. Take the hash of the very first commit from git log. Then type git restore, dash dash source equals that hash, and the file name. The file now looks exactly like it did in the first version.",
     vis=dict(type="timeline", title="Load an older save point", commits=[[h, m] for h, m in LOG[::-1]], back=0, back_label=f"git restore --source={H1} budget.py", span=0.3)),
dict(say="Run the script, and it prints thirteen fifty, the original number, before transport and fun money. Your history is still safe. Nothing was deleted. When you're done looking, git restore budget dot p y brings you back to the latest version, ten thirty.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S12"))),
dict(chapter="Undo a bad commit", say="What if the mistake was already committed? Here, I typed food equals forty five hundred instead of four fifty, and committed it. Now the budget says minus three thousand and twenty. Oops. And the bad commit is right there at the top of the log.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S13"))),
dict(say="The safe fix is git revert, then the hash, or just the word HEAD, which means the latest commit. Git creates a brand new commit that undoes the bad one. The budget is back to ten thirty. And the history shows both. The mistake, and the fix. Nothing is rewritten, which is exactly what you want when other people share your project.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S14"))),
dict(say="So remember the difference. git restore is for changes you haven't committed yet, or for peeking at an old version of a file. git revert is for a commit that was already saved, and it undoes it with a new commit.",
     vis=dict(type="compare", title="restore or revert?", left=("git restore <file>", ["Not committed yet", "Throws the edits away", "Or: --source=<hash> to peek"]), right=("git revert <hash>", ["Already committed", "Adds an \"undo\" commit", "History stays honest"]))),
dict(chapter="Ignore files with .gitignore", say="Some files should never be saved. Logs, temporary files, the cache folder Python creates. Git status shows them with two question marks, meaning untracked. To make Git ignore them, create a file called dot gitignore, and list them, one per line. A folder name ends with a slash.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S15", 0, 6))),
dict(say="Run git status again, and the clutter is gone. Only the new dot gitignore file shows up. Add it and commit it, so the rule is saved with your project. This is also where you list files with passwords or secret keys, so they never end up in your history.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S15", 6))),
dict(chapter="Bonus: try ideas on a branch", say="Bonus. Want to try an idea without risking your working version? Use a branch. git switch dash c savings creates a new branch called savings and moves you onto it. I add a savings goal, and commit. Little shortcut here. Dash a m adds every file Git already tracks and commits, in one go. On this branch, the budget now says seven thirty.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S16", 0, 7))),
dict(say="git switch main takes me back, and there the budget still says ten thirty. The experiment lives on its own line, and main is untouched. Like a parallel timeline.",
     vis=dict(type="timeline", title="A branch is a parallel timeline", commits=[[H2, "Add transport"], [H3, "Add fun money"], [HR, "Revert food"], [HI, "Ignore logs"]], branch=[3, [[HS, "Try a savings goal"]], "savings"], span=0.35)),
dict(say="Like the idea? Switch to main, and type git merge savings. The savings commit becomes part of main, and the script prints seven thirty. Don't like it? Just switch back to main and keep working. The branch stays out of your way.",
     vis=dict(type="term", title="Terminal — budget", lines=T("S16", 7, 18))),
dict(chapter="Common mistakes", say="Three errors you'll almost certainly see. Fatal, not a git repository. Your terminal is in the wrong folder, or you never ran git init. Nothing to commit, working tree clean. You haven't changed anything since the last commit, or you forgot to save the file in your editor. And author identity unknown. You skipped the one-time setup, so run the two git config lines from the start of this video.",
     vis=dict(type="compare", title="3 errors, 3 fixes", left=("You see", ["fatal: not a git repository", "nothing to commit, working tree clean", "Author identity unknown"]),
              right=("The fix", ["cd into the folder, or git init", "Save the file in your editor first", "Run the git config lines once"]))),
dict(say="Here's that last one, for real. Git even tells you which two commands to run. Read the error message slowly. In Git, it almost always contains the fix.",
     vis=dict(type="term", title="Terminal — new computer", lines=T("MIST3", 0, 10))),
dict(chapter="Pro tip: commit small, commit often", say="Pro tip. Commit small, and commit often. One change, one commit, with a clear message. Then, when something breaks, you go back one small step instead of losing a whole day. And type git status before and after every command. It always tells you where you are, and what to do next.",
     vis=dict(type="tip", tag="PRO TIP", text="One change = one commit. And when in doubt, type git status: it tells you where you are and what to do next.", color=LIME)),
dict(chapter="Recap", say="Quick recap. git init once per folder. git add to pick what to save, git commit to save it. git log to see your history. git restore to undo unsaved changes, or to load an old version. And git revert to undo a commit. Six commands, and you'll never lose your work again.",
     vis=dict(type="steps", title="Recap: 6 commands", items=["git init: start tracking a folder", "git add + git commit -m \"...\": save a version", "git log --oneline: see the history", "git restore: undo unsaved changes / load a version", "git revert: undo a commit", "git switch -c: try ideas on a branch"])),
dict(say="Next on Shortcut Lab, turn a spreadsheet into charts with Python. A few lines of pandas and matplotlib, and your data becomes pictures. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="Turn a Spreadsheet into Charts with Python")),
]
