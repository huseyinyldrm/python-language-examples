# setler direkt olarak indekslenemez.for dongusu gerekir.
# bir eelman liste içinde varsa bir daha ekleme yapmaz.

fruits={'orange','apple','banana'}

for i in fruits:
    print(i)

fruits.add('watermelon')
fruits.add('cherry')

fruits.update(['mango','grape','apple'])
fruits.remove('mango')
fruits.discard('apple')#ucu de eleman silmeye yarar.
fruits.pop()
print(fruits)

print('---------------------------')
fruits.clear()
print(fruits)


myList=[1,2,2,3,4,4,5,6,7,6,7,6]
print(set(myList))