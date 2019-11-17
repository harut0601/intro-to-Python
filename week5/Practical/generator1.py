def list_func(list1):
    for element in list1:
        print(element)
        yield(element)


a = list_func([1, 6, 7, 6])
c = 0

while c < 4:
    next(a)
    c += 1