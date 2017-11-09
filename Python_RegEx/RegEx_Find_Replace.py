import re

someString = "My name is Harshiv, hello sir!"
pattern = r"Harshiv"

replacedString = re.sub(pattern,"John", someString)

print(replacedString)