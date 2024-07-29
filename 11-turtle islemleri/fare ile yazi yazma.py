from turtle import*
pensize(3)
win=Screen()
win.setup(200,200)#çerçeve oluşturur
penup()
def nokta (x,y):
    goto(x,y)
    pendown()

win.onclick(nokta)#tıklanma olduğunda nokta fonksiyonunu çalıştır
mainloop()
