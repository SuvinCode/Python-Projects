"""
This code is to
Receive a list from the user
Receive an item from the user
Find the item using a binary search
"""

# Importing files
from Suvin.Searches.LIST_CREATOR import *

# Data
userList = []

# Creating a list
userList = getList(userList)

# Getting the item that need to be found in the list
item = input("\nEnter the item that you want to find in the list : ")

# List Data
lowestIndex = 0
highestIndex = len(userList) - 1

# Binary Search Algorithm

while highestIndex >= lowestIndex:
    mid = (highestIndex + lowestIndex) // 2

    if userList[mid] == item:
        print("The item has been found on index {}. ".format(mid + 1))
        break

    elif mid > userList.index(item):
        mid += 1
        lowestIndex = mid

    else:
        mid -= 1
        highestIndex = mid

    if highestIndex // lowestIndex == 0:
        print("The item is not found in the list.")
        break