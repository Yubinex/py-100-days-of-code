from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # labels
        self.score_label = Label(
            text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        image_check = PhotoImage(file="Proj33-GUI_QuizApp/images/true.png")
        self.button_true = Button(image=image_check, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)
        image_false = PhotoImage(file="Proj33-GUI_QuizApp/images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've finished the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
