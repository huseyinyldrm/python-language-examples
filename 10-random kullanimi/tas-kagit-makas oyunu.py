import random
liste=["taş","kağit","makas"]
pc=random.choice(liste)#bilgisayarın seçimi
player=input("[taş-kağit-makas]")

print("Bilgisayar=",pc,"secti.")
print("Sen=",player,"sectin.")

if pc==player:
    print("berabere")
if pc=="kağit" and player=="taş":
    print("Kaybettin")
if pc=="taş" and player=="makas":
    print("Kaybettin")
if pc=="makas" and player=="kağit":
    print("Kaybettin")

if pc=="kağit" and player=="makas":
    print("Kazandin")
if pc=="taş" and player=="kağit":
    print("Kazandin")
if pc=="makas" and player=="taş":
    print("Kazandin")

else:
    print("liste dişi giriş yaptiniz.!")
