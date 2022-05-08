from turtle import Turtle
import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)
    def goto_start(self):
        self.goto(STARTING_POSITION)
    def move_turtle_up(self):
        self.forward(MOVE_DISTANCE)
    def move_turtle_down(self):
        self.backward(MOVE_DISTANCE)
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto_start()
            return True
        return False
    def line_finish(self):
        turtle = Turtle('square')
        turtle.penup()
        turtle.goto(0,280)
        turtle.shapesize(stretch_wid=0.5,stretch_len=30)
    def line_start(self):
        turtle = Turtle('square')
        turtle.penup()
        turtle.goto(0,-270)
        turtle.shapesize(stretch_wid=0.5,stretch_len=30)

