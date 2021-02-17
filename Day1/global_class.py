class BIX:
    a = 15
    global b1

    def display(self):
        global  c1
        c1=10
        b1 = 10
        print(BIX.a + b1)

    def display1(self):
        print(b1)
b=BIX()
b.display()
b.display1()