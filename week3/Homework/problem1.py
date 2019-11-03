#Problem1
a = [1, 4, 5, 7, 8, -2, 0, -1]
#Problem2
print(a[3], a[5])

#Problem3
a_sorted = a.copy()
a_sorted.sort(reverse=True)
print(a_sorted)

#Problem4
print(a_sorted[0:3])
print(a_sorted[2:6])

#Problem5
print(a_sorted)
a_sorted.pop(3)
a_sorted.pop(2)
print(a_sorted)

#Problem6
b = ["grapes", "Potatoes","tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]

#Problem7
b_sorted = b.copy()
b_sorted.sort()
print(b_sorted)

#Problem8
c_first = a[0:2]
c_second = b[3:6]
print(c_first + c_second)
