from datetime import datetime

tasks = open("todo.txt").read().splitlines()
open_tasks = [t for t in tasks if t.startswith("[ ]")]

now = datetime.now().strftime("%Y-%m-%d %H:%M")
line = f"{now}  {len(open_tasks)} open tasks\n"

with open("report.txt", "a") as f:
    f.write(line)
print(line, end="")
