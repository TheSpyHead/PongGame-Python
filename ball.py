from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self): # bounce in y axis
        self.y_move *= -1 # multiplies y by -1 so 10y --> -10 so self.y_move = self_y * -1
        self.move_speed *= 0.9
    def bounce_x(self): # bounce in x axis
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x()

