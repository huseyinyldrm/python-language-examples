'''
 mukemmel sayi = kendisi haric pozitif bolenlerinin sayisinin toplami kendisine esit olan sayiya denir.//
 ornek= 6= 1+2+3=6,  28=1+2+3+4+7+14=28//   
'''

def mukemmelMi(sayi):
    toplam=0
    n=sayi

    for i in range(1,n):
        if n%i==0:
            toplam+=i
        
    return sayi==toplam

sayi=int(input("Lutfen bir sayi giriniz:"))

if mukemmelMi(sayi):
    print(f"{sayi} bir mukemmel sayidir.")

else:
    print(f"{sayi} bir mukemmel sayi degildir.")