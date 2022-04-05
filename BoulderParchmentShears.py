# Simple Rock, Paper, Scissors game, but re-named Boulder, Parchment, Shears in honour of Critical Role

import random
import math

def play():
    user = input("Choose your weapon! 'b' for boulder, 'p' for parchment, 's' for shears\n")
    user = user.lower()

    computer = random.choice(['b', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: b > s, s > p, p > b
    if (player == 'b' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'b'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('You and the computer have both chosen {}. It is a tie. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You win the battle!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost in disgrace. :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print('You have won the best of {} games! You have won the war! You are a smart wizard! :D'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. You are a sad wizard.'.format(n))


if __name__ == '__main__':
    play_best_of(3) # 2