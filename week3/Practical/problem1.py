import sys

list1 = ["Hello", 1, True]
list2 = sys.argv[1:]

list1.extend(list2)

print('New list:', list1)
