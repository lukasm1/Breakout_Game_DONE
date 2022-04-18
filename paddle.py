from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.color("white")
        self.shapesize(stretch_len=8)
        self.setheading(180)
        self.shape("square")
        self.penup()
        self.goto(position)

    def right(self):
        if self.xcor() < 300:
            new_x = self.xcor() + 55
            self.goto(new_x, self.ycor())

    def left(self):
        if self.xcor() > -300:
            new_x = self.xcor() - 55
            self.goto(new_x, self.ycor())
