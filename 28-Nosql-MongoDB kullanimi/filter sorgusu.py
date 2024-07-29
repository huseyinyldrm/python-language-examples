import pymongo
from bson.objectid import ObjectId # bu da eklenmeli id icin.

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

print("Tek bir kayit filtreleme icin ".center(60,"-"))

filter={"name":"samsung s6"}
result=mycollection.find_one(filter)
print(result)

print("\n")
print("id ile kayit filtreleme".center(60,"-"))

result1=mycollection.find_one({"_id":ObjectId("668625e9b44b421176e7dd34")})

print(result1)

print("\n")
print("$in parametresi ile kayit filtreleme".center(60,"-"))

result2=mycollection.find({
    "name":{
        "$in":["samsung s6","samsung s7"]  # icinde aranan kelime varsa filtreler.
    }
})

for i in result2:
    print(i)


print("\n")
print("$gt parametresi ile kayit filtreleme".center(60,"-"))

result3=mycollection.find({
    "price":{
        "$gt":2000 # verilen fiyattan yuksek ise filtreler.
    }
})

for a in result3:
    print(a)


print("\n")
print("$gte parametresi ile kayit filtreleme".center(60,"-"))

result4=mycollection.find({
    "price":{
        "$gte":3000 # verilen fiyattan yuksek ve esit ise filtreler.
    }
})

for b in result4:
    print(b)


print("\n")
print("$eq parametresi ile kayit filtreleme".center(60,"-"))

result5=mycollection.find({
    "price":{
        "$eq":5000 # verilen fiyata esit ise filtreler.
    }
})

for c in result5:
    print(c)


print("\n")
print("$regex parametresi ile kayit filtreleme".center(60,"-"))

result6=mycollection.find({
    "name":{
        "$regex":"^s" # s ile baslayan verileri filtreler.
    }
})

for d in result6:
    print(d)