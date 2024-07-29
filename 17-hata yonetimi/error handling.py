while True:
    try:
        x=int(input("x: "))
        y=int(input("y: "))

        print("Sonuc: ",x/y)
    except Exception as ex:
        print("yanlis bilgi girdiniz.",ex)

    else:
        print("Her sey yolunda.")
        break
    finally:
        print("try exept sonlandi.")
        

