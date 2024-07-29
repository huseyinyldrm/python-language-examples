print("Ehliyet Sartlari Sorgulama Programi")

yas=18
fiyat=5000
durum="saglikli"
surucuYas=int(input("Lutfen yasinizi giriniz:"))
surucuParasi=int(input("Lutfen ucretinizi giriniz:"))
surucuDurum=(input("Saglik durumunuzu giriniz:"))

if surucuYas<yas and surucuParasi<fiyat and durum!=surucuDurum:
    print("Ehliyet alamazsiniz.")
else:
    print("Ehliyet alabilirsiniz.")