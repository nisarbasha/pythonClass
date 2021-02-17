class Biggest:
    def __init__(self):
        self.a = int(input("Enter the 'a' value: "))
        self.b = int(input("Enter the 'b' value: "))


    def display(self):
        if self.a > self.b:
            print("the biggest value is 'a' {}".format(self.a))
        else:
            print("The biggest value is 'b' {}".format(self.b))



b = Biggest()

b.display()

