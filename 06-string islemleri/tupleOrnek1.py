#tuple turundeki listeye sonradan ekleme veya cikarma yapilmaz!!!
#Zaten tuple uzerinde sadece count ve index metotlari kullanilir. 

list=[1,2,3]
tuple=(1,'iki',3)

print(type(list))
print(type(tuple))

print(tuple[2])

print('----------------------')
list2=['Ali','Ahmet']
tuple2=('Mert','Hamdi')

list2[0]="Mehmet"
print(list2)

#tuple2[0]="Sena"
#print(tuple2) # bu iki satir calismaz.

names=('Demet','Sevgi','Ayse')+tuple2
print(names)