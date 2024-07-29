import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print("---------------------------")
print(numbers1)
print("---------------------------")
print(numbers2)
print("---------------------------")

result=numbers1+numbers2
print("iki dizinin ayini indexteki degerlerinin toplami:",result)

print("---------------------------")

result1=numbers1+10
print("numbers1 dizisinin her elemanina 10 eklenmis hali:",result1)

print("---------------------------")

result2=numbers1-numbers2
print("iki dizi elemanlari arasindaki fark:",result2)

print("---------------------------")


result3=numbers2-10
print("numbers2 dizisinin elemanlarindan 10 cikarilmis hali:",result3)

print("---------------------------")

result4=numbers1/numbers2
print("iki dizinin elemanlarinin birbirine bolunmus hali:",result4)

print("---------------------------")
result5=np.sin(numbers1)
print("numbers1'in sin degerleri :",result5)

print("---------------------------")
result6=np.cos(numbers2)
print("numbers2'nin cos degerleri:",result6)

print("---------------------------")
result7=np.sqrt(numbers1)
print("numbers1'in karekok degerleri: ",result7)

print("---------------------------")
result8=np.log(numbers1)
print("numbers1'in logaritma degerleri: ",result8)

print("---------------------------")
mnumbers1=numbers1.reshape(2,3)
print("numbers1'in 2x3 boyutundaki degerleri:\n",mnumbers1)

print("---------------------------")
mnumbers2=numbers2.reshape(2,3)
print("numbers2'nin 2x3 boyutundaki degerleri:\n",mnumbers2)

print("---------------------------")
result9=np.vstack((mnumbers1,mnumbers2)) # iki tane parantez olmalidir.
print("mnumbers1 ve mnumbers2 matrislerini dikey olarak bilestirir:\n",result9)

print("---------------------------")
result10=np.hstack((mnumbers1,mnumbers2))
print("mnumbers1 ve mnumbers2 matrislerini yatay olarak birlestirir:\n",result10)

print("---------------------------")

sonuc=numbers1>5
print("numbers1'deki 5'ten buyuk olan degerler:",sonuc)

print("---------------------------")
sonuc1=numbers1 %2==0
print("numbers1 degerlerinden hangileri 2'nin tam katlaridir:\n",sonuc1)

print("---------------------------")
