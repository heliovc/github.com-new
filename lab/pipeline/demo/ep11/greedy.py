import re

line = "Colors: <red> and <blue>"

print(re.findall(r"<.*>", line))
print(re.findall(r"<.*?>", line))
