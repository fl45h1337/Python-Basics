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


    # Python code to demonstrate working of
    # center(), ljust() and rjust()


    str = "geeksforgeeks"

    # Printing the string after centering with '-'
    print("The string after centering with '-' is : ", end="")
    print(str.center(20, '-'))

    # Printing the string after ljust()
    print("The string after ljust is : ", end="")
    print(str.ljust(20, '-'))

    # Printing the string after rjust()
    print("The string after rjust is : ", end="")
    print(str.rjust(20, '-'))