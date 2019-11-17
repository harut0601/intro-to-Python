import pretty_print as pp


def calculate_cube(x):
    return x**3


def calculate_square(x):
    return x**2


def main(x):
    print(str(pp.simple_print(str(calculate_square(x)))))
    print(str(pp.pro_print(str(calculate_cube(calculate_square(x))))))


if __name__ == '__main__':
    main(2)
