sayilar=[1,2,3,4,5,6,7,8,9]

#1-sayilar listesindeki hangi sayilar 3'un katidir?
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)

print('--------------------------------')

#2-sayilar listesinde sayilarin toplami kactir?

toplam=0
for sayi in sayilar:
    toplam+=sayi
    
print("Sayilarin toplami: ",toplam)

print('--------------------------------')

#3-sayilar listesindeki tek sayilarin karesini aliniz.

for sayi in sayilar:
     if(sayi%2==1):
         print(sayi**2)

print('--------------------------------')

sehirler=['kocaeli','istanbul','ankara','diyarbekir','van','mus']

#4-sehiirlerin hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)

print('--------------------------------')

urunler=[
    {'name':'samsung s10','price':'3000'},
    {'name':'samsung s12','price':'4000'},
    {'name':'samsung s20','price':'5000'},
    {'name':'samsung s21','price':'6000'},
    {'name':'samsung s22','price':'7000'}
]

#5-urunlerin fiyatlari toplami:

toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat

print("urunlrin toplam fiyati:",toplam)

print('--------------------------------')

#6-urunlerden fiyati en fazla 5000 olan urunleri gosteriniz.

for urun in urunler:
    fiyatlar=int(urun['price'])
    if(fiyatlar<=5000):
        print(urun['name'],urun['price'])