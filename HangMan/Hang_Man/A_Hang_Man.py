#Import modules

from HangMan.Hang_Man.B_Countries import  countries
from HangMan.Hang_Man.C_FruitsVegetables import fruitsVegetables
from HangMan.Hang_Man.D_Cars import car
from HangMan.Hang_Man.E_PeriodicTable import periodicTable
from HangMan.Hang_Man.F_Currency import money
from HangMan.Hang_Man.G_Geohazard import Geohazard
from HangMan.Hang_Man.H_HarryPotterSpells import Harry_Potter_Spells
from time import sleep

# Data
chances = 10
enumerator = 0
letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letterUsed = []
country = ["1", "country", "Country", "COUNTRY"]
fruitVegetables = ["2", "Fruit", "Vegetables", "fruit", "vegetables", "fruitvegtables", "FruitVegetables", "FRUITVEGETABLES"]
cars = ["3", "Car", "Cars", "car", "Car"]
table = ["4", "Periodic table", "periodic table", "PERIODIC TABLE", "periodictable", "PERIODICTABLE"]
currency = ["5", "currency", "CURRENCY", "Currency"]
geohazard = ["6", "geohazard", "Geohazard", "GEOHAZARD", "hazard", "HAZARD", "Hazard"]
spells = ["7", "Spells", "spells", "harry potter spells", "Harry Potter Spells", "harry potter", "Harry Potter", "SPELLS", "HARRY POTTER SPELLS", "HARRY POTTER"]

# Getting a replacer
def replacer(s, newstring, index):
    # if not error, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


# Introduction
print("----HANGMAN----- [ALL WORDS WILL BE CAPITALSED]")

print("\nWelcome to hangman!")
print("There are choices that you can pick")

print("\nChoices : ")
print("\n1. COUNTRIES")
print("2. FRUITS AND VEGETABLES")
print("3. CARS")
print("4. PERIODIC TABLE")
print("5. CURRENCY")
print("6. GEOHAZARD")
print("7. HARRY POTTER SPELLS")

userInput = input("\nEnter your choice : ")

# Give a word
word = ""

# Choice

if userInput in country:
    word = countries(word)
elif userInput in fruitVegetables:
    word = fruitsVegetables(word)
elif userInput in cars:
    word = car(word)
elif userInput in table:
    word = periodicTable(word)
elif userInput in currency:
    word = money(word)
elif userInput in geohazard:
    word = Geohazard(word)
elif userInput in spells:
    word = Harry_Potter_Spells(word)


# Getting the number of blanks
blanks = ""


for j in word:
    if j == " ":
        blanks += " "
    else:
        blanks += "_"

# Getting the introduction

print()
print("Number of chances :", chances)
print("Letters used :", letterUsed)
print()
print(blanks)

while True:

    identifier = True

    alphabet = input("\nEnter an alphabet : ")

    if alphabet in letterUsed:
        identifier = False

    if alphabet in letter and identifier == True:
        letterUsed.append(alphabet)
        if alphabet in word:
            for i in range(0, len(word)):
                if word[i] == alphabet:
                    blanks = replacer(blanks, alphabet, i)
                    enumerator += 1
    else:
        enumerator += 1

    if enumerator == 0:
        chances -= 1


    print()
    print("Number of chances :", chances)
    print("Letter used :", letterUsed)
    print()
    print(blanks)

    enumerator = 0

    if blanks == word:
        print("\nYou won!")
        break

    if chances == 0:

        print("\n\n\n\n\n\n\n")

    # Hangman Printing

        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("     |")
        print("=========''']")
        print("\n\n\n\n\n\n\n\n\n")

        sleep(1)

        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("=========''']")
        print("\n")

        print("\nYou lose!")
        print("The answer was :", word)
        print("\n\n")

        break



