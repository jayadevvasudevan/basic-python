from turtle import Turtle

START_COORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(START_COORDS[i])

    def add_segment(self, position):
        newturt = Turtle("square")
        newturt.color("white")
        newturt.penup()
        newturt.setpos(position)
        self.segs.append(newturt)

    def extend(self):
        self.add_segment(self.segs[-1].position())
    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            nx = self.segs[i - 1].xcor()
            ny = self.segs[i - 1].ycor()
            self.segs[i].goto(nx, ny)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def reset(self):
        for seg in self.segs:
            seg.goto(1000, 1000)
        self.segs.clear()
        self.create_snake()
        self.head = self.segs[0]
