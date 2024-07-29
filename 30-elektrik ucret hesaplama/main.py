print("*"*50)

print("Elektrik Faturasi Hesaplama Sistemine Hosgeldiniz")

print("*"*50)

while True:

    print("1-Tek Zamanli Fatura\n2-Uc Zamanli Fatura\n3-Cikis")
    print("*"*50)
    secim=(input("Elektrik Tarifesini Giriniz:"))
    print("*"*50)

    if(secim=="1"):
        gunBoyuKullanim=float(input("Gun Boyunca Harcanan Elektrik Miktarini Kwh Cinsinden Giriniz:"))

        print("*"*50)

        toplamTutar=gunBoyuKullanim*0.51

        print(f"Faturanizin Vergiler Haric Tuketim Ucreti:{toplamTutar} TL'dir.")

        kdv=toplamTutar*0.18
        etv=toplamTutar*0.02
        trtPayi=toplamTutar*0.01
        eFonu=toplamTutar*0.11

        print("*"*50)

        print(f"Faturanin KDV Ucreti :{kdv} TL'dir.")
        print(f"Faturanin ETV Ucreti :{etv} TL'dir.")
        print(f"Faturanin TRT Payi Ucreti :{trtPayi} TL'dir.")
        print(f"Faturanin E-Fonu Ucreti :{eFonu} TL'dir.")

        print("*"*50)

        netTutar=toplamTutar+trtPayi+kdv+etv+eFonu

        print(f"Faturanin Vergiler Ile Birlikte Toplam Tuketim Ucreti:{netTutar} TL'dir.")

        print("*"*50)

    elif(secim=="2"):
        gunduzTuketim=float(input("Sabah Diliminde Harcanan Elektrik Miktarini Kwh Cinsinden Giriniz:"))


        ogleTuketim=float(input("Sabah Diliminde Harcanan Elektrik Miktarini Kwh Cinsinden Giriniz:"))


        geceTuketim=float(input("Sabah Diliminde Harcanan Elektrik Miktarini Kwh Cinsinden Giriniz:"))

        gunduzTutar=gunduzTuketim*0.53
        ogleTutar=ogleTuketim*0.78
        geceTutar=geceTuketim*0.33

        toplamVergisiz=gunduzTutar+ogleTutar+geceTutar

        print(f"Faturanin Vergiler Haric Tuketim Ucreti:{toplamVergisiz} TL'dir.")

        kdv=toplamVergisiz*0.18
        etv=toplamVergisiz*0.02
        trtPayi=toplamVergisiz*0.01
        eFonu=toplamVergisiz*0.11

        print("*"*50)

        print(f"Faturanin KDV Ucreti :{kdv} TL'dir.")
        print(f"Faturanin ETV Ucreti :{etv} TL'dir.")
        print(f"Faturanin TRT Payi Ucreti :{trtPayi} TL'dir.")
        print(f"Faturanin E-Fonu Ucreti :{eFonu} TL'dir.")

        print("*"*50)

        netTutar=toplamVergisiz+trtPayi+kdv+etv+eFonu

        print(f"Faturanin Vergiler Ile Birlikte Toplam Tuketim Ucreti:{netTutar} TL'dir.")

        print("*"*50)

    elif(secim=="3"):
        print("Sistemden Cikis Yapiliyor.")
        break

    else:
        print("Gecersiz Deger Girdiniz.")