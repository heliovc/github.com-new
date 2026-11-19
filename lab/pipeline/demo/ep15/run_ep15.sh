#!/bin/bash
# Runs every EP15 script for real and writes transcript.txt (sections "### name"). Usage: bash run_ep15.sh <work dir>
set -u
D="$(cd "$(dirname "$0")" && pwd)"; W="${1:-$HOME/lab/ep15work}"
rm -rf "$W"; mkdir -p "$W"; python3 "$D/make_messy.py" "$W/project" >/dev/null
cp "$D"/*.py "$W/project/"; rm "$W/project/make_messy.py" "$W/project/export_clean.py"
OUT="$D/transcript.txt"; : > "$OUT"
sec() { echo "### $1" >> "$OUT"; }
cd "$W/project"
sec versions; python3 -c "import pandas; print(pandas.__version__)" >> "$OUT" 2>&1
sec csvhead; head -6 orders.csv >> "$OUT"
for s in look health forgot dupes_order status dates_bad price_bad clean check_clean report; do sec $s; python3 $s.py >> "$OUT" 2>&1; done
sec timing; TIMEFORMAT="%R s"; { time python3 clean.py > /dev/null ; } 2>> "$OUT"
echo done
