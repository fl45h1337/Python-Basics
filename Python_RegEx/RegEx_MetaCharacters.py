import re

#Dot MetaCharacter

print("------ Dot Character -----")

pattern = r"g.ld"

if re.match(pattern,"gold"):
    print("Match Found!")
else:
    print("Fail!")

if re.match(pattern, "glad"):
    print("Match Found!")
else:
    print("Glad is not a match")
print("------------------")

#Carat/Dollar Characters
print()
print("------ Carat / Dollar Character -----")

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match Found!")

if re.match(pattern,"graddy"):
    print("Match Found!")
else:
    print("Match not Found!")

if re.match(pattern,"gray"):
    print("Match Found!")

print("---------------------------")

print()
print("------ Star Character -----")

pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbacon"):
    print("Matched!")

if re.match(pattern, "eggsbaconbacon"):
    print("Matched!")

if re.match(pattern, "baconeggsbaconbacon"):
    print("Matched!")
else:
    print("Not matched!")

print("---------------------------")