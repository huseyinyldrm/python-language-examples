def armstrongMu(sayi):
    str_sayi=str(sayi) # sayiyi stringe cevirir basamaklarina ayirir.

    num_sayi=len(str_sayi) # yayinin basamak sayisini bulur.

    armsrong_sayi= sum(int(digit)**num_sayi for digit in str_sayi)

    return armsrong_sayi==sayi

sayi=int(input("Bir sayi giriniz:"))

if armstrongMu(sayi):
    print(f"{sayi} bir armstrong sayisidir.")

else:
    print(f"{sayi} bir armstrong sayisi degildir.")