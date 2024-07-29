def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islemAdi):
    if(islemAdi=="toplama"):
        print(f1(5,6))
    elif(islemAdi=="cikarma"):
        print(f2(41,5))
    elif(islemAdi=="carpma"):
        print(f3(3,6))
    elif(islemAdi=="bolme"):
        print(f4(10,5))
    else:
        print("Gecersiz islem...")

islem(toplama,cikarma,carpma,bolme,"toplama")
islem(toplama,cikarma,carpma,bolme,"cikarma")
islem(toplama,cikarma,carpma,bolme,"carpma")
islem(toplama,cikarma,carpma,bolme,"bolme")
islem(toplama,cikarma,carpma,bolme,"toplamaa")