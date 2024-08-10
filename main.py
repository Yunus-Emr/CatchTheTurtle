from turtle import Turtle, Screen
from random import randint

def score():
    turtle_score.speed(0)
    turtle_score.penup()
    turtle_score.goto(-20, 350)
    turtle_score.pendown()
    turtle_score.color("Blue")
    style = ("Verdana", 25, "italic")
    turtle_score.write(arg="Score :", align="center", font=style)

def timer():
    turtle_timer.speed(0)
    turtle_timer.penup()
    turtle_timer.goto(-20, 300)
    turtle_timer.pendown()
    turtle_timer.color("black")
    style = ("Verdana", 25, "italic")
    turtle_timer.write(arg="Time :", align="center", font=style)

def countdown(time):
    turtle_countdown.color("black")

    screen.onclick(None)
    turtle_countdown.clear()

    if time > 0:
        turtle_countdown.penup()
        turtle_countdown.goto(60, 298)
        turtle_countdown.pendown()
        turtle_countdown.write(time, align='center', font=Font)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle_timer.clear()
        turtle_countdown.penup()
        turtle_countdown.goto(-20, 298)
        turtle_countdown.pendown()
        turtle_countdown.write("Game Over", align='center', font=Font)
        turtle_turtle.hideturtle()
        screen.onclick(lambda x, y: start_game())

def start_game():
    global game_started
    if not game_started:
        game_started = True
        turtle_turtle.showturtle()
        turtle_turtle.onclick(move_turtle)
        countdown(30)
        move_turtle_randomly()

def move_turtle(x, y):
    global score_count
    if game_started:
        score_count += 1
        update_score()
        move_turtle_randomly()

def move_turtle_randomly():
    if game_started:
        x = randint(-300, 300)
        y = randint(-300, 300)
        turtle_turtle.penup()
        turtle_turtle.goto(x, y)
        turtle_turtle.pendown()
        screen.ontimer(move_turtle_randomly, 1000)  # Her 1 saniyede bir hareket ettirir

def update_score():
    turtle_score.clear()
    turtle_score.write(f"Score : {score_count}", align="center", font=Font)

Font = ("Arial", 25, "normal")

# Score ve Timer için
turtle_score = Turtle()
turtle_timer = Turtle()
turtle_score.hideturtle()
turtle_timer.hideturtle()

# Geri sayaç için
turtle_countdown = Turtle()
turtle_countdown.hideturtle()
turtle_countdown.write("Start ", align='center', font=Font)

screen = Screen()
screen.onclick(lambda x, y: start_game())

# Ekranımız
turtle_screen = Screen()
turtle_screen.bgcolor("light grey")
turtle_screen.title("Catch The Turtle")

score()
timer()

# Turtle için
turtle_turtle = Turtle()
turtle_turtle.shape("turtle")
turtle_turtle.speed(0)
turtle_turtle.shapesize(2)
turtle_turtle.hideturtle()  # Başlangıçta gizle

# Oyun durumu ve skor
game_started = False
score_count = 0

turtle_screen.mainloop()
