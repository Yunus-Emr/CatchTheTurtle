from turtle import Turtle, Screen

Font = ("Arial", 25, "normal")

def countdown(time):
    turtle.color("black")

    screen.onclick(None)  # disable click until countdown completes
    turtle.clear()
    if time > 0:
        turtle.penup()
        turtle.goto(60, 298)
        turtle.pendown()
        turtle.write(time, align='center', font=Font)
        screen.ontimer(lambda: countdown(time - 1), 10)
    else:
        turtle.penup()
        turtle.goto(130, 298)
        turtle.pendown()
        turtle.write("Game Over", align='center', font=Font)
        screen.onclick(lambda x, y: countdown(30))



turtle = Turtle()
turtle.hideturtle()
turtle.write("Start ", align='center', font=Font)
screen = Screen()


