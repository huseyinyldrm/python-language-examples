#stringi listeye dönüştürme: list() fonksiyonu kullanılır.

kelime='Andromeda Galaksisi'
L=[]
L=list(kelime)
print(L) # bütün harfleri birer elemana dönüştürür.

print("**********************************")

#listeden eleman silme: .remove() fonksiyonu kullanılır. .pop(indis no) ile istenilen indisteki eleman silinir. .clear() ile bütün elemanlari siler.

L.remove('A') # istenilen harfi siler.
print(L)

L.pop(5) # güncel listeden 5 nolu indisi siler.
print(L)

L.clear() # boş liste döndürür.
print(L)

print("****************************************")
#listede arama yapma:

A=[1,2,3,5,6,7,8,9,0,'a','f','t']

print(1 in A) #true döner

print('h' not in A) # true döner çünkü gerçektende h listede yoktur.

print(10 in A)# false döner.

print("****************************************")
#liste elemanlarını sıralama: .sort() fonksiyonu ile liste elemanları küçükten büyüğe doğru sıralanır.

L=[123,321,444,555,421,512,765,789]
L.sort()
print(L)
#güncel diziyi büyükten küçüğe doğru sıralamak için:
L=L[::-1]
print(L)