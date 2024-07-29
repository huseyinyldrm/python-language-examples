K={1,'hg','*',3} # küme tanımlaması bu şekildedir.
K=set('abcdefgh') # K yazdırılınca hepsi ayrı ayrı tırnak içerisinde yazılır.
print(K)

k1={1,2,3,4,5}
k2={1,2,7,8,9}

print(k1|k2) # k1 ve k2 yi birleştirir ve aynı olanları bir kez yazar.
print(k2|k1) # bu da üsttekinin aynısıdır.
print(k1&k2) # k1 ve k2 nin kesişim elemanlarını verir.
print(k1-k2) # k1'in k2'den farkını gösterir.
print(k2-k1) # k2'nin k1'den farkını gösterir.