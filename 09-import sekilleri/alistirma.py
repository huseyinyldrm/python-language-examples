from math import pi

class Kup:  # küp alma sınıfı
    def __init__(self, a):
        self.a = a
    
    def yuzey_alan(self):
        return 6 * pow(self.a, 2)
    
    def hacim(self):
        return pow(self.a, 3)

class Kure:  # küre sınıfı
    def __init__(self, r):
        self.r = r

    def yuzey_alan(self):
        return f"Yüzey alanı: {4 * pi * pow(self.r, 2)} cm2'dir."

    def hacim(self):
        return (4 / 3) * pi * pow(self.r, 3)

class Silindir:  # silindir sınıfı
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def yuzey_alan(self):
        return 2 * pi * self.r * (self.h + self.r)

    def hacim(self):
        return pi * pow(self.r, 2) * self.h

# Kure sınıfından bir nesne oluşturun
top = Kure(3)
tencere=Silindir(5,7)

# Yüzey alanı ve hacmi ekrana yazdırın
print(top.yuzey_alan())
print(f"Hacmi: {top.hacim()}")

print(tencere.yuzey_alan())
print(f"Hacim:{top.hacim()}")

