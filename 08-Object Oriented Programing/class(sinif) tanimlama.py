"""
class olusturma 

class <Class Ismi>():                            ***Class isminin buyuk harfle baslamasi tavsiye edilir 
    
    <class attribute>                            ***class a ait olan genel elemanlari icerir

    def __init__(self,<attribute>):              ***init, instantiation yani orneklendirmenin kisaltmasidir
        self.<instance attribute> = attribute    ***instance attribute lar, olusturulan objeye ozgudur
        .
        .
        .

    def <method>(self, <param>) :                ***methotlar class lara ozgu fonksiyonlardir
        .
        .
        .
        return ......
"""

class Araba():
    def __init__(self,marka,model,renk,km,hasar,fiyat):
        self.marka=marka
        self.model=model
        self.renk=renk
        self.km=km
        self.hasar=hasar
        self.fiyat=fiyat
    
    def AracBilgileri(self): # buraya dikkat
        print("Marka:",self.marka)
        print("Model:",self.model)
        print("Renk:",self.renk)
        print("Km Bilgisi:",self.km)
        print("Hasar Kaydi:",self.hasar)
        print("Fiyat Bilgisi:",self.fiyat,"TL")

taksi=Araba("Audi",2024,"Siyah",10000,"kayit yok",1000000)
print("\nTaksi Bilgileri")
taksi.AracBilgileri()