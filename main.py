from turtle import Screen
from score import Score
from blocks import Block
from paddle import Paddle
from ball import Ball
import time

PADDLE_POSITION = [(0, -300)]

# Blocks:
block_position_x = -380
block_position_y = 0
all_blocks = []
colors = ["red", "orange", "yellow", "green"]

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

screen.listen()

ball = Ball()
score = Score()
paddle = Paddle(PADDLE_POSITION[0])

# Create block wall:
for color in colors:

    for _ in range(2):

        for _ in range(0, 18):
            block = Block((block_position_x, block_position_y), color)
            block_position_x = block_position_x + 45
            all_blocks.append(block)

        block_position_y = block_position_y + 25
        block_position_x = -380

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

while score.user_lives != 0 and score.user_score != 144:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() < -390 or ball.xcor() > 390:
        ball.reverse_x()
    if ball.ycor() > 290:
        ball.reverse_y()

    # here we cannot use distance cause paddle is long, need to use xcors 100:
    if 100 >= paddle.xcor() - ball.xcor() >= -100 and ball.ycor() < -270:
        ball.reverse_y()
    if ball.ycor() < -300:
        score.life_less()
        ball.reset_ball()

    for block in all_blocks:
        if ball.distance(block) < 27:
            block.destroy_block()
            ball.reverse_y()
            score.user_point()

    screen.update()

if score.user_lives == 0:
    score.end_game()
if score.user_score == 144:
    score.win_game()

screen.exitonclick()