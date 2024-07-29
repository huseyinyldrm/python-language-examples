from turtle import*
colormode(255)
color(0,0,0)
pensize(5)

def ucgen ():
    for x in range(3):
        forward(200)
        left(120)
    
def kare():
    for x in range(4):
        forward(200)
        right(90)

begin_fill()
fillcolor(0,220,220)
ucgen()
end_fill()

begin_fill()
fillcolor(0,200,200)
kare()
end_fill()