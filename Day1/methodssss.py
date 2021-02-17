def get_input():

    try:
        a = int(input("Enter the value"))
        b = int(input("Enter the value 2nd value"))
        print(a/b)
    except:
        print("Enter correct value")
        get_input()
    print(a + 1)


if __name__ == '__main__':
    get_input()