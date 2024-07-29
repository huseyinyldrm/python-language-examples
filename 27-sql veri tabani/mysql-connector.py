import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255 ))")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE DATABASE mydatabase")
#print("Database created successfully.")

# for i in mycursor:
#     print(i)