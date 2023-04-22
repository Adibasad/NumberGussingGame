import tkinter as tk
from tkinter import Button
import random
import math

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("600x400")
window.config(bg="#065569")
window.resizable(width=False, height=False)

exit_button = tk.Button(window, text="EXIT", font=("black", 14, "bold"), fg="white", bg="red", command=exit)

title = tk.Label(window, text="Guess The Number:)", font=("white", 18), fg="#fffcbd", bg="#065569").place(x=200, y=30)


retries = 0


def update_result(recievedtext):
    result.config(text=recievedtext)


# to start the game by play button
def new_game():

    global chosenone, retries, totalretries
    guess_button.config(state="normal")
    l = int(lower_input.get())
    u = int(upper_input.get())
    totalretries = int(math.log((u-l+1),2))
    chosenone = random.randint(l, u)
    retries = 0
    update_result("Guess a number between {} and {} in {} tries".format(l,u,totalretries))


def play_game():
    global chosenone, retries, totalretries
    choice = int(guessed_number.get())

    if choice != chosenone and retries <= totalretries:
        retries += 1
        if choice > chosenone:
            hint = "Too high!!" \
                   "The number lies between 0 and {}".format(choice)
        else:
            hint = "Too low!!" \
                   "The number lies between {} and 1000".format(choice)
        update_result(hint)

    elif retries > totalretries:
        hint = "You Lose!!" \
               "Correct Number is {}".format(chosenone)
        update_result(hint)

    else:
        hint = "Congrats!You won in {} tries".format(retries)
        update_result(hint)
        guess_button.config(state="disable")


# a label to know what to do next and will be updated
result = tk.Label(window, text="Enter Lower and Upper bound and\nClick on Play to start a new game", font=("Arial", 12, "normal", "italic"), fg="White",
                  bg="#065569")

# button to start a new game
play_button = tk.Button(window, text="PLAY", font=("Ariel", 15, "bold"), fg="black", bg="green", command=new_game)
# button to guess the number on repeat
guess_button = tk.Button(window, text="Guess", font=("Ariel", 14), state="disable", fg="white", bg="black",
                         command=play_game)
# initially the state of the state button is disabled and only abled when we play the game

#placing Everything
exit_button.place(x=280, y=320)
play_button.place(x=200, y=320)
guess_button.place(x=380, y=250)
result.place(x=200, y=200)



# take input for lower and upper bound with two entry feilds and two labels
lowlabel = tk.Label(window, text="Enter Lower Bound", font=("Arial", 14, "normal", "italic"), fg="White", bg="#065569")
upplabel = tk.Label(window, text="Enter Upper Bound", font=("Arial", 14, "normal", "italic"), fg="White", bg="#065569")
lower_number = tk.StringVar()
upper_number = tk.StringVar()
lower_input = tk.Entry(window, font=("Ariel", 11), textvariable=lower_number)
upper_input = tk.Entry(window, font=("Ariel", 11), textvariable=upper_number)

lowlabel.place(x=150, y=100)
upplabel.place(x=150, y=140)
lower_input.place(x=350, y=110)
upper_input.place(x=350, y=150)

# take the input in entry feild
guessed_number = tk.StringVar()
number_input = tk.Entry(window, font=("Ariel", 11), textvariable=guessed_number)
number_input.place(x=200, y=260)
# number_input.pack(ipady=10)

window.mainloop()
