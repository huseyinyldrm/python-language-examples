for d in 'bilgisayar':
    print(d) # hepsini alt alta yazar.

a=' '
s=0

indis=int(input("İndis degerini giriniz:"))

for d in 'bilgisayar':

    if s==indis:
        a=d
    s+=1

print(a) # istenilen indisteki elemanı yazdırır.
