class BIX:

    def printmessage(self):
        print("Nisar")


class Training(BIX):
    def __init__(self, txt):
        super().printmessage()

    def printmessage(self):
        print("Hello, and welcome!")


x = Training("nisar")

x.printmessage()
