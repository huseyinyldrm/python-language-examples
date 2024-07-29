import os
import datetime

print("OS modulu icerisindeki bilgiler:".center(50,"*"))
print("\n")
res=dir(os)
print(res)

print("----------------")
print("Kullanilan isletim sistemi ile ilgili bilgi verir:",os.name)

print("----------------")
print("Dosyanin hangi kasorde bulundug bilgisi:",os.getcwd())

print("----------------")
print("Dizin degistirme".center(25,"*"))
#os.chdir('C:\\')
#os.mkdir('../..')

print("Klasor olusturma".center(25,"*"))
 # bunlari 1 kez calistirmak yeterlidir yoksa hata verir.

#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasor")
#os.rename("newdirectory","yeni klasor")
#os.removedirs("yeni klasor/yeniklasor") # var olan dosyalari alt klasorleri ile birlikte siler ama klasorlerin ici bos olmalidir.

print("Etkin dizin ogrenme".center(25,"*"))

result=os.getcwd()
print(result)

print("Listeleme".center(25,"*"))
os.listdir()

for dosya in os.listdir():
    if dosya.endswith('.txt'): # sadece txt uzantili dosyalari verir.
        print(dosya)

print("\n")

print("Dosya olusturma zamanini verir".center(50,"*"))
print("\n")
result1=os.stat("newfile.txt") # istenilen dosyanin olusturulma zamanini verir.
print(result1)

print("----------------")
result2=datetime.datetime.fromtimestamp(result1.st_ctime)
print("Dosyanin olusturulma zamani:",result2)

print("----------------")
result3=datetime.datetime.fromtimestamp(result1.st_atime)
print("Dosyanin son erisme tarihi:",result3)

print("----------------")
result4=datetime.datetime.fromtimestamp(result1.st_mtime)
print("Dosyanin son degisiklik tarihi:",result4)

print("----------------\n")
print("istenilen bir programi calistirmk icin:".center(50,"*"))
print("\n os.system('uygulama adi') kodu calisririlir.")
#os.system("notepad.exe")

print("\n")
print("path modulu".center(25,"*"))
sonuc=os.path.abspath("newfile.txt")
print("istenilen dosyanin komutu:",sonuc)

sonuc2=os.path.dirname("C:/Users/MONSTER/python-language-examples/newfile.txt")
print("Tam konumu verilen dosyanin dizin ismini bulma:",sonuc2)

sonuc3=os.path.dirname(os.path.abspath("newfile.txt"))
print("Dizin ismi icin:",sonuc3)

sonuc4=os.path.exists("newfile.txt")
print("istenilen dosya o konumda var mi:",sonuc4)

sonuc5=os.path.isdir("C:/Users/MONSTER/python-language-examples/newfile.txt")
print("Gİrilen isim klasor mu:",sonuc5)

sonuc6=os.path.isfile("C:/Users/MONSTER/python-language-examples/newfile.txt")
print("Girilen isim dosya mi:",sonuc6)

sonuc7=os.path.join("C:\\","deneme","deneme1")
print("Farkli bir yol olusturma:",sonuc7)

sonuc8=os.path.split("C:\\deneme")
print("Verilen klasor ismini parcalara ayirma:",sonuc8)

sonuc9=os.path.splitext("newfile.txt")
print("Verilen dosya ismini parcalara ayirma:",sonuc9)
sonuc9a=sonuc9[0]
sonuc9b=sonuc9[1]
print("parcalara ayrilan dosya isminin 1. indexteki verisi:",sonuc9a)
print("parcalara ayrilan dosya isminin 2. indexteki verisi:",sonuc9b)