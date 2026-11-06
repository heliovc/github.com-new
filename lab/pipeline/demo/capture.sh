set -e
cd /home/claude/lab/demo/sorter
L() { COLUMNS=86 ls -C -T 0 "$@"; }
rm -rf Downloads; python3 ../make_downloads.py .
echo "### ls0"; L Downloads
echo "### step1"; python3 step1.py
echo "### dry"; python3 dryrun.py
echo "### real"; python3 sort_v1.py; echo "### lsreal"; L Downloads
echo "### cat1"; cat Downloads/Documents/report.txt
echo "report version 2" > Downloads/report.txt
echo "### run_v1_again"; python3 sort_v1.py
echo "### cat2"; cat Downloads/Documents/report.txt
# unique test (final script)
rm -rf Downloads; python3 ../make_downloads.py .; python3 sort_downloads.py > /tmp/final1.txt
echo "### final1"; cat /tmp/final1.txt
echo "report version 2" > Downloads/report.txt
echo "### final_unique"; python3 sort_downloads.py; echo "### lsdocs"; L Downloads/Documents
echo "### catboth"; cat "Downloads/Documents/report.txt" "Downloads/Documents/report (1).txt"
echo "report version 3" > Downloads/report.txt; echo partial > Downloads/movie.mp4.crdownload; echo x > Downloads/.DS_Store
echo "### lsA_before"; COLUMNS=86 ls -A -C -T 0 Downloads
echo "### final_skip"; python3 sort_downloads.py; echo "### lsA"; COLUMNS=86 ls -A -C -T 0 Downloads
rm -rf Downloads; python3 ../make_downloads.py .
echo "### month"; python3 by_month.py; echo "### lsmonth"; L Downloads
