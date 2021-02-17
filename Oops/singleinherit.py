class one:

    def __init__(self):
        self.a = 'nisar'

    def display(self):
        self.b= 20
        print(self.a)


class two(one):

    def display(self):
        print(self.a)
        print('BIX')


class three(two):

    def display3(self):
        print("third class")


if __name__ == '__main__':
    obj = three()
    obj.display()
    obj.display3()

