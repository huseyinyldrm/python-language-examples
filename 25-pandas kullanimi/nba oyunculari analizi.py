import pandas as pd

data=pd.read_csv("nba.csv")
print(data)
print("**************************************************")
#1- ilk 10 kaydi getiriniz.

print("ilk 10 kayit:")
print(data.head(10))

print("**************************************************")
#2- toplam kac kayit vardir?

sonuc=len(data.index)
print("Toplam kayit:",sonuc)


print("**************************************************")
#3- tum oyuncularin toplam maas ortalamasi nedir?

sonuc1=data["Salary"].mean()
print("Tum oyuncularin maas ortalamasi:",sonuc1)

print("**************************************************")
#4- en yuksek maas ne kadardir?

sonuc2=data["Salary"].max()
print("En yuksek maas:",sonuc2)

print("**************************************************")
#5- en yuksek maasi alan oyuncu kimdir?

sonuc3=data[data["Salary"]==data["Salary"].max()]["Name"].iloc[0]
print("En yuksek maasi alan oyuncu:\n",sonuc3)

print("**************************************************")
#6- yasi 20-25 arasinda olan oyuncularin ismi ve oynadiklari takimlari azalan sekilde siralayiniz.

result= data[(data["Age"]>=20) & (data["Age"]<25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
print(result)

print("**************************************************")
#7- "John Holland" isimli oyuncunun oynadigi takim hangisidir?

sonuc4=data[data["Name"]=="John Holland"][["Team","Name"]]
print(sonuc4)


print("**************************************************")
#8- takimlara gore oyuncularin ortalama maaslari?
sonuc5=data.groupby("Team")["Salary"].mean() # dogrru kullanim bu  sekildedir.
print(sonuc5)


print("**************************************************")
#9- kac farkli takim mevcut?

sonuc6=len(data.groupby("Team"))
print("toplam takim sayisi:",sonuc6)

print("\nTakimlarin listesi:\n")
sonuc7=data["Team"].unique()
print(sonuc7)

sonuc8=data["Team"].nunique()
print("\nToplam takim sayisi:",sonuc8)


print("**************************************************")
#10-her takimda kac oyuncu oynamaktadir?

sonuc9=data["Team"].value_counts()
print(sonuc9)

print("**************************************************")
#11-ismmi icinde "and" gecen kayitlari bulunuz.

print("birinci yontem:".center(50,"-"))
data=data.dropna()  # NaN olan degerleri listeden cikardik.
sonuc10=data[data["Name"].str.contains("and")]
print(sonuc10)


print("ikinci yontem:".center(50,"-"))

def strFind(name):
    if "and" in  name.lower(): # butun harfleri kucuk yaptik.
        return True
    return False

result1=data[data["Name"].apply(strFind)]
print(result1)

print("**************************************************")

