import numpy as np

numbers=np.array([0,5,10,15,20,25,50,70])

print("--------------------------------")
result= numbers[5]
print("dizinin 5. indisindeki elemani:",result)

print("--------------------------------")
result1=numbers[-1]
print("dizinin son indisindeki eleman:",result1)

print("--------------------------------")
result2=numbers[0:3]
print("dizinin 0 ile 2. indisindeki elemanlar:",result2)

print("--------------------------------")
result3=numbers[3:]
print("dizinin 3. indisinden itibaren tum elemanlar:",result3)

print("--------------------------------")
result4=numbers[::]
print("dizinin tumu:",result4)

print("--------------------------------")
result5=numbers[::-1] # tersten yazdirir.
print("dizinin tersten yazilmis hali:",result5)

print("***********************************************")

numbers2=np.array([[0,5,10],[15,20,25],[50,75,80]])

print("--------------------------------")
sonuc=numbers2[0]
print("ilk satirdaki elemanlar:",sonuc)

print("--------------------------------")
sonuc1=numbers2[2]
print("2. satirdaki elemanlar:",sonuc1)

print("--------------------------------")
sonuc2=numbers2[0,2]
print("0.satir ile 2. sutundaki eleman:",sonuc2)

print("--------------------------------")
sonuc3=numbers2[2,2]
print("2.indis satir ile 2. indis sutundaki eleman: ",sonuc3)

print("--------------------------------")
sonuc4=numbers2[:,2] # tum satirlarin 2. ineksteki degerlerini verir.
print("tum satirlarda 2. indisteki eleman:",sonuc4)

print("--------------------------------")
sonuc5=numbers2[:,0:2] # sag tarafa yazilan degerler dahil degildir.
print("her satirin ilk 2 elemani:\n",sonuc5)

print("--------------------------------")
sonuc6=numbers2[-1,:]
print("son satirdaki elemanlar:",sonuc6)

print("--------------------------------")
sonuc7=numbers2[:3,:3]
print("matristeki tum elemanlar:\n",sonuc7)

print("--------------------------------")
sonuc8=numbers2[:2,:2]
print("matristeki ilk 2 satir ve sutundaki elemanalr:\n",sonuc8)

print("********************************")

arr1=np.arange(0,10)

arr2=arr1 # referance

print("1. dizi:",arr1)
print("--------------------------------")
print("2. dizi:",arr2)

print("--------------------------------")
arr2[0]=20

print("guncel 1.dizi:",arr1)
print("--------------------------------")
print("guncel 2. dizi:",arr2)

print("--------------------------------")

arr2=arr1.copy() # burada yapilan degisiklikler sadece arr2'de gerceklesir.

arr2[1]=20

print("--------------------------------")
print("kopyalanan guncel 1. dizi:",arr1)

print("--------------------------------")
print("kopyasi alinan guncel 2. dizi:",arr2)
