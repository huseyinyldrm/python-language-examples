class Araba:
    def __init__(self,marka,model,yil,renk):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        self.hiz=0

    def hizlan(self,miktar):
        self.hiz+=miktar
        print(f"{self.marka} {self.model} {miktar} km/h hizlandi.Yeni hiz :{self.hiz} km/h")

    def yavasla(self,miktar):
        self.hiz-=miktar
        if(self.hiz<0):
            self.hiz=0
        print(f"{self.marka} {self.model} {miktar} km/h yavasladi. Yni hiz:{self.hiz} km/h")

    def bilgileriGoster(self):
        print(f"Araba Bilgileri:Marka:{self.marka},Yil:{self.yil},Renk:{self.renk},Hiz:{self.hiz} km/h")

#araba nesnelerini olusturalim
araba1=Araba("Volvo","XC60",2024,"Gri")
araba2=Araba("Audi","RS7",2024,"Siyah")

#araba nesneleri uzerinde islemler yapalim.
araba1.bilgileriGoster()
print('--------------------------------------')
araba1.hizlan(60)
araba1.yavasla(20)
araba1.bilgileriGoster()

print('**************************************')

araba2.bilgileriGoster()
print('--------------------------------------')
araba2.hizlan(320)
araba2.yavasla(100)
araba2.bilgileriGoster()
        