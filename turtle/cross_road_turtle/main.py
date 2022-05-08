import time
from turtle import Screen
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
timmy = Player()
timmy.line_finish()
timmy.line_start()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(timmy.move_turtle_up,'Up')
screen.onkeypress(timmy.move_turtle_down,'Down')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    # Stop if turtle touch car 
    for stop_car in cars.all_cars:        
        if stop_car.distance(timmy)<20:
            scoreboard.game_over()
            game_is_on = False
    # Detect Seccessfull crossing
    if timmy.finish_line():
        scoreboard.score_finish_line()
        cars.level_up()


screen.exitonclick()
