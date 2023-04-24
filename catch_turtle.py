import turtle
import random

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Catch The Turtle")
FONT = ("Arial", 20, "normal")

def setup_score():
    cizgi.clear()
    cizgi.hideturtle()
    cizgi.penup()
    cizgi.setpos(0, 400)
    cizgi.write(f"Score: {sayac}", move=False, align="center", font=FONT)

def clicked_turtle(x, y):
    global sayac
    sayac += 1
    print("Tıklanan nokta: ", x, y)
    print("Skor: ", sayac)
    setup_score()

def make_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.shape("turtle")
    t.turtlesize(2, 2)

    while True:
        t.setpos(random.randint(-400, 400), random.randint(-400, 400))
        t.showturtle()  # Kaplumbağayı göster
        t.onclick(clicked_turtle)
        turtle.delay(500)
        t.hideturtle()  # Kaplumbağayı gizle

sayac = 0
cizgi = turtle.Turtle()
setup_score()
make_turtle()

turtle.mainloop()
