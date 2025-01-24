import turtle
import random
import time

def ThreeRaceTurtle():
    #Data
    turtleLst = []
    firstPlayerScore = 0
    secondPlayerScore = 0
    thirdPlayerScore = 0
    rounds = 0

    for i in range(3):
        turtleName = input("Enter the turtle's name: ")
        turtleLst.append(turtleName)

    playerRounds = int(input("\nEnter the amount of rounds: "))

    while playerRounds != 0:
        wn = turtle.Screen()
        wn.title("Turtle Race by @SuvinChin")
        wn.bgcolor("black")
        wn.setup(width=1200, height=300)
        wn.tracer(0)

        #First Turtle
        firstTurtle = turtle.Turtle()
        firstTurtle.shape("turtle")
        firstTurtle.speed(0)
        firstTurtle.shapesize(2)
        firstTurtle.color("red")
        firstTurtle.penup()
        firstTurtle.goto(-300, 100)


        #Second Turtle
        secondTurtle = turtle.Turtle()
        secondTurtle.shape("turtle")
        secondTurtle.speed(0)
        secondTurtle.shapesize(2)
        secondTurtle.color("green")
        secondTurtle.penup()
        secondTurtle.goto(-300, 0)

        # Third Turtle
        thirdTurtle = turtle.Turtle()
        thirdTurtle.shape("turtle")
        thirdTurtle.speed(0)
        thirdTurtle.shapesize(2)
        thirdTurtle.color("blue")
        thirdTurtle.penup()
        thirdTurtle.goto(-300, -100)


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
        score_a.goto(-450, 100)
        score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center", font=("Times", 25, "normal"))
        score_b = turtle.Turtle()
        score_b.color("green")
        score_b.hideturtle()
        score_b.penup()
        score_b.goto(-450, 0)
        score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center", font=("Times", 25, "normal"))
        score_c = turtle.Turtle()
        score_c.color("blue")
        score_c.hideturtle()
        score_c.penup()
        score_c.goto(-450, -100)
        score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center", font=("Times", 25, "normal"))

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
            random3 = random.randint(100, 200)

            firstTurtle.showturtle()
            firstTurtle.forward(random1)
            secondTurtle.showturtle()
            secondTurtle.forward(random2)
            thirdTurtle.showturtle()
            thirdTurtle.forward(random3)
            time.sleep(1)

            if firstTurtle.xcor() >= 450 and secondTurtle.xcor() >= 450 and thirdTurtle.xcor() >= 450:
                wn.update()
                if firstTurtle.xcor() > secondTurtle.xcor() and firstTurtle.xcor() > thirdTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=300)
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
                    score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

                if secondTurtle.xcor() > firstTurtle.xcor() and secondTurtle.xcor() > thirdTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=300)
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
                    score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

                if thirdTurtle.xcor() > firstTurtle.xcor() and thirdTurtle.xcor() > secondTurtle.xcor():
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=300)
                    wn2.tracer(0)

                    # Winner Indicator

                    winnerIndicator = turtle.Turtle()
                    winnerIndicator.color("white")
                    winnerIndicator.hideturtle()
                    winnerIndicator.penup()
                    winnerIndicator.goto(0, 0)
                    thirdPlayerScore+=1
                    roundTurtle.clear()
                    winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[2]), align="center",
                                          font=("Times", 25, "normal"))
                    score_a.clear()
                    score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    score_b.clear()
                    score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

                if firstTurtle.xcor() == secondTurtle.xcor() == thirdTurtle:
                    wn2 = turtle.Screen()
                    wn2.title("Turtle Race by @SuvinChin")
                    wn2.bgcolor("black")
                    wn2.setup(width=1200, height=300)
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
                    score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                    time.sleep(2)
                    wn2.clear()
                    break

            if firstTurtle.xcor() >= 450:
                wn2 = turtle.Screen()
                wn2.title("Turtle Race by @SuvinChin")
                wn2.bgcolor("black")
                wn2.setup(width=1200, height=300)
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
                score_c.clear()
                score_c.write("{} : {}".format(turtleLst[2], secondPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                time.sleep(2)
                wn2.clear()
                break

            if secondTurtle.xcor() >= 450:
                wn3 = turtle.Screen()
                wn3.title("Turtle Race by @SuvinChin")
                wn3.bgcolor("black")
                wn3.setup(width=1200, height=300)
                wn3.tracer(0)



                # Winner Indicator

                winnerIndicator = turtle.Turtle()
                winnerIndicator.color("white")
                winnerIndicator.hideturtle()
                winnerIndicator.penup()
                winnerIndicator.goto(0, 0)
                firstPlayerScore += 1
                roundTurtle.clear()
                winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[1]), align="center",
                                          font=("Times", 25, "normal"))
                score_a.clear()
                score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                score_b.clear()
                score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                                  font=("Times", 25, "normal"))
                score_c.clear()
                score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                              font=("Times", 25, "normal"))
                time.sleep(2)
                wn2.clear()
                break

        if thirdTurtle.xcor() >= 450:
            wn2 = turtle.Screen()
            wn2.title("Turtle Race by @SuvinChin")
            wn2.bgcolor("black")
            wn2.setup(width=1200, height=300)
            wn2.tracer(0)

            # Winner Indicator

            winnerIndicator = turtle.Turtle()
            winnerIndicator.color("white")
            winnerIndicator.hideturtle()
            winnerIndicator.penup()
            winnerIndicator.goto(0, 0)
            thirdPlayerScore += 1
            roundTurtle.clear()
            winnerIndicator.write("{}'s turtle have won the race! ".format(turtleLst[2]), align="center",
                                  font=("Times", 25, "normal"))
            score_a.clear()
            score_a.write("{} : {}".format(turtleLst[0], firstPlayerScore), align="center",
                          font=("Times", 25, "normal"))
            score_b.clear()
            score_b.write("{} : {}".format(turtleLst[1], secondPlayerScore), align="center",
                          font=("Times", 25, "normal"))
            score_c.write("{} : {}".format(turtleLst[2], thirdPlayerScore), align="center",
                          font=("Times", 25, "normal"))
            time.sleep(2)
            wn2.clear()
            break

        rounds += 1
        playerRounds -= 1

    while playerRounds == 0:
        wn = turtle.Screen()
        wn.title("Turtle Race by @SuvinChin")
        wn.bgcolor("black")
        wn.setup(width=1200, height=300)
        wn.tracer(0)

        endScore = turtle.Turtle()
        endScore.hideturtle()
        endScore.color("white")
        endScore.penup()
        endScore.goto(0, 0)

        if firstPlayerScore > secondPlayerScore and firstPlayerScore > thirdPlayerScore:
            endScore.write("{};s Turtle have won the entire race!".format(turtleLst[0]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break
        if secondPlayerScore > firstPlayerScore and secondPlayerScore > thirdPlayerScore:
            endScore.write("{}'s Turtle have won the entire race!".format(turtleLst[1]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break
        if thirdPlayerScore > firstPlayerScore and thirdPlayerScore > secondPlayerScore:
            endScore.write("{}'s Turtle have won the entire race!".format(turtleLst[2]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break
        if firstPlayerScore == secondPlayerScore == thirdPlayerScore:
            endScore.write("Tie the entire race!".format(turtleLst[0]), align="center", font=("Times", 25, "normal"))
            time.sleep(3)
            break

