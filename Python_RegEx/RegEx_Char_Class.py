import re

# For AA1

pattern = r"[A-Z][A-Z][0-9]"

if re.match(pattern,"AD2"):
    print("Match Found!")

if re.match(pattern,"ASA"):
    print("Match Found!")
else:
    print("Match Not Found!")