def changeName(n):
    n='Ada'
    print(n)

name='Yigit'
changeName(name)
print(name)

print('-----------------------------')
def change(n):
    n[0]='Istanbul'

sehirler=['Ankara','Izmir']

change(sehirler[:])
print(sehirler)

print('-----------------------------')

def add(a,b,c=0):# istendigi zaman 2 parametre istendigin zaman 3 parametre gonderilir.
    return sum((a,b))

print(add(10,20))
print(add(3,6))
print(add(3,4,5))

print('-----------------------------')

def add(*params):#istedigin kadar parametre gonderir.list gondermek icin
    sum=0

    for n in params:
        sum=sum+n

    return sum

print(add(10,20,50))
print(add(30,45))
print(add(1,2,3,4,5,6,7,8,9))

print('-----------------------------')

def displayUser(**args):#dictionary kullanmak icin
    for key,value, in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Cinar',age=2,city='istanbul')
print('--------------------------------------------------')
displayUser(name='Can',age=12,city='kocaeli',phone='12334')
print('--------------------------------------------------')
displayUser(name='Yigit',age=23,city='ankara',phone='1443')
print('--------------------------------------------------')

print('**************************************************')

def myFunc(a,b,c,*args,**keywords):
    print(a)
    print(b)
    print(c)
    print(args)
    print(keywords)

myFunc(10,20,30,40,50,key1='value1',key2='value2')