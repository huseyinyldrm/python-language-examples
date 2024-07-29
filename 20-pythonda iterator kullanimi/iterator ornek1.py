print('1.Ornek'.center(50,'-'))
liste=[1,2,3,4,5]
iterator=iter(liste) # iteratoru python kendisi yapar.

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # next ile her bir eleman teker teker ekrana bastirilir.

print('2.Ornek'.center(50,'-'))

for i in liste:
    print(i)

print('3.Ornek'.center(50,'-'))

liste2=[2,3,4,5,6,7]

iterator2=iter(liste2)

while True:
    try:
        element=next(iterator2)
        print(element)
    except StopIteration:
        break

print('4.Ornek'.center(50,'-'))

class myNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.start<=self.stop):
            x=self.start
            self.start+=1

            return x
        else:
             raise StopIteration
        

print('4.Ornek'.center(50,'-'))

list=myNumbers(10,15)
myIter=iter(list)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

print('5.Ornek'.center(50,'-'))

list=myNumbers(10,15)

for i in list:
    print(i)

print('6.Ornek'.center(50,'-'))

list=myNumbers(10,15)
myIter=iter(list)

while True:
    try:
        elemt=next(myIter)
        print(elemt)
    except StopIteration:
        break