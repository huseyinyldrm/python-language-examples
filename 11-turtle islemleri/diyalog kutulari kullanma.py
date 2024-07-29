from turtle import*
N=int(numinput("poliglon","kenar sayisi"))
renk=textinput("renk","iç rengi")

pensize(5)
begin_fill()
fillcolor(renk)
circle(100,360,N)
end_fill()