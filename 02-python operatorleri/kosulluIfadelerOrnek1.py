#Kullanicidan isim,yas ve egitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.Ehliyet alma kosulu en az 18 yas ve egitim durumu lise ya da universite olmalidir.

isim=input("Isminiz:")
yas=int(input("Yasiniz:"))
egitim=input("Egitiminiz:")

if(yas>=18):
    if(egitim=='lise' or egitim=='universite'):
        print(f"{isim} Ehliyet alabilirsiniz.")
    else:
        print(f"{isim} Ehliyet alamazsiniz egitim durumu yetersiz.")

else:
    print(f"{isim} Ehliyet alamazsiniz yasiniz tutmuyor.")