import re

a = "Welcome to BIX IT ACADEMY"

x = re.split("\s", a)
print(x)

x = re.split("\s", a, 2)
print(x)

x = re.sub("\s", "#",a, 2)
print(x)

x = re.search("o", a)
print(x.string)
print(x.group())


x = re.findall("o", a)
print(x)

list = ['8122330536', '9551110186', '2564785546', '5043552091']
for record in list:
    if re.match(r'[789]\d{9}$', record):
        print(record)

