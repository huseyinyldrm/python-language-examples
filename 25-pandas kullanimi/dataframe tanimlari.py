import pandas as pd
import numpy as np
print("-------------------------------------------------")
dataf=pd.DataFrame()
print(dataf)

print("-------------------------------------------------")

dataF=pd.DataFrame([1,2,3,4])
print(dataF)

print("-------------------------------------------------")
sinav=[["Ahmet",50],["Ali",60],["Yagmur",70],["Betul",80]]
sonuc=pd.DataFrame(sinav,columns=['Name','Grade'],index=[1,2,3,4]) # isim belirtilirse sirasinin bir onemi yoktur.
print(sonuc)

print("-------------------------------------------------")
s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])

data=dict(apples=s1,oranges=s2)

df=pd.DataFrame(data)

# iki pandas serisinin birlesimi 1 data frameye denk gelir.
print(df)

print("-------------------------------------------------")

dict={"Name":["Ahmet","Mehmet","Mert","Cinar"],"Grade":[50,60,70,80]}
df1=pd.DataFrame(dict,index=["222","223","224","225"])
print(df1)


print("-------------------------------------------------")

dictList=[
    {"Name":"Ali","Grade":50},
    {"Name":"Mehmet","Grade":60},
    {"Name":"Oya","Grade":70},
    {"Name":"Lale","Grade":80}
    ]

df2=pd.DataFrame(dictList,index=["222","221","223","334"])
print(df2)

