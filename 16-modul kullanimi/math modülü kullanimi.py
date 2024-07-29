"""
modul(kutuphane) cesitleri:
1-kendi hazirladigimiz moduller
2-hazir moduller:
   a-Standart kutuphane modulleri
   b-ucuncu sahis modulleri

pypl.org adresinden hazir kutuphanelere  bakilabilir.
indirmek icin gerekli olan komut:
pip install package-name

"""
#1.yontem:
import math

#value=dir(math)
#value=help(math)
#print(value)

print(math.sqrt(49))# karekok hesaplar.

print(math.floor(5.9))# asagi dogru yuvarlama yapar.

print(math.ceil(5.7))# yukari dogru yuvarlama yapar.

print(math.factorial(5)) # factorial alir.

print(math.pow(2,3))# us alir.

print('--------------------------------------------')
#2. yontem:

from math import* # tum ozellikleri kullaniriz.
print(factorial(5))
print(sqrt(9))
print(pow(3,2))


print('--------------------------------------------')
#3. yontem:

from math import factorial,sqrt,ceil # sadece 3 tanesini import eder.

print(sqrt(9))
print(ceil(8.9))
print(factorial(6))

# iki tane fonksiyonun ismi ayni oldugu zaman en son hangisi yazilmissa o kullanilir.