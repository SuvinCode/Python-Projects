# Importing files
from Black_Jack.BlackJack.B_AgaintsBot import fight_bot

# Data
bot = ["1", "AGAINST BOT", "Against bot", "against bot", "Bot", "BOT", "bot"]

# Introduction
print("-----BLACK JACK-------")

print("\nWelcome to black jack which is a ard game based n luck and strategical thinking.")
print("Black Jack will be using a deck of poker cards to play.")
print("Each card has a different value each game which are : ")

print("\nCARD VALUES : ")
print("\nA[A] - 11 points as the first card but 1 in the others")
print("King[K] - 10 points.")
print("queen[Q] - 10 points.")
print("Jack[J] - 10 points.")
print("10[10] - 10 points.")
print("9[9] - 9 points.")
print("8[8] - 8 points.")
print("7[7] - 7 points.")
print("6[6] - 6 points.")
print("5[5] - 5 points.")
print("4[4] - 4 points.")
print("3[3] - 3 points.")
print("2[2] - 2 points.")

print("\nThere are many modes in this game which are : ")
print("\n1. AGAINST BOT")

userChoice = input("\nEnter in your choice : ")

if userChoice in bot:
    fight_bot()
