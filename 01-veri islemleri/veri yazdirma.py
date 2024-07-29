'''
veri yazdirma su sekilde olur:
1)print() metodu
2)format() metodu, f metodu, + metodu
3)sep() metodu: ciktilarin arasina istenilen ayraci koyar.
'''

print('h','e','l','l','o') # aralarinda birer bosluk ile yazdirir.

print('J','u','p','i','t','e','r',sep='*') # her boslugun arasina * koyar.

print('m','a','r','s',sep='.') # her boslugun arasina . koyar

print("dunya "*3) # dunya kelimesini 3 kez yazdirir.

print("gunes\nsistemi") #\n den sonra satir basi yapar.

print("samanyolu\tgalaksisi")#\t bir tab bosluk birakir.

print("Hoca ogrencilere \"GUNAYDIN\" dedi.")# GUNAYDIN kelimesi tirnak icinde yazilir.

isim="Huseyin"
soyisim="Yildirim"

print(f"Merhaba {isim} {soyisim}") # f metodu ile cikti yazilir.

print("Merhaba {} {}".format(isim,soyisim))# .format() metodu ile cikti yazilir.

print("Merhaba "+str(isim)+' '+str(soyisim)) # + metodu kullanildi.

print("Merhaba",isim,soyisim)  # burada da , kullanildi . bunlarin hepsi ayni ciktiyi verir.