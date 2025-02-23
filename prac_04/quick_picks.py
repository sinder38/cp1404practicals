"""
CP1404/CP5632 Practical
Quick picks
"""

from random import randint

# Line:
NUMBERS_PER_LINE = 6

# Random generation:
MIN_RANGE = 1
MAX_RANGE = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    quick_pick_count = get_valid_quick_picks()

    for i in range(quick_pick_count):
        sorted_quick_pick = sorted(generate_quick_pick())
        print(" ".join(f"{number:2}" for number in sorted_quick_pick))


# NOTE: full error checking was not requested
def get_valid_quick_picks():
    """get valid number from user of quick picks"""
    quick_picks_count = int(input("How many quick picks? "))
    while quick_picks_count < 0:
        print("Error. Cannot be negative")
        quick_picks_count = int(input("How many quick picks? "))
    return quick_picks_count


# NOTE: should have used numbers_per_line as parameter
def generate_quick_pick():
    """Generate random number from user of quick pick"""
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = randint(MIN_RANGE, MAX_RANGE)
        while number in quick_pick:
            number = randint(MIN_RANGE, MAX_RANGE)
        quick_pick.append(number)
    return quick_pick


if __name__ == "__main__":
    main()
