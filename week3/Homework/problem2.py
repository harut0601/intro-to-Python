#Problem 1
a1 = ["Cookies", "Chocolate",8, True, -3, -5, "Chocolate", 8, False, 8]

#Problem 2
b1 = [8, True, 10, 14,"Chocolate", "Milk", "Jelly", True, False, True]

#Problem 3
set_a = set(a1)
print(set_a)

#Problem 4
set_b = set(b1)
print(set_b)

#Problem 5
union_ab = set_a.union(set_b)
print(union_ab)

#Problem 6
intersection_ab = set_a.intersection(set_b)
print(intersection_ab)

#Problem 7
a1b1 = a1 + b1
set_a1b1 = set(a1b1)
set_a1b1.add('kit-kat')
set_a1b1.add('Oreo')
print(set_a1b1)

#Problem 8
new_set = union_ab or intersection_ab
print(new_set)

#Problem 9
print('Chocolate' in new_set)

#Problem 10
set_a1b1.remove('Oreo')
print(set_a1b1)