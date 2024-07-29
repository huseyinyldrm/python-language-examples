
maxSayi=int(input("Ust sinir giriniz:"))
toplam=0

for i in range(1,maxSayi+1):# ust sayiyi de dahil etmek icin 1 fazlasi eklendi.
    toplam+=i
    print(i,end=' ')# yan yana yazdirip arasina bosluk birakir.

print("\nBu sayilarin toplami:",toplam)
