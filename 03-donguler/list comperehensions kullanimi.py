nubers=[]
for x in range(10):
    nubers.append(x)
print(nubers)

print("-------------------------")

number=[x for x in range(10)]
print(number)

print("-------------------------")

for x in range(6):
    print(x**2)

print("-------------------------")

sayilar=[x**2 for x in range(6)]
print(sayilar)

print("-------------------------")

nuberlar=[x*x for x in range(10) if(x%3==0)]
print(nuberlar)

print("-------------------------")

myString='Hello'
myList=[]

for letter in myString:
    myList.append(letter)

print(myList)

print("-------------------------")

myList=[letter for letter in myString]
print(myList)

print("-------------------------")

years=[1983,1999,2006,2005,2000]
ages=[2024-year for year in years]
print(ages)

print("-------------------------")

results=[x if(x%2==0) else 'TEK' for x in range(1,11)]
print(results)

print("-------------------------")

result=[]

for x in range(3):
    for y in range(3):
        result.append((x,y))# burada 2 parantez olmalidir dikkat...
print(result)

print("-------------------------")

sonuclar=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(sonuclar)

