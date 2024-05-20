import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle.title("Catch The Turtle")
turtle.shape("turtle")
turtle.shapesize(2)
turtle_instance = turtle.Turtle()
turtle.hideturtle()
turtle_instance.hideturtle()
turtle.penup()

def turtle_shower():
    turtle.showturtle()

turtle_screen.listen()
turtle_screen.onkey(fun=turtle_shower,key="l")
def f(running=2000, screen=300):
    if running:
        turtle.fd(150)
        turtle.lt(80)
        turtle_screen.ontimer(f, 250)
f()

turtle.done()
