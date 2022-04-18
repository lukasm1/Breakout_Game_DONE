from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, -100)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0, -100)
        self.reverse_x()

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        new_x += self.x_move
        new_y += self.y_move
        self.goto(new_x, new_y)

    def reverse_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def reverse_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9