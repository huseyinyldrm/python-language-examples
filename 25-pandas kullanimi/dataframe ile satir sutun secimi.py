import pandas as pd
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)

print("********************************************************")
print("Sutuna gore secme islemleri")

result=df["Column1"]
print("Sadece column1'i oldugu verler:")
print(result)

print("********************************************************")

result2=df[["Column1","Column2"]] # 2 koseli parantez var unutma.
print("Column1 ve Column2'nin oldugu veriler:")
print(result2)

print("********************************************************")
print("Satira gore secme islemleri")

sonuc=df.loc["A"]
print("Sadece A sutununda bulunan veriler:")
print(sonuc)

print("********************************************************")

#loc["row","column"] => loc["row"] => loc[:,"column"]

sonuc1=df.loc[:,"Column1"]
print("Sadece column1'in oldugu veriler:")
print(sonuc1)

print("********************************************************")

sonuc2=df.loc["A","Column2"]
print("Column2 ve A satirinda bulunan deger:")
print(sonuc2)

print("********************************************************")

sonuc3=df.loc[:,["Column1","Column2"]] # burada belirtilen baslangic ve bitis degerlerinin hepsi dahildir.
print("Column1 ve Column2 degerleri:")
print(sonuc3)

print("********************************************************")
sonuc4=df.loc[:,:"Column2"]
print("Bastan basla Column2'ye kadar git:")
print(sonuc4)

print("********************************************************")

sonuc5=df.loc["A":"C",:"Column3"]
print("A ile C arasindaki verileri bastan Column3'e kadar git: ")
print(sonuc5)

print("********************************************************")

sonuc6=df.iloc[2]
print("indexler ile calisma ornegi anahtar kelime iloc: ")
print(sonuc6)

print("********************************************************")

sonuc7=df.loc[["A","B"],["Column1","Column2"]]
print("A ve B satirlari ile Column1 ile Column2 sutunlarindaki degerler:")
print(sonuc7)

print("********************************************************")
print("Colon ekleme islemleri:")

df["Column4"]=pd.Series(randn(3),["A","B","C"])
print(df)

print("********************************************************")

df["Column5"]=df["Column1"]+df["Column4"]
print(df)

print("********************************************************")
print("Colon silme islemleri:")
print(df)
print("Silinmis seri:")
sonuc8=df.drop("Column5",axis=1,inplace=False)
print(sonuc8) # orijinal dataframe uzerinde degisiklik yapmak icin 'inplace=True' kopyasini almak icin ve orijinal dataframede degisiklik yapmamak icin 'inplace=False' islemlerini ekleriz.
print("\n")
print("Uzerinde degisiklik yapilmayan dataframe:")
print(df)