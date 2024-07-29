import json # bu json string ifadeyi dictionary'e cevirir.

# dictionary

personString='{"name":"Ali","languages":["Python","C#"]}'

# donusturme islemi:

donusum=json.loads(personString)
print(type(donusum))
print(donusum)

print("--------------------------------")
donusum1=donusum["name"]
print(donusum1)

print("--------------------------------")
donusum2=donusum["languages"]
print(donusum2)

print("--------------------------------\n")

print("json uzantili dosyadan verileri okuma islemi:".center(80,"*"))

print("--------------------------------\n")

with open("person.json") as file:
    data=json.load(file)
    print(data["name"])
    print(data["languages"][0])
    print(data["languages"][1])

    
print("\n")
print("Dict veri turunu json' a cevirme:".center(50,"*"))

personDict={
    "name":"Ahmet",
    "languages":["java","C++"]
}
result=json.dumps(personDict)
print(type(result))

with open("person.json","w") as file:
    json.dump(personDict,file)

print("Yapilan islemler json dosyasina kaydedildi.")

print("--------------------------------\n")

personDict=json.loads(personString)
print(personDict)

sonuc=json.dumps(personDict,indent=4,sort_keys=True)# istedigimiz sekilde konsola yazdirmak icin bu tarz kullanilir.

print(sonuc)