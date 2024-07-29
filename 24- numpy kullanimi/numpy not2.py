import numpy as np

result7=np.random.randint(0,10)
print(result7) # en altta oldugunda hata veriyor.

print("*************************************")
result=np.array=([1,3,5,7,9])
print(result)

print("*************************************")

result2=np.arange(0,10) # 0 - 10 arasi dizi olusturur.
print(result2)

print("*************************************")

result3=np.arange(10,100,3)
print(result3)

print("*************************************")

result4=np.zeros(10) # sadece 0 dan olusan dizi olusturur.
print(result4)

print("*************************************")

result5=np.ones(10) # sadece 1 den olusan dizi olusturur.
print(result5)

print("*************************************")

result6=np.linspace(0,100,5) # verilen baslangic ve bitis noktalarini esit olarak boler.
print(result6)

print("*************************************")

result8=np.random.randint(1,10,3) # 1-10 arasi 3 rastgele sayi uretir.
print(result8)

print("*************************************")
result9=np.random.rand(5) # 0-1 arasi 5 tane rastgele sayi uretir.
print(result9)

print("*************************************")

result10=np.random.randn(3) # -1,+1 arasi 3 tane rastgele sayi uretir.  
print(result10)

print("*************************************")

npArray=np.arange(50)
npMulti=npArray.reshape(5,10) # 5 - 10 luk bir dizi olusturur.
print(npMulti)
print("-------------------")
print(npMulti.sum(axis=1)) # satirlarin toplamini verir.
print("-------------------")
print(npMulti.sum(axis=0)) # sutunlarin toplamini verir.

print("*************************************")

rndNumbers=np.random.randint(1,100,10)
print(rndNumbers)

sonuc=rndNumbers.max() # uretilen sayilar icindeki en buyuk degeri bulur.
print("\nEn buyuk sayi:",sonuc)

sonucA=rndNumbers.min()
print("En kucuk sayi:",sonucA)

sonucB=rndNumbers.mean()
print("Verilen sayilarin ortalamasi:",sonucB)

sonucC=rndNumbers.argmax()
print("En buyuk deger hangi indexte:",sonucC)

sonucD=rndNumbers.argmin()
print("En kucuk deger hangi indexte:",sonucD)

print("*************************************")
