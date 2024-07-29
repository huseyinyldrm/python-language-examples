import mysql.connector

def getProducts():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )

    cursor=connection.cursor()
    cursor.execute("SELECT * From Products")
#sadece istenilen kolonlari getirmek icin:
    #cursor.execute("SELECT name,price From Products")

    result=cursor.fetchall() #fetchall yerine fetchone() dersek ilk kayit gelir. 
    
    for product in result:
        print(product)




def getStudents():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="schooldb"
    )

    cursor=connection.cursor()
    cursor.execute("SELECT *From student")

    result=cursor.fetchall()

    for students in result:
        print(students)



getProducts()
print("\n**************************************************************\n")
getStudents()