class Person :
    #pass # yer tutucudur hata almamak icin kullanilir.
    
    #class attributes
    address='no information'

    #constructor(yapici metot)
    def __init__(self,name,year):# self veya this kullanilir.
        
        #object attributes
        self.name=name
        self.year=year

        print("init metodu calisti.")
   

    #instance methods
    def intro(self):#istege bagli referans verilir.
        print("Hello There.I am "+self.name)
    
    #instance methods
    def calculateAge(self):
        return 2024-self.year
    


#object(instance)
p1=Person(name='Ahmet',year=1990)
p2=Person(name="Ali",year=1993)

p1.intro()
p2.intro()

print(f"adim:{p1.name} ve yasim:{p1.calculateAge()}")
print(f"adim:{p2.name} ve yasim:{p2.calculateAge()}")

#updating
p1.name="Mert"
p2.name="Kaan"
#accessing object attributes
print(f"name: {p1.name} , year: {p1.year} , address:{p1.address}")
print(f"name: {p2.name} , year: {p2.year} , address:{p2.address}")

print('***********************************************')

class Circle:
    pi=3.14

    def __init__(self,yariCap=1):
        self.yariCap=yariCap
    
    #methods
    def cevreHesabi(self):
        return 2*self.pi*self.yariCap
    
    def alanHesapla(self):
        return self.pi*(self.yariCap**2)
    
c1=Circle()#yaricap=1
c2=Circle(5)

print(f"c1 : alan={c1.alanHesapla()} cevre = {c1.cevreHesabi()}")
print(f"c2 : alan={c2.alanHesapla()} cevre = {c2.cevreHesabi()}")