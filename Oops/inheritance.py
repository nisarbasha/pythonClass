class Biggest:
    def __init__(self):
        self.a = int(input("Enter the 'a' value: "))
        self.b = int(input("Enter the 'b' value: "))

    def display(self):
        if self.a > self.b:
            print("the biggest value is 'a' {}".format(self.a))
        else:
            print("The biggest value is 'b' {}".format(self.b))


class Reverse(Biggest):
    def __init__(self):
        super().__init__()
        self.c = self.a + self.b
        self.reverse = 0
        self.temp = 0

    def display_1(self):
        while self.c > 0:
            self.temp = self.c % 10
            self.reverse = self.reverse * 10 + self.temp
            self.c = self.c // 10
        print("The reversed number is {}".format(self.reverse))


if __name__ == '__main__':
    obj = Reverse()
    obj.display()
    obj.display_1()
