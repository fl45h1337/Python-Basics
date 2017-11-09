import re

pattern = r"Harshiv"

if re.match(pattern,"HarshivMynameisHarshiv"):
    print("Match found!")
else:
    print("Match not found!")

if re.match(pattern, "My name is Harshiv"):
    print("Match found!")
else:
    print("Match not found!")

if re.match(pattern,"MynameisHarshiv"):
    print("Match found!")
else:
    print("Match not found!")

