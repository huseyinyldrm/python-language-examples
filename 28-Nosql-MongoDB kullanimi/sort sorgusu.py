import pymongo
from bson.objectid import ObjectId # bu da eklenmeli id icin.

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

result=mycollection.find().sort("name",1) # varsayilan azalandan artana olacak sekilde siralar 1 yazmasak da olur.
for i in result:
    print(i)

print("\n")

result1=mycollection.find().sort("name",-1) # azalana dogru siralama yapar.
for a in result1:
    print(a)

print("\n")

result2=mycollection.find().sort("price",1) # varsayilan azalandan artana olacak sekilde siralar 1 yazmasak da olur.
for b in result2:
    print(b)


print("\n")

result3=mycollection.find().sort("price",-1) # azalana dogru siralama yapar.
for c in result3:
    print(c)


print("\n")

result4=mycollection.find().sort([("name",1),("price",-1)]) # azalana dogru siralama yapar.
for d in result4:
    print(d)

