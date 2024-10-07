from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        newcar = Turtle()
        newcar.shape("square")
        newcar.penup()
        newcar.shapesize(stretch_wid=1, stretch_len=2)
        newcar.goto(300, random.randint(-245, 245))
        newcar.seth(180)
        newcar.color(random.choice(COLORS))
        self.cars.append(newcar)

    def movee(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
