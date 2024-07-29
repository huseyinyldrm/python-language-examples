print('1. Ornek'.center(50,"-"))
myStr="dubai"
x=0

for i in myStr:
    x+=1
    print(myStr[0:x]) 
for i in myStr:
    x-=1
    print(myStr[0:x])

print('2. Ornek'.center(50,"-"))

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    
    print() # alt satira gecmeye yarar


print('3. Ornek'.center(50,"-"))

for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()