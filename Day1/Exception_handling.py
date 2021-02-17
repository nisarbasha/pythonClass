
try:
    print(x)
except Exception as e:
    print("An exception occurred", e)
    print("HI")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

age = int(input("Enter the age"))
if age > 18:
    print("Age Is Valid")
else:
    raise Exception("Sorry, Age Is Not Valid")
