'''
mesela dikdortgenAlani isimli bir dosyamiz olsun.Bu dosyamizi çağirmak için şunu yazariz:
from dikdortgenAlani import* = bununla bütün özellikler kullanilabilir.
Eğer tek bir özellik kullanilmak isteniyorsa:
from dikdortgenAlani import cevre 
bu kodu çaliştirdiktan sonra diğerleri çalişmaz.Sadece çağrilan fonksiyon çalişir.
İsim uzun olduğunda kisaltmak için şu işlem yapilir: import dikdortgenAlani as dik = bundan sonra dik.cevre(8,2) gibi işlem yapilabilir.
'''
import math

print(math.sqrt(100))# karekok alir
print(math.pow(2,5))# üs alir.
print(math.factorial(6)) # faktorielini alır.
