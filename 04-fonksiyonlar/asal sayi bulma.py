def asalMi(sayi):

    if sayi>1:
       
       for i in range(2,sayi):
            if (sayi%i)==0:
               return 0
    
       return 1


sayi=int(input("Bir sayi giriniz:"))

if asalMi(sayi):
    print(sayi, "sayisi asaldir.")

else:
    print(sayi,"sayisi asal degildir.")