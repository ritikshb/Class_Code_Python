from tkinter import *
window  = Tk()
window.title("My first GUI program")
window.minsize(width='500',height='300')

label = Label(text='I\'m label',font=('Arial',24,'bold'))
label.pack()
label['text'] = "new text"
# or
# label.config(text="new text")




#Button

def button_command():
    text_input = input.get()
    # label['text'] ='Button Clicked'
    label.config(text=text_input)
button = Button(text='submit text',command=button_command)
button.pack()

#Entry
#small text box

input = Entry(width=10)
input.pack()
input.insert(END,string="Some text")

#Multiline Text 
text = Text(height=5,width=30)
#puts cursor in textbox
text.focus()
#Add some text to begin with
text.insert(END,"Example of multiline text")
#get current value in textbox at line 1, character 0
print(text.get('1.0',END))
text.pack()

#SpinBox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#Scale
#called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()

#check button
def check_button_used():
    #print 1 or 0
    print(checked_state.get())
#it is from intvar class
checked_state = IntVar()
checkbutton =Checkbutton(text="Is On",variable=checked_state,command=check_button_used)
# checked_state.get()
checkbutton.pack()

#Radio button
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text='option1', value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text='option2', value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple','Pear','Orange','Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()










window.mainloop()