#1. ornek:

def usAlma(number):
    def inner(power):
        return number ** power
    return inner

two=usAlma(2)   #2-3
three=usAlma(3) #3-4

print(two(3))
print(three(4))

#2. ornek:
print("---------------------------------------")

def yetkiSorgulama(page):
    def inner (role):
        if role=='Admin':
            return "{0} rolu {1} sayfasina ulasabilir.".format(role,page)
        else:
            return "{0} rolu {1} sayfasina ulasamaz.".format(role,page)
    return inner  

user1=yetkiSorgulama("Product Edit")
print(user1("Admin"))
print(user1("User"))

#3. ornek:
print("---------------------------------------")

def islem(islemAdi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    
    if(islemAdi=="toplama"):
        return toplam
    else:
        return carpma
    
toplama=islem("toplama")
print(toplama(1,2,3,4,5))

carpma=islem("carpma")
print(carpma(3,4,5,6))

#Bu konu cok onemlidir.