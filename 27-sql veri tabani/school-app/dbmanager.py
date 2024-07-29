import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self):
        self.connection=connection
        self.cursor=self.connection.cursor()

    def getStudentById(self,id):
        sql="SELECT *From student WHERE id=%s"
        value=(id,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata:",err)

    def deleteStudent(self,studentid):
        sql = "DELETE from student WHERE id=%s"
        value = (studentid,)
        try:
            cursor = self.connection.cursor()
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayit silindi.")
        except mysql.connector.Error as err:
            print("Hata:", err)

    
    def getClasses(self):
        sql="SELECT *From class"
        self.cursor.execute(sql)
        try:
            obj=self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Hata:",err)

        

    def getStudentByClassId(self,classid):
        
        sql="SELECT *From student WHERE classid=%s"
        value=(classid,)
        self.cursor.execute(sql,value)
        try:
            obj=self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata:",err)

    def addorEditStudent(self,student):
        pass


    def addStudent(self,student:Student):
        sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender,ClassId) VALUES (%s, %s, %s, %s, %s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        try:
            cursor = self.connection.cursor()
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayit eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)




    def editStudent(self,student:Student):
        sql ="UPDATE student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s WHERE id=%s"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid,student.id)
        try:
            cursor = self.connection.cursor()
            self.cursor.execute(sql, value)
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayit guncellendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        


    def addTeacher(self,teacher:Teacher):
        pass

    def editTeacher(self,teacher:Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi.")
    


# db=DbManager()

# student=db.getStudentById(7)
# student[0].name="Betul"
# student[0].surname="Cakirbeyli"
# student[0].studentNumber="500"
# #db.addStudent(student[0])
#db.editStudent(student[0])
#print(student[0].name+" "+student[0].surname)


# students=db.getStudentByClassId(1)
# print(students[0].name)