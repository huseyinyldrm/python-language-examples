import pandas as pd
import sqlite3


print("-------------------------------")
df1=pd.read_csv("sample.csv")

print("csv uzantili dosyanin okunmasi:")
print("-------------------------------")
print(df1)

print("-------------------------------")

df2=pd.read_excel("sample.xlsx",engine="openpyxl")
print("excel uzantili dosyanin okunmasi:")
print("-------------------------------")
print(df2)

# excel dosyasini okumak icin gerekli olan kod blogu:pip install xlrd 

print("-------------------------------")

df3=pd.read_json("sample.json")
print(".json uzantili dosyanin okunmasi:")
print("-------------------------------")
print(df3)

print("-------------------------------")


"""

connection=sqlite3.connect("sample.db")
df4=pd.read_sql_query("SELECT * veri ismi girilecek",connection)

print(df4)

# .db uzantili dosyalari okumak icin gerekli olan kod  blogu: pip install pysqlite3


"""