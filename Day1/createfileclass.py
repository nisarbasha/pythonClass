
try:
    f = open("sample1.txt", "x")
    f.close()
    print("succes")
except Exception as e:
    print(e)

