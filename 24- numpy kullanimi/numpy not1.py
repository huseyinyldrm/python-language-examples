import numpy as np

# python list
pyList=[1,2,3,4,5,6,7,8,9]

# numpy list

npArray=np.array([1,2,3,4,5,6,7,8,9])
print(type(pyList))
print(type(npArray))

pyMulti=[[1,2,3],[4,5,6],[7,8,9]]
npMulti=npArray.reshape(3,3) # cift boyutlu dizi olusturmaya yarar.

print(pyMulti)
print("\n")
print(npMulti)

print("\n********************************")
print(npArray.ndim) # dizinin kac boyutlu oldugu bilgisini yazdirir.
print(npMulti.ndim)

print("********************************")
print(npArray.shape) # dizilerin boyut bilgisini yazdirir.
print(npMulti.shape)

