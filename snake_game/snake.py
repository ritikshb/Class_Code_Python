from turtle import Screen,Turtle
import time
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment = []
        self.snake_create()
        self.head = self.segment[0]
    def snake_create(self):
        for starting_position in START_POSITION:
            self.add_segment(starting_position)
    def add_segment(self,position):
        timmy = Turtle(shape='square')
        timmy.color('white')
        timmy.penup()
        timmy.goto(position)
        self.segment.append(timmy)
    def extand_snake(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
                new_pos_x = self.segment[seg_num -1].xcor()
                new_pos_y = self.segment[seg_num-1].ycor()
                self.segment[seg_num].goto(new_pos_x,new_pos_y)
        self.head.forward(MOVE_DISTANCE)
        # self.segment[0].left(90)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
