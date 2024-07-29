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


def updateProdukt(name,price,id):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()
    sql="Update products Set name=%s ,price=%s where id=%s"
    values=(name,price,id)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane guncellendi.")
    except mysql.connector.Error as err:
        print("Hata:",err)
    finally:
        connection.close()
        print("Baglanti kapatildi.")


getProduct()
print("\n---------------------------------------------------------\n")
updateProdukt("Samsung S23",6000,3)
print("\n---------------------------------------------------------\n")
getProduct()
