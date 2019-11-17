def power(max):
    b = yield(max)
    next(max)
    2 ** b


power(5)