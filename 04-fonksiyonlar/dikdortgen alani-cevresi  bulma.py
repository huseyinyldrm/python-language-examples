
def alan(uzunluk,genislik):
    alan=(uzunluk*genislik)

    return alan

def cevre(uzunluk,genislik):
    cevre=2*(genislik+uzunluk)

    return cevre

uzunluk=int(input("Dikdortgenin uzun kenari:"))
genislik=int(input("Dikdortgenin kisa kenari:"))

print("Dikdortgenin Alani:",alan(uzunluk,genislik))

print("Dikdortgenin cevresi:",cevre(uzunluk,genislik))