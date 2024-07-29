'''Veri donusturmek icin donusturmek istedigimiz veri tipini degiskenin basina parantez icinde yazariz.'''

toplam=int(20.5) + int(20.5) # 20.5 float ama biz en basta tipini intager yaptik ve toplam= 40 oldu.
print(toplam)

a=5
b=6
islem=(float) (a*b) # cikti 30.0 olur intagerden floata cevirdik.
print(islem)

c=(str)(4)
print(type(c)) # intager verisini stringe cevirdik.

d=int('5')
print(type(d)) # string olan veriyi intagere cevirdik.

e=float(57)
print(e)
print(type(e)) #intager olan veriyi floata cevirdik.

f=(int)(4.6)
print(f)
print(type(f))# virgulden sonraki kisim atilir 4 ciktisi verir. float intagere donustu.