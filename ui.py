from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.title("Quizzer")

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white",
                                 font=("Courier", 14, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question = self.canvas.create_text(150, 125, text="",
                                                width=280,
                                                font=("Times New Roman", 18, "italic"),
                                                fill=THEME_COLOR)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png", )
        self.false_button = Button(image=false_img, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if not self.quiz.still_has_questions():
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def true_answer(self):
        score = self.quiz.check_answer("True")
        self.give_feedback(score)

    def false_answer(self):
        score = self.quiz.check_answer("False")
        self.give_feedback(score)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
