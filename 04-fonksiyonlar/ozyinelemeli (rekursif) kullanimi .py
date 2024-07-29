def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1)
    
a=int(input("Taban giriniz:"))
b=int(input("Us giriniz:"))
print(ustel(a,b))