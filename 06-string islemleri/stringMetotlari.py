website="https://www.sadikturan.com"
course="Python Kursu: Bastan Sona Python Programlama Rehberiniz(40 Saat)"

#1-' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result1=' Hello World '.strip()
print(result1)

result2=' Hello World'.lstrip()# soldaki boşlogu siler
print(result2)

result3=' Hello World '.rstrip()# sagdaki boslugu siler
print(result3)

#2-'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result4='www.sadikturan.com'.strip('w.com')
print(result4)
#3-'course' karakter dizisinin tüm karakterlerini buyultun.
result5=course.upper()
print(result5)

#4-"website" içinde kaç tane a karakteri vardır?(count('a'))
print(website.count('a'))
print(website.count('www'))
print(website.count('a',0,10))# 1-10 arası a var mı

#5-"website" 'www' ile baslayıp com ile bitiyor mu?
print(website.endswith('com'))
print(website.startswith('www'))

#6-"website" içinde '.com' ifadesi var mı?
print(len(website))
print(website.find('.com'))
print(website.find('com',0,10))#-1 =false ,1= true


#7-'course' içindeki tüm karakterler alfabetik mi?(isalpha,isdigit)
rs=course.isalpha()# parantezleri unutma.!!!
print(rs)

rs2=course.isalnum()
print(rs2)
#8-"Contents" ifadesini 50 karakter içine koy ve sağ ve soluna *ekle.

kelime1='Contents'.center(50,'*')
print(kelime1)

kelime2='Contents'.ljust(50,'*')
print(kelime2)

kelime3='Contents'.rjust(50,'*')
print(kelime3)

#9-'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştir.
print(course.replace(' ','-'))
print(course.replace(' ','*',5))


#10-"Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştir.
print('Hello World'.replace('World','There'))

#11-"course" karakter dizisini boşluk karakterlerinden ayırın.
print(course.split(' '))
