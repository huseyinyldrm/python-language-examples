import random
print("10 soruluk bir carpim tablosu testi")
skor=0
for a in range(10):
    i=random.randint(1,10)# 1-10 arası değer
    x=random.randint(1,10)
    soru="{}*{}=".format(i,x)

    dCvp=i*x
    cevap=input(soru)

    if int(cevap)==dCvp:
        skor+=1
print("dogru sayisi= ",skor) 
if skor>8:
    print("pekiyi")
elif skor>6:
    print("iyi")
elif skor>4:
    print("orta")
else:
    print("daha cok calis")
    
    

    
