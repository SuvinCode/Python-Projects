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
                    print(natureDeath.format(player=player1))
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


# Import random
from random import choice, randint
from time import sleep

# Dessert Function
def arctic(characters):

    # Data
    rounds = 1
    subrounds = 0
    accidentalKill = 0
    purposeKill = 0

    # Weapons

    stabbingWeapon = [
        "knife",
        "mallet",
        "ice shard",
        "icicles",
        "cleaver",
        "dagger",
        "crowbar",
    ]

    rangeWeapons = [
        "bow",
        "crossbow"
    ]

    throwingItems = [
        "ice",
        "snow",
        "ice shards",
        "icicles",
        "ice cube"
    ]

    suffocationItems = [
        "whale fat",
        "walrus fat",
        "water",
        "ice"
    ]

    # Deaths

    natureDeathLst = [
        "{player} gets mauled by a polar bear.",
        "{player} gets ambushed and attacked by a pack of wolves",
        "{player} gets crushed in an avalanche",
        "{player} froze to death",
        "{player} tries to get milk from a bison and ends up getting pierced by the bison.",
        "{player} gets pecked by a colony of penguins while {player} tried to steal a baby penguin",
        "{player} got stomped on an elephant seal",
        "{player} got bitten by a walrus to death while {player} tries to kill a walrus using a hand.",
        "{player} died in a blizzard",
        "{player} successfully started a fire but {player} burnt to death",
        "{player} starved to death",
        "{player} ate raw meat and died from food poisoning",
        "{player} got spiked by an icicle when exploring a cave",
        "{player} was too cold that he killed himself",
        "{player} got hyperthermia and decided it was a good idea to dive into the sea and froze to death",
        "{player} went fishing by diving in the sea and sadly drowned",
        "{player} tries to lick an icicle and his tongue got ripped so {player} bled to death"
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
        "{player1} went fishing",
        "{player1} tries to start a fire",
        "{player1} tries to hibernate",
        "{player1} decided to sleep through the whole hunger games",
        "{player1} successfully starts a fire",
        "{player1} was attacked by a polar bear but {player1} still lived. However, he was heavily injured",
        "{player1} was spiked by icicles but survived but {player1} is seriously injured"
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

    print("                  _.--\"\"\"-,")
    print("                .'            `\\")
    print("               /   _            \\")
    print(" .-""-.       |  (O\.--.-.-/O)          .-""-.")
    print("/ O O  \      .\|(_._.__._.__)         /  O O \\")
    print("|O .-.  \    (   )   0 _ 0   \        /  .-. O|")
    print("\ (   )  '.   `-|     (_)     |     .'  (   ) /")
    print(" '.`-'     '-./`|             |`\.-'     '-'.'")
    print("   \         |  \   \     /   /  |         /")
    print("    \        \   '.  '._.'  .'   /        /")
    print("     \        '.   `'-----'`   .'        /")
    print("      \   .'    '-._        .-'\   '.   /")
    print("       |/`          `'''''')    )    `\|")
    print("       /                  (    (      ,\\")
    print("      ;                    \    '-..-'/ ;")
    print("      |                     '.       /  |")
    print("      |                       `'---'`   |")
    print("      ;                                 ;")
    print("       \                               /")
    print("        `.                           .'")
    print("          '"
          "."
          "0-._                   _.-'")
    print("           __/`"  '  - - -  ' "`` \__")
    print("         /`            /^\           `\\")
    print("         \(          .'   '.         )/")
    print("          '.(__(__.-'       '.__)__).'")




    print("\nWelcome to the arctic, a freezing cold iceland filled with humongous animals. No plants grow are present here.")

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
                        print(positiveinjuring.format(player1 = player1, player2 = player2))

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
                    print(randomDoing.format(player1 = player1))

        subrounds += 1

        if subrounds % 3 == 0:
            rounds += 1




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