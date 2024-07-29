# inheritance(Kalitim): Miras alma

#Person => name,lastname,age,eat(),run(),drink()
#Student(Person), Teacher(Person)

#Animal => Dog(Animal),Cat(Animal)

class Person:
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print("Person created.")

    def whoAmI(self):
        print("I am a person.")
    
    def eat(self):
        print("I am eating.")


class Student(Person):# inheritance burada yapildi.
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname) # bunu yapilmasinin sebebi Person class'inin tum ozelliklerinden yararlanmaktir.
        self.studentNumber=number
        print("Student created.")
    
    #override
    def whoAmI(self):
        print("I am a student.")

    def sayHello(self):
        print("Hello I am a student.")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch

    def whoAmI(self):
        print(f"I am a {self.branch} teacher")

p1=Person('Ali','Yilmaz')
print('-----------------------------')
s1=Student('Cinar','Turan',457)

print('-----------------------------')

print(p1.firstName + ' '+ p1.lastName)
print(s1.firstName + ' '+ s1.lastName ,' ', s1.studentNumber)

print('-----------------------------')

p1.whoAmI()
s1.whoAmI()

print('-----------------------------')

p1.eat()
s1.eat()

print('-----------------------------')
s1.sayHello()
print('-----------------------------')

t1=Teacher("Huseyin","Yildirim","Software")
t1.whoAmI()