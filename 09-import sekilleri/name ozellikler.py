# __name__ == '__main__'  import edilen modülün ana programda olup olmadığını kontrol eder. Eğer ana programdaysa true değile false döndürür.
print("Python")
print("Hello world")

if(__name__=='__main__'):
    print("Ana program")

else:
    print("Bu modul ana program disinda import edildi.")