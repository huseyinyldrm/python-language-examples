from turtle import*
shape("turtle")
pensize(4)
w=Screen()
w.setup(500,500)

def solaDon():
    left(90)
    write("sola döndüm")
def sagaDon():
    right(90)
    write("sağa döndüm")
    
def ileri():
    forward(10)
    
def geri():
    backward(10)

w.onkeypress(solaDon,"Left")
w.onkeypress(sagaDon,"Right")
w.onkeypress(ileri,"Up")
w.onkeypress(geri,"Down")

w.listen()#bu kodu koymazsak klavyeyi dinlemez
w.mainloop()#olay yakalama döngüsünü başlatır
