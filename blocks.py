from turtle import Turtle


class Block(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.create_block(position, color)

    def create_block(self, position, color):
        self.shapesize(stretch_len=2)
        self.color(color)
        self.setheading(180)
        self.shape("square")
        self.penup()
        self.goto(position)

    def destroy_block(self):
        self.goto(1000, -1000)