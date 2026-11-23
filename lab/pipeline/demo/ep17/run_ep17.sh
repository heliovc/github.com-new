#!/bin/bash
# Runs every EP17 script for real against the local practice shop and writes transcript.txt (sections "### name").
# Usage: bash run_ep17.sh <work dir>
set -u
D="$(cd "$(dirname "$0")" && pwd)"; W="${1:-$HOME/lab/ep17work}"
rm -rf "$W"; mkdir -p "$W/project"; python3 "$D/make_site.py" "$W/site" >/dev/null
cp "$D"/*.py "$W/project/"; rm "$W/project/make_site.py"
(cd "$W/site" && python3 -m http.server 8000 > "$W/server.log" 2>&1 &) ; sleep 1.5
OUT="$D/transcript.txt"; : > "$OUT"
sec() { echo "### $1" >> "$OUT"; }
cd "$W/project"
sec versions; python3 versions.py >> "$OUT" 2>&1
for s in get_page soup_title select_books one_book bad_none bad_404 bad_js reviews_json scraper analyze robots; do sec $s; python3 $s.py >> "$OUT" 2>&1; done
sec head; head -4 books.csv >> "$OUT"
sec timing; TIMEFORMAT="%R s"; { time python3 scraper.py > /dev/null ; } 2>> "$OUT"
sec server; tail -5 "$W/server.log" | sed -E 's/\[[^]]*\]/[date]/' >> "$OUT"
cp books.csv "$D/books.csv"
pkill -f "http.server 8000" ; echo done
