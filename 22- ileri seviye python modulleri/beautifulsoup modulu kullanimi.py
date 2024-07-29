# bir html icerigini istedigimiz sekilde analiz etmemizi saglar.

htmlDoc="""




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>
<h1>Python Kursu</h1>

    <div class="grup1">
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>


    <h1>Yazilim Dilleri</h1>

    <div class="grup2">
        <ul>
            <li>Python</li>
            <li>Java</li>
            <li>Javascript</li>
    </ul>
    </div>

    <img src="" alt="">
    <a class="sister" href="https://www.example1.com">Click here to visit Example.com</a>
    <a class="sister" href="https://www.example2.com">Click here to visit Example.com</a>
    <a class="sister" href="https://www.example3.com">Click here to visit Example.com</a>
   
</body>
</html>

"""
from bs4 import BeautifulSoup

soup=BeautifulSoup(htmlDoc,"html.parser")
result=soup.prettify() # bozuk olan html dokumanini duzeltir.
print(result)

print("*********************************************************")

result2=soup.title # title etiketlerini verir.
print(result2)

print("*********************************************************")

result3=soup.body # body etiketini verir.
print(result3)

print("*********************************************************")

result4=soup.title.name
print(result4)

print("*********************************************************")

result5=soup.title.string
print(result5)

print("*********************************************************")

result6=soup.h1
print(result6)

print("*********************************************************")

result7=soup.h1.name
print(result7)

print("*********************************************************")

result8=soup.h1.string
print(result8)

print("*********************************************************")

result9=soup.find_all('h1')
result9a=soup.find_all('h1')[0]
result9b=soup.find_all('h1')[1]
print(result9)
print(result9a)
print(result9b)

print("*********************************************************")

result10=soup.div # sadece ilk div'i getirir.
print(result10)

print("*********************************************************")

result11=soup.find_all('div')[1] # 2. div etiketini verir.
print(result11)

print("*********************************************************\n")

result11a=soup.find_all('div')[1].ul.find_all('li')
print("1.gosterim:".center(25,'-'))
for i in result11a:
    print(i)

print("2.gosterim:".center(25,'-'))
print(result11a)

print("\n")

print("*********************************************************")

sonuc=soup.findChildren()
print(sonuc)

print("*********************************************************")

sonuc2=soup.div.find_next_sibling().findNextSibling() # div'in 2. cocugunu verir.
print(sonuc2)

print("*********************************************************")

sonuc3=soup.div.findNextSibling().findNextSibling().findPreviousSibling() # div 'in ilk ebeveyini verir.
print(sonuc3)

print("*********************************************************\n")

print("1.gosterim:".center(25,'-'))
sonuc4=soup.find_all('a')
print(sonuc4)

print("\n")

print("2.gosterim:".center(25,'-'))
for link in sonuc4:
    print(link)

print("\n*********************************************************\n")
print("Sadece linkleri getirmek icin:\n")

sonuc5=soup.find_all("a")

for i in sonuc5:
    print(i.get('href'))

print("\n*********************************************************")