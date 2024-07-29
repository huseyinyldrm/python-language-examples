def square(a):
    return a**2

list1=[2,3,4,6,7,9]
squareList=list(map(square,list1))
print(list1)

print("--------------")

print(squareList)

print('----------------------------')

def even (n):
    return n%2==0
L1=[1,2,3,4,5,6,7,8,9,10]
evenL1=list(filter(even,L1))
print(L1)

print("--------------")

print(evenL1)

print('----------------------------')

def tek(c):
    return c%2==1

L2=[11,22,3,4,6,7,5,9,89,21,23,33]

newL2=list(filter(tek,L2))
print(L2)

print("--------------")

print(newL2)
print('----------------------------')