"""
This code is to
Receive a list from the user
Receive an item from the user
Use a linear search to search for the item
"""

# Data
userList = []

# Importing the files
from Suvin.Searches.LIST_CREATOR import *

# Creating a list
userList = getList(userList)

# Getting the item that needs to be found
item = input("\nEnter the item that you want to find in the list : ")

print()

# Linear Search Algorithm

for i in userList:
    if i == item:
        print("The item have been found at index {} ".format(userList.index(item) + 1))
        break
else:
    print("The item is not in the list.")