from multipledispatch import dispatch


class demoo:

    @dispatch(int, int)
    def product(a, b):
        p = a * b
        print(p)

    @dispatch(int, int, int)
    def product(a, b, c):
        p = a * b * c
        print(p)


if __name__ == '__main__':
    obj = demoo
    obj.product(4, 6)
