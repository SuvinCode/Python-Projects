# Level input function

def level_input(level):
    print("\n-----Level {}--------".format(level))

# Level output function

def level_output(correct_n, wrong_n):
    print("\nNumber of corrects = {}".format(correct_n))
    print("Number of wrongs = {}".format(wrong_n))

    # Average

    # Data
    divisionZero = 1

    if wrong_n == 0:
        print("Average (Corrects / Wrongs) : ", correct_n / divisionZero)
    else:
        print("Average (Corrects / Wrongs) : ", correct_n / wrong_n)

    print()