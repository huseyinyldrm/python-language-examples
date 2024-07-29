import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])
print(df)

print("********************************************************")

sonuc=df.columns
print("Sutunlarin adedi ve isimleri:")
print(sonuc)

print("********************************************************")

sonuc1=df.head()
print("ilk 5 tane satir verileri:")
print(sonuc1)

print("********************************************************")

sonuc2=df.head(10)
print("Ilk 10 tane satir verileri:")
print(sonuc2)

print("********************************************************")

sonuc3=df.tail()
print("Son 5 tane kayit verileri:")
print(sonuc3)

print("********************************************************")

sonuc4=df.tail(10)
print("Sondan 10 tane kayit verileri:")
print(sonuc4)

print("********************************************************")

sonuc5=df["Column1"].head() # tavsiye edilen!!!!
print("Column1 'in ilk 5 kaydini vermek:")
print(sonuc5)

print("\nBu islemin alternatifi:\n")

sonuc5a=df.Column1.head()
print(sonuc5a)

print("********************************************************")

sonuc6=df[["Column1","Column2"]].head()
print("Column1 ve Column2 'nin ilk 5 kaydi:")
print(sonuc6)

print("********************************************************")

sonuc7=df[5:15][["Column1","Column2"]].head()
print("5 ile 15 arasindaki kayitlarin ilk 5 verisi:")
print(sonuc7)

print("********************************************************")

sonuc8=df[5:15][["Column1","Column2"]].tail()
print("5 ile 15 arasindaki kayitlarin son 5 verisi:")
print(sonuc8)

print("********************************************************")

sonuc9=df[df>50]
print("Tum veriler icinden 50'den buyuk olan sayilar:")
print(sonuc9)

print("********************************************************")

sonuc10=df[df%2==0]
print("Tum veriler icindeki cift sayilar:")
print(sonuc10)

print("********************************************************")

res=df[df["Column1"]>50][["Column1","Column2"]]
print("sadece column1 ve column2 verilerinden 50'den buyuk olan degerler:")
print(res)

print("********************************************************")

res1=df[(df["Column1"] >50) & (df["Column1"]<=70)][["Column1"]]
print("Column1'in 50 den buyuk ve 70'ten kucuk olan verileri:")
print(res1)

print("********************************************************")

res2=df[(df["Column1"]>50) | (df["Column2"]<70) | (df["Column3"]>80)][["Column1","Column2","Column3"]]
print(res2)

print("********************************************************")

res3=df.query("Column1>=50 & Column1 % 2==0")[["Column1"]]
print("Column1'de 50den buyuk ve cift olan sayilar:")
print(res3)

print("********************************************************")

res3=df.query("Column2>=50 & Column2 % 2==0")[["Column2"]]
print("Column2'de 50den buyuk ve cift olan sayilar:")
print(res3)

print("********************************************************")

res3=df.query("Column3>=50 & Column3 % 2==0")[["Column3"]]
print("Column3'de 50den buyuk ve cift olan sayilar:")
print(res3)

print("********************************************************")

res3=df.query("Column4>=50 & Column4 % 2==0")[["Column4"]]
print("Column4'de 50den buyuk ve cift olan sayilar:")
print(res3)

print("********************************************************")

res3=df.query("Column5>=50 & Column5 % 2==0")[["Column5"]]
print("Column5'de 50den buyuk ve cift olan sayilar:")
print(res3)

print("********************************************************")