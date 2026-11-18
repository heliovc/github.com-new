#!/bin/bash
# Runs every EP14 script for real and writes transcript.txt (sections "### name"). Usage: bash run_ep14.sh <work dir>
set -u
D="$(cd "$(dirname "$0")" && pwd)"; W="${1:-$HOME/lab/ep14work}"
rm -rf "$W"; mkdir -p "$W"; python3 "$D/make_files.py" "$W/project" >/dev/null
cp "$D"/*.py "$W/project/"; rm "$W/project/make_files.py"
OUT="$D/transcript.txt"; : > "$OUT"
sec() { echo "### $1" >> "$OUT"; }
cd "$W/project"
sec versions; python3 -c "import pandas, openpyxl; print(pandas.__version__, openpyxl.__version__)" >> "$OUT" 2>&1
sec ls; ls reports | head -3 >> "$OUT"; echo "..." >> "$OUT"; ls reports | tail -2 >> "$OUT"; ls reports | wc -l >> "$OUT"
sec peek; python3 peek.py >> "$OUT" 2>&1
sec wrong_folder; (cd "$W" && python3 project/merge.py) >> "$OUT" 2>&1
sec merge; python3 merge.py >> "$OUT" 2>&1
sec check; python3 check.py >> "$OUT" 2>&1
sec find_bad; python3 find_bad.py >> "$OUT" 2>&1
printf '\x0bOffice User  \x00' > "reports/~\$2026-11_store04.xlsx"   # stand-in for the hidden lock file Excel leaves while a workbook is open
sec lockfile; python3 merge.py >> "$OUT" 2>&1
sec merge_final; python3 merge_final.py >> "$OUT" 2>&1
sec check2; python3 check.py >> "$OUT" 2>&1
sec summary; python3 summary.py >> "$OUT" 2>&1
sec sheets; python3 sheets.py >> "$OUT" 2>&1
sec sheets_tag; python3 sheets_tag.py >> "$OUT" 2>&1
sec timing; TIMEFORMAT="%R s"; { time python3 merge_final.py > /dev/null ; } 2>> "$OUT"
echo done
