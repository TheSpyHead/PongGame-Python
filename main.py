# Pong Game
# created by TheSpyHead
from turtle import Screen
from paddel import  Paddle
from ball import Ball
import time
from score import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create objects
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# Controls
screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_right) < 50 and ball.xcor() > 280 or ball.distance(paddle_left) < 50 and ball.xcor() < - 280:

        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_game()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_game()


screen.exitonclick()