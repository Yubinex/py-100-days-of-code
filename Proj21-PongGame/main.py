from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setup screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create ball
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

screen.listen()
# right paddle control
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# left paddle control
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game main loop
running = True
while running:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()
    
    # detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detect ball missing right paddle
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()
        
    # detect ball missing left paddle
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

# keep window open until clicked
screen.exitonclick()
