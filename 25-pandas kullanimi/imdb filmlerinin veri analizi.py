import pandas as pd
import numpy as np

df=pd.read_csv("imdb.csv")
print("********************************************************")
#1- Dosya hakkindaki bilgiler.
print("Dosya bilgisi:")
print(df)

print("Kolon Bigileri:")
res=df.columns
print(res)

print("********************************************************")
#2- ilk 5 kaydi gosterin.
sonuc=df.head()
print("ilk 5 kayit:")
print(sonuc)

print("********************************************************")
#3- ilk 10 kaydi gosterin.

sonuc1=df.head(10)
print("ilk 10 kayit:")
print(sonuc1)

print("********************************************************")
#4- son 5 kaydi gosterin.

sonuc2=df.tail()
print("Son 5 kayit:")
print(sonuc2)

print("********************************************************")
#5- son 10 kaydi gosterin.

sonuc3=df.tail(10)
print("Son 10 kayit:")
print(sonuc3)

print("********************************************************")
#6- Sadece Movie_Title kolonunu alin.

sonuc4=df["Movie_Title"]
print(sonuc4)

print("********************************************************")
#7- Sadece Movie_Title kolonunu iceren ilk 5 kaydi alin.

sonuc5=df["Movie_Title"].head()
print("Sadece Movie_Title kolonu:")
print(sonuc5)

print("********************************************************")
#8- Sadece Movie_Title ve Rating kolonunu iceren ilk 5 kaydi alin.

sonuc6=df[["Movie_Title","Rating"]].head()
print("Movie_Title ve Rating kolonlari:")
print(sonuc6)

print("********************************************************")
#9- Sadece Movie_Title ve Rating kolonunu iceren son 7 kaydi alin.

sonuc7=df[["Movie_Title","Rating"]].tail(7)
print("Sadece Movie_Title ve Rating kolonlarinin son 7 verisi:")
print(sonuc7)

print("********************************************************")
#10-Sadece Movie_Title ve Rating kolonunu iceren ikinci 5 kaydi alin.

sonuc8=df[5:20][["Movie_Title","Rating"]].head(5)
print("Sadece Movie_Title ve Rating kolonunu iceren ikinci 5 kaydi:")
print(sonuc8)

print("********************************************************")
#11-Sadece Movie_Title ve Rating kolonunu iceren ve imdb puani 8.0 ve uzerinde olan kayitlardan ilk 50 tanesini aliniz.

sonuc9=df[df["Rating"]>=8.0][["Movie_Title","Rating"]].head(50)

print("Sadece Movie_Title ve Rating kolonunu iceren ve imdb puani 8.0 ve uzerinde olan kayitlardan ilk 50 film:")
print(sonuc9)


print("********************************************************")
#12-Yayin tarihi 2014 ile 2015 arasinda olan filmlerin isimlerini getiriniz.

sonuc10=df[(df["YR_Released"]>2018) & (df["YR_Released"]<2024)][["Movie_Title"]]
print("2014-2015 arasi filmler:")
print(sonuc10)

print("********************************************************")
#13-Degerlendirme sayisi(Num_Reviews) 100.000'den buyuk ya da imdb puani 8 ile 9 arasinda olan filmleri listeleyiniz.

sonuc11=df[(df["Num_Reviews"]>100000) | ((df["Rating"]>=8) & (df["Rating"]<=9))][["Movie_Title","Num_Reviews","Rating"]]
print("Num_Reviews sayisi 100.000'den buyuk ya da imdb puani 8 ile 9 arasinda olan filmler:")
print(sonuc11)

# parantezlere dikkat et.


