def factorialMi(sayi):
    faktor=0
    if sayi==1:
        faktor=1
    else:
        faktor=sayi*factorialMi(sayi-1)
    
    return faktor

sayi=int(input("Bir sayi giriniz:"))

print(f"{sayi}!={factorialMi(sayi)}")