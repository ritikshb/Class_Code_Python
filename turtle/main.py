import random
from turtle import Turtle,Screen, forward
from random import choice,randint
import turtle
timmy = Turtle()
timmy.color('purple')
timmy.shape('classic')
# for i in range(4):
#     timmy.forward(50)
#     timmy.right(90)
# for i in range(5):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
# def triangle():
#     for i in range(3):
#         timmy.right(120)
#         timmy.forward(100)
# def square():
#     for i in range(4):
#         timmy.right(90)
#         timmy.forward(100)
# def pentagon():
#     for i in range(5):
#         timmy.right(72)
#         timmy.forward(100)
# def hexagon():
#     for i in range(6):
#         timmy.right(60)
#         timmy.forward(100)
# def heptagon():
#     for i in range(7):
#         timmy.right(52.42)
#         timmy.forward(100)
# def octagon():
#     for i in range(8):
#         timmy.right(45)
#         timmy.forward(100)
# def nonagon():
#     for i in range(9):
#         timmy.right(40)
#         timmy.forward(100)
# def decagon():
#     for i in range(10):
#         timmy.right(36)
#         timmy.forward(100)
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()
# timmy.pensize(15)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_figure(degree,no_of_sides):
#     for i in range(0,no_of_sides):
#         timmy.right(degree)
#         timmy.forward(100)
# def calculation():
#     for i in range(3,11):
#         timmy.color(choice(colours))
#         degree = 360/i
#         draw_figure(degree,i)
# calculation()
# timmy.pensize(5)
timmy.speed("fastest")
# # timmy.forward(20)
# # choices(random_walk)
degree_ = [0,90,180,270]
turtle.colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tuples = (r,g,b)
    return tuples
# for i in range(200):
#     timmy.color(random_color())
#     timmy.setheading(choice(degree_))
#     timmy.forward(20)
# for i in range(200):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(5)
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
# draw_spirograph(5)
screen = Screen()
screen.exitonclick()