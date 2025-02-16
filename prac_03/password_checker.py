"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
MIN_NUMBER_OF_LOWER = 1
MIN_NUMBER_OF_UPPER = 1
MIN_NUMBER_OF_DIGIT = 1
MIN_NUMBER_OF_SPECIAL = 1
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print_requirements()

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print(f"Your {len(password)}-character password is valid: {password}")


def print_requirements():
    """Print requirements for a valid password"""
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    if MIN_NUMBER_OF_UPPER > 0:
        print(f"\t{MIN_NUMBER_OF_UPPER} or more uppercase characters")
    if MIN_NUMBER_OF_LOWER > 0:
        print(f"\t{MIN_NUMBER_OF_LOWER} or more lowercase characters")
    if MIN_NUMBER_OF_DIGIT > 0:
        print(f"\t{MIN_NUMBER_OF_DIGIT} or more numbers")
    if MIN_NUMBER_OF_SPECIAL > 0:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)


def is_valid_password(password):
    """Determine if the password is valid"""
    pwd_length = len(password)
    if pwd_length < MIN_LENGTH or pwd_length > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    if (number_of_special < MIN_NUMBER_OF_SPECIAL or
            number_of_lower < MIN_NUMBER_OF_LOWER or
            number_of_upper < MIN_NUMBER_OF_UPPER or
            number_of_digit < MIN_NUMBER_OF_DIGIT):
        return False

    return True

if __name__ == "__main__":
    main()
