
gun=input("Turkce gun adi: ")
TrEn={'pazartesi':'monday','sali':'tuesday','carsamba':'wednesday','persembe':'thruesday','cuma':'friday','cumartesi':'saturday','pazar':'sunday'}
print("ingilizcesi:",end=' ')
print(TrEn.get(gun,"Bu kelime sozlukte yoktur."))