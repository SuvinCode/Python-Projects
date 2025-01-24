"""
This game is the Hunger Game Simulator.

- Characters
- Kill Action
- Kill Action but gets himself killed instead
"""

# Import modules
from Hunger_Games_Simulation.Settings.Arctic import arctic
from Hunger_Games_Simulation.Settings.Dessert import dessert
from Hunger_Games_Simulation.Settings.Jungle import jungle


# Data
characterLst = []
doneLst = ["Done", "done"]

# Settings
arcticLst = ["1", "Arctic", "arctic", "Cold", "cold", "art", "Art", "A", "a"]
dessertLst = ["2", "Dessert", "dessert", "dess", "Dess", "d", "Hot", "hot", "D"]
jungleLst = ["3", "Jungle", "jungle", "Jung", "jung", "jun", "Jun", "J", "j"]

# Introduction
print("\n------------------------HUNGER GAMES-----------------------------------")
print("\nWelcome to the Hunger Games.")
print("\nThe objective of this game is, you as the user will enter in the characters that you want. ")
print("The last character that is still standing wins tha game.")
print("This game highly depends on luck.")
print("It is recommended to enter more than 10 characters for a fun and entertaining round.")
print("This game was absurdly inspired by Technoblade's Hunger Games. ")

print()

# Character Initializing

while True:
    userCharacter = input("Enter a character (Type 'done' when you are finish) : ")

    if userCharacter in doneLst:
        break
    else:
        characterLst.append(userCharacter)

# Choose the Setting
print("\nHere are the available settings for the Hunger Games that can be used:")

print("\n1. Arctic")
print("2. Dessert")
print("3. Jungle")

userSetting = input("\nEnter your setting for the Hunger Games : ")

if userSetting in arcticLst:
    arctic(characterLst)
elif userSetting in dessertLst:
    dessert(characterLst)
elif userSetting in jungleLst:
    jungle(characterLst)