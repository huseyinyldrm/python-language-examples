
def toplamileCarpma(sayi1,sayi2):
    sonuc=0
    for i in range(0,sayi1):
        sonuc=sonuc+sayi2
    return sonuc

sayi1=int(input("1.sayiyi giriniz:"))
sayi2=int(input("2. sayiyi giriniz:"))
carpimSonucu=toplamileCarpma(sayi1,sayi2)
print("Sonuç:",carpimSonucu)