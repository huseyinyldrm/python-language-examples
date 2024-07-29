import turtle
import time
import random # yem için rastgele seçim yapar
#import playsound # müzik eklemeye yarar yükleyince açılmalıdır

liste = []
skor = 0
maxSkor = 0

# Çerçeve ayarları yapıldı
w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600, 600)
w.bgcolor("green")
w.tracer(0)

# Yılan nesnesinin kafası oluşturuldu
yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("black")
yn.penup()
yn.goto(0, 0)
yn.yon = "dur"

# Yem nesnesi
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0, 100)

def hareket():
    if yn.yon == "ust":
        y = yn.ycor()    # y ekseninde yukarı gider
        yn.sety(y + 20)

    if yn.yon == "alt":
        y = yn.ycor()    # y ekseninde aşağı gider
        yn.sety(y - 20)

    if yn.yon == "sag":
        x = yn.xcor()    # x ekseninde sağa gider
        yn.setx(x + 20)

    if yn.yon == "sol":
        x = yn.xcor()    # x ekseninde sola gider
        yn.setx(x - 20)

def yukariGit():
    if yn.yon != "alt":
        yn.yon = "ust"

def asagiGit():
    if yn.yon != "ust":
        yn.yon = "alt"

def sagaGit():
    if yn.yon != "sol":
        yn.yon = "sag"

def solaGit():
    if yn.yon != "sag":
        yn.yon = "sol"

w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")

# Yılan yeme temas edince ne olacak kodu
def ye():
    global skor
    global maxSkor

    if yn.distance(yem) < 20:
        # Müzik ekleme playsound.playsound("müzikadresi.mp3")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        liste.append(kuyruk)

        skor += 5
        if skor > maxSkor:
            maxSkor = skor
        w.title(f"Skor: {skor} En yüksek skor: {maxSkor}")

    uzunluk = len(liste)
    for indis in range(uzunluk - 1, 0, -1):
        x = liste[indis - 1].xcor()
        y = liste[indis - 1].ycor()
        liste[indis].goto(x, y)

    if len(liste) > 0:
        x = yn.xcor()
        y = yn.ycor()
        liste[0].goto(x, y)

def baslangic():
    global skor
    time.sleep(0.1)
    yn.goto(0, 0)
    yn.yon = "dur"

    for eklem in liste:
        eklem.goto(1000, 1000)
    liste.clear()
    skor = 0
    w.title(f"Skor: {skor} En yüksek skor: {maxSkor}")

while True: # Ana program sonsuz döngüsü
    w.update()
    time.sleep(0.1)
    ye()
    hareket()

    if (yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290):
        # Müzik ekleme playsound.playsound("müzikadresi.mp3")
        baslangic() # Duvar ve kendine çarparsa

    for eklem in liste:
        if eklem.distance(yn) < 20:
            # Müzik ekleme playsound.playsound("müzikadresi.mp3")
            baslangic()

    time.sleep(0)
w.update()
