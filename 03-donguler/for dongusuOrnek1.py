numbers=[1,2,3,4,5]

for num in numbers:
    print(num)

print('----------------------')

names=['Cinar','Sadik','Sena']

for name in names:
    print(name)


print('----------------------')

isim='Huseyin'

for i in isim:
    print(i)

print('----------------------')

d={'k1':1,'k2':2,'k3':3}
 
for item in d.items():#burada parantez olmak zorunda dikkat!!!
    print(item)


print('----------------------')

a={'k4':4,'k5':5,'k6':6}

for key,value in a.items():
    
    print(key)
    print(value)
   

print('----------------------')

tuple=[(1,2),(2,3),(3,4),(4,5)]

for a,b in tuple:
    print(a,b)