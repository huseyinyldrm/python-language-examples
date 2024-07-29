from connection import connection
from datetime import datetime
import mysql.connector

class Student:
    def __init__(self, studentNumber, name, surname, birthdate, gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

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
        finally:
            cursor.close()

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
        finally:
            cursor.close()


# Öğrencileri Student sınıfından nesneler olarak tanımlayın
derya = Student("101", "Derya", "Cakir", datetime(2004, 5, 17), "K")
ahu = Student("102", "Ahu", "Candan", datetime(2003, 6, 3), "K")
nesrin = Student("103", "Nesrin", "Cakir", datetime(2002, 2, 7), "K")
sevda = Student("104", "Sevda", "Bas", datetime(2001, 4, 1), "K")
elfi = Student("105", "Elif", "Alemdar", datetime(2000, 7, 2), "K")
zeynep = Student("106", "Zeynep", "Bas", datetime(2005, 5, 7), "K")

# Öğrencileri tek tek kaydedin
try:
    derya.saveStudent()
    ahu.saveStudent()
    nesrin.saveStudent()
    sevda.saveStudent()
    elfi.saveStudent()
    zeynep.saveStudent()
except Exception as e:
    print(e)
finally:
    connection.close()

# Ya da hepsini bir arada kaydedin
students = [derya, ahu, nesrin, sevda, elfi, zeynep]
try:
    Student.saveStudents(students)
except Exception as e:
    print(e)
finally:
    connection.close()
