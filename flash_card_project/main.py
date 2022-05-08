from tkinter import *
from turtle import fillcolor
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


#####---------------------Using french word file---------------------######

try:
    data_file = pd.read_csv("flash_card_project\\data\\words_to_learn.csv")
except:
    data_file = pd.read_csv("flash_card_project\\data\\french_words.csv")
###---orient= "records" is use for make it list and in this it contain differint dictionaries that have keys of column name and data of there index row
dict_data_file = data_file.to_dict(orient="records")
# print(dict_data_file[0])
current_card = 0
def random_french_word():
    global current_card,flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(dict_data_file)
    canvas.itemconfig(canvas_text,text="French",fill= 'black')
    canvas.itemconfig(canvas_word,text = current_card["French"],fill = 'black')
    canvas.itemconfig(canvas_bg,image= image_front)
    flip_time = window.after(3000,func= french_english)
    # french_english()

def french_english():
    global current_card
    canvas.itemconfig(canvas_bg,image= image_back)
    canvas.itemconfig(canvas_text,text="English",fill= 'white')
    canvas.itemconfig(canvas_word,text = current_card["English"],fill= 'white')

def known_word():
    global current_card
    dict_data_file.remove(current_card)
    data= pd.DataFrame(dict_data_file)
    data.to_csv("flash_card_project\\data\\words_to_learn.csv", index= False)
#####---------------------UI---------------------######
#window---

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_time = window.after(3000,func= french_english)


#canvas----

image_front = PhotoImage(file="flash_card_project\\images\\card_front.png")
image_back = PhotoImage(file="flash_card_project\\images\\card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_bg = canvas.create_image(400,263,image=image_front)
canvas_text = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas_word = canvas.create_text(400,263,text="Word",font=("Arial",60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)


#Button-----

image_cross = PhotoImage(file="flash_card_project\\images\\wrong.png")
image_right = PhotoImage(file="flash_card_project\\images\\right.png")
button_cross = Button(image=image_cross,highlightthickness=0,bg=BACKGROUND_COLOR,command=random_french_word)
button_right = Button(image=image_right,highlightthickness=0,bg=BACKGROUND_COLOR,command=known_word)
button_cross.grid(column=0,row=1)
button_right.grid(column=1,row=1)

random_french_word()




window.mainloop()