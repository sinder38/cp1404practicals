"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""


def main():
    """Get user score and display its status"""
    score = float(input("Enter score: "))
    result = determine_status(score)
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
