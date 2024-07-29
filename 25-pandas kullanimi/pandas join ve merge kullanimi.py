import pandas as pd

customers={

    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]
}

orders={
    "OrdersId":[10,11,12,13],
    "CustomerId":[1,2,5,7],
    "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-05-03"]
}

dfCustomers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
print(dfCustomers)

print("***************************************************")

dforders=pd.DataFrame(orders,columns=["OrdersId","CustomerId","OrderDate"])
print(dforders)

print("***************************************************")

result=pd.merge(dfCustomers,dforders,how="inner")
print(result)

print("***************************************************")

result=pd.merge(dfCustomers,dforders,how="cross")
print(result)

print("***************************************************")

result=pd.merge(dfCustomers,dforders,how="left")
print(result)

print("***************************************************")
print("Sag ve sol butun isimlerin gelmesi islemi:")
result=pd.merge(dfCustomers,dforders,how="outer")
print(result)

print("***************************************************")

result=pd.merge(dfCustomers,dforders,how="right")
print(result)

print("***************************************************")

customersA={

    "CustomerId":[5,2,4,7],
    "FirstName":["Betul","Ali","Harun","Furkan"],
    "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]
}

customersB={

    "CustomerId":[1,4,5,3],
    "FirstName":["Mehmet","Ceren","Hamza","Can"],
    "LastName":["Yilmaz","Korkmaz","Celik","Toprak"]
}

dfCustomersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])

print(dfCustomersA)

print("***************************************************")

dfCustomersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

print(customersB)

print("***************************************************")
print("iki dataframeyi birlestirme islemi:")

result1=pd.concat([dfCustomersA,dfCustomersB])
print(result1)

print("***************************************************")

print("Kolona gore islem yapilirsa:")
result2=pd.concat([dfCustomersA,dfCustomersB],axis=1)
print(result2)
