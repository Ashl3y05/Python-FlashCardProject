from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title(string="Flash Card")
window.config(padx=50, pady=50,background=BACKGROUND_COLOR)

flashcard_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_file = PhotoImage(file="./images/card_front.png")
flashcard_canvas.create_image(400, 263, image=image_file)
flashcard_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
flashcard_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
flashcard_canvas.grid(column=0, row=0, columnspan=2)


wrong_file = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_file, highlightthickness=0)
wrong_button.grid(column=0, row=1)


right_file = PhotoImage(file="./images/right.png")
right_button = Button(image=right_file, highlightthickness=0)
right_button.grid(column=1, row=1)
window.mainloop()
