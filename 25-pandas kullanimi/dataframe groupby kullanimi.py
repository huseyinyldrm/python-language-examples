import pandas as pd
import numpy as np

personeller={
    "Calisan":["Ahmet Yilmaz","Can Erturk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Erturk","Mustafa Can"],
    "Departman":["Insan Kaynaklari","Bilgi Islem","Muhasebe","Insan Kaynaklari","Bilgi Islem","Muhasebe","Bilgi Islem"],
    "Yas":[30,25,45,50,23,34,42],
    "Semt":["Kadikoy","Tuzla","Maltepe","Tuzla","Kadikoy","Tuzla","Maltepe"],
    "Maas":[5000,3000,4000,3500,2750,6500,4500]
    }

df=pd.DataFrame(personeller)
print(df)

print("***************************************************************")

sonuc=df["Maas"].sum()
print("Personel Toplam Maasi:",sonuc)

print("***************************************************************")

sonuc1a=df.groupby(["Departman","Semt"]).groups # syntax'a dikkat.
print(sonuc1a)

print("***************************************************************")

sonuc1b=df.groupby("Departman").groups
print(sonuc1b)

print("***************************************************************")

semtler=df.groupby("Semt")

for name,group in semtler:
    print(name)
    print(group)

print("***************************************************************")

departmanlar=df.groupby("Departman")

for name,group in departmanlar:
    print(name)
    print(group)

print("***************************************************************")

sonuc2=df.groupby("Semt").get_group("Kadikoy")
print(sonuc2)

print("***************************************************************")

sonuc3=df.groupby("Departman").get_group("Muhasebe")
print(sonuc3)

print("***************************************************************")

sonuc4=df.groupby("Departman").sum()
print("Departmana gore toplam maas ve yas:")
print(sonuc4)

print("***************************************************************")

sonuc5=df.groupby("Departman")["Maas"].mean()
print("Departmana gore maas ortalamasi:")
print(sonuc5)

print("***************************************************************")

sonuc6=df.groupby("Departman")["Yas"].mean()
print("Departmana gore yas ortalamasi:")
print(sonuc6)

print("***************************************************************")

sonuc7=df.groupby("Departman")["Maas"].max()
print("Departmana gore en yuksek maas alanlar:")
print(sonuc7)

print("***************************************************************")

sonuc8=df.groupby("Semt")["Calisan"].count()
print("Semtlere gore hangi departmanda kac kisi calisiyor:")
print(sonuc8)

print("***************************************************************")

sonuc9=df.groupby("Departman")["Maas"].min()
print("Departmana gore en az maas alanlar:")
print(sonuc9)

print("***************************************************************")

result=df.groupby("Departman")["Maas"].min()["Muhasebe"]
print("Sadece Muhasebe departmaninda en dusuk maas alan:",result)

print("***************************************************************")

result1=df.groupby("Departman").agg({"Yas":"mean","Maas":"mean"}) # bu yeni kullanimdir.
print("Yas ve Maaslarin departmanlaraa gore ortalamasi:")
print(result1)

print("***************************************************************")

result2=df.groupby("Departman")["Maas"].agg(["sum","mean","max","min"])
print("Tum departmanlar icin islemler:")
print(result2)

print("***************************************************************")

result3=df.groupby("Departman")["Maas"].agg(["sum","mean","max","min"]).loc["Muhasebe"] # parantezlere dikkat!!!
print(result3)

