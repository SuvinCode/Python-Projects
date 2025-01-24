# Import modules
import time

# Importing files
from Math_Game.C_Beat_The_Clock.B_Beat_The_Clock_MathFunctions import *

# Very Easy Mode

def veryEasy():

    print("\nThis is the very easy mode.")
    print("This mode contains addition and subtraction. ")

    userTimer = int(input("\nFirst, enter the timer that you want in seconds : "))
    index = int(input("Secondly, enter the range for the randomiser : "))

    print("Try to answer as much questions in {} seconds".format(userTimer))

    print()

    # Data
    wrongs = 0
    corrects = 0
    question = 0

    answer = True
    timerLst = []

    while True:
        ran1 = random.randint(1, 2)

        if ran1 == 1:
            start = time.time()
            answer, index = addition(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        else:
            start = time.time()
            answer, index = substraction(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        if sum(timerLst) >= userTimer:
            break

    print("\nTime's up!!")

    # Corrects and Wrongs
    print("\n------Corrects And Wrongs --------")
    print("\nNumber of corrects :", corrects)
    print("Number of wrongs :", wrongs)

    if wrongs == 0:
        wrongs = 1
        print("Average of corrects and wrongs :", corrects / wrongs)
    else:
        print("Average of corrects and wrongs :", corrects / wrongs)

    # Speed And Question
    print("\n------Speed And Questions ------")
    print("\nNumber of questions answered :", question)
    print("Your fastest speed : {} seconds".format(min(timerLst)))
    print("Your slowest speed : {} seconds".format(max(timerLst)))
    print("Average speed : {} q/s".format(question / sum(timerLst)))

# Easy Mode

def Easy():

    print("\nThis is the easy mode.")
    print("This mode contains addition, subtraction, multiplication and division. ")

    userTimer = int(input("\nFirst, enter the timer that you want in seconds : "))
    index = int(input("Secondly, enter the range for the randomiser : "))

    print("Try to answer as much questions in {} seconds".format(userTimer))

    print()

    # Data
    wrongs = 0
    corrects = 0
    question = 0

    answer = True
    timerLst = []

    while True:
        ran1 = random.randint(1, 4)

        if ran1 == 1:
            start = time.time()
            answer, index = addition(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 2:
            start = time.time()
            answer, index = substraction(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 3:
            start = time.time()
            answer, index = multiplication(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        else:
            start = time.time()
            answer, index = division(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        if sum(timerLst) >= userTimer:
            break

    print("\nTime's up!!")

    # Corrects and Wrongs
    print("\n------Corrects And Wrongs --------")
    print("\nNumber of corrects :", corrects)
    print("Number of wrongs :", wrongs)

    if wrongs == 0:
        wrongs = 1
        print("Average of corrects and wrongs :", corrects / wrongs)
    else:
        print("Average of corrects and wrongs :", corrects / wrongs)

    # Speed And Question
    print("\n------Speed And Questions ------")
    print("\nNumber of questions answered :", question)
    print("Your fastest speed : {} seconds".format(min(timerLst)))
    print("Your slowest speed : {} seconds".format(max(timerLst)))
    print("Average speed : {} q/s".format(question / sum(timerLst)))


# Medium Mode

def Medium():
    print("\nThis is the medium mode.")
    print("This mode contains addition, subtraction, multiplication, division, square and squareroot. ")

    userTimer = int(input("\nFirst, enter the timer that you want in seconds : "))
    index = int(input("Secondly, enter the range for the randomiser : "))

    print("Try to answer as much questions in {} seconds".format(userTimer))

    print()

    # Data
    wrongs = 0
    corrects = 0
    question = 0

    answer = True
    timerLst = []

    while True:
        ran1 = random.randint(1, 6)

        if ran1 == 1:
            start = time.time()
            answer, index = addition(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 2:
            start = time.time()
            answer, index = substraction(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 3:
            start = time.time()
            answer, index = multiplication(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 4:
            start = time.time()
            answer, index = division(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 5:
            start = time.time()
            answer, index = square(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        else:
            start = time.time()
            answer, index = squareroot(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        if sum(timerLst) >= userTimer:
            break

    print("\nTime's up!!")

    # Corrects and Wrongs
    print("\n------Corrects And Wrongs --------")
    print("\nNumber of corrects :", corrects)
    print("Number of wrongs :", wrongs)

    if wrongs == 0:
        wrongs = 1
        print("Average of corrects and wrongs :", corrects / wrongs)
    else:
        print("Average of corrects and wrongs :", corrects / wrongs)

    # Speed And Question
    print("\n------Speed And Questions ------")
    print("\nNumber of questions answered :", question)
    print("Your fastest speed : {} seconds".format(min(timerLst)))
    print("Your slowest speed : {} seconds".format(max(timerLst)))
    print("Average speed : {} q/s".format(question / sum(timerLst)))

# Hard Mode

def Hard():
    print("\nThis is the hard mode.")
    print("This mode contains addition, subtraction, multiplication, division, square, squareroot, cube and cuberoot. ")

    userTimer = int(input("\nFirst, enter the timer that you want in seconds : "))
    index = int(input("Secondly, enter the range for the randomiser : "))

    print("Try to answer as much questions in {} seconds".format(userTimer))

    print()

    # Data
    wrongs = 0
    corrects = 0
    question = 0

    answer = True
    timerLst = []

    while True:
        ran1 = random.randint(1, 6)

        if ran1 == 1:
            start = time.time()
            answer, index = addition(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 2:
            start = time.time()
            answer, index = substraction(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 3:
            start = time.time()
            answer, index = multiplication(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 4:
            start = time.time()
            answer, index = division(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 5:
            start = time.time()
            answer, index = square(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 6:
            start = time.time()
            answer, index = squareroot(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        elif ran1 == 7:
            start = time.time()
            answer, index = cube(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        else:
            start = time.time()
            answer, index = cuberoot(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                wrongs += 1
                question += 1

        if sum(timerLst) >= userTimer:
            break

    print("\nTime's up!!")

    # Corrects and Wrongs
    print("\n------Corrects And Wrongs --------")
    print("\nNumber of corrects :", corrects)
    print("Number of wrongs :", wrongs)

    if wrongs == 0:
        wrongs = 1
        print("Average of corrects and wrongs :", corrects / wrongs)
    else:
        print("Average of corrects and wrongs :", corrects / wrongs)

    # Speed And Question
    print("\n------Speed And Questions ------")
    print("\nNumber of questions answered :", question)
    print("Your fastest speed : {} seconds".format(min(timerLst)))
    print("Your slowest speed : {} seconds".format(max(timerLst)))
    print("Average speed : {} q/s".format(question / sum(timerLst)))

# Fast But Perfect Mode

def fastButPerfect():
    print("\nThis is the hardest mode since you have everything and you can't get anything wrong.")
    print("This mode contains addition, subtraction, multiplication, division, square, squareroot, cube and cuberoot. ")
    print("If you get any questions wrong, the timer will immeadietly break off. ")

    userTimer = int(input("\nFirst, enter the timer that you want in seconds : "))
    index = int(input("Secondly, enter the range for the randomiser : "))

    print("Try to answer as much questions in {} seconds".format(userTimer))

    print()

    # Data
    corrects = 0
    question = 0

    answer = True
    timerLst = []

    while True:
        ran1 = random.randint(1, 6)

        if ran1 == 1:
            start = time.time()
            answer, index = addition(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 2:
            start = time.time()
            answer, index = substraction(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 3:
            start = time.time()
            answer, index = multiplication(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 4:
            start = time.time()
            answer, index = division(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 5:
            start = time.time()
            answer, index = square(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 6:
            start = time.time()
            answer, index = squareroot(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        elif ran1 == 7:
            start = time.time()
            answer, index = cube(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        else:
            start = time.time()
            answer, index = cuberoot(answer, index)
            end = time.time()
            duration = int(end - start)
            timerLst.append(duration)

            if answer == True:
                corrects += 1
                question += 1
            else:
                print("\nYou have got an answer wrong!")
                break

        if sum(timerLst) >= userTimer:
            break

    print("\nTime's up!!")

    # Corrects and Wrongs
    print("\n------Corrects And Wrongs --------")
    print("\nNumber of corrects :", corrects)


    # Speed And Question
    print("\nNumber of questions answered correctly :", question)
    print("Your fastest speed : {} seconds".format(min(timerLst)))
    print("Your slowest speed : {} seconds".format(max(timerLst)))
    print("Average speed : {} q/s".format(question / sum(timerLst)))


