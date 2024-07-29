import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

df=df.reindex(["a","b","c","d","e","f","g","h"])
print(df)

print("***************************************************")

newColumn=[np.nan,30,np.nan,51,np.nan,39,np.nan,10]
df["column4"]=newColumn

print(df)
print("***************************************************")

sonuc1=df.drop("column1",axis=1) # axis=1 sutun. axis=0 satir karsiliktir.
print(sonuc1)

print("***************************************************")

sonuc2=df.drop('a',axis=0)
print(sonuc2)

print("***************************************************")

sonuc3=df.drop(["a","b","h"],axis=0)
print(sonuc3)

print("***************************************************")

sonuc4=df.isnull()
print(sonuc4)

print("***************************************************")

sonuc5=df.notnull()
print(sonuc5)

print("***************************************************")

sonuc6=df.isnull().sum()
print(sonuc6)

print("***************************************************")

sonuc7=df["column1"].isnull().sum()
print(sonuc7)

print("***************************************************")

print("Matrisin son hali:")
print(df)

print("***************************************************")

sonuc8=df[df["column1"].isnull()]["column1"]
print("Sadece column1'deki null degerler:")
print(sonuc8)

print("***************************************************")

sonuc9=df[df["column1"].notnull()]
print("Null olanlarin matristen cikarilmis hali:")
print(sonuc9)

print("***************************************************")

sonuc10=df[df["column1"].notnull()]["column1"]
print(sonuc10)

print("***************************************************")

res=df.dropna() # varsayilan olarak axis=0 => satirlari siler.
print(res)

print("***************************************************")

res1=df.dropna(axis=1) # kolonlari silmek icin axis=1 yapilir.
print(res1)

print("***************************************************")

res2=df.dropna(how="any")
print("hic null olmayan degerleri dondurur: how= anahtar kelime:")
print(res2)

print("***************************************************")

res3=df.dropna(how="all")
print("null olan degerleri dondurur en az 1 tane olsa bile: how= anahtar kelime:")
print(res3)

print("***************************************************")

res4=df.dropna(subset=["column1","column2"],how="all")
print(res4)

print("***************************************************")

res5=df.dropna(subset=["column1","column2"],how="any")
print(res5)

print("***************************************************")

res6=df.dropna(thresh=3) # en az sayida normal veri
print("icinde en az 3 veri olan satirlar gelir anahtar kelime thresh:")
print(res6)

print("***************************************************")

res7=df.fillna(value=1)
print("null olan yerlere istenilen deger eklenir: anahtar kelime fillna:")
print(res7)

print("***************************************************")

res8=df.sum().sum()
print("Tum verilerin toplami:")
print(res8)

print("***************************************************")

res8a=df.sum()
print("colonlardaki verilerin toplami:")
print(res8a)

print("***************************************************")

result=df.size
print("dataframe boyutunu alma islemi:",result)

print("***************************************************")

result1=df.isnull().sum().sum()
print("null yani bos degerlerin sayisini bulma islemi:",result1)

print("***************************************************")

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size-df.isnull().sum().sum()

    return toplam/adet

result2=df.fillna(value=ortalama(df))
print("nul olan yerlere ortalama deger yazildi:")
print(result2)