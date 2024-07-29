def sayHello(name):
    print("Hello "+name)

sayHello("Ahmet")
sayHello("Mehmet")

print('-----------------------------')

def sayMrb(name='user'):
    return 'Hello '+name
msg1=sayMrb('Mert')
msg2=sayMrb('Fuat')
print(msg1)
print(msg2)

print('-----------------------------')

def total(num1,num2):
    return num1+num2
result1=total(10,20)
result2=total(15,25)

print(result1)
print(result2)

print('-----------------------------')

def yasHesapla(dogumYili):
    return 2024-dogumYili
ageCinar=yasHesapla(2000)
ageNur=yasHesapla(1990)
print(ageNur)
print(ageCinar)

print('-----------------------------')

def EmekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING:Dogum yilina gore emeklilige kac yil kaldi.
    INPUT: Dogum yili.
    OUTPUT:Hesaplanan yil bilgisi.
    '''
    yas=yasHesapla(dogumYili)#fonk icinde fonk cagirma
    emeklilik=65-yas

    if(emeklilik>0):
        print(f"Emekliliginize {emeklilik} yil kaldi.")
    else:
        print("Zaten emekli oldunuz.")

EmekliligeKacYilKaldi(1993,"Ali")
EmekliligeKacYilKaldi(1970,"Berk")
EmekliligeKacYilKaldi(1925,"Ahmet")

#help(EmekliligeKacYilKaldi) # bu calisritilirsa fonk.un ne ise yaradigini aciklar.Ust tarafta yazdigimiz aciklamayi konsolda yazar.

print('-----------------------------')






