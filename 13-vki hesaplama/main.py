kilo=float(input("Kilonuzu giriniz:"))
boy=float(input("Boyunuzu metre cinsinden giriniz:"))

vki=float(kilo/(boy*boy))

if vki<18.5:
    print("Sonuc: ideal kilonun altinda.VKİ=",vki)


elif vki>=18.5 and vki<=24.9:
    print("Sonuç: ideal kiloda.VKİ=",vki) 

elif vki>=25 and vki<=29.9:
    print("Sonuç:İdeal kilonun üstünde.VKİ:",vki)

elif vki>=30 and vki<=39.9:
    print("Sonuç:İdeal kilonun çok üstünde(obez).VKİ:",vki)

else:
    print("Sonuç:İdeal kilonun çok daha fazla üstünde (morbit obez).VKİ:",vki)