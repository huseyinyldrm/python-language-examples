import pymongo

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

productList=[
    {"name":"samsung s6","price":1000},
    {"name":"samsung s7","price":2000},
    {"name":"samsung s8","price":3000},
    {"name":"samsung s9","price":4000},
    {"name":"samsung s10","price":5000},
    {"name":"samsung s11","price":6000}
]
result=mycollection.insert_many(productList)
print(result)