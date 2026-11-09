#!/bin/bash
# EP05 demo: every git command shown in the video, run for real. Output -> captured transcript.
rm -rf /home/sam && mkdir -p /home/sam && export HOME=/home/sam GIT_PAGER=cat TERM=dumb
unset GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL EMAIL
cd /home/sam && mkdir budget && cd budget
run(){ echo "\$ $*"; eval "$@" 2>&1; }
cat > budget.py <<'EOF'
income = 3000
rent = 1200
food = 450

left = income - rent - food
print("Left this month:", left)
EOF
echo "### S1"; run git --version
echo "### S2"; run git status
echo "### S3"; run git config --global user.name '"Sam Rivera"'; run git config --global user.email sam@example.com; run git config --global init.defaultBranch main
echo "### S4"; run git init; run git status
echo "### S5"; run git add budget.py; run git status
echo "### S6"; run git commit -m '"First version of budget"'; run python3 budget.py; sleep 1
cat > budget.py <<'EOF'
income = 3000
rent = 1200
food = 450
transport = 120

left = income - rent - food - transport
print("Left this month:", left)
EOF
echo "### S7"; run git status --short; run git diff
echo "### S8"; run git add budget.py; run git commit -m '"Add transport costs"'; sleep 1
cat > budget.py <<'EOF'
income = 3000
rent = 1200
food = 450
transport = 120
fun = 200

left = income - rent - food - transport - fun
print("Left this month:", left)
EOF
run git add budget.py; run git commit -m '"Add fun money"'
echo "### S9"; run git log --oneline
# accident: the food line gets deleted by mistake
sed -i '/^food = 450$/d' budget.py
echo "### S10"; run python3 budget.py; run git status --short
echo "### S11"; run git restore budget.py; run python3 budget.py
echo "### S12"; H1=$(git rev-list --max-parents=0 --abbrev-commit HEAD); run git restore --source=$H1 budget.py; run python3 budget.py; run git restore budget.py; run python3 budget.py
# bad commit + revert
sed -i 's/food = 450/food = 4500/' budget.py; git add budget.py; git commit -q -m "Update food budget"
echo "### S13"; run python3 budget.py; run git log --oneline
echo "### S14"; run git revert --no-edit HEAD; run python3 budget.py; run git log --oneline
echo "### S15"; touch notes.log; mkdir -p __pycache__; touch __pycache__/budget.cpython-312.pyc; run git status --short
printf 'notes.log\n__pycache__/\n' > .gitignore
run cat .gitignore; run git status --short; run git add .gitignore; run git commit -m '"Ignore logs and cache"'
echo "### S16"; run git switch -c savings; sleep 1
sed -i 's/^fun = 200/fun = 200\nsavings = 300/; s/ - fun$/ - fun - savings/' budget.py
run git commit -am '"Try a savings goal"'; run python3 budget.py; run git switch main; run python3 budget.py; run git merge savings; run python3 budget.py; run git log --oneline --graph
echo "### MIST1"; mkdir -p /home/sam/other && cd /home/sam/other && run git commit -m '"oops"'
echo "### MIST2"; cd /home/sam/budget && run git commit -m '"nothing new"'
echo "### MIST3"; export HOME=/tmp/noid; rm -rf /tmp/noid; mkdir -p /tmp/noid/proj; cd /tmp/noid/proj; git init -q; echo hi > a.txt; git add a.txt; run git commit -m '"First"'
