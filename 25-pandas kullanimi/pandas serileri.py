import pandas as pd
import numpy as np

#data turleri
print("---------------------------------")
numbers=[10,20,30,40]

pSerisi=pd.Series(numbers)
print(pSerisi)

print("---------------------------------")

letters=['a','b','c','d']
pSerisi2=pd.Series(letters)
print(pSerisi2)

print("---------------------------------")

scalar=5
pSerisi3=pd.Series(scalar,[0,1,2,3,4])
print(pSerisi3)

print("---------------------------------")

sayilar=[2,4,6,8,10]
pSerisi4=pd.Series(sayilar,['a','b','c','d','e'])
print(pSerisi4)

print("---------------------------------")

dict={'a':10,'b':20,'c':30,'d':40}
sonuc=pd.Series(dict)
print(sonuc)

print("---------------------------------")

sayilar=np.random.randint(10,100,6)

result=pd.Series(sayilar)
print(result)

print("---------------------------------")

pandasSerisi=pd.Series([20,30,40,51],['a','b','c','d'])

print("Olusan pandas serisi:")
print(pandasSerisi)

print("*********************************")

sonuc1=pandasSerisi.iloc[0] # gelecekteki kullanim icin iloc oneriliyor.
print("Pandas serisinin 0. indisindeki veri:",sonuc1)

print("*********************************")

sonuc2=pandasSerisi.iloc[-1]
print("pandas serisinin sonuncuindisindeki veri:",sonuc2)

print("*********************************")

sonuc3=pandasSerisi.iloc[:2]
print("Pandas serisindeki ilk 2 eleman verisi:")
print(sonuc3)

print("*********************************")

sonuc4=pandasSerisi[-2:]
print("Pandas serisindeki son 2 eleman verisi:")
print(sonuc4)

print("*********************************")

sonuc5a=pandasSerisi['a']
print("a 'ya karsilik gelen deger:",sonuc5a)
sonuc5b=pandasSerisi['b']
print("b 'ya karsilik gelen deger:",sonuc5b)
sonuc5c=pandasSerisi['c']
print("c 'ya karsilik gelen deger:",sonuc5c)
sonuc5d=pandasSerisi['d']
print("d 'ya karsilik gelen deger:",sonuc5d)

print("*********************************")

sonuc6=pandasSerisi[['a','c']]
print("a ve c'ye karsilik gelen degerler:")
print(sonuc6)


print("---------------------------------")

toplam=pandasSerisi.sum()
print("pandas serisindeki verilerin toplami:",toplam)

print("---------------------------------")

ndim=pandasSerisi.ndim
print("dizi kac boyutlu:",ndim)

print("---------------------------------")

dtype=pandasSerisi.dtype
print("pandas dizisinin data tipi:",dtype)

print("---------------------------------")

shape=pandasSerisi.shape
print("pandas serisindeki eleman sayisi:",shape)

print("---------------------------------")

maxDeger=pandasSerisi.max()
print("Pandas serisindeki en buyuk degeri:",maxDeger)

minDeger=pandasSerisi.min()
print("Pandas serisindeki en kucuk deger:",minDeger)

ekleme=pandasSerisi+50
print("Pandas serisine ekleme islemi:")
print(ekleme)

karekok=np.sqrt(pandasSerisi)
print("Pandas serisindeki verilerin karekoku:")
print(karekok)

sart=pandasSerisi[pandasSerisi>=50]
print("Pandas serisinde 50'den buyuk degerler:")
print(sart)

ciftler=pandasSerisi[pandasSerisi % 2==0]
print("Pandas serisindeki cift degerler:")
print(ciftler)

print("---------------------------------")

opel2018=pd.Series([20,30,40,10],["Astra","Corsa","Mokka","Insignia"])
opel2019=pd.Series([40,30,20,10],["Astra","Corsa","Grandland","Insignia"])

total=opel2018 + opel2019
print(total)

print("*********************************")

# iki veriyi birlestirir ve karsilikli olmayan verileri nan dondurur.
print("iki verideki Astra fiyat bilgisi:",total["Astra"])

print("*********************************")