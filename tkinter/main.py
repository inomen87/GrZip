from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# function "is_known" is triggered if we know what this French word means. So then it removes that word from a
# "to-learn" list so it doesn't get shown again.
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# in a code block below we set up our window with some initial settings: window title and padding around the
# window content
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# window.after is there to flip the card after 3000 milliseconds. It does so by calling a function "flip_card"
flip_timer = window.after(3000, func=flip_card)


# code block below puts content in our window: card front, card back(they both come from image files in our folder)
# and some text that will show French and English words. "canvas.grid()" is a system that tells those images where
# to go on the window in comparison to other elements such as buttons.
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)



# The code block below is our first button. This is "X" button which we click when we don't know the French word
# It takes image from our folder. When we press it a function called "next_card" gets triggered.
# It uses a grid system to position itself in the window.
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# This code block is our second button, it is same as first one but with different position, image and a function
# it triggers. This one triggers "is_known" function.
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

# From the internet:
# mainloop() is simply a method in the main window that executes what we wish to execute in
# an application (lets Tkinter to start running the application). As the name implies it will loop forever until
# the user exits the window or waits for any events from the user. Any code after this mainloop() method will not run.
window.mainloop()



