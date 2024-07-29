
#*************dosyada istenilen konumda degisiklik yapma islemi**********
# with open("newfile.txt","r+",encoding='utf-8') as file:
#     file.seek(0)
#     file.write("Albeni\n")

#*******************sayfa sonuna gunceleme  islemi**********************
# bu kod da ne kadar calistirilirsa o kadar ekleme yapar.

# with open("newfile.txt","a",encoding='utf-8') as file:
#     file.write("\nDosya sonuna bilgi girme islemi.")

# with open("newfile.txt","r",encoding='utf-8') as file:
#     print(file.read())

#*******************sayfa basina guncelleme islemi*********************

# with open("newfile.txt","r+",encoding='utf-8') as file:
#         content=file.read()
#         content="Wanted\n"+content
#         file.seek(0)
#         file.write(content) # dosya basina kalici olarak eklenir.

# with open("newfile.txt","r",encoding='utf-8') as file:
#         print(file.read())

# bu kod blogu da ne kadar calistirilirsa o kadar eklem yapar.

#******************sayfa ortasinda guncelleme islemi*********************

with open("newfile.txt","r+",encoding='utf-8') as file:
    list=file.readlines()
    list.insert(1,"Petito\n") # verilen index degerinden once ekleme yapar.
    file.seek(0)
    file.writelines(list) # hepsini dosyaya yazdirma metodu

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())
