from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(x=0, y=275)
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Current Score: {self.score}, High Score: {self.high_score}", move=False, align="center", font=("Comic Sans MS", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.display()

    def reset_s(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over!! Your Final score is: {self.score}", move=False, align="center", font=("Comic Sans MS", 16, "normal"))
