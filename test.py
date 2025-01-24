import random

userinput = int(input("Enter a number from 1-10: "))

rannum = random.randint(1, 10)

if rannum == userinput:
    print("You won. The number is", rannum)
else:
    print("You lose. The number is", rannum)