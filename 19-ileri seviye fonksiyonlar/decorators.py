# bir ozelligi bir kac kez kullanmak istiyorsak bu fonksiyon turunu kullaniriz.
print("1. ornek".center(50,'*'))
def myDecorator(func):
    def wrapper():
        print("fonksiyondan onceki islemler")
        func()
        print("fonksiyondan sonraki islemler.")
    return wrapper



@myDecorator # burada ustteki fonk. ozelligini kullanmak icin bunu kullaniriz.
def sayHello():
    print("hello")

sayHello()

print("****************************************")

@myDecorator
def sayMerhaba():
    print("Merhaba")

sayMerhaba()

print("2. ornek".center(50,'*'))

import math
import time

def calculateTime(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1) # 1 saniye islemi geciktirmeli yapiyoruz.
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon "+str(finish-start) + " saniye surdu.")
    return inner

@calculateTime
def usAlma(a,b):
    print(math.pow(a,b))

@calculateTime
def factoriel(num):
    print(math.factorial(num))

@calculateTime
def toplama(a,b):
    print(a+b)
   
usAlma(3,4)
print('-------------------------------------')
factoriel(5)
print('-------------------------------------')
toplama(5,6)
print('-------------------------------------')
