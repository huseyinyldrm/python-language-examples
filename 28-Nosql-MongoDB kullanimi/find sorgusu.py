import pymongo
from bson.objectid import ObjectId # bu da eklenmeli id icin.

#myclient=pymongo.MongoClient("Buraya database baglantisi yapistirilir.")


myclient=pymongo.MongoClient("mongodb://localhost:27017") # mongodb compas uzerinde baglanti olusturur.

mydb=myclient["node-app"]
mycollection=mydb["products"]

for i in mycollection.find({},{"_id":0,"name":1,"price":1}):
    print(i)

# id'yi listede görmek istemedigimiz icin 0 yazdik. name ve priiceyi listede gormek icin 1 yazdik.
# tek bir veriyi listelemek istiyorsak mycollection.find_one() yazariz.
#find() icindeki parametrelerde ilk parametre mysql deki WHERE gibi durumlara karsilik gelir.