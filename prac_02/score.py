"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

def main():
    """Get user and random score and display their statuses"""

    # User score
    score = float(input("Enter score: "))
    result = determine_status(score)
    print(result)

    # Random score
    random_score = randint(0, 100)
    print(f"Your random score is {random_score}")
    result = determine_status(random_score)
    print(result)


def determine_status(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
