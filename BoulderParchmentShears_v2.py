# Simple Rock, Paper, Scissors game, but re-named Boulder, Parchment, Shears in honour of Critical Role

import random

user_wins = 0
computer_wins = 0

options = ['boulder', 'parchment','shears']
print("\n")
print("\t=========================================")
print("\t=          Hail and well met!           =")
print("\t=========================================")
print("\t=                                       =")
print("\t=          WELCOME TO BOULDER           =")
print("\t=       PARCHMENT AND SHEARS GAME       =")
print("\t=                                       =")
print("\t=========================================")
print("\t= You have been challenged to a battle  =")
print("\t=   of wits by an evil cackling lich!   =")
print("\t=========================================")


while True:
    user_input = input('\nBoulder '
                       '\nParchment '
                       '\nShears '
                       '\nQ to quit'
                       '\nYour Pick: ').lower()
    if user_input == 'q':
        break

    if user_input not in ['boulder', 'parchment','shears']:
        print("Choose only from the options.\n")
        continue
    random_num = random.randint(0,2)
    #boulder: 0, parchment: 1, shears: 2
    ai_pick = options[random_num]
    print('The lich chose', ai_pick + ".")

    if user_input == 'boulder' and ai_pick == 'shears':
        print("You defeated the lich!")
        user_wins += 1

    elif user_input == 'parchment' and ai_pick == 'boulder':
        print("You defeated the lich!")
        user_wins += 1

    elif user_input == 'shears' and ai_pick == 'parchment':
        print("You defeated the lich!")
        user_wins += 1

    elif user_input == ai_pick:
        print("It's a draw.")

    else:
        print("You have been bested by the lich!")
        computer_wins += 1

print("\nYou defeated the lich", user_wins, "times.")
print("The lich bested you", computer_wins, "times.")
print("Farewell!")


if __name__ == "__main__":
    print()