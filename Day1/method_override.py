class Add:
    def result(self):
        self.a = 20
        self.b = 30
        self.c = self.a + self.b
        print(self.c)


class HelloWorld(Add):
    def __init__(self):
        super().result()

    def result(self):
        print("Hello world")


if __name__ == '__main__':
    obj = HelloWorld()
    obj.result()
