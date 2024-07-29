
sayi1=int(input("1. sayiyi giriniz: "))
sayi2=int(input("2. sayiyi giriniz:"))
sayi3=int(input("3. sayiyi giriniz:"))

if sayi1>sayi2:
    if sayi1 > sayi3:
        print("En buyuk sayi: ",sayi1)
    else:
        print("En buyuk sayi: ",sayi3)
    
else:
    if sayi2>sayi3:
        print("En buyuk sayi: ",sayi2)
    else:
        print("En buyuk sayi ",sayi3)