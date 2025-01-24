"""
This code is to
Create a list
for the user
"""

def getList(userList):

    # Data
    x = 0

    # Receive the number of data to be entered in the list
    dataNum = int(input("\nEnter the number of variables in your list : "))

    # Creating the list

    print()

    while x < dataNum:
        userElement = str(input("Enter an element in the list : "))
        userList.append(userElement)
        x += 1

    return userList