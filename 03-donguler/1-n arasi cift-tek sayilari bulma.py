
n=int(input("Ust sinir giriniz:"))
toplam=0

for i in range(1,n):

    if i%2==0:
        toplam+=i
        print(i,end=" ")

print("\nBu sayilarin toplami:",toplam)