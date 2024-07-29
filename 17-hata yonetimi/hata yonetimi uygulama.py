
#1-liste elemanlari icindeki sayisal degerleri bulun.

def sayisalDegerBul(liste):
    import re
    sayisalListe=[]
    
    for eleman in liste:
        if eleman.isdigit(): # Elemanın tamamının sayısal olup olmadığını kontrol eder
            sayisalListe.append(eleman)
    
    return sayisalListe

liste=["1","2","3","5a","10b","abc"]
try:
    sayisalListe=sayisalDegerBul(liste)
    print("Sayisal Degerler:",sayisalListe)
except Exception as ex:
    print(ex)

print('------------------------------------------------------')

print("\n1. ornegin baska bir cozumu:")

for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

print('------------------------------------------------------')
#2-Kullanici 'q' degerini girmedikce aldiginiz her inputun sayi oldugundan emin olunuz aksi halde hata mesaji yazin.

while True:
    mesaj=(input("Mesaj giriniz:"))
    if(mesaj=="q"):
       print("Sistemden cikis yapiliyor...")
       break

    try:
        result=float(mesaj)
        print("Gecerli sayi:",result)
    except ValueError:
        print("Gecersiz sayi")
        continue

    
print('------------------------------------------------------')
#3-Girilen parola icinde turkce karakter hatasi veriniz.


def controlSifre(psw):
    import re

    if re.search(r"[ç,ğ,İ,ş,ü,ö,ı]",psw):
        raise Exception("Sifre turkce karakter icermemelidir.")
    

while True:
    sifre=input("Sifrenizi giriniz:")

    try:
        controlSifre(sifre)
        print("Girilen sifre:",sifre)
    except Exception as ex:
        print(ex)
    else:
        print("Sifre gecerli")
        break

print('------------------------------------------------------')
#4-factoriel fonksiyonu olusturup fonksiyona gelen deger icin hata mesajlari verin.

def factorial(x):
    x=int(x)

    if(x<0):
        raise ValueError('Negatif deger.')
    
    result=1 # ilklendirme yapiliyor
    
    for i in range(1,x+1):
        result *=i
    return result

while True:
    sayi = input("Sayi giriniz (cikmak icin 'a' yaziniz): ")
    if(sayi.lower()=="a"):
        print("Sistemden cikis yapiliyor...")
        break
    try:
        sayi=int(sayi)
        y=factorial(sayi)
        print(f"{sayi}! : {y}")
    
    except ValueError as err:
        print(err)
    except Exception as ex:
        print(f"Bir hata olustu:{ex}")
    


