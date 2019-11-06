#Problem 1
t1 = (1, True, "a", -2, "Anna")
print(t1)

#Problem 2
t1_copy = set(t1)
t1_copy.remove(True)
print(tuple(t1_copy))

#Problem 3
t2 = (1, 2, 3, 4, 5)

#Problem 4
t3_start = t1[0:2]
t3_end = t2[0:3]
t3_new = t3_start + t3_end
t3 = tuple(t3_new)
print(f"The new tuple: {t3}")

#Problem 5
print(f"2nd index: {t3[2]}")

#Problem 6
t4 = [(1, 3, 5), (8, 9), ("Anna", "Bob", "Alice")]
print(f"0 1 index: {t4[0][1]}")
