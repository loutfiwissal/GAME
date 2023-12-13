from tkinter import *
import random

nbr_secret = random.randint (1 , 100)

def Check_Guess() :
    guess = int(number.get())
    if guess == nbr_secret :
        result_label.config(text="Bravoo 👏🏻!!")
    elif guess < nbr_secret :
        result_label.config(text="More !")
    else:
        result_label.config(text="Less !")
game =Tk()
game.title("GUESS THE NUMBER !")

Label(game, text="Guess The Nunber Between 1 And 100")
number = Entry(game)
number.pack()

Button ( game, text="Check!", command=Check_Guess).pack()

result_label = Label (game, text="")
result_label.pack()
game.mainloop()