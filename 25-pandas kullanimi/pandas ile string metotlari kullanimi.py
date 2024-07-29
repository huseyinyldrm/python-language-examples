import pandas as pd

print("***********************************************")
print("Orijinal veri bilgileri:")
data=pd.read_csv("nba.csv")
print(data)

print("***********************************************")

print("NaN degerlere sahip satirlari veya sutunlari kalici olarak kaldirmak icin kullanilir.")

data.dropna(inplace=True)
print(data)

print("***********************************************")
print("Tum isimlerin buyuk harfe dondurulmus sekli:")

data["Name"]=data["Name"].str.upper()
print(data.head(10))

print("***********************************************")
print("Tum isimlerin kucuk harfe dondurulmus sekli:")

data["Name"]=data["Name"].str.lower()
print(data.head(10))

print("***********************************************")
print("Tum veriler uzerinde string arama islemi:")

data["index"]=data["Name"].str.find('a')
print(data.head(10))

print("***********************************************")

data=data[data["Name"].str.contains('Johnson',case=False)]
print("johnson isminin gectigi veriler:")
print(data.head(10))

print("***********************************************")

data["Team"] = data["Team"].str.replace(' ', '-')
print("replace ile bosluk yerine farkli bir karakter getirme:")
print(data.head(10))
print("***********************************************")

data[["FirstName", "LastName"]] = data["Name"].loc[data["Name"].str.split
().str.len() == 2].str.split(expand=True)
print("Firstname ne Lastname ayirma islemi:")
print(data.head(10))