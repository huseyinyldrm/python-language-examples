#dosya olusturma islemi

file=open("newfile.txt","a",encoding='utf-8') #bu kod satiri ne kadar acik kalirsa o kadar ekleme yapar.

file.write("Karam\nDido\nPetito\nBrowni\n") # bu kod satiri ne kadar acik kalirsa o kadar ekleme yapar.

#file.close()

print("-----------------------------------")
try:
     file=open("newfile.txt","r")
     print(file)

except FileNotFoundError:
     print("Dosya okuma hatasi.")


finally:

     print("Dosya kapandi.")
     file.close()

print("-----------------------------------")

#hepsini birden yorum satiri yapmak icin ctrl + a ile hepsini sac sonra ctrl + k + c ile hepsini ayni anda yorun satiri yap.


# for dongusu ile okuma yapma:
print("for dongusu ile okuma yapma".center(50,"*"))

file=open("newfile.txt","r",encoding='utf-8')

for i in file:
    print(i,end=' ')


file=open("newfile.txt","r",encoding='utf-8')

# read() fonksiyonu ile dosya okuma:
print("icerik 1:read() ile okuma yapma".center(50,"*"))
content1=file.read()
print(content1)


file=open("newfile.txt","r",encoding='utf-8') # her defasinda dosyayi tekrar acmak gerekir.
print("icerik 2 :".center(50,"*"))
content2=file.read()
print(content2)

print("-----------------------------------")

# readline() fonksiyonu her defasinda bir satir okur.

print("readline() kullanimi".center(50,"*"))
file=open("newfile.txt","r",encoding='utf-8')

print(file.readline(),end='')
print(file.readline(),end='')
print(file.readline(),end='')
print(file.readline(),end='')

print("-----------------------------------")

# # readlines() fonksiyonu her bir satir bilgiyi dizi olarak konsola yazdirir.
print("readlines() kullanimi".center(50,"*"))

file=open("newfile.txt","r",encoding='utf-8')


liste=file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])

file.close() # en son dosya kapatilmalidir.