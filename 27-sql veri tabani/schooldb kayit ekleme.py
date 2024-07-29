#1- Workbench IDE ile schooldb isminde bir database olusturup Student tablosu ekleyiniz.
# Id,StudentNumber,Name,Surname,Birthdate,Gender

#2- Database baglantisini olusturunuz.

#3-Asagidaki bilgiler icin insert sorgulari olusturup kayitlari ekleyiniz.

#("101","Polat","Alemdar",datetime(2003,5,17),"E")
#("102","Ali","Candan",datetime(2000,6,3),"E")
#("103","Yusuf","Karahanli",datetime(2001,2,7),"E")
#("104","Memati","Bas",datetime(2002,4,6),"E")
#("105","Halo","Dayi",datetime(2001,7,8),"E")
#("106","Zaza","Dayi",datetime(2000,5,5),"E")


import mysql.connector
from datetime import datetime


connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="schooldb"
)

mycursor=connection.cursor()

sql="INSERT INTO Student(StudentNumber,Name ,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"

ogrenciler=[
    ("101","Polat","Alemdar",datetime(2003,5,17),"E"),
    ("102","Ali","Candan",datetime(2000,6,3),"E"),
    ("103","Yusuf","Karahanli",datetime(2001,2,7),"E"),
    ("104","Memati","Bas",datetime(2002,4,6),"E"),
    ("105","Halo","Dayi",datetime(2001,7,8),"E"),
    ("106","Zaza","Dayi",datetime(2000,5,5),"E")
]

mycursor.executemany(sql,ogrenciler)

try:
    connection.commit()
    print(f"{mycursor.rowcount} tane kayit eklendi.")

except mysql.connector.Error as err:
    print("Hata:",err)
finally:
    connection.close()