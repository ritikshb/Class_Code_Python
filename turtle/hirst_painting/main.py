from turtle import Turtle,Screen
import random
import turtle

from pkg_resources import to_filename
timmy = Turtle()

# import colorgram
# color = colorgram.extract('turtle/hirst_painting/download.jpg',21)
# rgb_colors = []
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
turtle.colormode(255)
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
# timmy.pendown()
timmy.setheading(0)
timmy.speed('fastest')
no_of_counts = 101
colors_rgb= [ (39,86,172), (103, 160, 209),(229, 199, 57), (180, 61, 100), (148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39), (51, 110, 95), 
 (65, 53, 42), (12, 66, 135), (57, 52, 67), (187, 78, 103), (60, 50, 64), (96, 107, 170), (221, 172, 191)]
for i in range(1,no_of_counts):
    timmy.dot(20,random.choice(colors_rgb))
    # timmy.penup()
    timmy.forward(50)
    # timmy.pendown()
    if i % 10 == 0:
        # timmy.penup()
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        # timmy.pendown()
screen = Screen()
screen.exitonclick()