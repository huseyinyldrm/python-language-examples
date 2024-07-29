#Identity Operator:is
x=y=[1,2,3]
z=[1,2,3]#adres onemlidir burada icindeki degerler degil.

print(x is y)#true
print(x is z)#false

#Membership Operator:in

a=['apple','banana']
print('banana' in a)#true


name='Taha'
print('a' in name)#true
print('r' in name)#false