import turtle
from random import randint

# Turtle objesi oluşturuluyor
tur = turtle.Turtle()

# Turtle'ın şekli ve başlangıç konumu ayarlanıyor
tur.shape('turtle')
tur.shapesize(2)
tur.color("purple")
tur.penup()

# GameBy
name = turtle.Turtle()
name.hideturtle()
name.penup()
name.goto(-50,230)
name.write(f"By Kuday Güllü", font=("Arial",20,"normal"))

# Sayaç için ayrı bir turtle objesi oluşturuluyor
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-200, 200)

# Tıklanma sayısını göstermek için ayrı bir turtle objesi oluşturuluyor
click_counter = turtle.Turtle()
click_counter.hideturtle()
click_counter.penup()
click_counter.goto(100, 200)

# Başlangıç zamanı (30 saniye) ve tıklanma sayısı
time_left = 30
click_count = 0

def update_counter():
    global time_left
    # Sayaç ekranı temizleniyor ve güncelleniyor
    counter.clear()
    counter.write(f"Süre: {time_left} saniye", font=("Arial", 16, "normal"))
    # Zamanı azalt
    time_left -= 1
    # Eğer zaman bitmemişse 1 saniye sonra bu fonksiyonu tekrar çağır
    if time_left >= 0:
        turtle.ontimer(update_counter, 1000)
    else:
        # Zaman bittiğinde turtle'ın hareketini durdur
        turtle.bye()

def move_turtle():
    # Turtle'ı rastgele bir konuma taşı
    tur.goto(randint(-150, 150), randint(-150, 150))
    # 100 milisaniye sonra bu fonksiyonu tekrar çağır
    turtle.ontimer(move_turtle, 500)

def on_turtle_click(x, y):
    global click_count
    click_count += 1
    click_counter.clear()
    click_counter.write(f"Tıklanma sayısı: {click_count}", font=("Arial", 16, "normal"))

# Tıklanma sayısını ilk başta göster
click_counter.write(f"Tıklanma sayısı: {click_count}", font=("Arial", 16, "normal"))

# Turtle'a tıklama olayını bağla
tur.onclick(on_turtle_click)

# Sayaç ve hareketi başlat
update_counter()
move_turtle()

# Turtle grafik ekranını açık tut
turtle.done()