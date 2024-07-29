class Sekil:
    def __init__(self,isim):
        self.isim=isim
    
    def alan(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, isim,genislik,yukseklik):
        super().__init__(isim) #1. kullanim(inheritance)
        self.genislik=genislik
        self.yukseklik=yukseklik
    
    def alan(self):
        return self.genislik*self.yukseklik
    
    def cevre(self):
        return 2*(self.genislik+self.yukseklik)
    

class Daire(Sekil):
    def __init__(self, isim,yaricap):
        Sekil.__init__(self,isim) #2. kullanim(inheritance)
        self.yaricap=yaricap
        self.pi=3.14

    def alan(self):
        return self.pi*(self.yaricap**2)
    def cevre(self):
        return 2*self.pi*self.yaricap

dikdortgen=Dikdortgen("Dikdortgen",4,5)
kare=Dikdortgen("Kare",6,6)
daire=Daire("Daire",5)

print('----------------------------------------------------')

print(f"{dikdortgen.isim} alani: {dikdortgen.alan()}")
print(f"{dikdortgen.isim} cevresi:{dikdortgen.cevre()}")

print('----------------------------------------------------')

print(f"{kare.isim} alani: {kare.alan()}")
print(f"{kare.isim} cevresi: {kare.cevre()}")

print('----------------------------------------------------')

print(f"{daire.isim} alani: {daire.alan()}")
print(f"{daire.isim} cevresi: {daire.cevre()}")

print('----------------------------------------------------')
