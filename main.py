from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move, "w")
a = 0.1
while game_is_on:
    time.sleep(a)
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        a = player.start(a)
        car_manager.level()
        scoreboard.level_up()
        car_manager.speed_up()
    screen.update()

screen.exitonclick()
