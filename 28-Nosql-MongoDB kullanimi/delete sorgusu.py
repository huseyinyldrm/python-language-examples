import pymongo
from bson.objectid import ObjectId # bu da eklenmeli id icin.

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

for i in mycollection.find():
    print(i)

print("*"*50)

# mycollection.delete_many({"name":{
#     "$in":["samsung s7","samsung s8","samsung s9","samsung s10","samsung s11"]}
    
#})
mycollection.delete_many({}) # bu calisirsa hepsi silinir.

print("*"*50)

for i in mycollection.find():
    print(i)