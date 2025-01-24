# Import modules
import random

# Addition Function

def addition(answer, index):
    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    ans = ran1 + ran2

    userNumber = int(input("{} + {} : ".format(ran1, ran2)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index

# Substraction Function

def substraction(answer, index):

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)

    if ran1 > ran2:

        ans = ran1 - ran2

        userNumber = int(input("{} - {} : ".format(ran1, ran2)))


        if userNumber == ans:
            return answer, index
        else:
            answer = False
            return answer, index
    else:
        ans = ran2 - ran1

        userNumber = int(input("{} - {} : ".format(ran2, ran1)))

        if userNumber == ans:
            return answer, index
        else:
            answer = False
            return answer, index

# Multiplication Function

def multiplication(answer, index):

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    ans = ran1 * ran2

    userNumber = int(input("{} X {} : ".format(ran1, ran2)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index

# Division Function

def division(answer, index):

    ran1 = random.randint(1, index)
    ran2 = random.randint(1, index)
    multiple_ans = ran1 * ran2

    division_ran = random.randint(1, 3)

    if division_ran == 1:
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran1)))
        ans = multiple_ans / ran1

        if userNumber == ans:
            return answer, index
        else:
            answer = False
            return answer, index
    else:
        ans = multiple_ans / ran2
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran2)))

        if userNumber == ans:
            return answer, index
        else:
            answer = False
            return answer, index


# Square Function

def square(answer, index):
    ran1 = random.randint(1, index)
    ans = ran1 ** 2

    userNumber = int(input("{} ^ 2 : ".format(ran1)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index

# SquareRoot Fnction

def squareroot(answer, index):

    ran1 = random.randint(1, index)
    square_ans = ran1 ** 2
    ans = ran1

    userNumber = int(input("{} Squarerooted : ".format(square_ans)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index

# Cube Function

def cube(answer, index):
    ran1 = random.randint(1, index)

    ans = ran1 ** 3

    userNumber = int(input("{} ^ 3 : ".format(ran1)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index

def cuberoot(answer, index):

    ran1 = random.randint(1, index)
    square_ans = ran1 ** 3
    ans = ran1

    userNumber = int(input("{} Cuberooted : ".format(square_ans)))

    if userNumber == ans:
        return answer, index
    else:
        answer = False
        return answer, index




