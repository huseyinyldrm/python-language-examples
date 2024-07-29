myList=[1,2,3]
class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi olusturuldu.")
        
    def __str__(self):
        return f"film adi:{self.title} \nfilm yonetmeni:{self.director} \nfilm suresi:{self.duration}"
        #returnda tekrardan print yazilmaz.

    def __len__(self):
       return self.duration
    
    def __del__(self):
        print("Film objesi silindi.")

    
m=Movie("Interstaller","Hams Zemmer",3)
print('********************************')
print(str(m))
print('********************************')
print(str(myList))
print('********************************')
print(len(m))
print('********************************')
#bir objeyi silmek icin
del m
print('********************************')