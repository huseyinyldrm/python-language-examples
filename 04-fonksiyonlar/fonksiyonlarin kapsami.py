#global scope
x='global x'

def function():
    #local scope
    x='local x' # buradaki degiskenler sadece bu fonk. kapsar.
    print(x)

function()
print(x)

print('************************************************')

name='Taha'

def changeName(newName):
    name=newName
    print(name)

changeName('Ada')
print(name)

print('************************************************')

x=50

def test():
    global x # ustte tanimlanan global  deger uzerinde degisiklik yapmaya olanak saglar.
    print(f"x : {x}")

    x=100
    print(f"changed x to:{x}")

test()
print(x)