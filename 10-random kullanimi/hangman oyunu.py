import random
liste=["python","while","print","random","choice"]
kelime=random.choice(liste)
adam=['''
   +----+
   o    |
  /|\   |
  / \   |
       ---''','''
   +----+
   o    |
  /|\   |
  /     |
       ---''','''
   +----+
   o    |
  /|\   |
        |
       ---''','''
   +----+
   o    |
  /|    |
        |
       ---''','''
   +----+
   o    |
   |    |
        |
       ---''','''
   +----+
   o    |
        |
        |
       ---''','''
   +----+
        |
        |
        |
       ---''']


dogruHarf=[]
yanlisHarf=[]
hak=len(adam)

while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
            
    if out==kelime:
        break
    print("Kelime: ",out)
    print(adam[hak-1])
    girdiHarf=input()
    
    if girdiHarf == dogruHarf or girdiHarf == yanlisHarf:
        print(girdiHarf, "Zaten girildi.")
    elif girdiHarf in kelime:
        print("Doğru harf")
        dogruHarf.append(girdiHarf)
    else:
        print("Yanliş harf...")
        hak-=1
        yanlisHarf.append(girdiHarf)

if hak!=0:
    print("Tebrikler .Kazandiniz. Kelime= ",kelime)
else:
    print("Maalesef. Kaybettiniz. Kelime= ",kelime)
