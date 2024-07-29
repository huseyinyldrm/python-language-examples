#Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesaplayiniz:
#1.Bakim =>1.yil
#2.Bakim =>2.yil
#3.Bakim =>3.yil
# ** Sure hesabini gun,ay yil bilgisine gore gun bazli hesaplayiniz.
# *** datetime modulunu kullanmaliyiz.
#(simdi)-(2018/8/1) => gun

import datetime

tarih=(input("Arac hangi tarihte trafige cikti(yil/ay/gun):"))
tarih=tarih.split('/')# alinan tarihi parcalara boler.
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))# parcalara bolunen verileri alir int e dondurur.
simdi=datetime.datetime.now()#simdiki zamani alir.

fark=simdi-trafigeCikis

days=fark.days
print("Gecen Sure:",days)

if(days<=365):
    print("1.Servis Araligi.")
elif(days>365) and(days<=365*2):
    print("2.Servis Araligi.")
elif(days>365*2) and (days<=365*3):
    print("3.Servis Araligi.")
else:
    print("Hatali sure.")