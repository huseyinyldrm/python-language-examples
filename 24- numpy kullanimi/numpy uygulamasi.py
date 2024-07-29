import numpy as np

print("\n-------------------1.ornek--------------------------\n")
#1-(10,15,20,30,45) degerlerine sahip numpy dizisi olusturun.

sonuc=np.array([10,15,20,35,40])
print("Olusan dizi:",sonuc)


print("\n-------------------2.ornek--------------------------\n")
#2-(5-15) arasindaki sayilarla numpy dizisini olusturunuz.


sonuc1=np.arange(5,15)
print("Olusan dizi:",sonuc1)

print("\n-------------------3.ornek--------------------------\n")
#3-(50-100) arasinda 5'er 5'er artarak numpy dizisi olusturunuz.


sonuc2=np.arange(50,100,5)
print("Olusan dizi:",sonuc2)


print("\n-------------------4.ornek--------------------------\n")
#4-10 elemanli 0'lardan olusan bir dizi olusturunuz.

sonuc3=np.zeros(10)
print("Olusan dizi:",sonuc3)

print("\n-------------------5.ornek--------------------------\n")
#5-10 elemanli 1'lerden olusan bir dizi olusturunuz.


sonuc4=np.ones(10)
print("Olusan dizi:",sonuc4)


print("\n-------------------6.ornek--------------------------\n")
#6-(0-100) arasi esit aralikta 5 sayi uretin.


sonuc5=np.linspace(0,100,5)
print("Olusan dizi:",sonuc5)

print("\n-------------------7.ornek--------------------------\n")
#7-(10-30) arasinda rastgele 5 tane tamsayi uretin.


sonuc6=np.random.randint(10,30,5)
print("Olusan dizi:",sonuc6)

print("\n-------------------8.ornek--------------------------\n")
#8-(-1,1) arasinda 10 adet sayi uretin.

sonuc7=np.random.randn(10)
print("Olusan dizi:",sonuc7)

print("\n-------------------9.ornek--------------------------\n")
#9-(3x5) boyutlarinda (10-50) arasinda rastgele bir matris olusturun.

sonuc8=np.random.randint(10,50,15).reshape(3,5)
print("Olusan 3x5'lik matris:\n",sonuc8)

print("\n-------------------10.ornek-------------------------\n")
#10-uretilen matrisin satir ve sutun sayilarinin toplamini hesaplayiniz.
matris=np.random.randint(10,50,15).reshape(3,5)
print(matris)
print("---------------------")
rowTotal=matris.sum(axis=1)
print("satirlarin toplami:",rowTotal)
print("---------------------")
colTotal=matris.sum(axis=0)
print("sutunlarin toplami:",colTotal)


print("\n-------------------11.ornek-------------------------\n")
#11-uretilen matrisin en buyuk , en kucuk ve ortalamasini bulunuz.
dizi=np.random.randint(10,50,15).reshape(3,5)
print("Olusan dizi:\n",dizi)


print("-----------------------")
enBuyuk=np.max(dizi)
print("En buyk deger:",enBuyuk)

print("-----------------------")

enKucuk=np.min(dizi)
print("En kucuk deger:",enKucuk)

print("-----------------------")

averaj=np.mean(dizi)
print("Dizinin ortalamasi:",averaj)

print("\n-------------------12.ornek-------------------------\n")
#12-uretilen matrisin en buyuk degerinin matrisi nedir.
sonuc9=np.random.randint(10,50,15).reshape(3,5)
print("Olusan dizi:\n",sonuc9)

print("-----------------------")
sonuc9a=sonuc9.argmax()
print("En buyuk degerin indexi:",sonuc9a)

print("-----------------------")

sonuc9b=sonuc9.argmin()
print("En kucuk degerin indexi:",sonuc9b)

print("\n-------------------13.ornek-------------------------\n")
#13-(10-20) arasindaki sayilari iceren dizinin ilk 3 elemanini seciniz.
result=np.arange(10,20)
print("Olusan dizi:",result)

print("-------------------")

elemanlar=result[0:3]
print("ilk 3 eleman:",elemanlar)
print("\n-------------------14.ornek-------------------------\n")
#14-uretilen dizinin elemanlarini tersten yaziniz.

result1=np.arange(10,20)
print("Olusturulan dizi:",result1)

print("-------------------")
ters=result1[::-1]
print("dizinin tersten yazilmis hali:",ters)

print("\n-------------------15.ornek-------------------------\n")
#15-uretilen matrisin ilk satirini seciniz.

dizi1=np.random.randint(10,50,15).reshape(3,5)
print(dizi1)

result2=dizi1[0]

print("-----------------------------")

print("dizi1'in ilk satiri:",result2)


print("\n-------------------16.ornek-------------------------\n")
#16-uretilen matrisin 2.satir ve 3.sutundaki elemani hangisidir.

dizi2=np.random.randint(10,50,15).reshape(3,5)
print(dizi2)

print("-----------------------------")

result3=dizi2[1,2]
print("2. satir 3. sutundaki eleman:",result3)


print("\n-------------------17.ornek-------------------------\n")
#17-uretilen matrisin tum satirlarindaki ilk elemani seciniz.

dizi3=np.random.randint(10,50,15).reshape(3,5)
print(dizi3)

print("-----------------------------")

result4=dizi3[:,0]
print("tum satirlardaki ilk eleman:",result4)


print("\n-------------------18.ornek-------------------------\n")
#18-uretilen matrisin herhangi bir elemanin karesin aliniz.

dizi4=np.random.randint(10,50,15).reshape(3,5)
print(dizi4)

print("-----------------------------")

result5=dizi4**2
print("tum matrisin karesinin alinmis hali:\n",result5)


print("\n-------------------19.ornek-------------------------\n")
#19-uretilen matrix elemanlarinin hangisi pozitif cift sayidir.
# araligi (-50,50) arasinda yapiniz.

dizi5=np.arange(-50,50)
print(dizi5)

print("-----------------------------")
ciftler=dizi5[dizi5 % 2==0]
print("uretilen matrix icindeki cift sayilar:\n",ciftler)

print("-----------------------------")

pozitifler=ciftler[ciftler>0]
print("0'dan buyuk cift sayilar:\n",pozitifler)