"""
This code is to
Get all the factors from a number
Sum up all the numbers
"""

# Data
ans = 0

# Receive an integer from the user
user_integer = int(input("\nEnter an integer : "))

# Getting all the factors from the number

for i in range(1, user_integer + 1):
    if user_integer % i == 0:
        ans += i

# Printing the answer
print("\nThe sum of all the factors : ", ans)