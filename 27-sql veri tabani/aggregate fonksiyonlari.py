#count() , avg() , max() , min() , sum() fonksiyonlari vardir.
import mysql.connector

def getProductById():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()
    #sql="SELECT COUNT(*) From Products"
    #sql="SELECT AVG(Price) From Products"
    #sql="SELECT SUM(Price) From Products"
    sql="SELECT Name,Price From Products Where Price =(SELECT MIN(Price) From Products)"
    cursor.execute(sql)


    result=cursor.fetchall()

    print(f"result={result[0]}")

getProductById()