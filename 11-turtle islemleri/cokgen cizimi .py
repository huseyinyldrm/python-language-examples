from turtle import*
N=int(input("Köşe sayisi giriniz:"))
aci=360/N
pensize(3)

for i in range(N):
    forward(200)
    left(aci)