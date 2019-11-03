import sys

list1 = ["Hello", 1, True]

list2 = list1.copy()

list2.extend(sys.argv[1:])

print("Old arguments:", list1)
print("New arguments:", list2)