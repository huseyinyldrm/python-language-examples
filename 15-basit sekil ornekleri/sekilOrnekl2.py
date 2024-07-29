print('Kare Cizimi'.center(50,"-"))

for i in range(0,5):
    for j in range(0,5):
        print("*",end=" ")
    print()

print('Ici Bos Kare Cizimi'.center(50,"-"))

size=5
for i in range(size):
    for j in range(size):
        if(i==0 or i==size-1 or j==0 or j==size-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('Icinde Kum Saati Olan Kare'.center(50,"-"))

sayi=5

for i in range(sayi):
    for j in range(sayi):
        if(i==0 or i==sayi-1 or j==0 or j==sayi-1 or i==j or i+j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()