# map kullanimi:
def square(num):
    return num**2

numbers=[1,2,3,4,5]
result=list(map(square,numbers))
print(result)

print('************************************************')


#lambda kullanimi:

sayilar=[2,3,4,5,6,7]

sonuc=list(map(lambda num: num**2,sayilar))
print(sonuc)

print('************************************************')

result1=square(10)
print(result1)

print('************************************************')

#filter kullanimi:

numaralar=[1,2,3,4,5,6,7,8,9,10]
def checkEven(num): 
    return num%2==0

sonuc1=list(filter(checkEven,numaralar))
print(sonuc1)

sonuc2=list(filter(lambda num:num%2==0,numaralar))#tek satir ile de yapilabilir.
print(sonuc2)


