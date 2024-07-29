# 1. ornek:

x=int(input("x:"))
if(x>5):
    raise Exception("x 5'ten buyuk olamaz.")


print('-----------------------------------')

#2. ornek:

def checkPassword(psw):
    import re

    if(len(psw)<8):
        raise Exception("Parola en az 7 karakter olamlidir.")
    elif not re.search(r"[a-z]",psw):
        raise Exception("Parola kucuk harf icermelidir.")
    elif not re.search(r"[A-Z]",psw):
        raise Exception("Parola buyuk harf icermelidir.")
    elif not re.search(r"[0-9]",psw):
        raise Exception("Parola rakam icermelidir.")
    elif not re.search(r"[_@$]",psw):
        raise Exception("Parola alpha numeric karakter icermelidir.")
    elif re.search(r"\s",psw):
        raise Exception("Parola bosluk icermemelidir.")
    else: 
        print("Gecerli parola.")

password="12345678Aa@"

try:
    checkPassword(password)
except Exception as ex:
    print(ex)

else:
    print("gecerli parola : else")

finally:
    print("Validation tamalandi.")



'''
Raw string'ler (r"...") kullanmak, kacis dizileriyle ilgili sorunlar olmadan,duzenli ifadelerin dogru sekilde yorumlanmasini saglar.
'''
print('-----------------------------------')
# 3. ornek:

class Person:
    def __init__(self,name,year):
        if(len(name)>10):
            raise Exception("name alani fazla karakter iceriyor.")
        else:
            self.name=name
            self.year=year
try:
    p=Person("Aliiiiiiiiiiii",30)
except Exception as ex:
    print(ex)