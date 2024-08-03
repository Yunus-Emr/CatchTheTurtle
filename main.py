from turtle import Turtle, Screen

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



def countdown(time):
    turtle.color("black")

    screen.onclick(None)  # disable click until countdown completes
    turtle.clear()
    if time > 0:
        turtle.penup()
        turtle.goto(60, 298)
        turtle.pendown()
        turtle.write(time, align='center', font=Font)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle.penup()
        turtle.goto(130, 298)
        turtle.pendown()
        turtle.write("Game Over", align='center', font=Font)
        screen.onclick(lambda x, y: countdown(30))


Font = ("Arial", 25, "normal")


turtle_instance = Turtle()
turtle_instance.hideturtle()

turtle = Turtle()
turtle.hideturtle()
turtle.write("Start ", align='center', font=Font)

screen = Screen()
screen.onclick(lambda x, y: countdown(30))

turtle_screen = Screen()
turtle_screen.bgcolor("light grey")
turtle_screen.title("Catch The Turtle ")

score()
timer()


turtle_screen.mainloop()
