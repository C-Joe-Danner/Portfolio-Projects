# A simple Rock, Paper, Scissors game but re-named in honour of Critical Role.

# Import Required Library
from tkinter import *
import random

root = Tk()
root.geometry("630x225")
root.title("Boulder, Parchment, Shears!")

# Dictionaries and vars
outcomes = {
	"Boulder": {"Boulder": 1, "Parchment": 0, "Shears": 2},
	"Parchment": {"Boulder": 2, "Parchment": 1, "Shears": 0},
	"Shears": {"Boulder": 0, "Parchment": 2, "Shears": 1}
}

comp_score = 0
player_score = 0


# Functions
def converted_outcome(number):
	if number == 1:
		return "Boulder"
	elif number == 2:
		return "Parchment"
	elif number == 3:
		return "Shears"


def outcome_handler(user_choice):
	global comp_score
	global player_score
	random_number = random.randint(1, 3)
	computer_choice = converted_outcome(random_number)
	outcome = outcomes[user_choice][computer_choice]

	player_choice_label.config(fg="blue", text="Adventurer's Choice : " + str(user_choice))
	computer_choice_label.config(fg="red", text="The Lich's Choice : " + str(computer_choice))

	if outcome == 2:
		player_score = player_score + 1
		player_score_label.config(text="Adventurer : " + str(player_score))
		outcome_label.config(fg="purple", text="Outcome : Adventurer Won")
	elif outcome == 0:
		comp_score = comp_score + 1
		computer_score_label.config(text="The Lich : " + str(comp_score))
		outcome_label.config(fg="purple", text="Outcome : The Lich Won")
	elif outcome == 1:
		player_score = player_score
		comp_score = comp_score
		player_score_label.config(text="Adventurer : " + str(player_score))
		computer_score_label.config(text="The Lich : " + str(comp_score))
		outcome_label.config(fg="purple", text="Outcome : Draw")


# Labels
Label(root, fg="blue", text="Boulder, Parchment, Shears!", font=("Calibri Bold", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(root, text="Choose your weapon", font=("Calibri", 12)).grid(row=1, sticky=N)
player_score_label = Label(root, text="Adventurer : 0", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(root, text="The Lich : 0", font=("Calibri", 12))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(root, font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(root, font=("Calibri", 12))
computer_choice_label.grid(row=3, sticky=E)
outcome_label = Label(root, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

# Buttons
Button(root, text="Boulder", width=15, command=lambda: outcome_handler("Boulder")).grid(row=4, sticky=W, padx=5, pady=5)
Button(root, text="Parchment", width=15, command=lambda: outcome_handler("Parchment")).grid(row=4, sticky=N, pady=5)
Button(root, text="Shears", width=15, command=lambda: outcome_handler("Shears")).grid(row=4, sticky=E, padx=5, pady=5)

# Execute Tkinter
root.mainloop()
