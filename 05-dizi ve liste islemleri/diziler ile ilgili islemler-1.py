liste=[1,2,3,'a','b','c']
print(liste) # listeyi oldugu gibi yazdırır.
print(liste[-1]) # en son indisteki değeri yazdırır.
no=liste[4]
print(no) # listedeki 4. elemanı yazdırır.


print("*************************************")
# listedeki bir elemanın indis numarasını ogrenmek için:

print(liste.index(3)) # 3 elemanı 2.indistedir.
print(liste.index('a'))# 'a' nın indisi=3

# listeyi dilimlemek için:
print("*************************************")

L=[0,1,2,3,4,5,6,7,8,9,10]
print(L[2:]) # 2. indisten itibaren yazdırır.
print(L[::-1]) # listeyi tersten yazdırır.
print(L[::2]) # 1den baslayarak ikişerli arttırır.
print(L[::3]) # 1 den baslatır üçerli yazdırır.
print(L[::-2])#sondan başlar ve ikiserli azaltır.

print("*************************************")
# listeye eleman eklemek için:
# .append() fonksiyonu kullanılır.

liste2=[1,3,5,7,9,11,13]
print(liste2) #olduğu gibi yazdırır.

liste2.append(15) # listenin sonuna ekler.
print(liste2)

liste2.insert(0,'a')#ilk argüman=istenen indis. 2. argüman = istenen eleman
print(liste2)


print("*************************************")
# döngüyle bir liste oluşturmak için:

A=[]

for i in range(0,5):
    sayi=int(input("Sayi giriniz:"))
    A.append(sayi)

print(A) # olusan listeyi yazdırır.

for i in range(0,5): # hangi indise hangi elemanın eklendiğini yazdırır.
    print("A[",i,"]",A[i])




