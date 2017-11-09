import re

pattern = r"Harshiv"

if re.search(pattern,"Do you want something to eat, Harshiv?"):
    print("Match found!")
else:
    print("Match not found!")

if re.search(pattern,"Do you want something to eat, sir?"):
    print("Match found!")
else:
    print("Match not found!")

if re.findall(pattern, "Do you want something to eat, Harshiv?"):
    print("Match found!")
else:
    print("Match not found!")

