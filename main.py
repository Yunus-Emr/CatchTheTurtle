from turtle import Turtle, Screen
import CountDown

def score():
    text(x=-20, y=350, value="Score :")
def timer():
    text(x=-20,y=300,value="Timer :")

def text(x: int, y: int, value: str) -> None:
    turtle_instance.penup()
    turtle_instance.goto(x, y)
    turtle_instance.pendown()
    turtle_instance.color("black")
    style = ("Verdana", 25, "italic")
    turtle_instance.write(arg=value, align="center", font=style)


turtle_instance = Turtle()
turtle_instance.hideturtle()

turtle_screen = Screen()
turtle_screen.bgcolor("light grey")
turtle_screen.title("Catch The Turtle ")

score()
timer()
CountDown.screen.onclick(lambda x, y: CountDown.countdown(30))

turtle_screen.mainloop()
