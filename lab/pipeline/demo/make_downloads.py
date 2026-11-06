import os, time, sys
from pathlib import Path
from datetime import datetime
base = Path(sys.argv[1]); d = base / "Downloads"; d.mkdir(parents=True, exist_ok=True)
files = {"IMG_2041.JPG": "2026-09-14", "budget.xlsx": "2026-10-03", "clip.mp4": "2026-11-01", "data.csv": "2026-10-21",
 "font.ttf": "2026-09-30", "invoice_october.pdf": "2026-10-31", "meme.gif": "2026-11-02", "photos_backup.zip": "2026-09-05",
 "podcast_ep12.mp3": "2026-10-12", "report.txt": "2026-11-03", "resume.docx": "2026-09-22", "screenshot.png": "2026-11-04",
 "setup.zip": "2026-10-08", "voice_memo.wav": "2026-11-05"}
for n, day in files.items():
    p = d / n; p.write_text("report version 1\n" if n == "report.txt" else f"sample {n}\n")
    t = datetime.strptime(day + " 12:00", "%Y-%m-%d %H:%M").timestamp(); os.utime(p, (t, t))
(d / "project-files").mkdir(exist_ok=True); (d / "project-files" / "main.py").write_text("print('hi')\n")
