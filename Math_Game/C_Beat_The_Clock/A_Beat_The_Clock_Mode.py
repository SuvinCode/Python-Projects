# Importing files
from Math_Game.C_Beat_The_Clock.C_Beat_The_Clock_RandomisedTimer import *

# Beat The Clock Function

def beat_the_clock():
    print("\n-------Beat The Clock Mode--------")
    print("\nWelcome to the Beat The Clock Mode of this math game. ")
    print("This mode is played to see how many questions you can answer in a certain amount of time. ")
    print("\nThere are many modes that you can choose which are :- ")

    # Modes
    print("\n1. Very Easy Mode (Consists of : Addition and subtraction) ")
    print("2. Easy Mode (Consists of : Addition, subtraction, multiplication, division) ")
    print("3. Medium Mode (Consists of Addition, subtraction, multiplication, division, square, squareroot) ")
    print("4. Hard Mode (Consists of Addition, subtraction, multiplication, division, square, squareroot) ")
    print("5. Fast But Perfect (Consists of everything in hard mode but ou must get nothing wrong) ")

    # Receive the user's choice
    userChoice = int(input("\nChoose your mode in (Numerical Mode) : "))

    # If and else statements

    if userChoice == 1:
        veryEasy()
    elif userChoice == 2:
        Easy()
    elif userChoice == 3:
        Medium()
    elif userChoice == 4:
        Hard()
    elif userChoice == 5:
        fastButPerfect()
    else:
        print("Invalid choice")
