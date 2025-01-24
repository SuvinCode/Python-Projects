# Import math
# Import random
import random
import math


# Addition Function

def addition(answer, level):

    # Data
    index = 5 * level

    # Random generated number
    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)

    ans = ran1 + ran2

    userNumber = int(input("\n{} + {} : ".format(ran1, ran2)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} + {} : {}".format(ran1, ran2, ans))
        print()
        answer = False
        return answer, level




# Substraction Function

def substraction(answer, level):

    # Data
    index = 5 * (level - 4)

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)

    if ran1 > ran2:

        ans = ran1 - ran2

        userNumber = int(input("\n{} - {} : ".format(ran1, ran2)))

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("{} - {} : {}".format(ran1, ran2, ans))
            print()
            answer = False
            return answer, level
    else:
        ans = ran2 - ran1

        userNumber = int(input("\n{} - {} : ".format(ran2, ran1)))

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("{} - {} : {}".format(ran2, ran1, ans))
            print()
            answer = False
            return answer, level



# Multiplication Function

def multiplication(answer, level):

    # Data
    index = 1 * (level - 9)

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    ans = ran1 * ran2

    userNumber = int(input("{} X {} : ".format(ran1, ran2)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} X {} : {}".format(ran1, ran2, ans))
        print()
        answer = False
        return answer, level




# Division Function

def division(answer, level):

    # Data
    index = 1 * (level - 14)

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    multiple_ans = ran1 * ran2

    division_ran = random.randint(1, 3)

    if division_ran == 1:
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran1)))
        ans = multiple_ans / ran1

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("{} / {} : {}".format(multiple_ans, ran1, ans))
            print()
            answer = False
            return answer, level
    else:
        ans = multiple_ans / ran2
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran2)))

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("{} / {} : {}".format(multiple_ans, ran2, ans))
            print()
            answer = False
            return answer, level

def square(answer, level):

    # Data
    index = 1 * (level - 19)

    ran1 = random.randint(1, index)
    ans = ran1 ** 2

    userNumber = int(input("\n{} ^ 2 : ".format(ran1)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} ^ 2 : {}".format(ran1, ans))
        print()
        answer = False
        return answer, level

# SquareRoot Function

def squareroot(answer, level):

    # Data
    index = 1 * (level - 24)

    ran1 = random.randint(1, index)
    square_ans = ran1 ** 2
    ans = ran1

    userNumber = int(input("\n{} Squarerooted : ".format(square_ans)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} squarerooted : {}".format(square_ans, ans))
        print()
        return answer, level

# Cube function

def cube(answer, level):
    # Data
    index = 1 * (level - 29)

    ran1 = random.randint(1, index)
    ans = ran1 ** 3

    userNumber = int(input("\n{} ^ 3 : ".format(ran1)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} ^ 3 : {}".format(ran1, ans))
        print()
        return answer, level

# CubeRoot Function

def cuberoot(answer, level):

    # Data
    index = 1 * (level - 31)

    ran1 = random.randint(1, index)
    cube_ans = ran1 ** 3
    ans = ran1

    userNumber = int(input("\n{} Cuberooted : ".format(cube_ans)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} cuberooted : {}".format(cube_ans, ans))
        print()
        return answer, level

def addAllDigits(answer, level):

    # Data
    index = 1 * (level - 36)

    if index > 9:
        while index > 9:
            index -= 1

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    ran3 = random.randint(1, index)

    ans = ran1 + ran2 + ran3

    userNumber = int(input("\nAdd all the digits of {}{}{} : ".format(ran1, ran2, ran3)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} + {} + {} : {}".format(ran1, ran2, ran3, ans))
        print()
        return answer, level

def IsAPrimeNumber(answer, level):

    # Data
    index = 1 * (level - 41)

    ran1 = random.randint(1, index)
    ans = "Y"

    for i in range(2, ran1):
        if ran1 % 2 == 0:
            ans = "N"
            break
    else:
        ans = "Y"

    userChoice = input("\nIs {} a prime number (Y/N) : ".format(ran1))

    if userChoice == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print()
        return answer, level

def PowerOf(answer, level):

    # Data
    index = 1 * (level - 201)

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    ans = ran1 ** ran2

    userNumber = int(input("\n{} ^ {} : ".format(ran1, ran2)))

    if userNumber == ans:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{} ^ {} : {}".format(ran1, ran2, ans))
        print()
        return answer, level

def log(answer, level):

    # Data
    index = 1 * (level - 211)

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    power = ran1 ** ran2

    randomChoice = random.randint(1, 3)

    if randomChoice == 1:
        userNumber = int(input("log {}, {} : ".format(power, ran1)))
        ans = math.log(power, ran1)

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("log {}, {} : {}".format(power, ran1, ans))
            print()
            return answer, level
    else:
        userNumber = int(input("log {}, {} : ".format(power, ran2)))
        ans = math.log(power, ran2)

        if userNumber == ans:
            print("\nCorrect")
            print()
            return answer, level
        else:
            print("\nWrong")
            print("log {}, {} : {}".format(power, ran2, ans))
            print()
            return answer, level

def factorial(answer, level):

    # Data
    index = 1 * (level - 1001)

    ran1 = random.randint(1, index)
    ans = 1

    while ran1 != 1:
        ans *= ran1
        ran1 -= 1

    userNumber = int(input("\n{} factorial : ".format(ran1)))

    if userNumber == ran1:
        print("\nCorrect")
        print()
        return answer, level
    else:
        print("\nWrong")
        print("{}! : {}".format(ran1, ans))
        print()
        return answer, level


