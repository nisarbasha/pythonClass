input_1 = int(input("Enter the value of input_1: "))
input_2 = int(input("Enter the value of input_2: "))


def addition_operation():
    c = input_1 + input_2
    print(f"The sum of the value is: {c}")


def subtraction_operation():
    addition_operation()
    d = input_1 - input_2
    print(f"The subtraction result is: {d}")


def division_operation():
    div = input_1 / input_2
    return div


def flor_division_operation(a: int, b: int):
    result = a / b
    print(f"The flor division result is: {result}")


x = lambda a, b: a * b

print(x(a=20, b=40))


def myfunc(n, a):
    return lambda a: a * n


subtraction_operation()
print(myfunc(10, 20))