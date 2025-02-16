"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

NAME = "Gibson L-5 CES"
YEAR = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + NAME + ", first made in " + str(YEAR))

# A better way - using str.format() (don't do this unless you need to):
print("My guitar: {}, first made in {}".format(NAME, YEAR))
print("My guitar: {0}, first made in {1}".format(NAME, YEAR))
print("My {0} was first made in {1} (that's right, {1}!)".format(NAME, YEAR))

# And with f-string formatting, introduced in Python 3.6 (do this)
print(f"My {NAME} was first made in {YEAR} (that's right, {YEAR}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(NAME, cost))  # str.format version
print(f"My {NAME} would cost ${cost:,.2f}")  # preferred f-string version

# Aligning columns by using width after the :
# This loop uses enumerate, which is useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# 1922 Gibson L-5 CES for about $16,036!
output = f"{YEAR} {NAME} for about ${cost:,.0f}!"
print(output)

# produce the following right-aligned output (DO NOT use a list):
# 2 ^ 0 is    1
# 2 ^ 1 is    2
# 2 ^ 2 is    4
# 2 ^ 3 is    8
# 2 ^ 4 is   16
# 2 ^ 5 is   32
# 2 ^ 6 is   64
# 2 ^ 7 is  128
# 2 ^ 8 is  256
# 2 ^ 9 is  512
# 2 ^10 is 1024
BASE = 2
EXPONENT_LIMIT = 10  # don't use numbers higher than 99

for i in range(EXPONENT_LIMIT + 1):
    print(f"{BASE} ^{i:2} is {BASE ** i:4}")
