# eleman ekleme ve çıkarma işlemini listenin başından gerçekleştiği özel bir yapıdır.
#listeye son giren - son çıkar(last in - last out). sırada bekleyen insanlar misali.
#burada da .append() ve .pop() kullanılır. yığın oluşturmadan farkı pop içine parametre girilmelidir.

L=[]
L.append(1)
L.append(2)
L.append(50)
L.append(90)
L.append(78)

print(L)

L.pop(0) # istenilen indisteki eleman yazılır listeden çıkarılır.
print(L)
print(L[-1])# 78
print(L[::-1])