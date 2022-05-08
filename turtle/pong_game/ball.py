from turtle import Turtle, speed 
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed_ball = 0.1
        self.x_position = 10
        self.y_position = 10
    def move_ball(self):
        time.sleep(self.speed_ball) 
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_position *= -1
        self.speed_ball *= 0.9
    def bounce_x(self):
        self.x_position *= -1
        self.speed_ball *= 0.9
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.speed_ball = 0.1
