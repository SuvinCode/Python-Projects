import turtle
import random
import time

def TwoRaceTurtle():
    #Data
    turtleLst = []
    firstPlayerScore = 0
    secondPlayerScore = 0
    rounds = 0

    for i in range(2):
        turtleName = input("Enter the turtle's name: ")
        turtleLst.append(turtleName)

    playerRounds = int(input("\nEnter the amount of rounds: "))

    while playerRounds != 0:
        wn = turtle.Screen()
        wn.title("Turtle Race by @SuvinChin")
        wn.bgcolor("black")
        wn.setup(width=1200, height=200)
        wn.tracer(0)

        #First Turtle
        firstTurtle = turtle.Turtle()
        firstTurtle.shape("turtle")
        firstTurtle.speed(0)
        firstTurtle.shapesize(2)
        firstTurtle.color("red")
        firstTurtle.penup()
        firstTurtle.goto(-300, 50)


        #Second Turtle
        secondTurtle = turtle.Turtle()
        secondTurtle.shape("turtle")
        secondTurtle.speed(0)
        secondTurtle.shapesize(2)
        secondTurtle.color("blue")
        secondTurtle.penup()
        secondTurtle.goto(-300, -50)


        #First Border
        firstborder = turtle.Turtle()
        firstborder.speed(0)
        firstborder.shape("square")
        firstborder.color("white")
        firstborder.shapesize(stretch_wid=9, stretch_len=1)
        firstborder.penup()
        firstborder.goto(-350, 0)

        #Finish Line
        finishline = turtle.Turtle()
        finishline.speed(0)
        finishline.shape("square")
        finishline.color("white")
        finishline.shapesize(stretch_wid=9, stretch_len=1)
        finishline.penup()
        finishline.goto(450, 0)

        #Score
        score_a = turtle.Turtle()
        score_a.color("red")
        score_a.hideturtle()
        score_a.penup()
        score_a.goto(-450, 40)
        score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center", font=("Times", 25, "normal"))
        score_b = turtle.Turtle()
        score_b.color("blue")
        score_b.hideturtle()
        score_b.penup()
        score_b.goto(-450, -60)
        score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center", font=("Times", 25, "normal"))

        wn.update()
        roundTurtle = turtle.Turtle()
        roundTurtle.hideturtle()
        roundTurtle.color("white")
        roundTurtle.penup()
        roundTurtle.goto(0, 0)
        roundTurtle.write("Round : {}".format(rounds + 1), align="center", font=("Times", 25, "normal"))
        time.sleep(3)

        while True:

            wn.update()

            # Event
            random1 = random.randint(100, 200)
            random2 = random.randint(100, 200)

            firstTurtle.showturtle()
            firstTurtle.forward(random1)
            secondTurtle.showturtle()
            secondTurtle.forward(random2)
            time.sleep(1)

            if firstTurtle.xcor() >= 450 and secondTurtle.xcor() >= 450:
                wn.update()
                if firstTurtle.xcor() > secondTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=200)
                    wn2.tracer(0)

                    # Winner Indicator

                    winnerIndicator = turtle.Turtle()
                    winnerIndicator.color("white")
                    winnerIndicator.hideturtle()
                    winnerIndicator.penup()
                    winnerIndicator.goto(0, 0)
                    firstPlayerScore += 1
                    roundTurtle.clear()
                    winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[0]), align="center",
                                          font=("Times", 25, "normal"))
                    score_a.clear()
                    score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    score_b.clear()
                    score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

                if secondTurtle.xcor() > firstTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=200)
                    wn2.tracer(0)

                    # Winner Indicator

                    winnerIndicator = turtle.Turtle()
                    winnerIndicator.color("white")
                    winnerIndicator.hideturtle()
                    winnerIndicator.penup()
                    winnerIndicator.goto(0, 0)
                    secondPlayerScore+=1
                    roundTurtle.clear()
                    winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[1]), align="center",
                                          font=("Times", 25, "normal"))
                    score_a.clear()
                    score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    score_b.clear()
                    score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

                if firstTurtle.xcor() == secondTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=200)
                    wn2.tracer(0)

                    # Winner Indicator

                    winnerIndicator = turtle.Turtle()
                    winnerIndicator.color("white")
                    winnerIndicator.hideturtle()
                    winnerIndicator.penup()
                    winnerIndicator.goto(0, 0)
                    roundTurtle.clear()
                    winnerIndicator.write("Draw!", align="center",
                                          font=("Times", 25, "normal"))
                    score_a.clear()
                    score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    score_b.clear()
                    score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

            if firstTurtle.xcor() >= 450:
                wn2 = turtle.Screen()
                wn2.title("Turtle Race by @SuvinChin")
                wn2.bgcolor("black")
                wn2.setup(width=1200, height=200)
                wn2.tracer(0)

                # Winner Indicator

                winnerIndicator = turtle.Turtle()
                winnerIndicator.color("white")
                winnerIndicator.hideturtle()
                winnerIndicator.penup()
                winnerIndicator.goto(0, 0)
                firstPlayerScore += 1
                roundTurtle.clear()
                winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[0]), align="center",
                                      font=("Times", 25, "normal"))
                score_a.clear()
                score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                score_b.clear()
                score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                time.sleep(2)
                wn2.clear()
                break

            if secondTurtle.xcor() >= 450:
                wn3 = turtle.Screen()
                wn3.title("Turtle Race by @SuvinChin")
                wn3.bgcolor("black")
                wn3.setup(width=1200, height=200)
                wn3.tracer(0)

                # Winner Indicator

                winnerIndicator = turtle.Turtle()
                winnerIndicator.color("white")
                winnerIndicator.hideturtle()
                winnerIndicator.penup()
                winnerIndicator.goto(0, 0)
                secondPlayerScore += 1
                roundTurtle.clear()
                winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[1]), align="center",
                                      font=("Times", 25, "normal"))
                score_a.clear()
                score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                score_b.clear()
                score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                time.sleep(2)
                wn3.clear()
                break

        rounds += 1
        playerRounds -= 1

    while playerRounds == 0:
        wn = turtle.Screen()
        wn.title("Turtle Race by @SuvinChin")
        wn.bgcolor("black")
        wn.setup(width=1200, height=200)
        wn.tracer(0)

        endScore = turtle.Turtle()
        endScore.hideturtle()
        endScore.color("white")
        endScore.penup()
        endScore.goto(0, 0)

        if firstPlayerScore > secondPlayerScore:
            endScore.write("{};s Turtle have won the entire race!".format(turtleLst[0]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break
        if secondPlayerScore > firstPlayerScore:
            endScore.write("{}'s Turtle have won the entire race!".format(turtleLst[1]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break
        if firstPlayerScore == secondPlayerScore:
            endScore.write("Tie the entire race!".format(turtleLst[0]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break

