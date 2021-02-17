import math

x = abs(-7.25)

print(x)
print("***************")
x = pow(5, 3)

print(x)
print("***************")
x = math.sqrt(49)

print(x)
print("***************")

x = math.ceil(1.8)
y = math.floor(1.4)


print(x)
print(y)
print("***************")

x = math.pi

print(x)
print("***************")
print(math.isclose(50, 100, abs_tol=40))
c = float(input("enter your percentage"))
x = math.isclose(c, 1.9, abs_tol=0.2)
if x:
    print("magesh selected")
else:
    print("Not Selected")
