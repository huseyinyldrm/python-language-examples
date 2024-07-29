import random

# Kelime listeleri
kolay_kelime_listesi = ["elma", "armut", "kedi", "köpek", "yüz"]
orta_kelime_listesi = ["insan", "araba", "kavun", "limon", "kitap"]
zor_kelime_listesi = ["mühendis", "bilgisayar", "program", "puzzle", "matematik"]

adam_cizimleri = [
    """
     ------
     |    |
          |
          |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ---------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ---------
    """
]

def kelime_sec(zorluk):
    if zorluk == 'kolay':
        return random.choice(kolay_kelime_listesi)
    elif zorluk == 'orta':
        return random.choice(orta_kelime_listesi)
    elif zorluk == 'zor':
        return random.choice(zor_kelime_listesi)
    else:
        return None

def adam_asmaca():
    print("Adam Asmaca Oyununa Hos Geldiniz!")
    zorluk = input("Zorluk seviyesi seciniz (kolay/orta/zor): ").lower()
    
    kelime = kelime_sec(zorluk)
    if kelime is None:
        print("Gecersiz zorluk seviyesi!")
        return

    kelime_harfleri = set(kelime)
    tahmin_edilen_harfler = set()
    dogru_tahmin_edilen_harfler = set()
    yanlis_tahmin_sayisi = 0
    max_yanlis_tahmin = 6

    while len(kelime_harfleri) > 0 and yanlis_tahmin_sayisi < max_yanlis_tahmin:
        print(adam_cizimleri[yanlis_tahmin_sayisi])
        print("Tahmin edilen harfler: ", " ".join(tahmin_edilen_harfler))
        kelime_listesi = [harf if harf in dogru_tahmin_edilen_harfler else '_' for harf in kelime]
        print("Kelime: ", " ".join(kelime_listesi))
        
        tahmin = input("Bir harf tahmin ediniz: ").lower()
        
        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten tahmin ettiniz!")
        elif tahmin in kelime_harfleri:
            dogru_tahmin_edilen_harfler.add(tahmin)
            kelime_harfleri.remove(tahmin)
            print(f"{tahmin} harfi dogru!")
        else:
            tahmin_edilen_harfler.add(tahmin)
            yanlis_tahmin_sayisi += 1
            print(f"{tahmin} harfi yanlis! Kalan yanlis tahmin hakkiniz: {max_yanlis_tahmin - yanlis_tahmin_sayisi}")
    
    if len(kelime_harfleri) == 0:
        print("Tebrikler! Kelimeyi buldunuz: {}".format(kelime))
    else:
        print(adam_cizimleri[max_yanlis_tahmin])
        print("Kaybettiniz! Kelime suydu: {}".format(kelime))


"""
Bu kalip, bir dosyanin hem bagimsiz bir program olarak calistirilabilmesini hem de baska bir dosya tarafindan modul olarak kullanilabilmesini saglar. Bu sayede kodunuzu yeniden kullanilabilir hale getirmis olursunuz.
"""
if __name__ == "__main__":
    adam_asmaca()
