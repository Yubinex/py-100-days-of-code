import turtle as t
import random
from random_rgb_color import rand_rgb_color


tim = t.Turtle()
tim.speed(0)
tim.pensize(8)
tim.hideturtle()
t.colormode(255)

directions = [0, 90, 180, 270, 360]


def rand_walk():
    tim.pencolor(rand_rgb_color())
    tim.setheading(random.choice(directions))
    tim.forward(20)


def check_pos():
    if tim.xcor() > 300 or tim.xcor() < -300 or tim.ycor() > 300 or tim.ycor() < -300:
        tim.penup()
        tim.setposition(0, 0)
        tim.pendown()


while True:
    check_pos()
    rand_walk()
