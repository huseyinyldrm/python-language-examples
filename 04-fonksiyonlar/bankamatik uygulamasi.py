sadikHesap={
    'ad':'Sadik Turan',
    'hesapNo':'12345678',
    'bakiye':3000,
    'ekHesap':4000
}
ahmetHesap={
    'ad':'Ahmet Turan',
    'hesapNo':'124589',
    'bakiye':9000,
    'ekHesap':4000
}
mehmetHesap={
    'ad':'Mehmet Turan',
    'hesapNo':'13579',
    'bakiye':2000,
    'ekHesap':1000
}
hamdikHesap={
    'ad':'Hamdi Turan',
    'hesapNo':'02468',
    'bakiye':5000,
    'ekHesap':7000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print("Paranizi alabilirsiniz.")
        print(f"Guncel bakiyeniz:{hesap['bakiye']} TL")
        bakiyeSorgu(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']

        if(toplam>=miktar):
            ekHesapKullanimi=input("Ek hesap kullanilsin mi(e/h):")

            if(ekHesapKullanimi=='e'):
                ekHesapKullanilacakMiktar=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                print("Paranizi alabilirsiniz.")
                print(f"Guncel ek hesap bakiyeniz:{hesap['ekHesap']} TL")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else: 
            print("Uzgunuz bakiyeniz yetersiz.")

def bakiyeSorgu(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
    print('*'*50)
    print(f"{hesap['hesapNo']} nolu hesabinizin guncel ek bakiyesinde {hesap['ekHesap']} TL bulunmaktadir. ")



paraCek(sadikHesap,2000)
print('*'*50)
bakiyeSorgu(sadikHesap)
print('*'*50)
paraCek(hamdikHesap,5000)
print('*'*50)
paraCek(hamdikHesap,4000)