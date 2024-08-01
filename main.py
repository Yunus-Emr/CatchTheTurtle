import turtle
from random import randint

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light grey")
turtle_screen.title("Catch The Turtle ")

turtle_location = randint(a=0, b=300)


turtle_instance = turtle.Turtle()

def game_start():
    score()
    counter()

def score():
    text(x=-20, y=350,value="Score :")

def counter():
  text(x=-20, y=300,value="Time : ")

def text(x:int,y:int,value:str)->None:
    turtle_instance.penup()
    turtle_instance.goto(x, y)
    turtle_instance.pendown()
    turtle_instance.color("black")
    style = ("Verdana", 25, "italic")
    turtle_instance.write(arg=value, align="center", font=style, move=False)
    turtle_instance.hideturtle()

game_start()
turtle.done()


