from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("Proj30-FlashCardApp/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Proj30-FlashCardApp/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# FUNCTIONS
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    
    flip_timer = window.after(3000, func=flip_card)
    
    
def is_known():
    to_learn.remove(current_card)
    
    data = pd.DataFrame(to_learn)
    data.to_csv("Proj30-FlashCardApp/data/words_to_learn.csv", index=False)
    next_card()
    
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back_image)


# WINDOW SETUP
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# CANVAS
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="Proj30-FlashCardApp/images/card_front.png")
card_back_image = PhotoImage(file="Proj30-FlashCardApp/images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# WRONG/RIGHT BUTTONS
wrong_image = PhotoImage(file="Proj30-FlashCardApp/images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="Proj30-FlashCardApp/images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

mainloop()
