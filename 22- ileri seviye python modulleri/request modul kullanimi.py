import requests
import json


# HTML kaynagi uzerindeki bilgileri kendi bilgisayarimiza cekmeyi saglar.
result=requests.get("https://jsonplaceholder.typicode.com/todos")
print(result) # respose 200 ciktisi basarili oldugunu gosterir.

print("********************************************************")

result2=json.loads(result.text)

for i in result2:

    if i["userId"]==1:
         
        print(i["title"])

print("********************************************************")
print(type(result2))