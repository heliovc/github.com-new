import re

text = open("inbox.txt").read()

emails = re.findall(r"[\w.+-]+@[\w-]+\.\w+", text)
for email in emails:
    print(email)
