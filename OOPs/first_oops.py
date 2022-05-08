from turtle import Turtle,Screen
daboo = Turtle()
my_screen = Screen()
# print(daboo)
daboo.shape("turtle")
daboo.fillcolor("red")
my_screen.delay(1000)
daboo.forward(50)
my_screen.delay(1000)
daboo.backward(30)
print(my_screen.canvheight)
my_screen.exitonclick()


