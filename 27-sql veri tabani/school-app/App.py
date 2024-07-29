from dbmanager import DbManager
import datetime
from Student import Student

class App:
    def __init__(self):
        self.db=DbManager()
    
    def initApp(self):
        msg="********************\n1-Ogrenci Listesi\n2-Ogrenci Ekle\n3-Ogrenci Guncelle\n4-Ogrenci Sil\n5-Ogretmen Ekle\n6-Siniflara Gore Dersler\n7-Cikis(E/C)\n******************** "

        while True:
            print(msg)
            islem=input("Seciminiz:")

            if islem=="1":
                self.displayStudents()
            elif islem=="2":
                self.addStudent()
            elif islem=="3":
                self.editStudent()
            elif islem=="4":
                self.deleteStudent()
            elif islem=="5":
                pass
            elif islem=="6":
                pass
            elif islem=="e" or islem=="c":
                break
            else:
                print("Yanlis secim...")
    
    def deleteStudent(self):
        classid=self.displayStudents()
        studentid=int(input("Ogrenci id:"))
        self.db.deleteStudent(studentid)
    



    def editStudent(self):
        classid=self.displayStudents()
        studentid=int(input("Ogrenci id:"))
        student=self.db.getStudentById(studentid)

        student[0].name=input("Name:") or student[0].name
        student[0].surname=input("Surname:") or student[0].surname
        student[0].gender=input("Cinsiyet(E/K):") or student[0].gender
        student[0].clasid=input("Sinif:") or student[0].classid
        
        year=input("Year:") or student[0].birthdate.year
        month=input("Month:") or student[0].birthdate.month
        day=input("Day:") or student[0].birthdate.day
        
        student[0].birthdate=datetime.date(year,month,day)
        self.db.editStudent(student[0])



    def addStudent(self):
        self.displayClasses()
        classid=int(input("Hangi sinif:"))
        number=input("Numara:")
        name=input("Ad:")
        surname=input("Soyad:")
        year=int(input("Yil:"))
        month=int(input("Ay:"))
        day=int(input("Gun:"))  
        birthdate=datetime.date(year,month,day)
        gender=input("Cinsiyet (E/K):")

        student=Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)



    def displayClasses(self):
        
        classes=self.db.getClasses()
        for c in classes:
            print(f"{c.id} : {c.name}")



    
    def displayStudents(self):
        
        self.displayClasses()
        print("\n--------------------------------\n")
        classid=int(input("Hangi sinif:"))
        print("\n--------------------------------\n")

        students=self.db.getStudentByClassId(classid)

        print("Ogrenci Listesi")
        print("\n--------------------------------\n")

        for index,std in enumerate(students):
            print(f"{index+1}--{std.name} {std.surname}")
        
        return classid



app=App()
app.initApp()