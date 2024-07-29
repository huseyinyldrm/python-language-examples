# burada kuyruk oluşturma uygulaması vardır.

L=[]

while True:
    isim=input("İsim giriniz:")
    L.append(isim)

    if isim=='siradaki':
        L.pop(0)
        print(L)
    if isim=='bitti':
        print("Yarin kaldigimiz yerden devam ederiz.")
        break