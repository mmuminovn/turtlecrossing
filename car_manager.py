from turtle import Turtle
from random import randint, choice

COLORS = ["red", "yellow", "green", "blue", "brown", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):

        self.speed = 0
        self.cars = []
        self.time_sleep = 0.1

    def create_car(self):
        num = randint(1, 6)
        if num == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(10)

    def level(self):
        self.time_sleep *= 0.9

    def speed_up(self):
        self.speed += MOVE_INCREMENT
