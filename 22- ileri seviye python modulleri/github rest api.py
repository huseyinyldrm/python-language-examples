import requests

class Github:
    def __init__(self):
        self.apiUrl="https://api.github.com" # bu adresi duzgun yaz.
        self.token="2a0cebe35888589a756953098fb345a5c26fc79b"
    
    def getUser(self,username):
        response=requests.get(self.apiUrl+"/users/"+username)
        return response.json()
    
    def getRepositories(self,username):
        response=requests.get(self.apiUrl+"/users/" +username+"/repos/")
        return response.json()
    
    def createRepositories(self,name):
        response=requests.post(self.apiUrl+"/user/repos?access_token="+self.token,json={
            "name":name,
            "description":"This is your first repository",
            "homepage":"https://sadikturan.com",
            "private":False,
            "has_issuses":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json()

github=Github()


while True:
    secim=input("1-Find User\n2-Get Repostories\n3-Create Repository\n4-Exit\nSeciminiz: ")

    if(secim=="4"):
        break

    else:
        if(secim=="1"):
            username=input("User name:")
            result= github.getUser(username)
            print(f"name :{result["name"]} public repos:{result["public_repos"]} follower: {result["followers"]}")

        elif(secim=="2"):
            username=input("Username: ")
            result=github.getRepositories(username)
            if isinstance(result,list):
                for repo in result:
                    print(repo["name"])
            else:
                print("Depolar alinirken bir hata olustu veya hic depo bulunamadi.")

        elif(secim=="3"):
            name=input("Repository name: ")
            result=github.createRepositories(name)
            print(result)
        else:
            print("Yanlis secim...")