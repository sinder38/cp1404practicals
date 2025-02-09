STAR_SYMBOL = "★"
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
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


def get_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100, inclusive.")
        score = float(input("Enter a valid score (0-100): "))
    return score


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score. Score must be between 0 and 100, inclusive."
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print(STAR_SYMBOL * int(score))


main()
