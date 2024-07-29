def notHesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')
    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=((not1+not2+not3)/3)

    if(ortalama>=90 and ortalama<=100):
        harf='AA'
    elif(ortalama>=85 and ortalama<=89):
        harf='BA'
    elif(ortalama>=80 and ortalama<=84):
        harf='BB'
    elif(ortalama>=75 and ortalama<=79):
        harf='CB'
    elif(ortalama>=70 and ortalama<=74):
        harf='CC'
    elif(ortalama>=65 and ortalama<=69):
        harf='DC'
    elif(ortalama>=60 and ortalama<=64):
        harf='DD'
    elif(ortalama>=50 and ortalama<=59):
        harf='FD'
    else:
        harf='FF'
    
    return ogrenciAdi +": "+ str(ortalama) +' => '+ harf + "\n"


def ortalamalariOku():
    with open("sinavNotlari.txt","r",encoding='utf-8') as file:
        for satir in file:
            print(notHesapla(satir))

def notGir():
    ad=input("Ogrenci Adi:")
    soyad=input("Ogrenci Soyadi:")
    not1=(input("1.Not:"))
    not2=(input("2.Not:"))
    not3=(input("3.Not:"))


    with open("sinavNotlari.txt","a",encoding='utf-8') as file:
        file.write(ad+' '+soyad +':'+not1+','+not2+','+not3+'\n')



def notlariKaydet():
    with open("sinavNotlari.txt","r",encoding='utf-8') as file:
        liste=[]

        for i in file:
            liste.append(notHesapla(i))
        with open("sonuclar.txt","w",encoding='utf-8') as file2:
            for i in liste:
                 file2.write(i)
    
    print("Notlar basarili bir sekilde kaydedildi...")

while True:
    print("*"*50)
    print("1-Notlari Oku\n2-Not Gir\n3-Notlari Kaydet\n4-Cikis\n")
    print("*"*50)
    islem=input("Bir islem seciniz: ")

    print("-"*20)

    if (islem=="1"):
        ortalamalariOku()
    elif(islem=="2"):
        notGir()
    elif (islem=="3"):
        notlariKaydet()
    elif(islem=="4"):
        print("Sistemden cikis yapiliyor...")
        break
    else:
        print("Gecersiz deger girdiniz...")
