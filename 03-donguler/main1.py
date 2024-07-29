liste=['ali','mert','murat','zeynep','sevda']
print(liste)

liste2=[1,2,3,4,5]
print(liste2)

print('ali' in liste)#true döner
print('2' in liste)#false döner

isim=input("isminizi giriniz:")

print("----------Restaurant randevu sorgusu----------")
if isim in liste:
    print("Rezrevasyon var.")
if isim not in liste:
    print("Rezervasyon yok.")

Liste=['ali','mert','murat']
Liste2=['burak','fuat','remzi']
masaNo=0

isim=input("İsminiz nedir:")

if isim=='ali':
    masaNo=5
if isim=='mert':
    masaNo=6
if isim=='murat':
    masaNo=7
if isim in Liste:
    print(masaNo," Numarali masada rezervasyonu var.")
elif isim in Liste2:
    print("Rezervasyon bugun degil.")
else:
    print("Rezervasyonunuz yoktur. ")
