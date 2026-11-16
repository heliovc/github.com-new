#!/bin/bash
# usage: cap.sh SECTION "cmd1" "cmd2" ...   (runs as alex in /home/alex/scripts, appends to transcript)
T=/root/lab/demo/transcript.txt; sec=$1; shift
echo "### $sec" >> $T
for c in "$@"; do
  echo "\$ $c" >> $T
  su - alex -c "cd ~/scripts && $c" >> $T 2>&1
done
