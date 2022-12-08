import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setup screen
screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# initialize player
player = Player()

# player movement
screen.onkey(player.go_up, "Up")

# initialize car manager
car_manager = CarManager()

# initialize scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    scoreboard.update_scoreboard()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    # detect if player crossed finish line
    if player.is_at_finish_line():
        scoreboard.increase_score()
        car_manager.level_up()
        player.return_to_start()
            
screen.exitonclick()
