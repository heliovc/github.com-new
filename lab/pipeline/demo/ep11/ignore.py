import re

text = open("inbox.txt").read()

print(re.findall(r"invoice \d+", text))
print(re.findall(r"invoice \d+", text, re.IGNORECASE))
