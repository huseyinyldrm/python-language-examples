def hesapla(a,b,islem):
    if islem not in "+-/*":
        return "Lütfen şu işlemlerden birini seçiniz:+/*-"
    if islem=="+":
        return (str(a) +" + "+ str(b)+" = "+ str(a+b))
    
    if islem=="-":
        return (str(a) +" - "+ str(b)+" = "+ str(a-b))
    
    if islem=="*":
        return (str(a) +" * "+ str(b)+" = "+ str(a*b))
    
    if islem=="/":
        return (str(a) +" / "+ str(b)+" = "+ str(a/b))


while True:
    try:
        a=int(input("İlk sayiyi giriniz:"))
        b=int(input("İkinci sayiyi giriniz:"))
        islem=input("İşleminizi seçiniz:+-*/")
        sonuc=hesapla(a,b,islem)
        print(sonuc)
    except:
        print("Lütfen sayilari düzgün giriniz.")