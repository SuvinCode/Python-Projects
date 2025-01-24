"""
This code is to
Get all the prime factors from a single number
"""

# Data
prime_factors = []
index = 1

# Receive an integer from the user
user_integer = int(input("\nEnter an integer : "))

# Getting the prime number factors from the user

for i in range(1, user_integer):
    if user_integer % i == 0 and i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_factors.append(i)

prime_factors.append(user_integer)

# Printing the answer
print("\nThe Prime Factors : ", prime_factors)