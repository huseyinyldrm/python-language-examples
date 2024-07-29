import mysql.connector

def inserProduct():
    connection=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor=connection.cursor()

    #kayit eklemek icin sql cumlecigi olusturacagiz.
    #kolon isimlerini dogru girmelisiniz.
    sql="INSERT INTO Products(name,price,imageurl,productscol) VALUES(%s,%s,%s,%s)"
    values=("Samsung S8",1000,"1.jpg","iyi telefon")

    cursor.execute(sql,values)
    
    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("Hata:",err)
    finally:
        connection.close()
        print("Database baglantisi kapatildi.")



inserProduct()