myList=[11,22,33,44,55,3,4,67,76,78,8,6]
print(f"Benim ilk listem:\n{myList}")

print('----------------------------')

ciftListe=[]
tekListe=[]

for num in myList:
    if(num%2==0):
        ciftListe.append(num)
    else:
        tekListe.append(num)

print(f"Cift sayilarin olusturdugu dizi:\n{ciftListe}")

print('----------------------------')

print(f"Tek sayilarin olusturdugu dizi:\n{tekListe}")
