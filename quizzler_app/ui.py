from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.creating_inner_ui()
        self.next_question()
        self.window.mainloop()
        
    def creating_inner_ui(self):
        ###Canvas

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,
                                    120,
                                    text="created here",
                                    font=("Arial",20,'italic'),
                                    width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=10)

        #LABEL
        self.label_score = Label(text="Score: 0",bg=THEME_COLOR,fg='white')
        self.label_score.grid(column=1,row=0)

        #BUTTON

        self.image_right = PhotoImage(file="quizzler_app\\images\\true.png")
        self.image_wrong = PhotoImage(file="quizzler_app\\images\\false.png")
        self.button_right = Button(image=self.image_right,command=self.bt_correct)
        self.button_wrong = Button(image=self.image_wrong,command=self.bt_wrong)
        self.button_right.grid(column=0,row=2,pady=10)
        self.button_wrong.grid(column=1,row=2,pady=10)

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=self.question)
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text = "You've reached the end the questions")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def bt_correct(self):
        is_right =self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def bt_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        if is_right == False:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)
        