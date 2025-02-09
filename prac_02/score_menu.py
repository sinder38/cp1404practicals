"""
CP1404 - Practical
Program to determine score status and print matching amount of stars
"""

STAR_SYMBOL = "★"  # Aste risk my ****                                                                                                        (word "mark" is censored here)
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score program and continue until the user exits"""
    score = get_score()
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = determine_status(score)
            print(f"Your final grade is: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid option, please try again.")

        print(MENU)
        choice = input("Enter choice: ").upper()

    print("Thank you for playing!")  # Screw you


def get_score():
    """Get a valid score"""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100, inclusive.")
        score = float(input("Enter a valid score (0-100): "))
    return score


def determine_status(score):
    """Determine score status (0-100)"""
    # No need to check score validity as
    # it is checked by get_score() function
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many  stars as the score"""
    print(STAR_SYMBOL * int(score))


if __name__ == "__main__":
    main()
