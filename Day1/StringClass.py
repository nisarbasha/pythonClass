name = ['nisar', 'magesh', 'parthiban', 'lokesh']
k = '  kar,thik'
num = [101, 102, 103, 104, 105, 106]


# String Methods
print(name[1])
print(len(name))
print('lokesh'  in name)
print(k.upper())
print(k.lower())
print(k.strip())
print(k.replace('k', 'p'))
print(k.split(","))
print(max(num))
print(sum(num))

m_nake = 'Parthi'
data = "My \"name\" is \n{}"
print( "my name is {}".format(m_nake))

print(data.format(m_nake))
for record in name:
    if record =='magesh':
        print('record found')

#Slicing Strings
print(k[:5])
print(k[2:6])
print(k[5:])
print(k[-3:-1])


