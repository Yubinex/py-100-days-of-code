import turtle as t
from random_rgb_color import rand_rgb_color

tim = t.Turtle()
tim.pensize(3)
tim.hideturtle()
t.colormode(255)


def draw_spirograph(radius=150, speed=0):
    tim.speed(speed)
    for heading in range(0, 360, 5):
        tim.setheading(heading)
        tim.pencolor(rand_rgb_color())
        tim.circle(radius)


def draw_spirograph_example_solution(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(rand_rgb_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(200)
draw_spirograph_example_solution(5)

screen = t.Screen()
screen.exitonclick()
