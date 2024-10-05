from turtle import Turtle

FONT = ("Times New Roman", 24, "normal")


class Scoreboard():

    def __init__(self):
        self.level = 1
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(-250, 250)
        self.update_level()

    def update_level(self):
        self.turtle.clear()
        self.turtle.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()


    def game_over(self):
        # self.turtle.clear()
        self.turtle.goto(0,0)
        self.turtle.write(arg="GAME OVER!", align="center", font=FONT)
