x,y,z=2,5,10

numbers=1,5,7,10,6

#1-Kullanicidan aldiginiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir?
sayi1=int(input("1.sayi: "))
sayi2=int(input("2.sayi: "))
result1=sayi1*sayi2
print(result1)

result2=x+y+z
print(result2)

sonuc=result1-result2
print("Sonuc:",sonuc)


#2-y'nin x'e kalansiz bolumunu hesaplayiniz.
cozum2=y/x
print("2.soru cevabi: ",cozum2)

#3-(x,y,z) toplaminin mod 3'u nedir?

cozum3=(x+y+z)%3
print("3.soru cevabi: ",cozum3)

#4-y'nin x. kuvvetini hesaplayiniz.
cozum4=y**x

print("4.soru cevabi: ",cozum4)

#5-x,*y,z = numbers islemine gore z'nin kupu kactir?
#numbers=1,5,7,10,6
x,*y,z=numbers
print("5.soru cevabi: ",z**3)
#6-x,*y,z = numbers islemine gore y'nin degerleri toplami kactir? 
#numbers=1,5,7,10,6
x,*y,z=numbers

toplam=y[0]+y[1]+y[2]
print("6.soru cevabi: ",toplam)