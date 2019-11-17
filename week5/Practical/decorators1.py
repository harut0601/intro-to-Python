def decorator2(func):
    def wrapper(*args, **kwargs):
        b = func(*args, **kwargs)
        c = "!!! Welcome to the party."
        print(b + c)
    return wrapper


def decorator1(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        return a.capitalize()
    return wrapper


@decorator2
@decorator1
def hi_everyone():
    return "HI EVERYONE"


hi_everyone()
