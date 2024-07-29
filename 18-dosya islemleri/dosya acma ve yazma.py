"""
Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
Kullanimi: open(dosyaAdi,dosyaErismeModu)
dosyaErismemodu => dosyayi hangi amacla actigimizi belirtir.

"w": (write) yazma modu. Dosyayi konumda olusturur.
dosyada varolanlari siler .
"a": (append) ekleme. Dosya konumda yoksa olusturur.
"x": (create) olusturma. Dosya zaten varsa hata verir.
"r": (read) okuma.varsayilan.Dosya konumda yoksa hata verir.

"""
# file=open("newfile.txt","w") # ayni klasorde dosya acar.
# file=open("C:/users/huseyinyildirim/desktop/newfile.txt","w") # masaustunde dosya acar.
# file=open("newfile.txt","w",encoding='utf-8') # turkce karakter tanimlar.
#file.write("Huseyin") # acik olan dosyaya ekler.Onceden varolani siler.
#file.close() # acik olan dosyayi islemler bittikten sonra kapatir.

#"a" modunda acilirsa dosya icinde olanlara ekleme yapar.
#file=open("newfile.txt","a",encoding='utf-8')
#file.write("Sadik\n") #dosya icindekilere ekleme yapar. 
#file.close()

#"x": sadece isimiz bir dosya olusturmak ise bu mod kullanilir.
#file=open("newfile2.txt","x",encoding='utf-8')

