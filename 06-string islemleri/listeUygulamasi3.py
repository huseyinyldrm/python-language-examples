names=['Ali','Hakan','Deniz','Karam','Dido']
years=[1999,2019,2001,2022,2000]

"""
1-"Cenk" ismini listenin sonuna ekleyin.
2-"Sena" ismini listenin basina ekleyin.
3-"Deniz" ismini listeden silin.
4-"Karam" isminin indeksi nedir.
5-"Ali" listenin bir elemani midir?
6-Liste elemanlarini tersten yaz.
7-Liste elemanlarini alfabetik olarak siralayiniz
8-years listesindeki sayilari buyukluge gore siralayin
9-str="Chevrolet,Dacia" karakter dizisini listeye cevirin ve names'e ekleyin.
10-years dizisinin en buyuk ve en kucuk elemani nedir?
11-years dizisinde kac tane 1999 vardir?
12-years dizisindeki tum elemanlari siliniz.
13-Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz.

"""
#1.soru cevabi:
names.append('Cenk')
print(names)

#2.soru cevabi:

names.insert(0,'Sena')
print(names)

#3.soru cevabi:

names.remove('Deniz')
print(names)

#4.soru cevabi:
print(names)
index=names.index('Karam')
print("Karam'in index degeri:",index)

#5.soru cevabi:
result1='Ali' in names
result2=names.index('Ali')
print(result1)
print(result2)

#6.soru cevabi:
names.reverse()
print(names)

#7.soru cevabi:
names.sort()
print(names)

#8.soru cevabi:
years.sort()
print(years)

#9.soru cevabi:
str="Chevrolet,Dacia"
res=str.split(',')
print(res)

ekleme=names+res
print(ekleme)

#10.soru cevabi:
print(min(years))
print(max(years))

#11.soru cevabi:

print(years.count(1999))

#12.soru cevabi:
years.clear()
print(years)

#13.soru cevabi:

markalar=[]

for i in range(3):
    marka=input("Marka: ")
    markalar.append(marka)

print(markalar)

