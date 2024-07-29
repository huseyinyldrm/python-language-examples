#1-100 e kadar olan sayileri yazdir:
x=0
while (x<=100):
    print(x)
    x+=5
print("Bitti...")
print('--------------------------------')

#1-50 arasi cift sayilari yazdir:
b=0
while (b<=50):
    if(b%2==0):
        print(b)

    b+=1
print("Bitti...")
print('--------------------------------')

name=''
while not name.strip():#bosluk karakterinin onune gecer.
    name=input("isminizi giriniz:")
print(f"Merhaba {name}")
