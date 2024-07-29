website="https://www.sadikturan.com"
course="Python Kursu: Bastan Sona Python Programlama Rehberi(40 Saat)"

#1-"course" karakter dizisinde kaç karakter bulunmaktadadır?
print('-'*50)
print(len(course))

print('-'*50)
#2-"website" içinden www karakterlerini alın.
print('-'*50)
print(website[8:11])

print('-'*50)
#3-"website" içinden com karakterlerini alın.
print(len(website))
print(website[23:26])

print('-'*50)
#4-"course" içinden ilk 15 ve son 15 karakterlerini alın.

print(course[:16])#ilk 15 karakter
print(course[16:])#son 15 karakter

print('-'*50)
#5-"course" ifadesini tersten yazın.

print(course[::-1])

print('-'*50)

name,surname,age,job='Bora','Yilmaz',32,'muhendis'

#1-Yukarıda verilen degiskeni ekrana yazdır.
print(f"Benim adim {name+" "+surname} . Yasim {age} meslegim {job}")
print("Benim adim {0}{1} . Yasim{2} meslegim {3}".format(name,surname,age,job))

print('-'*50)
#2-'Hello world' ifadesindeki w yerine W yazdır.
s='Hello world'
s=s[0:6]+'W'+s[-4:]
print(s)

print('-'*50)
#3-'abc' ifadesini yan yana 3 defa yazdır.
print('abc '*3)

