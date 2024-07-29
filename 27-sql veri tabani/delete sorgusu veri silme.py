import mysql.connector

def getProduct():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()
    cursor.execute("SELECT *From Products")

    result=cursor.fetchall()

    for i in result:
        print(i)


def deleteProduct(id):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()

    sql="delete from products where id=%s"
    # eger sadece delete from products yazilirsa tum veriler silinir.
    values=(id,)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit silindi.")
    except mysql.connector.Error as err:
        print("Hata:",err)
    finally:
        connection.close()
        print("Database baglantisi kapatildi.")

getProduct()
print("\n---------------------------------------------------------\n")
deleteProduct(7)
print("\n---------------------------------------------------------\n")
getProduct()


