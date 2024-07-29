class Hayvan:
    def __init__(self,isim):
        self.isim=isim
    
    def sesCikar(self):
        pass

class Kopek(Hayvan):
    def sesCikar(self):
        return "Hav hav!"
class Kedi(Hayvan):
    def sesCikar(self):
        return "Miyav miyav!"

kopek=Kopek("Karabas")
kedi=Kedi("Minnos")

print(f"{kopek.isim} ses cikarir: {kopek.sesCikar()}")

print(f"{kedi.isim} ses cikarir: {kedi.sesCikar()}")
        