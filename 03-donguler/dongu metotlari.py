# range kullanimi:

for item in range(50,100,10):# 50-100 arasi 10 artarak git demek.
    print(item)

print(list(range(50,100,10)))# bu kodda ustteki gibi calisir ama degerleri liste icine atar.

#enumerate kullanimi:

greeting='Hello There'
index=0

for letter in greeting:
    print(f"index:{index} letter:{greeting[index]}")
    index+=1

print("--------------------------------------")
print("Enumerate kullanimi:")
for index,item in enumerate(greeting):
    print(f"index:{index} letter:{item}")


print("--------------------------------------")

# zip metodu:

liste1=[1,2,3,4,5]
liste2=['a','b','c','d','e']
liste3=[100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))

print("--------------------------------------")
# zip metodunda for kullanilirsa:
for item in zip(liste1,liste2,liste3):
    print(item)

print("--------------------------------------")

for a,b,c in zip(liste1,liste2,liste3):
    print(a)
    print(b)
    print(c)
    print("--------------------------------------")

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c)#listeden cikarip yan yana yazdirir.
    


