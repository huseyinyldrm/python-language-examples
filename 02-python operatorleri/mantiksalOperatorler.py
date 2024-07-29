#1-Girilen bir sayinin 0-100 arasinda oldugunu kontrol et.

sayi=float(input("Sayi:"))
result=(sayi>0) and (sayi<=100)
print(f"sayi 0-100 arasinda mi: {result}")

print('*'*50)
#2-Girilen bir sayinin pozitif cift olma kontrolu yap.

number=float(input("Sayi :"))
sonuc=(number>0) and (number%2==0)
print(f"{number} sayisi pozitif ve cift mi: {sonuc}")

print('*'*50)
#3-Girilen 3 sayiyi buyukluk olarak karsilastirin.

sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
sayi3=int(input("3.sayi:"))

result1=(sayi1>sayi2) and (sayi1>sayi3)
print(f"1.sayi en buyuk sayidir: {result1}")

result1=(sayi2>sayi1) and (sayi2>sayi3)
print(f"2.sayi en buyuk sayidir: {result1}")

result1=(sayi3>sayi1) and (sayi3>sayi2)
print(f"3.sayi en buyuk sayidir: {result1}")


print('*'*50)
#4-Kullanicidan 2 vize(%60) ve final(%40) notunu alıp ortalam hesaplayin.
#Eger ortalama 50 ve ustu ise gecti degilse kaldi.
# a) Ortalama 50 olsa bile final en az 50 olmalidir.
# b) Finalden 70 alindiginda ortalamanin onemi olmasin.

vize1=float(input("1.vize notu:"))
vize2=float(input("2.vize notu:"))
final=float(input("Final  notu:"))

ortalama=(((vize1+vize2)/2)*0.6 + final*0.4)

sartlar1=(ortalama>=50) and (final>=50)
print(f"Ogrencinin ortalamasi:{ortalama} ve gecme durumu:{sartlar1}")

sartlar2=(ortalama>=50) or (final>=70)
print(f"Ogrencinin ortalamasi:{ortalama} ve gecme durumu:{sartlar2}")

print('*'*50)
#5-vki hesaplayiniz. 
# 0-18,4=>Zayif
# 18.5-24.9=>Normal
# 25.0-29.9=> Fazla Kilolu
# 30.0-34.9=>Sisman(obez)

name=input("Adiniz:")
kg=float(input("Kilonuz:"))
hg=float(input("Boyunuz:"))

index=(kg)/(hg**2)

zayif=(index>=0) and (index<=18.4)
normal=(index>=18.5) and (index<=24.9)
kilolu=(index>=25.0) and (index<=29.9)
obez=(index>=30.0) and (index<=34.9)

print(f"{name} kilo indeksin:{index} ve kilo degerlendirmen zayif:{zayif}")
print(f"{name} kilo indeksin:{index} ve kilo degerlendirmen normal:{normal}")
print(f"{name} kilo indeksin:{index} ve kilo degerlendirmen kilolu:{kilolu}")
print(f"{name} kilo indeksin:{index} ve kilo degerlendirmen obez:{obez}")

print('*'*50)
#6-Email ve parola bilgileri ile giris kontrolu yapınız.

email="email@sadikturan.com"
password="abc123"

girilenEmail=input("Email:")
girilenPassword=input("password:")

sart=(email==girilenEmail) and (password==girilenPassword)
print(f"Uygulamaya giris basarili mi:{sart}")
