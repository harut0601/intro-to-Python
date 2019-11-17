list1 = ['Anna', 'Edgar']


def decorator(func):
    def wrapper(*args, **kwargs):
        print(list1)
        list5 = func(*args, **kwargs)
        print(list5)
    return wrapper


@decorator
def add_values(list2):
    return list1 + list(set(list2).difference(list1))


values = add_values([1, 3, 5])

