
###################################################
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

###################################################
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)



from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)

# from pprint import pprint
# pprint([[0 for x in range(10)] for y in range(10)])


import string

for letter in string.ascii_lowercase:
    print(list(letter))