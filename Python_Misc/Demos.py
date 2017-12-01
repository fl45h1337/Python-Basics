#
# ###################################################
# a = ["1", 1, "1", 2]
# a = list(set(a))
# print(a)
#
# ###################################################
# from collections import OrderedDict
# a = ["1", 1, "1", 2]
# a = list(OrderedDict.fromkeys(a))
# print(a)
#
#
#
# from pprint import pprint
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# pprint(d)

# from pprint import pprint
# pprint([[0 for x in range(10)] for y in range(10)])

#
# import string
#
# for letter in string.ascii_lowercase:
#     print(list(letter))
#
#     # Python code to demonstrate working of
#     # center(), ljust() and rjust()
#     str = "geeksforgeeks"
#
#     # Printing the string after centering with '-'
#     print("The string after centering with '-' is : ", end="")
#     print(str.center(20, '-'))
#
#     # Printing the string after ljust()
#     print("The string after ljust is : ", end="")
#     print(str.ljust(20, '-'))
#
#     # Printing the string after rjust()
#     print("The string after rjust is : ", end="")
#     print(str.rjust(20, '-'))

# line = "Geek1 Geek2 Geek3";
# print(line.split(' ', 1))
#
# str1 = ''
# str2 = 'geeks'
#
# # repr is used to print the string along with the quotes
# print(repr(str1 and str2))  # Returns str1
# print(repr(str2 and str1))  # Returns str1
# print(repr(str1 or str2)) # Returns str2
# print(repr(str2 or str1)) # Returns str2
# print(repr(str2 or str1)) # Returns str2

# letters  = []
# check = "p y t h o n"
# for letter in check:
#         letters = check.split(" ")
#         if letter in letter:
#             letters.append(letter)
# # print(letters)
#
# for letter in "Hello":
#     if letter == "e":
#       print(letter)

a = set([2,5])
b = set([2,4,6])

print(a<b)