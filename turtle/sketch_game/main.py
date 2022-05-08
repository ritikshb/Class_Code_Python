from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()
screen.listen()
def move_forward():
    timmy.forward(20)
def back_move():
    timmy.backward(20)
def counter_clockwise():
    timmy.left(10)
def clockwise():
    timmy.right(10)
screen.onkeyrelease(move_forward,'w')
screen.onkeyrelease(back_move,'s')
screen.onkeyrelease(counter_clockwise,'a')
screen.onkeyrelease(clockwise,'d')
screen.onkeyrelease(timmy.reset,'c')
screen.exitonclick()