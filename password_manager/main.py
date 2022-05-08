from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_generate():
    password_letter = [choice(letters) for i in range(randint(8,10))]
    password_symbol = [choice(symbols) for i in range(randint(2,4))]
    password_number = [choice(numbers) for i in range(randint(2,4))]
    password_list = password_letter + password_number + password_symbol 
    shuffle(password_list)
    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    input_password.config(text=f'{password}')
    input_password.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- Find Password  ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open('password_manager\\new_details.json','r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f'{website}',message='no data file found')
    else: 
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f'{website}',message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title=f'{website}',message='no details of this website exits')
            



# ---------------------------- SAVE PASSWORD In Text ------------------------------- #
# def check_file():
#     with open('password_manager\\saved_details.txt','r') as saved_file:
#         one_char = saved_file.read(1)
#         if not one_char:
#             save_file()
#         else:
#             add_data()
# def add_data():
#     with open('password_manager\\saved_details.txt','a') as saved_file:
#         web =input_website.get()
#         password = input_password.get()
#         email= input_username.get()
#         saved_file.write(f"\n{web} | {email} | {password}")
#         clear_entry()
# def save_file():
#     web =input_website.get()
#     password = input_password.get()
#     email= input_username.get()
#     if len(web) == 0 or len(password) == 0:
#         messagebox.showwarning(title='Error',message="You left some filed empty please fill these")
#     else:
#         is_ok = messagebox.askokcancel(title=web,message=f"These are the details you entered \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
#         if is_ok:
#             with open('password_manager\\saved_details.txt','a') as saved_file:
#                 saved_file.write(f"{web} | {email} | {password}\n")
#             clear_entry()
# def clear_entry():
#     input_password.delete(0,END)
#     input_website.delete(0,END)
    # input_username.delete(0,END)
# ---------------------------- SAVE PASSWORD In Json ------------------------------- #
def save_file():
    web =input_website.get()
    password = input_password.get()
    email= input_username.get()
    new_data = {
        web: {
            "email" : email,
            "password" : password
        }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error',message="You left some filed empty please fill these")
    else:
        is_ok = messagebox.askokcancel(title=web,message=f"These are the details you entered \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('password_manager\\new_details.json','r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('password_manager\\new_details.json','w') as data_file:
                    json.dump(new_data,data_file,indent=4) 
            else:
                data.update(new_data)
                with open('password_manager\\new_details.json','w') as data_file:
                    json.dump(data,data_file,indent=4) 
            finally:
                input_password.delete(0,END)
                input_website.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #
#window Creation
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas and photoimage
image_lock = PhotoImage(file="password_manager\\logo.png")
canvas = Canvas(width=200,height=200,bg='black')
canvas.create_image(100,100,image=image_lock)
canvas.grid(column=1,row=0)

#labels
label_website = Label(text="Website:")
label_username = Label(text='Email/Username:')
label_password = Label(text='Password:')
label_website.grid(column=0,row=1)
label_username.grid(column=0,row=2)
label_password.grid(column=0,row=3)


#entry text_box
input_website = Entry(width=21)
input_username = Entry(width=35)
input_password = Entry(width=21)
input_website.grid(column=1,row=1)
input_website.focus()
input_username.grid(column=1,row=2, columnspan=2)
input_username.insert(0,"sharma2001hritik@gmail.com")
input_password.grid(column=1,row=3)

#function call

#buttons
button_generate_password = Button(text='Generate Pass',command=password_generate)
button_add = Button(text='Add',width=36,command=save_file)
button_generate_password.grid(column=2,row=3)
button_add.grid(column=1,row=4,columnspan=2)
button_search = Button(text='Search',command=find_password,width=11)
button_search.grid(column=2,row=1)




window.mainloop()