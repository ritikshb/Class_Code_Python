from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball_create = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(right_paddle.up,'Up')
screen.onkeypress(right_paddle.down,'Down')
screen.onkeypress(left_paddle.up,'w')
screen.onkeypress(left_paddle.down,'s')
game_is_on = True
while game_is_on:
    screen.update()
    ball_create.move_ball()
    #Wall detect by ball
    if ball_create.ycor()>280 or ball_create.ycor()<-280:
        ball_create.bounce_y()
    if ball_create.distance(right_paddle) < 50 and ball_create.xcor() >320 or ball_create.distance(left_paddle)< 50 and ball_create.xcor() < -320:
        ball_create.bounce_x()
    #right paddle miss
    if ball_create.xcor()>380:
        ball_create.reset_ball()
        scoreboard.left_score()
    #left paddle miss
    if  ball_create.xcor() < -380 :
        scoreboard.right_score()
        ball_create.reset_ball()
    






screen.exitonclick()