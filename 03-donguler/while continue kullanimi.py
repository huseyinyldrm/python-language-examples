x=1
print("Cikis icin 0'a bas")

while x!=0:
    x=int(input("Sayi giriniz:"))
    print("Sayinin karesi:",x*x)
print("gule gule")


for i in range(25):# 1-25 arasi 6 nin katlarini yazdirmaz.
    if i%6==0:
      continue
    
    print(i)