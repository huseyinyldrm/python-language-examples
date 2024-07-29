L=[]
while True:
    TC=int(input("TC numaranizi giriniz : "))
    if TC in L:
        i=L.index(TC)
        print("Muayene Sirasi = ",i+1)
    elif TC==0:
        print(L[0], " TC numarali hasta doktorun yanina gidiniz:")
        L.pop(0)
    elif TC==1:
        print("Mesai bitmistir.")
        break
    
    else:
        L.append(TC)
        print(TC, " TC numarali hasta siraya alindi. ")
        
        
