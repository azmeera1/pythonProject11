import random
from tkinter import *
import pandas
import random

current_card = {}

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("C:\\Users\\rb632\\Downloads\\flash-card-project-start\\data\\french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_text, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = windows.after(3000, func=next_card)


def flip_card():
    canvas.itemconfig(card_text, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


windows = Tk()
windows.title("flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="C:\\Users\\rb632\\Downloads\\flash-card-project-start\\images\\card_front.png")
card_back_image = PhotoImage(file="C:\\Users\\rb632\\Downloads\\flash-card-project-start\\images\\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
my_image = PhotoImage(file="C:\\Users\\rb632\\Downloads\\flash-card-project-start\\images\\right.png")
button = Button(image=my_image, padx=50, pady=50, highlightthickness=0, command=next_card)
button.grid(row=1, column=1)
red_image = PhotoImage(file="C:\\Users\\rb632\\Downloads\\flash-card-project-start\\images\\wrong.png")
button1 = Button(image=red_image, padx=50, pady=50, highlightthickness=0, command=next_card)
button1.grid(row=1, column=0)
next_card()
windows.mainloop()