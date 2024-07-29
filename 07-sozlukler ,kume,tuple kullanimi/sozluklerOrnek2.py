ogrenciler={}
for i in range(3):
    number=input("Ogrenci No: ")
    name=input("Ogrenci Adi: ")
    surName=input("Ogrenci Soyadi: ")
    phone=input("Ogrenci Telefon: ")
    sinif=input("Ogrenci Sinifi: ")
    print('------------------------')

    ogrenciler[number]={
        'ad':name,
        'soyad':surName,
        'telefon':phone,
        'sinif':sinif
    }

    #2. kullanim:

    ogrenciler.update({#birden fazla veri ayni anda eklenebilir.
        number:{
            'ad':name,
            'soyad':surName,
            'telefon':phone,
            'sinif':sinif

        }
    })

print(ogrenciler)

ogrNo=input("Ogrenci No: ")
ogrenci=ogrenciler[ogrNo]

print(f"Aranilan {ogrNo} nolu ogrencinin adi:{ogrenci['ad']},soyadi:{ogrenci['soyad']} , telefon numarasi:{ogrenci['telefon']} ve sinifi:{ogrenci['sinif']} ")

