import mysql.connector

def inserProduct(name,price,imageurl,productscol):
    connection=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor=connection.cursor()

    #kayit eklemek icin sql cumlecigi olusturacagiz.
    #kolon isimlerini dogru girmelisiniz.
    sql="INSERT INTO Products(name,price,imageurl,productscol) VALUES(%s,%s,%s,%s)"
    values=(name,price,imageurl,productscol)

    cursor.execute(sql,values)
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi.")
        print(f"Son eklenen kaydin id'si:{cursor.lastrowid}")

    except mysql.connector.Error as err:

        print("Hata:",err)
    finally:

        connection.close()
        print("Database baglantisi kapatildi.")


def inserProducts(list):
    connection=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
    cursor=connection.cursor()

    #kayit eklemek icin sql cumlecigi olusturacagiz.
    #kolon isimlerini dogru girmelisiniz.
    sql="INSERT INTO Products(name,price,imageurl,productscol) VALUES(%s,%s,%s,%s)"
    values=list

    cursor.executemany(sql,values) # coklu ekleme
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi.")
        print(f"Son eklenen kaydin id'si:{cursor.lastrowid}")

    except mysql.connector.Error as err:

        print("Hata:",err)
    finally:

        connection.close()
        print("Database baglantisi kapatildi.")

list=[]
while True:
    name=input("Urun Adi:")
    price=float(input("Urun Fiyati:"))
    imageurl=input("Urun resim adi:")
    productscol=input("Urun Aciklamasi:")

    list.append((name,price,imageurl,productscol))

    result=input("Devam etmek istiyor musunuz?(e/h)")
    if (result=='h'):
        print("Kayitlariniz veritabanina aktariliyor...")
        print(list)
        inserProducts(list)
        break



inserProduct(name,price,imageurl,productscol)