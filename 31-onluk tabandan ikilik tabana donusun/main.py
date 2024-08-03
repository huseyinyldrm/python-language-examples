from math import pow

#degiskenlerin tanimlanmasi

s=0
i=0
basamak=0

#sayinin girilmesi
sayi=int(input("Sayi giriniz:"))

while(sayi>0):
    #cevirme isleminin yapilmasi
    basamak=int((sayi%2)*pow(10,i))
    i+=1
    sayi=sayi//2
    s=s+basamak

#cevrilen sayinin ekrana yazilmasi

print(s)