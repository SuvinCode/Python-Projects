# Data
count = 0
playerTurn = 0

# Initialize a variable for the tic tac toe border
first_border = [[1], [2], [3]]
second_border = [[4], [5], [6]]
third_border = [[7], [8], [9]]

# Printing the border to be like
print(first_border)
print(second_border)
print(third_border)

while True:

    # First Player turn
    if playerTurn % 2 == 0:
        first_player = int(input("\n[FIRST PLAYER] Enter a number from 1 - 9 to replace with the corresponding symbol : "))

        # Inserting the first player's movement

        if 0 < first_player < 4:
            if first_player == 1:
                if first_border[0] == "O":
                    print("That border is taken")
                else:
                    first_border[0] = "X"
                    count += 1
                    playerTurn += 1
            elif first_player == 2:
                if first_border[1] == "O":
                    print("That border is taken")
                else:
                    first_border[1] = "X"
                    count += 1
                    playerTurn += 1
            else:
                if first_border[2] == "O":
                    print("That border is taken")
                else:
                    first_border[2] = "X"
                    count += 1
                    playerTurn += 1
        elif 3 < first_player < 7:
            if first_player == 4:
                if second_border[0] == "O":
                    print("That border is taken")
                else:
                    second_border[0] = "X"
                    count += 1
                    playerTurn += 1
            elif first_player == 5:
                if second_border[1] == "O":
                    print("That border is taken")
                else:
                    second_border[1] = "X"
                    count += 1
                    playerTurn += 1
            else:
                if second_border[2] == "O":
                    print("That border is taken")
                else:
                    second_border[2] = "X"
                    count += 1
                    playerTurn += 1
        elif 6 < first_player < 10:
            if first_player == 7:
                if third_border[0] == "O":
                    print("That border is taken")
                else:
                    third_border[0] = "X"
                    count += 1
                    playerTurn += 1
            elif first_player == 8:
                if third_border[1] == "O":
                    print("That border is taken")
                else:
                    third_border[1] = "X"
                    count += 1
                    playerTurn += 1
            else:
                if third_border[2] == "O":
                    print("That border is taken")
                else:
                    third_border[2] = "X"
                    count += 1
                    playerTurn += 1
        else:
            print("The range is out of limit")

    else:

        # Second player turn

        second_player = int(input("\n[SECOND PLAYER] Enter a number from 1 - 9 to replace with the corresponding symbol : "))

        # Inserting the second player turn

        if 0 < second_player < 4:
            if second_player == 1:
                if first_border[0] == "X":
                    print("That border is taken")
                else:
                    first_border[0] = "O"
                    count += 1
                    playerTurn += 1
            elif second_player == 2:
                if first_border[1] == "X":
                    print("That border is taken")
                else:
                    first_border[1] = "O"
                    count += 1
                    playerTurn += 1
            else:
                if first_border[2] == "X":
                    print("That border is taken")
                else:
                    first_border[2] = "O"
                    count += 1
                    playerTurn += 1
        elif 3 < second_player < 7:
            if second_player == 4:
                if second_border[0] == "X":
                    print("That border is taken")
                else:
                    second_border[0] = "O"
                    count += 1
                    playerTurn += 1
            elif second_player == 5:
                if second_border[1] == "X":
                    print("That border is taken")
                else:
                    second_border[1] = "O"
                    count += 1
                    playerTurn += 1
            else:
                if second_border[2] == "X":
                    print("That border is taken")
                else:
                    second_border[2] = "O"
                    count += 1
                    playerTurn += 1
        elif 6 < second_player < 10:
            if second_player == 7:
                if third_border[0] == "X":
                    print("That border is taken")
                else:
                    third_border[0] = "O"
                    count += 1
                    playerTurn += 1
            elif second_player == 8:
                if third_border[1] == "X":
                    print("That border is taken")
                else:
                    third_border[1] = "O"
                    count += 1
                    playerTurn += 1
            else:
                if third_border[2] == "X":
                    print("That border is taken")
                else:
                    third_border[2] = "O"
                    count += 1
                    playerTurn += 1
        else:
            print("The range is out of limit")

    # Printing the changing border

    print()
    print(first_border)

    print(second_border)
    print(third_border)

    # X winning position

    # Horizontal winning position

    if first_border[0] == "X" and first_border[1] == "X" and first_border[2] == "X":
        print("\nThe first player wins!")
        break
    elif second_border[0] == "X" and second_border[1] == "X" and second_border[2] == "X":
        print("\nThe first player wins!")
        break
    elif third_border[0] == "X" and third_border[1] == "X" and third_border[2] == "X":
        print("\nThe first player wins!")
        break

    # Vertical winning position

    elif first_border[0] == "X" and second_border[0] == "X" and third_border[0] == "X":
        print("\nThe first player wins!")
        break
    elif first_border[1] == "X" and second_border[1] == "X" and third_border[1] == "X":
        print("\nThe first player wins!")
        break
    elif first_border[2] == "X" and second_border[2] == "X" and third_border[2] == "X":
        print("\nThe first player wins!")
        break

    # Zig zag winning position

    elif first_border[0] == "X" and second_border[1] == "X" and third_border[2] == "X":
        print("\nThe first player wins!")
        break
    elif first_border[2] == "X" and second_border[1] == "X" and third_border[0] == "X":
        print("\nThe first player wins!")
        break

    # O winning position

    # Horizontal winning position

    elif first_border[0] == "O" and first_border[1] == "O" and first_border[2] == "O":
        print("\nThe second player wins!")
        break
    elif second_border[0] == "O" and second_border[1] == "O" and second_border[2] == "O":
        print("\nThe second player wins!")
        break
    elif third_border[0] == "O" and third_border[1] == "O" and third_border[2] == "O":
        print("\nThe second player wins!")
        break

    # Vertical winning position

    elif first_border[0] == "O" and second_border[0] == "O" and third_border[0] == "O":
        print("\nThe second player wins!")
        break
    elif first_border[1] == "O" and second_border[1] == "O" and third_border[1] == "O":
        print("\nThe second player wins!")
        break
    elif first_border[2] == "O" and second_border[2] == "O" and third_border[2] == "O":
        print("\nThe second player wins!")
        break

    # Zig zag winning position

    elif first_border[0] == "O" and second_border[1] == "O" and third_border[2] == "O":
        print("\nThe second player wins!")
        break
    elif first_border[2] == "O" and second_border[1] == "O" and third_border[0] == "O":
        print("\nThe second player wins!")
        break

    # Breaking if the tic tac toe border is full
    if count == 9:
        break

