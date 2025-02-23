"""
CP1404/CP5632 Practical
List Exercises
"""


def main():
    """Do list exercises 1 and 2"""
    # Part 1
    numbers = get_numbers()
    print_numbers_data(numbers)

    # Part 2 Woefully inadequate security checker
    username = input("Enter username:")
    check_username(username)


def get_numbers(count=5):
    """Get specified quantity of numbers from user"""
    numbers = []
    for i in range(count):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def print_numbers_data(numbers):
    """Prints some cool data about numbers list"""
    # We don't check list length as this was not requested
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


# NOTE: Not sure if this should  be capital or not. it depends
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']


def check_username(username):
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
