from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True


# def game():
#
# game()


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision detection (Food)
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.update_score()

    # Collision detection (Wall):
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_s()
        snake.reset()

    # Collision detection (Body and Tail)
    for segment in snake.segs[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_s()
            snake.reset()






screen.exitonclick()