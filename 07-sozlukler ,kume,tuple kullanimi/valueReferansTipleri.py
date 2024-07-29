#value types:string ve number tipler buna dahil olur.
x=5
y=25

x=y

y=10

print(x,y)#cikti:25,10 olur

print('-'*50)

#referance types:liste,class

a=["apple","banana"]
b=["apple","banana"]

a=b

b[0]="grape"
print(a,b)
#ozetle vakue typelerle ugrasirken verinin kendisiyle , referance typeler ile ugrasirken listenin adresiyle ugrasiriz.