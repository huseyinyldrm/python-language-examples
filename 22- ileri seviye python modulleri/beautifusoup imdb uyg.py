import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,asc"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    # bunu network kismindan aybisini kopyala yapistir. 
}
html=requests.get(url,headers=headers).content
soup=BeautifulSoup(html,"html.parser")

liste=soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=10) # 25 e kadar alabilirsin.limit degisir.

for item in liste:
    filmAdi=item.find("h3",{"class":"ipc-title__text"}).text
    puan=item.find("span",{"class":"ipc-rating-star"}).text
    print(filmAdi,puan)

