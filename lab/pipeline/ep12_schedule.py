# Shortcut Lab - EP12: Run a Python Script Automatically Every Day (cron on Mac/Linux, Task Scheduler on Windows)
# AUTHENTICITY: report_v1.py / report.py / todo.txt are in demo/ep12/ and really ran under a REAL cron daemon (Debian cron, Python 3.11.18)
# as a practice user "alex"; every terminal line comes verbatim from demo/ep12/transcript.txt (container clock is UTC). The cron
# FileNotFoundError is the real log of the first scheduled run. The "cron" scenes compute every run time at render time.
# Windows steps checked against Microsoft's Task Scheduler / schtasks documentation (Create Basic Task wizard, "Start in", Settings tab).
import os
TITLE = "Run a Python Script Automatically Every Day"
SPEED = 0.82
ACCENT = (64, 214, 255)  # cyan (EP01 lime, EP02 sky, EP03 coral, EP04 violet, EP05 gold, EP06 mint, EP07 pink, EP08 orange, EP09 periwinkle, EP10 ruby, EP11 magenta)
SKY, YEL, MINT, CORAL, VIO, LIME = (108, 196, 255), (255, 211, 105), (80, 220, 190), (255, 122, 89), (190, 150, 255), (182, 243, 92)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo", "ep12")
def src(n): return open(os.path.join(D, n)).read()
TR = src("transcript.txt")
def T(name): return TR.split(f"### {name}\n")[1].split("###")[0].rstrip("\n").split("\n")
LINE = "* * * * * /usr/local/bin/python3 /home/alex/scripts/report.py >> /home/alex/scripts/cron.log 2>&1"
DAILY = T("crontab2")[1]
def cr(name): l = T(name); return [l[0], l[1][:58], "  " + l[1][58:]]  # long crontab line wrapped for the window (same text)

SCENES = [
dict(chapter="The result", say="Look at this report file. The first line, I ran by hand. Every line after that, I didn't touch anything. My computer ran the script on its own, every minute, on a schedule. In this video, you'll set that up for any Python script. On a Mac, on Linux, and on Windows. It takes about five minutes.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("works"), out_gap=0.5)),
dict(say="A script that runs itself is the moment automation really clicks. Backups, reports, reminders, cleaning your downloads folder. Write it once, schedule it, and forget about it. Let's do it step by step, from zero.",
     vis=dict(type="title", kicker="Python automation for beginners", text="Run a Python Script Automatically Every Day", sub="cron on Mac and Linux  ·  Task Scheduler on Windows")),
dict(chapter="Why schedule a script?", say="Here's the difference. When you run a script by hand, you have to remember. You open a terminal, you type the command, every single day. A scheduled script just runs. At the same time, every day, even when you forget. And every run leaves a record, so you can check it worked.",
     vis=dict(type="compare", title="By hand vs. on a schedule", left=("By hand", ["You have to remember", "Open a terminal every day", "Skipped when you're busy"]),
              right=("On a schedule", ["Runs at the same time daily", "No typing, no clicking", "Leaves a log you can check"]))),
dict(chapter="The plan", say="Here's the plan. A small script to schedule. Then cron, the scheduler built into Mac and Linux. I'll show you the mistake that breaks almost everyone's first schedule, and how to fix it. Then Windows Task Scheduler. And finally, how to make sure it never silently fails.",
     vis=dict(type="steps", title="The plan", items=["A small script worth scheduling", "cron: the Mac and Linux scheduler", "The mistake that breaks first schedules", "Task Scheduler on Windows", "Logs, missed runs and pro tips"])),
dict(chapter="The script", say="First, the script. I have a folder called scripts, with a to do list inside. Each line is a task. An x in the brackets means done. Empty brackets mean still open. Our script will count the open tasks, and write one line with the date and the count, into a report file.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("todo"), out_gap=0.25)),
dict(say="Here's report dot py. It opens todo dot t x t, and keeps only the lines that start with empty brackets. Then it gets the current date and time with datetime. It builds one line, and appends it to report dot t x t. The letter a means append, so each run adds a new line instead of erasing the file.",
     vis=dict(type="code", file="report.py", code=src("report_v1.py"), hl=(3, 9), note="\"a\" = append: every run adds one new line")),
dict(say="Always run it by hand first. Inside the folder, python three report dot py. It prints today's line, three open tasks. And report dot t x t now has that line. The script works. Now let's make it run on its own.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("manual")[2:], out_gap=0.4)),
dict(chapter="Mac and Linux: cron", say="On Mac and Linux, the scheduler is called cron. It's already installed, and it's always running in the background. Each user has a list of jobs, called a crontab. Type crontab dash l, l for list. No crontab for alex. So the list is empty. Let's add our first job.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("crontab0"), out_gap=0.4)),
dict(chapter="How to read a cron schedule", say="A cron job is one line. It starts with five time fields, then the command. Minute. Hour. Day of the month. Month. And day of the week. A star means every. So five stars means every minute, of every hour, of every day. Perfect for testing. Watch how many runs that is in one week. Over ten thousand.",
     vis=dict(type="cron", expr="* * * * *", means=["every minute", "every hour", "every day", "every month", "any weekday"], cmd="python3 report.py", english="Every minute: great for a quick test")),
dict(chapter="Use full paths", say="Now, one important rule. Cron doesn't run from your folder, and it doesn't know your shortcuts. So we give it full paths. Type which python three, to see exactly where Python lives. Mine is slash user slash local slash bin slash python three. Yours might be different. Copy whatever yours says. And p w d gives the full path of the scripts folder.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("which"), out_gap=0.4)),
dict(chapter="Add the job: crontab -e", say="Type crontab dash e, e for edit. It opens your crontab in a text editor. If it asks you to pick an editor, choose nano, the easiest. On a Mac, type EDITOR equals nano, then crontab dash e, to get the same one. On a new line, type the five stars, a space, the full path to Python, and the full path to the script. At the end, two greater than signs, and a log file. That saves everything the script prints, including errors. Two greater than one sends errors there too. Save and close. In nano, that's control O, enter, then control X.",
     vis=dict(type="code", file="crontab -e", code="# m h  dom mon dow   command\n" + LINE, lang="sh", hl=(2,), size=24, note=">> cron.log 2>&1  =  save output AND errors to a log")),
dict(say="Run crontab dash l again. There's our job. Cron checks this list every minute, so we only have to wait.",
     vis=dict(type="term", title="Terminal — scripts", lines=cr("crontab1"), out_gap=0.4)),
dict(chapter="The mistake that breaks first schedules", say="A minute later, let's check the log. And, an error. File not found, todo dot t x t. But the file is right there. It worked a minute ago. What happened? This is the number one mistake. When cron runs your script, it doesn't start in your scripts folder. It starts in your home folder. So open todo dot t x t looks in the wrong place.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("fail"), out_gap=0.3)),
dict(chapter="The fix: use the script's own folder", say="The fix is two lines. Import Path from pathlib. Then folder equals Path, of underscore underscore file underscore underscore, dot parent. That's the folder where the script itself lives, no matter where it was started from. Now we open folder slash todo dot t x t, and write to folder slash report dot t x t. Use this trick in every script you schedule.",
     vis=dict(type="code", file="report.py", code=src("report.py"), hl=(2, 4, 6, 12), note="Path(__file__).parent = the script's own folder")),
dict(say="Save it, and wait a couple of minutes. Now the report file grows by itself. One line from when I ran it by hand, and then one new line every minute, from cron. No typing at all.",
     vis=dict(type="term", title="Terminal — scripts", lines=T("works"), out_gap=0.4)),
dict(chapter="Every day at 9 AM", say="Every minute was just for testing. To run it once a day, at nine in the morning, change the first two fields. Zero for the minute. Nine for the hour. Then three stars, any day, any month, any weekday. Watch the week fill in. One run a day, at nine o'clock. Seven runs.",
     vis=dict(type="cron", expr="0 9 * * *", means=["at minute 0", "at 9 AM", "every day", "every month", "any weekday"], cmd="python3 report.py", english="Every day at 9:00")),
dict(say="Back in crontab dash e, I replaced the five stars with zero, nine, star, star, star, and saved. Crontab dash l confirms the new schedule.",
     vis=dict(type="term", title="Terminal — scripts", lines=cr("crontab2"), out_gap=0.4)),
dict(chapter="Weekdays only", say="Only on work days? The last field is the day of the week. Zero is Sunday, one is Monday, and so on. So one dash five means Monday to Friday. Thirty, eight, star, star, one dash five. Eight thirty on weekdays. Five runs, and the weekend stays free.",
     vis=dict(type="cron", expr="30 8 * * 1-5", means=["at minute 30", "at 8 AM", "every day", "every month", "Mon to Fri"], cmd="python3 report.py", english="8:30 on weekdays", colors=[SKY, YEL, MINT, CORAL, LIME])),
dict(chapter="Cron cheat sheet", say="Here are the schedules you'll use most. Star slash fifteen in the minute field means every fifteen minutes. Zero, star, star, star, star is every hour, on the hour. Zero nine star star one is Mondays at nine. Zero zero one star star is midnight on the first of every month. And you can list hours with commas, like nine and seventeen, for twice a day.",
     vis=dict(type="cards", title="Cron schedules you'll actually use", cols=3, span=0.7, colors=[ACCENT, YEL, MINT, CORAL, VIO, SKY],
              items=[["* * * * *", "Every minute (for testing)"], ["*/15 * * * *", "Every 15 minutes"], ["0 * * * *", "Every hour, on the hour"],
                     ["0 9 * * 1", "Mondays at 9:00"], ["0 0 1 * *", "Midnight on the 1st"], ["0 9,17 * * *", "Twice a day: 9:00 and 17:00"]])),
dict(chapter="Mistake 2: minute and hour swapped", say="Mistake two. Swapping the first two fields. People write nine, zero, thinking nine o'clock. But the first field is always the minute. So nine, zero means nine minutes past midnight. Your report runs while you sleep. Remember. Minute first, then hour.",
     vis=dict(type="cron", expr="9 0 * * *", means=["at minute 9", "at 0 = midnight", "every day", "every month", "any weekday"], english="Oops: 00:09, not 9:00", engcol=CORAL, colors=[CORAL, CORAL, MINT, SKY, VIO])),
dict(chapter="Windows: Task Scheduler", say="Now Windows. Cron isn't there, but Windows has Task Scheduler built in. First, find Python's full path. Open Command Prompt and type where python. Copy the path it shows, the one ending in python dot e x e. Then open the Start menu, search for Task Scheduler, and open it.",
     vis=dict(type="steps", title="Windows: get ready", items=["Command Prompt:  where python", "Copy the path ending in python.exe", "Start menu: search \"Task Scheduler\"", "Open it, then click Create Basic Task"])),
dict(say="Click Create Basic Task, on the right. Give it a name, like Daily report. Click next. For the trigger, choose Daily, and set the start time, say nine A M. Next, choose Start a program. Now three boxes. Program or script, paste the full path to python dot e x e. Add arguments, type report dot py. And Start in, paste the full path of your scripts folder. Click next, and finish.",
     vis=dict(type="steps", title="Create Basic Task", items=["Name: Daily report  ·  Trigger: Daily, 9:00 AM", "Action: Start a program", "Program/script:  full path to python.exe", "Add arguments:  report.py", "Start in:  your scripts folder  ·  Finish"])),
dict(say="That Start in box is the Windows version of our cron mistake. It sets the folder the script starts in. Leave it empty, and Windows starts somewhere else, and you get the same file not found error. With the Path trick in our script, you're safe either way.",
     vis=dict(type="tip", tag="WATCH OUT", text="Fill in \"Start in\" with your script's folder. Empty = the script starts in the wrong folder.", color=CORAL)),
dict(say="To test it, find your task in the Task Scheduler Library, right click it, and choose Run. Then look at the Last Run Result column. The operation completed successfully, zero x zero, means it worked. Any other code means the script failed, so check the paths.",
     vis=dict(type="cards", title="Test it on Windows", cols=3, span=0.55, colors=[ACCENT, MINT, CORAL],
              items=[["Right-click > Run", "Runs the task right now"], ["0x0", "Last Run Result: success"], ["Other code", "Failed: check the paths"]])),
dict(chapter="Mistake 3: the computer was asleep", say="Mistake three. A scheduler can only run while the computer is on. If your laptop is asleep at nine, cron simply skips that run. On Windows, open the task's properties, go to the Settings tab, and tick, run task as soon as possible after a scheduled start is missed. Or pick a time when your computer is usually awake.",
     vis=dict(type="compare", title="If the computer is off at 9:00", left=("cron (Mac, Linux)", ["The run is skipped", "Pick a time you're usually on", "Or use a server that's always on"]),
              right=("Task Scheduler", ["Properties > Settings tab", "Tick: run as soon as possible", "after a missed start"]))),
dict(chapter="Pro tips", say="Pro tip one. Always keep the log. Without it, when a scheduled script fails, it fails silently, and you won't know for weeks. With two greater than signs and a log file, one look tells you what went wrong. Pro tip two. To change or stop a job, use crontab dash e, and edit or delete the line. Careful with crontab dash r. It deletes your whole crontab, with no question asked.",
     vis=dict(type="tip", tag="PRO TIP", text="Always log: >> cron.log 2>&1. To stop a job, delete its line in crontab -e. Avoid crontab -r: it erases everything.", color=ACCENT)),
dict(say="And on a Mac, if your script reads files in Desktop, Documents or Downloads, macOS privacy settings may block cron. The simple fix is to keep your scheduled scripts and their files in their own folder, like scripts in your home folder, just like we did.",
     vis=dict(type="tip", tag="MAC NOTE", text="macOS may block cron from Desktop, Documents and Downloads. Keep scheduled scripts in their own folder, like ~/scripts.", color=YEL)),
dict(chapter="Recap", say="Quick recap. Run the script by hand first. Use Path of underscore underscore file, dot parent, for every file it opens. On Mac and Linux, crontab dash e, five time fields, full paths, and a log. Minute first, then hour. On Windows, Create Basic Task, the path to python, your script as the argument, and fill in Start in.",
     vis=dict(type="steps", title="Recap", items=["Test by hand  ·  use Path(__file__).parent", "crontab -e  ·  minute hour day month weekday", "Full paths + >> cron.log 2>&1", "0 9 * * *  =  every day at 9:00", "Windows: Create Basic Task + Start in"])),
dict(say="Next on Shortcut Lab, the V S Code shortcuts that save hours. Edit ten lines at once, jump anywhere in a second, and stop reaching for the mouse. Subscribe, so you don't miss it.",
     vis=dict(type="outro", next="VS Code Shortcuts That Save Hours")),
]
