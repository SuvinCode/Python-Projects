"""
This code is to:
Get all the common factors from a specifc number following the range of 1 to zero
"""

# Data
index = 1
factorList = []

# Receive an integer from a user
userInteger = int(input("\nEnter an integer : "))

# Getting the common factors from the user

while index <= userInteger:
    if userInteger % index == 0:
        factorList.append(index)

    # Increasing index
    index += 1

# Printing the common factors
print("\nCommon Factors :", factorList)

