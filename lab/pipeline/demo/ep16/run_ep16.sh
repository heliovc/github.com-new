#!/bin/bash
# Runs every EP16 script for real and writes transcript.txt (sections "### name"). Usage: bash run_ep16.sh <work dir>
set -u
D="$(cd "$(dirname "$0")" && pwd)"; W="${1:-$HOME/lab/ep16work}"
rm -rf "$W"; mkdir -p "$W"; python3 "$D/make_messy.py" "$W/project" >/dev/null
cp "$D"/*.py "$W/project/"; rm "$W/project/make_messy.py" "$W/project/export_xlsx.py"
OUT="$D/transcript.txt"; : > "$OUT"
sec() { echo "### $1" >> "$OUT"; }
cd "$W/project"
python3 clean.py > /dev/null
sec versions; python3 -c "import pandas, openpyxl; print(pandas.__version__, openpyxl.__version__)" >> "$OUT" 2>&1
for s in look month_bad summary pivot sheets_bad index_bad report_v1; do sec $s; python3 $s.py >> "$OUT" 2>&1; done
cp report.xlsx report_v1.xlsx
for s in report check name; do sec $s; python3 $s.py >> "$OUT" 2>&1; done
sec timing; TIMEFORMAT="%R s"; { time python3 report.py > /dev/null ; } 2>> "$OUT"
python3 "$D/export_xlsx.py" . "$D/xlsx.json"
echo done
