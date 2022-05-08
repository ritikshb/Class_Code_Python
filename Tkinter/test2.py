from cgitb import text
from tkinter import *
window = Tk()
window.title("Hello my title")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

label = Label(text="my label",font=("Arial",20,'bold'))
label.grid(column=0,row=0)
def button_click():
    input_text = input_user.get()
    label.config(text = input_text )
button = Button(text = 'Button Text',command= button_click)
button.grid(column=1,row=1)

new_button = Button(text='new_Button',command= button_click)
new_button.grid(column= 2,row=0)

input_user = Entry(width= 10)
input_user.insert(END,string="some_text")
input_user.grid(column=3,row=2)


window.mainloop()