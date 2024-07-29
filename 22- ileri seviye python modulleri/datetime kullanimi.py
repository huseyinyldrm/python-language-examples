# dosya adinin 'datetime.py' olarak yazma yoksa datetime kutuphanesi duzgun calismaz.

from datetime import datetime
from datetime import timedelta

res8=dir(datetime)
print("Datetime kutuphanesindeki tum modulleri verir:\n\n",res8)

print("\n---------------------")

simdi=datetime.today()

res1=datetime.now()
print("Su anki tarihi verir:",res1)

print("---------------------")
res2=simdi.year 
print("Yil bilgisi verir:",res2)

print("---------------------")
res3=simdi.month #
print("Ay bilgisi verir:",res3)

print("---------------------")
res4=simdi.day # 
print("Gun bilgisi verir:",res4)

print("---------------------")
res5=simdi.hour #
print("Saat bilgisi verir:",res5)

print("---------------------")
res6=simdi.minute # 
print("Dakika bilgisi verir:",res6)

print("---------------------")
res7=simdi.second # 
print("Saniye bilgisi verir:",res7)

print("---------------------")

print("Asagidakiler baska metotlar ile yapildi:".center(60,"*"))
suan=datetime.today()

print("\n---------------------")
sonuc1= datetime.ctime(suan)
print("Su anki tarihi verir:",sonuc1)

print("---------------------")

sonuc2=datetime.strftime(suan,'%Y')
print("Su anki yil bilgisini verir:",sonuc2)

print("---------------------")
sonuc3=datetime.strftime(suan,'%X')
print("Su naki saat bilgisini verir:",sonuc3)

print("---------------------")
sonuc4=datetime.strftime(suan,'%d')
print("Ayin gun bilgisini verir:",sonuc4)


print("---------------------")
sonuc5=datetime.strftime(suan,'%A')
print("Haftanin hangi gun oldugu bilgisini verir:",sonuc5)


print("---------------------")
sonuc6=datetime.strftime(suan,'%B')
print("Ay bilgisini verir:",sonuc6)

print("---------------------")
sonuc7=datetime.strftime(suan,'%Y %B %A')
print("Yil , ay , gun bilgisini verir:",sonuc7)

print("---------------------")
# verilen tarihi parcalara ayirma islemi:

t='20 Haziran 2024'

gun,ay,yil=t.split()

print(gun)
print(ay)
print(yil)

print("---------------------")
#Verilen tarihi parcalara ayirma islemi2:

t2='20 June 2024 hour 10:12:30'

dt=datetime.strptime(t2,'%d %B %Y hour %H:%M:%S')
# Dikkat !!! strptime metodu bilgileri ingilizce ister.
print(dt)

bilgi1=dt.year
print(bilgi1)

bilgi2=dt.day
print(bilgi2)

bilgi3=dt.hour
print(bilgi3)

print("---------------------")

birthday=datetime(1993,5,6,12,30,10)
print(birthday)

result1=datetime.timestamp(birthday)
print("Verilen tarihi saniyeye cevirir:",result1) # saniye

print("---------------------")

result2=datetime.fromtimestamp(result1) # saniye to datetime
print("Verilen saniyeyi tarihe cevirir:",result2)

print("---------------------")

result3=datetime.fromtimestamp(0)
print("Bilgisayar icin milad tarihini veirir:",result3)

print("---------------------\n")

print("Verilen tarihler arasinda cikarma islemleri:".center(75,'*'))

ika=datetime.now()
dogumGunu=datetime(1995,6,5,12,45,25)

print("---------------------")
misal1=ika - dogumGunu
print("Verilen tarh ile simdiki tarih arasindaki farki verir gun olarak:",misal1)

print("---------------------")
misal2=misal1.days
print("Sadece cikan gun sayisini verir:",misal2)

print("---------------------")
misal3=misal1.seconds
print("Cikan gun farkini saniye cinsinden verir:",misal3)

print("---------------------")
misal4=misal1.microseconds
print("Cikan tarih bilgisini mikrosanye cinsinden verir:",misal4)

print("---------------------\n")
print("Verilen tarihler arasinda ekleme  islemleri:".center(75,'*'))

newe=datetime.now()
#waxt=datetime(1995,6,4,12,45,00)

ekleme1=newe + timedelta(days=10)
print("Verilen tarihe ekleme yapar:",ekleme1)

print("---------------------")
ekleme2=newe + timedelta(days=730,minutes=10)
print("Verilen tarihe eklem yapar:",ekleme2)

print("---------------------")
ekleme3=newe - timedelta(days=20)
print("Verilen tarihten cikarma yapar:",ekleme3)