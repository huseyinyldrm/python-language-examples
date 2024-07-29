# kalıtım üst sınıfa ait olan özelliklerin alt sınıflara miras olarak aktarılması özelliğidir. böylece alt sınıf üst sınıfın özelliğini taşır.

import datetime

class Araba(): # üst sınıf
    def __init__(self,model,fiyat):
        self.model=model
        self.fiyat=fiyat

    def aracBilgisi(self):
        print("Araba Modeli:",self.model)
        print("Araba Fiyati:",self.fiyat)
        return (datetime.datetime.now())

class kamyon(Araba): #alt sınıf
    def __init__(self, model, fiyat,renk):
        Araba.__init__(self,model, fiyat)
        self.renk=renk

k1=kamyon(2022,12000,"siyah")
k1.aracBilgisi()