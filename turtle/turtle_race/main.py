from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
timmy_turtle = []
user_input = screen.textinput(title="Make your bet",prompt='Which turtle will win the race! enter the Color').lower()
colors = ['red','green','purple','yellow','blue','orange']
y_axis = [-100,-50,0,50,100,150]
is_race_on = False
for i in range(6):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x= -230,y = y_axis[i])
    timmy_turtle.append(timmy)

if user_input:
    is_race_on = True
while is_race_on:
    for turtle in timmy_turtle:
        if turtle.xcor()>210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is winner")
            else:
                print(f"You've lost! The {winning_color} turtle is winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()