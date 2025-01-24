# Importing modules
import random
import time

# Timer Function

def timer(question):
    if question >= 40:
        return 5
    elif question >= 35:
        return 10
    elif question >= 30:
        return 15
    elif question >= 25:
        return 20
    elif question >= 20:
        return 25
    elif question >= 15:
        return 30
    elif question >= 10:
        return 60
    elif question >= 5:
        return 300
    else:
        return 600

# Addition Function

def addition(answer, question, speed):

    t = timer(question)

    ran1 = random.randint(1, 15)
    ran2 = random.randint(1, 15)
    ans = ran1 + ran2

    start = time.time()
    userNumber = int(input("{} + {} : ".format(ran1, ran2)))
    end = time.time()
    time_taken = int(end - start)

    speed.append(time_taken)

    if userNumber == ans and time_taken < t:
        return answer, question, speed
    else:
        answer = False
        return answer, question, speed

# Substraction Function

def substraction(answer, question, speed):
    t = timer(question)

    ran1 = random.randint(1, 15)
    ran2 = random.randint(1, 15)

    if ran1 > ran2:

        ans = ran1 - ran2

        start = time.time()
        userNumber = int(input("{} - {} : ".format(ran1, ran2)))
        end = time.time()
        time_taken = int(end - start)

        speed.append(time_taken)

        if userNumber == ans and time_taken < t:
            return answer, question, speed
        else:
            answer = False
            return answer, question, speed
    else:
        ans = ran2 - ran1

        start = time.time()
        userNumber = int(input("{} - {} : ".format(ran2, ran1)))
        end = time.time()
        time_taken = int(end - start)

        speed.append(time_taken)

        if userNumber == ans and time_taken < t:
            return answer, question, speed
        else:
            answer = False
            return answer, question, speed


# Multiplication Function

def multiplication(answer, question, speed):
    t = timer(question)

    ran1 = random.randint(1, 15)
    ran2 = random.randint(1, 15)
    ans = ran1 * ran2

    start = time.time()
    userNumber = int(input("{} X {} : ".format(ran1, ran2)))
    end = time.time()
    time_taken = int(end - start)

    speed.append(time_taken)

    if userNumber == ans and time_taken < t:
        return answer, question, speed
    else:
        answer = False
        return answer, question, speed

# Division Function

def division(answer, question, speed):
    t = timer(question)

    ran1 = random.randint(1, 15)
    ran2 = random.randint(1, 15)
    multiple_ans = ran1 * ran2

    division_ran = random.randint(1, 3)

    if division_ran == 1:
        start = time.time()
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran1)))
        ans = multiple_ans / ran1
        end = time.time()
        time_taken = int(end - start)

        speed.append(time_taken)

        if userNumber == ans and time_taken < t:
            return answer, question, speed
        else:
            answer = False
            return answer, question, speed
    else:
        ans = multiple_ans / ran2
        start = time.time()
        userNumber = int(input("{} / {} : ".format(multiple_ans, ran2)))
        end = time.time()
        time_taken = int(end - start)

        speed.append(time_taken)

        if userNumber == ans and time_taken < t:
            return answer, question, speed
        else:
            answer = False
            return answer, question, speed
