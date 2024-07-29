sayi=int(input("Carpanlari hesaplanacak sayiyi giriniz:"))

n=0
toplam=0

for i in range(1,sayi+1):
    if sayi%i==0:
        print(i,end=' ')

        n+=1 # carpanlarinin adedini belirler.

        toplam+=i

print("\n",sayi,"Sayisinin",n,"Tane pozitif tam bolenleri vardir.")
print("Bu sayilarin toplami:",toplam)