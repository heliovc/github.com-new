import re

text = open("inbox.txt").read()

for year, month, day in re.findall(r"(\d{4})-(\d{2})-(\d{2})", text):
    print(f"{day}/{month}/{year}")
