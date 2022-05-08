from ast import Break
from time import time
from turtle import Turtle,Screen
import turtle
import pandas as pd
screen = Screen()
image = 'us-states-game-start/blank_states_img.gif'
screen.addshape(image)
Turtle(image)
# correct_number = 0
# print(answer_state)
data = pd.read_csv('us-states-game-start\\50_states.csv')
states_name = data.state.to_list()
# answer_state = screen.textinput(title='Guess the state',prompt='What\'s another state name').title()
# left_states = []
guessed_state =[]
for i in range(0,50):
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 States Correct',prompt='What\'s another state name').title()
    if answer_state in guessed_state:
        pass
    elif answer_state in states_name:
        state_data = data[data['state'] == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        timmy = Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(state_x,state_y)
        timmy.write(answer_state,move=False)
        # correct_number +=1
        guessed_state.append(answer_state) 
    if answer_state == 'Exit':
        # for i in states_name:
        #     if i not in guessed_state:
        #         left_states.append(i)
        left_states = [num for num in states_name if num not in guessed_state]
        left_states_data = {'left_states_c' : left_states}
        left_data = pd.DataFrame(left_states_data)
        left_data.to_csv('us-states-game-start\left_states.csv')
        break









# To find out the coordinates of pointer when click on image
# def get_mouse_click_coordinate(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coordinate)
# screen.mainloop()






screen.exitonclick()

