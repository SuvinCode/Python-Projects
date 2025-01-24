from random import choice
from time import sleep

# Data
ran_lst = []
tot_time = 0
duplicateLst = []
lengthofNumber = 0
highestDuplicate = 0
highest_lst = []
numTimes = 0

# Input
startingRange = int(input("\nEnter the first range of your integer: "))
endingRange = int(input("Enter the ending range of your integer: "))

# Procedure

for i in range(startingRange, endingRange + 1):
    ran_lst.append(str(i))

while True:
    if len(duplicateLst) == 0:
        rand_num = choice(ran_lst)
        duplicateLst.append(rand_num)

    ran_num2 = choice(ran_lst)

    if ran_num2 != duplicateLst[0]:
        lengthofNumber = len(duplicateLst)

        if lengthofNumber > highestDuplicate:
            highestDuplicate = lengthofNumber

        numTimes += 1

        print("\nList:", duplicateLst)
        print("Length of duplicate numbers:", lengthofNumber)
        print("Highest length of duplicate number achieved:", highestDuplicate)

        if len(duplicateLst) > len(highest_lst):
            highest_lst = duplicateLst

        print("Highest list achieved:", highest_lst)
        print("Number of times:", numTimes)

        duplicateLst = []
        lengthofNumber = 0
        sleep(1)

    else:
        duplicateLst.append(ran_num2)


