import mysql.connector

def getProducts():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()

    cursor.execute("SELECT *From Products Order By name,price DESC") # varsayilan olarak artan sekilde ilerler.Tersi icin DESC yazilir.
    try:
        result=cursor.fetchall()
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Baglanti kapatildi.")
    for products in result:
        print(f"id={products[0]} name={products[1]} price={products[2]}")


getProducts()