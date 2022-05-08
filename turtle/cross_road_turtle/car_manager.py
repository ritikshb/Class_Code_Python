from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            pos_y = random.randint(-250,260)
            cars_turtle = Turtle('square')
            cars_turtle.shapesize(stretch_wid=1,stretch_len=2)
            cars_turtle.penup()
            cars_turtle.color(random.choice(COLORS))
            cars_turtle.goto(280,pos_y)
            # cars_turtle.setheading(180)
            self.all_cars.append(cars_turtle)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        

        
        