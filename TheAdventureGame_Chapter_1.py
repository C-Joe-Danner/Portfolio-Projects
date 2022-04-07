# Authors Bats and Capybara

import sys
import time

a = 2.1
b = 0.19
c = 0.12

def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling.")
    time.sleep(a)
    print("Light begins flooding in.")
    time.sleep(a)
    print()
    question = '"I\'m in a cave...?"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print("The rock released a boulder that was blocking the cave entrance.")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Exit forward through the caves entrance, into the light.")
    time.sleep(a)
    print("Path #2: Explore the depths of the rear of the cave, into the darkness.")
    time.sleep(a)
    print("Path #3: Climb down the vines into a bottomless hole in the ground.")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


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
print("It's a beautiful morning by the lake when an adorable Capybara swims up to you.")
time.sleep(a)
print("You're taken aback when the Capy begins to speak to you...")
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
print("=================================END OF CHAPTER 1=================================")
