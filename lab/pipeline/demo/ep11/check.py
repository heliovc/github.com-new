import re

codes = ["AB-1234", "ab-1234", "AB-12345", "XAB-1234"]

for code in codes:
    if re.fullmatch(r"[A-Z]{2}-\d{4}", code):
        print(code, "valid")
    else:
        print(code, "invalid")
