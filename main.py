from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# ----------------------------------- CSV  ----------------------------------- #

data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
chosen_word = {}

# ----------------------------------- FUNCTIONS ----------------------------------- #


def randomize_dict():
    global chosen_word, start_timer
    window.after_cancel(start_timer)
    flashcard_canvas.itemconfig(canvas_image, image=front_image_file)
    chosen_data = random.choice(data_dict)
    chosen_word = chosen_data
    french_word = chosen_word["French"]
    flashcard_canvas.itemconfig(word_text, text=french_word, fill="black")
    flashcard_canvas.itemconfig(title_text, text="French", fill="black")
    start_timer = window.after(3000, func=mod_card)

def mod_card():
    english_word = chosen_word["English"]
    flashcard_canvas.itemconfig(canvas_image, image=back_image_file)
    flashcard_canvas.itemconfig(word_text, text=english_word, fill="white")
    flashcard_canvas.itemconfig(title_text, text="English", fill="white")

# ----------------------------------- UI  ----------------------------------- #
window = Tk()
window.title(string="Flash Card")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)



flashcard_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image_file = PhotoImage(file="./images/card_front.png")
back_image_file = PhotoImage(file="./images/card_back.png")
canvas_image = flashcard_canvas.create_image(400, 263, image=front_image_file)
title_text = flashcard_canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = flashcard_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
flashcard_canvas.grid(column=0, row=0, columnspan=2)


wrong_file = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_file, command=randomize_dict, highlightthickness=0)
wrong_button.grid(column=0, row=1)


right_file = PhotoImage(file="./images/right.png",)
right_button = Button(image=right_file, command=randomize_dict, highlightthickness=0)
right_button.grid(column=1, row=1)

start_timer = window.after(3000, func=mod_card)
randomize_dict()


window.mainloop()
