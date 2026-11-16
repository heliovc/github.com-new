from datetime import datetime
from pathlib import Path

folder = Path(__file__).parent  # the folder this script lives in

tasks = (folder / "todo.txt").read_text().splitlines()
open_tasks = [t for t in tasks if t.startswith("[ ]")]

now = datetime.now().strftime("%Y-%m-%d %H:%M")
line = f"{now}  {len(open_tasks)} open tasks\n"

with open(folder / "report.txt", "a") as f:
    f.write(line)
print(line, end="")
