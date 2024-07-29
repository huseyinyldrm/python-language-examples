# bellekte gereksiz yer kaplamamak icin generator kullanilir.
# yield anahtar sozcugunu kullaniriz.
# ne zaman generator gerekli olur: anlik istenen deger varsa talep edildigi zaman deger getirilir , bellekte yer tutmaz.

print("1.Ornek".center(50,'-'))

def cube(): 
    for i in range(5):
        yield (i**3)

for i in cube():
    print(i)

print("2.Ornek".center(50,'-'))

generator=(i**3 for i in range(5)) # generatorde koseli parantez yerine normal parantez kullanilir dikkat!!!

print(generator)

for i in generator:
    print(i)