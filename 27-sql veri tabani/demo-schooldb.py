#1- Workbench IDE ile schooldb isminde bir database olusturup Student tablosu ekleyiniz.
# Id,StudentNumber,Name,Surname,Birthdate,Gender

#2- Database baglantisini olusturunuz.

import mysql.connector

# Önce veritabanını oluşturun

# Daha sonra veritabanına bağlanın ve tabloyu oluşturun
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="schooldb"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    StudentNumber VARCHAR(255),
    Name VARCHAR(255),
    Surname VARCHAR(255),
    Birthdate DATE,
    Gender VARCHAR(10)
)
""")
print("Table created successfully.")

#mycursor.execute("CREATE DATABASE mydatabase") # bir kere olusturuldugu icin yorum satiri ekledim.

mycursor.execute("Show Databases")

for i in mycursor:
    print(i) 

