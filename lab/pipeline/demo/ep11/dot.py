import re

print(re.findall(r"2026.10.03", "2026-10-03 and 2026x10x03"))
print(re.findall(r"2026\.10\.03", "2026.10.03 and 2026x10x03"))
