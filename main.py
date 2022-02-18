from tkinter import *
from random import randint
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FRONTCARD_COLOR = "#FDFDFE"
TEXT_BACKGROUND = "#90C0AF"

data_frame_main = pandas.read_csv("data/french_words.csv")

try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
    word_dict = data_frame.to_dict(orient="records")
except FileNotFoundError:
    word_dict = data_frame_main.to_dict(orient="records")


new_word = {}


def french_word_gen():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = word_dict[randint(0, len(word_dict))]
    new_french_word = new_word['French']
    french.config(text="French", bg=FRONTCARD_COLOR, fg="black")
    canvas.itemconfig(card_background, image=logo_img)
    word.config(text=new_french_word, bg=FRONTCARD_COLOR, fg="black")
    window.after(3000, translated_word)


def translated_word():
    new_english_word = new_word['English']
    word.config(text=new_english_word)
    french.config(text="English")
    canvas.itemconfig(card_background, image=new_image)
    word.config(bg=TEXT_BACKGROUND, fg=FRONTCARD_COLOR)
    french.config(bg=TEXT_BACKGROUND, fg=FRONTCARD_COLOR)


def known_card():
    word_dict.remove(new_word)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(word_dict))
    french_word_gen()



window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, translated_word)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
card_background = canvas.create_image(400, 263, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)


french = Label(text="French", font=("Arial", 40, "italic"), bg=FRONTCARD_COLOR)
french.place(x=400, y=150,anchor='center')

word = Label(text="", font=("Arial", 60, "bold"), bg=FRONTCARD_COLOR)
word.place(x=400, y=263, anchor='center')

french_word_gen()

wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT, command=french_word_gen)
wrong.grid(column=0, row=2,)

right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT, command=known_card)
right.grid(column=1, row=2,)










window.mainloop()