# Importing modules
import random

# Addition function

def addition():

    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ran2 = random.randint(1, index)
        ans = ran1 + ran2

        userNumber = int(input("\n{} + {} : ".format(ran1, ran2)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break


# Subtraction function

def subtraction():
    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ran2 = random.randint(1, index)
        ans = ran1 - ran2

        if ran1 > ran2:
            userNumber = int(input("\n{} - {} : ".format(ran1, ran2)))

            if userNumber == ans:
                print("Correct")
                corrects += 1
            else:
                print("Wrong")
                wrongs += 1
        else:
            userNumber = int(input("{} - {} : ".format(ran2, ran1)))

            if userNumber == ans:
                print("Correct")
                corrects += 1
            else:
                print("Wrong")
                wrongs += 1

            question += 1
            index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break


# Multiplication function

def multiplication():
    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ran2 = random.randint(1, index)
        ans = ran1 * ran2

        userNumber = int(input("\n{} X {} : ".format(ran1, ran2)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break


# Division function

def division():
    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ran2 = random.randint(1, index)
        multiple_ans = ran1 * ran2

        division_ran = random.randint(1, 3)

        if division_ran == 1:
            userNumber = int(input("\n{} / {} : ".format(multiple_ans, ran1)))
            ans = multiple_ans / ran1

            if userNumber == ans:
                print("Correct")
                corrects += 1
            else:
                print("Wrong")
                wrongs += 1
        else:
            ans = multiple_ans / ran2
            userNumber = int(input("{} / {} : ".format(multiple_ans, ran2)))

            if userNumber == ans:
                print("Correct")
                corrects += 1
            else:
                print("Wrong")
                wrongs += 1

        question += 1
        index += 1

        userChoice = input("\nDo you want to quit :")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break

# Square function

def square():

    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ans = ran1 ** 2

        userNumber = int(input("\n{} ^ 2 : ".format(ran1)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break

# SquareRoot Function

def squareroot():

    # Data
    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:
        ran1 = random.randint(1, index)
        square_ans = ran1 ** 2
        ans = ran1

        userNumber = int(input("\n{} Squarerooted : ".format(square_ans)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break

# Cube function

def cube():

    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:

        ran1 = random.randint(1, index)
        ans = ran1 ** 3

        userNumber = int(input("\n{} ^ 2 : ".format(ran1)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break

# CubeRoot Function

def cuberoot():

    # Data
    # Data

    question = 1
    corrects = 0
    wrongs = 0
    index = 1
    quit = ["quit", "q", "Quit", "q", "Yes", "Y", "y", "yes"]

    while True:
        ran1 = random.randint(1, index)
        cube_ans = ran1 ** 3
        ans = ran1

        userNumber = int(input("\n{} Cuberooted : ".format(cube_ans)))

        if userNumber == ans:
            print("Correct")
            corrects += 1
        else:
            print("Wrong")
            wrongs += 1

        question += 1
        index += 1

        userChoice = input("Do you want to quit : ")

        if userChoice in quit:
            print("\nNumber of questions answered :", question)
            print("Number of corrects :", corrects)
            print("Number of wrongs :", wrongs)
            break

# Greeting

def practiceMode():
    print("\nWelcome to the practice mode.")
    print("This practice mode is an infinte mode")

    print("\nChoices :")

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. SquareRoot")
    print("7. Cube")
    print("8. CubeRoot")

    userChoice = int(input("\nChoose your mode (in numerical form) : "))

    if userChoice == 1:
        addition()
    elif userChoice == 2:
        subtraction()
    elif userChoice == 3:
        multiplication()
    elif userChoice == 4:
        division()
    elif userChoice == 5:
        square()
    elif userChoice == 6:
        squareroot()
    elif userChoice == 7:
        cube()
    elif userChoice == 8:
        cuberoot()
    else:
        print("\nInvalid Choice!")
