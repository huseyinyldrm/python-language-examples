#1-Girilen 2 sayidan hangisi buyuktur?

a=int(input("1.sayi: "))
b=int(input("2.sayi: "))

if(a>b):
    print(f"a:{a} sayisi b:{b} sayisindan buyuktur.")
else:
    print(f"a:{a} sayisi b:{b} sayisindan buyuk degildir.")


print("------------------------------------------------------")

#2-Kullanicidan 2 vize(%60) ve final(%40) notunu alip ortalama hesaplayin.
#Eger ortalama 50 ve uzeri ise gecti degilse kaldi.

vize1=float(input("1.vize notu: "))
vize2=float(input("2.vize notu: "))
final=float(input("final  notu: "))

ortalama=((vize1+vize2)*0.6 + final*0.4)

if(ortalama>=50):
    print("Dersi gectiniz.Ortalama: ",ortalama)
else:
    print("Dersten kaldiniz.Ortalama: ",ortalama)

print("------------------------------------------------------")

#3-girilen bir sayinin tek-cift durumunu kontrol edin.

number=int(input("Bir sayi giriniz: "))

if(number%2==0):
    print(f"{number} sayisi cifttir.")
else:
    print(f"{number} sayisi tektir.")

print("------------------------------------------------------")

#4-girilen bir sayinin negatif pozitif durumunu yazdirin.

sayi=int(input("Bir sayi giriniz: "))

if(sayi==0):
    print(f"{sayi} sayisi ne pozitif ne de negatiftir.")
elif(sayi>0):
    print(f"{sayi} sayisi pozitiftir.")
else:
    print(f"{sayi} sayisi negatiftir.")

print("------------------------------------------------------")

#5-Parola ve email bilgilerinin dogrulugunu kontrol ediniz.

email="email@sadikturan.com"
parola="abc123"

girisMail=input("Email adresini girin: ")
girisParola=input("Parolanizi girin: ")

if(email==girisMail):
    print("Girilen email dogrudur.")
    if(parola==girisParola):
        print("Girilen sifre dogrudur.")
    else:
        print("Girilen sifre yanlistir.")
else:
    print("Girilen email yanlistir.")
   
    if(parola==girisParola):
        print("Girilen sifre dogrudur.")
    else:
        print("Girilen sifre yanlistir.")