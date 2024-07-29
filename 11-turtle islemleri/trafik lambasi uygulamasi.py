from turtle import*
import time #bu modül zamanla ilgili çeşitli işlevler sağlar
w=Screen()
w.setup(300,700)
w.title("Trafik Işık Uygulaması")

penup()#kalemi kaldırır
goto(0,180)
pendown()
pensize(4)

for i in range(2):
    forward(80)#ileri gider
    right(90)#90 derece döner
    forward(220)#ileri gider
    right(90)#90 derece döner

def kirmizi():#9 saniye
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)
    
def sari():#3 saniye
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def yesil():#9 saniye
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

sayac=0
while sayac<1:
  yesil()
  time.sleep(3)# başka bir işlem yapmamıza izin vermiyor

  sari()
  time.sleep(3)

  kirmizi()
  time.sleep(3)
  
  sayac+=1
    
w.mainloop()
