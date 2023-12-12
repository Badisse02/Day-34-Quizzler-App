from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "normal"))
        self.score_label.grid(column=2, row=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=260,
                                                     text=" Question ",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.config(padx=20, pady=20)
        self.true_button.grid(column=1, row=3)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.config(padx=20, pady=20)
        self.false_button.grid(column=2, row=3)
        self.ident = "0"
        self.next_qt()

        self.window.mainloop()

    def next_qt(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            qt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qt)
            score = self.quiz.score
            self.score_label.config(text=f"Score: {score}")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have finished all the questions!"
                                        f"\n  Your score was: "
                                        f"\n         {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        if self.quiz.check_answer("true"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_qt)

    def false_answer(self):
        if self.quiz.check_answer("false"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_qt)
