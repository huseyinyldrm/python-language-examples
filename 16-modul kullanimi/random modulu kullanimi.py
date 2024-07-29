import random

#result=dir(random)
#print(result)
#result=random.random() # 0.0-1.0
#result=random.random*100 #1-100
print('--------------------------------------------')

result=int(random.uniform(1,10)) #1-10 arasi bir sayi uretir.
print(result)

print('--------------------------------------------')

result2=random.randint(1,10)
print(result2)

print('--------------------------------------------')

names=['Ali','Yagmur','Deniz','Cenk','Efe','Can']
result3=names[random.randint(0,len(names)-1)]
result4=random.choice(names)# bu da ayni gorevi gorur.
print(result4)
print(result3)

print('--------------------------------------------')

greeting='hello there'
result5=random.choice(greeting) # girilen string mesaj icinden rastgele karakter secer.
print(result5)

print('--------------------------------------------')
liste=list(range(10))
random.shuffle(liste) # verilen liste elemanlarini karistirir.
print(liste)

print('--------------------------------------------')

liste2=range(100)
result6=random.sample(liste2,3) # verilen deger araliginda rastgele sayi getirir. 
print(result6)