"""
This code is used to:
Get the highest common factor
of as many numbers as the user determines it
"""

# Data
integer_lst = []
decoyInteger_lst = []
index = 2
factor_lst = []
count = 0
ans = 1

# Receive the number of variables from the user
userVariable = int(input("\nEnter the number of variables : "))

print()

# Getting the variables

while userVariable > 0:
    userNumber = int(input("Enter an integer : "))
    integer_lst.append(userNumber)
    userVariable -= 1

# Getting the length of the list
lstLength = len(integer_lst)
maximum = max(integer_lst)

# Finding the HCF

while index < maximum:
    for i in integer_lst:
        if i % index != 0:
            break
    else:
        factor_lst.append(index)

        for j in integer_lst:
            j = j / index
            decoyInteger_lst.append(j)

        integer_lst.clear()
        integer_lst += decoyInteger_lst
        decoyInteger_lst.clear()
        index = 1

    index += 1

# Multiplying everything

for i in factor_lst:
    ans *= i

# Printing the answer

if len(factor_lst) == 0:
    print("\nHCF Factors : 1")
else:
    print("\nHCF Factors :", factor_lst)

print("The HCF :", ans)
