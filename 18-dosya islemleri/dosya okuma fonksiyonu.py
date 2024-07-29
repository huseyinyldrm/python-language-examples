with open("newfile.txt","r",encoding='utf-8') as file:
    content=file.read()
    print(content)
    file.seek(0) # kursoru 0 a getirdik.
    print(file.tell())
   
# bu kod blogunu yazdiktan sonra close() fonksiyonuna gerek yoktur.