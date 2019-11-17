def iter_num(n):
    c = 0
    while c < n/2 + 1:
        for element in range(1, n+1):
            print(element)
            yield(element)
            c += 1


a = iter_num(10)
c = 0

while c < 1:
    next(a)
    c += 1