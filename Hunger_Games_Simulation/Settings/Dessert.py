# Import random
from random import choice, randint
from time import sleep

# Dessert Function
def dessert(characters):

    # Data
    rounds = 1
    subrounds = 0
    accidentalKill = 0
    purposeKill = 0

    # Weapons

    stabbingWeapon = [
                     "knife",
                     "mallet",
                     "thorns",
                     "cactus",
                     "stone",
                     "sandstone",
                     "cleaver",
                     "dagger",
                     "crowbar"
    ]

    rangeWeapons = [
                    "bow",
                    "crossbow"
    ]

    throwingItems = [
                    "stone",
                    "sand",
                    "shurikens",
                    "sandstone"
    ]

    suffocationItems = [
                        "sand",
                        "mud",
                        "rope"
    ]

    # Animals

    poisonousAnimals = [
                      "rattlesnake",
                      "scorpion",
                      "dessert Scorpian",
                      "cobra",
                      "king cobra"
    ]

    swarmAnimals = [
                    "fire Ants",
                    "vultures",
                    "foxes",
                    "termites"
    ]

    # Deaths

    natureDeathLst = [
                       "{player} became an idiot and was pricked to death by a cactus.",
                       "{player} became drunk and fell into a ravine.",
                       "{player} proceeds to climb a tree and fall to {player} death.",
                       "{player} died of thirst.",
                       "{player} died of hunger.",
                       "{player} tries to stomp on {animal} but instead gets poisoned by the {animal}.",
                       "{player} got swarmed by {animal}",
                       "{player} tried to act like an ostrich and decided to put head in the sand and suffocates to death.",
                       "{player} tried to tame a camel but gets kicked to death by that camel",
                       "{player} finds a river but drowns instead.",
                       "{player} burns to death while trying to light a fire.",
                       "{player} tried to eat a cactus for hunger but dies from getting pricked instead",
                       "{player} fell into quicksand and died.",
                       "{player} got killed by a sandstorm",
                       "{player}'s toe got stubbed and {player} fell over a cactus."
    ]

    killLst = [
                "{player1} stabs {player2} using a {weapon}.",
                "{player1} shoots {player2} using a {weapon}.",
                "{player1} pushed {player2} off the cliff.",
                "{player1} suffocates {player2} using {suffocation}.",
                "{player1} kept on throwing {throw} at {player2} until {player2} dies",
                "{player1} jumped at {player2} immediately killing {player2} from suffocation",
                "{player1} ambushes {player2} immediately killing {player2}",
                "{player1} broke {player2} nose making {player2} die out of breath",
                "{player1} broke {player2}'s head"
    ]


    nonKillLst = [
        "{player1} gathers food and water.",
        "{player1} hides in a hole.",
        "{player1} lies down and rest under the sunset",
        "{player1} meditates",
        "{player1} tries to quit the hunger games but was forced back in.",
        "{player1} tried to solve world hunger but forgets that he was in a hunger game.",
        "{player1} tries to call for help",
        "{player1} stared at the skies",
        "{player1} tries to find a water source",
        "{player1} tries to get WiFi.",
        "{player1} tries to find a buried treasure in the sand",
        "{player1} grabs an abandoned backpack, not realizing it's empty"
    ]

    stupidDeaths = [
        "{player1} tried to bribe {player2} but fails and get murdered instead.",
        "{player1} tried to team with {player2} but {player2} backstabs {player1} by stabbing {player1}.",
        "{player1} wanted everyone to be peaceful and harmonious but everyone teamed against {player1} and kill {player1}."

    ]

    sparesLife = [
        "{player1} wants to kill {player2} but spares him instead",
        "{player1} almost kills {player2} but {player1} didn't have the heart too."
    ]

    injuredPositive = [
        "{player2} found {player1} injured. {player1} begs for {player2} to end him but {player2} left him so that he can suffer",
        "{player2} found {player1} injured. {player1} begs for {player2} to end him but {player2} didn't have the heart to."
    ]

    injuredNegative = [
        "{player2} found {player1} injured. {player2} ends {player1}'s misery",
        "{player2} found {player1} injured and {player2} felt bad so {player2} ended his misery",
        "{player2} found {player1} injured and got a free kill"
    ]

    goodInjuredEnding = [
        "After getting injured, {player1} healed and stood back up",
        "After getting injured, {player1} didn't give up and move on"
    ]

    badInjuredEnding = [
        "After getting injured, {player1} decided to end the suffering",
        "After getting injured, {player1} decided to jump off a cliff"
    ]

    # Introduction

    print("\n\n")

    print("   .     _    +     .  ______   .          .  ")
    print("(       /|\      .    |      \      .   +     ")
    print("    .  |||||     _    | |   | | ||         .  ")
    print(".      |||||    | |  _| | | | |_||    .      ")
    print("   /\  ||||| .  | | |   | |      |       .   ")
    print("__||||_|||||____| |_|_____________\__________")
    print(". |||| |||||  /\   _____      _____  .   .   ")
    print("  |||| ||||| ||||   .   .  .         ________")
    print(" . \|`-'|||| ||||    __________       .    . ")
    print("    \__ |||| ||||      .          .     .    ")
    print("__    ||||`-'|||  .       .    __________    ")
    print(".    . |||| ___/  ___________             .  ")
    print("   . _ ||||| . _               .   _________ ")
    print("_   ___|||||__  _ \\--//    .          _     ")
    print("     _ `---'    .)=\oo|=(.   _   .   .    .  ")
    print("_  ^      .  -    . \.|                      ")




    print("\nWelcome to the dessert, a hot and dry wasteland filled with formidable animals and unexpected traps. Only cactus roams here.")

    userReady = input("\nPress anything to began the simulation.")

    print()

    # Simulation Starting
    print(" (                                 _")
    print("  )                               /=>")
    print(" (  +____________________/\/\___ / /|")
    print("  .''._____________'._____      / /|/\\")
    print("  : () :              :\ ----\|    \ )")
    print("  '..'______________.'0|----|      \\")
    print("                   0_0/____/        \\")
    print("                       |----    /----\\")
    print("                      || -\\ --|      \\")
    print("                      ||   || ||\      \\")
    print("                       \\____// '|      \\")
    print("Bang! Bang!                     .'/       |")
    print("                               .:/        |")
    print("                               :/_________|")

    print("\nTRUMPETS BLEW AND GUNS WERE FIRED. THE LAST MAN THAT SURVIVES THIS HUNGER GAMES WINS!!!")

    while True:


        sleep(10)

        if len(characters) == 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("+88_________________+880_______")
            print("_+880_______________++80_______")
            print("_++88______________+880________")
            print("_++88_____________++88________")
            print("__+880___________++88_________")
            print("__+888_________++880__________")
            print("__++880_______++880___________")
            print("__++888_____+++880____________")
            print("__++8888__+++8880++88_________")
            print("__+++8888+++8880++8888________")
            print("___++888++8888+++888888+80____")
            print("___++88++8888++8888888++888___")
            print("___++++++888888fx88888888888___")
            print("____++++++88888888888888888___")
            print("____++++++++000888888888888___")
            print("_____+++++++00008f8888888888___")
            print("______+++++++00088888888888___")
            print("_______+++++++0888f8888888")

            print("\nCongrats {} for being the last survivor!".format(characters[0]))

            print("\n\n--------RESULTS---------------")
            print("\nAccidental Kills :", accidentalKill)
            print("Purpose Kills:", purposeKill)
            break

        if subrounds % 3 == 0:
            print("\n\n\n---------Rounds {}-----------".format(rounds))

        if rounds > 0 and rounds < 3:

            chancesofDeath = [1, 10]

        elif rounds >= 3 and rounds < 5:

            chancesofDeath = [1, 5]

        elif rounds >= 5 and rounds < 8:

            chancesofDeath = [1, 3]

        else:
            chancesofDeath = [1, 2]

        killorDeath = choice(chancesofDeath)

        if killorDeath == chancesofDeath[-1]:

            if rounds > 0 and rounds < 3:
                probability = ["Nature death", "Nature death", "Nature death", "Nature death","Nature death", "Nature death","Nature death",
                               "Nature death", "Nature Death", "Kill"]

                killDeath = choice(probability)

            elif rounds >= 3 and rounds < 5:
                probability = ["Nature death", "Nature death", "Nature death", "Kill", "Kill",
                                "Kill", "Kill",
                                "Kill", "Spare life", "Kill"]

                killDeath = choice(probability)

            else:
                probability = ["Nature death", "Kill", "Kill", "Kill", "Kill",
                                "Kill", "Kill",
                                "Spare life", "Spare life", "Kill"]

                killDeath = choice(probability)

            if killDeath == "Nature death":
                natureDeath = choice(natureDeathLst)

                player1 = choice(characters)

                if "stomp" in natureDeath:

                    randomPoisonousAnimal = choice(poisonousAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomPoisonousAnimal))
                    characters.remove(player1)
                    natureDeathLst.remove(natureDeath)
                    accidentalKill += 1

                elif "swarmed" in natureDeath:

                    randomSwarmAnimal = choice(swarmAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomSwarmAnimal))
                    characters.remove(player1)
                    natureDeathLst.remove(natureDeath)
                    accidentalKill += 1

                else:
                    print()
                    print(natureDeath.format(player = player1))
                    characters.remove(player1)
                    accidentalKill += 1

            elif killDeath == "Spare life":
                spareLife = choice(sparesLife)

                player1 = choice(characters)
                player2 = choice(characters)

                while player2 == player1:
                    player2 = choice(characters)

                print()
                print(spareLife.format(player1 = player1, player2 = player2))

            else:
                randomKill = choice(killLst)

                player1 = choice(characters)
                player2 = choice(characters)

                while player2 == player1:
                    player2 = choice(characters)

                if "stabs" in randomKill:

                    stabKill = choice(stabbingWeapon)
                    print()
                    print(randomKill.format(player1 = player1, weapon = stabKill, player2 = player2))
                    characters.remove(player2)
                    purposeKill += 1

                elif "shoots" in randomKill:

                    rangeKill = choice(rangeWeapons)
                    print()
                    print(randomKill.format(player1 = player1, weapon = rangeKill, player2 = player2))
                    characters.remove(player2)
                    purposeKill += 1

                elif "suffocate" in randomKill:
                    randomsuffocationItems = choice(suffocationItems)
                    print()
                    print(randomKill.format(player1 = player1, suffocation = randomsuffocationItems, player2 = player2))
                    characters.remove(player2)
                    purposeKill += 1

                elif "throwing" in randomKill:
                    randomThrowingItem = choice(throwingItems)
                    print()
                    print(randomKill.format(player1 = player1, throw = randomThrowingItem, player2 = player2))
                    characters.remove(player2)
                    purposeKill += 1

                else:
                    print()
                    print(randomKill.format(player1 = player1, player2 = player2))
                    characters.remove(player2)
                    purposeKill += 1

        else:
            randomStuff = randint(1, 5)

            if randomStuff == 5:
                actualKill = choice(stupidDeaths)


                if "peaceful" in actualKill and len(characters) > 4:
                    player1 = choice(characters)

                    print()
                    print(actualKill.format(player1 = player1))
                    characters.remove(player1)
                    purposeKill += 1

                else:

                    player1 = choice(characters)
                    player2 = choice(characters)

                    while player2 == player1:
                        player2 = choice(characters)

                    print()
                    print(actualKill.format(player1 = player1, player2 = player2))
                    characters.remove(player1)
                    purposeKill += 1

            else:

                randomDoing = choice(nonKillLst)

                if "injured" in randomDoing:

                    player1 = choice(characters)

                    print()
                    print(randomDoing.format(player1 = player1))

                    player2 = choice(characters)

                    while player2 == player1:
                        player2 = choice(characters)

                    randomChoice = randint(1, 2)

                    if randomChoice == 1:

                        positiveinjuring = choice(injuredPositive)

                        print()
                        print(positiveinjuring.format(player1=player1, player2=player2))

                        randomEnding = randint(1, 2)

                        if randomEnding == 1:

                            randomGoodEnding = choice(goodInjuredEnding)

                            print()
                            print(randomGoodEnding.format(player1=player1, player2=player2))

                        else:

                            randomBadEnding = choice(badInjuredEnding)

                            print()
                            print(randomBadEnding.format(player1=player1, player2=player2))
                            characters.remove(player1)
                            purposeKill += 1

                    else:
                        negativeinjuring = choice(injuredNegative)

                        print()
                        print(negativeinjuring.format(player1=player1, player2=player2))
                        characters.remove(player1)
                        purposeKill += 1

                else:
                    player1 = choice(characters)

                    print()
                    print(randomDoing.format(player1=player1))

        subrounds += 1

        if subrounds % 3 == 0:
            rounds += 1
