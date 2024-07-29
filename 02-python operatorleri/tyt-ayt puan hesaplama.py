print("Universite Puan Hesaplama Programi\n")

okulPuani=100
def secim():
    print("1-Sadece TYT Puan Hesaplama")
    print("2-Ayt Sayisal Puan Hesaplama")
    print("3-Ayt Esit Agirlik Puan Hesaplama")
    print("4-Ayt Sozel Puan Hesaplama")
    print("5-Ayt Dil Puan Hesaplama")
    print("6-Cikis")


print("Lutfen alaninizi giriniz:")
secim()
secim=int(input("Secim Yapiniz:"))

if secim==1:
    diploma=(float)(input("Diploma notunuzu giriniz:"))

    turkceDogru=int(input("Turkce dogru sayisi:"))
    turkceYanlis=int(input("Turkce yanlis sayisi:"))

    sosyalDogru=int(input("Sosyal Bilgiler dogru sayisi:"))
    sosyalYanlis=int(input("Sosyal Bilgiler yanlis sayisi:"))
    
    matDogru=int(input("Matematik dogru sayisi:"))
    matYanlis=int(input("Matematik yanlis sayisi:"))
    
    fenDogru=int(input("Fen Bilimleri dogru sayisi:"))
    fenYanlis=int(input("Fen Bilimleri yanlis sayisi:"))

    turkceNet=(float)(turkceDogru-(turkceYanlis/4))
    sosyalNet=(float)(sosyalDogru-(sosyalYanlis/4))
    matNet=(float)(matDogru-(matYanlis/4))
    fenNet=(float)(fenDogru-(fenYanlis/4))

    print("Turkce Net:",turkceNet)
    print("Matematik Net:",matNet)
    print("Sosyal Bilgiler Net:",sosyalNet)
    print("Fen Bilimleri Net:",fenNet)

    toplamDogru=(int)(turkceDogru+sosyalDogru+fenDogru+matDogru)
    toplamYanlis=(int)(turkceYanlis+matYanlis+sosyalYanlis+fenYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))
    
    print("Toplam Net: ",net)

    toplamPuan=100 + net*3.35 + diploma*0.6
    print("TYT Puani: ",toplamPuan)

elif secim==2:
    diploma=(float)(input("Diploma notunuzu giriniz:"))

    turkceDogru=int(input("Turkce dogru sayisi:"))
    turkceYanlis=int(input("Turkce yanlis sayisi:"))

    sosyalDogru=int(input("Sosyal Bilgiler dogru sayisi:"))
    sosyalYanlis=int(input("Sosyal Bilgiler yanlis sayisi:"))
    
    matDogru=int(input("Matematik dogru sayisi:"))
    matYanlis=int(input("Matematik yanlis sayisi:"))
    
    fenDogru=int(input("Fen Bilimleri dogru sayisi:"))
    fenYanlis=int(input("Fen Bilimleri yanlis sayisi:"))

    turkceNet=(float)(turkceDogru-(turkceYanlis/4))
    sosyalNet=(float)(sosyalDogru-(sosyalYanlis/4))
    matNet=(float)(matDogru-(matYanlis/4))
    fenNet=(float)(fenDogru-(fenYanlis/4))

    print("Turkce Net:",turkceNet)
    print("Matematik Net:",matNet)
    print("Sosyal Bilgiler Net:",sosyalNet)
    print("Fen Bilimleri Net:",fenNet)

    toplamDogru=(int)(turkceDogru+sosyalDogru+fenDogru+matDogru)
    toplamYanlis=(int)(turkceYanlis+matYanlis+sosyalYanlis+fenYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))
    
    print("Toplam Net: ",net)

    toplamPuan=100 + net*3.35 + diploma*0.6
    print("TYT Puani: ",toplamPuan)

    mat2Dogru=int(input("Matematik dogru sayisi:"))
    mat2Yanlis=int(input("Matematik yanlis sayisi:"))

    fizikDogru=int(input("Fizik dogru sayisi:"))
    fizikYanlis=int(input("Fizik yanlis sayisi:"))

    kimyaDogru=int(input("Kimya dogru sayisi:"))
    kimyaYanlis=int(input("Kimya yanlis sayisi:"))

    biyoDogru=int(input("Biyoloji dogru sayisi:"))
    biyoYanlis=int(input("Biyoloji yanlis sayisi:"))

    toplamDogru=(int)(mat2Dogru+fizikDogru+kimyaDogru+biyoDogru)
    toplamYanlis=(int)(mat2Yanlis+fizikYanlis+kimyaYanlis+biyoYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))

    print("Toplam Net: ",net)

    aytPuan=(100+net*4.2+diploma*0.6)*0.6
    sayisalPuan=aytPuan+toplamPuan*0.4

    print("Ayt Sayisal Puan:",sayisalPuan)

elif secim==3:
    diploma=(float)(input("Diploma notunuzu giriniz:"))

    turkceDogru=int(input("Turkce dogru sayisi:"))
    turkceYanlis=int(input("Turkce yanlis sayisi:"))

    sosyalDogru=int(input("Sosyal Bilgiler dogru sayisi:"))
    sosyalYanlis=int(input("Sosyal Bilgiler yanlis sayisi:"))
    
    matDogru=int(input("Matematik dogru sayisi:"))
    matYanlis=int(input("Matematik yanlis sayisi:"))
    
    fenDogru=int(input("Fen Bilimleri dogru sayisi:"))
    fenYanlis=int(input("Fen Bilimleri yanlis sayisi:"))

    turkceNet=(float)(turkceDogru-(turkceYanlis/4))
    sosyalNet=(float)(sosyalDogru-(sosyalYanlis/4))
    matNet=(float)(matDogru-(matYanlis/4))
    fenNet=(float)(fenDogru-(fenYanlis/4))

    print("Turkce Net:",turkceNet)
    print("Matematik Net:",matNet)
    print("Sosyal Bilgiler Net:",sosyalNet)
    print("Fen Bilimleri Net:",fenNet)

    toplamDogru=(int)(turkceDogru+sosyalDogru+fenDogru+matDogru)
    toplamYanlis=(int)(turkceYanlis+matYanlis+sosyalYanlis+fenYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))
    
    print("Toplam Net: ",net)

    toplamPuan=100 + net*3.35 + diploma*0.6
    print("TYT Puani: ",toplamPuan)

    mat2Dogru=int(input("Matematik dogru sayisi:"))
    mat2Yanlis=int(input("Matematik yanlis sayisi:"))

    edebiyatDogru=int(input("Edebiyat dogru sayisi:"))
    edebiyatYanlis=int(input("Edebiyat yanlis sayisi:"))

    tarihDogru=int(input("Tarih dogru sayisi:"))
    tarihYanlis=int(input("Tarih yanlis sayisi:"))

    cogDogru=int(input("Cografya dogru sayisi:"))
    cogYanlis=int(input("Cografya yanlis sayisi:"))

    toplamDogru=(int)(mat2Dogru+edebiyatDogru+tarihDogru+cogDogru)
    toplamYanlis=(int)(mat2Yanlis+edebiyatYanlis+tarihYanlis+cogYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))

    print("Toplam Net: ",net)

    aytPuan=(100+net*4.2+diploma*0.6)*0.6
    esitAgirlikPuan=aytPuan+toplamPuan*0.4

    print("Ayt Esit Agirlik Puani:",esitAgirlikPuan)


elif secim==4:
    diploma=(float)(input("Diploma notunuzu giriniz:"))

    turkceDogru=int(input("Turkce dogru sayisi:"))
    turkceYanlis=int(input("Turkce yanlis sayisi:"))

    sosyalDogru=int(input("Sosyal Bilgiler dogru sayisi:"))
    sosyalYanlis=int(input("Sosyal Bilgiler yanlis sayisi:"))
    
    matDogru=int(input("Matematik dogru sayisi:"))
    matYanlis=int(input("Matematik yanlis sayisi:"))
    
    fenDogru=int(input("Fen Bilimleri dogru sayisi:"))
    fenYanlis=int(input("Fen Bilimleri yanlis sayisi:"))

    turkceNet=(float)(turkceDogru-(turkceYanlis/4))
    sosyalNet=(float)(sosyalDogru-(sosyalYanlis/4))
    matNet=(float)(matDogru-(matYanlis/4))
    fenNet=(float)(fenDogru-(fenYanlis/4))

    print("Turkce Net:",turkceNet)
    print("Matematik Net:",matNet)
    print("Sosyal Bilgiler Net:",sosyalNet)
    print("Fen Bilimleri Net:",fenNet)

    toplamDogru=(int)(turkceDogru+sosyalDogru+fenDogru+matDogru)
    toplamYanlis=(int)(turkceYanlis+matYanlis+sosyalYanlis+fenYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))
    
    print("Toplam Net: ",net)

    toplamPuan=100 + net*3.35 + diploma*0.6
    print("TYT Puani: ",toplamPuan)

    edebiyatDogru=int(input("Edebiyat dogru sayisi:"))
    edebiyatYanlis=int(input("Edebiyat yanlis sayisi:"))

    tarihDogru=int(input("Tarih dogru sayisi:"))
    tarihYanlis=int(input("Tarih yanlis sayisi:"))

    cogDogru=int(input("Cografya dogru sayisi:"))
    cogYanlis=int(input("Cografya yanlis sayisi:"))

    felsefeDogru=int(input("Felsefe dogru sayisi:"))
    felsefeYanlis=int(input("Felsefe yanlis sayisi:"))

    tarih2Dogru=int(input("Tarih-2 dogru sayisi:"))
    tarih2Yanlis=int(input("Tarih-2 yanlis sayisi:"))

    cog2Dogru=int(input("Cografya-2 dogru sayisi:"))
    cog2Yanlis=int(input("Cografya-2 yanlis sayisi:"))

    dinDogru=int(input("Din Bilgisi dogru sayisi:"))
    dinYanlis=int(input("Din Bilgisi yanlis sayisi:"))



    toplamDogru=(int)(felsefeDogru+tarih2Dogru+cog2Dogru+dinDogru+edebiyatDogru+tarihDogru+cogDogru)
    toplamYanlis=(int)(felsefeYanlis+tarih2Yanlis+cog2Yanlis+dinYanlis+edebiyatYanlis+tarihYanlis+cogYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))

    print("Toplam Net: ",net)

    aytPuan=(100+net*4.2+diploma*0.6)*0.6
    sozelPuan=aytPuan+toplamPuan*0.4

    print("Ayt Sozel Puani:",sozelPuan)


elif secim==5:
    diploma=(float)(input("Diploma notunuzu giriniz:"))

    turkceDogru=int(input("Turkce dogru sayisi:"))
    turkceYanlis=int(input("Turkce yanlis sayisi:"))

    sosyalDogru=int(input("Sosyal Bilgiler dogru sayisi:"))
    sosyalYanlis=int(input("Sosyal Bilgiler yanlis sayisi:"))
    
    matDogru=int(input("Matematik dogru sayisi:"))
    matYanlis=int(input("Matematik yanlis sayisi:"))
    
    fenDogru=int(input("Fen Bilimleri dogru sayisi:"))
    fenYanlis=int(input("Fen Bilimleri yanlis sayisi:"))

    turkceNet=(float)(turkceDogru-(turkceYanlis/4))
    sosyalNet=(float)(sosyalDogru-(sosyalYanlis/4))
    matNet=(float)(matDogru-(matYanlis/4))
    fenNet=(float)(fenDogru-(fenYanlis/4))

    print("Turkce Net:",turkceNet)
    print("Matematik Net:",matNet)
    print("Sosyal Bilgiler Net:",sosyalNet)
    print("Fen Bilimleri Net:",fenNet)

    toplamDogru=(int)(turkceDogru+sosyalDogru+fenDogru+matDogru)
    toplamYanlis=(int)(turkceYanlis+matYanlis+sosyalYanlis+fenYanlis)
    net=(float)(toplamDogru-(toplamYanlis/4))
    
    print("Toplam Net: ",net)

    toplamPuan=100 + net*3.35 + diploma*0.6
    print("TYT Puani: ",toplamPuan)

    dilDogru=int(input("Yabanci Dil dogru sayisi:"))
    dilYanlis=int(input("Yabanci Dil yanlis sayisi:"))

    net=(float)(dilDogru-(dilYanlis/4))

    print("Toplam Net: ",net)

    aytPuan=(100+net*4.2+diploma*0.6)*0.6
    dilPuan=aytPuan+toplamPuan*0.4

    print("Yabanci Dil Puani:",dilPuan)


elif secim==6:
    print("Sistemden cikiliyor.")

else:
    print("Gecerli bir islem seciniz.")




