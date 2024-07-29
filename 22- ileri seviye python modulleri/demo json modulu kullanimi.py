import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = None  # Bos sozluk degil, None olmalı
        
        # Kullanicilari .json dosyasindan yukle
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("user.json"):
            try:
                with open("user.json", "r", encoding="utf-8") as file:
                    users = json.load(file)  # Degisken adi users olarak duzeltildi

                    for userData in users:
                        userDict = json.loads(userData)  # Degisken adi userData olarak duzeltildi
                        newUser = User(username=userDict["username"], password=userDict["password"], email=userDict["email"])
                        self.users.append(newUser)
                        print("\n")
                
                print("Kullanicilar yuklendi:", self.users)
            except json.JSONDecodeError:
                print("***********************************************************************************")
                print(" user.json dosyasi bos veya gecersiz JSON formatinda.\n Yeni bir kullanici olusturana kadar bos bir kullanici listesi ile devam edilecek.")
                print("***********************************************************************************\n")
        else:
            print("user.json dosyasi bulunamadi. Yeni bir dosya olusturulacak.")

    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanici olusturuldu...")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Giris yapildi.")
                break
        else:
            print("Kullanici adi veya sifre yanlis.")

    def logout(self):
        if self.isLoggedIn:
            self.isLoggedIn = False
            self.currentUser = None
            print("Cikis yapildi.")
        else:
            print("Zaten giris yapilmamis.")

    def identity(self):
        if self.isLoggedIn:
            print(f"Giris yapan kullanici: {self.currentUser.username}")
        else:
            print("Giris yapilmamis.")

    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))  # Kullanıcı nesnesini sozluge ve sonra JSON stringe donustur
        with open("user.json", "w", encoding="utf-8") as file:  # Tutarlilik icin encoding eklendi
            json.dump(list, file)

repository = UserRepository()

while True:
    print("Menu".center(50, "*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz:")

    if secim == '5':
        print("Sistemden cikis yapiliyor...")
        break
    else:
        if secim == '1':
            username = input("Username:")
            password = input("Password:")
            email = input("Email:")

            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == '2':
            if repository.isLoggedIn:
                print("Zaten giris yapmissiniz.")
            else:
                username = input("Username:")
                password = input("Password:")
                repository.login(username, password)

        elif secim == '3':
            repository.logout()

        elif secim == '4':
            repository.identity()
        else:
            print("Yanlis secim...")
