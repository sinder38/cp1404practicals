"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When I enter a value not convertable to an integer. Like "one", "0.1", "****"

2. When will a ZeroDivisionError occur?
When I enter numerator correctly and denominator as 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I could but I won't hahahaha. Fine I will do it

A ZeroDivisionError occurs when trying to divide a number by zero.
To avoid the ZeroDivisionError, you could add a check before dividing:
don't tell me what to do, that is boring
"""

# Code for question 3
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:  # We check for zero before causing an error
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# Initial code

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")
