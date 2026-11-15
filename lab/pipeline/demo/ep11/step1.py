import re

text = open("inbox.txt").read()

print(re.findall(r"Invoice", text))
print(re.findall(r"\d+", text))
