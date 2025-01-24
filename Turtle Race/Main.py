import TurtleRace2
import TurtleRace3

rounds = 0
turtleLst = []
numTurtle = int(input("How many turtles do you want to put in a race [2-5]: "))

while numTurtle <= 1 or numTurtle >= 6:
    print("\nOne or anything lower, or 6 or anything higher can't be accepted, get a better number")
    numTurtle = int(input("How many turtles do you want to put in a race: "))

print()

if numTurtle == 2:
    TurtleRace2.TwoRaceTurtle()
if numTurtle == 3:
    TurtleRace3.ThreeRaceTurtle()