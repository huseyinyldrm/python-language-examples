import mysql.connector

def getProducts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    
    cursor = connection.cursor()
    #sql="SELECT *From Categories"
    #sql="SELECT *From Products"
    
    #sql = "SELECT Products.*, Categories.* FROM Products INNER JOIN Categories ON Categories.id = Products.categoryid"
    
    #sql="SELECT Products.name,Products.price,Categories.name From Products INNER JOIN Categories ON Categories.id=Products.categoryid"

    #sql="SELECT Products.name,Products.price,Categories.name From Products INNER JOIN Categories ON Categories.id=Products.categoryid WHERE Categories.name='telefon'"

    #sql="SELECT Products.name,Products.price,Categories.name From Products INNER JOIN Categories ON Categories.id=Products.categoryid WHERE Products.name='samsung s7'"

    sql="SELECT p.name,p.price,c.name From Products as p INNER JOIN Categories as c ON c.id=p.categoryid WHERE p.name='samsung s6'"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    
    except mysql.connector.Error as err:
        print("Hata:", err)
    finally:
        connection.close()
        print("Database baglantisi kapatildi.")

getProducts()
