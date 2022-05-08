from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on = True

while game_is_on: 
    screen.update()
    time.sleep(0.1)   
    snake.move()
    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extand_snake()
        score_board.scoreboard()
    #Detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        game_is_on =False
        score_board.game_over()
    #Detect collision with snake itself
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) <10:
            game_is_on = False
            score_board.game_over()
            

screen.exitonclick()