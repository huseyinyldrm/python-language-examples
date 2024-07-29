#1- Gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyon yazin.

def kelimeYazma(kelime,sayi):
    for i in range(sayi):
        print((i+1),'. tekrar=',kelime)

kelime=input("Bir kelime giriniz:")
sayi=int(input("Kac kez tekrar istiyorsunuz:"))
kelimeYazma(kelime,sayi)

print('************************************************')
#2-kendine gonderilen sinirsiz sayidaki parametreyi bir listeye ceviren fonksiyon yaziniz.

def parametreDondurme(*args):#sinirsiz sayida parametre gondermek icin * konuldu.
    liste=[]
    for i in args:
        liste.append(i)
    print(liste)

parametreDondurme(10,20,30,40,50)
print('---------------------')
parametreDondurme(2,3,4,5,5,5,7)

print('************************************************')
#3-gonderilen iki sayi arasindaki tum asal sayilari bulun.

def asalBul(sayi1,sayi2):
    a=1
    for sayi in range(sayi1,sayi2+1):
        if(sayi>1):
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
            else:
                print((a),'. asalSayi:',sayi)
                a+=1

sayilar1=int(input("1.sayiyi giriniz:"))
sayilar2=int(input("2.sayiyi giriniz:"))

asalBul(sayilar1,sayilar2)

print('************************************************')
#4-kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde donduren fonksiyon yaziniz.

def bolenleriBulma(sayi):
    liste=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            liste.append(i)
    return liste

sayi=int(input("Bir sayi giriniz:"))
print(bolenleriBulma(sayi))

print('************************************************')