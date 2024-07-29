from turtle import*
pensize(5)
shape("blank")
fillcolor("black")
begin_fill()
for x in range(2):
    forward(100)
    right(90)
    forward(250)
    right(90)
end_fill()
    
pencolor("red")
penup()# çizim yapmadan istenilen konuma götürür kalemi.
goto(50,-80)
pendown()
fillcolor("red")
begin_fill()
circle(30)# burası 3 parametre alır ilk parametre yarıçaptır.Saat yönünün tersine çizer.
end_fill()

pencolor("yellow")
penup()# çizim yapmadan istenilen konuma götürür kalemi.
goto(50,-150)
pendown()
fillcolor("yellow")
begin_fill()
circle(30)# burası 3 parametre alır ilk parametre yarıçaptır.Saat yönünün tersine çizer.
end_fill()

pencolor("green")
penup()# çizim yapmadan istenilen konuma götürür kalemi.
goto(50,-220)
pendown()
fillcolor("green")
begin_fill()
circle(30)# burası 3 parametre alır ilk parametre yarıçaptır.Saat yönünün tersine çizer.
end_fill()



