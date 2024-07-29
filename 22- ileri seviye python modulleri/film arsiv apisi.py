"""
themoviedb.org => film ve dizi arsivi
themoviedb'nin sundugu apiyi uygulamanizda kullaniniz.
en populer film listesi
vizyondaki film listesi

"""
import requests

class theMovieDb:
    def __init__(self):
        self.apiUrl="https://api.themoviedb.org/3"
        self.apiKey="api anahtari alinacak siteden ve buraya kopyalanacak"

    def getPopulars(self):
        response=requests.get(f"{self.apiUrl}/movie/popular?api_key={self.apiKey}&language=en-US&page=1")

        return response.json()
    
    def getSearchResults(self,keyword):
        response=requests.get(f"{self.apiUrl}/search/keyword?api_key={self.apiKey}&query={keyword}&page=1")

        return response.json()

movieApi=theMovieDb()

while True:
    secim=input("1-Populer Movies\n2-Search Movies\n3-Exit\nSecim: ")
    if(secim=="3"):
        break
    else:
        if(secim=="1"):
            movies=movieApi.getPopulars()
            for movie in movies['results']:
                print(movie["title"])

        if(secim=="2"):
            keyword=input()
            movies=movieApi.getSearchResults(keyword)

            for movie in movies["results"]:
                print(movie["name"])
            

# bu kodun tam calisabilmesi icin self.apiKey=yerine siteden alinan keyi koymamiz gerekir.

