import sqlite3

connection=sqlite3.connect("dosyaAdi.db")

cursor=connection.cursor()
cursor.execute("SELECT *From istenilen kolon adi")

result=cursor.fetchall()

for i in result:
    print(i)

connection.close()