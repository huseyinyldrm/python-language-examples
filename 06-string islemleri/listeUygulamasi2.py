"""
1-"Bmw,Mercedes,Opel,Mazda" elemanlarina sahip bir liste olusturun.
2-Liste kac elemanlidir?
3-Listenin ilk ve son elemani nedir?
4-Mazda degerini Toyota ile degistirin.
5-Mercedes listenin bir elemani midir?
6-Listenin -2 indexsindeki deger nedir?
7-Listenin ilk 3 elemanini alin?
8-Listenin son 2 elemani yerine "Toyota" ve "Volvo" degerlerini ekleyin.
9-Listenin uzerine "Audi" ve "Nissan" degerlerini ekleyin.
10-Listenin son elemanini silin.
11-Listenin elemanlarini tersten yazin.
12-Asagidaki verileri bir liste icinde saklayin:

studentA:Yigit Bilgi 2010,(70,60,70)
studentB:Sena Turan 1999,(80,80,70)
studentC:Ahmet Turan 1998,(80,70,90)

13-Liste elemanlarini ekrana yazdirin.

"""
arabalar=['Bmw','Mercedes','Opel','Mazda']
print(arabalar)#1.soru cevabi

print(len(arabalar))#2.soru cevabi
print(arabalar[0])#3.soru cevabi
print(arabalar[-1])

arabalar[-1]='Toyota'#4.soru cevabi
print(arabalar)

result='Mercedes' in arabalar#5.soru cevabi
print(result)

print(arabalar[-2])#6.soru cevabi

print(arabalar[0:3])#7.soru cevabi
print(arabalar[:3])
print(arabalar[-2:])


arabalar[-2:]=['Toyota','Volvo']#8.soru cevabi
print(arabalar)

ekleme=arabalar+['Audi','Nissan']#9.soru cevabi
print(ekleme)

print(arabalar.pop(-1))#10.soru cevabi
print(arabalar)

print(arabalar[::-1])#11.soru cevabi

studentA=['Yigit','Bilgi',2010,[70,60,70]]#12.soru cevabi
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

print('-------------------------------------')


print(studentA)
print(studentB)
print(studentC)

print('-------------------------------------')

resultA=f"{studentA[0]} {studentA[1]} isimli ogrencinin yasi:{2024-studentA[2]} ve ortalamasi:{(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(resultA)
print('-------------------------------------')

resultB=f"{studentB[0]} {studentB[1]} isimli ogrencinin yasi:{2024-studentB[2]} ve ortalamasi:{(studentB[3][0] + studentB[3][1] + studentB[3][2])/3}"
print(resultB)
print('-------------------------------------')

resultC=f"{studentC[0]} {studentC[1]} isimli ogrencinin yasi:{2024-studentC[2]} ve ortalamasi:{(studentC[3][0] + studentC[3][1] + studentC[3][2])/3}"
print(resultC)

print('-------------------------------------')