#Bir ogrencinin 2 yazili 1 sozlu notunu alip hesaplanan ortalamaya gore not araligina karsilik gelen not bilgilerini yazdiriniz.
#0-24 => 0
#25-44 => 1
#45-54=>2
#55-69=>3
#70-89=>4
#85-100=>5

yazili1=float(input("1. yazili notu:"))
yazili2=float(input("2. yazili notu:"))
sozlu=float(input("Sozlu notu:"))

ortalama=(yazili1+yazili2+sozlu)/3

if(ortalama>=0) and (ortalama<=24):
    print(f"Oralamaniz:{ortalama} Notunuz:0")
elif(ortalama>=25) and (ortalama<45):
    print(f"Ortalamaniz:{ortalama} Notunuz:1")
elif(ortalama>=45) and (ortalama<55):
    print(f"Ortalamaniz:{ortalama} Notunuz:2")
elif(ortalama>=55) and (ortalama<=69):
    print(f"Ortalamaniz:{ortalama} Notunuz:3")
elif(ortalama>=70) and(ortalama<=84):
    print(f"Ortalamaniz:{ortalama} Notunuz:4")
elif(ortalama>=85) and (ortalama<=100):
    print(f"Ortalamaniz:{ortalama} Notunuz:5")
else:
    print("Yanlis bilgi girdiniz.")