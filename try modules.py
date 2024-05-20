import turtle
from turtle import Turtle, Screen
import random
import time

t = Turtle()
t.shape("turtle")
t.shapesize(2)
turtle.bgcolor("light blue")
Font=15
t.write(move=5,align="left",arg="time")
screen.ontimer(lambda: countdown(time - 1), 1000)


direction = [0,45,90,135,180,225,270,360]

for x in range(50):
    t.hideturtle()
    t.penup()
    t.forward(130)
    t.left(90)
    t.right(90)
    t.setheading(random.choice(direction))
    t.showturtle()


turtle.mainloop()








''''
import time

from turtle import Screen, Turtle

FONT = ('Arial', 30, 'normal')

def countdown():


    screen.onclick()  # disable click until countdown completes
    turtle.clear()

    if time > 0:
        turtle.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle.write("Click Screen", align='center', font=FONT)
        screen.onclick(lambda x, y: countdown(15))

turtle = Turtle()
turtle.hideturtle()
turtle.write("Click Screen", align='center', font=FONT)

screen = Screen()
screen.onclick(lambda x, y: countdown(30))
screen.mainloop()

