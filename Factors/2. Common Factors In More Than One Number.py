"""
This code is to:
Get as many variables
And find the common factors between more numbers
"""

# Data
integerLst = []
index = 1
factor_lst = []

# Receive the number of variables from the user
userVariable = int(input("\nEnter the number of variables that you want : "))

print()

# Getting the variables

while userVariable > 0:
    userNumber = int(input("Enter an integer : "))
    integerLst.append(userNumber)
    userVariable -= 1

# Getting the common factors in the list

while index <= max(integerLst):
    for i in integerLst:
        if i % index != 0:
            break
    else:
        factor_lst.append(index)

    index += 1

# Printing the answer
print("\nThe Common Facrtors between the numbers : ", factor_lst)
