# Import random
import random

def fight_bot():
    # Data
    cardTakingPositive = ["Y", "Yes"]
    cardDeck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    botPoints = 0
    userPoints = 0
    userDeck = []
    userValue = 0
    botValue = 0
    botDeck = []
    round_n = 1
    valueArray = []
    A_Counter = 1

    # Most frequent element in a list function

    def most_frequent(List):
        counter = 0
        num = List[ 0 ]

        for i in List:
            curr_frequency = List.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i

        return num

    # Card Identifier Function

    def CardIdentifier(card, value, deck):
        if card == "A":
            for i in deck:
                if deck[0] == "A":
                    value += 11
                    return card, value, deck
            else:
                value += 1
                return card, value, deck
        elif card == 2:
            value += 2
            return card, value, deck
        elif card == 3:
            value += 3
            return card, value, deck
        elif card == 4:
            value += 4
            return card, value, deck
        elif card == 5:
            value += 5
            return card, value, deck
        elif card == 6:
            value += 6
            return card, value, deck
        elif card == 7:
            value += 7
            return card, value, deck
        elif card == 8:
            value += 8
            return card, value, deck
        elif card == 9:
            value += 9
            return card, value, deck
        elif card == 10 or "J" or "K":
            value += 10
            return card, value, deck
        elif card == "A":
            if deck[0] == "A":
                value += 11
            else:
                value += 1
                return card, value, deck



    # Introduction

    print("\nIn this mode, you will be fighting against a bot that is also playing black jack.")
    print("You will be given a two cards each and there is no timer.")

    # Ready Identifier
    userRound = int(input("\nHow many rounds do you want : "))

    while userRound != 0:

        print("\n\n-------Round", round_n, "-------------")

        # Process of Black Jack

        for i in range(2):
            randomCard = random.choice(cardDeck)
            userDeck.append(randomCard)

        for j in range(2):
            randomCard = random.choice(cardDeck)
            botDeck.append(randomCard)

        # Printing the deck of cards
        print("\nYour deck :", userDeck)

        # User taking a card
        userCardChoice = input("\nDo you want to add another card : [Y/N] : ")

        while userCardChoice in cardTakingPositive:
            if userCardChoice in cardTakingPositive:
                A_Counter += 1
                randomCard = random.choice(cardDeck)
                userDeck.append(randomCard)
                print("\nYour deck :", userDeck)
                userCardChoice = input("\nDo you want to add another card : [Y/N] : ")

        A_Counter = 1

        # Bot taking a card

        for card in botDeck:
            card, botValue, A_Counter = CardIdentifier(card, botValue, botDeck)

        while botValue < 15:
            randomBotChoice = random.choice(cardDeck)
            botDeck.append(randomBotChoice)
            botValue = 0

            for card in botDeck:
                card, botValue, A_Counter = CardIdentifier(card, botValue, botDeck)

        A_Counter = 1

        # Value check

        for card in userDeck:
            card, userValue, A_Counter = CardIdentifier(card, userValue, userDeck)

        # Finalizing

        if userValue > 21 and botValue > 21:
            print("\nTie")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            print("\nUser Points :", userPoints, "Bot Points :", botPoints)

        elif userValue > 21:
            print("\nYou lose")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            botPoints += 1

            print("\nUser Points :", userPoints, "Bot Points :", botPoints)
        elif botValue > 21:
            print("\nYou win")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            userPoints += 1

            print("\nUser Points :", userPoints, "Bot Points :", botPoints)

        elif userValue > botValue and userValue < 22:
            print("\nYou win")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            userPoints += 1

            print("\nUser Points :", userPoints, "Bot Points :", botPoints)

        elif botValue > userValue and botValue < 22:
            print("You lose")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            botPoints += 1

            print("\nUser Points :", userPoints, "Bot Points :", botPoints)
        elif userValue == botValue:
            print("\nTie")
            print("Your card deck :", userDeck)
            print("The robot's deck :", botDeck)
            print("\nUser Points :", userPoints, "Bot Points :", botPoints)


        valueArray.append(userValue)

        A_Counter = 0
        userValue = 0
        botValue = 0
        userDeck.clear()
        botDeck.clear()
        round_n += 1
        userRound -= 1

    print("\n\n------Total Results------")

    if userPoints > botPoints:
        print("\nYOU WON THE ENTIRE GAME!.")
    elif botPoints > userPoints:
        print("\nYOU LOSE THE ENTIRE GAME!")
    else:
        print("\nTIE")

    if botPoints == 0:
        botPoints = 1
        print("Win loss  Ratio [WLR]:", userPoints / botPoints)
    else:
        print("Win loss Ratio [WLR]:", userPoints / botPoints)
    print("Highest value :", max(valueArray))
    print("Lowest value :", min(valueArray))
    print("Most frequent value :", most_frequent(valueArray))


