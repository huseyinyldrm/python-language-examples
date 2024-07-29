import pandas as pd
import numpy as np

data={
    "Column1":[1,2,3,4,5],
    "Column2":[10,10,10,40,50],
    "Column3":["abc","def","ghe","dea","xyz"] # butun veriler ayni sayida olmalidir.

}


df=pd.DataFrame(data)

print(df)

print("**************************************")

sonuc=df["Column2"].unique()
print("Column2'de tekrar eden verileri silme:")
print(sonuc)

print("**************************************")
sonuc1=df["Column2"].nunique()
print("Kac farkli deger vardir:")
print(sonuc1)

print("**************************************")
sonuc2=df["Column2"].value_counts()
print("Verilen colonda hangi deger kac kere tekrar etmis:")
print(sonuc2)

print("**************************************")

sonuc3=df["Column1"]*2
print(sonuc3)

print("**************************************")

def kareAl(x):
    return x*x

sonuc4=df["Column1"].apply(kareAl)
print(sonuc4)

print("**************************************")

kareAl2=lambda x : x *x
sonuc5=df["Column1"].apply(kareAl2)
print(sonuc5)

print("**************************************")


df["Column4"]=df["Column3"].apply(len)
print(df)

print("**************************************")

sonuc6=df.columns
print(sonuc6)

print("**************************************")

sonuc7=df.info
print(sonuc7)

print("**************************************")

sonuc8=df.index
print(sonuc8)

print("**************************************")

sonuc9=df.sort_values("Column2")
print("Verilen degeri artan sira ile siralama:")
print(sonuc9)

print("**************************************")

sonuc10=df.sort_values("Column3")
print(sonuc10)

print("**************************************")

print("Verilen degerleri artandan azalana dogru siralama:")
sonuc11=df.sort_values("Column3",ascending=False)
print(sonuc11)

print("**************************************")

data2={
    "Ay":["Mayis","Haziran","Nisan","Mayis","Haziran","Nisan","Mayis","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Dergi","Dergi","Dergi"],
    "Gelir":[20,30,40,50,60,70,10,80,90]
}

df=pd.DataFrame(data2)
print(df)

result=(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))
print(result)