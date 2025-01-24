# Import modules
import random

# Import files
from .B_Level_Type_MathFunctions import *

# Level 1 - 5

def level_1_5(answer, level):
    answer, level = addition(answer, level)
    return answer, level

# Level 6 - 10

def level_6_10(answer, level):
    ran1 = random.randint(1, 2)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    else:
        answer, level = substraction(answer, level)
        return answer, level

# Level 10 - 15

def level_11_15(answer, level):
    ran1 = random.randint(1, 4)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    else:
        answer, level = multiplication(answer, level)
        return answer, level

# Level 16 - 20

def level_16_20(answer, level):
    ran1 = random.randint(1, 5)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    else:
        answer, level = division(answer, level)
        return answer, level

def level_21_25(answer, level):
    ran1 = random.randint(1, 6)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    else:
        answer, level = square(answer, level)
        return answer, level

def level_26_30(answer, level):
    ran1 = random.randint(1, 7)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    else:
        answer, level = squareroot(answer, level)
        return answer, level

def level_31_35(answer, level):
    ran1 = random.randint(1, 8)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    else:
        answer, level = cube(answer, level)
        return answer, level

def level_36_40(answer, level):
    ran1 = random.randint(1, 9)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    else:
        answer, level = cuberoot(answer, level)
        return answer, level

def level_41_50(answer, level):
    ran1 = random.randint(1, 10)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    elif ran1 == 8:
        answer, level = cuberoot(answer, level)
        return answer, level
    else:
        answer, level = addAllDigits(answer, level)
        return answer, level

def level_200_210(answer, level):
    ran1 = random.randint(1, 14)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    elif ran1 == 8:
        answer, level = cuberoot(answer, level)
        return answer, level
    elif ran1 == 9:
        answer, level = addAllDigits(answer, level)
        return answer, level
    elif ran1 == 10:
        answer, level = IsAPrimeNumber(answer, level)
        return answer, level
    else:
        answer, level = PowerOf(answer, level)
        return answer, level

def level_51_60(answer, level):
    ran1 = random.randint(1, 13)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    elif ran1 == 8:
        answer, level = cuberoot(answer, level)
        return answer, level
    elif ran1 == 9:
        answer, level = addAllDigits(answer, level)
        return answer, level
    else:
        answer, level = IsAPrimeNumber(answer, level)
        return answer, level

def level_211_220(answer, level):
    ran1 = random.randint(1, 15)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    elif ran1 == 8:
        answer, level = cuberoot(answer, level)
        return answer, level
    elif ran1 == 9:
        answer, level = addAllDigits(answer, level)
        return answer, level
    elif ran1 == 10:
        answer, level = IsAPrimeNumber(answer, level)
        return answer, level
    elif ran1 == 11:
        answer, level = PowerOf(answer, level)
        return answer, level
    else:
        answer, level = log(answer, level)
        return answer, level

def level_1000_1010(answer, level):
    ran1 = random.randint(1, 16)

    if ran1 == 1:
        answer, level = addition(answer, level)
        return answer, level
    elif ran1 == 2:
        answer, level = substraction(answer, level)
        return answer, level
    elif ran1 == 3:
        answer, level = multiplication(answer, level)
        return answer, level
    elif ran1 == 4:
        answer, level = division(answer, level)
        return answer, level
    elif ran1 == 5:
        answer, level = square(answer, level)
        return answer, level
    elif ran1 == 6:
        answer, level = squareroot(answer, level)
        return answer, level
    elif ran1 == 7:
        answer, level = cube(answer, level)
        return answer, level
    elif ran1 == 8:
        answer, level = cuberoot(answer, level)
        return answer, level
    elif ran1 == 9:
        answer, level = addAllDigits(answer, level)
        return answer, level
    elif ran1 == 10:
        answer, level = IsAPrimeNumber(answer, level)
        return answer, level
    elif ran1 == 11:
        answer, level = PowerOf(answer, level)
        return answer, level
    elif ran1 == 12:
        answer, level = log(answer, level)
        return answer, level
    else:
        answer, level = factorial(answer, level)
        return answer, level



