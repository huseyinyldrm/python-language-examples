"""
1-10 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleri ile bulmaya calisin.
** 100 uzerinden puanlama yapin ve her soru 20 puan olsun.
** hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.

"""
import random

#rastgele sayi belirleme
rastgeleSayi=random.randint(1,10)

#kullanicidan can bilgisi alma
can=int(input("Kac tane hak istiyorsunuz:"))


#puan ve baslangic
puan=100
saruPuani=20
sayac=0

#oyunu baslatma:

while can>0:
    sayac+=1
    print(f"Kalan hak:{can} , Puan:{puan}")
    tahmin=int(input("1-10 arasinda bir sayi tahmin edin: "))

    if(tahmin==rastgeleSayi):
        print(f"Tebrikler , {sayac}.defada bildiniz. dogru tahmin ettiniz!")
        break
    elif(tahmin<rastgeleSayi):
        print("Daha buyuk bir sayi girin.")
    else:
        print("Daha kucuk bir sayi girin.")

    #can ve puan guncellemesi
    can-=1
    puan-=saruPuani
    

    if(can==0):
        print(f"Hakkiniz bitti.Dogru sayi:{rastgeleSayi} 'idi.")

print(f"Oyun bitti.Toplam Puaniniz:{puan}")


