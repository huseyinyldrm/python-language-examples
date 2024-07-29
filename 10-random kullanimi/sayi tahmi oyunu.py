import random
sayi=random.randint(1,6)#1-6 arası 6 dahil rastgele sayı seçer.
tahmin=int(input("Tahmin Et ..:"))
skor=5

while True:
    
    if sayi==tahmin:
        print("Kazandiniz....Skorunuz=",skor)
        break
    else:
        print("olmadi...Skorunuz=",skor)
        skor-=1
        tahmin=int(input("Tahmin Et ..:"))
