from tkinter import *
window = Tk()
window.title("mile to km")
# window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
mile_input = Entry(width=10)
mile_input.insert(END,string="0")
mile_input.grid(column=1,row=0)
label_mile = Label(text="mile")
label_mile.grid(column=2,row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0,row=1)
# in_km = 0
def converter_mile_km():
    # global in_km
    mile_input_int = float(mile_input.get())
    in_km = mile_input_int*1.6
    # label_input = Label(text=f"{in_km}")
    # label_input.grid(column=1,row=2)
    km_convert_label.config(text=f"{in_km}")
label_km = Label(text="km")
label_km.grid(column=2,row=1)

km_convert_label = Label(text="0")
km_convert_label.grid(column=1,row=1)

button = Button(text= 'calculate',command=converter_mile_km)
button.grid(column=1,row=3)

window.mainloop()