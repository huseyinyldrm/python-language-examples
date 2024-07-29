sayilar=[1,3,5,7,9,12,19,21]
#1-sayilar listesini while ile ekrana yazdirin.
sira=0
while (sira<len(sayilar)):
    print(sayilar[sira])
    sira+=1
print('--------------------------------')
#2-baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari ekrana yazdirin.

baslangic=int(input("Baslangic:"))
bitis=int(input("Bitis:"))

i=baslangic
while i<bitis:
    i+=1
    if(i%2==1):
        print(i)

print('--------------------------------')
#3- 1-100 arasindaki sayilari azalan sekilde yazdirin.
sayi=100
while sayi>=0:
    print(sayi)
    sayi-=1

print('--------------------------------')
#4-kullanicidan alacaginiz 5 sayiyi sirali bir sekilde yazdirin.
numbers=[]
i=0
while i<5:
    number=int(input("Sayi giriniz:"))
    numbers.append(number)
    i+=1
print("Sayilarin sirali bir sekilde yazdirilmis hali:")
print(numbers)

print('--------------------------------')
#5-kullanicidan aldiginiz sinirsiz urun bilgisini urunler listesi icinde saklayin.
# ** urun sayisini kullaniciya sorun.
# ** dictionary listesi yapisi (name,price) seklinde olsun.
# ** urun ekleme islemi bittiginde urunleri ekrana while ile yazdirin.    

urunler=[]
adet=int(input("Kac urun girmek istiyorsunuz:"))
i=0
while (i<adet):
    name=input("Urun ismi:")
    price=input("Urun fiyati:")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f"Urun adi: {urun['name']}, Urun fiyati:{urun['price']}")

print('--------------------------------')