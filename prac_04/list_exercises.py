"""
CP1404/CP5632 Practical
List Exercises
"""


def main():
    """Gets numbers list from user and prints some data about them"""
    numbers = get_numbers()
    print_numbers_data(numbers)


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


if __name__ == '__main__':
    main()