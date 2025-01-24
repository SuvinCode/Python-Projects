# Importing the modules
import random

# Importing the files
from .B_Quick_Maths_MathFunctions import *

# Main Tutorial

def quick_math():

    # Data

    answer = True
    question = 1
    speed = []

    print("\n-----Quick Maths--------")
    print("\nThis mode is an infinte mode. ")
    print("This mode will see how fast you can answer the question. ")
    print("If you are slow, you will lose. ")
    print("The time that is given to you to answer will be 1 minute. ")
    print("Each question, the time will decrease every 10 questions asked.")
    print("The range will always be the same which is 10")
    print("\nIf you progress on, it means you got a question right but if the whole program stop, you have gotten the question wrong. ")

    userReady = input("\nPress anything if you are ready : ")

    print()

    while True:
        ran1 = random.randint(1, 4)

        if question == 1:

            userStop = input("\nTime for each question : 600 seconds OR 10 minutes")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 5:

            userStop = input("\nTime for each question : 300 seconds OR 5 minutes")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 10:

            userStop = input("\nTime for each question : 60 seconds OR 1 minutes")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 15:

            userStop = input("\nTime for each question : 30 seconds OR 0.5 minutes")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 20:

            userStop = input("\nTime for each question : 25 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed )
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 25:

            userStop = input("\nTime for each question : 20 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 30:

            userStop = input("\nTime for each question : 15 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 35:

            userStop = input("\nTime for each question : 10 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 40:

            userStop = input("\nTime for each question : 10 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        elif question == 50:

            userStop = input("\nTime for each question : 5 seconds")

            print()

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

        else:

            if ran1 == 1:
                answer, question, speed = addition(answer, question, speed)
            elif ran1 == 2:
                answer, question, speed = substraction(answer, question, speed)
            elif ran1 == 3:
                answer, question, speed = multiplication(answer, question, speed)
            else:
                answer, question, speed = division(answer, question, speed)

            if answer == False:
                break

            question += 1

    print("\nSorry that was wrong : ( ")
    print("\nGood job you have completed {} questions. ".format(question))

    total_speed = sum(speed)
    max_speed = max(speed)
    min_speed = min(speed)
    question_speed = question / total_speed

    print("Your total speed was {} seconds ".format(total_speed))
    print("Your fastest speed was {} seconds".format(min_speed))
    print("Your slowest speed was {} seconds".format(max_speed))

    print("\nYour average speed : {} questions/seconds (q/s2"
          ") ".format(question_speed))

