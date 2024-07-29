import pymongo
from bson.objectid import ObjectId # bu da eklenmeli id icin.

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

for i in mycollection.find({},{"_id":0}):
    print(i)

print("\n")
mycollection.update_many(
    {"name":"samsung s6"},
    {"$set":{
        "name":"iphone 13 pro max",
        "price":10000
    
    }}
)

print("\n")
for j in mycollection.find({},{"_id":0}):
    print(j)