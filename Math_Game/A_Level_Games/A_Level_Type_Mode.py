# Importing files
from .C_Level_Type_Functions import *
from .D_Level_Type_SayingFunction import *
from .E_Level_Type_Ranks import *
from .F_Level_Type_Difficulity import *

# Level gamemode function

def Level_Mode():
    print("\n----Level Mode------")
    print("\nThis mode is an infinite mode.")
    print("\nEach levels increases your difficulity. ")
    print("So good luck!")

    # Data
    level = 1
    correct = 0
    wrong = 0


    # Choosing the levels

    while True:

        answer = True

        if level >= 1000:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_1000_1010(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 210:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_211_220(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 200:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_200_210(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)


        elif level >= 50:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_51_60(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 40:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_41_50(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 35:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_36_40(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 30:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_31_35(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 25:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_26_30(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 20:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_21_25(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 15:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_16_20(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 10:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_11_15(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        elif level >= 5:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_6_10(answer, level)

            if answer == True:
                level += 1
                correct += 1
            else:
                wrong += 1

            level_output(correct, wrong)

        else:
            level_input(level)
            showRank(level)
            showDifficulty(level)
            answer, level = level_1_5(answer, level)

            if answer == True:
                correct += 1
                level += 1
            else:
                wrong += 1

            level_output(correct, wrong)











