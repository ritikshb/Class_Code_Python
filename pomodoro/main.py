import math
from tkinter import*
from turtle import title
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- Sound ------------------------------- # 
def sound_play():
    pygame.mixer.init()
    pygame.mixer.music.load(filename="pomodoro\\audio1.mp3")
    pygame.mixer.music.play(loops=0)
def sound_play_start():
    pygame.mixer.init()
    pygame.mixer.music.load(filename="pomodoro\\audio2.mp3")
    pygame.mixer.music.play(loops=0)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label_timer.config(text='Timer')
    label_check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        label_timer.config(text='Break',fg=RED,font=(FONT_NAME,50,'bold'),bg=YELLOW)
        sound_play()
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text='Break',fg=PINK,font=(FONT_NAME,50,'bold'),bg=YELLOW)
        sound_play()
        count_down(short_break_sec)
    else:
        sound_play_start()
        label_timer.config(text='Work',fg=GREEN,font=(FONT_NAME,50,'bold'),bg=YELLOW)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
       timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps):
            marks += "🗸"
            label_check_mark.config(text=marks)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
image_tomato = PhotoImage(file='pomodoro\\tomato.png')

#canvas
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112,image=image_tomato)
timer_text = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)
#count Function
# count_down(5)

#label
label_timer = Label(text='Timer',font=(FONT_NAME,50,'bold'),fg=GREEN,bg=YELLOW)
label_timer.grid(column=1,row=0)
label_check_mark = Label(bg=YELLOW)
label_check_mark.grid(column=1,row=3)
  
#button
start_button = Button(text='start',bg='white',width=5,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
rest_button = Button(text='rest',bg='white',width=5,highlightthickness=0,command=reset_timer)
rest_button.grid(column=2,row=2)

window.mainloop()