import mysql.connector

def getProduct():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()
    cursor.execute("SELECT *From Products Where name LIKE '%Samsung%' or price>=2000")

    result=cursor.fetchall()

    for product in result:
        print(product)

getProduct()

print("\n************************************************************\n")

def getProductById(id):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()

    sql="SELECT *From Products Where id=%s"
    params=(id,) #params degiskeninin bir demet (tuple) olarak tanimlanmasini saglamaktir.
    cursor.execute(sql,params)
    result=cursor.fetchone()
    
    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")


getProductById(1)
getProductById(3)
