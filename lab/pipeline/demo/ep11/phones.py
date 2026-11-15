import re

text = open("inbox.txt").read()

phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(phones)
print(len(phones), "phone numbers")
