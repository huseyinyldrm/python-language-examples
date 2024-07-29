'''
def fonksiyonAdi():
    <kodlarin yazim alani>
fonksiyonAdi() # en son fonk.cagirilir.

eger foksiyon olusturup icerigini simdi yazmak istemiyorsaniz: <kod yazma alani> yerine pass veya return yazabilirsiniz.

'''

def topla():
    print(5,'+',7,'=',5+7)

topla()

print('************************')


def selamlama(isim):
    print("Sayin",isim,"restorantimiza hos geldiniz.")

selamlama("Ahmet")
selamlama("Fuat")

print('************************')

while True:
    ad=input("İsminiz nedir?")

    if ad=="dur":
        break
    selamlama(ad)