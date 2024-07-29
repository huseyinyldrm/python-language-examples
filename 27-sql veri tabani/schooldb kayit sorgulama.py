"""
Asagidaki sorulari yanitlayiniz:
1-Tum ogrencilerin kayitlarini aliniz.
2-Tum ogrencilerin sadece ogrenci no,ad ve soyad bilgilerini aliniz.
3-Sadece kiz ogrencilerin ad ve soyadlarini aliniz.
4-2003 dogumlu ogrenci bilgilerini aliniz.
5-ismi Ali ve dogum tarihi 2005 olan ogrenci bilgilerini aliniz.
6-Ad veya soyadi icinde 'an' ifadesi gecen kayitlari bulunuz.
7-Kac erkek ogrenci vardir.
8-Kiz ogrencileri harf sirasina gore getiriniz.
9-Kac kiz ogrenci vardir.

"""

import mysql.connector
from datetime import datetime
from connection import connection

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="schooldb"
)

print("1.Soru Cevabi".center(50,"*"))

cursor=connection.cursor()
cursor.execute("SELECT *From student")
result=cursor.fetchall()
for a in result:
    print(a)

print("2.Soru Cevabi".center(50,"*"))

cursor1=connection.cursor()
cursor1.execute("SELECT StudentNumber,Name,Surname From student")
result1=cursor1.fetchall()
for b in result1:
    print(b)

print("3.Soru Cevabi".center(50,"*"))

cursor2=connection.cursor()
cursor2.execute("SELECT Name,Surname From student Where Gender='K'")
result2=cursor2.fetchall()
for c in result2:
    print(c)


print("4.Soru Cevabi".center(50,"*"))

cursor3=connection.cursor()
cursor3.execute("SELECT *From student Where YEAR(Birthdate)=2003")
result3=cursor3.fetchall()
for d in result3:
    print(d)

print("5.Soru Cevabi".center(50,"*"))

cursor4=connection.cursor()
cursor4.execute("SELECT *From student Where Name='Ali' AND YEAR(Birthdate)=2000")
result4=cursor4.fetchall()
for e in result4:
    print(e)


print("6.Soru Cevabi".center(50,"*"))

cursor5=connection.cursor()
cursor5.execute("SELECT *From student WHERE Name LIKE'%an%' OR Surname LIKE '%an%'")
result5=cursor5.fetchall()
for f in result5:
    print(f)


print("7.Soru Cevabi".center(50,"*"))

cursor6=connection.cursor()
cursor6.execute("SELECT COUNT(*) From student WHERE Gender='E'")
result6=cursor6.fetchall()
for g in result6:
    print("Toplam erkek sayisi:",g)


print("8.Soru Cevabi".center(50,"*"))

cursor7=connection.cursor()
cursor7.execute("SELECT Name,Surname From student WHERE Gender='K' ORDER BY Name,Surname")
result7=cursor7.fetchall()
print("Kiz ogrencilerin alfabetik siraya gore siralanisi:")
for h in result7:
    print(h)

print("9.Soru Cevabi".center(50,"*"))

cursor8=connection.cursor()
cursor8.execute("SELECT COUNT(*) From student WHERE Gender='K'")
result8=cursor8.fetchall()
for g in result8:
    print("Toplam kiz sayisi:",g)