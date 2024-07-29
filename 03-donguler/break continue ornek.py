name='Huseyin'

for letter in name:
    if(letter=='i'):
          break
    print(letter) # donguyu kirar ve sonlandirir.

print('--------------------------------')

names='Yildirim'
for i in names:
    if(i=='l'):
         continue # donguyu atlar ve bitirir.
    print(i)

print('--------------------------------')

x=0
while (x<5):
    x+=1
    if(x==2):
        continue
    print(x)
   

print('--------------------------------')

# 1-100 arasi tek sayilerin toplami:

a=0
result=0
while (a<=100):
    a+=1
    if(a%2==0):
        continue
    result+=a
print(f"Tek sayilarin toplami:{result}")