kelime=input("Kelime giriniz:")
print(kelime," tersi:",kelime[::-1]," seklindedir.")

if kelime==kelime[::-1]:
    print(kelime," bir polindromdur.")

else:
    print(kelime," bir polidrom degildir.")