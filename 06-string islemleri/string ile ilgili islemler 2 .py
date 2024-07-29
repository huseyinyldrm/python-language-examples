str=input("İsim giriniz:")

if 'ali' in str:
    print("Ali hoşgeldin.")

else:
    print("Ali nerede.")

print("*************************")

'''
string içerisine eleman ekleme:
stringAdi[ilk indis: son indis: adim miktari]
bu birinci yontemdir.
ikinci yontem: .format() fonksiyonu kullanilir.

'''
metin="ali {} veli"
a=' ile '
print(metin.format(a))
