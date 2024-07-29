#1-id'ye gore aldigini bir ogrencinin bilgilerini guncelleyin
#2-cinsiyete gore aldiginiz bir ogrencinin bilgilerini guncelleyiniz.

import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender

    def saveStudent(self):
            sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
            value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
            try:
                cursor = connection.cursor()
                cursor.execute(sql, value)
                connection.commit()
                print(f"{cursor.rowcount} tane kayit eklendi.")
            except mysql.connector.Error as err:
                print("Hata:", err)
            

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = [(student.studentNumber, student.name, student.surname, student.birthdate, student.gender) for student in students]
        try:
            cursor = connection.cursor()
            cursor.executemany(sql, values)
            connection.commit()
            print(f"{cursor.rowcount} tane kayit eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
    
    
    def updateStudent(self):
        sql="update student set studentNumber=%s,Name=%s,Surname=%s,Birthdate=%s,Gender=%s WHERE id=%s"
        values=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)

        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit guncellendi.")
        except mysql.connector.Error as err:
            print("Hata:",err)
        

        
        
