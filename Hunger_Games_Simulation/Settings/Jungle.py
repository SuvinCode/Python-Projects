# Import random
from random import choice, randint
from time import sleep

# Dessert Function
def jungle(characters):

    # Data
    rounds = 1
    subrounds = 0
    accidentalKill = 0
    purposeKill = 0

    # Weapons

    stabbingWeapon = [
        "knife",
        "tiger's claw",
        "tiger's fang",
        "sharp leave",
        "stone",
        "stalactite",
        "stalagmite",
        "dagger",
        "crowbar",
        "karambit",
        "viper's fangs",
        "rhinoceros horn",
        "axe",
        "machete"
    ]

    rangeWeapons = [
        "bow",
        "poison arrows",
        "poison darts",
        "viper's venom",
        "crossbow",
        "shotgun",
        "sniper rifle"
    ]

    throwingItems = [
        "stone",
        "grenade",
        "shurikens",
        "sandstone"
    ]

    suffocationItems = [
        "sand",
        "mud",
        "dirt",
    ]

    # Animals

    poisonousAnimals = [
        "king Cobra",
        "cobra",
        "viper",
        "poison arrow frog",
        "red belly newt",
        "green tree snake",
        "gaboon viper",
        "black mamba"
    ]

    swarmAnimals = [
        "fire Ants",
        "beetles",
        "army ants",
        "wasps",
        "wolves",
        "hyenas",
        "wild dogs",
        "vultures",
        "foxes",
        "termites"
    ]

    maulAnimals = [
        "brown bear",
        "black bear",
        "grizzly bear",
        "tiger",
        "lion",
        "cheetah",
        "jaguar",
        "ocelot",
        "cougar",
        "leopard",
        "white tiger",
    ]

    peckingAnimals = [
        "hornbills",
        "toucans",
        "eagles",
        "falcons",
        "seagulls",
        "parrots",
        "owls",
        "hummingbirds",
        "sparrows",
        "ducks",
        "geese"

    ]

    kickingAnimals = [
        "wildebeests",
        "deers",
        "bulls",
        "gazelles",
        "horses",
        "donkeys",
        "goats",
        "girrafes",
    ]

    # Deaths

    natureDeathLst = [
        "{player} got poisoned by {animal} and died to death",
        "{player} got swarmed by {animal}",
        "{player} got mauled by a {animal}",
        "{player} was pecked by {animal} to death after trying to steal its eggs",
        "{player} was kicked to death by {animal} after trying to act like a lion",
        "{player} tried to take some honey but got stung to death by a swarm of bees and wasps",
        "{player} got attacked by a hippopotamus when {player} went swimming",
        "{player} died from trying to consume raw meat",
        "{player} thought it would be a good idea to enter a deep cavern and fell down and died",
        "{player} got stabbed by a rhinoceros",
        "{player} got attacked from a bear while trying to enter a cave.",
        "{player} thought it would be a good idea to enter a snake pit and died from too much venom",
        "{player} wanted to do rock climbing and died of fall damage instead",
        "{player} thought it would be a good idea to junp down a waterfall and {player}'s head was broken",
        "{player} was picking berries, not realizing it was poisonous berries and died from daftness",
        "{player} was picking mushroom, not realizing it was poisonous mushrooms and died from poison",
        "{player} drown to death",
        "{player} was crushed by a falling boulder out of nowhere",
        "{player} tried to steal a tiger's food but instead gets killed",
        "{player} tries to join the lion pack but gets attacked to death instead",
        "{player} was crushed to death by a python",
        "{player} was crushed by an elephant after thinking it was a good idea to sit in front of the elephant",
        "{player} was crushed by a raging elephant after attempting to bite it",
        "{player} starved to death",
        "{player} died of thirst",
        "{player1} decided to sleep through the whole hunger games"
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
        "{player1} grabs an abandoned backpack, not realizing it's empty",
        "{player1} kept on shouting like a lunatic",
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

    print(".. ........... .............  ........... . ..... ........ .......")
    print("......  ....................%.... .... ..... .........%............")
    print(".@@@ ........ @@.... @@@@  . ............................  *  .....")
    print("....@@ ..... @ .... @ .............   ....... .....; .... *** .....")
    print(".....\@\....@ .... @ ............................. #  .. *****  ...")
    print(" @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******")
    print("....@-@..@ ..@......@@@\...... %...... ....... <## ####>********")
    print("  @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********")
    print("....%..@  @@ /@@@@@ . ....... ...............<###########> *******")
    print("...... .@-@@@@ ...V......     .... %.......... {#######}******* ***")
    print("...... .  @@ .. ..v.. .. . { } ............<###############>*******")
    print("......... @@ .... ........ {^^,     .......   {## ######}***** ****")
    print("..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****")
    print(". .... . @@ . .... .. _  .. `;;~~ ......... {#############}********")
    print(".... ... @@ ... ..   /(______); .. ....<################  #####>***")
    print(". .... ..@@@ ...... (         (  .........{##################}*****")
    print("......... @@@  ....  |:------( )  .. <##########################>**")
    print(" @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****")
    print("@@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>")
    print("@@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@")
    print("@@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@")
    print("-@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


    print("\nWelcome to the Jungle, a tropical and warm plain. However, be aware that petrifying and blood-thirsty creatures are lurking around.")

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
                    accidentalKill += 1

                elif "swarmed" in natureDeath:

                    randomSwarmAnimal = choice(swarmAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomSwarmAnimal))
                    characters.remove(player1)
                    accidentalKill += 1

                elif "mauled" in natureDeath:

                    randomMaulAnimal = choice(maulAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomMaulAnimal))
                    characters.remove(player1)
                    accidentalKill += 1

                elif "pecked" in natureDeath:
                    randomPeckingAnimal = choice(peckingAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomPeckingAnimal))
                    characters.remove(player1)
                    accidentalKill += 1

                elif "kicked" in natureDeath:
                    randomKickingAnimal = choice(kickingAnimals)

                    print()
                    print(natureDeath.format(player = player1, animal = randomKickingAnimal))
                    characters.remove(player1)
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


                if "peaceful" in actualKill:
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
