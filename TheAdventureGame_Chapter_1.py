# Authors Bats and Capybara

import sys
import time

a = 2.5
b = 0.25
c = 0.12

def intro():
    print()
    print("Beams of sunlight shine through the trees and over the crystal clear lake.")
    time.sleep(a)
    print("The calm you feel this morning is matched by the stillness of the water's surface.")
    time.sleep(a)
    print("You can hear the rustling of small animals in the forest behind you.")
    time.sleep(a)
    print()
    print("You blink your eyes as you see a sudden change in the water.")
    time.sleep(a)
    print("There's something in the water! It's big, much bigger than a fish.")
    time.sleep(a)
    print("And it's coming right towards you!!!")
    time.sleep(a)
    print()
    beginGame = input("Do you run or stay still? (R/S)")
    if beginGame == "r" or beginGame == "R":
        time.sleep(a)
        game_over("You slipped on a rock, hit your head and died. \nOh no! Maybe next time.")
        time.sleep(a)
    elif beginGame == "s" or beginGame == "S":
        begin()

def begin():
    print()
    time.sleep(a)
    print("You stay still as the water breaks, and reveals...")
    time.sleep(a)
    print()
    print("A...Capybara?")
    print()
    time.sleep(a)
    print("The Capybara shakes out its fur and slowly walks right up to you.")
    time.sleep(a)
    print("It tilts its head to look up at you...and begins talking!?!?")
    question = '"Hail and well met!\n I\'m Capy the Capybara, and I need your help."'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)
    print()
    print()
    print("Shocked, you are unsure how to react.")
    time.sleep(a)
    print()
    question = '"I\'m in search of an artifact of incredible power.\n A magical hat that is rumoured to have been worn by famed adventurers Vex\'ahlia and Taako!"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)
    print()
    time.sleep(a)
    print()
    print("Capy looks to you for recognition, but lets out a sigh when they realize you have no idea what they are talking about.")
    time.sleep(a)
    question = '"Anyway... The hat is located in the Abandoned Keep in the middle of the forest.\n Will you go and find this artifact for me?\n You will be greatly rewarded."'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)
    print()
    time.sleep(a)
    print()
    time.sleep(a)
    print("After a moment you nod your head to Capy.")
    time.sleep(a)
    print()
    print("Capy smiles in an odd way and reveals three different paths you can take to get to the Abandoned Keep. ")
    time.sleep(a)
    print()
    print("Option #1: Take the Twisting Forest Path to the Abandoned Keep.")
    time.sleep(a)
    print("Option #2: Take the River Route to the Abandoned Keep.")
    time.sleep(a)
    print("Option #3: Take the Main Road the Abandoned Keep.")
    time.sleep(a)
    print()
    print("You think for a moment and realize there is a fourth option.")
    time.sleep(a)
    print("Option #4: Go home and take a nap.")
    time.sleep(a)
    print()
    firstPath = input("Which option will you choose? (1/2/3/4): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()
    elif firstPath == '4':
        time.sleep(a)
        game_over_begin("You head straight home, get into bed and take a nap. Hoping it was all just a dream.\nYour house catches on fire as you sleep and you die.\nOh no! Maybe next time.")
        time.sleep(a)
def game_over_begin(reason):
    print("\n" + reason)
    time.sleep(a)
    print("Game Over!")
    play_again_begin()
def play_again_begin():
    print("\nDo you want to play from the beginning?\nReplay last decision?\nOr leave the adventure? (B/R/L)")
    answer = input(">").lower()
    if "b" in answer:
        intro()
    elif "r" in answer:
        begin()
    elif "l" in answer:
        print("=================================Play Again Soon=================================")
        exit()

def path1():
    print("Yay!")

def path2():
    print("Woohoo!")

def path3():
    print("Yassss!")


# function to ask play again or not
def play_again():
    print("\nDo you want to play again? (Y/N)")
    answer = input(">").lower()
    if "y" in answer:
        intro()
    else:
        print("=================================Play Again Soon=================================")
        exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
    print("\n" + reason)
    time.sleep(a)
    print("Game Over!")
    play_again()

# Opening

print()
print()
print("          |=================================|")
time.sleep(b)
print("          |                                 |")
time.sleep(b)
print("          |        Bats and Capybara        |")
time.sleep(b)
print("          |             presents            |")
time.sleep(b)
print("          |       The Adventure Game!       |")
time.sleep(b)
print("          |                                 |")
time.sleep(b)
print("          |=================================|")
print()
print()
time.sleep(a)
print("Hail and Well Met!")
time.sleep(a)
print("Welcome to The Adventure Game!")
time.sleep(a)
print()
question = '"Would you like to go on an adventure?"'
for character in question:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(c)
print("\n")
startGame = input('(Y/N):')
if startGame == "n" or startGame == "N":
    print("Oh no! Maybe next time.")
    time.sleep(a)
elif startGame == "y" or startGame == "Y":
    intro()

print("\n\n")
print("=================================Play Again Soon=================================")
