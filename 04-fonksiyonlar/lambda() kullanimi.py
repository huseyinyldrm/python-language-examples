# tek satirlik fonksiyon kulnmada lambda() kullanilir.

dolar=lambda TL: TL/30

TL=int(input("TL giris:"))
print(TL,"Turk Lirasi:",dolar(TL),"Dolar.")

euro=lambda TL: TL/33
TL=int(input("TL giris:"))
print(TL,"Turk Lirasi:",euro(TL),"EURO.")

altin=lambda TL: TL /2000
TL=int(input("Tl giris:"))
print(TL," ile ",altin(TL),"Giram altin alinabilir.")


