import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Python Turtle")
'''''
#Square Drawing
turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)

#Star Drawing
turtle_instance= turtle.Turtle()
for i in range(5):
    turtle_instance.right(135)
    turtle_instance.forward(200)
    turtle_instance.right(9)
    turtle_instance.forward(200)

turtle_instance= turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(300)
'''
turtle_instance=turtle.Turtle()
num_sides = 6
angle = 360.0/num_sides
sides_length = 150
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(sides_length)
turtle.done()