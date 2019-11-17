def power(max):
    for element in range(0, max+1):
        yield(2**element)


new = power(10)
print(next(new))