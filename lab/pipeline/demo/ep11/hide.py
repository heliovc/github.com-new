import re

text = open("inbox.txt").read()

safe = re.sub(r"\d{3}-\d{3}-(\d{4})", r"XXX-XXX-\1", text)
print(safe)
