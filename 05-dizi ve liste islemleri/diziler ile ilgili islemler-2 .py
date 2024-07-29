# listenin eleman sayısını öğrenme: len() ve .count() fonksiyonları kullanılır.

A=[0,1,2,3,4,4,4,4,4,4,5,6,7,8,9]
print(A.count(4)) # 4'ün liste içinde kaç kere tekrarlandığını bulur ve yazdırır.

print(len(A)) # listenin uzunluğunu yazdırır.

#iki listeyi birleştirme: + operatörü ve .extend() fonksiyonu kullanılır.
print("****************************************")

#1. yol:

L1=[1,3,5,7,9]
L2=[0,2,4,6,8]

L3=L1+L2 # iki listeyi birleştirir.
print(L3)

#2. yol:

L1.extend(L2) # L2'yi L1'in sonuna ekler.
print(L1)

L2.extend(L1) # Güncel olan L1' i L2'nin sonuna ekler.
print(L2)

#listeyi ters çevirme: .reverse() fonksiyonu kullanılır.

print("****************************************")

#1. yol

myList=['a','d','c',1,4,75,87,55]
print(myList[::-1]) # listeyi ters çevirir.

#2. yol:

myList.reverse() # bu fonksiyon da aynı görevi görür.
print(myList)


#Liste içindeki en büyük ve en küçük elemanı bulma:min() ve max() metotları kullanılır.
print("****************************************")

List=[21,22,30,42,55,88,76,89,68,99]
print(min(List))
print(max(List))

print("****************************************")


bosListe=[]
topla=0

for i in range(0,5):
    sayi=int(input("Sayi giriniz:"))
    bosListe.append(sayi)
    topla+=sayi

print("Listenin en buyuk ve en kucuk elemaninin toplami:",max(bosListe)+min(bosListe))
print("Bu listenin aritmetik ortalamasi:",topla/len(bosListe))