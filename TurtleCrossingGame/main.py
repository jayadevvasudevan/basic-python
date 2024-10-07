import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
cars = CarManager()
scores = Scoreboard()
screen.onkey(tim.move_up, "Up")
loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_counter += 1
    cars.movee()

    if loop_counter == 6:
        cars.generate_car()
        loop_counter = 0

    for car in cars.cars:
        if car.distance(tim) < 20:
            scores.game_over()
            game_is_on = False


    if tim.ycor() == 280:
        scores.level_up()
        tim.reset_turtle()
        cars.speed_up()


screen.exitonclick()