dic = {"name": "Nisar", "age": "25", "location": "chennai"}

dic1 = {"name": ['nisar', 'nisar', 'karthi', 'parthiban'], "age": ['25', '30','32']}
print(dic1)
print(dic1['name'])
record = dic1['name']

print(dic)
print(dic.keys())
print(dic.values())

for i in record:
    if i == 'karthi':
        print(record)
