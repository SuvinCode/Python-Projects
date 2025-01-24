# Importing random
from random import randint
from time import sleep

# Data

# User Choice
noLst = ["No", "no", "N", "n"]
change = None
userLst = []
pointsLst = []
endingIndex = 0

# Choices [Upper section]
acesChoices = ["Aces", "aces", "Ace", "ace", "Ones", "ones", "One", "one", "1"]
twosChoices = ["Twos", "twos", "Two", "two", "2"]
threesChoices = ["Threes", "threes", "Three", "three", "3"]
foursChoices = ["Fours", "fours", "Four", "four", "4"]
fivesChoices = ["Fives", "fives", "Five", "five", "5"]
sixesChoices = ["Sixes", "sixes", "Six", "six", "6"]

# Choices [Lower section]
threeKindChoices = ["3 of a kind", "Three of a kind", "3OAK", "Kind Three", "kind three", "Kind three", "kind Three"]
fourKindChoices = ["4 of a kind", "Four of a kind", "4OAK", "KInd Four", "kind four", "Kind four", "kind Four"]
fullHouseChoices = ["Full House", "full House", "Full House", "full house", "FH"]
smallStraightChoices = ["Small Straight", "Small straight", "small Straight", "small straight", "SS"]
largeStraightChoices = ["Large Straight", "Large straight", "large Straight", "large straight", "LS"]
yathzeeChoices = ["Yathzee", "yathzee", "Y"]
chanceChoices = ["Chance", "chance", "chances", "C"]

total = 0
upper_totalScore = 0
lower_totalScore = 0
grand_totalScore = 0
userChoice = None

fullHouseLst = [
    [1, 1, 1, 2, 2],
    [1, 1, 1, 3, 3],
    [1, 1, 1, 4, 4],
    [1, 1, 1, 5, 5],
    [1, 1, 1, 6, 6],
    [1, 1, 2, 2, 2],
    [1, 1, 3, 3, 3],
    [1, 1, 4, 4, 4],
    [1, 1, 5, 5, 5],
    [1, 1, 6, 6, 6],
    [2, 2, 2, 3, 3],
    [2, 2, 2, 4, 4],
    [2, 2, 2, 5, 5],
    [2, 2, 2, 6, 6],
    [2, 2, 3, 3, 3],
    [2, 2, 4, 4, 4],
    [2, 2, 5, 5, 5],
    [2, 2, 6, 6, 6],
    [3, 3, 3, 4, 4],
    [3, 3, 3, 5, 5],
    [3, 3, 3, 6, 6],
    [3, 3, 4, 4, 4],
    [3, 3, 5, 5, 5],
    [3, 3, 6, 6, 6],
    [4, 4, 4, 5, 5],
    [4, 4, 4, 6, 6],
    [4, 4, 5, 5, 5],
    [4, 4, 6, 6, 6],
    [5, 5, 5, 6, 6],
    [5, 5, 6, 6, 6]
                ]

diceNumbers = []
firstNumber = None
secondNumber = None
thirdNumber = None
fourthNumber = None
fifthNumber = None
turn = 1
roll = 1
noneLst = ["None", "none", "No", "no", "N", "n"]
countingIndex = 0
availableChoices = []

# Upper Section
aces = []
twos = []
threes = []
fours = []
fives = []
sixes = []
upperTotal = []
current_upperTotal = []
bonusScore = []

# Lower Section
threeKind = []
fourKind = []
fullHouse = []
smallStraight = []
largeStraight = []
yathzee = []
chance = []
lowerTotal = []
grandTotal = []

# Introduction
print("\n---------YATHZEE------------")
sleep(1)

print("\nWelcome to the game, Yathzee. This game can be played by countless numbers of people.")
sleep(1)

print("\n---------RULES--------------")
sleep(1)

print("\n1. Roll 5 dices")
sleep(1)
print("2. Roll up to 3 times each turn to rack up the best possible score.")
sleep(1)
print("3. You can choose which dice you want to roll again by entering the dice number position but it is up to 3 turns.")
sleep(1)
print("4. Decide which dice combo you're going for.")
sleep(1)
print("5. If you get the exact combo you need, enter none to stop the loop.")
sleep(1)
print("6. However, if you have done 3 rolls, the program will stop you from making any more rolls.")
sleep(1)
print("7. The program will then give you the available combos you can execute based on your dice numbers.")
sleep(1)
print("8. Your score will appear in the score box based on your dice combos.")
sleep(1)
print("9. After 13 rounds, the program will calculate your final score.")
sleep(1)
print("10. If they are any missing boxes that are unfilled, the program will count those boxes as zeros.")
sleep(1)
print("11. If a box is already filled in, you cannot fill in that box anymore although you scored that dice combo.")
sleep(1)
print("12. You get a bonus of 35 points if the total number of points you scored in the upper section is 63 or higher.")
sleep(1)

print("\n---------DICE COMBOS------------")
sleep(1)

print("\n1. ACES")

print("The aces combo can be executed if your number of aces / ones in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n2. TWOS")
print("The twos combo can be executed if your number of twos in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n3. THREES")
print("The threes combo can be executed if your number of threes in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n4. FOURS")
print("The fours combo can be executed if your number of fours in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n5. FIVES")
print("The fives combo can be executed if your number of fives in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n6. SIXES")
print("The sixes combo can be executed if your number of sixes in your dice numbers are more than 1.")
print("The points are determined by the number of ones you have in your dice number added up all together.")

sleep(1)

print("\n7. 3 OF A KIND")
print("The 3 of a kind box may be filled in only if the dice show at least 3 of the same number.")
print("The points are determined by the sum of the dice numbers.")

sleep(1)

print("\n8. 4 OF A KIND")
print("Score the total of all dice provided they include 4 dice of the same number.")
print("The points are determined by the sum of the dice numbers.")

sleep(1)

print("\n9. FULL HOUSE")
print("You need to roll both a 3 of a kind and a pair.")
print("A Full House scores 25 points.")

sleep(1)

print("\n10. SMALL STRAIGHT")
print("This dice combo can be executed if your dice numbers consist of 1, 2, 3, 4, 5")
print("A Small Straight scores 30 points.")

sleep(1)

print("\n11. LARGE STRAIGHT")
print("This dice combo can be executed if your dice numbers consist of 2, 3, 4, 5, 6")
print("A Large Straight scores 40 points.")

sleep(1)

print("\n12. CHANCE")
print("This offers a player the opportunity to score on any turn where he does not choose to score in any of the other open boxes.")
print("The points are determined by the sum of the dice numbers.")

sleep(1)

print("\n13. YATHZEE")
print("This is any five of a kind or get all five dice the same number")
print("Yathzee scores 50 points")
print("If you roll a Yahtzee and you already filled in the Yahtzee box with a 50, you get a 100-point bonus!")

sleep(1)

while True:
    userName = input("\nEnter your name : ")

    while turn < 14:
        print("\n\n\n----------Rounds :", turn, "--------------")

        firstNumber = randint(1, 6)
        secondNumber = randint(1, 6)
        thirdNumber = randint(1, 6)
        fourthNumber = randint(1, 6)
        fifthNumber = randint(1, 6)

        diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]
        print("\nDice Numbers :", diceNumbers)


        while True:
            change = input("\nEnter which numbers do you want to change (Enter 'none' if they are no numbers that you want to chane) : ")

            if change in noneLst:
                break
            else:
                roll += 1

            for i in change:
                if i == '1':
                    firstNumber = randint(1, 6)
                    diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]
                elif i == '2':
                    secondNumber = randint(1, 6)
                    diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]
                elif i == '3':
                    thirdNumber = randint(1, 6)
                    diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]
                elif i == '4':
                    fourthNumber = randint(1, 6)
                    diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]
                elif i == '5':
                    fifthNumber = randint(1, 6)
                    diceNumbers = [firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber]

            print("\nDice Numbers :", diceNumbers)

            if roll == 3:
                print("\nYour number of rolls and chances are up!!!!!")
                break

        print("\n\nFinal Dice Numbers :", diceNumbers)
        print("Sum of dice numbers :", sum(diceNumbers))


        firstCount = diceNumbers.count(diceNumbers[0])
        secondCount = diceNumbers.count(diceNumbers[1])
        thirdCount = diceNumbers.count(diceNumbers[2])
        fourthCount = diceNumbers.count((diceNumbers[3]))
        fifthCount = diceNumbers.count(diceNumbers[4])

        diceNumbers.sort()

        # Upper section

        if len(aces) == 0 and 1 in diceNumbers and diceNumbers.count(1) > 1:
                availableChoices.append("Aces")

        if len(twos) == 0 and 2 in diceNumbers and diceNumbers.count(2) > 1:
                availableChoices.append("Twos")

        if len(threes) == 0 and 3 in diceNumbers and diceNumbers.count(3) > 1:
                availableChoices.append("Threes")

        if len(fours) == 0 and 4 in diceNumbers and diceNumbers.count(4) > 1:
                availableChoices.append("Fours")

        if len(fives) == 0 and 5 in diceNumbers and diceNumbers.count(5) > 1:
                availableChoices.append("Fives")

        if len(sixes) == 0 and 6 in diceNumbers and diceNumbers.count(6) > 1:
                availableChoices.append("Sixes")

        # Lower section

        if len(threeKind) == 0:
            if firstCount >= 3 or secondCount >= 3 or thirdCount >= 3 or fourthCount >= 3 or fifthCount >= 3:
                availableChoices.append("3 of a kind")

        if len(fourKind) == 0:
            if firstCount >= 4 or secondCount >= 4 or thirdCount >= 4 or fourthCount >= 4 or fifthCount >= 4:
                availableChoices.append("4 of a kind")

        if diceNumbers in fullHouseLst and len(fullHouse) == 0:
            availableChoices.append("Full House")

        if diceNumbers == [2, 3, 4, 5, 6] and len(largeStraight) == 0:
            availableChoices.append("Large Straight")

        if firstNumber == secondNumber == thirdNumber == fourthNumber == fifthNumber:
            availableChoices.append("Yathzee")

        if diceNumbers == [1, 2, 3, 4, 5] and len(smallStraight) == 0:
            availableChoices.append("Small Straight")

        if len(chance) == 0:
                availableChoices.append("Chance")

        if len(availableChoices) > 0:
            print("\nAvailable Choices :", availableChoices)
            userChoice = input("\nEnter your choice : ")
        else:
            sleep(2)
            print("\nSorry there are no available choices")
            sleep(2)

        # Upper section

        if userChoice in acesChoices and len(aces) == 0 and 1 in diceNumbers and diceNumbers.count(1) > 1:
            for i in diceNumbers:
                if i == 1:
                    total += 1
            aces.append(total)

        elif userChoice in twosChoices and len(twos) == 0 and 2 in diceNumbers and diceNumbers.count(2) > 1:
            for i in diceNumbers:
                if i == 2:
                    total += 2
            twos.append(total)

        elif userChoice in threesChoices and len(threes) == 0 and 3 in diceNumbers and diceNumbers.count(3) > 1:
            for i in diceNumbers:
                if i == 3:
                    total += 3
            threes.append(total)

        elif userChoice in foursChoices and len(fours) == 0 and 4 in diceNumbers and diceNumbers.count(4) > 1:
            for i in diceNumbers:
                if i == 4:
                    total += 4
            fours.append(total)

        elif userChoice in fivesChoices and len(fives) == 0 and 5 in diceNumbers and diceNumbers.count(5) > 1:
            for i in diceNumbers:
                if i == 5:
                    total += 5
            fives.append(total)

        elif userChoice in sixesChoices and len(sixes) == 0 and 6 in diceNumbers and diceNumbers.count(6) > 1:
            for i in diceNumbers:
                if i == 6:
                    total += 6
            sixes.append(total)

        # Lower section

        elif userChoice in threeKindChoices and len(threeKind) == 0:
            if firstCount >= 3 or secondCount >= 3 or thirdCount >= 3 or fourthCount >= 3 or fifthCount >= 3:
                total = sum(diceNumbers)
                threeKind.append(total)

        elif userChoice in fourKindChoices and len(fourKind) == 0:
            if firstCount >= 4 or secondCount >= 4 or thirdCount >= 4 or fourthCount >= 4 or fifthCount >= 4:
                total = sum(diceNumbers)
                fourKind.append(total)

        elif userChoice in fullHouseChoices and len(fullHouse) == 0 and diceNumbers in fullHouseLst:
            fullHouse.append(25)

        elif userChoice in largeStraightChoices and len(largeStraight) == 0 and diceNumbers == [2, 3, 4, 5, 6]:
            largeStraight.append(40)

        elif userChoice in yathzeeChoices and firstNumber == secondNumber == thirdNumber == fourthNumber == fifthNumber:
            if len(yathzee) == 0:
                yathzee.append(50)
            else:
                yathzee[0] += 100

        elif userChoice in smallStraightChoices and len(smallStraight) == 0 and diceNumbers == [1, 2, 3, 4, 5]:
                smallStraight.append(30)

        elif userChoice in chanceChoices and len(chance) == 0:
            chance.append(sum(diceNumbers))

        print("\nName :", userName)

        print("\nUpper Section")
        print("Count and add only Aces         :", aces)
        print("Count and add only Twos         :", twos)
        print("Count and add only Threes       :", threes)
        print("Count and add only Fours        :", fours)
        print("Count and add only Fives        :", fives)
        print("Count and add only Sixes        :", sixes)
        print("Total                           :", current_upperTotal)
        print(" 63 + scores a 35 Bonus         :", bonusScore)
        print("Total of Upper Section          :", upperTotal)

        print("\nLower Section")
        print("3 of a kind (Total of all dice) :", threeKind)
        print("4 of a kind (Total of all dice) :", fourKind)
        print("Full House                      :", fullHouse)
        print("Small Straight                  :", smallStraight)
        print("Large Straight                  :", largeStraight)
        print("Yathzee                         :", yathzee)
        print("Chance (Total of all dice)      :", chance)
        print("Total of Upper Section          :", upperTotal)
        print("Total of Lower Section          :", lowerTotal)

        print("\nGrand Total                   :", grandTotal)

        roll = 1
        availableChoices.clear()
        turn += 1
        total = 0

    if len(aces) == 0:
        aces.append(0)

    if len(twos) == 0:
        twos.append(0)

    if len(threes) == 0:
        threes.append(0)

    if len(fours) == 0:
        fours.append(0)

    if len(fives) == 0:
        fives.append(0)

    if len(sixes) == 0:
        sixes.append(0)

    if len(threeKind) == 0:
        threeKind.append(0)

    if len(fourKind) == 0:
        fourKind.append(0)

    if len(fullHouse) == 0:
        fullHouse.append(0)

    if len(smallStraight) == 0:
        smallStraight.append(0)

    if len(largeStraight) == 0:
        largeStraight.append(0)

    if len(yathzee) == 0:
        yathzee.append(0)

    if len(chance) == 0:
        chance.append(0)

    # Calculation of the score

    upper_totalScore = aces[0] + twos[0] + threes[0] + fours[0] + fives[0] + sixes[0]
    current_upperTotal.append(upper_totalScore)

    if upper_totalScore >= 63:
        upper_totalScore += 35
        bonusScore.append(35)

    upperTotal.append(upper_totalScore)

    lower_totalScore = threeKind[0] + fourKind[0] + fullHouse[0] + smallStraight[0] + largeStraight[0] + yathzee[0] + chance[0]
    lowerTotal.append(lower_totalScore)

    grand_totalScore = upper_totalScore + lower_totalScore
    grandTotal.append(grand_totalScore)

    # Final

    print("\nName :", userName)

    print("\nUpper Section")
    print("Count and add only Aces         :", aces)
    print("Count and add only Twos         :", twos)
    print("Count and add only Threes       :", threes)
    print("Count and add only Fours        :", fours)
    print("Count and add only Fives        :", fives)
    print("Count and add only Sixes        :", sixes)
    print("Total                           :", current_upperTotal)
    print(" 63 + scores a 35 Bonus         :", bonusScore)
    print("Total of Upper Section          :", upper_totalScore)

    print("\nLower Section")
    print("3 of a kind (Total of all dice) :", threeKind)
    print("4 of a kind (Total of all dice) :", fourKind)
    print("Full House                      :", fullHouse)
    print("Small Straight                  :", smallStraight)
    print("Large Straight                  :", largeStraight)
    print("Yathzee                         :", yathzee)
    print("Chance (Total of all dice)      :", chance)
    print("Total of Upper Section          :", upper_totalScore)
    print("Total of Lower Section          :", lower_totalScore)

    print("\nGrand Total                   :", grandTotal)

    userLst.append(userName)
    pointsLst.append(grandTotal)

    userContinue = input("\nDo you want to continue (Y/N) : ")

    if userContinue in noLst:

        while len(userLst) > endingIndex:
                print(userLst[endingIndex], ":", pointsLst[endingIndex], "points")
                endingIndex += 1
    else:
        total = 0
        upper_totalScore = 0
        lower_totalScore = 0
        grand_totalScore = 0
        diceNumbers = []
        firstNumber = None
        secondNumber = None
        thirdNumber = None
        fourthNumber = None
        fifthNumber = None
        turn = 1
        roll = 1
        countingIndex = 0
        availableChoices.clear()
        aces.clear()
        twos.clear()
        threes.clear()
        fours.clear()
        fives.clear()
        sixes.clear()
        upperTotal.clear()
        current_upperTotal.clear()
        bonusScore.clear()
        threeKind.clear()
        fourKind.clear()
        fullHouse.clear()
        smallStraight.clear()
        largeStraight.clear()
        yathzee.clear()
        chance.clear()
        lowerTotal.clear()
        grandTotal.clear()
        availableChoices.clear()
        change = None


