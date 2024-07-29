import re
# arama sonuclarini gosterir.
print("re kutuphanesi degerleri aciklamasi:".center(50,"*"))
print("----------------------------------------")
print("\n")

aciklama=dir(re)
print(aciklama)

print("\n")

#re module


str="Python Kursu: Python Programlama Rehberiniz | 40 Saat"

print("----------------------------------------")

print("re.findall() metodu ile istenilen ifadenin aramasi:".center(60,"*"))
sonuc=re.findall("Python",str)
print(sonuc)
print("----------------------------------------")

print("re.split() ile verilen ifadeden itibaren her string ifadeyi bolme: ".center(80,"*"))
sonuc2=re.split(" ",str)
print(sonuc2)
print("----------------------------------------")

print("re.sub() metodu ile degistirme yapma islemi:".center(50,"*"))
sonuc3a=re.sub(" ","-",str)
print(sonuc3a)
print("----------------------------------------")

sonuc3b=re.sub("\s","*",str)
print(sonuc3b)
print("----------------------------------------")

print("re.search() metodu ile verilen ifadenin ilk nerde gectigini bulma:".center(80,"*"))
print("----------------------------------------")
sonuc4=re.search("Python",str)
print(sonuc4)

print("----------------------------------------")

sonuc4a=sonuc4.span()
print("Bulunan kelime hangi indeksler arasinda:",sonuc4a)

print("----------------------------------------")

sonuc4b=sonuc4.start()
print("Bulunan kelime hangi indexten basliyor:",sonuc4b)

print("----------------------------------------")

sonuc4c=sonuc4.end()
print("Bulunan kelime hangi index ile bitiyor:",sonuc4c)

print("----------------------------------------")

sonuc4d=sonuc4.group()
print("Bulunan kelimeyi gonderir:",sonuc4d)

print("----------------------------------------")

sonuc4e=sonuc4.string
print("Aranan ifade nerede araniyor:",sonuc4e)

print("----------------------------------------")

# regular expression

"""
[]- Koseli parantezler arasina yazilan butun karakterler aranir.
     
    [abc] =>a      : 1 match 
            ac     : 2 match  
            Python : No matches
    [a-e] => [abcde]
    [1-5] => [12345]
    [^abc]=> abc disindaki karakterler.
    [^0-9]=> rakam olmayan karakterler.
 
"""
result=re.findall("[a-e]",str)
print("str metni icindeki a-e harfleri:\n",result)

print("----------------------------------------")

result1=re.findall("[0-9]",str)
print("str metni icindeki 0-9 arasi rakamlar:\n",result1)

print("----------------------------------------")

result1=re.findall("[^0-9]",str)
print("str metni icindeki rakamlar haric karakterler:\n",result1)

print("----------------------------------------")

result=re.findall("[^abc]",str)
print("str metni icindeki abc disindaki karakterler:\n",result)

print("----------------------------------------")

"""
. ifadesi herhangi bir karakteri belirtir.
    .. => a     : No match
          ab    : 1 match   (ab)
          abc   : 1 match   (ab)
          abcd  :2 matches  (ab ve cd)
"""
rs1=re.findall("...",str)
print("str metni icindeki 3 gruplu karakterler:\n",rs1)

print("----------------------------------------")

rs2=re.findall("Py..on",str)
print(rs2)

print("----------------------------------------")

"""
^ - Belirtilen karakter ile basliyor mu?
^a => a   : 1 match
      abc : 1 match
      bac : No match
"""

rs3=re.findall("^P",str) # baska harf yazilirsa bos kume doner.
print("String ifade P ile basliyor mu:",rs3)

print("----------------------------------------")

"""
$ - Belirtilen karakterle bitiyor mu?

a$ => a     : 1 match
     lamba  : 1 match
     python : No match

"""

rslt=re.findall("t$",str)
print("String ifade t ile bitiyor mu:",rslt)
print("----------------------------------------")

"""
* - Bir karakterin sifir ya da daha fazla sayida olmasini kontrol eder.

ma*n => mn   : 1 match
        man  : 1 match
        maaan: 1 match
        main : No match (a'nin arkasina n gelmiyor.)
"""
result2=re.findall("Sa*t",str) # buyuk-kucuk harf uyumu vardir.Dikkat
print("String ifadede istenilen veri var mi:",result2)

print("----------------------------------------")

"""
+ - Bir karakterin bir ya da daha fazla sayida olmasini kontrol eder.

ma+n => mn    : No match
        man   : 1 match
        maaan : 1 match
        main  : No match(a'nin arkasina n gelmiyor.)
        
"""
rest1=re.findall("Sa+t",str)
print("String ifadede istenilen veri var mi:",rest1)

"""
? - Bir karakterin sifir ya da bir kez olmasini kontrol eder.

        ma?n => mn    : No match
                man   : 1 match
                maaan :1 match
                main  : No match(a'nin arkasina n gelmiyor.)

"""

rest2=re.findall("S?a",str)
print("String ifadede istenilen veri var mi:",rest2)

print("----------------------------------------")

"""
{} - Karakter sayisini kotrol eder.

al{2} => a karakterinin arkasina l karakteri 2 kez tekrarlanmali.
al{2,3} => a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlanmali.
[0-9]{2,4} => en az 2 en cok 4 basamakli sayilar.

"""
rest3=re.findall("a{2}",str)
print("a'nin 2 kere tekrarlandigi ifadeler:",rest3)

print("----------------------------------------")

rest4=re.findall("[0-9]{2}",str)
print("Stringifade icindeki 2 basamakli sayilar:",rest4)

"""
| - Alternatif seceneklerden birinin gerceklesmesi gerekir.

    a|b => a ya da b

        cde    => No match
        ade    => 1 match
        acdbea => 3 match

"""

rest5=re.findall("a|b",str)
print("String ifade icindeki a veya b ifadeleri:",rest5)

print("----------------------------------------")

"""
() - gruplamak icin kullanilir.

    (a|b|c)xz => abc karakterlerinin arkasina xz gelmelidir.


"""
rest6=re.findall("(a|b|c)t",str)
print("a,b,c karakterlerinin arkasina t gelen ifadeler: ",rest6)

print("----------------------------------------")

"""
\ - Ozel karakterleri aramamizi saglar.
    \$a => $ karakterinin arkasina a karakterini arar.Yani $ regular exp. tarafindan yorumlanmaz.

    \A - Belirtilen karakter string'in basinda mi:
        \Athe => the stringin basinda mi?

    \Z - Belirtilen karakter stringin sonunda mi?
        the\Z => the string'in sonunda mi?

    \b - Belirtilen karakter kelimenin basinda ya da sonunda mi?
        \bthe => the kelimenin in basinda mi?
        the\b => the kelimenin in sonunda mi?

    \B - Belirtilen karakter kelimenin in basinda ya da sonunda degil mi?
        \Bthe => the kelimenin in basinda degil mi?
        the\B => the kelimenin in sonunda degil mi?

    \d - [0-9] ile ayni anlama gelir yani rakamlari arar.
        \d => 12abc34

    \D - [^0-9] ile ayni anlam gelir yani rakam olmayanlari arar.
        \D => 1ab44_50

    \s - Bosluk karakterlerini arar.
    \S - Bosluk karakterleri disindakileri arar.
    \w - Alfabetik karakterler , rakamlar ve cizgi karakteri.
    \W - \w'nin tam tersi arama yapar. 

"""

rest7=re.findall("\APython",str)
print("String ifade Python ile mi bitiyor:",rest7)

print("----------------------------------------")

rest8=re.findall("Saat\Z",str)
print("String ifade Saat ifadesi ile mi bitiyor:",rest8)

# bunlarin hepsi ve daha fazlasi W3school sitesinden bulabiliriz.