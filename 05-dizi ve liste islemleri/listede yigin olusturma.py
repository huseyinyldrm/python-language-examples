# eleman ekleme ve çıkarma işlemlerinin listenin en son elemanı üzerinden yapılan özel bir yapıdır.
# .append() fonksiyonu ile her kullanıldığında listenin sonuna ekleme yapar.
# .pop() fonksiyonu ile her kullanıldığında listenin sonundan eleman silinir.
#listeye son giren - ilk çıkar (last in - first out) 

L=[]
L.append(12)#0. index
L.append(13)#1. index
L.append(21)#2. index
L.append(34)
print(L)

L.pop() # en son eklenen ilk çıkar . ilk çıkan 34
print(L)
L.pop() # 21 çıkar.
print(L)

print(L[-1]) # günce listedeki son indekste olan elemanı verir.
